---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: system
    dtype: string
  splits:
  - name: train
    num_bytes: 612455566
    num_examples: 54046
  download_size: 241069122
  dataset_size: 612455566
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- en
size_categories:
- 10K<n<100K
tags:
- sft
- instruction-tuning
- question-answering
- reasoning
- llm
pretty_name: SFT Formatted 54k Dataset with Reasoning Scores
annotations_creators:
- XuHu6736 (formatting and derivation)
- derived from XuHu6736/s1_54k_filter_with_isreasoning
language_creators:
- derived from source datasets
multilinguality: monolingual
source_datasets:
- XuHu6736/s1_54k_filter_with_isreasoning
---


# Dataset Card for XuHu6736/SFT_54k_reasoning

## Dataset Description

**XuHu6736/SFT_54k_reasoning** is a processed version of the [XuHu6736/s1_54k_filter_with_isreasoning](https://www.google.com/url?sa=E&source=gmail&q=https://huggingface.co/datasets/XuHu6736/s1_54k_filter_with_isreasoning) dataset, specifically reformatted for instruction fine-tuning (SFT) of language models.

The original `question` and `solution` pairs have been converted into an instruction-following format. Critically, the `isreasoning_score` and `isreasoning` labels from the parent dataset are preserved, allowing for targeted SFT on samples evaluated for their reasoning suitability.

For comprehensive details on the original data sources, initial filtering, annotation process for reasoning scores, and composition, please refer to the dataset cards for its predecessors:
* [XuHu6736/s1_54k_filter_with_isreasoning](https://www.google.com/url?sa=E&source=gmail&q=https://huggingface.co/datasets/XuHu6736/s1_54k_filter_with_isreasoning)
* [XuHu6736/s1_54k_filter](https://huggingface.co/datasets/XuHu6736/s1_54k_filter)
* [XuHu6736/s1_59k](https://huggingface.co/datasets/XuHu6736/s1_59k)

## Instruction Formatting

The dataset has been transformed into an instruction format suitable for many SFT pipelines. While the exact fields should be inspected by the user, a common structure for instruction datasets is:

* **`instruction`**: Contains the task description, typically derived from the original `question` field.
* **`input`**: May contain additional context for the instruction. For this dataset, it might be empty if the original `question` was self-contained.
* **`output`**: Contains the desired response, typically derived from the original `solution` field.
