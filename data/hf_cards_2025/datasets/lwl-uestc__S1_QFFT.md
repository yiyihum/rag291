---
license: apache-2.0
dataset: S1-QFFT
tags:
- reasoning
- instruction-tuning
- qfft
- llamafactory
- distillation
task_categories:
- text-generation
---

# 📘 S1–QFFT

**S1–QFFT** is a question-free version of the original [simplescaling/s1K-1.1](https://huggingface.co/datasets/simplescaling/s1K-1.1) dataset, designed for QFFT training workflows.

## 🔍 Description

This dataset discards the **original questions and any system instructions**, keeping only the **reasoning completions** as supervision. It is especially useful for models that aim to learn **when and how to think**, rather than just **how to answer**.

The dataset is fully converted into a format compatible with **LLaMA-Factory** training.

## ✅ Use Case

- Lightweight adaptive fine-tuning
- Robust reasoning in noisy or underspecified contexts

## 📌 Source

Based on: [simplescaling/s1K-1.1](https://huggingface.co/datasets/simplescaling/s1K-1.1)

Converted and open-sourced by the [QFFT](https://github.com/LWL-cpu/Question-Free-Fine-Tuning) project.

## 💻 Code

The QFFT project's GitHub repository can be found [here](https://github.com/LWL-cpu/Question-Free-Fine-Tuning).

---
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