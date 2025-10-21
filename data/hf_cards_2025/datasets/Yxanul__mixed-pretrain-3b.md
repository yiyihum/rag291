---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- pretraining
- mathematics
- code
- education
size_categories:
- 1B<n<10B
pretty_name: Mixed Pretraining Dataset 3B
configs:
- config_name: default
  data_files:
  - split: train
    path: '*.parquet'
---

# Mixed Pretraining Dataset (3B Tokens)

A carefully curated and mixed pretraining dataset containing 3 billion tokens from high-quality educational, mathematical, and programming sources.

## Dataset Description

This dataset combines three high-quality data sources with specific proportions optimized for language model pretraining:

- **60% FineWeb-Edu** (1.8B tokens): High-quality educational web content
- **30% Mathematics** (900M tokens): Mathematical problems, solutions, and explanations  
- **10% Python Code** (300M tokens): Well-documented Python implementations

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Tokens** | 3,000,000,000 |
| **Total Samples** | 2,527,528 |
| **File Size** | 5.7 GB |
| **Format** | Parquet (Snappy compression) |
| **Tokenizer** | cl100k_base (GPT-4) |

### Token Distribution

| Source | Tokens | Percentage | Samples |
|--------|--------|------------|---------|
| FineWeb-Edu | 1,800,000,000 | 60.0% | ~750,000 |
| Mathematics | 900,000,000 | 30.0% | ~1,650,000 |
| Python Code | 300,000,000 | 10.0% | ~127,000 |

## Dataset Structure

Each sample contains three fields:

```python
{
    "text": str,           # The actual text content
    "token_count": int,    # Number of tokens (cl100k_base tokenizer)
    "source": str          # Source identifier: "fineweb_edu", "math", or "code"
}
```

### Sample Characteristics

| Source | Avg Tokens/Sample | Avg Chars/Sample | Token/Char Ratio |
|--------|------------------|------------------|------------------|
| FineWeb-Edu | ~2,400 | ~9,600 | 0.25 |
| Mathematics | ~545 | ~1,800 | 0.30 |
| Python Code | ~2,360 | ~6,750 | 0.35 |

## Usage

### Loading with Datasets Library

```python
from datasets import load_dataset

# Load the entire dataset
dataset = load_dataset("Yxanul/mixed-pretrain-3b")

# Load with streaming for memory efficiency
dataset = load_dataset("Yxanul/mixed-pretrain-3b", streaming=True)

# Access samples
for sample in dataset['train']:
    print(f"Source: {sample['source']}")
    print(f"Tokens: {sample['token_count']}")
    print(f"Text preview: {sample['text'][:200]}...")
    break
```

### Loading with Pandas

```python
import pandas as pd

# Load the entire dataset
df = pd.read_parquet("mixed_dataset_3b.parquet")

# Load specific columns
df = pd.read_parquet("mixed_dataset_3b.parquet", columns=['text', 'source'])

# Sample by source
math_samples = df[df['source'] == 'math']
code_samples = df[df['source'] == 'code']
```

### PyTorch DataLoader Example

```python
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class PretrainingDataset(Dataset):
    def __init__(self, parquet_path):
        self.df = pd.read_parquet(parquet_path)
    
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        return {
            'text': row['text'],
            'token_count': row['token_count'],
            'source': row['source']
        }

dataset = PretrainingDataset("mixed_dataset_3b.parquet")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

## Data Sources

### FineWeb-Edu
- **Source**: FineWeb-Edu Highest Quality 2025
- **Description**: Curated educational content from Common Crawl
- **Processing**: Filtered for high educational value

### Mathematics Dataset
- **Source**: High-quality mathematical problems and solutions
- **Content**: Algebra, calculus, geometry, statistics
- **Format**: Step-by-step solutions and explanations

### Python Code Dataset
- **Source**: Curated Python implementations
- **Content**: Functions, classes, algorithms
- **Quality**: Well-documented code with docstrings

## Dataset Creation Process

1. **Token Counting**: Used approximate token counting (character-based ratios) for speed
2. **Proportional Sampling**: Extracted exact token counts per source
3. **Shuffling**: Random shuffling ensures good mixing across the dataset
4. **Compression**: Snappy compression for efficient storage

## Intended Use

This dataset is designed for:
- Pretraining language models
- Fine-tuning on educational content
- Multi-task learning across domains
- Research on curriculum learning

## Limitations

- English language only
- Token counts are approximate (±5% variance)
- Some FineWeb-Edu samples may be truncated
- Python code is the primary programming language

## License

Apache 2.0

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{mixed_pretrain_3b_2024,
  title={Mixed Pretraining Dataset 3B},
  author={Yxanul},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Yxanul/mixed-pretrain-3b}
}
```

## Acknowledgments

- FineWeb-Edu team for high-quality educational content
- Original dataset creators for math and code content
- Hugging Face for hosting infrastructure