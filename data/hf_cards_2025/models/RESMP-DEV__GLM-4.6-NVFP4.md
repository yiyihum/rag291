---
language:
- en
- zh
library_name: transformers
license: mit
pipeline_tag: text-generation
base_model:
- zai-org/GLM-4.6
---
# GLM-4.6-NVFP4

**Quantized version of [GLM-4.6](https://huggingface.co/zai-org/GLM-4.6)** using **LLM Compressor** and the **NVFP4** (E2M1 + E4M3) format.

**This time it actually works!**  *We think* 

This should be the start of a new series of *hopefully optimal* NVFP4 quantizations as capable cards continue to grow out in the wild. 

---

## Model Summary

| Property | Value |
|-----------|--------|
| Base model | GLM-4.6 |
| Quantization | NVFP4 (FP4 microscaling, block = 16, scale = E4M3) |
| Method | Post-Training Quantization with LLM Compressor |
| Toolchain | LLM Compressor |
| Hardware target | NVIDIA Blackwell (Untested on RTX cards) / GB200 Tensor Cores |
| Precision | Weights & activations = FP4 • Scales = FP8 (E4M3) |
| Maintainer | **REMSP.DEV** |

---

## Description

This model is a drop-in replacement for GLM-4.6 that runs in **NVFP4 precision**, enabling up to **6× faster GEMM throughput** and around **65 % lower memory use** compared with BF16.
Accuracy remains within ≈ 1 % of the FP8 baseline on standard reasoning and coding benchmarks.

---
