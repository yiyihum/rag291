---
license: apache-2.0
language:
- th
- en
- zh
base_model:
- deepseek-ai/DeepSeek-V2-Lite
pipeline_tag: text-generation
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

This modelcard aims to be a base template for new models. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md?plain=1).

## Model Details

### Model Description

DeepSeek-V2-Lite Quantized to NVFP4 Using TensorRT-Model-Optimizer. The model has 15.6B parameters in total, in Nvidia float precision 4 bit.
Require Blackwell GPU, NVFP4 supported inference engine(if use with inference engine)

- **Developed by:** Krisakorn Chanthasang
- **Model type:** LLM TextGeneration
- **Language(s) (NLP):** Chinese English Thai
- **License:** Apache 2.0
- **Quantized from model:** DeepSeek-V2-Lite
### Model Information

Read https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite for Basic model information

## How to Get Started with the Model

GPU requirement: Blackwell Series

## Hardware

Quantization Hardware: Nvidia RTX PRO 6000 Blackwell Workstation

