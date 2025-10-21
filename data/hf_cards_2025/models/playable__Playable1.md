---
license: apache-2.0
base_model: Qwen/Qwen2.5-Coder-7B-Instruct
tags:
- safetensors
- text-generation
---

# Playable1

This is a fine-tuned version of Qwen/Qwen2.5-Coder-7B-Instruct using the 'iat-05-1' adapter.

## Model Details

- **Base Model:** Qwen/Qwen2.5-Coder-7B-Instruct
- **Adapter:** iat-05-1
- **Format:** SafeTensors

## Usage

This model can be used with transformers library:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("playable/Playable1")
tokenizer = AutoTokenizer.from_pretrained("playable/Playable1")

inputs = tokenizer("Your prompt here", return_tensors="pt")
outputs = model.generate(**inputs)
print(tokenizer.decode(outputs[0]))
```
