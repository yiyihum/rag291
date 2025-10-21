---
license: gpl-3.0
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 10782048942
    num_examples: 214822
  download_size: 5530889398
  dataset_size: 10782048942
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- en
tags:
- biology
size_categories:
- 1B<n<10B
---
