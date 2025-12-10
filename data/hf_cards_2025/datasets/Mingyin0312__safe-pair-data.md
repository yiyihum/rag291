---
pretty_name: Safe Pair Data
license: apache-2.0
language:
- en
tags:
- rlhf
- preferences
task_categories:
- text-classification
source_datasets:
- PKU-Alignment/PKU-SafeRLHF-30K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 3834097
    num_examples: 5125
  - name: test
    num_bytes: 424062
    num_examples: 561
  download_size: 2470601
  dataset_size: 4258159
---

# Safe Pair Data

A locally curated dataset with `train` and `test` splits for preference-based training.
This is a filtered subset of **PKU-Alignment/PKU-SafeRLHF-30K**.

## Usage

    from datasets import load_dataset
    ds = load_dataset('Mingyin0312/safe-pair-data')
    print(ds)

## Splits
- `train/`
- `test/`

## Notes
- Saved with `datasets.save_to_disk`; reloadable via `load_from_disk`.
