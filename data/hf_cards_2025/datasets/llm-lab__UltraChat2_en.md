---
license: apache-2.0
tags:
- instruction-tuning
language:
- en
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 601622695
    num_examples: 103933
  download_size: 302900030
  dataset_size: 601622695
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# llm-lab/UltraChat2_en

This dataset is part of the **OryxTrain** collection.

Stored in efficient `.parquet` format for large-scale instruction-tuning.

## Format

Each record includes:
- `messages`: user/assistant dialogue 

Total examples: 103933

## Usage

```python
from datasets import load_dataset

ds = load_dataset("llm-lab/llm-lab/UltraChat2_en", split="train")
print(ds[0])
