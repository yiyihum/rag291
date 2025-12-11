# Enhanced RAG System

This project implements an enhanced Retrieval-Augmented Generation (RAG) system divided into three main components: Data Preprocessing, Retrieval, and RAG System.

## Project Structure

- `data_processor.py`: Handles data cleaning, keyword extraction (LLM-based), and summarization.
- `retrieval_system.py`: Manages document indexing and retrieval with source filtering.
- `rag_system.py`: Implements 4 different RAG modes and a reranking module.
- `llm_client.py`: Interface for LLM interactions (Mock and OpenAI).
- `rag_utils.py`: Utility functions for loading data and text processing.

## 1. Data Preprocessing

The `DataProcessor` class in `data_processor.py` has been refined to handle specific data sources (Arxiv, GitHub, Hugging Face) and implements adaptive chunking.

**Features:**
- **Multi-source Support**: Automatically processes `arxiv_llm_2025`, `github_readmes`, and `hf_cards_2025`.
- **Adaptive Chunking**:
    - **Arxiv**: Semantic chunking.
    - **GitHub**: Markdown header-based chunking.
    - **Hugging Face**: Semantic chunking.
    - **No Chunking**: Option to treat full document as a single chunk (`--no-chunk`).
- **Parallel Processing**: Uses multi-threading to speed up LLM calls (`--workers`).
- **Robustness**:
    - **Batch Saving**: Saves progress every N items (`--batch-size`) to prevent data loss.
    - **Resume Capability**: Automatically skips already processed documents (based on source + path/title).
    - **Rate Limit Handling**: Automatically retries for transient errors and exits gracefully for daily limits.
- **Quality Filtering**: Filters low-quality documents (e.g., code-heavy READMEs).
- **Enrichment**: Adds metadata and summaries to chunks.
- **Cleaning**: Hybrid cleaning (heuristic + optional LLM).


**Command Line:**
```bash
python3 rag_enhanced/data_processor.py \
  --data-root data \
  --output processed_data_1000.jsonl \
  --clean \
  --summary \
  --chunk-size 1000 \
  --workers 10
```

**Parameters Used:**
- `--clean`: Enables text cleaning (removing noise).
- `--summary`: Generates summaries for documents using LLM.
- `--chunk-size 100000`: Effectively disables chunking by setting a very large size, keeping documents intact as requested.
- `--workers 5`: Uses 5 parallel workers for faster processing. \
  --no-chunk  # Optional: Disable chunking

## 2. Retrieval

The `RetrievalSystem` class in `retrieval_system.py` handles efficient document retrieval.

**Features:**
- **Hybrid Retrieval**: Supports Dense (Sentence Transformers) or Sparse (TF-IDF) embeddings.
- **Source Filtering**: Filter results by source (e.g., 'arxiv', 'github', 'hf').
- **Top-N Control**: Retrieve exact number of top results.

**Usage:**
```python
from retrieval_system import RetrievalSystem

retriever = RetrievalSystem(root_dir="./data", embedding_type="dense")
hits = retriever.retrieve("query", sources=['arxiv'], top_k=5)
```

## 3. RAG System

The `RAGSystem` class in `rag_system.py` provides advanced question-answering capabilities.

**Features:**
- **Reranking**: Uses `CrossEncoder` to re-score retrieved documents for better relevance.
### RAG Modes

The system supports 3 different RAG strategies, selectable via the `--method` argument:

1.  **Simple RAG (`simple`)**
    -   **Mechanism**: Directly retrieves documents using the user's query, reranks them, and generates an answer.
    -   **Pros**: Fast, low latency, cheap (fewer LLM calls).
    -   **Cons**: Struggles with complex queries or vocabulary mismatch between query and documents.

2.  **Agent Single-turn (`agent-single`)**
    -   **Mechanism**: Uses an LLM to rewrite the user's query into a better search query before retrieval.
    -   **Pros**: improved retrieval quality for vague or poorly phrased questions.
    -   **Cons**: Adds one LLM call latency.

3.  **Agent Multi-turn Loop (`agent-loop`)**
    -   **Mechanism**: Iterative "Reasoning Loop". Retrieves -> Evaluates if info is sufficient -> If NO, generates a new query and repeats (max 3 turns).
    -   **Pros**: Best for complex research tasks requiring deep exploration.
    -   **Cons**: Slowest and most expensive mode.

**Usage:**
```python
from rag_system import RAGSystem
from llm_client import get_llm_client

llm = get_llm_client() # Defaults to OpenRouter
rag = RAGSystem(retriever, llm)

# Process a single query with a specific method
answer, docs = rag.answer_agent_single("Compare RAG vs Fine-tuning")
```

## 4. Request Processing

To evaluate the system on the provided dataset:

**Script:** `run_requests.py`

**Goal:** Process `/Users/yimih/Documents/ucsd/rag291/requests.jsonl` and generate `responses.jsonl`.

**Features:**
- **Flexible RAG Methods**: Supports 3 modes via `--method` (`simple`, `agent-single`, `agent-loop`).
- **Full Search**: Searches all available corpora (Arxiv, GitHub, HuggingFace) for every query to maximize recall.
- **Comprehensive Output**: Saves both the generated answer (`llm_response`) and the retrieved evidence (`retrieve_results`) for evaluation.

**Parameters:**

- `--input`: Path to the input `requests.jsonl` file containing queries.
- `--output-dir`: Directory where the results will be saved. The filename is automatically generated based on the method and settings.
- `--data-root`: Root directory containing the raw data folders (`arxiv`, `github_readmes`, `hf_cards`).
- `--processed-file`: (Optional) Path to the pre-processed data file (e.g., `processed_data.jsonl`). Using this significantly speeds up initialization by skipping raw data loading and chunking.
- `--embedding_type`: Retrieval embedding strategy.
    - `dense`: Uses semantic embeddings only.
    - `hybrid`: Combines dense embeddings with sparse (BM25/TF-IDF) keyword matching.
- `--method`: The RAG strategy to employ.
    - `simple`: Direct retrieval and generation.
    - `agent-single`: Query rewriting before retrieval.
    - `agent-loop`: Multi-turn reasoning loop.

## 5. Run All Combinations

Here is a comprehensive list of commands to run all supported configurations.

### Using Pre-processed Data (Recommended)

**Simple RAG**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type dense --method simple

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type hybrid --method simple
```

**Agent Single-turn**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type dense --method agent-single

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type hybrid --method agent-single
```

**Agent Multi-turn Loop**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type dense --method agent-loop

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --processed-file processed_data.jsonl --embedding_type hybrid --method agent-loop
```

### Using Raw Data

**Simple RAG**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type dense --method simple

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type hybrid --method simple
```

**Agent Single-turn**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type dense --method agent-single

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type hybrid --method agent-single
```

**Agent Multi-turn Loop**
```bash
# Dense Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type dense --method agent-loop

# Hybrid Embedding
python3 rag_enhanced/run_requests.py --input requests.jsonl --output-dir results_enhanced --data-root data --embedding_type hybrid --method agent-loop
```
