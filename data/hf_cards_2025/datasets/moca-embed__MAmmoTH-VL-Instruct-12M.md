---
license: apache-2.0
language:
- en
size_categories:
- 10M<n<100M
task_categories:
- visual-question-answering
- question-answering
tags:
- reasoning
- CoT
- math
- pretraining
- multimodal
dataset_info:
  features:
  - name: text
    dtype: string
  - name: images
    sequence: binary
  splits:
  - name: train
    num_bytes: 848332512985
    num_examples: 10190972
  download_size: 789093064839
  dataset_size: 848332512985
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# MAmmoTH-VL-Instruct-12M used in MoCa Pre-training

[🏠 Homepage](https://haon-chen.github.io/MoCa/) | [💻 Code](https://github.com/haon-chen/MoCa) | [🤖 MoCa-Qwen25VL-7B](https://huggingface.co/moca-embed/MoCa-Qwen25VL-7B) | [🤖 MoCa-Qwen25VL-3B](https://huggingface.co/moca-embed/MoCa-Qwen25VL-3B) | [📚 Datasets](https://huggingface.co/moca-embed/datasets) | [📄 Paper](https://arxiv.org/abs/2506.23115)

## Introduction

This is a VQA style dataset used in the modality-aware continual pre-training of MoCa models. It is adapted from [MAmmoTH-VL-Instruct-12M](https://huggingface.co/datasets/MAmmoTH-VL/MAmmoTH-VL-Instruct-12M) by concatenating prompts and responses.

The dataset consists of interleaved multimodal examples. `text` is a string containing text while `images` are image binaries that can be loaded with the following code snippet:

```python
import PIL.Image
from io import BytesIO

image_bytes = example['images'][0]
image = PIL.Image.open(BytesIO(image_bytes))
```

## Citation
MoCa

```bibtex
@article{chen2025moca,
  title={MoCa: Modality-aware Continual Pre-training Makes Better Bidirectional Multimodal Embeddings},
  author={Chen, Haonan and Liu, Hong and Luo, Yuping and Wang, Liang and Yang, Nan and Wei, Furu and Dou, Zhicheng},
  journal={arXiv preprint arXiv:2506.23115},
  year={2025}
}
```

MAmmoTH-VL

```bibtex
@article{guo2024mammothvlelicitingmultimodalreasoning,
      title={MAmmoTH-VL: Eliciting Multimodal Reasoning with Instruction Tuning at Scale}, 
      author={Jarvis Guo and Tuney Zheng and Yuelin Bai and Bo Li and Yubo Wang and King Zhu and Yizhi Li and Graham Neubig and Wenhu Chen and Xiang Yue},
      year={2024},
      eprint={2412.05237},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.05237}, 
}
```