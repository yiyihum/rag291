---
task_categories:
- robotics
library_name: rlds
tags:
- vision-language-action
- instruction-tuning
- manipulation
- embodied-ai
- benchmark
---

This repository contains the **VLA-IT dataset**, a curated 650K-sample Vision-Language-Action Instruction Tuning dataset, and the **SimplerEnv-Instruct** benchmark. These are presented in the paper [InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation](https://huggingface.co/papers/2507.17520). The dataset is designed to enable robots to integrate multimodal reasoning with precise action generation, preserving the flexible reasoning of large vision-language models while delivering leading manipulation performance.

Project Page: https://yangs03.github.io/InstructVLA_Home/
Code: https://github.com/InternRobotics/InstructVLA

# Using the VLA-IT Dataset and Benchmark

***Update 25/9/11***: We upload a data loading example, `data_loading_example.ipynb`, which shows how to get a single episode with the corresponding VLA-IT annotation.

## 1. Install Customized `ManiSkill2_real2sim`

To ensure compatibility with our evaluation setup, please replace the default `ManiSkill2_real2sim` in [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) with the customized version available at:

**Repository:** [YangS03/my_maniskill](https://github.com/YangS03/my_maniskill)
 **Evaluation Scripts:** [scripts directory](https://github.com/YangS03/my_maniskill/tree/main/scripts)

## 2. Modify RLDS Dataloader for Fractal Dataset

The original Fractal dataset lacks unique episode IDs. To address this, we adapt it to follow the format used in ECoT, enabling consistent reasoning indexing across both Bridge and Fractal datasets.

You can refer to the modified dataloader here:
 [Modified RLDS Dataloader](https://github.com/MichalZawalski/embodied-CoT/blob/1813ad76001f1e08095088f94a86c43fc0e457a3/prismatic/vla/datasets/rlds/dataset.py#L157)
