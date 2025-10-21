---
library_name: transformers
language: en
license: apache-2.0
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-generation
tags:
- roleplay
- rp
- character
- peft
- unsloth
- llama-3.2
- instruct
- creative-writing
- storytelling
- gguf
- llama.cpp
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="./shiro.jpg" alt="Peach" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

# Llama-3.2-3B-small_Shiro_roleplay-gguf - GGUF
- small but not useless enjoy role-playing 

## Available Model files:
- `Llama-3.2-3B-Instruct.Q8_0.gguf`
- ``Llama-3.2-3B-Instruct.Q4_K_M.gguf`

## Model Details

- **Base Model:** `unsloth/Meta-Llama-3.2-3B-Instruct-bnb-4bit`
- **Original LoRA Model:** [`samunder12/llama-3.2-3b-roleplay-lora`](https://huggingface.co/samunder12/llama-3.2-3b-lora)
- **Fine-tuning Method:** PEFT (LoRA) with Unsloth's performance optimizations.
- **LoRA Rank (`r`):** 64
- **Format:** GGUF
- **Quantization:** Q4_K_M , Q8_0
- **context_window** 4096

**Llama-3.2-3B-small_Shiro_roleplay-gguf** is a fine-tuned version of Llama 3.2 3B Instruct, specifically crafted to be a master of high-concept, witty immersive , and darkly , intense creative writing.

This isn't your average storyteller. Trained on a curated dataset of absurd and imaginative scenarios—from sentient taxidermy raccoons to cryptid dating apps—this model excels at generating unique characters, crafting engaging scenes, and building fantastical worlds with a distinct, cynical voice. If you need a creative partner to brainstorm the bizarre, this is the model for you.

This model was fine-tuned using the Unsloth library for peak performance and memory efficiency.

**Provided files:**
*   LoRA adapter for use with the base model.
*   **GGUF (`q4_k_m`)** version for easy inference on local machines with `llama.cpp`, LM Studio, Ollama, etc.

## 💡 Intended Use & Use Cases

This model is designed for creative and entertainment purposes. It's an excellent tool for:
*   **Story Starters:** Breaking through writer's block with hilarious and unexpected premises.
*   **Character Creation:** Generating unique character bios with strong, memorable voices.
*   **Scene Generation:** Writing short, punchy scenes in a dark comedy or absurd fantasy style.
*   **Roleplaying:** Powering a game master or character with a witty, unpredictable personality.
*   **Creative Brainstorming:** Generating high-concept ideas for stories, games, or scripts.

📝 Prompting Format
This model follows the official Llama 3.1 Instruct chat template. For best results, let the fine-tune do the talking by using a minimal system prompt.

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{your_system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{your_user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```