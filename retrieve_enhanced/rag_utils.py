# -*- coding: utf-8 -*-
import json, glob, re, math
from pathlib import Path
from collections import Counter
from datetime import datetime
from typing import List, Tuple, Dict, Any, Optional
import numpy as np
import sentencepiece as spm
from sentence_transformers import SentenceTransformer
import torch

# 导入文本处理模块
try:
    from text_processing import (
        clean_text,
        calculate_text_quality_score,
        filter_low_quality_docs,
        generate_extractive_summary,
        extract_keywords,
        semantic_chunking,
        chunk_by_markdown_headers,
        enrich_chunk_with_summary,
        add_metadata_context,
    )
    TEXT_PROCESSING_AVAILABLE = True
except ImportError:
    TEXT_PROCESSING_AVAILABLE = False
    print("[WARNING] text_processing module not available. Advanced features disabled.")

# ---------- IO ----------
def read_jsonl(path: Path):
    out = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out

def read_text_file(path: Path):
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def safe_glob(patterns):
    files = []
    for p in patterns:
        files.extend(glob.glob(p, recursive=True))
    return sorted(set(files))

# ---------- Chunking ----------
def chunk_text(text: str, chunk_size=1000, overlap=200):
    if chunk_size <= 0:
        return [text]
    overlap = max(0, min(overlap, chunk_size - 1))
    chunks = []
    i, n = 0, len(text)
    while i < n:
        j = min(i + chunk_size, n)
        chunks.append(text[i:j])
        if j == n:
            break
        i = j - overlap
    return chunks

MD_H_RE = re.compile(r"^\s{0,3}(#+)\s*(.+?)\s*$", re.M)
def extract_md_section(md_text: str, section_name: str):
    titles = [(m.start(), m.end(), len(m.group(1)), m.group(2).strip())
              for m in MD_H_RE.finditer(md_text)]
    if not titles:
        return md_text
    target_idx = -1
    lower_target = section_name.lower()
    for i, (_, _, _, t) in enumerate(titles):
        if lower_target in t.lower():
            target_idx = i
            break
    if target_idx < 0:
        return md_text
    start = titles[target_idx][0]
    cur_level = titles[target_idx][2]
    end = len(md_text)
    for j in range(target_idx + 1, len(titles)):
        if titles[j][2] <= cur_level:
            end = titles[j][0]
            break
    return md_text[start:end].strip()

# ---------- Corpora loaders ----------
def _s(v):
    if v is None:
        return ""
    if isinstance(v, str):
        return v.strip()
    return str(v).strip()

def _join_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return v
    if isinstance(v, str):
        return [t.strip() for t in re.split(r"[;,]", v) if t.strip()]
    return [str(v)]

def load_arxiv(root: Path, enable_cleaning: bool = True):
    p = root / "arxiv_llm_2025" / "arxiv_llm_2025.jsonl"
    if not p.exists():
        return []
    rows = read_jsonl(p)
    docs = []
    for r in rows:
        title = _s(r.get("title"))
        abstract = _s(r.get("abstract"))
        comment = _s(r.get("comment"))
        jr = _s(r.get("journal_ref"))
        text = "\n".join([title, abstract, comment, jr]).strip()
        
        # 文本清洗
        if enable_cleaning and TEXT_PROCESSING_AVAILABLE:
            text = clean_text(text)
        
        meta = {
            "source": "arxiv",
            "arxiv_id": _s(r.get("id")),
            "title": title,
            "primary_category": _s(r.get("primary_category")),
            "categories": _join_list(r.get("categories")),
            "authors": _join_list(r.get("authors")),
            "year": r.get("year"),
            "pdf_url": _s(r.get("pdf_url")),
            "link": _s(r.get("link")),
        }
        docs.append((text, meta))
    return docs

def load_github_readmes(root: Path, enable_cleaning: bool = True):
    base = root / "github_readmes"
    if not base.exists():
        return []
    files = safe_glob([str(base / "**" / "README*")])
    out = []
    for f in files:
        p = Path(f)
        txt = read_text_file(p)
        
        # 文本清洗
        if enable_cleaning and TEXT_PROCESSING_AVAILABLE:
            txt = clean_text(txt)
        
        parts = p.parts
        repo = "/".join(parts[-3:-1]) if len(parts) >= 3 else ""
        meta = {"source": "github", "repo": repo, "title": p.name, "path": str(p)}
        out.append((txt, meta))
    return out

def load_hf_cards(root: Path):
    base = root / "hf_cards_2025"
    out = []
    mani_models = read_jsonl(base / "manifest_models.jsonl") if (base / "manifest_models.jsonl").exists() else []
    mani_dsets = read_jsonl(base / "manifest_datasets.jsonl") if (base / "manifest_datasets.jsonl").exists() else []
    m_models = {row.get("id"): row for row in mani_models}
    m_dsets = {row.get("id"): row for row in mani_dsets}
    for sub, kind, manifest_map in [
        (base / "models", "hf_model_card", m_models),
        (base / "datasets", "hf_dataset_card", m_dsets),
    ]:
        if not sub.exists():
            continue
        files = safe_glob([str(sub / "*.md")])
        for f in files:
            p = Path(f)
            stem = p.stem
            hf_id = stem.replace("__", "/")
            txt = read_text_file(p)
            meta = {"source": kind, "path": str(p), "title": p.name, "hf_id": hf_id}
            mani = manifest_map.get(hf_id)
            if mani:
                meta.update({
                    "created_at": mani.get("created_at"),
                    "last_modified": mani.get("last_modified"),
                    "downloads": mani.get("downloads"),
                    "likes": mani.get("likes"),
                    "license": mani.get("license"),
                    "pipeline_tag": mani.get("pipeline_tag"),
                    "tags": mani.get("tags"),
                    "author": mani.get("author"),
                })
            out.append((txt, meta))
    return out

# ---------- Global chunk preparation ----------
def prepare_chunks_all_docs(all_docs, chunk_size=1000, chunk_overlap=200, enable_chunk=True, 
                           use_semantic_chunking=False, use_summary_context=False,
                           enable_quality_filter=False, min_quality_score=0.3):
    """
    Build chunks over the ENTIRE corpus (ignore required_corpora/filters).
    Return (texts, metas).
    Each meta carries chunk_id (per-doc), char_start/end, global_idx, etc.
    
    New parameters:
    - use_semantic_chunking: Use semantic-aware chunking instead of fixed-size
    - use_summary_context: Add document summary to each chunk
    - enable_quality_filter: Filter low-quality documents
    - min_quality_score: Minimum quality score threshold
    """
    # 质量过滤
    if enable_quality_filter and TEXT_PROCESSING_AVAILABLE:
        print(f"[INFO] Filtering documents with quality score >= {min_quality_score}")
        all_docs = filter_low_quality_docs(all_docs, min_score=min_quality_score)
        print(f"[INFO] Kept {len(all_docs)} documents after quality filtering")
    
    texts, metas = [], []
    global_idx = 0
    
    for text, meta in all_docs:
        # 生成文档级摘要 (如果需要)
        doc_summary = ""
        if use_summary_context and TEXT_PROCESSING_AVAILABLE:
            # 优先使用已有的 abstract
            if meta.get('abstract'):
                doc_summary = meta['abstract'][:200]
            else:
                doc_summary = generate_extractive_summary(text, max_sentences=2)
            meta['doc_summary'] = doc_summary
        
        if not enable_chunk:
            # 不分块，保存整个文档
            m = dict(meta)
            m.update({
                "chunk_id": 0,
                "char_len": len(text),
                "char_start": 0,
                "char_end": len(text),
                "chunk_size": -1,
                "chunk_overlap": 0,
                "global_idx": global_idx,
            })
            
            # 添加摘要上下文
            final_text = text
            if use_summary_context and doc_summary:
                final_text = enrich_chunk_with_summary(text, doc_summary)
            
            texts.append(final_text)
            metas.append(m)
            global_idx += 1
            continue

        # 使用语义分块
        if use_semantic_chunking and TEXT_PROCESSING_AVAILABLE:
            # 根据文档类型选择分块策略
            if meta.get('source') == 'github' and 'README' in meta.get('title', ''):
                chunks = chunk_by_markdown_headers(text, max_chunk_size=chunk_size)
            else:
                chunks = semantic_chunking(text, max_chunk_size=chunk_size, overlap=chunk_overlap)
            
            for chunk_info in chunks:
                ch = chunk_info['text']
                if not ch.strip():
                    continue
                
                m = dict(meta)
                m.update({
                    "chunk_id": chunk_info['chunk_id'],
                    "char_len": chunk_info['size'],
                    "char_start": 0,  # semantic chunking doesn't track exact positions
                    "char_end": chunk_info['size'],
                    "chunk_size": chunk_size,
                    "chunk_overlap": chunk_overlap,
                    "chunk_type": chunk_info['type'],
                    "global_idx": global_idx,
                })
                
                # 添加 section 信息 (如果有)
                if 'section_title' in chunk_info:
                    m['section_title'] = chunk_info['section_title']
                    m['section_level'] = chunk_info['section_level']
                
                # 添加摘要上下文
                final_text = ch
                if use_summary_context and doc_summary:
                    final_text = enrich_chunk_with_summary(ch, doc_summary)
                
                texts.append(final_text)
                metas.append(m)
                global_idx += 1
        else:
            # 使用固定大小分块 (原始逻辑)
            overlap = max(0, min(chunk_overlap, chunk_size - 1))
            i, n, doc_chunk_idx = 0, len(text), 0
            while i < n:
                j = min(i + chunk_size, n)
                ch = text[i:j]
                if ch.strip():
                    m = dict(meta)
                    m.update({
                        "chunk_id": doc_chunk_idx,
                        "char_len": len(ch),
                        "char_start": i,
                        "char_end": j,
                        "chunk_size": chunk_size,
                        "chunk_overlap": chunk_overlap,
                        "global_idx": global_idx,
                    })
                    
                    # 添加摘要上下文
                    final_text = ch
                    if use_summary_context and doc_summary:
                        final_text = enrich_chunk_with_summary(ch, doc_summary)
                    
                    texts.append(final_text)
                    metas.append(m)
                    global_idx += 1
                    doc_chunk_idx += 1
                if j == n:
                    break
                i = j - overlap
    
    return texts, metas

# ---------- SPM + TF-IDF ----------
def train_or_load_sp(spm_dir: Path, prefix: str, spm_size: int, spm_type: str, corpus_samples):
    spm_dir.mkdir(parents=True, exist_ok=True)
    model_path = spm_dir / f"{prefix}.model"
    if not model_path.exists():
        train_txt = spm_dir / "train_corpus.txt"
        total, lines, limit = 0, [], 50_000_000
        for t in corpus_samples:
            if not t:
                continue
            lines.append(t)
            total += len(t)
            if total >= limit:
                break
        train_txt.write_text("\n".join(lines), encoding="utf-8")
        spm.SentencePieceTrainer.Train(
            input=str(train_txt),
            model_prefix=str(spm_dir / prefix),
            vocab_size=int(spm_size),
            model_type=spm_type,
            character_coverage=1.0,
            input_sentence_size=2_000_000,
            shuffle_input_sentence=True,
            normalization_rule_name="nmt_nfkc",
        )
    sp = spm.SentencePieceProcessor()
    sp.load(str(model_path))
    return sp

def sp_encode(sp, text):
    return sp.encode(text, out_type=str)

def build_tfidf(pieces_list):
    df = Counter()
    for pcs in pieces_list:
        df.update(set(pcs))
    vocab = {tok: i for i, tok in enumerate(sorted(df.keys()))}
    N = len(pieces_list)
    D = len(vocab)
    X = np.zeros((N, D), dtype=np.float32)
    for i, pcs in enumerate(pieces_list):
        tf = Counter(pcs)
        for t, c in tf.items():
            j = vocab.get(t)
            if j is None:
                continue
            idf = math.log((1 + N) / (1 + df[t])) + 1.0
            X[i, j] = float(c) * idf
    X /= (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)
    return X.astype(np.float32), vocab

def embed_queries(sp, queries, vocab):
    Q = np.zeros((len(queries), len(vocab)), dtype=np.float32)
    for i, q in enumerate(queries):
        pcs = sp_encode(sp, q)
        tf = Counter(pcs)
        for t, c in tf.items():
            j = vocab.get(t)
            if j is not None:
                Q[i, j] = float(c)
    Q /= (np.linalg.norm(Q, axis=1, keepdims=True) + 1e-12)
    return Q.astype(np.float32)


def build_dense_encoder(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Load a sentence-transformers embedding model.
    Returns the model object.
    """
    if SentenceTransformer is None:
        raise RuntimeError(
            "sentence-transformers not installed. pip install sentence-transformers"
        )
    model = SentenceTransformer(model_name, device="cuda" if torch.cuda.is_available() else "cpu")
    return model

def build_dense_embeddings(model, texts, normalize=True):
    """
    Encode a list of strings -> np.ndarray [N, dim]
    Optionally L2-normalize the rows.
    """
    import numpy as np
    embs = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=False, 
    )
    if normalize:
        norms = np.linalg.norm(embs, axis=1, keepdims=True) + 1e-12
        embs = embs / norms
    return embs.astype(np.float32)

def embed_queries_dense(model, queries, normalize=True):
    """
    Same as build_dense_embeddings but for queries (list of str).
    Returns shape [len(queries), dim]
    """
    import numpy as np
    qembs = model.encode(
        queries,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=False,
    )
    if normalize:
        norms = np.linalg.norm(qembs, axis=1, keepdims=True) + 1e-12
        qembs = qembs / norms
    return qembs.astype(np.float32)


# ---------- Helpers ----------
def dedup_by_parent(hits):
    """Dedup top hits to parent docs by ('source','path','arxiv_id','hf_id','repo')."""
    seen, out = set(), []
    for h in hits:
        key = (h.get("source"), h.get("path"), h.get("arxiv_id"), h.get("hf_id"), h.get("repo"))
        if key in seen:
            continue
        seen.add(key); out.append({k: h.get(k) for k in ["source","path","title","arxiv_id","hf_id","repo"] if k in h})
    return out
