---
dataset: true
tags:
- chatbot
- instruction-tuning
license: cc-by-nc-4.0
language: en
---

# Chat-Based Instruction Dataset (Character Persona)

This dataset contains **question–answer dialogues** designed to fine-tune a language model to adopt a fictional character's persona. In this case, the dataset helps the model respond **in-character**, emulating the speech style and tone of a well-known superhero character.

## Dataset Structure

- Format: JSONL
- Each entry follows the **chat template** format used by Hugging Face’s LLaMA-style models:
  
json
  {
    "messages": [
      {"role": "system", "content": "<persona/prompt>"},
      {"role": "user", "content": "<question>"},
      {"role": "assistant", "content": "<response>"}
    ]
  }