---
license: apache-2.0
tags:
- gguf
- qwen
- qwen3
- qwen3-8b
- qwen3-8b-gguf
- llama.cpp
- quantized
- text-generation
- reasoning
- agent
- chat
- multilingual
base_model: Qwen/Qwen3-8B
author: geoffmunn
pipeline_tag: text-generation
language:
- en
- zh
- es
- fr
- de
- ru
- ar
- ja
- ko
- hi
---

# Qwen3-8B-GGUF

This is a **GGUF-quantized version** of the **[Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)** language model — an **8-billion-parameter** LLM from Alibaba's Qwen series, designed for **advanced reasoning, agentic behavior, and multilingual tasks**.

Converted for use with `llama.cpp` and compatible tools like OpenWebUI, LM Studio, GPT4All, and more.

> 💡 **Key Features of Qwen3-8B**:
> - 🤔 **Thinking Mode**: Use `enable_thinking=True` or `/think` for step-by-step logic, math, and code.
> - ⚡ **Non-Thinking Mode**: Use `/no_think` for fast, lightweight dialogue.
> - 🧰 **Agent Capable**: Integrates with tools via MCP, APIs, and plugins.
> - 🌍 **Multilingual Support**: Fluent in 100+ languages including Chinese, English, Spanish, Arabic, Japanese, etc.

## Available Quantizations (from f16)

These variants were built from a **f16** base model to ensure consistency across quant levels.

| Level     | Speed     | Size        | Recommendation                                                                        |
|-----------|-----------|-------------|---------------------------------------------------------------------------------------|
| Q2_K      | ⚡ Fastest | 3.28 GB     | Not recommended. Came first in the bat & ball question, no other appearances.         |
| 🥉Q3_K_S  | ⚡ Fast    | 3.77 GB     | 🥉 Came first and second in questions covering both ends of the temperature spectrum. |
| 🥇 Q3_K_M | ⚡ Fast    | 4.12 GB     | 🥇 **Best overall model.** Was a top 3 finisher for all questions except the haiku.   |
| 🥉Q4_K_S  | 🚀 Fast   | 4.8 GB      | 🥉 Came first and second in questions covering both ends of the temperature spectrum. |
| Q4_K_M    | 🚀 Fast   | 5.85 GB     | Came first and second in questions covering high temperature questions.               |
| 🥈 Q5_K_S | 🐢 Medium | 5.72 GB     | 🥈 A good second place. Good for all query types.                                     |
| Q5_K_M    | 🐢 Medium | 5.85 GB     | Not recommended, no appeareances in the top 3 for any question.                       |
| Q6_K      | 🐌 Slow   | 6.73 GB     | Showed up in a few results, but not recommended.                                      |
| Q8_0      | 🐌 Slow   | 8.71 GB     | Not recommended, Only one top 3 finish.                                               |

## Model anaysis and rankings

There are numerous good candidates - lots of different models showed up in the top 3 across all the quesionts. However, **Qwen3-8B-f16:Q5_K_M** was a finalist in all but one question so is the recommended model. **Qwen3-8B-f16:Q5_K_S** did nearly as well and is worth considering, 

The 'hello' question is the first time that all models got it exactly right. All models in the 8B range did well and it's mainly a question of what one works best on your hardware.

You can read the results here: [Qwen3-8b-analysis.md](Qwen3-8b-analysis.md)

If you find this useful, please give the project a ❤️ like.

## Usage

Load this model using:
- [OpenWebUI](https://openwebui.com) – self-hosted AI interface with RAG & tools
- [LM Studio](https://lmstudio.ai) – desktop app with GPU support and chat templates
- [GPT4All](https://gpt4all.io) – private, local AI chatbot (offline-first)
- Or directly via `llama.cpp`

Each quantized model includes its own `README.md` and shares a common `MODELFILE` for optimal configuration.

Importing directly into Ollama should work, but you might encounter this error: `Error: invalid character '<' looking for beginning of value`.
In this case try these steps:

1. `wget https://huggingface.co/geoffmunn/Qwen3-4B/resolve/main/Qwen3-4B-f16%3AQ3_K_M.gguf` (replace the quantised version with the one you want)
2. `nano Modelfile` and enter these details (again, replacing Q3_K_M with the version you want):
```text
FROM ./Qwen3-4B-f16:Q3_K_M.gguf

# Chat template using ChatML (used by Qwen)
SYSTEM You are a helpful assistant

TEMPLATE "{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>{{ end }}<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>

# Default sampling
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER min_p 0.0
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 4096
```

The `num_ctx` value has been dropped to increase speed significantly.

3. Then run this command: `ollama create Qwen3-4B-f16:Q3_K_M -f Modelfile`

You will now see "Qwen3-4B-f16:Q3_K_M" in your Ollama model list.

These import steps are also useful if you want to customise the default parameters or system prompt.

## Author

👤 Geoff Munn (@geoffmunn)  
🔗 [Hugging Face Profile](https://huggingface.co/geoffmunn)

## Disclaimer

This is a community conversion for local inference. Not affiliated with Alibaba Cloud or the Qwen team.
