import sys
from pathlib import Path
import numpy as np
from typing import List, Dict, Any

# Add current directory to sys.path to ensure local imports work
THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from rag_utils import (
    load_arxiv, load_github_readmes, load_hf_cards,
    prepare_chunks_all_docs,
    build_dense_encoder, build_dense_embeddings, embed_queries_dense,
    train_or_load_sp, sp_encode, build_tfidf, embed_queries
)

import os
os.environ["FLAGS_logtostderr"] = "0"
os.environ["FLAGS_minloglevel"] = "3"  # 0=INFO,1=WARNING,2=ERROR,3=FATAL

class RetrievalSystem:
    """
    Retrieval system with *self-implemented* retrieval mechanisms:

    - dense vector search (cosine similarity via normalized vectors)
    - tf-idf sparse search (dot product scoring)
    - hybrid retrieval: linear fusion of dense + tf-idf scores

    embedding_type:
        "dense"  -> only dense vector search
        "tfidf"  -> only tf-idf vector search
        "hybrid" -> fusion of dense + tf-idf
    """

    def __init__(
        self,
        root_dir: str,
        processed_file: str = None,
        embedding_type: str = "dense",
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        hybrid_alpha: float = 0.5,
    ):
        self.root = Path(root_dir)
        self.processed_file = Path(processed_file) if processed_file else None
        self.embedding_type = embedding_type  # "dense", "tfidf", or "hybrid"
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.hybrid_alpha = hybrid_alpha  # weight for dense vs tf-idf in hybrid

        # Storage
        self.texts: List[str] = []
        self.metas: List[Dict[str, Any]] = []

        # Dense
        self.model = None
        self.embeddings_dense: np.ndarray | None = None  # shape: (N, d_dense)

        # TF-IDF
        self.sp = None
        self.vocab = None
        self.embeddings_tfidf: np.ndarray | None = None  # shape: (N, d_sparse)

        self._build_index()

    # ---------- Utilities ----------

    @staticmethod
    def _l2_normalize(x: np.ndarray, axis: int = 1, eps: float = 1e-9) -> np.ndarray:
        """Row-wise L2 normalization for cosine similarity."""
        norm = np.linalg.norm(x, axis=axis, keepdims=True)
        norm = np.maximum(norm, eps)
        return x / norm

    @staticmethod
    def _normalize_scores(scores: np.ndarray) -> np.ndarray:
        """Min-max normalize scores to [0,1] to allow fusion."""
        s_min = scores.min()
        s_max = scores.max()
        if s_max <= s_min:
            return np.zeros_like(scores)
        return (scores - s_min) / (s_max - s_min)

    # ---------- Index building (embeddings only, no FAISS) ----------

    def _build_index(self):
        import json

        # 1) Load texts + metas
        if self.processed_file and self.processed_file.exists():
            print(f"[INFO] Loading pre-processed data from {self.processed_file}...")
            with open(self.processed_file, "r") as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        d = json.loads(line)
                        # Prioritize 'content' as it contains the enriched text for RAG
                        text = d.get("content") or d.get("text")
                        if text:
                            self.texts.append(text)
                            # Store the FULL document object as metadata to preserve all fields
                            self.metas.append(d)
                    except Exception:
                        pass
            print(f"[INFO] Loaded {len(self.texts)} chunks from processed file.")
        else:
            print("[INFO] Loading documents from source directories...")
            arxiv_docs = load_arxiv(self.root)
            gh_docs = load_github_readmes(self.root)
            hf_docs = load_hf_cards(self.root)
            all_docs = arxiv_docs + gh_docs + hf_docs

            if not all_docs:
                print("[WARN] No documents found.")
                return

            print(f"[INFO] Loaded {len(all_docs)} documents. Preparing chunks...")
            self.texts, self.metas = prepare_chunks_all_docs(
                all_docs,
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
            )

        if not self.texts:
            print("[WARN] No chunks created/loaded.")
            return

        print(
            f"[INFO] Building embeddings ({self.embedding_type}) "
            f"for {len(self.texts)} chunks..."
        )

        # Depending on embedding_type, build dense / tfidf / both
        need_dense = self.embedding_type in ("dense", "hybrid")
        need_tfidf = self.embedding_type in ("tfidf", "hybrid")

        if need_dense:
            print("[INFO] Building dense (neural) embeddings...")
            self.model = build_dense_encoder()
            xb_dense = build_dense_embeddings(self.model, self.texts).astype(np.float32)
            # cosine similarity via normalized vectors
            self.embeddings_dense = self._l2_normalize(xb_dense, axis=1)

        if need_tfidf:
            print("[INFO] Building TF-IDF embeddings...")
            self.sp = train_or_load_sp(
                self.root / "spm_assets",
                "llm_assets_bpe",
                4000,
                "bpe",
                self.texts,
            )
            pieces_list = [sp_encode(self.sp, t) for t in self.texts]
            xb_tfidf, self.vocab = build_tfidf(pieces_list)
            # ensure numpy array
            if hasattr(xb_tfidf, "toarray"):
                xb_tfidf = xb_tfidf.toarray()
            self.embeddings_tfidf = xb_tfidf.astype(np.float32)

        print("[INFO] Embeddings built successfully.")

    # ---------- Core retrieval mechanisms (self-implemented) ----------

    def _search_dense(self, q_vec: np.ndarray, top_k: int) -> np.ndarray:
        """
        Dense vector search via cosine similarity:
            scores = q ⋅ x   (both normalized)
        q_vec: shape (d,)
        returns: indices of top_k docs (sorted by score desc)
        """
        if self.embeddings_dense is None:
            return np.array([], dtype=int)

        # ensure normalized
        q_vec = q_vec.astype(np.float32)
        q_vec = q_vec / (np.linalg.norm(q_vec) + 1e-9)

        # scores shape: (N,)
        scores = self.embeddings_dense @ q_vec  # cosine similarity
        # top_k indices
        k = min(top_k, scores.shape[0])
        if k <= 0:
            return np.array([], dtype=int)
        top_idx = np.argpartition(-scores, k - 1)[:k]
        # sort by score desc
        top_idx = top_idx[np.argsort(-scores[top_idx])]
        return top_idx, scores

    def _search_tfidf(self, q_vec: np.ndarray, top_k: int) -> np.ndarray:
        """
        Sparse vector search (TF-IDF) via dot product:
            scores = q ⋅ x
        q_vec: shape (d,)
        returns: indices of top_k docs (sorted by score desc)
        """
        if self.embeddings_tfidf is None:
            return np.array([], dtype=int)

        q_vec = q_vec.astype(np.float32)
        scores = self.embeddings_tfidf @ q_vec  # shape: (N,)
        k = min(top_k, scores.shape[0])
        if k <= 0:
            return np.array([], dtype=int)
        top_idx = np.argpartition(-scores, k - 1)[:k]
        top_idx = top_idx[np.argsort(-scores[top_idx])]
        return top_idx, scores

    def _search_hybrid(self, q_dense: np.ndarray, q_tfidf: np.ndarray, top_k: int):
        """
        Hybrid retrieval:
            score = alpha * dense_score_norm + (1 - alpha) * tfidf_score_norm
        """
        dense_idx, dense_scores = self._search_dense(q_dense, top_k=top_k * 5)
        tfidf_idx, tfidf_scores = self._search_tfidf(q_tfidf, top_k=top_k * 5)

        # unify candidate set
        N = len(self.texts)
        final_scores = np.zeros(N, dtype=np.float32)
        used = np.zeros(N, dtype=bool)

        # normalize scores separately
        if dense_scores.size > 0:
            dense_norm = self._normalize_scores(dense_scores)
            for idx in dense_idx:
                final_scores[idx] += self.hybrid_alpha * dense_norm[idx]
                used[idx] = True

        if tfidf_scores.size > 0:
            tfidf_norm = self._normalize_scores(tfidf_scores)
            for idx in tfidf_idx:
                final_scores[idx] += (1.0 - self.hybrid_alpha) * tfidf_norm[idx]
                used[idx] = True

        cand_idx = np.where(used)[0]
        if cand_idx.size == 0:
            return np.array([], dtype=int), final_scores

        k = min(top_k, cand_idx.size)
        top_cand = np.argpartition(-final_scores[cand_idx], k - 1)[:k]
        top_idx = cand_idx[top_cand]
        top_idx = top_idx[np.argsort(-final_scores[top_idx])]
        return top_idx, final_scores

    # ---------- Public API ----------

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Retrieve documents based on query.
        Filters are ignored in this version.

        Retrieval mechanism controlled by self.embedding_type:
            - "dense"  -> pure vector search (cosine)
            - "tfidf"  -> tf-idf search (dot product)
            - "hybrid" -> fusion of the above
        """
        if not self.texts:
            return []

        # 1) Embed query
        q_dense = None
        q_tfidf = None

        if self.embedding_type in ("dense", "hybrid"):
            q_dense = embed_queries_dense(self.model, [query]).astype(np.float32)[0]

        if self.embedding_type in ("tfidf", "hybrid"):
            q_tfidf = embed_queries(self.sp, [query], self.vocab).astype(np.float32)[0]

        # 2) Run retrieval
        if self.embedding_type == "dense":
            cand_idx, scores = self._search_dense(q_dense, top_k=top_k)
        elif self.embedding_type == "tfidf":
            cand_idx, scores = self._search_tfidf(q_tfidf, top_k=top_k)
        else:  # "hybrid"
            cand_idx, scores = self._search_hybrid(
                q_dense, q_tfidf, top_k=top_k
            )

        hits: List[Dict[str, Any]] = []
        if cand_idx.size == 0:
            return hits

        # 3) Construct hits
        for idx in cand_idx:
            meta = self.metas[idx]
            text = self.texts[idx]
            score = float(scores[idx])

            # Resolve actual metadata dictionary
            # If loaded from processed_data.jsonl, meta is the full doc 'd', so real metadata is in d['metadata']
            # If loaded from raw files, meta is already the metadata dict
            real_meta = meta.get("metadata", meta)

            hits.append(
                {
                    "score": score,
                    "content": text,
                    "metadata": real_meta,
                    "raw_content": meta.get("raw_content") if isinstance(meta, dict) else None,
                }
            )

        # sort final hits by score desc
        hits = sorted(hits, key=lambda x: x["score"], reverse=True)

        return hits
