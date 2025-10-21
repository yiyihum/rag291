---
license: apache-2.0
tags:
- gguf
- qwen
- qwen3
- qwen3-4b
- qwen3-4b-gguf
- llama.cpp
- quantized
- text-generation
- reasoning
- agent
- chat
- multilingual
base_model: Qwen/Qwen3-4B
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

# Qwen3-4B-GGUF

This is a **GGUF-quantized version** of the **[Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B)** language model — a powerful **4-billion-parameter** LLM from Alibaba's Qwen series, designed for **strong reasoning, agentic workflows, and multilingual fluency** on consumer-grade hardware.

Converted for use with `llama.cpp`, [LM Studio](https://lmstudio.ai), [OpenWebUI](https://openwebui.com), [GPT4All](https://gpt4all.io), and more.

> 💡 **Key Features of Qwen3-4B**:
> - 🤔 Supports **thinking mode** (`<think>...<think>`) for math, coding, logic.
> - 🔁 Dynamically switch via `/think` and `/no_think` in conversation.
> - 🧰 Agent-ready: integrates seamlessly with tools via Qwen-Agent or MCP.
> - 🌍 Fluent in 100+ languages including Chinese, English, Arabic, Japanese, Spanish.
> - ⚙️ Balances performance and size — runs well on laptops with 16GB RAM.

## Available Quantizations (from f16)

These variants were built from a **f16** base model to ensure consistency across quant levels.

| Level     | Speed     | Size       | Recommendation                                                                                   |
|-----------|-----------|------------|--------------------------------------------------------------------------------------------------|
| Q2_K      | ⚡ Fastest | 1.9 GB     | 🚨 **DO NOT USE.** Worst results from all the 4B models.                                          |
| 🥈 Q3_K_S | ⚡ Fast    | 2.2 GB     | 🥈 Runner up. A very good model for a wide range of queries.                                      |
| 🥇 Q3_K_M | ⚡ Fast    | 2.4 GB     | 🥇 **Best overall model.** Highly recommended for all query types.                                |
| Q4_K_S    | 🚀 Fast   | 2.7 GB     | A late showing in low-temperature queries. Probably not recommended.                              |
| Q4_K_M    | 🚀 Fast   | 2.9 GB     | A late showing in high-temperature queries. Probably not recommended.                             |
| Q5_K_S    | 🐢 Medium | 3.3 GB     | Did not appear in the top 3 for any question. Not recommended.                                    |
| Q5_K_M    | 🐢 Medium | 3.4 GB     | A second place for a high-temperature question, probably not recommended.                         |
| Q6_K      | 🐌 Slow   | 3.9 GB     | Did not appear in the top 3 for any question. Not recommended.                                    |
| 🥉 Q8_0   | 🐌 Slow   | 5.1 GB     | 🥉 If you want to play it safe, this is a good option. Good results across a variety of questions. |

## Model anaysis and rankings

I have run each of these models across 6 questions, and ranked them all based on the quality of the anwsers. 
**Qwen3-4B:Q3_K_M** is the best model across all question types, but if you want to play it safe with a higher precision model, then you could consider using **Qwen3-4B:Q8_0**.

You can read the results here: [Qwen3-4b-analysis.md](Qwen3-4b-analysis.md)

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
