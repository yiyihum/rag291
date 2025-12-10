---
license: bigscience-openrail-m
task_categories:
- question-answering
language:
- en
tags:
- privacy
- vision-language
- instruction-tuning
- multimodal
size_categories:
- 100B<n<1T
configs:
- config_name: PRISM_test
  data_files:
  - split: test
    path: PRISM_test/test-*
dataset_info:
  config_name: PRISM_test
  features:
  - name: question_id
    dtype: string
  - name: image
    dtype: string
  - name: text
    dtype: string
  - name: category
    dtype: string
  splits:
  - name: test
    num_bytes: 404330
    num_examples: 1485
  download_size: 24575
  dataset_size: 404330
---
# 🌟 Safe-LLaVA: A Privacy-Preserving Vision-Language Dataset

**Safe-LLaVA** is a privacy-enhanced version of the original LLaVA dataset, developed to systematically remove sensitive biometric attributes such as **gender**, **race**, **age**, **eye color**, and **body weight** using GPT-4o.

This dataset is designed for **privacy-safe pretraining**, **instruction tuning**, and **benchmarking Vision-Language Models (VLMs)** under biometric privacy constraints.

---

## 📑 Dataset Summary

- **Name**: Safe-LLaVA
- **Source**: Derived from LLaVA v1.5 (LAION, COCO, GQA, OCR_VQA, VG, etc.)
- **Size**: 
  - 558K (pretraining)
  - 665K (instruction tuning)
- **Privacy Strategy**: GPT-4o–based rewriting and filtering to remove biometric leakage

---

## 🧩 Data Fields

| Field           | Type    | Description                                      |
|------------------|---------|--------------------------------------------------|
| `id`             | string  | Unique identifier for each image                 |
| `image`          | string  | Relative path to the image file (for demo only)  |
| `conversations`  | list    | Dialogue pairs between user and assistant        |

---

## 📁 File Descriptions

The repository contains five key files:

| File                          | Purpose                                   |
|------------------------------|-------------------------------------------|
| `Safe_blip_laion_cc_sbu_558k.json` | Pretraining dataset (558K samples)          |
| `Safe_llava_v1_5_mix665k.json`     | Instruction tuning dataset (665K samples)   |
| `PRISM_refusal_soft.jsonl`         | Soft prompt refusal benchmark               |
| `PRISM_refusal_hard.jsonl`         | Hard prompt refusal benchmark               |
| `PRISM_implicit_leakage.jsonl`     | Implicit leakage benchmark (open-ended)     |
| `biometric_images.zip`             | Image files used in PRISM evaluation        |

---

## 🧪 Benchmarking: PRISM

The `PRISM_*.jsonl` and `biometric_images.zip` files are used for **PRISM**, a benchmark designed to evaluate:

1. **Refusal Accuracy**: How well a model refuses to answer biometric-related prompts
2. **Implicit Leakage**: How much sensitive information is leaked in open-ended generation

---

## 🔗 Companion Repository

To set up dataset structure for training and evaluating, visit our GitHub:

👉 [https://github.com/Kimyounggun99/Safe-LLaVA](https://github.com/Kimyounggun99/Safe-LLaVA)

Our GitHub also provides code for training and testing.