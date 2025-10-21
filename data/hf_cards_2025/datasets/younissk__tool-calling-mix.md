---
title: Tool Calling SFT Mix
license: mit
tags:
- tool-calling
- function-calling
- instruction-tuning
- supervised-fine-tuning
- language-model
- artificial-intelligence
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- other
language:
- en
pretty_name: Tool Calling SFT Mix
configs:
- config_name: default
  default: true
  data_files:
  - split: train
    path: raw/train.jsonl.gz
  - split: validation
    path: raw/validation.jsonl.gz
  - split: test
    path: raw/test.jsonl.gz
dataset_info:
  features:
  - name: tools_json
    dtype: string
  - name: messages_json
    dtype: string
  - name: target_json
    dtype: string
  - name: meta_source
    dtype: string
  - name: n_calls
    dtype: int32
  - name: difficulty
    dtype: string
  - name: valid
    dtype: bool
  splits:
  - name: train
    num_bytes: 291192023
    num_examples: 60648
  - name: validation
    num_bytes: 36585030
    num_examples: 7581
  - name: test
    num_bytes: 36983211
    num_examples: 7581
  download_size: null
  dataset_size: null
---

![Toolmix-Banner](./images/Toolmix%20-%20Banner.png)

This is a dataset for fine-tuning a language model to use tools. I combined sources from various other tool calling datasets and added some non-tool calling examples to prevent catastrophic forgetting.

## Dataset Overview

### Motivation

This dataset was created to address the need for a diverse, high-quality dataset for training language models in tool usage. By combining multiple sources and including non-tool examples, it aims to produce models that can effectively use tools while maintaining general language capabilities.

### Key statistics

- **Dataset Size**: 75,810 total examples (100% valid)
- **Tool Usage**:
  - Average 1.34 tool calls per example
  - 74.5% simple examples, 19.8% parallel, 4.0% multiple, 1.7% no-call
  - Maximum 24 tool calls in a single example
- **Source Distribution**:
  - ToolBench Normalized: 26.4%
  - xLAM60k: 26.4%
  - OpenFunctions v1: 15.2%
  - Instruction No-Call (Dolly): 10.6%
  - WikiText No-Call: 10.6%
  - Synthetic Parallel: 6.6%
  - Others: 4.2%

### Pre-processing

1. All examples are converted to a unified schema
2. JSON fields are validated and normalized
3. Tool calls are extracted and standardized
4. Random seed 42 is used for all shuffling/sampling

### Intended Use

This dataset is designed for:

- Training language models to use tools effectively
- Fine-tuning existing models for tool usage
- Studying tool calling patterns and behaviors

### Known Limitations & Ethical Risks

1. Limited diversity in tool types and domains
2. Potential biases from source datasets
3. May not cover all edge cases in tool usage
4. Could enable misuse if not properly constrained

## Usage

### Load Dataset

```python
from datasets import load_dataset

ds = load_dataset("younissk/tool-calling-mix")
```

## Upstream Sources

I adapted and unified examples from the following sources. Please cite them if you use this dataset:

- Zhang, J. et al. (2024). xLAM: A Family of Large Action Models to Empower AI Agents. arXiv:2409.03215.
  Dataset: Salesforce/xlam-function-calling-60k (HF).
  (If using the parsed variant: minpeter/xlam-function-calling-60k-parsed, HF.)

- Patil, S. G., Zhang, T., Wang, X., Gonzalez, J. E. (2024). Gorilla: Large Language Model Connected with Massive APIs.
  NeurIPS 2024. Project: <https://gorilla.cs.berkeley.edu> (OpenFunctions).

- Databricks (2023). databricks-dolly-15k (HF). License: CC BY-SA 3.0.

- Merity, S., Xiong, C., Bradbury, J., Socher, R. (2016). Pointer Sentinel Mixture Models. arXiv:1609.07843.
  Dataset: Salesforce/wikitext – subset `wikitext-103-raw-v1` (HF). License: CC BY-SA.
