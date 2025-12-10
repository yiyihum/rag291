---
license: apache-2.0
language:
- en
tags:
- instruction-tuning
- dpo
- quality-comparison
---

# DPO Contrast Sample

This dataset provides a **direct comparison** between high-quality and low-quality instruction-output pairs evaluated by a LLaMA-2-7B-Chat model in a DPO-style workflow.

## Structure

- `instruction`: The generated prompt (x).
- `output`: The associated output (y).
- `score`: Quality rating assigned by LLaMA2 (1 = high, 5 = low).

## Samples

5 examples with score = 1 (excellent), and 5 with score = 5 (poor).
