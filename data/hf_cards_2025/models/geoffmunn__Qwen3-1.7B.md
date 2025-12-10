---
license: apache-2.0
tags:
- gguf
- qwen
- qwen3-1.7b
- qwen3-1.7b-gguf
- llama.cpp
- quantized
- text-generation
- chat
- reasoning
base_model: Qwen/Qwen3-1.7B
author: geoffmunn
pipeline_tag: text-generation
language:
- en
- zh
---

# Qwen3-1.7B-GGUF

This is a **GGUF-quantized version** of the **[Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B)** language model — a balanced **1.7-billion-parameter** LLM designed for **efficient local inference with strong reasoning and multilingual capabilities**.

Converted for use with `llama.cpp`, [LM Studio](https://lmstudio.ai), [OpenWebUI](https://openwebui.com), [GPT4All](https://gpt4all.io), and more.

> 💡 **Key Features of Qwen3-1.7B**:
> - 🤔 Supports **thinking mode** (`<think>...</think>`) for step-by-step logic, math, and coding.
> - ⚡ Can switch dynamically between **thinking** and **non-thinking** modes via `/think` and `/no_think`.
> - 🧰 Agent-ready: excels at tool calling and integration (via Qwen-Agent, MCP).
> - 🌍 Multilingual: fluent in 100+ languages including Chinese, English, Spanish, Arabic, Japanese.

## Available Quantizations (from f16)

These variants were built from a **f16** base model to ensure consistency across quant levels.

| Level     | Speed     | Size     | Recommendation                                                         |
|-----------|-----------|----------|------------------------------------------------------------------------|
| Q2_K      | ⚡ Fastest | 880 MB   | 🚨 **DO NOT USE** Did not return results for most questions.           |
| Q3_K_S    | ⚡ Fast    | 1.0 GB   | 🥉 Got good results across all question types.                         |
| Q3_K_M    | ⚡ Fast    | 1.07 GB  | Not recommended, did not appear in the top 3 models on any question.   |
| Q4_K_S    | 🚀 Fast   | 1.24 GB  | 🥈 Runner up. Got very good results across all question types.          |
| Q4_K_M    | 🚀 Fast   | 1.28 GB  | 🥉 Got good results across all question types.                          |
| Q5_K_S    | 🐢 Medium | 1.44 GB  | Made some appearances in the top 3, good for low-temperature questions. |
| Q5_K_M    | 🐢 Medium | 1.47 GB  | Not recommended, did not appear in the top 3 models on any question.    |
| Q6_K      | 🐌 Slow   | 1.67 GB  | Made some appearances in the top 3 across a range of temperatures.      |
| Q8_0      | 🐌 Slow   | 2.17 GB  | 🥇 **Best overall model.** Highly recommended for all query types.      |

## Model anaysis and rankings

I have run each of these models across 6 questions, and ranked them all based on the quality of the anwsers. 
**Qwen3-1.7B:Q8_0** is the best model across all question types, but you could use a smaller sized model such as **Qwen3-1.7B:Q4_K_S** and also get excellent results.

You can read the results here: [Qwen3-1.7b-analysis.md](Qwen3-1.7b-analysis.md)

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

1. `wget https://huggingface.co/geoffmunn/Qwen3-1.7B/resolve/main/Qwen3-1.7B-f16%3AQ8_0.gguf` (replace the quantised version with the one you want)
2. `nano Modelfile` and enter these details (again, replacing Q8_0 with the version you want):
```text
FROM ./Qwen3-1.7B-f16:Q8_0.gguf

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

3. Then run this command: `ollama create Qwen3-1.7B-f16:Q8_0 -f Modelfile`

You will now see "Qwen3-1.7B-f16:Q8_0" in your Ollama model list.

These import steps are also useful if you want to customise the default parameters or system prompt.

## Author

👤 Geoff Munn (@geoffmunn)  
🔗 [Hugging Face Profile](https://huggingface.co/geoffmunn)

## Disclaimer

This is a community conversion for local inference. Not affiliated with Alibaba Cloud or the Qwen team.
