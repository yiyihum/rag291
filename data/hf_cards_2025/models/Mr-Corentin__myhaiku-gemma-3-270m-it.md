---
base_model: google/gemma-3-270m-it
tags:
- text-generation
- haiku
- poetry
- gemma
- fine-tuning
- lora-merged
language:
- en
---

# myhaiku — Fine-tuned Gemma 3 270M (Haiku Generator)

This model is a fine-tuned version of `google/gemma-3-270m-it` trained to generate **English haiku poems**.

## Description

The model was fine-tuned using a dataset of approximately 4000 *traditional Japanese haiku* translated into English, where each example contains:
- a *prompt-style instruction* such as `"Please create a haiku about the transition between seasons."`
- the corresponding haiku of exactly three short lines.
  
While inspired by the original Japanese poetic tradition, the model does not strictly enforce the 5–7–5 syllabic pattern, as this rhythm is rarely preserved literally in English translations.  
The fine-tuning was performed using **LoRA adapters**, then merged into the base weights for lightweight deployment.

---

## Recommended usage

The model works best with **instruction-style prompts** similar to those used during fine-tuning:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

repo_id = "Mr-Corentin/myhaiku-gemma-3-270m-it"
tok = AutoTokenizer.from_pretrained(repo_id)
mdl = AutoModelForCausalLM.from_pretrained(repo_id, device_map="auto")
pipe = pipeline("text-generation", model=mdl, tokenizer=tok)

messages = [
    {"role": "system", "content": "You are a haiku generator. Reply with exactly three short lines, no extra text."},
    {"role": "user", "content": "Please create a haiku about the sound of rain on old rooftops."}
]
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
out = pipe(prompt, max_new_tokens=40)[0]["generated_text"][len(prompt):].strip()
print(out)
```

You can also try shorter theme-only prompts, e.g. "sound of rain on old rooftops", but instruction-style inputs will usually yield more stable results.

## Training details

Base model: google/gemma-3-270m-it

LoRA rank: 16  
LoRA dropout: 0.1  
Learning rate: 5e-5  
Epochs: 3  
Batch size: 4 per device  
Eval strategy: epoch
