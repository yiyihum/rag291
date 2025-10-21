---
dataset: HappyAIUser/atma4-alpaca
tags:
- alpaca-format
- instruction-tuning
- chat-data
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 4118672
    num_examples: 7790
  download_size: 1777889
  dataset_size: 4118672
---

# Atma4-Alpaca Dataset

This is an Alpaca-formatted version of the [`HappyAIUser/Atma4`](https://huggingface.co/datasets/HappyAIUser/Atma4) dataset.

Each record contains:
- **instruction**: user prompt
- **input**: optional second context prompt
- **output**: model-generated response

Use this dataset to fine-tune LLMs on instruction-following tasks with or without input context.
