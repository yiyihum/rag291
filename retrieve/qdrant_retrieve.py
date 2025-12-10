# -*- coding: utf-8 -*-
"""
Qdrant retriever over the FULL corpus (ignore required_corpora/filters in requests.jsonl).
Builds an embedded Qdrant collection once; search each query against the same collection.
"""
import argparse, sys, json
from pathlib import Path
import numpy as np

# prefer local rag_utils.py
THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
from rag_utils import *

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct

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
    ap.add_argument("--collection", type=str, default="llm_assets_full")
    ap.add_argument("--qdrant-path", type=str, default=":memory:", help=":memory: or a folder path to persist")
    ap.add_argument("--save-results", type=str, default="retrieve_results/retrieval_results_qdrant.json")
    return ap.parse_args()

def build_qdrant_index(xb: np.ndarray, metas, collection: str, qdrant_path=":memory:"):
    client = QdrantClient(path=qdrant_path)
    d = xb.shape[1]
    client.recreate_collection(
        collection_name=collection,
        #vectors_config=VectorParams(size=d, distance=Distance.COSINE),
        #vectors_config=VectorParams(size=d, distance=Distance.DOT)，
        vectors_config=VectorParams(size=d, distance=Distance.EUCLID)
    )
    points = [
        PointStruct(id=i, vector=xb[i].tolist(), payload=metas[i])
        for i in range(xb.shape[0])
    ]
    client.upsert(collection_name=collection, points=points)
    return client

def qdrant_search(client: QdrantClient, collection: str, q, topk: int, texts, include_context=False, preview_len=600):
    qv = q[0].tolist()
    res = client.search(
        collection_name=collection,
        query_vector=qv,
        limit=topk,
        search_params={"hnsw_ef": 8}  
    )
    hits = []
    for rank, sp in enumerate(res, start=1):
        m = dict(sp.payload or {})
        hit = {
            "rank": rank,
            "score": float(sp.score),
            **m
        }
        gi = m.get("global_idx")
        if isinstance(gi, int) and 0 <= gi < len(texts):
            if include_context:
                hit["context"] = texts[gi]
            else:
                hit["preview"] = texts[gi][:max(0, preview_len)]
        hits.append(hit)
    return hits

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

    # 2) Chunk ENTIRE corpus once
    texts, metas = prepare_chunks_all_docs(all_docs, args.chunk_size, args.chunk_overlap, enable_chunk=args.enable_chunk)
    if not texts:
        print("No chunks/texts prepared.", file=sys.stderr); sys.exit(2)
    print(f"[INFO] Prepared chunks: {len(texts)} (enable_chunk={args.enable_chunk})")

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

    # 4) Build Qdrant collection once
    client = build_qdrant_index(xb, metas, args.collection, qdrant_path=args.qdrant_path)

    # 5) Read requests (only for queries; filters are ignored for indexing)
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

        k_eff = min(args.topk, len(texts))
        hits = qdrant_search(client, args.collection, qv, k_eff,
                             texts=texts,
                             include_context=args.include_context,
                             preview_len=args.preview_len)

        results_by_qid[qid] = {
            "qid": qid,
            "query": query,
            "answer_type": req.get("answer_type"),
            "intent": req.get("intent"),
            "filters": req.get("filters"),  # kept only for audit
            "hits": hits,
        }

        print(f"\n[QDRANT][{qid}] {query}")
        print(f"  chunks_in_index={len(texts)} topk={k_eff} hits={len(hits)}")
        for h in hits:
            src = h.get("source"); title = h.get("title") or h.get("arxiv_id") or h.get("hf_id") or ""
            info = h.get("repo") or h.get("path") or h.get("pdf_url") or ""
            print(f"  #{h['rank']} score={h['score']:.4f} [{src}] {title} (chunk {h.get('chunk_id')}) {('-> ' + info) if info else ''}")

    # 7) Save
    out_results = Path(args.save_results)
    out_results.parent.mkdir(parents=True, exist_ok=True)
    out_results.write_text(json.dumps(results_by_qid, indent=2), encoding="utf-8")
    print(f"\n[INFO] Saved Qdrant hits to {out_results}")

if __name__ == "__main__":
    main()
