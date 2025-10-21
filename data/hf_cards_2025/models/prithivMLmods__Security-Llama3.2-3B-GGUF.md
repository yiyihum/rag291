---
license: llama3.2
base_model:
- viettelsecurity-ai/security-llama3.2-3b
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- text-generation-inference
---

# **Security-Llama3.2-3B-GGUF**

> security-llama3.2-3b is a dense, decoder-only Transformer model with approximately 3 billion parameters. It is optimized for generating text, particularly in response to prompts in a chat format, with a context length of up to 4,000 tokens. The model is specialized toward cybersecurity content, drawing on a mixture of publicly available blogs, papers, reference datasets (e.g. from the PEASEC cybersecurity repository), synthetic “textbook-style” data, and academic Q&A sources to enhance performance in security-themed tasks. For usage, the model accepts chat-style inputs (e.g. alternating “user” / “assistant” messages) and can be deployed via the Hugging Face transformers library (e.g. via pipeline("text-generation", model="viettelsecurity-ai/security-llama3.2-3b")). The model weights are stored in safetensors format, configured with fp16 (half precision), and no inference provider currently hosts it by default.

## Model Files

| File Name | Quant Type | File Size |
| - | - | - |
| security-llama3.2-3b.BF16.gguf | BF16 | 6.43 GB |
| security-llama3.2-3b.F16.gguf | F16 | 6.43 GB |
| security-llama3.2-3b.F32.gguf | F32 | 12.9 GB |
| security-llama3.2-3b.Q2_K.gguf | Q2_K | 1.36 GB |
| security-llama3.2-3b.Q3_K_L.gguf | Q3_K_L | 1.82 GB |
| security-llama3.2-3b.Q3_K_M.gguf | Q3_K_M | 1.69 GB |
| security-llama3.2-3b.Q3_K_S.gguf | Q3_K_S | 1.54 GB |
| security-llama3.2-3b.Q4_0.gguf | Q4_0 | 1.92 GB |
| security-llama3.2-3b.Q4_1.gguf | Q4_1 | 2.09 GB |
| security-llama3.2-3b.Q4_K.gguf | Q4_K | 2.02 GB |
| security-llama3.2-3b.Q4_K_M.gguf | Q4_K_M | 2.02 GB |
| security-llama3.2-3b.Q4_K_S.gguf | Q4_K_S | 1.93 GB |
| security-llama3.2-3b.Q5_0.gguf | Q5_0 | 2.27 GB |
| security-llama3.2-3b.Q5_1.gguf | Q5_1 | 2.45 GB |
| security-llama3.2-3b.Q5_K.gguf | Q5_K | 2.32 GB |
| security-llama3.2-3b.Q5_K_M.gguf | Q5_K_M | 2.32 GB |
| security-llama3.2-3b.Q5_K_S.gguf | Q5_K_S | 2.27 GB |
| security-llama3.2-3b.Q6_K.gguf | Q6_K | 2.64 GB |
| security-llama3.2-3b.Q8_0.gguf | Q8_0 | 3.42 GB |

## Quants Usage 

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)