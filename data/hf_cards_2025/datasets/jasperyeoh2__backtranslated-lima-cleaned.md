---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 263835
    num_examples: 115
  download_size: 165909
  dataset_size: 263835
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc
task_categories:
- question-answering
language:
- en
tags:
- llama
- instruction-tuning
- self-alignment
- backtranslation
pretty_name: Backtranslated LIMA (Cleaned)
size_categories:
- n<1K
---
