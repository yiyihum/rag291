---
base_model:
- yamatazen/FusionEngine-12B
- nbeerbower/Mistral-Nemo-12B-abliterated-LORA
library_name: transformers
tags:
- merge
- lorablated
---
![image/png](https://huggingface.co/yamatazen/FusionEngine-12B-Lorablated/resolve/main/4f77ffde-e497-46c4-bfb4-bcf346453bc9-0.jpg?download=true)
# Merged Model

This model is a combination of:

- **Base Model**: `yamatazen/FusionEngine-12B`
- **LoRA Adapter**: `nbeerbower/Mistral-Nemo-12B-abliterated-LORA`

The model is saved in `bfloat16` format and is ready for deployment or fine-tuning.