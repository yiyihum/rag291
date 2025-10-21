---
license: mit
dataset_info:
  features:
  - name: conversation
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 710695855
    num_examples: 462883
  download_size: 263888496
  dataset_size: 710695855
datasets:
- Vikhrmodels/russian_math
- Vikhrmodels/russian_physics
- d0rj/MathInstruct-ru
- d0rj/orca-math-word-problems-200k-ru
- evilfreelancer/MATH-500-Russian
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ru
tags:
- math
- physics
- conversational
- chat
- instruct
size_categories:
- 100M<n<1B
---

Combined dataset of mostly Russian math and physics tasks in form of conversation suitable for LLM fine-tuning scenarios.

Total samples: 462883

Datasets used:
- Vikhrmodels/russian_math
- Vikhrmodels/russian_physics
- d0rj/MathInstruct-ru
- d0rj/orca-math-word-problems-200k-ru
- evilfreelancer/MATH-500-Russian