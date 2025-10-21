---
tags:
- text
- instruction-tuning
- alignment
- fine-tuning
- non-dual
- mlabonne
datasets:
- mlabonne/FineTome-100k
language:
- en
license: cc-by-4.0
---

# fine_tome_100k_nondual

A non-dual reformulation of the [**mlabonne/FineTome-100k**](https://huggingface.co/datasets/mlabonne/FineTome-100k) dataset.  
All assistant outputs (`from: gpt`) have been rewritten into **impersonal, non-dual language** using OpenAI models.  
User inputs and other roles remain unchanged.

## Dataset Summary

- **Source:** [FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)  
- **Size:** ~100,000 conversations (JSONL, one per line)  
- **Format:** ShareGPT-style conversations, with fields:
  ```json
  {
    "conversations": [
      {"from": "user", "value": "User message..."},
      {"from": "gpt", "value": "Non-dual rewritten assistant response..."}
    ],
    "source": "...",
    "score": ...
  }
