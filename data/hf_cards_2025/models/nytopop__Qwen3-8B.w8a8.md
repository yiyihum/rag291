---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE
pipeline_tag: text-generation
base_model: Qwen/Qwen3-8B
---

Int8 quant for optimized performance on Ampere.

# usage

```shell
uv venv --python 3.12

uv pip install sglang[all] --find-links https://flashinfer.ai/whl/cu124/torch2.5/flashinfer-python

uv run python -m sglang.launch_server --model-path nytopop/Qwen3-8B.w8a8 --quantization w8a8_int8 --reasoning-parser qwen3
```

# creation

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import GPTQModifier
from llmcompressor.modifiers.smoothquant import SmoothQuantModifier

model_id  = "Qwen/Qwen3-8B"
model_out = "Qwen3-8B.w8a8"

num_samples = 256
max_seq_len = 4096

tokenizer = AutoTokenizer.from_pretrained(model_id)

def preprocess_fn(example):
  return {"text": tokenizer.apply_chat_template(example["messages"], add_generation_prompt=False, tokenize=False)}

ds = load_dataset("neuralmagic/LLM_compression_calibration", split="train")
ds = ds.shuffle().select(range(num_samples))
ds = ds.map(preprocess_fn)

recipe = [
  SmoothQuantModifier(smoothing_strength=0.7),
  GPTQModifier(sequential=True,targets="Linear",scheme="W8A8",ignore=["lm_head"],dampening_frac=0.01),
]

model = AutoModelForCausalLM.from_pretrained(
  model_id,
  device_map="auto",
  torch_dtype="bfloat16",
)

oneshot(
  model=model,
  dataset=ds,
  recipe=recipe,
  max_seq_length=max_seq_len,
  num_calibration_samples=num_samples,
  output_dir=model_out,
)
```
