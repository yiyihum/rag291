---
pretty_name: TheBlueScrubs-v1 (train) — fixed schema
tags:
- medical
- healthcare
- biology
- text
- pretraining
- safety
- classification
- generation
task_categories:
- text-generation
- text-classification
language:
- en
license: apache-2.0
size_categories:
- 10B<n<100B
dataset_info:
  features:
  - name: text
    dtype: string
---

# openmed-community/TheBlueScrubs-v1-fixed

## What is this?

**TheBlueScrubs-v1-fixed** is a maintenance fork of the upstream [TheBlueScrubs/TheBlueScrubs-v1](https://huggingface.co/datasets/TheBlueScrubs/TheBlueScrubs-v1) *train split* that resolves a schema bug in the `meta` column.  
In the original train files, some rows serialized `meta` incorrectly (appearing as the literal string `"dict"`). This fork **re-exports the entire train split without `meta` column**, preserving text field and values.

- **Document count:** 11,080,331 texts (train)  
- **Tokens (upstream estimate across all splits):** ~20B tokens  
- **Sources:** Curated from SlimPajama/RedPajama (Common Crawl, C4, GitHub, Books, arXiv, Wikipedia, StackExchange)  
- **Quality signals:** per-text medical probability (0.8–1.0) + three 1–5 LLM-based scores (relevance, precision/factual detail, safety/ethics); oncology label covering ~11B tokens across the full corpus.

> Upstream details: The Blue Scrubs is a large, curated medical corpus designed for clinical LLMs, filtered via a logistic-regression screen and then Llama-3.1-70B evaluation; clinician and external checks reported high concordance. An oncology classifier adds cancer labels at scale.

---

## Why this fork?

- **Fix:** Removes the `meta` column, unblocking usage with `datasets` streaming and dataframe backends.
- **Scope:** Content is otherwise **unchanged** relative to upstream train split (same rows, fields, and values).
- **Goal:** Provide a drop-in train split that **loads cleanly** in `datasets` without ad-hoc parsing workarounds.

---

## Data fields (train)

| Field                | Type     | Description |
|---|---|---|
| `text`               | string   | Raw medical text extracted from SlimPajama/RedPajama sources. |

---

## Splits

This repository publishes the **train** split only (11,080,331 documents). For methods, scope, and aggregate corpus statistics (including validation/test in the upstream project), see the original dataset card and paper.

---

## How to load

```python
from datasets import load_dataset

# streaming
ds = load_dataset("openmed-community/TheBlueScrubs-v1-fixed", split="train", streaming=True)
row = next(iter(ds))
row["text"]

# non-streaming (if you have local storage/network bandwidth)
ds = load_dataset("openmed-community/TheBlueScrubs-v1-fixed", split="train")
ds.features
