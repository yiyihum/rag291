import sys
from pathlib import Path
import faiss
import numpy as np
from typing import List, Dict, Any, Optional

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

class RetrievalSystem:
    def __init__(self, root_dir: str, processed_file: str = None, embedding_type: str = "dense", chunk_size: int = 1000, chunk_overlap: int = 200):
        self.root = Path(root_dir)
        self.processed_file = Path(processed_file) if processed_file else None
        self.embedding_type = embedding_type
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        self.index = None
        self.texts = []
        self.metas = []
        self.model = None # For dense
        self.sp = None    # For tfidf
        self.vocab = None # For tfidf
        
        self._build_index()

    def _build_index(self):
        import json
        
        if self.processed_file and self.processed_file.exists():
            print(f"[INFO] Loading pre-processed data from {self.processed_file}...")
            with open(self.processed_file, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        d = json.loads(line)
                        self.texts.append(d['text'])
                        self.metas.append(d['metadata'])
                    except Exception as e:
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
                chunk_overlap=self.chunk_overlap
            )
        
        if not self.texts:
            print("[WARN] No chunks created/loaded.")
            return

        print(f"[INFO] Building {self.embedding_type} embeddings for {len(self.texts)} chunks...")
        if self.embedding_type == "dense":
            self.model = build_dense_encoder()
            xb = build_dense_embeddings(self.model, self.texts)
        else:
            # TF-IDF
            # Note: For TF-IDF we might need original docs for training SP, 
            # but if we load from processed, we might not have them easily.
            # For now assuming dense is primary or SP assets exist.
            self.sp = train_or_load_sp(
                self.root / "spm_assets", "llm_assets_bpe", 4000, "bpe", self.texts
            )
            pieces_list = [sp_encode(self.sp, t) for t in self.texts]
            xb, self.vocab = build_tfidf(pieces_list)
            
        print("[INFO] Building FAISS index...")
        d = xb.shape[1]
        self.index = faiss.IndexFlatIP(d)
        self.index.add(xb)
        print("[INFO] Index built successfully.")

    def retrieve(self, query: str, sources: List[str] = None, filters: Dict[str, Any] = None, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve documents based on query, optional source filtering, and metadata filters.
        sources: list of strings, e.g. ['arxiv', 'github', 'hf_model_card', 'hf_dataset_card']
        filters: dict of metadata key-value pairs to match.
        """
        if not self.index:
            return []

        # Embed query
        if self.embedding_type == "dense":
            qv = embed_queries_dense(self.model, [query])
        else:
            qv = embed_queries(self.sp, [query], self.vocab)
            
        # Search with larger k to allow for filtering
        search_k = top_k * 10 if (sources or filters) else top_k
        search_k = min(search_k, self.index.ntotal)
        
        D, I = self.index.search(qv, search_k)
        
        hits = []
        for rank, (score, idx) in enumerate(zip(D[0], I[0]), start=1):
            if idx < 0: continue
            
            meta = self.metas[idx]
            text = self.texts[idx]
            
            # 1. Filter by source
            if sources:
                src = meta.get('source', '')
                allowed = False
                for s in sources:
                    if s == src:
                        allowed = True
                        break
                    if s == 'hf' and 'hf_' in src: # 'hf' matches 'hf_model_card' and 'hf_dataset_card'
                        allowed = True
                        break
                if not allowed:
                    continue

            # 2. Filter by metadata (exact match or containment)
            if filters:
                match = True
                for k, v in filters.items():
                    # Special handling for IDs which might be in title/path
                    if k in ['dataset_id', 'model_id', 'repo', 'arxiv_id']:
                        # Check if value is contained in title, path, or specific field
                        val_str = str(v).lower()
                        meta_vals = [
                            str(meta.get('title', '')).lower(),
                            str(meta.get('path', '')).lower(),
                            str(meta.get('repo', '')).lower(),
                            str(meta.get('id', '')).lower()
                        ]
                        if not any(val_str in mv for mv in meta_vals):
                            match = False
                            break
                    else:
                        # General metadata match (e.g. year)
                        # Check if key exists in meta and values match
                        # Note: meta keys might not match filter keys exactly, so this is best-effort
                        if k in meta and str(meta[k]) != str(v):
                            match = False
                            break
                if not match:
                    continue
            
            hits.append({
                "score": float(score),
                "content": text,
                "metadata": meta
            })
            
            if len(hits) >= top_k:
                break
                
        return hits
