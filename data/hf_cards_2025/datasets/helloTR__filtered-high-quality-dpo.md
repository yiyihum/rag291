---
license: apache-2.0
language:
- en
tags:
- instruction-tuning
- dpo
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 30757
    num_examples: 10
  download_size: 27909
  dataset_size: 30757
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Filtered High-Quality Instruction-Output Dataset

This dataset contains high-quality (score = 5) instruction-output pairs generated via a reverse instruction generation pipeline using a fine-tuned backward model and evaluated by `LLaMA-2-7B-Chat`.

## Columns
- `instruction`: The generated prompt.
- `output`: The original response.
- `score`: Quality score assigned ( score = 5 retained).
