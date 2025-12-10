---
base_model: google/t5-v1_1-xxl
base_model_relation: quantized
datasets:
- mit-han-lab/svdquant-datasets
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- text-generation
- AWQ
- Quantization
---
<p align="center" style="border-radius: 10px">
  <img src="https://huggingface.co/datasets/nunchaku-tech/cdn/resolve/main/nunchaku/assets/nunchaku_v2.png" width="30%" alt="Nunchaku Logo"/>
</p>

<div align="center">
  <a href=https://discord.gg/Wk6PnwX9Sm target="_blank"><img src=https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2FWk6PnwX9Sm%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&logo=discord&logoColor=white&label=Discord&color=green&suffix=%20total height=22px></a>
  <a href=https://huggingface.co/datasets/nunchaku-tech/cdn/resolve/main/nunchaku/assets/wechat.jpg target="_blank"><img src=https://img.shields.io/badge/WeChat-07C160?logo=wechat&logoColor=white height=22px></a>
</div>

# Model Card for nunchaku-t5

This repository contains Nunchaku-quantized versions of [T5-XXL](https://huggingface.co/google/t5-v1_1-xxl), used to encode text prompt to the embeddings. It is used to reduce the memory footprint of the model.

## Model Details

### Model Description

- **Developed by:** Nunchaku Team
- **Model type:** text-generation
- **License:** apache-2.0
- **Quantized from model:** [t5_v1_1_xxl](https://huggingface.co/google/t5-v1_1-xxl)

### Model Files

- [`awq-int4-flux.1-t5xxl.safetensors`](./awq-int4-flux.1-t5xxl.safetensors): AWQ quantized W4A16 T5-XXL model for FLUX.1.


### Model Sources

- **Inference Engine:** [nunchaku](https://github.com/nunchaku-tech/nunchaku)
- **Quantization Library:** [deepcompressor](https://github.com/nunchaku-tech/deepcompressor)
- **Paper:** [SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models](http://arxiv.org/abs/2411.05007)
- **Demo:** [svdquant.mit.edu](https://svdquant.mit.edu)

## Usage

- Diffusers Usage: See [flux.1-dev-qencoder.py](https://github.com/nunchaku-tech/nunchaku/blob/main/examples/flux.1-dev-qencoder.py). Check our [tutorial](https://nunchaku.tech/docs/nunchaku/usage/qencoder.html) for more advanced usage.
- ComfyUI Usage: See [nunchaku-flux.1-dev-qencoder.json](https://nunchaku.tech/docs/ComfyUI-nunchaku/workflows/t2i.html#nunchaku-flux-1-dev-qencoder-json).

## Citation

```bibtex
@inproceedings{
  li2024svdquant,
  title={SVDQuant: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models},
  author={Li*, Muyang and Lin*, Yujun and Zhang*, Zhekai and Cai, Tianle and Li, Xiuyu and Guo, Junxian and Xie, Enze and Meng, Chenlin and Zhu, Jun-Yan and Han, Song},
  booktitle={The Thirteenth International Conference on Learning Representations},
  year={2025}
}
@inproceedings{
  lin2023awq,
  title={AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration},
  author={Lin, Ji and Tang, Jiaming and Tang, Haotian and Yang, Shang and Chen, Wei-Ming and Wang, Wei-Chen and Xiao, Guangxuan and Dang, Xingyu and Gan, Chuang and Han, Song},
  booktitle={MLSys},
  year={2024}
}
```