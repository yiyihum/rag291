---
dataset_info:
- config_name: WebInstruct-CFT-4K
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 17964182
    num_examples: 4000
  download_size: 7440270
  dataset_size: 17964182
- config_name: WebInstruct-CFT-50K
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 224310117
    num_examples: 50000
  download_size: 93221720
  dataset_size: 224310117
- config_name: WebInstruct-CFT-600K
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 1546662303
    num_examples: 600000
  download_size: 702269217
  dataset_size: 1546662303
configs:
- config_name: WebInstruct-CFT-4K
  data_files:
  - split: train
    path: WebInstruct-CFT-4K/train-*
- config_name: WebInstruct-CFT-50K
  data_files:
  - split: train
    path: WebInstruct-CFT-50K/train-*
- config_name: WebInstruct-CFT-600K
  data_files:
  - split: train
    path: WebInstruct-CFT-600K/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- tigerlab
- math
- cft
---

# WebInstruct-CFT Dataset

This dataset is introduced in our paper [Critique Fine-Tuning: Learning to Critique is More Effective than Learning to Imitate](https://huggingface.co/papers/2501.17703).

| [**🚀Project Page**](https://tiger-ai-lab.github.io/CritiqueFineTuning/) | [**📖Paper**](https://arxiv.org/pdf/2501.17703) | [**🔗Github**](https://github.com/TIGER-AI-Lab/CritiqueFineTuning) | [**🤗7B Model**](https://huggingface.co/TIGER-Lab/Qwen2.5-Math-7B-CFT) | [**🤗32B Model**](https://huggingface.co/TIGER-Lab/Qwen2.5-32B-Instruct-CFT) |

## Overview

WebInstruct-CFT is a critique-based instruction dataset derived from WebInstruct. Unlike traditional instruction datasets that focus on correct answers, our dataset includes critiques of responses, enabling models to learn through critical analysis.

## Dataset Composition

The original WebInstrcut dataset covers diverse topics:
- Mathematics (65%)
- Business (10%) 
- Physics (8%)
- Chemistry (4%)
- Humanities (4%)
- Other topics

We provide three variants:
- `WebInstruct-CFT-600K`: Full version of our dataset
- `WebInstruct-CFT-50K`: Medium-sized subset used to train [Qwen2.5-Math-7B-CFT](https://huggingface.co/TIGER-Lab/Qwen2.5-Math-7B-CFT)
- `WebInstruct-CFT-4K`: Small subset used to train [Qwen2.5-32B-Instruct-CFT](https://huggingface.co/TIGER-Lab/Qwen2.5-32B-Instruct-CFT)

## Data Format

Each example follows this structure:
```json
{
    "instruction": "Please critique whether the following solution to the question is correct.",
    "input": "Question:\n[The original question]\n\nSolution:\n[The original response to be critiqued]",
    "output": "[GPT-4o generated detailed critique of the response]"
}
```

## Citations

```
@misc{wang2025critiquefinetuninglearningcritique,
      title={Critique Fine-Tuning: Learning to Critique is More Effective than Learning to Imitate}, 
      author={Yubo Wang and Xiang Yue and Wenhu Chen},
      year={2025},
      eprint={2501.17703},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.17703}, 
}
```