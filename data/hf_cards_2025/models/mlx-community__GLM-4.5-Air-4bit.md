---
license: mit
language:
- en
- zh
pipeline_tag: text-generation
library_name: mlx
base_model: zai-org/GLM-4.5-Air
tags:
- mlx
---

# mlx-community/GLM-4.5-Air-4bit

This model [mlx-community/GLM-4.5-Air-4bit](https://huggingface.co/mlx-community/GLM-4.5-Air-4bit) was
converted to MLX format from [zai-org/GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air)
using mlx-lm version **0.26.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/GLM-4.5-Air-4bit")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
