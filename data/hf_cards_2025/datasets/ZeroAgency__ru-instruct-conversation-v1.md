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
    num_bytes: 292145052.10901386
    num_examples: 82208
  download_size: 131907315
  dataset_size: 292145052.10901386
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
- chat
- instruct
- russian
- conversational
size_categories:
- 10K<n<100K
---

Combined dataset of mostly Russian dialogs in form of conversations suitable for LLM fine-tuning scenarios.

Total samples: 82208

Deduplicated using simhash(hamming_treshold=3).

Datasets used:
- IlyaGusev/saiga_scored (min_score: 8, no bad by regexp)
- IlyaGusev/oasst2_ru_main_branch
- attn-signs/kolmogorov-3
- attn-signs/russian-easy-instructions