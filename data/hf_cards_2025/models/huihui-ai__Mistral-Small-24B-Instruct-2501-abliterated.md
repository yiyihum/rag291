---
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: apache-2.0
library_name: vllm
inference: false
base_model:
- mistralai/Mistral-Small-24B-Instruct-2501
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
tags:
- abliterated
- uncensored
- transformers
---

# huihui-ai/Mistral-Small-24B-Instruct-2501-abliterated


This is an uncensored version of [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).  
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens.    

## Use with ollama

You can use [huihui_ai/mistral-small-abliterated](https://ollama.com/huihui_ai/mistral-small-abliterated) directly
```
ollama run huihui_ai/mistral-small-abliterated
```