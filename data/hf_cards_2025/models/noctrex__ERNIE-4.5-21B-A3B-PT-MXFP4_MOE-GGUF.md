---
base_model:
- unsloth/ERNIE-4.5-21B-A3B-PT-GGUF
license: apache-2.0
language:
- en
- zh
pipeline_tag: text-generation
tags:
- ERNIE4.5
- unsloth
library_name: transformers
---

This is a MXFP4_MOE quantization of the model ERNIE-4.5-21B-A3B-PT

Model quantized with BF16 GGUF's from: https://huggingface.co/unsloth/ERNIE-4.5-21B-A3B-PT-GGUF

Original model: https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-PT


MMLU Pro Benchmark:
| overall | biology | business | chemistry | computer science | economics | engineering | health | history | law | math | philosophy | physics | psychology | other |
| ------- | ------- | -------- | --------- | ---------------- | --------- | ----------- | ------ | ------- | --- | ---- | ---------- | ------- | ---------- | ----- |
| 65.13 | 80.47 | 71.86 | 72.53 | 67.80 | 70.85 | 54.39 | 63.81 | 49.34 | 34.97 | 80.53 | 53.11 | 71.05 | 65.91 | 61.80 |
