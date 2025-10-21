---
license: apache-2.0
language:
- ru
base_model:
- RefalMachine/RuadaptQwen2.5-32B-Pro-Beta
datasets:
- pomelk1n/RuadaptQwen-Quantization-Dataset
pipeline_tag: text-generation
tags:
- AWQ
- GEMM
---

Эта модель является квантизированной версией.

```
pip install autoawq==0.2.8

from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer
import torch

# Specify paths and hyperparameters for quantization
model_path = "/data/models/RuadaptQwen2.5-32B-Pro-Beta"
quant_path = "/data/models/RuadaptQwen2.5-32B-Pro-Beta-AWQ"
quant_config = {"zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM"}

# Load your tokenizer and model with AutoAWQ
model = AutoAWQForCausalLM.from_pretrained(
    model_path, safetensors=True, torch_dtype=torch.bfloat16
)

model.quantize(tokenizer, quant_config=quant_config, calib_data="/data/scripts/RuadaptQwen-Quantization-Dataset", text_column='text')

model.save_quantized(quant_path, safetensors=True, shard_size="5GB")
```