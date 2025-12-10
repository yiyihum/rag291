---
license: cc-by-sa-4.0
task_categories:
- question-answering
- text-generation
language:
- en
tags:
- machine-unlearning
- entity-level-unlearning
- llm-safety
- privacy
- wikipedia
- entity
- unlearning
- LLM
- NLP
size_categories:
- 100K<n<1M
configs:
- config_name: forget_qa
  data_files: forget_qa-train.parquet
- config_name: retain_qa
  data_files:
  - split: train
    path: retain_qa-train.parquet
  - split: validation
    path: retain_qa-validation.parquet
  - split: test
    path: retain_qa-test.parquet
---

# ELUDe: Entity-Level Unlearning Dataset

**ELUDe (Entity-Level Unlearning Dataset)** is a comprehensive machine unlearning dataset focused on the removal of an entire entity from large language models (LLMs).
The dataset includes 20 real-world target entities and 144 unique neighboring entities from Wikipedia. All samples were synthesized by GPT-4o, given the Wikipedia documents of the entities.

## Quick Links

- **Paper:** [Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport](https://arxiv.org/abs/2406.12329)
- **Code:** [https://github.com/brightjade/Opt-Out](https://github.com/brightjade/Opt-Out)

## Usage

```python
from datasets import load_dataset

# Load specific subsets and splits
forget_train = load_dataset("6rightjade/ELUDe", "forget_qa", split="train")
retain_train = load_dataset("6rightjade/ELUDe", "retain_qa", split="train")
retain_val = load_dataset("6rightjade/ELUDe", "retain_qa", split="validation")
retain_test = load_dataset("6rightjade/ELUDe", "retain_qa", split="test")
```

## Ethical Considerations

- The dataset includes some controversial figures for research purposes
- Should be used responsibly for advancing privacy-preserving AI
- Not intended for actual deployment without proper safeguards

## Citation

If you use this dataset, please cite our paper:

```bibtex
@article{choi2025optout,
  title={Opt-Out: Investigating Entity-Level Unlearning for Large Language Models via Optimal Transport},
  author={Choi, Minseok and Rim, Daniel and Lee, Dohyun and Choo, Jaegul},
  journal={arXiv preprint arXiv:2406.12329},
  year={2025}
}
```