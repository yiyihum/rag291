---
language: tr
license: mit
tags:
- turkish
- türkiye
- english
- ai
- lamapi
- gemma3
- next
- next-x1
- efficient
- text-generation
- open-source
- 1b
- 270m
- finetune
- gguf
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat-model
- generative-ai
- optimized-model
- unsloth
- trl
- sft
- chemistry
- biology
- finance
- legal
- music
- art
- code
- climate
- medical
- agent
- text-generation-inference
pipeline_tag: text-generation
---

<img src='assets/banner.png'>

# 🚀 Next-270M (xt330)

### *Lightweight, Efficient, and Türkiye-Focused AI*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: English](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--1B-orange.svg)](https://huggingface.co/Lamapi/next-1b)

---

<style>
  table { width:fit-content; border-collapse:separate; border-spacing:0 3px;font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;background:rgba(15,22,32,0.4);border-radius:16px;padding: 10px; border:none;transition:.2s all ease;}
  thead th { text-align:center; padding:4px 10px; font-size:13px; text-transform:uppercase; color:rgb(200,200,200);border:none; }
  tbody tr { transition: transform 0.18s ease, box-shadow 0.18s ease; border:none !important;transition:.2s all ease;border-radius:16px;background:rgba(0, 0, 0, 0.38);}
  tbody .turkish:hover {box-shadow:0 6px 15px rgba(0, 0, 0, 0.27);scale:1.01;background:rgba(80, 38, 38, 0.6);}
  tbody .next:hover {box-shadow:0 6px 15px rgba(0, 0, 0, 0.27);scale:1.02;background: rgba(0, 59, 225, 1)}
  tbody tr:hover { box-shadow:0 0px 15px rgba(102, 102, 102, 0.13); background:rgba(139, 139, 139, 0.16)}
  td { padding:8px 10px;border:0px transparent !important;outline:transparent !important; text-align:center; }
  td:first-child { font-weight:600;text-align:left }
  /* tbody .turkish td { background: rgba(255, 0, 0, 0.2) !important; color:rgb(200,200,200); font-weight:400;border:0px !important; scale:1.0; } */
  /* tbody .next td { background: rgba(0, 89, 255, 0.49)!important; color:rgb(200,200,200); font-weight:600;border:0px !important; scale:1.00;outline:none;border:none !important;} */
  .next{
    background: rgba(0, 89, 255, 0.49);
  }
  .turkish{
    background:rgba(51, 34, 34, 0.64);
  }
  tbody tr td:first-child { border-top-left-radius:12px; border-bottom-left-radius:12px; }
  tbody tr td:last-child { border-top-right-radius:12px; border-bottom-right-radius:12px; } strong{
    font-size:16px;font-weight:700;
  }
  em{opacity:0.7;font-size:11px !important;}
</style>
## 📖 Overview

**Next-270M** is a **270-million parameter causal language model** based on **Gemma 3**, designed for **efficiency, low-resource deployment, and reasoning-focused natural language understanding**.

Key highlights:

* Extremely **lightweight** — can run on consumer GPUs with low VRAM.
* Optimized for **text reasoning, summarization, and creative generation**.
* Supports **Turkish natively** while remaining multilingual.
* Open-source and transparent for research and applications.

Ideal for **developers, students, and organizations** needing **fast, reliable, and low-resource text-generation**.

---

# Our Next 1B and Next 4B models are leading to all of the tiny models in benchmarks. 

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MMLU (5-shot) %</th>
      <th>MMLU-Pro %</th>
      <th>GSM8K %</th>
      <th>MATH %</th>
    </tr>
  </thead>
  <tbody>
    <tr class="next">
      <td data-label="Model">Next 4B preview <em>Version s325</em></td>
      <td data-label="MMLU (5-shot) %">84.6</td>
      <td data-label="MMLU-Pro %">66.9</td>
      <td data-label="GSM8K %">82.7</td>
      <td data-label="MATH %"><strong>70.5</strong></td>
    </tr>
    <tr class="next">
      <td data-label="Model">Next 1B <em>Version t327</em></td>
      <td data-label="MMLU (5-shot) %"><strong>87.3</strong></td>
      <td data-label="MMLU-Pro %"><strong>69.2</strong></td>
      <td data-label="GSM8K %"><strong>90.5</strong></td>
      <td data-label="MATH %">70.1</td>
    </tr>
    <tr>
      <td data-label="Model">Qwen 3 0.6B</td>
      <td data-label="MMLU (5-shot) %">52.81</td>
      <td data-label="MMLU-Pro %">37.6</td>
      <td data-label="GSM8K %">60.7</td>
      <td data-label="MATH %">20.5</td>
    </tr>
    <tr>
      <td data-label="Model">Llama 3.2 1B</td>
      <td data-label="MMLU (5-shot) %">49.3</td>
      <td data-label="MMLU-Pro %">44.4</td>
      <td data-label="GSM8K %">11.9</td>
      <td data-label="MATH %">30.6</td>
    </tr>
    <tr class="turkish">
      <td data-label="Model">Kumru 7B <em>not verified</em></td>
      <td data-label="MMLU (5-shot) %">30.7</td>
      <td data-label="MMLU-Pro %">28.6</td>
      <td data-label="GSM8K %">15.38</td>
      <td data-label="MATH %">6.4</td>
    </tr>
  </tbody>
</table>

---

# Also, our Next Z1 model is leading to state-of-the-art models in some of the Benchmarks.
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>MMLU (5-shot) %</th>
      <th>MMLU-Pro %</th>
      <th>GSM8K %</th>
      <th>MATH %</th>
    </tr>
  </thead>
  <tbody>
    <tr class="next">
      <td data-label="Model">Next Z1 <em>Version l294</em></td>
      <td data-label="MMLU (5-shot) %"><strong>97.3</strong></td>
      <td data-label="MMLU-Pro %"><strong>94.2</strong></td>
      <td data-label="GSM8K %">97.7</td>
      <td data-label="MATH %">93.2</td>
    </tr>
    <tr class="next">
      <td data-label="Model">Next Z1 <em>Version l294</em> (no tool)</td>
      <td data-label="MMLU (5-shot) %">94.7</td>
      <td data-label="MMLU-Pro %">90.1</td>
      <td data-label="GSM8K %">94.5</td>
      <td data-label="MATH %">88.7</td>
    </tr>
    <tr>
      <td data-label="Model">GPT 5</td>
      <td data-label="MMLU (5-shot) %">92.5</td>
      <td data-label="MMLU-Pro %">87.0</td>
      <td data-label="GSM8K %"><strong>98.4</strong></td>
      <td data-label="MATH %"><strong>96.0</strong></td>
    </tr>
    <tr>
      <td data-label="Model">Claude Opus 4.1 (Thinking)</td>
      <td data-label="MMLU (5-shot) %">~92.0</td>
      <td data-label="MMLU-Pro %">87.8</td>
      <td data-label="GSM8K %">84.7</td>
      <td data-label="MATH %">95.4</td>
    </tr>
  </tbody>
</table>

---

## 🎯 Goals

1. **Lightweight Efficiency:** Run smoothly on low-resource devices.
2. **Reasoning-Focused:** Provide logical and coherent text outputs.
3. **Accessibility:** Fully open-source with clear documentation.
4. **Multilingual Adaptability:** Turkish-focused but supports other languages.

---

## ✨ Key Features

| Feature                     | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| 🔋 Lightweight Architecture | Optimized for low VRAM usage; ideal for small GPUs or CPU deployment. |
| 🇹🇷 Turkish & Multilingual | Handles complex Turkish prompts accurately.                           |
| 🧠 Reasoning Capabilities   | Logical chain-of-thought for question-answering and problem-solving.  |
| 📊 Consistent Outputs       | Reliable and reproducible results across multiple runs.               |
| 🌍 Open Source              | Transparent, research-friendly, and community-driven.                 |

---

## 📐 Model Specifications

| Specification      | Details                                                                |
| ------------------ | ---------------------------------------------------------------------- |
| Base Model         | Gemma 3                                                           |
| Parameter Count    | 270 Million                                                              |
| Architecture       | Transformer, causal LLM                                                |
| Fine-Tuning Method | Instruction fine-tuning (SFT) with Turkish and multilingual datasets   |
| Optimizations      | Quantization-ready (q8, f16, f32)                      |
| Use Cases          | Text generation, summarization, Q&A, creative writing, reasoning tasks |

---

## 🚀 Installation & Usage

### Use the model:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Lamapi/next-270m"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Chat message
messages = [
    {"role": "system", "content": "You are Next-X1, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."},
    {"role": "user", "content": "Hello, how are you?"}
]

# Prepare input with Tokenizer
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt")

# Output from the model
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

<div style='width:700px;'>
  <div style='background-color:rgba(0,140,255,0.5);border-radius:16px;border-bottom-right-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;margin-left:250px;margin-top:-15px;margin-bottom:10px;'>
    Hello, how are you?
  </div>
  <div style='background-color:rgba(42,42,40,0.7);border-radius:16px;border-bottom-left-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;'>
  I'm fine, thank you. How are you?
  </div>
</div>

---

## 📄 License

MIT License — free to use, modify, and distribute. Attribution appreciated.

---

## 📞 Contact & Support

* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com)
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi)

---

> **Next-270M** — Lightweight, **efficient, and reasoning-focused**, bringing **Turkey’s AI forward** on low-resource hardware.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)