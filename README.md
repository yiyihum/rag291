# RAG System Project

This repository contains the implementation of a Retrieval-Augmented Generation (RAG) system, including data processing, baseline retrieval methods, an enhanced RAG system, and evaluation scripts.

## Directory Structure

### 1. Data (`data/`)
Contains the raw data sources and a README with details on the dataset structure.
- **Sources**: Arxiv papers, GitHub READMEs, Hugging Face cards.
- See `data/README.md` for more details.

### 2. Evaluation (`eval/`)
Contains scripts and utilities for evaluating the RAG systems.
- **Scripts**: `evaluate.py`, `evaluate_ragas.py`, etc.
- See `eval/README.md` for usage instructions.

### 3. Baseline RAG (`rag_baseline/` & `results_baseline/`)
Implements baseline retrieval methods and stores their results.
- **rag_baseline/**: Contains baseline retrieval scripts (e.g., `faiss_retrieve.py`, `qdrant_retrieve.py`).
- **results_baseline/**: Stores the retrieval results for the baseline methods.
- *[Placeholder: Add more details about baseline performance and methodology]*

### 4. Enhanced RAG (`rag_enhanced/` & `results_enhanced/`)
A more advanced RAG system with adaptive chunking, query optimization, and agentic workflows.
- **rag_enhanced/**: Contains the enhanced RAG implementation (Data Processor, RAG System, etc.).
  - See `rag_enhanced/README.md` for detailed documentation.
- **results_enhanced/**: Stores the results for different RAG settings (Simple, Agent-Single, Agent-Loop).
  - *[To be updated: Detailed results for different enhanced settings]*

### 5. Core Files
- **`processed_data.jsonl`**: The preprocessed and cleaned dataset used by the enhanced RAG system.
- **`requests.jsonl`**: Manually constructed test set containing queries and ground truth for evaluation.

---

## Quick Start

To run the enhanced RAG system:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Request Processing**:
   ```bash
   python3 rag_enhanced/run_requests.py \
     --input requests.jsonl \
     --output responses.jsonl \
     --data-root data \
     --processed-file processed_data.jsonl \
     --embedding_type hybrid \
     --method agent-single
   ```

For more details on the Enhanced RAG system, please refer to [rag_enhanced/README.md](rag_enhanced/README.md).
