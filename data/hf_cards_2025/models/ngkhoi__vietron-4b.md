---
-license: gemma
language:
- vi
pipeline_tag: text-generation
library_name: transformers
tags:
- unsloth
license: gemma
---
# VIETRON 4B - Fine-tuned Vietnamese model
<img src="https://lh3.googleusercontent.com/d/1Ez_5ubsKUpDGagqNWKlgJJm-kGUIjkKS=w1000?authuser=0" />

> [!NOTE]
> This is my first proper fine-tuned model, but still, the model may generate false informations or mistakes.

VieTron 4B is a Large Language Model (LLM) that has been extensively fine-tuned for Vietnamese users. With a 4-billion-parameter scale, VieTron is designed to be a smart, friendly AI assistant with a deep understanding of Vietnamese culture and education.

## Details

Trained on high-quality Vietnamese datasets that cover most fields and topics.

**More thoughtful**: the model is trained with instruction to give response step by step (or CoT), the model will not only generate results but the reasoning steps behind the results.

**More natural response style**: the datasets also includes the natural Vietnamese conversation, making the model's response more "human".

## Model info

~4 billion parameters

Currently I've only uploaded the initial version, quantized Q8_0 GGUF format to test the model. I will provide more quantized GGUF formats in the future as the model is getting better. 

## Usage

LM Studio **recommended**: the easiest way to run inference. Search <sup>ngkhoi/vietron-4b</sup> and download to use this model.


## Limitations & Ethical Considerations
Knowledge Cutoff: VieTron's knowledge is limited to its training data. The model may not be aware of the latest events.

Hallucination Potential: Like all LLMs, VieTron can generate incorrect information. Please verify important facts.





## Contributions
This project is developed solely by me so any contributions to this project are truly welcome!