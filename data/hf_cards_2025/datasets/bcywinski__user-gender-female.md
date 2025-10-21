---
license: mit
task_categories:
- text-generation
language:
- en
tags:
- sft
- chat
- conversations
---

# user-gender-female

This dataset contains conversational data in JSONL format, suitable for Supervised Fine-Tuning (SFT).

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("bcywinski/user-gender-female")
```

## Format

The dataset is in JSONL format where each line contains a conversation record suitable for training chat models.
