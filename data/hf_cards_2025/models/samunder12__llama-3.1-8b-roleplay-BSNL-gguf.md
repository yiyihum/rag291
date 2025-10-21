---
library_name: transformers
license: apache-2.0
base_model:
- meta-llama/Llama-3.1-8B-Instruct
pipeline_tag: text-generation
tags:
- roleplay
- rp
- character
- peft
- unsloth
- bitsandbytes
---




<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="./Bsnl.jpeg" alt="Peach" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>



# Llama-3.1-8B-Roleplay-BSNL-Story-GGUF

This is a GGUF quantized version of a fine-tuned Llama 3.1 8B Instruct model, specialized for **fast-paced, Post-training Llama-3.1-8B mostly for story generation , less conversational role-play**.

This model was fine-tuned using Unsloth on a curated dataset of over 300 examples designed to mimic a "quick response" chat style, similar to platforms like Character.AI. The persona is dominant, assertive, and direct, using a combination of expressive actions and concise dialogue.

This repository contains the `Q4_K_M` GGUF version, which offers an excellent balance of quality and performance for local inference.

## Model Details

- **Base Model:** `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
- **Original LoRA Model:** [`samunder12/llama-3.1-8b-roleplay-v4-lora`](https://huggingface.co/samunder12/llama-3.1-8b-roleplay-v4-lora)
- **Fine-tuning Method:** PEFT (LoRA) with Unsloth's performance optimizations.
- **LoRA Rank (`r`):** 32
- **Format:** GGUF
- **Quantization:** Q4_K_M

## How to Use in LM Studio

1.  **Search:** Find this model (`samunder12/llama-3.1-8b-roleplay-BSNL-gguf`) on the LM Studio home screen.
2.  **Download:** Download the `llama3BSNL.Q4_K_M.gguf` file.
3.  **Load:** Go to the Chat tab (💬 icon) and select this model to load at the top.
4.  **Set Prompt Format:** In the right-hand panel, under "Preset," select **`Llama 3`**. **This is a critical step!**
5.  **Set Context Length:** Set the `Context Length (n_ctx)` to **`4096`** to match the model's training.
6.  **Apply a Sampler Preset:** Use one of the presets below for the best experience.

## Intended Use & Limitations

This model is intended for creative writing, immersive role-playing, and chatbot development where a quick, conversational interaction style is desired.

- The model's output is unfiltered and reflects the persona and content of its training data.
- It is highly specialized for its role-play task and may not perform well on other tasks like coding, summarization, or factual question-answering.

## Training Procedure

- **Framework:** Unsloth
- **Dataset:** 513 examples of short-form, multi-turn conversational data. The data emphasizes a structure of `*Action/Expression in asterisks.* Short, impactful dialogue.`
- **Key Hyperparameters:**
  - `num_train_epochs`: 2
  - `max_seq_length`: 4096
  - `learning_rate`: 2e-4
  - `lr_scheduler_type`: cosine
  - `lora_r`: 32
  - `lora_alpha`: 32

---