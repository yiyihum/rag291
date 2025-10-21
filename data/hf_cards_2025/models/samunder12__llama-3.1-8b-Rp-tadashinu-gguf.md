---
library_name: transformers
language: en
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
- llama-3.1
- instruct
- creative-writing
- storytelling
---



<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="./tadashinu.jpg" alt="Peach" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>



# llama-3.1-8b-Rp-tadashinu-gguf  - A dark , immersive , dialogue ready , High-Concept Storyteller and Roleplayer


## Model Details

- **Base Model:** `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
- **Original LoRA Model:** [`samunder12/llama-3.1-8b-roleplay-v5-lora`](https://huggingface.co/samunder12/llama-3.1-8b-roleplay-v5-lora)
- **Fine-tuning Method:** PEFT (LoRA) with Unsloth's performance optimizations.
- **LoRA Rank (`r`):** 64
- **Format:** GGUF
- **Quantization:** Q4_K_M
- **context_window** 4096

**llama-3.1-8b-Rp-tadashinu-gguf** is a fine-tuned version of Llama 3.1 8B Instruct, specifically crafted to be a master of high-concept, witty immersive , and darkly , intense creative writing.

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

## 🔧 How to Use

### With Transformers (and Unsloth)

This model is a LoRA adapter. You must load it on top of the base model, `unsloth/meta-llama-3.1-8b-instruct-bnb-4bit`.

```python
from unsloth import FastLanguageModel
from transformers import TextStreamer

model_repo = "samunder12/llama-3.1-8b-roleplay-v5-lora"
base_model_repo = "unsloth/meta-llama-3.1-8b-instruct-bnb-4bit"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = model_repo,
    base_model = base_model_repo,
    max_seq_length = 4096,
    dtype = None,
    load_in_4bit = True,
)

# --- Your system prompt ----
system_prompt = "You are a creative and witty storyteller." # A simple prompt is best
user_message = "A timid barista discovers their latte art predicts the future. Describe a chaotic morning when their foam sketches start depicting ridiculous alien invasions."

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_message},
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")
text_streamer = TextStreamer(tokenizer)
_ = model.generate(inputs, streamer=text_streamer, max_new_tokens=512)

```

With GGUF
The provided GGUF file (q4_k_m quantization) can be used with any llama.cpp compatible client, such as:
LM Studio: Search for your model name **samunder12/llama-3.1-8b-Rp-tadashinu-gguf** directly in the app.
Ollama: Create a Modelfile pointing to the local GGUF file.
text-generation-webui: Place the GGUF file in your models directory and load it.
Remember to use the correct Llama 3.1 Instruct prompt template.



📝 Prompting Format
This model follows the official Llama 3.1 Instruct chat template. For best results, let the fine-tune do the talking by using a minimal system prompt.

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{your_system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{your_user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```
