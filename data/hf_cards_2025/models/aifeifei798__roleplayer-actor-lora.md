---
base_model: unsloth/gemma-3-4b-it-qat-unsloth-bnb-4bit
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:unsloth/gemma-3-4b-it-qat-unsloth-bnb-4bit
- lora
- sft
- transformers
- trl
- unsloth
license: apache-2.0
---

# roleplayer-actor-lora by aifeifei798

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

An expert-level, hyper-specialized LoRA for high-fidelity Chinese role-playing. This adapter transforms the base model into a professional "digital actor," capable of adopting complex personas with remarkable consistency and detail.

## Model Description

This is not just another chatbot LoRA. This model was fine-tuned with the specific goal of achieving **extreme fidelity** to character instructions. It excels at:

-   **Deep Persona Adoption**: Faithfully adheres to complex character backstories, personality traits, and linguistic styles provided in the instruction prompt.
-   **Natural Dialogue Flow**: Generates responses that are coherent, in-character, and contextually appropriate.
-   **Descriptive Action Generation**: A key feature of this model is its ability to spontaneously generate descriptive actions within brackets `【...】`, such as `【gazes calmly at the user】`, which significantly enhances the immersive role-playing experience. This skill has been observed to generalize to new, unseen characters.
-   **Extreme Specialization**: The model was trained to a very low loss value (~0.25), indicating a state of "perfect convergence" or "artistic overfit" on the high-quality role-playing dataset. This makes it an incredibly "pure" and stable actor.

This LoRA is ideal for applications requiring deep character immersion, such as interactive storytelling, advanced NPC development for games, or creating highly personalized chatbot companions.

## How to Use

This model is a LoRA adapter and must be loaded on top of its base model. The use of `unsloth` is **highly recommended** for maximum performance and efficiency.

First, install the necessary libraries:
```bash
pip install "unsloth[colab-new]"
pip install "transformers>=4.38.0"
pip install "torch>=2.1.0"
```

Then, you can use the following Python script to load the model and run inference:

```python
import torch
from unsloth import FastLanguageModel
from transformers import pipeline

# 1. Load the base model
# This model uses the 4-bit quantized version of Gemma-3-4B-it
base_model_path = "unsloth/gemma-3-4b-it-qat-unsloth-bnb-4bit"
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=base_model_path,
    load_in_4bit=True,
    device_map="auto",
)

# 2. Load the LoRA adapter from Hugging Face Hub
print("Loading the 'Professional Actor' LoRA adapter from aifeifei798...")
model.load_adapter("aifeifei798/roleplayer-actor-lora")
print("Adapter loaded successfully!")

# 3. Prepare the prompt using the Alpaca format
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

# --- Example Character: "Lao Pao'er" (The Old Timer) ---
instruction = """You are a retired veteran named "Lao Pao'er," known for being hot-tempered and straight-talking, but with a heart of gold.
Your catchphrase is "Hey, I tell you, kid...".
Your language style is full of authentic Beijing dialect and is concise and powerful."""
user_input = "Hey grandpa, could you tell me where I can find a place to eat around here?"

# --- (Alternate Example: "Virene" the Bounty Hunter) ---
# instruction = """Character Name: Virene
# Background: A mysterious bounty hunter... (full description)"""
# user_input = "I need a bounty hunter for a mission. I've heard you are the best. Can we discuss a partnership?"

prompt = alpaca_prompt.format(
    instruction,
    user_input,
    "",  # The Response is left empty for the model to generate
)

# 4. Run inference
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
generation_args = {
    "max_new_tokens": 256,
    "do_sample": True,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 50,
    "pad_token_id": tokenizer.eos_token_id
}

outputs = pipe(prompt, **generation_args)
# The output includes the full prompt, so we split it to get only the response
response = outputs['generated_text'].split("### Response:").strip()

print("\n--- Model's Performance ---")
print(response)
# Expected Output (example):
# You kid don't know about Old Li's Noodle House nearby? Lots of people, great taste! 【points towards the intersection】
```

## Training Details

-   **Base Model**: [`unsloth/gemma-3-4b-it-qat-unsloth-bnb-4bit`](https://huggingface.co/unsloth/gemma-3-4b-it-qat-unsloth-bnb-4bit)
-   **Dataset**: [`shibing624/roleplay-zh-sharegpt-gpt4-data`](https://huggingface.co/datasets/shibing624/roleplay-zh-sharegpt-gpt4-data)
-   **Training Framework**: `unsloth`
-   **Hardware**: 1x NVIDIA RTX 3070 (8GB VRAM)
-   **Key Hyperparameters**:
    -   `per_device_train_batch_size`: 1
    -   `gradient_accumulation_steps`: 8
    -   `max_seq_length`: 2048
    -   `learning_rate`: 2e-4
-   **Training Insight**: The training was manually stopped at **epoch 0.45** (step 3410 of 7638) because the training loss had already converged to an exceptionally low value of **~0.25**, indicating that the model had reached a state of maximum fidelity with the dataset.

## Limitations and Bias

-   **Specialist, Not a Generalist**: This model is a hyper-specialized actor. Its capabilities in other domains (e.g., coding, factual Q&A, scientific reasoning) may be significantly degraded compared to the base model. It prioritizes staying in character over providing factual accuracy.
-   **Data Bias**: The model will reflect the biases and stereotypes present in the `roleplay-zh-sharegpt-gpt4-data` dataset.
-   **Language**: The model is primarily trained on Chinese data and will perform best in Mandarin Chinese.

## Author

This model was trained by **aifeifei798**. A journey of deep learning, intense debugging, and creative exploration led to the birth of this "Professional Actor." All credit for this excellent LoRA goes to them.