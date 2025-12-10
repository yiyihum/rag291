---
license: apache-2.0
dataset: LIMO-QFFT
task_categories:
- text-generation
tags:
- reasoning
- chain-of-thought
- instruction-tuning
- qfft
- llamafactory
---

# 📘 LIMO–QFFT

**LIMO–QFFT** is a question-free variant of the original [GAIR/LIMO](https://huggingface.co/datasets/GAIR/LIMO) dataset, tailored for use in QFFT (Question-Free Fine-Tuning) pipelines.

## 🔍 Description

This dataset removes the **original input questions and system prompts** from the LIMO dataset, and keeps only the **long-form reasoning responses**. The goal is to enable training large language models to **learn from reasoning traces alone**, without depending on task-specific questions.

All entries are converted into **LLaMA-Factory-compatible training format**, and ready for direct use in instruction tuning with QFFT methods.

## ✅ Use Case

- Adaptive reasoning fine-tuning
- Long-chain-of-thought distillation

## 📌 Source

Based on: [GAIR/LIMO](https://huggingface.co/datasets/GAIR/LIMO)

Converted and released by the [QFFT](https://github.com/LWL-cpu/Question-Free-Fine-Tuning) team.

Code: https://github.com/LWL-cpu/Question-Free-Fine-Tuning

## 📖 Citation

```
@misc{liu2025qfft,
  title={QFFT, Question-Free Fine-Tuning for Adaptive Reasoning},
  author={Wanlong Liu and Junxiao Xu and Fei Yu and Yukang Lin and Ke Ji and Wenyu Chen and Yan Xu and Yasheng Wang and Lifeng Shang and Benyou Wang},
  year={2025},
  eprint={2506.12860},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2506.12860},
}
```