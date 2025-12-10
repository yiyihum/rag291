---
language:
- en
license: other
pretty_name: BIOBERT — Microbiology OA Full-Text Corpus
dataset_type: text
task_categories:
- fill-mask
tags:
- microbiology
- open-access
- pmc
- europe-pmc
- fulltext
- mlm
- pretraining
- biobert
- english
size_categories:
- unknown
---

# BIOBERT — Microbiology OA Full-Text Corpus

**Purpose:** Provide an English **Open-Access–only** full-text corpus in microbiology and related domains for:
- Domain/Task-Adaptive Pretraining (DAPT/TAPT) with **Masked Language Modeling (MLM)**
- Fine-tuning BERT-style models such as BioBERT

> ⚠️ **Copyright / License:** This repository includes **OA items only** (e.g., PMC / Europe PMC OA). Each item must be used under its **original upstream license**. The fields `license_type` and `license_url` are included in every record. This repository does **not** grant a new license for redistribution.

## Data format
Recommended file format: **JSON Lines (`.jsonl`)** — one document/section per line.

**Example record**
```json
{
  "id": "pmcid:PMC1234567#sec3",
  "title": "Sample article title",
  "text": "full body text …",
  "source": "PMC",
  "pmcid": "PMC1234567",
  "doi": "10.xxxx/xxxx",
  "year": 2024,
  "journal": "Journal Name",
  "section": "body",
  "license_type": "CC-BY-4.0",
  "license_url": "https://creativecommons.org/licenses/by/4.0/",
  "url": "https://europepmc.org/…"
}
