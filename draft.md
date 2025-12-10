Great—your domain is clear: the 2025 LLM ecosystem spanning arXiv papers, linked GitHub repos, and Hugging Face (HF) model/dataset cards. Below is a concrete, rubric-aligned plan for (1) posing a strong request set, (2) building retrieval that actually works on your three corpora, and (3) evaluating it rigorously.

⸻

1) Request Set (10–15 non‑trivial queries)

Design queries that force cross-source evidence, use filters/fields (date, tags, license, pipeline), and sometimes require multi-hop linkage (paper → repo → HF). Use the JSONL schema below and fill in for each query.

Suggested schema (requests.jsonl):

{
  "qid": "Q1",
  "query": "Which 2025 arXiv papers that introduce new LLMs also released open weights on Hugging Face? Return the paper IDs and HF model IDs.",
  "intent": "entity-linking+filtering",
  "required_corpora": ["arxiv", "hf_models"],
  "filters": {"year": 2025, "hf_repo_type": "model", "license_family": "open"},
  "answer_type": "list_of_pairs",
  "notes_for_judges": "Primary evidence is the HF model card explicitly linking to the paper ID or title; arXiv abstract should indicate the introduction of a model."
}

15 query ideas (mix of difficulty and coverage):
	1.	(Cross-link)
Which 2025 arXiv papers that introduce new LLMs also released open weights on HF? Return paper ID ↔ HF model ID.
	2.	(Method→Code)
For paper {arXiv ID or title}, retrieve the GitHub README section with Installation or Quickstart that implements it.
	3.	(Safety datasets)
List 2025 HF datasets tagged with safety/jailbreak/red-teaming and provide their licenses and gating status.
	4.	(RLHF corpora)
Which 2025 datasets are designed for RLHF/DPO/KTO/ORPO? Provide dataset IDs and evidence snippets defining the alignment method.
	5.	(Licenses)
Find 2025 models with permissive licenses (e.g., Apache-2.0, MIT). Return model ID, license, and download counts.
	6.	(Reasoning evals)
Which 2025 models report results on GSM8K / MATH / AIME / MMLU? Provide model cards and the section with numbers.
	7.	(RAG benchmarks)
Which 2025 arXiv papers evaluate RAG on BEIR / HotpotQA / NQ / FiQA? Return paper IDs with abstract snippets.
	8.	(MoE inference)
Identify 2025 GitHub repos that provide MoE inference or custom kernels (e.g., FlashAttention/FlashInfer). Return repo → README snippet with throughput claims.
	9.	(Tool use / calculator)
Which 2025 papers integrate tool use (calculator/retrieval/code execution), and what repos/models implement them?
	10.	(Data provenance)
Find HF model cards (2025) that disclose training data sources (e.g., web, curated datasets). Return the policy/provenance section.
	11.	(Gated access)
Which 2025 HF models/datasets are gated/private? Provide gating status and justification text from the card.
	12.	(Instruction-tuned chat)
Retrieve instruction-tuned chat models created in 2025, with library_name and pipeline_tag; list likes/downloads.
	13.	(Eval replication)
For paper {title|ID}, find the exact command or script path in the linked README that reproduces evaluation.
	14.	(RAG corpora release)
Which 2025 RAG papers released retrieval corpora or evaluation sets? Return paper IDs and any HF datasets they link to.
	15.	(Model–dataset co-mention)
Find HF model cards (2025) that explicitly cite an arXiv paper by ID (e.g., 2501.xxxx) and return model ↔ paper mapping.

Judging guidance: For each Q, specify what counts as primary relevance (contains the authoritative answer snippet) vs secondary (contextual but not decisive).

⸻

2) How to Retrieve (indexing, hybrid search, linking, and ranking)

2.1 Canonical IDs & Cross-links

Create consistent IDs and link tables so multi-hop queries are possible.
	•	Doc IDs
	•	arxiv:2501.00684
	•	gh:owner/repo#readme#h2=Installation (section-level if possible)
	•	hf:model:org/repo and hf:dataset:user/dataset
	•	Link extraction
	•	From arXiv JSONL: URLs matching https://github.com/{owner}/{repo} → paper→repo edges.
	•	From HF cards: regex for arXiv:\s*([0-9]{4}\.[0-9]{5}) and for GitHub links → model/dataset→paper and →repo edges.
	•	Store a links.jsonl:

{"src": "arxiv:2501.00684", "type": "points_to", "dst": "gh:flashinfer-ai/flashinfer"}



2.2 Field-aware indexing (two-store design)

A. Catalog store (structured)
	•	Index manifests with strongly typed fields for filters/facets:
	•	arXiv: year, primary_category, authors, title
	•	HF models/datasets: created_at, license, pipeline_tag, tags, gated, private, downloads, likes, repo_type
	•	Backends: Elasticsearch/OpenSearch (BM25 + filters) or SQLite/duckdb for prototyping filters.

B. Content store (semantic)
	•	Index text content:
	•	arXiv: title + abstract (short)
	•	GitHub: README by Markdown section
	•	HF cards: full card by sections (headings)
	•	Chunking:
	•	Section-aware: split on #, ##, ###; keep headers in chunk metadata.
	•	Token target: 500–800 tokens with 80–120 overlap for long sections.
	•	Embeddings:
	•	Open-source: bge-m3 or bge-small-en-v1.5
	•	Hosted option: text-embedding-3-large
	•	Vector backends: FAISS (local), Qdrant/Weaviate (service).

2.3 Hybrid retrieval + fusion
	1.	Apply filters in the catalog store (date=2025, tags, license, repo_type).
	2.	BM25 search on titles, tags, headings (fast keyword grounding).
	3.	Dense retrieval on content chunks.
	4.	Reciprocal Rank Fusion (RRF) to combine BM25 and vector hits.
	5.	Rerank (optional but strong):
	•	Cross-encoder (e.g., ms-marco-MiniLM-L-6-v2) on top‑20 to top‑50.
	6.	Diversity & quotas
	•	Ensure cross-corpus coverage with MMR or per‑corpus caps (e.g., at k=10 aim for 4 HF, 3 GitHub, 3 arXiv if the query is cross-source).

2.4 Snippet selection & provenance
	•	Return the best scoring chunk + 2–3 surrounding sentences.
	•	Always include: {doc_id, corpus, title, url_or_path, heading, score, line_offsets}.
	•	For HF cards and READMEs, prefer heading-anchored snippets (Installation, License, Evaluation, Dataset).

2.5 Output format for runs

Write one file per system per query, e.g.:

runs/
  faiss/
    Q1.json
  qdrant/
    Q1.json
  elastic/
    Q1.json

Payload (Q1.json):

{
  "qid": "Q1",
  "hits": [
    {"rank": 1, "doc_id": "hf:model:org/repo", "score": 27.1, "corpus": "hf_models"},
    {"rank": 2, "doc_id": "arxiv:2501.00684", "score": 25.3, "corpus": "arxiv"},
    {"rank": 3, "doc_id": "gh:owner/repo#readme#h2=Installation", "score": 24.8, "corpus": "github"}
  ]
}


⸻

3) Evaluation (quant + qual, with manual baseline)

3.1 Build qrels (manual relevance)

Use TREC-style pooling:
	•	For each query, pool top‑10 from each system (BM25, FAISS, Qdrant).
	•	Judge only the pooled union (saves effort).
	•	Grades:
	•	2 (Primary): directly contains the answer (e.g., license on model card; install commands in README).
	•	1 (Secondary): supporting context or partial mention.
	•	0 (Irrelevant).
	•	Store as qrels.jsonl:

{"qid":"Q1","doc_id":"hf:model:org/repo","rel":2}
{"qid":"Q1","doc_id":"arxiv:2501.00684","rel":1}

3.2 Core retrieval metrics

Compute per system and macro-average:
	•	nDCG@k (k=10) – supports graded relevance.
	•	Recall@k (k=10, 20, 50) – critical for multi-hop queries.
	•	MAP@100 – overall ranking quality.
	•	MRR@10 – first correct hit latency.

3.3 Domain-specific metrics (recommended)
	•	Cross-source coverage@k: fraction of required corpora present in the top‑k (e.g., query requires both HF model card and its arXiv paper).
	•	Provenance completeness: when the answer demands multiple items (e.g., model+dataset), measure the fraction retrieved.
	•	Field-consistency accuracy for filter queries: % of returned items actually satisfying license, gated, pipeline_tag, created_at ∈ 2025.
	•	Snippet support rate: % of hits where the returned snippet includes a sentence that justifies relevance (regex heuristics for licenses, eval names, arXiv IDs).

3.4 Evaluator I/O

Inputs:
	•	requests.jsonl
	•	qrels.jsonl
	•	runs/<system>/<qid>.json (for each system)

Outputs:
	•	metrics/<system>.json (per-metric scores)
	•	leaderboard.csv
	•	per_query_breakdown.csv
	•	errors/ (missed-primary, false-positives)

Evaluator logic (sketch):

# load requests, qrels, and runs
# compute nDCG@k, Recall@k, MAP, MRR
# compute domain extras:
#   - coverage@k using requests[qid]["required_corpora"]
#   - field-consistency: re-check filters against catalog metadata
#   - snippet support via regexes (e.g., r'\bApache-2\.0\b', r'arXiv:\s*\d{4}\.\d{5}')

3.5 Qualitative case studies

For 3–5 queries, include:
	•	Top results from each system with snippets and why they scored.
	•	Missed-but-relevant items (from qrels=2 not in top‑k) and why missed (bad chunking, no synonyms, weak link detection).
	•	Concrete remediation (add synonyms to BM25, add link edges, tune chunk size, add reranker).

⸻

4) Minimal, Reproducible Baseline

4.1 Data normalization
	•	Create canonical namespaces:
	•	corpus ∈ {arxiv, github, hf_models, hf_datasets}
	•	doc_id scheme as above.
	•	Produce:
	•	catalog/*.parquet (structured fields)
	•	chunks/*.parquet (chunk_id, doc_id, corpus, title, heading, text, tokens)
	•	links.jsonl (edges)

4.2 Two retrieval stacks to compare
	•	BM25 + filters (Elasticsearch/OpenSearch)
	•	FAISS + RRF with BM25 (dense + keyword fusion)
	•	Embedding: bge-small-en-v1.5 (fast) or bge-m3 (multilingual)

4.3 Reranker (optional but impactful)
	•	Cross-encoder on the top‑50 from fusion; write to runs/<system>_rerank.

⸻

5) Deliverables Checklist (matches grading rubric)

Data & Requests
	•	requests.jsonl (≥10 queries with intent, filters, required_corpora, answer_type, notes_for_judges)
	•	catalog/*.parquet and chunks/*.parquet (cleaned, chunked, with metadata)
	•	links.jsonl (paper↔repo↔HF edges)

Manual Baseline
	•	qrels.jsonl with graded relevance (2/1/0)
	•	README describing judging guidelines and examples

Systems & Raw Results
	•	runs/faiss/*.json, runs/elastic/*.json, (optional) runs/qdrant/*.json
	•	Exact commands / scripts to reproduce

Evaluator
	•	evaluate.py (computes nDCG@10, Recall@{10,20,50}, MAP, MRR, + domain metrics)
	•	metrics/*.json, leaderboard.csv, per_query_breakdown.csv
	•	Short report with 3–5 qualitative case studies

⸻

6) Practical Tips (so it works on your data)
	•	Chunk by headings for READMEs and HF cards; keep headings in metadata to target sections like “License”, “Evaluation”, “Installation”.
	•	Normalize licenses (e.g., map variants of “Apache 2.0” to Apache-2.0) before field-consistency checks.
	•	Link detection: build regexes for arXiv IDs and GitHub URLs in HF cards; store edges and use them as boosts at ranking time.
	•	Fusion weights: start with RRF (k=60) and optionally add a small link-boost (e.g., +α if an item is linked to another top-ranked item).
	•	Corpus quotas: for cross-source queries, enforce a minimum of 1–2 results per required corpus in the top‑k.
	•	Failure modes: very long sections dilute signal—split >1,000 tokens; very short chunks (<100 tokens) are noisy—merge them.

⸻