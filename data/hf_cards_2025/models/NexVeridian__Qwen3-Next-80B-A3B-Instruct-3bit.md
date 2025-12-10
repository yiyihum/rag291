---
library_name: mlx
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/main/LICENSE
pipeline_tag: text-generation
base_model: Qwen/Qwen3-Next-80B-A3B-Instruct
tags:
- mlx
---

# NexVeridian/Qwen3-Next-80B-A3B-Instruct-3bit

This model [NexVeridian/Qwen3-Next-80B-A3B-Instruct-3bit](https://huggingface.co/NexVeridian/Qwen3-Next-80B-A3B-Instruct-3bit) was
converted to MLX format from [Qwen/Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
using mlx-lm version **0.28.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("NexVeridian/Qwen3-Next-80B-A3B-Instruct-3bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
