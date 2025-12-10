---
license: apache-2.0
base_model: DavidAU/Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B
datasets:
- DavidAU/The-works-PK-Dick
language:
- en
pipeline_tag: text-generation
tags:
- programming
- code generation
- code
- coding
- coder
- chat
- brainstorm
- llama 3.2
- llama
- llama-3.2
- brainstorm 40x
- all uses cases
- finetune
- unsloth
- not-for-all-audiences
- mlx
library_name: mlx
---

# Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B-qx86-hi-mlx

This model [Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B-qx86-hi-mlx](https://huggingface.co/Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B-qx86-hi-mlx) was
converted to MLX format from [DavidAU/Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B](https://huggingface.co/DavidAU/Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B)
using mlx-lm version **0.28.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("Llama-3.2-PKD-Deckard-Almost-Human-abliterated-uncensored-7B-qx86-hi-mlx")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
