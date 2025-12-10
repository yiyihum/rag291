---
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
tags:
- vllm
- mlx
- mlx-my-repo
- gpt
- gpt-oss
- openai
base_model: openai/gpt-oss-20b
---

# SiddhJagani/gpt-oss-20b-no-think-mlx-2Bit

The Model [SiddhJagani/gpt-oss-20b-mlx-2Bit](https://huggingface.co/SiddhJagani/gpt-oss-20b-no-think-mlx-2Bit) was converted to MLX format from [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) using mlx-lm version **0.28.2**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("SiddhJagani/gpt-oss-20b-no-think-mlx-2Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```