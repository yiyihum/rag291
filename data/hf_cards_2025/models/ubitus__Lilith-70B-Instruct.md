---
base_model:
- meta-llama/Llama-3.3-70B-Instruct
license: llama3.3
language:
- zh
- en
library_name: transformers
extra_gated_fields:
  Company: text
  Country: country
  Specific date: date_picker
  I want to use this model for:
    type: select
    options:
    - Research
    - Education
    - label: Other
      value: other
---

# Overview

This model is a fine-tuned version of LLaMA 3.3 70B, optimized for multilingual benchmarks including TMMlu+, TMlu, and MMLU. The fine-tuning process focused on enhancing reasoning, comprehension, and domain-specific performance. This model was developed as part of an iterative pipeline leveraging large-scale datasets and Chain-of-Thought (CoT) methodologies.

---
# Key Features

	•	Base Model: LLaMA 3.3 70B
	•	Dataset Sources: Custom-generated using LLMs, focused on high-quality, multilingual tasks.
	•	Chain-of-Thought Fine-Tuning: Enhanced logical reasoning with curated datasets.

# Data Preparation

	1.	Custom Dataset Generation
	2.	Traditional Chinese Data Filtering


# Evaluation
Please checkout  [Open TW LLM Leaderboard](https://huggingface.co/spaces/yentinglin/open-tw-llm-leaderboard) for full and updated list.
| Model                                                       | TMMLU+    | TMLU                    | Function Calling |
| :---------------------------------------------------------- | :-------- | :---------------------- | :--------------- |
| [ubitus/Lilith-70B-Instruct](https://huggingface.co/ubitus/Lilith-70B-Instruct) | **76.06%** | 73.70%                  | ✅               |
| [Llama-3-Taiwan-70B-Instruct](https://huggingface.co/yentinglin/Llama-3-Taiwan-70B-Instruct) | 67.53%    | **74.76%**              | ✅               |
| [Qwen1.5-110B-Chat](https://huggingface.co/Qwen/Qwen1.5-110B-Chat) | 65.81%    | 75.69%                  | ✅               |
| [Yi-34B-Chat](https://huggingface.co/01-ai/Yi-34B-Chat)       | 64.10%    | 73.59%                  | ✅               |
| [Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct) | 62.75%    | 70.95%                  | ✅               |
| [Llama-3-Taiwan-8B-Instruct](https://huggingface.co/yentinglin/Llama-3-Taiwan-8B-Instruct) | 52.28%    | 59.50%                  | ✅               |
| [Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) | 52.16%    | 55.57%                  | ✅               |
| [Gemini-1.5-Pro](https://ai.google.dev/gemini-api/docs)       | 49.92%^   | 61.40% (5-shot)         | ✅               |
| [Breexe-8x7B-Instruct-v0_1](https://huggingface.co/MediaTek-Research/Breexe-8x7B-Instruct-v0_1) | 48.92%    | -                       | ❓               |
| [Breeze-7B-Instruct-v1_0](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v1_0) | 41.77%    | 55.57%                  | ❓               |
| [Llama3-TAIDE-LX-8B-Chat-Alpha1](https://huggingface.co/taide/Llama3-TAIDE-LX-8B-Chat-Alpha1) | 39.03%    | 47.30%                  | ❓               |
| [Claude-3-Opus](https://www.anthropic.com/api)                 | -         | 73.59% (5-shot)         | ✅               |
| [GPT4-o](https://platform.openai.com/docs/api-reference/chat/create)       | -         | 65.56% (0-shot), 69.88% (5-shot) | ✅               |

## This model is well-suited for:

	1.	Multilingual Comprehension Tasks: Designed to handle diverse languages and formats.
	2.	Domain-Specific Applications: Excels in logical reasoning and structured problem-solving.
	3.	Benchmarks and Testing: An excellent choice for academic and industrial evaluations in multilingual NLP.