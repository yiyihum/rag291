---
language:
- en
license: apache-2.0
size_categories:
- 100M<n<1B
task_categories:
- text-generation
pretty_name: Experimental Pretraining Dataset 1B
dataset_info:
  features:
  - name: text
    dtype: string
  - name: source
    dtype: string
  - name: num_tokens
    dtype: int64
  splits:
  - name: train
    num_bytes: 2247849472
    num_examples: 637270
  download_size: 2247849472
  dataset_size: 2247849472
configs:
- config_name: default
  data_files:
  - split: train
    path: dataset_1b.parquet
tags:
- pretraining
- experimental
- education
- mathematics
- code
- python
---

# Dataset Card for Experimental Pretraining Dataset 1B

## Dataset Details

### Dataset Description

A meticulously curated 1 billion token dataset optimized for experimental pretraining of small language models. This dataset represents a balanced mixture of the highest quality educational content (60%), mathematical reasoning (30%), and Python code (10%), specifically designed for rapid experimentation and research in language model training.

- **Curated by:** Yxanul
- **Language(s):** English
- **License:** Apache 2.0 (see individual source datasets for specific licenses)

### Dataset Sources

The dataset is composed from three high-quality sources:

- **[FineWeb-Edu Highest Quality 2025](https://huggingface.co/datasets/Yxanul/fineweb-edu-highest-quality-2025)** (60%)
- **[CC-Math Finest](https://huggingface.co/datasets/Yxanul/cc-math-finest)** (30%)
- **[Python Finest Pretrain](https://huggingface.co/datasets/Yxanul/python-finest-pretrain)** (10%)

## Uses

### Direct Use

This dataset is intended for:
- Pretraining small language models (100M - 1B parameters)
- Research on training dynamics and curriculum learning
- Educational purposes for understanding LLM training
- Rapid prototyping of training techniques

### Out-of-Scope Use

This dataset is NOT recommended for:
- Production-grade model training (use larger datasets)
- Training models > 1B parameters (insufficient data)
- Fine-tuning (this is a pretraining dataset)

## Dataset Structure

### Data Fields

- `text` (string): The text content for training
- `source` (string): Source category - one of ['fineweb', 'math', 'code']
- `num_tokens` (int64): Pre-computed token count using GPT-2 tokenizer

### Data Splits

| Split | Examples | Tokens | Size |
|-------|----------|--------|------|
| train | 637,270 | 1,000,002,516 | 2.2 GB |

## Dataset Creation

### Curation Rationale

This dataset was created to provide researchers and enthusiasts with a small but high-quality dataset for experimenting with pretraining techniques without requiring massive computational resources. The 60/30/10 distribution was chosen based on research showing this ratio provides good general-purpose capabilities.

### Source Data

All source datasets are publicly available on HuggingFace and represent some of the highest quality filtered content available:

- **Educational Content**: Ultra-filtered web text focused on explanatory and instructional material
- **Mathematics**: Problem-solution pairs with step-by-step reasoning
- **Code**: Production-quality Python with documentation

### Data Collection and Processing

1. Proportional sampling from each source (60/30/10)
2. Length filtering (50-50,000 characters per document)
3. Random shuffling with seed=42
4. Token counting with GPT-2 tokenizer
5. Exact truncation to 1,000,002,516 tokens

### Personal and Sensitive Information

The dataset has been filtered through the original source datasets' cleaning processes. No additional PII removal was performed.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset is designed for educational and research purposes. Users should be aware that models trained on this data may reflect biases present in web text, mathematical content, and code repositories.

### Discussion of Biases

The dataset may contain:
- Geographic and cultural biases from web content
- Programming style biases from Python repositories  
- Mathematical notation preferences from educational sources

### Other Known Limitations

- Limited to English language content
- Python-only for code (no other programming languages)
- May not represent the full diversity needed for general-purpose models

## Additional Information

### Dataset Curators

Yxanul

### Licensing Information

This compilation is released under Apache 2.0. Individual components have their own licenses:
- FineWeb-Edu: ODC-By 1.0
- CC-Math: MIT  
- Python-Finest: Apache 2.0

### Citation Information

```bibtex
@dataset{experimental_pretrain_1b_2025,
  author = {Yxanul},
  title = {Experimental Pretraining Dataset 1B},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/datasets/Yxanul/experimental-pretrain-1b}
}
```

### Contributions

Thanks to the open-source community for making high-quality datasets available for research and experimentation.