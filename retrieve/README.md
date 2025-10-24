# Retrieve Module

This folder implements two interchangeable retrieval backends (**FAISS** and **Qdrant**) and a shared utility library for consistent document preprocessing, chunking, and embedding.


## 🧩 Purpose

These scripts perform **retrieval-only evaluation** for pre-defined queries (`requests.jsonl`) over existing corpora under `data/`.  
Each backend produces ranked results (`Top-K` chunks) and the document list used for retrieval.

---

## ⚙️ Installation

```bash
pip install -U faiss-cpu qdrant-client sentencepiece numpy


🚀 Usage
FAISS**

Without Chunk:
python retrieve/faiss_retrieve.py \
  --root data \
  --requests-jsonl requests.jsonl \
  --topk 5 \
  --save-results retrieve_results/retrieval_results_faiss.json 

Chunk:
python retrieve/faiss_retrieve.py \
  --root data \
  --requests-jsonl requests.jsonl \
  --topk 5 \
  --save-results retrieve_results/retrieval_results_chunk_faiss.json \
  --enable-chunk \
  --chunk-size 1000 \
  --chunk-overlap 200 \
  --include-context

Qdrant (Embedded mode)**

Without Chunk:
python retrieve/qdrant_retrieve.py \
  --root data \
  --requests-jsonl requests.jsonl \
  --topk 5 \
  --save-results retrieve_results/retrieval_results_qdrant.json 

Chunk:
python retrieve/qdrant_retrieve.py \
  --root data \
  --requests-jsonl requests.jsonl \
  --topk 5 \
  --save-results retrieve_results/retrieval_results_chunk_qdrant.json \
  --enable-chunk \
  --chunk-size 1000 \
  --chunk-overlap 200 \
  --include-context

📄 Output

All results are saved under retrieve_results/.

retrieval_results_<backend>.json – ranked hits per query
