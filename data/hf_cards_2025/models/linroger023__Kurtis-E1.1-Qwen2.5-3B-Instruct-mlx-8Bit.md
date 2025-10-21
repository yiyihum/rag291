---
library_name: transformers
license: mit
datasets:
- ethicalabs/Kurtis-E1-SFT
language:
- en
base_model: ethicalabs/Kurtis-E1.1-Qwen2.5-3B-Instruct
pipeline_tag: text-generation
tags:
- mlx
---

# linroger023/Kurtis-E1.1-Qwen2.5-3B-Instruct-mlx-8Bit

The Model [linroger023/Kurtis-E1.1-Qwen2.5-3B-Instruct-mlx-8Bit](https://huggingface.co/linroger023/Kurtis-E1.1-Qwen2.5-3B-Instruct-mlx-8Bit) was converted to MLX format from [ethicalabs/Kurtis-E1.1-Qwen2.5-3B-Instruct](https://huggingface.co/ethicalabs/Kurtis-E1.1-Qwen2.5-3B-Instruct) using mlx-lm version **0.22.3**.

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate

model, tokenizer = load("linroger023/Kurtis-E1.1-Qwen2.5-3B-Instruct-mlx-8Bit")

prompt="hello"

if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

response = generate(model, tokenizer, prompt=prompt, verbose=True)
```
