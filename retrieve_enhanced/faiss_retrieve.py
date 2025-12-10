# -*- coding: utf-8 -*-
"""
FAISS retriever over the FULL corpus (ignore required_corpora/filters in requests.jsonl).
Index is built once over all docs; each query searches the same index.
"""
import argparse, sys, json
from pathlib import Path
import numpy as np
import faiss

# prefer local rag_utils.py
THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
from rag_utils import *

def build_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=".", help="project root")
    ap.add_argument("--requests-jsonl", type=str, required=True)
    ap.add_argument("--spm-dir", type=str, default="spm_assets")
    ap.add_argument("--spm-prefix", type=str, default="llm_assets_bpe")
    ap.add_argument("--spm-size", type=int, default=4000)
    ap.add_argument("--spm-type", type=str, default="bpe", choices=["bpe","unigram","char","word"])
    ap.add_argument(
        "--embedding-type",
        type=str,
        default="dense",
        choices=["tfidf", "dense"],
        help="Which embedding to use for retrieval."
    )
    ap.add_argument(
        "--dense-model-name",
        type=str,
        default="BAAI/bge-base-en-v1.5",
        help="HF model name for dense embedding if --embedding-type=dense"
    )
    ap.add_argument("--enable-chunk", action="store_true", help="Enable chunking (default off)")
    ap.add_argument("--chunk-size", type=int, default=1000)
    ap.add_argument("--chunk-overlap", type=int, default=200)
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--include-context", action="store_true", help="Include full matched text in results")
    ap.add_argument("--preview-len", type=int, default=600, help="Preview length when include-context is off")
    ap.add_argument("--save-results", type=str, default="retrieve_results/retrieval_results_faiss.json")
    
    # 文本处理增强参数
    ap.add_argument("--use-semantic-chunking", action="store_true", help="Use semantic-aware chunking")
    ap.add_argument("--use-summary-context", action="store_true", help="Add document summary to chunks")
    ap.add_argument("--enable-quality-filter", action="store_true", help="Filter low-quality documents")
    ap.add_argument("--min-quality-score", type=float, default=0.3, help="Minimum quality score (0-1)")
    
    return ap.parse_args()

def build_faiss_index(xb: np.ndarray):
    d = xb.shape[1]
    index = faiss.IndexFlatIP(d)  # cosine via normalized vectors
    index.add(xb)
    return index

def search(index, q, metas, texts, topk=5, include_context=False, preview_len=600):
    D, I = index.search(q, topk)
    results = []
    for qi in range(q.shape[0]):
        hits = []
        for rank, (score, idx) in enumerate(zip(D[qi], I[qi]), start=1):
            if idx < 0:
                continue
            m = dict(metas[idx])
            hit = {
                "rank": rank,
                "score": float(score),
                **m
            }
            if include_context:
                hit["context"] = texts[idx]
            else:
                hit["preview"] = texts[idx][:max(0, preview_len)]
            hits.append(hit)
        results.append(hits)
    return results

def main():
    args = build_args()
    root = Path(args.root)

    # 1) Load full corpus
    arxiv_docs = load_arxiv(root)
    gh_docs = load_github_readmes(root)
    hf_docs = load_hf_cards(root)
    all_docs = arxiv_docs + gh_docs + hf_docs
    if not all_docs:
        print("No documents found under --root.", file=sys.stderr); sys.exit(1)
    print(f"[INFO] Loaded docs: arxiv={len(arxiv_docs)} github={len(gh_docs)} hf={len(hf_docs)} total={len(all_docs)}")

    # 2) Chunk ENTIRE corpus once (with optional text processing enhancements)
    texts, metas = prepare_chunks_all_docs(
        all_docs, 
        chunk_size=args.chunk_size, 
        chunk_overlap=args.chunk_overlap, 
        enable_chunk=args.enable_chunk,
        use_semantic_chunking=args.use_semantic_chunking,
        use_summary_context=args.use_summary_context,
        enable_quality_filter=args.enable_quality_filter,
        min_quality_score=args.min_quality_score
    )
    if not texts:
        print("No chunks/texts prepared.", file=sys.stderr); sys.exit(2)
    
    enhancement_info = []
    if args.use_semantic_chunking:
        enhancement_info.append("semantic_chunking")
    if args.use_summary_context:
        enhancement_info.append("summary_context")
    if args.enable_quality_filter:
        enhancement_info.append(f"quality_filter(>={args.min_quality_score})")
    
    enhancements = f" [{', '.join(enhancement_info)}]" if enhancement_info else ""
    print(f"[INFO] Prepared chunks: {len(texts)} (enable_chunk={args.enable_chunk}){enhancements}")

    # 3) Build embedding
    if args.embedding_type == "tfidf":
        # SentencePiece tokenizer + TF-IDF
        sp = train_or_load_sp(
            Path(args.spm_dir),
            args.spm_prefix,
            args.spm_size,
            args.spm_type,
            [t for t,_ in all_docs]
        )
        pieces_list = [sp_encode(sp, t) for t in texts]
        xb, vocab = build_tfidf(pieces_list)

    elif args.embedding_type == "dense":
        # sentence-transformers encoder
        enc_model = build_dense_encoder(args.dense_model_name)
        xb = build_dense_embeddings(enc_model, texts)
        sp = None
        vocab = None

    else:
        raise ValueError("unknown embedding_type")

    # 4) Build FAISS index once
    index = build_faiss_index(xb)

    # 5) Read requests (we ignore filters for indexing; still record them into output for reference)
    requests = read_jsonl(Path(args.requests_jsonl))
    if not requests:
        print("Empty requests.jsonl", file=sys.stderr); sys.exit(3)

    results_by_qid = {}

    for req in requests:
        qid = req.get("qid") or "QUNK"
        query = req.get("query") or ""
        if args.embedding_type == "tfidf":
            qv = embed_queries(sp, [query], vocab)
        else:
            qv = embed_queries_dense(enc_model, [query])

        k_eff = min(args.topk, index.ntotal)
        hits = search(index, qv, metas, texts,
                      topk=k_eff,
                      include_context=args.include_context,
                      preview_len=args.preview_len)[0]

        results_by_qid[qid] = {
            "qid": qid,
            "query": query,
            "answer_type": req.get("answer_type"),
            "intent": req.get("intent"),
            "filters": req.get("filters"),  # kept only for audit
            "hits": hits,
        }
        # used docs = parent docs of the hits (dedup)

        print(f"\n[FAISS][{qid}] {query}")
        print(f"  chunks_in_index={index.ntotal} topk={k_eff} hits={len(hits)}")
        for h in hits:
            src = h.get("source"); title = h.get("title") or h.get("arxiv_id") or h.get("hf_id") or ""
            info = h.get("repo") or h.get("path") or h.get("pdf_url") or ""
            print(f"  #{h['rank']} score={h['score']:.4f} [{src}] {title} (chunk {h.get('chunk_id')}) {('-> ' + info) if info else ''}")

    # 7) Save
    out_results = Path(args.save_results)
    out_results.parent.mkdir(parents=True, exist_ok=True)
    out_results.write_text(json.dumps(results_by_qid, indent=2), encoding="utf-8")
    print(f"\n[INFO] Saved FAISS hits to {out_results}")

if __name__ == "__main__":
    main()
