---
license: mit
task_categories:
- text-classification
language:
- ja
tags:
- japanese
- formality
- chat
- conversation
size_categories:
- n<1K
---

# Japanese Real Chat Dataset

This dataset contains Japanese conversational text samples labeled by formality level (business vs casual).

## Dataset Details

### Dataset Description

- **Language:** Japanese
- **Task:** Text classification (formality detection)
- **Size:** 124 samples
- **Format:** Parquet

### Dataset Structure

The dataset contains two columns:
- `text`: Japanese conversational text
- `category`: Formality label (`business` or `casual`)

### Data Distribution

- **Business:** 60 samples (48.4%)
- **Casual:** 64 samples (51.6%)

### Usage

This dataset can be used for:
- Training Japanese formality classifiers
- Studying linguistic patterns in Japanese business vs casual communication
- Fine-tuning language models for Japanese text classification

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("LiquidAI/yongmin-small_jp_realchat")
```

### Citation

If you use this dataset, please cite:

```
@dataset{yongmin_japanese_realchat_2025,
  title={Japanese Real Chat Dataset},
  author={LiquidAI},
  year={2025},
  url={https://huggingface.co/datasets/LiquidAI/yongmin-small_jp_realchat}
}
```