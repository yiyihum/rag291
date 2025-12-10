---
license: apache-2.0
language:
- en
task_categories:
- text-generation
tags:
- text
- music
- sound-design
- synthesizer
- yamaha-dx7
- text-to-json
- structured-data-generation
- pydantic
- json-schema
- instruction-tuning
- multi-task-learning
- chain-of-thought
- self-correction
- peft
- lora
- mistral
pretty_name: 'Yamaha DX7: A Multi-Task Dataset for Sound Synthesis'
size_categories:
- 10K<n<100K
---

# Yamaha DX7 Synthesizer Patches with AI-Generated Prompts

## Dataset Description

This is a comprehensive, multi-task dataset designed for fine-tuning language models to understand and generate synthesizer patches for the Yamaha DX7.

The dataset contains over 20,000 examples across three distinct but related tasks, making it ideal for creating models that can not only generate patches but also understand and reason about their structure and validity.

## How the Data Was Created

The dataset was built in several stages:
1.  A corpus of over 6,900 unique Yamaha DX7 patches was collected from various online archives.
2.  Each patch was parsed from its original `.syx` format into a valid JSON structure.
3.  A custom script (`fix_source_patches.py`) was used to clean and normalize all data fields to conform to a strict Pydantic schema.
4.  `google/gemma-3-27b-it` model was used in a "Patch-to-Prompt" workflow to generate a creative, descriptive prompt for each of the 6,962 clean patches. This forms the basis of the `dx7_dataset_final.jsonl` file.
5.  Two additional auxiliary datasets were synthetically generated to teach error identification and self-correction.

## Data Fields and File Formats

This repository contains three `.jsonl` files, each corresponding to a different fine-tuning task.

### 1. `dx7_dataset_final.jsonl`
* **Purpose:** Primary text-to-JSON generation task.
* **Structure:** Each line is a JSON object with `{"prompt": "...", "patch": {...}}`.

### 2. `dx7_error_explanation_dataset.jsonl`
* **Purpose:** Auxiliary task for teaching schema violation detection.
* **Structure:** Each line is a JSON object with `{"instruction": "{...invalid_json...}", "response": "Explanation of the error."}`.

### 3. `dx7_self_correction_dataset.jsonl`
* **Purpose:** Auxiliary task for teaching Chain-of-Thought style self-correction.
* **Structure:** Each line is a JSON object with `{"instruction": "Original prompt...", "response": "{\"reasoning\": \"...\", \"patch\": {...corrected_patch...}}"}`.


## Citation

If you use this dataset in your research, please cite it as follows:

```bibtex
@misc{cerati2025dx7,
  author = {Carlo Cerati},
  title = {A Multi-Task Dataset for Yamaha DX7 Patch Generation and Understanding},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{[https://huggingface.co/datasets/ccerati/dx7-patches-and-prompts](https://huggingface.co/datasets/ccerati/dx7-patches-and-prompts)}}
}