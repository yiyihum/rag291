---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-14B
tags:
- chat
library_name: transformers
---

<p align="left">
  <img src="https://huggingface.co/datasets/whyu/misc/resolve/main/AHN/ahn_logo_horizontal_small.png" width="700">
</p>

# AHN: Artificial Hippocampus Networks for Efficient Long-Context Modeling

<p align="left">
<a href="https://arxiv.org/abs/2510.07318">
  <img src="https://img.shields.io/badge/arXiv-2510.07318-b31b1b?logo=arxiv&logoColor=white&labelColor=555555" />
</a>
<a href="https://github.com/ByteDance-Seed/AHN">
  <img src="https://img.shields.io/badge/GitHub-AHN-181717?logo=github&logoColor=white&labelColor=555555" />
</a>

### Introduction
<p align="left">
  <img src="https://huggingface.co/datasets/whyu/misc/resolve/main/AHN/teaser.png" width="700">
</p>

> Artificial Hippocampus Networks (AHNs) transform lossless memory into fixed-size compressed representations for long-context modeling. Lossless memory (e.g., attention’s key-value (KV) cache) stores exact input information but grows with sequence length, making it inefficient for long sequences. In contrast, compressed memory (e.g., RNNs’ hidden state) maintains a constant size and offers fixed computational costs per input token, but this comes at the cost of information loss. To harness the benefits of both memory types, AHNs continually convert lossless memory outside the sliding attention window into compressed form. AHNs can be instantiated with any RNN-like architectures. The model then integrates both memory types to make predictions across long contexts.

This repository hosts the model weights for AHN. For installation, usage instructions, and further documentation, please visit our [GitHub repository](https://github.com/bytedance-seed/AHN).

### Method
<p align="left">
  <img src="https://huggingface.co/datasets/whyu/misc/resolve/main/AHN/method.png" width="700">
</p>
**(a)** Illustration of the model augmented with Artificial Hippocampus Networks (AHNs). In this example, the sliding window length is 3. When the input sequence length is less than or equal to the window length, the model operates identically to a standard Transformer. For longer sequences, AHNs continually compress the token outside the window into a compact memory representation. The model then utilizes both the lossless information within window, and the compressed memory to generate the next token. **(b)** Self-distillation training framework of AHNs based on an open-weight LLM. During training, the base LLM's weights are frozen, and only the AHNs' parameters are trained.


### Model Zoo
| base model | AHN module | #params | checkpoint (AHN only) |
|:---:|:---:| :---:|:---:|
| Qwen2.5-3B-Instruct | Mamba2 | 119M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-Mamba2-for-Qwen-2.5-Instruct-3B) |
| Qwen2.5-3B-Instruct | DeltaNet | 118M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-DN-for-Qwen-2.5-Instruct-3B) |
| Qwen2.5-3B-Instruct | GatedDeltaNet | 130M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-GDN-for-Qwen-2.5-Instruct-3B) |
| Qwen2.5-7B-Instruct | Mamba2 | 186M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-Mamba2-for-Qwen-2.5-Instruct-7B) |
| Qwen2.5-7B-Instruct | DeltaNet | 185M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-DN-for-Qwen-2.5-Instruct-7B) |
| Qwen2.5-7B-Instruct | GatedDeltaNet | 213M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-GDN-for-Qwen-2.5-Instruct-7B) |
| Qwen2.5-14B-Instruct | Mamba2 | 514M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-Mamba2-for-Qwen-2.5-Instruct-14B) |
| Qwen2.5-14B-Instruct | DeltaNet | 511M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-DN-for-Qwen-2.5-Instruct-14B) |
| Qwen2.5-14B-Instruct | GatedDeltaNet | 610M | [🤗model](https://huggingface.co/ByteDance-Seed/AHN-GDN-for-Qwen-2.5-Instruct-14B) |

### Evaluation

#### LV-Eval & InfiniteBench Results
<p align="left">
  <img src="https://huggingface.co/datasets/whyu/misc/resolve/main/AHN/ultra_long_bmk.png" width="700">
</p>

#### LongBench Results
<p align="left">
  <img src="https://huggingface.co/datasets/whyu/misc/resolve/main/AHN/longbench_bmk.png" width="700">
</p>

## Contact

- Yunhao Fang: yunhao.fang@bytedance.com
- Weihao Yu (corresponding author): weihao.yu@bytedance.com

## Citation

**BibTeX:**

```bibtex
@article{fang2025artificial,
  title={Artificial hippocampus networks for efficient long-context modeling},
  author={Fang, Yunhao and Yu, Weihao and Zhong, Shu and Ye, Qinghao and Xiong, Xuehan and Wei, Lai},
  journal={arXiv preprint arXiv:2510.07318},
  year={2025}
}
```