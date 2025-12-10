---
library_name: mlx
license: mit
pipeline_tag: text-generation
tags:
- mlx
base_model:
- inclusionAI/Ling-1T
---

# mlx-community/Ling-1T-mlx-3bit/

This model [mlx-community/Ling-1T-mlx-3bit/](https://huggingface.co/mlx-community/Ling-1T-mlx-3bit/) was
converted to MLX format from [inclusionAI/Ling-1T](https://huggingface.co/inclusionAI/Ling-1T)
using mlx-lm version **0.28.1**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Ling-1T-mlx-3bit/")

prompt = "hello"

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```