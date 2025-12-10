---
language:
- en
license: cc-by-nc-4.0
size_categories:
- 100K<n<1M
task_categories:
- image-text-to-text
pretty_name: LLaVA-1.5-665K-GenQA-Random-500K
tags:
- vlm
- multimodal
- instruction-tuning
---

# LLaVA-1.5-665K-GenQA-Random-500K

This dataset is used in the paper [Zero-Shot Vision Encoder Grafting via LLM Surrogates](https://huggingface.co/papers/2505.22664).

The code for the paper can be found at: [https://github.com/kaiyuyue/zero](https://github.com/kaiyuyue/zero)

## Dataset Composition

This repository contains the `llava-665k_genqa-500k_shuffled.json` file, which mixes samples from two sources:

-   [llava-1.5-665k-instructions](https://huggingface.co/datasets/kaiyuyue/llava-1.5-665k-instructions) without the text-only samples of ShareGPT-40K.
-   500K randomly sampled sequences from [genqa](https://huggingface.co/datasets/tomg-group-umd/GenQA).

The order of samples has been already balanced and shuffled.

For more details on the dataset creation and its usage, please refer to the [paper](https://huggingface.co/papers/2505.22664) and the [GitHub repository](https://github.com/kaiyuyue/zero).

---

**License:** Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC 4.0)