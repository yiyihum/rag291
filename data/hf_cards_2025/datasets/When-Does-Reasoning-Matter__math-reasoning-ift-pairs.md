---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: reasoning
    dtype: string
  - name: ift
    dtype: string
  splits:
  - name: reasoning_ift_pairs
    num_bytes: 4791272983
    num_examples: 152609
  - name: reasoning
    num_bytes: 4253775427
    num_examples: 152609
  - name: ift
    num_bytes: 582162589
    num_examples: 152609
  download_size: 4299534121
  dataset_size: 9627210999
configs:
- config_name: default
  data_files:
  - split: reasoning_ift_pairs
    path: data/reasoning_ift_pairs-*
  - split: reasoning
    path: data/reasoning-*
  - split: ift
    path: data/ift-*
license: mit
task_categories:
- question-answering
- text-generation
language:
- en
tags:
- math
- instruction-tuning
- reasoning
- synthetic
pretty_name: IFT & Reasoning Paired Math Dataset
size_categories:
- 100K<n<1M
---

# Reasoning-IFT Pairs (Math Domain)

<p align="left">
  <img src="https://cdn-avatars.huggingface.co/v1/production/uploads/62be186a5f59ff2320e6e32b/GjJ15tY7-F4bqR96FN4pd.png" alt="Dataset Icon" width="180"/>
</p>

<p align="left">
<a href="https://arxiv.org/pdf/2509.22193" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/arXiv-2509.22193-b31b1b.svg?style=for-the-badge" alt="arXiv:2509.22193" />
  </a>
</p>

This dataset provides **the largest set of IFT and Reasoning answers pairs** for a set of math queries (cf: [general-domain](https://huggingface.co/datasets/When-Does-Reasoning-Matter/general-reasoning-ift-pairs)).<br>
It is based on the `Llama-Nemotron-Post-Training` dataset, an extensive and high-quality collection of math instruction fine-tuning data.  

We curated **150k queries** from the `math` subset of Llama-Nemotron-Post-Training, which covers multiple domains of math questions.  
For each query, we used [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B), which supports a configurable reasoning flag, to generate two answer formats:  

- **IFT Answer** → concise, direct response
- **Reasoning Answer** → response with reasoning mode enabled (chain-of-thought style)

If you use this dataset in your work, please cite: **[When Does Reasoning Matter?](https://arxiv.org/pdf/2509.22193)**

```bibtex
@misc{boizard2025doesreasoningmattercontrolled,
      title={When Does Reasoning Matter? A Controlled Study of Reasoning's Contribution to Model Performance}, 
      author={Nicolas Boizard and Hippolyte Gisserot-Boukhlef and Kevin El-Haddad and Céline Hudelot and Pierre Colombo},
      year={2025},
      eprint={2509.22193},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.22193}, 
}
```

---

## 📂 Dataset Details

- **Source**: Based on *Llama-Nemotron-Post-Training* (`math` subset)  
- **Size**: ~150k query–answer pairs  
- **Format**: Each entry contains:  
  - `prompt`: input question
  - `reasoning`: synthetic answer with reasoning enabled  
  - `ift`: synthetic answer without reasoning  
- **Model used for generation**: `Qwen/Qwen3-235B-A22B` (open-weight, mixture-of-experts, reasoning toggle)  

---

## 🎯 Research Motivation

Frontier research initiatives highlight the potential of reasoning models, but progress is often confounded by opaque data mixtures and shifting supervision schemes.  
This dataset moves the needle by isolating reasoning itself:

- Using a single teacher model to generate paired IFT and reasoning answers for the same queries, we enable clean attribution of performance improvements specifically to reasoning.  
- This controlled setup avoids reliance on expensive RL pipelines (e.g. Magistral, Qwen3).  
- It facilitates systematic study across model scales and data domains.