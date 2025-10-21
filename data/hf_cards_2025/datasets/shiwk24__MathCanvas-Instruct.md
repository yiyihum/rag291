---
language:
- en
license: apache-2.0
task_categories:
- image-text-to-text
tags:
- mathematics
- multimodal-reasoning
- visual-chain-of-thought
- vcot
- instruction-tuning
- generative-ai
- computer-vision
configs:
- config_name: default
  data_files:
  - split: Algebra
    path: data/Algebra-*
  - split: Analytic_Geometry
    path: data/Analytic_Geometry-*
  - split: Calculus_and_Vector
    path: data/Calculus_and_Vector-*
  - split: Plane_Geometry
    path: data/Plane_Geometry-*
  - split: Solid_Geometry
    path: data/Solid_Geometry-*
  - split: Statistics
    path: data/Statistics-*
  - split: Transformational_Geometry
    path: data/Transformational_Geometry-*
  - split: Trigonometry
    path: data/Trigonometry-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: options
    list:
    - name: letter
      dtype: string
    - name: value
      dtype: string
  - name: answer
    dtype: string
  - name: question_interleave
    list:
    - name: content
      dtype: string
    - name: index
      dtype: int64
    - name: type
      dtype: string
  - name: solution_interleave
    list:
    - name: content
      dtype: string
    - name: index
      dtype: int64
    - name: type
      dtype: string
  - name: question_images
    list: image
  - name: solution_images
    list: image
  - name: knowledge
    dtype: string
  - name: subknowledge
    dtype: string
  splits:
  - name: Algebra
    num_bytes: 1961863324
    num_examples: 21600
  - name: Analytic_Geometry
    num_bytes: 3855307634
    num_examples: 42199
  - name: Calculus_and_Vector
    num_bytes: 298930623
    num_examples: 3270
  - name: Plane_Geometry
    num_bytes: 9660398949
    num_examples: 106685
  - name: Solid_Geometry
    num_bytes: 3322191291
    num_examples: 36457
  - name: Statistics
    num_bytes: 170763055
    num_examples: 1872
  - name: Transformational_Geometry
    num_bytes: 58147045
    num_examples: 645
  - name: Trigonometry
    num_bytes: 532053077
    num_examples: 5876
  download_size: 21166209339
  dataset_size: 19859654998
---

# MathCanvas-Instruct Dataset

<p align="center">
  <a href="https://arxiv.org/pdf/2510.14958" target="_blank">
    <img src="https://img.shields.io/badge/Paper-PDF-b31b1b.svg" alt="Paper PDF">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://mathcanvas.github.io/" target="_blank">
    <img src="https://img.shields.io/badge/Project-Page-blue.svg" alt="Project Page">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/shiwk24/MathCanvas" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Code-green.svg" alt="GitHub Code">
  </a>
</p>

## 📖 Overview

**MathCanvas-Instruct** is a high-quality, fine-tuning dataset with 219K examples of interleaved visual-textual reasoning paths. It is the core component for the second phase of the **[MathCanvas]** framework: **Strategic Visual-Aided Reasoning**.

After a model learns foundational diagram generation and editing from `MathCanvas-Imagen` and `MathCanvas-Edit`, this dataset teaches it the crucial next step: **when** and **how** to strategically leverage visual aids to solve complex mathematical problems. Each sample in `MathCanvas-Instruct` provides a complete reasoning trace, demonstrating how a model can generate intermediate diagrams as part of its chain of thought, mimicking the problem-solving process of a human expert.

For more technical details on our data curation process, please refer to our [[paper]](https://arxiv.org/pdf/2510.14958). For guidance on using this dataset for model training, please see our [[GitHub repository]](https://github.com/shiwk24/MathCanvas).

## 📊 Dataset Statistics

The dataset is carefully curated to cover a wide range of mathematical domains and problem structures, ensuring a robust and comprehensive fine-tuning process.

<p align="left">
  <img src="instruct_stat.jpg" width="30%">
  <!-- <br> -->
  <em>Distribution of knowledge type of MathCanvas-Instruct dataset.</em>
</p>

The table below provides a detailed breakdown of the dataset's statistics:

| Statistic                         | Value      |
|:----------------------------------|:-----------|
| **Total Samples**                 | **218,604**|
| **Question Modality**             |            |
| &nbsp;&nbsp;&nbsp;&nbsp;Text questions  | 35%        |
| &nbsp;&nbsp;&nbsp;&nbsp;Multimodal questions | 65%        |
| **Sub-question Distribution**     |            |
| &nbsp;&nbsp;&nbsp;&nbsp;One question   | 68%        |
| &nbsp;&nbsp;&nbsp;&nbsp;Two sub-questions  | 18%        |
| &nbsp;&nbsp;&nbsp;&nbsp;Three sub-questions| 12%        |
| &nbsp;&nbsp;&nbsp;&nbsp;Four or more     | 2%         |
| **Question Length (text tokens)** |            |
| &nbsp;&nbsp;&nbsp;&nbsp;Average          | 107.92     |
| &nbsp;&nbsp;&nbsp;&nbsp;Maximum          | 466        |
| **Solution Length (text tokens)** |            |
| &nbsp;&nbsp;&nbsp;&nbsp;Average          | 539.66     |
| &nbsp;&nbsp;&nbsp;&nbsp;Maximum          | 2001       |
| **Images in Multimodal Question** |            |
| &nbsp;&nbsp;&nbsp;&nbsp;Average          | 1.03       |
| &nbsp;&nbsp;&nbsp;&nbsp;Maximum          | 5          |
| **Images in Solution**            |            |
| &nbsp;&nbsp;&nbsp;&nbsp;Average          | 1.18       |
| &nbsp;&nbsp;&nbsp;&nbsp;Maximum          | 5          |

## 📜 Citation

If you find our work useful, please consider citing us!

```bibtex
@misc{shi2025mathcanvasintrinsicvisualchainofthought,
      title={MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning}, 
      author={Weikang Shi and Aldrich Yu and Rongyao Fang and Houxing Ren and Ke Wang and Aojun Zhou and Changyao Tian and Xinyu Fu and Yuxuan Hu and Zimu Lu and Linjiang Huang and Si Liu and Rui Liu and Hongsheng Li},
      year={2025},
      eprint={2510.14958},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.14958}, 
}
```