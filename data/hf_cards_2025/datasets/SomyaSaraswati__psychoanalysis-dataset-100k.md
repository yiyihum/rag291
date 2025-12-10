---
datasets:
- SomyaSaraswati/psychoanalysis-dataset-100k
language:
- en
- hi
language_bcp47:
- hi-Latn
tags:
- psychoanalysis
- instruction-tuning
- india
- hinglish
- safety
license: cc-by-sa-4.0
task_categories:
- text-generation
pretty_name: Psychoanalysis Synthetic Instruction Dataset (100k)
size_categories:
- 100K<n<1M
---

# Psychoanalysis Synthetic Instruction Dataset (v1, 100k)

**Domain:** psychoanalytic reflection / therapy-style dialogues  
**Locale:** English + Hinglish (India context)  
**Size:** 100,000 rows; 10 shards × 10k JSONL  

## Schema
Chat-style `messages` + `instruction/input/output` + `safety` + `metadata`.  
Educational only; not clinical advice.

## Split
`train` only (create validation downstream with `train_test_split`).

## Generation Notes
Synthetic templates + slot-filling; no diagnosis/medication guidance; includes escalation triggers.
