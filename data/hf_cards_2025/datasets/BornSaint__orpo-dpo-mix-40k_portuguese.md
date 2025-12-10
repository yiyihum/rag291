---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: source
    dtype: string
  - name: chosen
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 169105230
    num_examples: 44245
  download_size: 87715945
  dataset_size: 169105230
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- dpo
- rlhf
- preference
- orpo
language:
- pt
---

# Portuguese translation of [`mlabonne/orpo-dpo-mix-40k`](https://huggingface.co/datasets/mlabonne/orpo-dpo-mix-40k)


# How it was made?
I have used a ctranslate2 version of [`google/madlad400-3b-mt`](https://huggingface.co/google/madlad400-3b-mt) quantized in int8_f16

Took more than a week to translate all in a single thread using RTX 3060 12GB

# Whats next?
Using the same model to translate [`cognitivecomputations/Wizard-Vicuna-7B-Uncensored`](https://huggingface.co/cognitivecomputations/Wizard-Vicuna-7B-Uncensored)

But now I'm using 3 threads, 1 model each.

# Plans
I'm focusing in datasets that can be useful for my future finetunes. 

The goal is to align a model without any censoring.

The following are my 2 small datasets I plan to use for this purpose.

- [`BornSaint/D33_590d`](https://huggingface.co/datasets/BornSaint/D33_590d)
  
- [`BornSaint/D33_alignment`](https://huggingface.co/datasets/BornSaint/D33_alignment)
  

# Below is the original README.md

## ORPO-DPO-mix-40k v1.2

![image/webp](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/s3uIwTgVl1sTm5_AX3rXH.webp)

This dataset is designed for [ORPO](https://huggingface.co/docs/trl/main/en/orpo_trainer#expected-dataset-format) or [DPO](https://huggingface.co/docs/trl/main/en/dpo_trainer#expected-dataset-format) training.
See [Fine-tune Llama 3 with ORPO](https://huggingface.co/blog/mlabonne/orpo-llama-3) for more information about how to use it.
It is a combination of the following high-quality DPO datasets:

- [`argilla/Capybara-Preferences`](https://huggingface.co/datasets/argilla/Capybara-Preferences): highly scored chosen answers >=5 (7,424 samples)
- [`argilla/distilabel-intel-orca-dpo-pairs`](https://huggingface.co/datasets/argilla/distilabel-intel-orca-dpo-pairs): highly scored chosen answers >=9, not in GSM8K (2,299 samples)
- [`argilla/ultrafeedback-binarized-preferences-cleaned`](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned): highly scored chosen answers >=5 (22,799 samples)
- [`argilla/distilabel-math-preference-dpo`](https://huggingface.co/datasets/argilla/distilabel-math-preference-dpo): highly scored chosen answers >=9 (2,181 samples)
- [`unalignment/toxic-dpo-v0.2`](https://huggingface.co/datasets/unalignment/toxic-dpo-v0.2) (541 samples)
- [`M4-ai/prm_dpo_pairs_cleaned`](https://huggingface.co/datasets/M4-ai/prm_dpo_pairs_cleaned) (7,958 samples)
- [`jondurbin/truthy-dpo-v0.1`](https://huggingface.co/datasets/jondurbin/truthy-dpo-v0.1) (1,016 samples)

Rule-based filtering was applied to remove gptisms in the chosen answers (2,206 samples).

Thanks to [argilla](https://huggingface.co/argilla), [unalignment](https://huggingface.co/unalignment), [M4-ai](https://huggingface.co/M4-ai), and [jondurbin](https://huggingface.co/jondurbin) for providing the source datasets.

## 🔎 Usage

v1.2 adds a `question` column to ensure compatibility with both DPO and ORPO formats in Axolotl.

Here's an example as an ORPO dataset in Axolotl:

```yaml
rl: orpo
orpo_alpha: 0.1
chat_template: chatml
datasets:
  - path: mlabonne/orpo-dpo-mix-40k
    type: chat_template.argilla
    chat_template: chatml
```

For DPO, I recommend using [mlabonne/orpo-dpo-mix-40k-flat](https://huggingface.co/datasets/mlabonne/orpo-dpo-mix-40k-flat) instead.

## Toxicity

Note that ORPO-DPO-mix-40k contains a dataset (`toxic-dpo-v0.2`) designed to prompt the model to answer illegal questions. You can remove it as follows:

```python
dataset = load_dataset('mlabonne/orpo-dpo-mix-40k', split='train')
dataset = dataset.filter(
    lambda r: r["source"] != "toxic-dpo-v0.2"
)
```

## History

I'm saving previous versions of this dataset in different branches.

- [v1.0](https://huggingface.co/datasets/mlabonne/orpo-dpo-mix-40k/tree/v1.0)
Dataset Not Finished: 44991/44245 ready