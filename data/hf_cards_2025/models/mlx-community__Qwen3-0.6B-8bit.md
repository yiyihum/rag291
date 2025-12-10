---
library_name: mlx
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-0.6B/blob/main/LICENSE
pipeline_tag: text-generation
base_model: Qwen/Qwen3-0.6B
tags:
- mlx
---

# mlx-community/Qwen3-0.6B-8bit

This model [mlx-community/Qwen3-0.6B-8bit](https://huggingface.co/mlx-community/Qwen3-0.6B-8bit) was
converted to MLX format from [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B)
using mlx-lm version **0.24.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen3-0.6B-8bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
