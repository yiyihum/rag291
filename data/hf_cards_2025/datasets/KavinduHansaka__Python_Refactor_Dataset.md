---
license: apache-2.0
task_categories:
- text-generation
language:
- en
size_categories:
- 10K<n<100K
pretty_name: Python Refactor Dataset
tags:
- python
- refactoring
- code-quality
- instruction-tuning
---

# 🧩 Python Refactor Dataset (45k)

### Behavior-Preserving Refactoring Examples for Instruction-Tuning Code Models

This dataset contains **45,000** synthetic Python code refactoring examples designed for
instruction-tuning models such as **IBM Granite 4.0 (micro/h-tiny)** and **Meta CodeLlama-7B-Python**.

Each example demonstrates a **behavior-preserving refactor** — improving code readability,
maintainability, and style (PEP8, type hints, context managers, modularization, etc.)
without altering functionality.

---

## 📦 Dataset Overview

| Field | Description |
|-------|-------------|
| `id` | Unique UUID for each record |
| `task` | Always `"python_refactor"` |
| `instruction` | Natural-language instruction guiding the refactor |
| `constraints` | Optional rules (e.g., "No external dependencies") |
| `input_code` | The unrefactored, original Python snippet |
| `target_code` | The desired refactored version (same behavior) |
| `rationale` | Explanation of why changes were made |
| `language` | Always `"python"` |
| `tags` | List of refactor categories (e.g., `["pep8", "docstring"]`) |
| `granite_prompt` | Formatted input for **Granite** chat-style models |
| `codellama_prompt` | Formatted input for **CodeLlama** instruction-style models |

---

## 🧱 Prompt Format Examples

### Granite
```
<|system|>
You are Granite, a Python code refactoring assistant. Keep behavior identical.
<|user|>
Refactor the following Python code for readability and maintainability.
Constraints: No external dependencies may be added.

```python
def process_numbers(nums):
    s=0
    for i in nums:
        s+=i
    print(s)
```
<|assistant|>
```python
def process_numbers(nums: list[int]) -> None:
    """Print the sum of numbers with PEP8 style."""
    print(sum(nums))
```
```

### CodeLlama
```
[INST] <<SYS>>You are a Python refactoring assistant. Keep behavior identical. Follow PEP8, typing, and docstrings.<</SYS>>
Refactor the following Python code for readability and maintainability.
Constraints: No external dependencies may be added.
```python
def process_numbers(nums):
    s=0
    for i in nums:
        s+=i
    print(s)
```
[/INST]
```python
def process_numbers(nums: list[int]) -> None:
    """Print the sum of numbers with PEP8 style."""
    print(sum(nums))
```
```

---

## ⚙️ Compatibility

| Model Family | Format Field | Recommended Model |
|---------------|---------------|--------------------|
| IBM Granite | `granite_prompt` | `ibm-granite/granite-4.0-micro-base` |
| CodeLlama | `codellama_prompt` | `meta-llama/CodeLlama-7b-Python-hf` |

The dataset is ready for **QLoRA / LoRA** fine-tuning using Hugging Face’s
[`transformers`](https://github.com/huggingface/transformers) and
[`trl`](https://github.com/huggingface/trl) libraries.

---

## 🧠 Example Use (QLoRA)

```bash
python train_codellama_refactor_qlora.py   --model_id meta-llama/CodeLlama-7b-Python-hf   --data_path ./python_refactor_45k.jsonl   --out_dir ./codellama_refactor_lora   --epochs 2 --max_seq_len 2048 --batch_size 1 --grad_accum 8 --lr 2e-4
```

---

## 📊 Statistics

| Metric | Value |
|---------|-------|
| Total samples | 45,000 |
| Avg. input length | ~80 tokens |
| Avg. target length | ~100 tokens |
| Distinct refactor patterns | 10 |
| Average tags per sample | 3.2 |

---

## 🪄 Refactor Categories

- **Style & Naming:** PEP8 spacing, clearer variable names  
- **Structure:** Extract functions, modularize code  
- **Safety:** Add context managers, logging, exception handling  
- **Typing:** Add type hints and docstrings  
- **Pythonic Improvements:** f-strings, list comprehensions, early returns  
- **Immutability:** Avoid in-place mutation when unnecessary  

---

## 🧩 License

This dataset is **synthetically generated** and released under **Apache 2.0 License**.  
You may use, modify, and redistribute it for research or commercial purposes.

---

## 🧭 Citation

If you use this dataset, please cite as:

```
@dataset{python_refactor_45k,
  title     = {Python Refactor Dataset (45k)},
  author    = {Kavindu Jayasinghe and GPT-5 (OpenAI Assistant)},
  year      = {2025},
  license   = {Apache-2.0},
  url       = {https://huggingface.co/datasets/yourname/python-refactor-45k}
}
```

---

## 💡 Recommended Models

| Goal | Model | Notes |
|------|--------|-------|
| Lightweight / fast finetune | **Granite 4.0 micro** | Fits easily on 8 GB GPU |
| High accuracy & deeper context | **CodeLlama-7B-Python** | Requires QLoRA on 8 GB |

---

## 🧰 Next Steps

You can now:
- Split into train/dev/test via `datasets` library:
  ```python
  from datasets import load_dataset
  ds = load_dataset("json", data_files="python_refactor_45k.jsonl")["train"]
  ds = ds.train_test_split(test_size=0.02)
  ```
- Train with the provided QLoRA script.
- Merge the LoRA adapter into base weights using the provided merge utility.
- Quantize to GGUF for inference with llama.cpp or Ollama.

---

**Author:** Kavindu Jayasinghe  
**Generated with:** OpenAI GPT-5  
**Date:** October 2025