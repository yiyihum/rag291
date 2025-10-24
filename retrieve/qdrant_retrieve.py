# -*- coding: utf-8 -*-
"""
Qdrant retriever (embedded, no external server) over your assets.
"""
import argparse, sys, json
from pathlib import Path
import numpy as np


THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
from rag_utils import *   

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct

def build_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=".", help="project root")
    ap.add_argument("--enable-chunk", action="store_true", help="Enable chunking (default off)")
    ap.add_argument("--requests-jsonl", type=str, required=True)
    ap.add_argument("--spm-dir", type=str, default="spm_assets")
    ap.add_argument("--spm-prefix", type=str, default="llm_assets_bpe")
    ap.add_argument("--spm-size", type=int, default=4000)
    ap.add_argument("--spm-type", type=str, default="bpe", choices=["bpe","unigram","char","word"])
    ap.add_argument("--chunk-size", type=int, default=1000)
    ap.add_argument("--chunk-overlap", type=int, default=200)
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--collection", type=str, default="llm_assets_demo")
    ap.add_argument("--save-results", type=str, default="retrieve_results/retrieval_results_qdrant.json")
    ap.add_argument("--include-context", action="store_true",
                    help="Write matched chunk text into results (default off)")
    ap.add_argument("--preview-len", type=int, default=600,
                    help="If include-context is off, include a short preview of this length")
    return ap.parse_args()

def build_qdrant_index(xb: np.ndarray, metas, collection: str):
    client = QdrantClient(path=":memory:")  
    d = xb.shape[1]
    client.recreate_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=d, distance=Distance.COSINE),
    )
    points = [
        PointStruct(id=i, vector=xb[i].tolist(), payload=metas[i])
        for i in range(xb.shape[0])
    ]
    client.upsert(collection_name=collection, points=points)
    return client

def qdrant_search(client, collection: str, q, topk: int, texts, include_context=False, preview_len=600):
    qv = q[0].tolist()
    res = client.search(collection_name=collection, query_vector=qv, limit=topk)
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

    # Load corpora
    arxiv_docs = load_arxiv(root)
    gh_docs = load_github_readmes(root)
    hf_docs = load_hf_cards(root)
    all_docs = arxiv_docs + gh_docs + hf_docs
    if not all_docs:
        print("No documents found under --root.", file=sys.stderr); sys.exit(1)

    # Requests
    requests = read_jsonl(Path(args.requests_jsonl))
    if not requests:
        print("Empty requests.jsonl", file=sys.stderr); sys.exit(2)

    # Train SPM
    sp = train_or_load_sp(Path(args.spm_dir), args.spm_prefix, args.spm_size, args.spm_type, [t for t,_ in all_docs])

    results_by_qid = {}

    for req in requests:
        qid = req.get("qid") or "QUNK"
        query = req.get("query") or ""

        texts, metas, _ = prepare_chunks_for_request(all_docs, req,
                                           chunk_size=args.chunk_size,
                                           chunk_overlap=args.chunk_overlap,
                                           enable_chunk=args.enable_chunk)
        if not texts:
            results_by_qid[qid] = {"qid": qid, "query": query, "hits": [], "note": "no docs matched filters"}
            continue

        pieces_list = [sp_encode(sp, t) for t in texts]
        xb, vocab = build_tfidf(pieces_list)
        qv = embed_queries(sp, [query], vocab)

        client = build_qdrant_index(xb, metas, args.collection)
        hits = qdrant_search(client, args.collection, qv, args.topk,
                     texts=texts,
                     include_context=args.include_context,
                     preview_len=args.preview_len)

        results_by_qid[qid] = {
            "qid": qid,
            "query": query,
            "answer_type": req.get("answer_type"),
            "intent": req.get("intent"),
            "filters": req.get("filters"),
            "hits": hits,
        }

        print(f"\n[QDRANT][{qid}] {query}")
        for h in hits:
            src = h.get("source"); title = h.get("title") or h.get("arxiv_id") or h.get("hf_id") or ""
            info = h.get("repo") or h.get("path") or h.get("pdf_url") or ""
            print(f"  #{h['rank']} score={h['score']:.4f} [{src}] {title} (chunk {h.get('chunk_id')}) {('-> ' + info) if info else ''}")

    out_results = Path(args.save_results)
    out_results.parent.mkdir(parents=True, exist_ok=True)

    out_results.write_text(json.dumps(results_by_qid, indent=2), encoding="utf-8")
    print(f"\n[INFO] Saved Qdrant hits to {args.save_results}")

if __name__ == "__main__":
    main()
