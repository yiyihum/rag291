---
license: cc-by-4.0
language:
- en
size_categories:
- 10M<n<100M
tags:
- pretraining
- text
dataset_info:
  features:
  - name: text
    dtype: string
  - name: images
    sequence: 'null'
  splits:
  - name: train
    num_bytes: 116521171921
    num_examples: 20582647
  download_size: 71520997481
  dataset_size: 116521171921
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# DCLM used in MoCa Pre-training

[🏠 Homepage](https://haon-chen.github.io/MoCa/) | [💻 Code](https://github.com/haon-chen/MoCa) | [🤖 MoCa-Qwen25VL-7B](https://huggingface.co/moca-embed/MoCa-Qwen25VL-7B) | [🤖 MoCa-Qwen25VL-3B](https://huggingface.co/moca-embed/MoCa-Qwen25VL-3B) | [📚 Datasets](https://huggingface.co/moca-embed/datasets) | [📄 Paper](https://arxiv.org/abs/2506.23115)

## Introduction

This is a text pre-training dataset used in the modality-aware continual pre-training of MoCa models. It is adapted from [DCLM](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0-parquet) and randomly downsampled to ~20B tokens.

The dataset consists of text examples. `text` is a string containing text while `images` are left blank intentionally since there is no image available.



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

DCLM

```bibtex
@misc{li2024datacomplm,
      title={DataComp-LM: In search of the next generation of training sets for language models}, 
      author={Jeffrey Li and Alex Fang and Georgios Smyrnis and Maor Ivgi and Matt Jordan and Samir Gadre and Hritik Bansal and Etash Guha and Sedrick Keh and Kushal Arora and Saurabh Garg and Rui Xin and Niklas Muennighoff and Reinhard Heckel and Jean Mercat and Mayee Chen and Suchin Gururangan and Mitchell Wortsman and Alon Albalak and Yonatan Bitton and Marianna Nezhurina and Amro Abbas and Cheng-Yu Hsieh and Dhruba Ghosh and Josh Gardner and Maciej Kilian and Hanlin Zhang and Rulin Shao and Sarah Pratt and Sunny Sanyal and Gabriel Ilharco and Giannis Daras and Kalyani Marathe and Aaron Gokaslan and Jieyu Zhang and Khyathi Chandu and Thao Nguyen and Igor Vasiljevic and Sham Kakade and Shuran Song and Sujay Sanghavi and Fartash Faghri and Sewoong Oh and Luke Zettlemoyer and Kyle Lo and Alaaeldin El-Nouby and Hadi Pouransari and Alexander Toshev and Stephanie Wang and Dirk Groeneveld and Luca Soldaini and Pang Wei Koh and Jenia Jitsev and Thomas Kollar and Alexandros G. Dimakis and Yair Carmon and Achal Dave and Ludwig Schmidt and Vaishaal Shankar},
      year={2024},
      eprint={2406.11794},
      archivePrefix={arXiv},
      primaryClass={id='cs.LG' full_name='Machine Learning' is_active=True alt_name=None in_archive='cs' is_general=False description='Papers on all aspects of machine learning research (supervised, unsupervised, reinforcement learning, bandit problems, and so on) including also robustness, explanation, fairness, and methodology. cs.LG is also an appropriate primary category for applications of machine learning methods.'}
```

