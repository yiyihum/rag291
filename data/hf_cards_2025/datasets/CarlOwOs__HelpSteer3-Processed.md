---
pretty_name: HelpSteer3 Preference Pairs (chat format)
dataset_name: CarlOwOs/HelpSteer3-Processed
task_categories:
- text-generation
- preference-modeling
tags:
- rlhf
- pairwise-preference
- conversations
language:
- en
size_categories:
- n<1M
---

# HelpSteer3 Preference Pairs (chat format)

This dataset converts the HelpSteer3 preference pairs into a unified format with chat-style conversations under keys `chosen` and `rejected`, and a single integer `margin` derived from the dataset's overall preference score.

Last updated: 2025-10-13 10:45 UTC

## Preference → margin mapping

The original HelpSteer3 `overall_preference` is an integer in [-3, 3]:

- -3: Response 1 is much better than Response 2
- -2: Response 1 is better than Response 2
- -1: Response 1 is slightly better than Response 2
- 0: Responses are about the same
- 1: Response 2 is slightly better than Response 1
- 2: Response 2 is better than Response 1
- 3: Response 2 is much better than Response 1

We set:

- `chosen` to the conversation with the preferred response appended
- `rejected` to the conversation with the other response appended
- `margin = abs(overall_preference)` (a non-negative integer in [0, 3])

This `margin` can be used in margin-aware reward training, e.g. to encourage `reward(chosen) - reward(rejected) ≥ margin`.

## Splits

- train: 38459 examples
- validation: 2017 examples

## Features

- `chosen`: list of role/content messages representing the preferred conversation
- `rejected`: list of role/content messages representing the alternative conversation
- `margin`: integer in [0, 3] indicating preference strength

## Loading

```python
from datasets import load_dataset

ds = load_dataset("CarlOwOs/HelpSteer3-Processed")
print(ds)
```

## Source

Derived from `nvidia/HelpSteer3`.