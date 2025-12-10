---
license: llama3.1
language:
- en
tags:
- abliterated
- uncensored
base_model:
- cognitivecomputations/Dolphin3.0-Llama3.1-8B
library_name: transformers
---

# huihui-ai/Dolphin3.0-Llama3.1-8B-abliterated


This is an uncensored version of [cognitivecomputations/Dolphin3.0-Llama3.1-8B](https://huggingface.co/cognitivecomputations/Dolphin3.0-Llama3.1-8B) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).  
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens.    

## Use with ollama

You can use [huihui_ai/dolphin3-abliterated](https://ollama.com/huihui_ai/dolphin3-abliterated) directly
```
ollama run huihui_ai/dolphin3-abliterated
```
