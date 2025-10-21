---
license: apache-2.0
language:
- en
base_model:
- lastmass/Qwen3_Medical_GRPO
pipeline_tag: text-generation
library_name: transformers
tags:
- text-generation-inference
---

# **Qwen3-Medical-GRPO-GGUF**

> Qwen3_Medical_GRPO is a specialized medical language model fine-tuned from the Qwen3 base using Supervised Fine-Tuning (SFT) and enhanced with Group Relative Policy Optimization (GRPO) to deliver advanced performance in clinical case analysis, differential diagnosis, and medical reasoning tasks. The model is designed to provide both detailed, step-by-step reasoning (chain-of-thought) and clear, structured final answers, enabling greater transparency and reliability for healthcare professionals and research applications. By separating its internal analysis from synthesized conclusions, Qwen3_Medical_GRPO allows users to trace the logic behind clinical recommendations, optimizing accuracy and trustworthiness in complex medical scenarios.

## Model Files

| File Name | Quant Type | File Size |
| - | - | - |
| Qwen3-Medical-GRPO.BF16.gguf | BF16 | 8.05 GB |
| Qwen3-Medical-GRPO.F16.gguf | F16 | 8.05 GB |
| Qwen3-Medical-GRPO.F32.gguf | F32 | 16.1 GB |
| Qwen3-Medical-GRPO.Q2_K.gguf | Q2_K | 1.67 GB |
| Qwen3-Medical-GRPO.Q3_K_L.gguf | Q3_K_L | 2.24 GB |
| Qwen3-Medical-GRPO.Q3_K_M.gguf | Q3_K_M | 2.08 GB |
| Qwen3-Medical-GRPO.Q3_K_S.gguf | Q3_K_S | 1.89 GB |
| Qwen3-Medical-GRPO.Q4_K_M.gguf | Q4_K_M | 2.5 GB |
| Qwen3-Medical-GRPO.Q4_K_S.gguf | Q4_K_S | 2.38 GB |
| Qwen3-Medical-GRPO.Q5_K_M.gguf | Q5_K_M | 2.89 GB |
| Qwen3-Medical-GRPO.Q5_K_S.gguf | Q5_K_S | 2.82 GB |
| Qwen3-Medical-GRPO.Q6_K.gguf | Q6_K | 3.31 GB |
| Qwen3-Medical-GRPO.Q8_0.gguf | Q8_0 | 4.28 GB |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)