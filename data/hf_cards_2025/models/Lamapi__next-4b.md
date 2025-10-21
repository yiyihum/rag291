---
language:
- tr
- en
- de
- ka
- el
- ku
- es
- sl
- sk
- af
- da
- nl
- fa
- fi
- fr
- ga
- hi
- hu
- hy
- ja
- kg
- kk
- ko
- ky
- la
- lb
- id
- it
- is
- za
- zh
- zu
- cs
- vi
- be
- bg
- bs
- ne
- mn
- rm
- ro
- ru
- te
- th
- tk
- tt
- uk
- uz
- ug
- pl
- pt
- 'no'
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
- 4b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- language
- multilingual
- multimodal
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat
- generative-ai
- optimized
- unsloth
- trl
- sft
- chemistry
- code
- biology
- finance
- legal
- music
- art
- state-of-the-art
- climate
- medical
- agent
- text-generation-inference
- merge
- dense
pipeline_tag: text-generation
library_name: transformers
---

<img src='assets/banner.png'>

# 🚀 Next 4B (s330)

### *Türkiye’s First Vision-Language Model — Efficient, Multimodal, and Reasoning-Focused* 

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Language: English](https://img.shields.io/badge/Language-Multilingual-red.svg)]()
[![HuggingFace](https://img.shields.io/badge/🤗-Lamapi/Next--4B-orange.svg)](https://huggingface.co/Lamapi/next-4b)

---

## 📖 Overview

**Next 4B** is a **4-billion parameter multimodal Vision-Language Model (VLM)** based on **Gemma 3**, fine-tuned to handle **both text and images** efficiently. It is **Türkiye’s first open-source vision-language model**, designed for: 

* Understanding and generating **text and image descriptions**.
* Efficient reasoning and context-aware multimodal outputs.
* Turkish support with multilingual capabilities.
* Low-resource deployment using **8-bit quantization** for consumer-grade GPUs. 

This model is ideal for **researchers, developers, and organizations** who need a **high-performance multimodal AI** capable of **visual understanding, reasoning, and creative generation**.

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

## 🚀 Installation & Usage

### Use with vision:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoProcessor
from PIL import Image
import torch

model_id = "Lamapi/next-4b"

model = AutoModelForCausalLM.from_pretrained(model_id)
processor = AutoProcessor.from_pretrained(model_id) # For vision.
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Read image
image = Image.open("image.jpg")

# Create a message in chat format
messages = [
  {"role": "system","content": [{"type": "text", "text": "You are Next-X1, a smart and concise AI assistant trained by Lamapi. Always respond in the user's language. Proudly made in Turkey."}]},

  {
      "role": "user","content": [{"type": "image", "image": image},
      {"type": "text", "text": "Who is in this image?"}
    ]
  }
]

# Prepare input with Tokenizer
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image], return_tensors="pt")

# Output from the model
output = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(output[0], skip_special_tokens=True))


```
<div style='width:700px;'>
  <img src='/Lamapi/next-4b/resolve/main/assets/image.jpg' style='height:192px;border-radius:16px;margin-left:225px;'>
  <div style='background-color:rgba(0,140,255,0.5);border-radius:16px;border-bottom-right-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;margin-left:250px;margin-top:-25px;margin-bottom:10px;'>
    Who is in this image?
  </div>
  <div style='background-color:rgba(42,42,40,0.7);border-radius:16px;border-bottom-left-radius:0px;padding:3px 10px;width:fit-content;max-width:400px;'>
  The image shows <strong>Mustafa Kemal Atatürk</strong>, the founder and first President of the Republic of Turkey.
  </div>
</div>

### Use without vision:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Lamapi/next-4b"
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

## 🎯 Goals

1. **Multimodal Intelligence:** Understand and reason over images and text.
2. **Efficiency:** Run on modest GPUs using 8-bit quantization. 
3. **Accessibility:** Open-source availability for research and applications.
4. **Cultural Relevance:** Optimized for Turkish language and context while remaining multilingual.

---

## ✨ Key Features

| Feature                           | Description                                                             |
| --------------------------------- | ----------------------------------------------------------------------- |
| 🔋 Efficient Architecture         | Optimized for low VRAM; supports 8-bit quantization for consumer GPUs.  | 
| 🖼️ Vision-Language Capable       | Understands images, captions them, and performs visual reasoning tasks. |
| 🇹🇷 Multilingual & Turkish-Ready | Handles complex Turkish text with high accuracy.                        |
| 🧠 Advanced Reasoning             | Supports logical and analytical reasoning for both text and images.     |
| 📊 Consistent & Reliable Outputs  | Reproducible responses across multiple runs.                            |
| 🌍 Open Source                    | Transparent, community-driven, and research-friendly.                   |

---

## 📐 Model Specifications

| Specification      | Details                                                                            |
| ------------------ | ---------------------------------------------------------------------------------- |
| Base Model         | Gemma 3                                                                       | 
| Parameter Count    | 4 Billion                                                                          | 
| Architecture       | Transformer, causal LLM + Vision Encoder                                           |
| Fine-Tuning Method | Instruction & multimodal fine-tuning (SFT) on Turkish and multilingual datasets    |
| Optimizations      | Q8_0, F16, F32 quantizations for low VRAM and high VRAM usage                       | 
| Modalities         | Text & Image                                                                       |
| Use Cases          | Image captioning, multimodal QA, text generation, reasoning, creative storytelling |

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute. Attribution is appreciated.

---

## 📞 Contact & Support


* 📧 **Email:** [lamapicontact@gmail.com](mailto:lamapicontact@gmail.com) 
* 🤗 **HuggingFace:** [Lamapi](https://huggingface.co/Lamapi) 

---

> **Next 4B** — Türkiye’s **first vision-language AI**, combining **multimodal understanding, reasoning, and efficiency**.

[![Follow on HuggingFace](https://img.shields.io/badge/Follow-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/Lamapi)