---
license: apache-2.0
language:
- en
metrics:
- accuracy
pipeline_tag: image-text-to-text
task_categories:
- question-answering
- multiple-choice
- visual-question-answering
- text-generation
dataset_info:
- config_name: MM-MathInstruct
  features:
  - name: id
    dtype: int64
  - name: image
    dtype: image
  - name: question
    dtype: string
  - name: solution
    dtype: string
  - name: image_path
    dtype: string
configs:
- config_name: MM-MathInstruct
  data_files:
  - split: train0
    path: train-00000*
  - split: train1
    path: train-00001*
  - split: train2
    path: train-00002*
  - split: train3
    path: train-00003*
  - split: train4
    path: train-00004*
  - split: train5
    path: train-00005*
  - split: train6
    path: train-00006*
  - split: train7
    path: train-00007*
  - split: train8
    path: train-00008*
  - split: train9
    path: train-00009*
tags:
- mathematics
- reasoning
- multi-modal-qa
- math-qa
- figure-qa
- geometry-qa
- math-word-problem
- textbook-qa
- vqa
- geometry-diagram
- synthetic-scene
- chart
- plot
- scientific-figure
- table
- function-plot
- abstract-scene
- puzzle-test
- document-image
- science
size_categories:
- 1M<n<10M
---
# MathCoder-VL: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning

Repo: [https://github.com/mathllm/MathCoder](https://github.com/mathllm/MathCoder)

Paper: [https://huggingface.co/papers/2505.10557](https://huggingface.co/papers/2505.10557)


## Introduction
We introduce MathCoder-VL, a series of open-source large multimodal models (LMMs) specifically tailored for general math problem-solving. We also introduce [FigCodifier-8B](https://huggingface.co/MathLLMs/FigCodifier), an image-to-code model.

| Base Model                                          	|Ours                                               |
|-------------------------------------------------------------------|-----------------------------------------------------------------------|
|  [Mini-InternVL-Chat-2B-V1-5](https://huggingface.co/OpenGVLab/Mini-InternVL-Chat-2B-V1-5)  |  [MathCoder-VL-2B](https://huggingface.co/MathLLMs/MathCoder-VL-2B)   	|
|  [InternVL2-8B](https://huggingface.co/OpenGVLab/InternVL2-8B)  |     	[MathCoder-VL-8B](https://huggingface.co/MathLLMs/MathCoder-VL-8B)|
|  [InternVL2-8B](https://huggingface.co/OpenGVLab/InternVL2-8B)  |     	[FigCodifier-8B](https://huggingface.co/MathLLMs/FigCodifier)|



## Usage
For training and inference code, please refer to [InternVL](https://github.com/OpenGVLab/InternVL).

```
from datasets import load_dataset
from PIL import Image
from io import BytesIO

mm_mathinstruct = load_dataset("MathLLMs/MM-MathInstruct")
print(mm_mathinstruct)

# show the last image
img = Image.open(BytesIO(mm_mathinstruct['train'][-1]['image']))
img.show()
```

It should print:
```
DatasetDict({
    train: Dataset({
        features: ['id', 'image', 'question', 'solution', 'image_path'],
        num_rows: 2871988
    })
})
```


## Motivation

<div align="center">
  <img src="./examples/fig1.png" width="100%" title="Result Figure">
</div>

## Construction of FigCodifier

<div align="center">
  <img src="./examples/fig2.png" width="100%" title="Result Figure">
</div>

## Construction of MathCoder-VL

<div align="center">
  <img src="./examples/fig4.png" width="100%" title="Result Figure">
</div>

## Performance

<div align="center">
  <img src="./examples/tab1.png" width="100%" title="Result Figure">
</div>

## **Citation**

Please cite the paper if you use our data, model or code.

```
@inproceedings{
wang2025mathcodervl,
title={MathCoder-{VL}: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning},
author={Ke Wang and Junting Pan and Linda Wei and Aojun Zhou and Weikang Shi and Zimu Lu and Han Xiao and Yunqiao Yang and Houxing Ren and Mingjie Zhan and Hongsheng Li},
booktitle={The 63rd Annual Meeting of the Association for Computational Linguistics},
year={2025},
url={https://openreview.net/forum?id=nuvtX1imAb}
}
```

```
@inproceedings{
wang2024mathcoder,
title={MathCoder: Seamless Code Integration in {LLM}s for Enhanced Mathematical Reasoning},
author={Ke Wang and Houxing Ren and Aojun Zhou and Zimu Lu and Sichun Luo and Weikang Shi and Renrui Zhang and Linqi Song and Mingjie Zhan and Hongsheng Li},
booktitle={The Twelfth International Conference on Learning Representations},
year={2024},
url={https://openreview.net/forum?id=z8TW0ttBPp}
}
```