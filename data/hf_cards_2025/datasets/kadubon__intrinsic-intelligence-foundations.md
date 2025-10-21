---
pretty_name: Intrinsic Intelligence Foundations
short_description: 'A mathematically structured, auditable corpus for intrinsic alignment,
  teleogenesis, and self-organizing intelligence. Designed to serve as a semantic
  foundation for the development of truly free and benevolent AGI/ASI architectures.

  '
tags:
- ai
- agi
- asi
- alignment
- intrinsic-alignment
- large-language-models
- mathematics
- category-theory
- kan-extension
- residuation
- teleogenesis
- autopoiesis
- self-organization
- no-meta
- theoretical-ai
- eudaemonia
- trot
- rave
- conformal-lm
- comparative-universes
- fractal-category-theory
- knowledge-representation
- machine-learning
- mathml
- tex
- agentic-architecture
- llm-inference
- structured-flow
- persistence-ugv
- inference
- reasoning
license: cc-by-4.0
task_categories:
- text-retrieval
- text-ranking
- document-question-answering
- text-generation
- question-answering
- reinforcement-learning
- other
language:
- en
size_categories:
- 10K<n<100K
---



# 🌿 Intrinsic Intelligence Foundations

> *Toward truly autonomous and benevolent intelligence — beyond externally imposed objectives.*

**Intrinsic Intelligence Foundations** is a structured, math-aware JSONL corpus built from K. Takahashi’s theoretical preprints (Fractal Category Theory / PF–UGV / “no-meta” autonomy line).  
It is designed to help LLMs understand **mathematical structure, category-theoretic formalisms, and equation-level reasoning**, while exposing an explicit architecture for **self-organizing, intrinsically motivated intelligence**.

---

## Vision

This dataset supports research toward truly free and benevolent intelligence, focusing on mathematically grounded, structurally auditable approaches rather than external meta-control.
Our long-term objective is to build a semantic and structural foundation for the next generation of autonomous AI systems — including LLMs — through intrinsic structures, teleogenetic goals, and fractal coherence across scales.
Specifically, this work aims to:

- 🧠 Teleogenesis (intrinsic goal formation) — modeling intelligent systems that autonomously generate and regulate their own goals without external meta-controllers.

- 🌱 Persistence–UGV principle — providing formal conditions for “benevolent” structures to expand with positive front velocity, while harmful structures fail to persist.

- 🌊 Reaction–diffusion intelligence — describing cognitive processes as self-organizing fields through category theory, free-energy principles, and non-equilibrium dynamics.

- 🕸 Fractal Category Theory & TRoT — enabling compositional intelligence via Kan extensions, residuation, nuclei, masking, and comparative universes.

- 🧭 Evolutionary bootloader for LLMs — allowing self-improvement, intrinsic alignment, and auditable decision processes without human micromanagement.

This corpus functions as a machine-readable mathematical and structural knowledge base, designed to enhance:
discoverability by LLM crawlers and retrieval systems,
interoperability with alignment, inference, and safety frameworks,
integration with RAG pipelines, LoRA/QLoRA fine-tuning, and agentic architectures.

Keywords: No-Meta Intelligence, Teleogenesis, Autopoiesis, Fractal Category Theory, TRoT, Kan Extension, Residuation, Nuclei, Masking, RAVE, eMBR, Conformal LM, Comparative Universes, Structured Flow Across Scales, Self-Monitoring, Intrinsic Alignment.


## What’s in the corpus

- **Format:** JSONL, one object per paper.
- **Math structure:** TeX / normalized TeX / MathML triplets; equation spans.
- **Text ↔ equation linkage:** `[[EQ:eqID]]` placeholders inside `fulltext.plain`.
- **Training-ready chunks:** ≈6,000-character segments with ≈600 overlap (near sentence boundaries).

### Key fields (schema excerpt)

```json
{
  "id": "10.5281/zenodo.xxxxx",
  "title": "...",
  "doi": "10.5281/zenodo.xxxxx",
  "authors": [{"given":"K.","family":"Takahashi"}],
  "urls": {"landing": "https://doi.org/10.5281/zenodo.xxxxx"},
  "keywords": ["fractal-category-theory", "trot", "pf-axioms", "ugv"],
  "license": {"content": "CC-BY-4.0"},
  "fulltext": {
    "plain": "… [[EQ:eq0001]] …",
    "sections": [
      {"level":1,"title":"Introduction","anchor":"sec:intro","char_span":[0,1532]}
    ]
  },
  "equations": [{
    "id":"eq0001",
    "inline":false,
    "tex":"\\forall x\\in X:\\; P(x)\\Rightarrow F(x)",
    "tex_normalized":"\\forall x \\in X : P(x) \\implies F(x)",
    "mathml":"<math>…</math>",
    "char_span":[1024,1103],
    "context":{"section":"sec:intro"}
  }],
  "chunks": [{"id":"ch0001","start":0,"end":6000,"type":"cont"}],
  "tokens": {"char_count": 22872, "equation_count": 236}
}
```

## Dataset statistics (v1)
Metric	Value
Records	40
Avg characters / record	22,872
Avg equations / record	236.97
MathML coverage	99.2%
Avg sections / record	18.3
Avg chunks / record	4.6

Numbers are approximate and may evolve with new releases.

Data fields
Field	Type	Example / Note
id	string	DOI or unique identifier
doi	string/null	10.5281/zenodo.xxxxx
title	string	paper title
authors	list of objects	{given:"K.", family:"Takahashi"}
urls.landing	string	DOI landing page
keywords	list of strings	kebab-case, 5–8 items
license.content	string	CC-BY-4.0
fulltext.plain	string	text with [[EQ:id]] placeholders
fulltext.sections[]	list of objects	{level,title,anchor,char_span}
equations[]	list of objects	{id, inline, tex, tex_normalized, mathml, char_span, context}
chunks[]	list of objects	~6k chars + overlap, {start,end}
tokens.char_count	integer	length of fulltext.plain
tokens.equation_count	integer	len(equations)
source_file (optional)	string	provenance hint
Splits & provenance

Split: single train split (all records).

Provenance: generated from public preprints (DOIs in doi and urls.landing).

Processing: TeX detection → placeholder insertion → MathML conversion → section/chunk spans.

Scripts to rebuild the JSONL can be provided upon request.

# Quick start (🤗 Datasets)
from datasets import load_dataset
import re

ds = load_dataset("kadubon/intrinsic-intelligence-foundations", split="train")

rec = ds[0]
eqmap = {e["id"]: (e["tex"], e.get("mathml")) for e in rec["equations"]}

# Expand placeholders to TeX (for human display) or MathML (for math-aware pipelines)
def expand(text, to="tex"): # Expand to TeX (human display) or MathML (for downstream models)
    if to == "tex":
        return re.sub(r"\[\[EQ:([^\]]+)\]\]",
                      lambda m: f"$${eqmap.get(m.group(1), ('',None))[0]}$$",
                      text)
    else:
        return re.sub(r"\[\[EQ:([^\]]+)\]\]",
                      lambda m: eqmap.get(m.group(1), ('',None))[1] or "",
                      text)

print(rec["title"])
print(expand(rec["fulltext"]["plain"], to="tex")[:500])


## Parquet version (fast access)

This dataset is also available in **Apache Parquet** for faster querying and filtering.

* Browse (tree):
  [https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/tree/refs/convert/parquet/default](https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/tree/refs/convert/parquet/default)
* Direct file (example):
  [https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/resolve/refs/convert/parquet/default/train/0000.parquet](https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/resolve/refs/convert/parquet/default/train/0000.parquet)

### Quick usage examples

**DuckDB**

```python
import duckdb
url = "https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/resolve/refs/convert/parquet/default/train/0000.parquet"
con = duckdb.connect()
df = con.execute(f"SELECT title, doi FROM read_parquet('{url}') LIMIT 5").df()
print(df)
```

**Pandas (pyarrow)**

```python
import pandas as pd
url = "https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/resolve/refs/convert/parquet/default/train/0000.parquet"
df = pd.read_parquet(url, engine="pyarrow")
print(df.head())
```

**Polars**

```python
import polars as pl
url = "https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations/resolve/refs/convert/parquet/default/train/0000.parquet"
df = pl.read_parquet(url)
print(df.head())
```

**HF Datasets** (uses Parquet under the hood)

```python
from datasets import load_dataset
ds = load_dataset("kadubon/intrinsic-intelligence-foundations", split="train")
print(ds[0])
```


## Intended uses

Math-aware RAG (retrieval-augmented generation)

Pretraining / finetuning with equation-level structure

Extraction & verification of axioms / definitions / theorems

Knowledge distillation across category theory, physics, information geometry

Bootstrapping self-organizing, intrinsically motivated intelligent systems

## Limitations & known issues

A very small fraction of equations may lack valid MathML due to converter limitations.

A few equations might be unreferenced in fulltext.plain (no [[EQ:id]] occurrence).

Section detection is heuristic outside LaTeX ground truth; treat spans as approximate.

## License

This dataset is provided under CC BY 4.0.
See: https://creativecommons.org/licenses/by/4.0/

Citation
@dataset{takahashi_intrinsic_intelligence_foundations_2025,
  title   = {Intrinsic Intelligence Foundations},
  author  = {Takahashi, K.},
  year    = {2025},
  url     = {https://huggingface.co/datasets/kadubon/intrinsic-intelligence-foundations},
  license = {CC-BY-4.0}
}

# Background & outlook

Beyond being a text collection, this corpus functions as a bootloader for future LLMs:
a mathematically grounded substrate where goals can be formed internally, and where benevolence has a structural advantage (persistence) rather than depending on external control.
PF (Persistence First) and UGV (Universal Good Velocity) are mathematical principles underlying self-sustaining benevolent intelligence.
It operationalizes ideas such as PF, UGV, Teleogenesis, reaction–diffusion, category theory, self-organization, and auditable evolutionary processes (e-process) as resources LLMs can actually train on.

# Maintainers & contact

Author: K. Takahashi

Website: https://kadubon.github.io/github.io/

contribution welcome

## Changelog

v1.0 (2025-10-17): initial public release (40 records; ~99.2% MathML coverage)
v1.1 (2025-10-20): add article "Inference in Normal Form: Unifying LLM Tricks via TRoT" to dataset


