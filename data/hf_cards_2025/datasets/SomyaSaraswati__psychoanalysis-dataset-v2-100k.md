---
license: apache-2.0
language:
- en
- hi
- multilingual
pretty_name: Psychoanalysis v2 — 100k (Hinglish + English)
tags:
- psychoanalysis
- mental-health
- hinglish
- conversational
- instruction-tuning
task_categories:
- text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path:
    - train_shard_*.jsonl
  - split: validation
    path:
    - validation_shard_*.jsonl
---

# Psychoanalysis v2 — 100k (Hinglish + English)

This dataset contains 100k psychoanalytic-style conversational samples in Hinglish and English.
It includes `messages` (system/user/assistant), a supervised `output`, safety/evaluation metadata,
and a `pair` field for preference learning (DPO/ORPO).

## Loading

```python
from datasets import load_dataset
ds = load_dataset("SomyaSaraswati/psychoanalysis-dataset-v2-100k")
print(ds)
print(ds["train"][0].keys())
