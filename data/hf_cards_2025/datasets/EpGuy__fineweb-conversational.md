---
license: odc-by
source_datasets:
- HuggingFaceFW/fineweb
task_categories:
- text-generation
language:
- en
tags:
- conversational
- instruct
- chat
- synthetic
size_categories:
- 1K<n<10K
pretty_name: FineWeb-Conversational
configs:
- config_name: default
  data_files:
  - split: train
    path: data.parquet
---

# Dataset Card for fineweb-conversational

---

## 1. Dataset Overview

**fineweb-conversational** is a dataset crafted for training conversational AI models in an instruction-following format. It transforms cleaned and deduplicated English web data from the [FineWeb dataset](https://huggingface.co/datasets/HuggingFaceFW/fineweb) into a prompt-completion structure. The dataset is curated by [me, a.k.a EpGuy](https://huggingface.co/EpGuy), is under an **odc-by** license, and is still in active development with periodic updates.

---

## 2. Structure & Creation Process

The data is provided in CSV format with two main columns:  
- **prompt:** An AI-generated text that simulates a user query, created using Google's Gemini 2.0 Flash model.  
- **completion:** The original text from the FineWeb dataset intended as the response.

The creation process involves a Python script that:
- Uses a meta-prompt to instruct Gemini 2.0 Flash to generate natural, open-ended prompts.
- Associates these generated prompts with corresponding completions sourced directly from FineWeb, which itself is derived from CommonCrawl (2013-2024).

---

## 3. Usage, Limitations & Citations

**Usage:**  
This dataset is primarily for fine-tuning large language models for conversational tasks and instruction following.

**Considerations & Limitations:**  
- **Biases:** Inherits societal biases and potential toxic content from its web-sourced data.
- **AI-Generated Prompts:** The prompt generation process might occasionally yield unrealistic or misaligned queries.
- **Incomplete Data:** The dataset is not final; updates will continue as more data is processed.
- **Sensitive Information:** Some Personal and Sensitive Information (PII) may remain despite anonymization efforts.

**Citation:**  
If you use the dataset, please cite the original FineWeb dataset (you should only use this dataset as a footnote):
```bibtex
@inproceedings{
  penedo2024the,
  title={The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale},
  author={Guilherme Penedo and Hynek Kydl{\'\i}{\v{c}}ek and Loubna Ben allal and Anton Lozhkov and Margaret Mitchell and Colin Raffel and Leandro Von Werra and Thomas Wolf},
  booktitle={The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2024},
  url={https://openreview.net/forum?id=n6SCkn2QaG}
}
```