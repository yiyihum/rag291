---
language:
- en
- zh
library_name: transformers
license: mit
pipeline_tag: text-generation
base_model:
- huihui-ai/Huihui-GLM-4.5-Air-abliterated-GGUF
tags:
- abliterated
- uncensored
---

# huihui-ai/Huihui-GLM-4.5-Air-abliterated-lossytensors


This is a **lossy safetensors** version of [Huihui-GLM-4.5-Air-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-4.5-Air-abliterated-GGUF) that can be run with huggingface transformers, since the original release did not include safetensors files.

It was re-converted back into .safetensors manually from the **Q4_K_M GGUF** file. 

As such, although the weights are now in BF16, it is considered a "lossy" version of inferior quality to the full precision model.

However, you should now be able to use it with backends that cannot use GGUF and require safetensors (e.g. MLX, VLLM).

**Avoid requantizing it to formats above Q4_K_M - You will NOT gain any additional quality.**

If you require the max precision version, you'll have to buy it from huihui.