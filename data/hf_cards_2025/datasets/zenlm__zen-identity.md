---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- zen
- identity
- instruction-tuning
size_categories:
- n<1K
---

# Zen Identity Dataset

This dataset contains identity training data for the Zen family of AI models.

## Models Covered

- **Zen Nano (0.6B)**: Ultra-efficient edge computing model
- **Zen Eco (3B)**: Balanced performance and efficiency
- **Zen Coder (7B)**: Specialized for code generation
- **Zen Omni (14B)**: Versatile multi-domain model

## Dataset Structure

Each example contains:
- `instruction`: The user's question
- `output`: The model's response
- `model`: Which Zen model this example is for
- `text`: Full conversation format (Human/Assistant)

## Usage

```python
from datasets import load_dataset

# Load full dataset
dataset = load_dataset("zenlm/zen-identity")

# Load model-specific data
zen_nano_data = dataset.filter(lambda x: x["model"] == "zen-nano")
```

## Files

- `train.jsonl`: Complete dataset for all models
- `zen-nano_train.jsonl`: Zen Nano specific examples
- `zen-eco_train.jsonl`: Zen Eco specific examples  
- `zen-coder_train.jsonl`: Zen Coder specific examples
- `zen-omni_train.jsonl`: Zen Omni specific examples

## License

Apache 2.0
