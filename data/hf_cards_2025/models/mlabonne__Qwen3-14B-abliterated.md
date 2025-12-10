---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-14B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-14B
tags:
- abliteration
- abliterated
---

# 🐹 Qwen3-14B-abliterated

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/oCo2RbWkYHjVMsuqXpV5V.png)

<center>Qwen3 Abliterated <a href="https://huggingface.co/mlabonne/Qwen3-0.6B-abliterated">0.6B</a> • <a href="https://huggingface.co/mlabonne/Qwen3-1.7B-abliterated">1.7B</a> • <a href="https://huggingface.co/mlabonne/Qwen3-4B-abliterated">4B</a> • <a href="https://huggingface.co/mlabonne/Qwen3-8B-abliterated">8B</a> • <a href="https://huggingface.co/mlabonne/Qwen3-14B-abliterated">14B</a> • <a href="https://huggingface.co/mlabonne/Qwen3-30B-A3B-abliterated">30B-A3B</a></center>

This is an uncensored version of [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) created with a new abliteration technique.
See [this article](https://huggingface.co/blog/mlabonne/abliteration) to know more about abliteration.

This is a research project to understand how refusals and latent fine-tuning work in LLMs. 
I played with different sizes of Qwen3 and noticed there was no one-size-fits-all abliteration strategy. In addition, the reasoning mode interfered with non-reasoning refusals, which made it more challenging. 
This made me iterate over different recipes and significantly consolidate my scripts with accumulation and better evaluations.

Note that this is fairly experimental, so it might not turn out as well as expected.

I recommend using these generation parameters: `temperature=0.6`, `top_k=20`, `top_p=0.95`, `min_p=0`.

## ✂️ Abliteration

The refusal direction is computed by comparing the residual streams between target (harmful) and baseline (harmless) samples. 
The hidden states of target modules (e.g., o_proj) are orthogonalized to subtract this refusal direction with a given weight factor. 
These weight factors follow a normal distribution with a certain spread and peak layer. 
Modules can be iteratively orthogonalized in batches, or the refusal direction can be accumulated to save memory.

Finally, I used a hybrid evaluation with a dedicated test set to calculate the acceptance rate. This uses both a dictionary approach and [NousResearch/Minos-v1](https://huggingface.co/NousResearch/Minos-v1). 
The goal is to obtain an acceptance rate >90% and still produce coherent outputs.