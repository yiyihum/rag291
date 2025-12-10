---
language:
- en
license: apache-2.0
tags:
- code-generation
- documentation
- codet5
- ai-assistant
- developer-tools
pipeline_tag: text-generation
library_name: transformers
base_model: Salesforce/codet5-small
datasets:
- custom
metrics:
- bleu
- rouge
---


# AutoDocGen 🧠 — AI Code Documentation & Test Generator

AutoDocGen is an advanced model built on **CodeT5** that automatically generates
documentation, comments, and unit tests for source code files.

---
### 🚀 Features
- Auto-generate docstrings for Python functions
- Create unit tests from given functions
- Trainable and extendable on custom datasets

---
### 📦 Files
- `train_codet5_docgen.py` — training script
- `inference.py` — run doc generation on your code
- `cli.py` — command-line interface
- `configs/train_config.json` — training parameters
- `data_examples/` — contains example dataset and code
- `tests/` — unit test folder

---
### 🧠 Model Description
This model fine-tunes **CodeT5-small** from Hugging Face Transformers
on a dataset of Python code and natural language descriptions.

---
### ⚖️ License
Licensed under the **Apache License 2.0**.
