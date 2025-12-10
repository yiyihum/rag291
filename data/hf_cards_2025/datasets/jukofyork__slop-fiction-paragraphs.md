---
language: en
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.json
license: apache-2.0
task_categories:
- text-generation
size_categories:
- 10M<n<100M
---
# "Slop" Fiction Paragraphs Dataset

This dataset was created by combining:

- [ajibawa-2023/General-Stories-Collection](https://huggingface.co/datasets/ajibawa-2023/General-Stories-Collection)
- [ajibawa-2023/Children-Stories-Collection](https://huggingface.co/datasets/ajibawa-2023/Children-Stories-Collection)

and then splitting by paragraph.

Only non-first and non-final paragraphs (ie: each story's "inner" paragraphs only) between 75 and 2000 characters were then retained in the `"text"` field.

The combined dataset was then de-duplicated and re-shuffled.