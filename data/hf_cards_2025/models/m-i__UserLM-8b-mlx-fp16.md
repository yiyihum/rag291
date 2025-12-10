---
license: mit
datasets:
- allenai/WildChat-1M
language:
- en
base_model: microsoft/UserLM-8b
pipeline_tag: text-generation
tags:
- userlm
- simulation
- mlx
- mlx-my-repo
---

# m-i/UserLM-8b-mlx-fp16

The Model [m-i/UserLM-8b-mlx-fp16](https://huggingface.co/m-i/UserLM-8b-mlx-fp16) was converted to MLX format from [microsoft/UserLM-8b](https://huggingface.co/microsoft/UserLM-8b) using mlx-lm version **0.26.4**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("m-i/UserLM-8b-mlx-fp16")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
