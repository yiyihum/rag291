---
language: en
license: apache-2.0
datasets: daily_dialog
pipeline_tag: text-generation
library_name: transformers
tags:
- gpt2
- conversational
- chatbot
- nlp
base_model: gpt2
---

# GPT-2 Personal Assistant

**Model repo:** `hmnshudhmn24/gpt2-personal-assistant`
A lightweight conversational assistant based on **GPT-2**, fine-tuned on the **DailyDialog** dataset for chat and casual Q&A.

## Model details
- **Base model:** gpt2
- **Task:** Conversational text generation / Chatbot
- **Dataset used for demo:** daily_dialog (small subset used in training script for quick demo)
- **Language:** English
- **License:** Apache-2.0

## How to use (inference)

```python
from transformers import pipeline

generator = pipeline("text-generation", model="hmnshudhmn24/gpt2-personal-assistant")
prompt = "User: Hello\nAssistant: Hi! How can I help you?\nUser: What's the weather like today?\nAssistant:"
print(generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"])
```

## Train locally (quick demo)
Run:
```bash
python train_chatbot.py
```
This script fine-tunes `gpt2` on a subset of the DailyDialog dataset and saves the model to `./gpt2-personal-assistant` folder.

## Files in this repo
- `config.json`, `tokenizer_config.json`, `special_tokens_map.json` — model/tokenizer configs
- `train_chatbot.py` — training script (demo)
- `inference.py` — simple inference example
- `utils.py` — helper to build conversation prompts
- `example_conversations.txt` — small sample dialogues
- `requirements.txt` — Python dependencies

## Notes & limitations
- GPT-2 is a general-purpose LM; it can generate incorrect or unsafe outputs. Do not rely on it for critical advice.
- For production, use larger datasets, more epochs, and safety filtering.
- If uploading to Hugging Face, include `pytorch_model.bin` (weights) after training.

## License
Apache-2.0
