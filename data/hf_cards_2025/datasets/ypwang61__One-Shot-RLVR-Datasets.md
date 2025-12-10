---
license: apache-2.0
dataset_info:
  features:
  - name: data_source
    dtype: string
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: ability
    dtype: string
  - name: reward_model
    struct:
    - name: ground_truth
      dtype: string
    - name: style
      dtype: string
  - name: extra_info
    struct:
    - name: index
      dtype: int64
    - name: split
      dtype: string
  splits:
  - name: pi1
    num_bytes: 61568
    num_examples: 128
  - name: pi2
    num_bytes: 25472
    num_examples: 128
  - name: pi13
    num_bytes: 49152
    num_examples: 128
  - name: pi1209
    num_bytes: 67328
    num_examples: 128
  - name: merge_pi1_pi13
    num_bytes: 55360
    num_examples: 128
  - name: merge_pi1_pi2_pi13_pi1209_r128
    num_bytes: 50880
    num_examples: 128
  - name: dsr_sub
    num_bytes: 475872
    num_examples: 1209
  download_size: 243791
  dataset_size: 785632
configs:
- config_name: default
  data_files:
  - split: pi1
    path: data/pi1-*
  - split: pi2
    path: data/pi2-*
  - split: pi13
    path: data/pi13-*
  - split: pi1209
    path: data/pi1209-*
  - split: merge_pi1_pi13
    path: data/merge_pi1_pi13-*
  - split: merge_pi1_pi2_pi13_pi1209_r128
    path: data/merge_pi1_pi2_pi13_pi1209_r128-*
  - split: dsr_sub
    path: data/dsr_sub-*
task_categories:
- text-generation
---




This repository contains the dataset presented in [Reinforcement Learning for Reasoning in Large Language Models with One Training Example](https://huggingface.co/papers/2504.20571).

Code: https://github.com/ypwang61/One-Shot-RLVR