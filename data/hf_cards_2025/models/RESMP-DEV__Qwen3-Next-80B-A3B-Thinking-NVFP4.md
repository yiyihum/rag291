---
language:
- en
- zh
license_link: https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/main/LICENSE
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-Next-80B-A3B-Thinking
---
# Qwen3-Next-80B-A3B-Thinking-NVFP4

**Quantized version of [Qwen/Qwen3-Next-80B-A3B-Thinking](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)** using **LLM Compressor** and the **NVFP4** (E2M1 + E4M3) format.

**This time it actually works!** *We think*

This should be the start of a new series of *hopefully optimal* NVFP4 quantizations as capable cards continue to grow out in the wild.

---

## Model Summary

| Property | Value |
|-----------|--------|
| Base model | Qwen/Qwen3-Next-80B-A3B-Thinking |
| Quantization | NVFP4 (FP4 microscaling, block = 16, scale = E4M3) |
| Method | Post-Training Quantization with LLM Compressor |
| Toolchain | LLM Compressor |
| Hardware target | NVIDIA Blackwell (Untested on RTX cards) / GB200 Tensor Cores |
| Precision | Weights & activations = FP4 • Scales = FP8 (E4M3) |
| Maintainer | **RESMP.DEV** |

---

## Description

This model is a drop-in replacement for Qwen/Qwen3-Next-80B-A3B-Thinking that runs in **NVFP4 precision**.
Accuracy remains within ≈ 1 % of the FP8 baseline on standard reasoning and coding benchmarks.
