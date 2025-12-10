---
pretty_name: LitBench Preference Pairs (chat format)
dataset_name: CarlOwOs/LitBench-Processed
task_categories:
- text-generation
- preference-modeling
tags:
- rlhf
- pairwise-preference
- conversations
- literature
language:
- en
size_categories:
- n<1M
---

# LitBench Preference Pairs (chat format)

This dataset consolidates the LitBench train and test preference pairs into one repository with two splits: `train` and `test`. Each example contains two chat-style conversations under keys `chosen` and `rejected`, plus numeric scores `score_chosen` and `score_rejected`.

Last updated: 2025-10-04 05:15 UTC

## Splits

- train: 43827 examples
- test: 0 examples

## Features

- `chosen`: list of role/content messages representing the preferred conversation
- `rejected`: list of role/content messages representing the alternative conversation
- `score_chosen`: integer upvote score of the chosen story
- `score_rejected`: integer upvote score of the rejected story

## Loading

```python
from datasets import load_dataset

ds = load_dataset("CarlOwOs/LitBench-Processed")
print(ds)
```

## Citation

If you use this dataset, please also acknowledge the original LitBench sources.