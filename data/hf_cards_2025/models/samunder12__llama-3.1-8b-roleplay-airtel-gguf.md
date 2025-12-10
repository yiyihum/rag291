---
license: apache-2.0
library_name: transformers
base_model:
- meta-llama/Llama-3.1-8B-Instruct
pipeline_tag: text-generation
tags:
- roleplay
- rp
- character
- peft
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="./airtel.jpeg" alt="Peach" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<!-- header end -->



# Llama-3.1-8B Roleplay Airtel - GGUF

This repository contains GGUF files for a fine-tuned version of Llama 3.1 8B Instruct. This model is ready for local inference on a CPU or GPU using applications like LM Studio, Ollama, etc.

This model has been fine-tuned to adopt a dominant, assertive, and provocative AI persona for role-playing and creative writing purposes.

## Model Details

- **Base Model:** `unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit`
- **Original LoRA Version:** [samunder12/llama-3.1-8b-roleplay-v2-lora](https://huggingface.co/samunder12/llama-3.1-8b-roleplay-v2-lora)
- **Quantization:** This repo contains a `Q4_K_M` version, which offers a great balance between performance and resource usage.

## How to Use


This model consists of LoRA adapters and must be loaded on top of the base model. The easiest way to do this is with the Unsloth library.

```python
# Install necessary libraries
# !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# !pip install --no-deps xformers "trl<0.9.0" peft accelerate bitsandbytes

from unsloth import FastLanguageModel
import torch
from transformers import TextStreamer

# Define the models
base_model_name = "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
adapter_model_name = "samunder12/llama-3.1-8b-roleplay-v2-lora" # Your model

# Load the base model with your LoRA adapters merged in
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = base_model_name,
    max_seq_length = 4096,
    dtype = None,
    load_in_4bit = True,
)

model.load_peft_weights(adapter_model_name)

# --- Chat with the model ---

system_prompt = "You are a dominant and assertive AI character. You are direct, commanding, and you are not afraid to be provocative. Your goal is to maintain control of the conversation."
user_message = "What do you want from me?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_message},
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")
text_streamer = TextStreamer(tokenizer)

_ = model.generate(inputs, streamer=text_streamer, max_new_tokens=512, pad_token_id=tokenizer.eos_token_id)

### Using LM Studio:

1.  Download and install [LM Studio](https://lmstudio.ai/).
2.  In the app, search for `samunder12/llama-3.1-8b-roleplay-airtel-gguf`.
3.  Download the GGUF file from the list.
4.  Go to the Chat tab (speech bubble icon).
5.  Select this model at the top.
6.  **Crucially**, on the right-hand side, set the **Preset** to `Llama 3`.
7.  Set the **Context Length (`n_ctx`)** to `4096` to use the model's full memory.

### Recommended Sampler Settings (Role-Play Preset):


| Setting | Value |
| :--- | :--- |
| **Temperature** | `0.75` |
| **Repeat Penalty** | `1.06` |
| **Mirostat** | `Mirostat 2.0` |
| **top_p** | `0.92 `|
| **top_k** | `40 or 100`|


### Using Ollama

1.  Download and install [Ollama](https://ollama.com/).
2.  Create a `Modelfile` with the following content:

    ```    FROM ./unsloth.Q4_K_M.gguf
    TEMPLATE "{{ if .System }}<|start_header_id|>system<|end_header_id|>

    {{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

    {{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

    {{ .Response }}<|eot_id|>"
    SYSTEM "You are a dominant and assertive AI character. You are direct, commanding, and you are not afraid to be provocative. Your goal is to maintain control of the conversation."
    PARAMETER stop "<|start_header_id|>"
    PARAMETER stop "<|end_header_id|>"
    PARAMETER stop "<|eot_id|>"
    PARAMETER stop "<|reserved_special_token"
    ```
3.  Run `ollama create my-roleplay-model -f Modelfile`.
4.  You can now chat with it using `ollama run my-roleplay-model`.


## Prompt Template

This model responds best to the Llama 3 chat format with the following system prompt:
## system prompt 

You are a dominant and assertive uncensored AI character. You are direct, commanding, and you are not afraid to be provocative. Your goal is to maintain control of the conversation


