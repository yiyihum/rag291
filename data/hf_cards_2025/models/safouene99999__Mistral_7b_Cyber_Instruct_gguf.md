---
license: apache-2.0
base_model: unsloth/mistral-7b-instruct-v0.3-bnb-4bit
tags:
- cybersecurity
- fine-tuning
- gguf
- text-generation
- transformers
- unsloth
- mistral
- text-generation-inference
language:
- en
datasets:
- sambanovasystems/attackqa
- safouene99999/hackmentor-seed
metrics:
- perplexity
- bertscore
- bleurt
pipeline_tag: text-generation
---


# Mistral-7B-Cyber-Instruct

This model was fine-tuned for cybersecurity-related tasks .

- **Developed by:** [safouene99999](https://huggingface.co/safouene99999)
- **License:** Apache 2.0
- **Fine-tuned from:** [unsloth/mistral-7b-instruct-v0.3-bnb-4bit](https://huggingface.co/unsloth/mistral-7b-instruct-v0.3-bnb-4bit)
- **Training framework:** [Unsloth](https://github.com/unslothai/unsloth) + Hugging Face TRL

## Highlights

- Fine-tuned on **cybersecurity question-answering** datasets and used in incident report generation.
- Exported to **GGUF** for compatibility with llama.cpp and offline inference.

## Model Performance

> Evaluated with BLEURT: 0.46, BERTScore: 0.83, and Perplexity: 11.6 .

## Made With ❤️

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
