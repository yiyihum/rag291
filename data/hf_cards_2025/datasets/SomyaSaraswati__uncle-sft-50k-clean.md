---
pretty_name: Uncle SFT 50k (clean)
language:
- en
task_categories:
- text-generation
size_categories:
- 10K<n<100K
license: cc-by-4.0
tags:
- instruction-tuning
- career-advice
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 32901349.0
    num_examples: 49000
  - name: validation
    num_bytes: 671639.0
    num_examples: 1000
  download_size: 522950
  dataset_size: 33572988.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
---

# Uncle SFT 50k (clean)

Cleaned version of `SomyaSaraswati/uncle-sft-50k`:
- Ensured assistant turns end with `<|eot_id|>`
- Removed looping / mantra-like samples
- De-duplicated near-identical entries

Splits:
- train: 0
- validation: 0
