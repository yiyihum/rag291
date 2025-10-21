---
license: apache-2.0
pipeline_tag: text-generation
library_name: mlx
tags:
- vllm
- mlx
base_model: openai/gpt-oss-20b
---

# mlx-community/gpt-oss-20b-MXFP4-Q8

This model [mlx-community/gpt-oss-20b-MXFP4-Q8](https://huggingface.co/mlx-community/gpt-oss-20b-MXFP4-Q8) was
converted to MLX format from [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)
using mlx-lm version **0.27.0**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/gpt-oss-20b-MXFP4-Q8")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
