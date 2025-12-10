## Data Asset Overview

The scripts in the `RAG` directory curate three resources that track the 2025 LLM ecosystem: an arXiv literature digest, the README files for referenced GitHub repositories, and a snapshot of newly created LLM models and datasets on Hugging Face. This document summarizes how each dataset was collected, what it contains, and its current scale so you can reuse the data quickly.

### Quick snapshot

| Directory | What it contains | Current size (captured on 2025-10-21) |
| --- | --- | --- |
| `arxiv_llm_2025/` | arXiv metadata for LLM/RAG papers published in 2025 | 200 records in JSONL; companion CSV export with the same 200 entries (multi-line fields) |
| `github_readmes/` | Raw README files for GitHub repositories referenced in those papers | 30 repositories, 30 README files |
| `hf_cards_2025/` | Hugging Face repo cards for 2025 LLM models and datasets | 907 model manifest rows & 904 model cards; 536 dataset manifest rows & 521 dataset cards |

> **Counting notes**
> * Each JSONL/manifest line corresponds to one unique resource after deduplication.
> * The CSV export may have a `wc -l` result higher than 200 because description fields wrap across lines, but it still represents the same 200 papers.

---

## `arxiv_llm_2025/` — arXiv LLM paper index

* **Collection script**: `arxiv.py`
  * Queries the arXiv Atom API (`https://export.arxiv.org/api/query`) using `submittedDate:[202501010000 TO 202512312359]` plus LLM/RAG keywords and filters for `cs.CL`, `cs.LG`, `cs.AI`, `cs.IR`, and `stat.ML` categories.
  * Normalizes IDs such as `2301.01234v2` to their base form to avoid duplicates and parses author lists, category tags, primary category, PDF links, and other metadata for each entry.
  * Produces both `arxiv_llm_2025.jsonl` and `arxiv_llm_2025.csv` with fields `id / version / title / abstract / authors / categories / primary_category / published / updated / doi / journal_ref / comment / pdf_url / link / year / source` for downstream processing.

* **Directory layout**
  ```text
  arxiv_llm_2025/
  ├── arxiv_llm_2025.jsonl  # 200 UTF-8 records, one JSON object per line
  └── arxiv_llm_2025.csv    # Same content as CSV (authors & categories joined by semicolons)
  ```

* **Sample JSON entry**
  ```json
  {
    "id": "2501.00684",
    "title": "IGC: Integrating a Gated Calculator into an LLM to Solve Arithmetic Tasks Reliably and Efficiently",
    "abstract": "Solving arithmetic tasks is a simple and fundamental skill...",
    "authors": ["Florian Dietz", "Dietrich Klakow"],
    "categories": ["cs.LG", "cs.CL"],
    "primary_category": "cs.LG",
    "published": "2025-01-01T00:01:27Z",
    "updated": "2025-01-01T00:01:27Z",
    "pdf_url": "http://arxiv.org/pdf/2501.00684v1",
    "link": "http://arxiv.org/abs/2501.00684v1",
    "year": 2025,
    "source": "arxiv_api"
  }
  ```

---

## `github_readmes/` — README files for referenced repositories

* **Collection script**: `fetch_github_readmes.py`
  * Scans every string field in `arxiv_llm_2025.jsonl`, extracts URLs that match `https://github.com/{owner}/{repo}`, and deduplicates the set of repositories.
  * Downloads each README concurrently from `raw.githubusercontent.com/{owner}/{repo}/HEAD/README*`, trying common case variants and extensions (`.md`, `.rst`, `.txt`).
  * Stores results under `github_readmes/{owner}/{repo}/README.*` to keep provenance clear.

* **Directory layout (excerpt)**
  ```text
  github_readmes/
  ├── flashinfer-ai/
  │   └── flashinfer/README.md
  ├── RUCKBReasoning/
  │   └── CoT-based-Synthesizer/README.md
  └── ... 27 more owner/repo pairs
  ```

* **Use cases**: Offline inspection of implementation details, licenses, or replication steps tied to each paper. The README files mirror the HEAD branch at download time, so you can fetch full repositories later if needed.

---

## `hf_cards_2025/` — Hugging Face LLM resource cards

* **Collection script**: `huggingface.py`
  * Uses `huggingface_hub.HfApi` to enumerate models and datasets, applying `pipeline_tag`, `tags`, and `task_categories` filters for LLM, chat, instruction-tuning, RLHF, and related workloads.
  * Keeps only repositories created within a configurable date range (default `2025-01-01` to `2025-12-31`).
  * Saves structured manifests (`manifest_models.jsonl`, `manifest_datasets.jsonl`) and downloads each Repo Card as Markdown (`models/org__repo.md`, `datasets/author__dataset.md`). File names replace `/` with `__` to remain filesystem-safe.
  * Optional parameters include `--max-models`, `--max-datasets`, `--include-docs` (grab relevant guide pages), and `--token` for gated/private repos.

* **Directory layout**
  ```text
  hf_cards_2025/
  ├── manifest_models.jsonl   # 907 rows of model metadata
  ├── manifest_datasets.jsonl # 536 rows of dataset metadata
  ├── models/                 # 904 model Repo Cards
  │   └── org__repo.md
  └── datasets/               # 521 dataset Repo Cards
      └── author__dataset.md
  ```

* **Manifest fields**: `id`, `author`, `created_at`, `last_modified`, `private`, `gated`, `downloads`, `likes`, `library_name`, `pipeline_tag`, `tags`, `license`, and `repo_type`—handy for analytics or further filtering.

---

## Reproducing or refreshing the datasets

1. **Set up the environment**: install dependencies via `uv` or any interpreter compatible with the `pyproject.toml`.
2. **Update the arXiv index**:
   ```bash
   uv run python arxiv.py
   ```
   Adjust `QUERY_HUMAN` or date windows in `arxiv.py` if you need different coverage.
3. **Refresh GitHub README files**:
   ```bash
   uv run python fetch_github_readmes.py --input arxiv_llm_2025/arxiv_llm_2025.jsonl --output-dir github_readmes
   ```
   Use `--dry-run` to list the repos without downloading, and `--max-workers` to tune concurrency.
4. **Collect new Hugging Face cards**:
   ```bash
   uv run python huggingface.py --out hf_cards_2025 --date-range 2025-01-01:2025-12-31 --max-models 2000 --max-datasets 2000
   ```
   Narrow the date range or provide `--token` for gated content when doing incremental refreshes.

---

