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
<img src="./Jio.jpeg" alt="Peach" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<!-- 



# Llama 3.1 8B - Assertive Role-Play (v3 GGUF)

This repository contains the GGUF version of the [v3 Assertive Role-Play LoRA model](https://huggingface.co/YourUsername/llama-3.1-8b-roleplay-v3-lora). <!--- <<< Change this link! --->

This model is designed for easy, local inference on CPUs and GPUs using llama.cpp-based software like **LM Studio** and **Ollama**.

The model embodies a dominant, assertive, and creative persona for role-playing and storytelling. It was fine-tuned on a multi-turn conversational dataset to enhance its coherence and memory.

## Model Details

*   **Original LoRA Model:** [`samunder12/llama-3.1-8b-roleplay-v3-lora`](https://huggingface.co/samunder12/llama-3.1-8b-roleplay-v3-lora) <!--- <<< Change this link! --->
*   **Quantization:** `Q4_K_M`. This method provides an excellent balance between model size, performance, and VRAM/RAM usage.
*   **Context Length:** `4096` tokens.

## Usage Instructions

### LM Studio (Recommended)

1.  Download and install [LM Studio](https://lmstudio.ai/).
2.  In the app, search for this model repo: `samunder12/llama-3.1-8b-roleplay-v3-gguf`. <!--- <<< Change this --->
3.  Download the GGUF file listed in the "Files" tab.
4.  Go to the Chat tab (💬 icon) and load the model you just downloaded.
5.  **CRITICAL:** On the right-hand panel, under "Prompt Format", select the **Llama 3** preset.
6.  Set the `Context Length (n_ctx)` to **4096**.
7.  Use the "Role-Play" sampler settings below for best results.

#### Recommended Sampler Settings (Role-Play Preset)

| Setting | Value |
| :--- | :--- |
| **Temperature** | `0.75` |
| **Repeat Penalty** | `1.06` |
| **Mirostat** | `Mirostat 2.0` |
| **top_p** | `0.92 `|
| **top_k** | `40 or 100`|

