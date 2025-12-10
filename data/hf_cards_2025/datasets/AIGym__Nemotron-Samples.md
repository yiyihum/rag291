---
tags:
- text-generation
- pretraining
- nvidia
- nemotron
language:
- en
- multilingual
license: other
---

# Nemotron Samples Dataset

This dataset combines all subsets from the NVIDIA Nemotron-Pretraining-Dataset-sample with a 90/5/5 train/validation/test split.

## Subsets Included

- Nemotron-CC-High-Quality
- Nemotron-CC-Diverse-QA
- Nemotron-CC-High-Quality-Synthetic
- Nemotron-CC-MATH
- Nemotron-CC-Translated-Diverse-QA
- Nemotron-Synthetic-Code

## Dataset Statistics

- **Total samples**: 23,706
- **Train**: 21,335 samples
- **Validation**: 1,185 samples  
- **Test**: 1,186 samples

## Subset Distribution

- **Nemotron-CC-High-Quality**: 785 samples (3.3%)
- **Nemotron-CC-Diverse-QA**: 2,065 samples (8.7%)
- **Nemotron-CC-High-Quality-Synthetic**: 3,461 samples (14.6%)
- **Nemotron-CC-MATH**: 954 samples (4.0%)
- **Nemotron-CC-Translated-Diverse-QA**: 15,441 samples (65.1%)
- **Nemotron-Synthetic-Code**: 1,000 samples (4.2%)

## Dataset Schema

Each sample contains:
- `id`: Unique identifier
- `text`: Main text content
- `subset`: Source subset name
- `language`: Language code (en for English, others for multilingual content)
- `metadata`: Additional metadata as JSON string (if available)

## Usage

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("AIGym/Nemotron-Samples")

# Load specific split
train_data = load_dataset("AIGym/Nemotron-Samples", split="train")

# Filter by subset
math_samples = dataset.filter(lambda x: x["subset"] == "Nemotron-CC-MATH")

# Filter by language
english_samples = dataset.filter(lambda x: x["language"] == "en")
```

## Source

Original dataset: [nvidia/Nemotron-Pretraining-Dataset-sample](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample)

## Processing Notes

- All subsets have been standardized to a common schema
- Metadata from different subsets has been preserved as JSON strings
- Language information is included where available
- Random seed 42 used for reproducible splits
