---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
- zh
- ko
- ja
license: llama3.1
pipeline_tag: text-generation
tags:
- roleplay
- llama3
- sillytavern
- idol
- facebook
- meta
- pytorch
- llama
- llama-3
- mlx
- mlx-my-repo
extra_gated_fields:
  First Name: text
  Last Name: text
  Date of birth: date_picker
  Country: country
  Affiliation: text
  Job title:
    type: select
    options:
    - Student
    - Research Graduate
    - AI researcher
    - AI developer/engineer
    - Reporter
    - Other
base_model: aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored
---

# Wwayu/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-mlx-6Bit

The Model [Wwayu/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-mlx-6Bit](https://huggingface.co/Wwayu/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-mlx-6Bit) was converted to MLX format from [aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored) using mlx-lm version **0.26.4**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Wwayu/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-mlx-6Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
