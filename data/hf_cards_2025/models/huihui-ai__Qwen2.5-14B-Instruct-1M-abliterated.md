---
license: apache-2.0
license_link: https://huggingface.co/huihui-ai/Qwen2.5-14B-Instruct-1M-abliterated/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-14B-Instruct-1M
tags:
- chat
- abliterated
- uncensored
library_name: transformers
---
# huihui-ai/Qwen2.5-14B-Instruct-1M-abliterated


This is an uncensored version of [Qwen/Qwen2.5-14B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).  
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens.    

## Use with ollama

You can use [huihui_ai/qwen2.5-1m-abliterated](https://ollama.com/huihui_ai/qwen2.5-1m-abliterated) directly
```
ollama run huihui_ai/qwen2.5-1m-abliterated:14b
```