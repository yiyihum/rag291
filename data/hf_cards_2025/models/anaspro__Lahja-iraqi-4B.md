---
language:
- ar
license: apache-2.0
base_model: google/gemma-3-4b
pipeline_tag: text-generation
tags:
- arabic
- iraqi
- lahja
- llm
- fine-tuning
- unsloth
- dialect
---

# Model Card for `Lahja-iraqi-4B`

**Lahja-iraqi-4B** is the **first Arabic–Iraqi large language model** built to understand and generate natural dialogue in the Iraqi dialect and broader spoken Arabic varieties.  
It represents the foundation of the *Lahja* project — an initiative to bring authentic regional Arabic communication into open-source AI.

This initial release focuses on **spoken fluency**, **contextual comprehension**, and **cultural tone adaptation**, enabling human-like Iraqi conversations while retaining Modern Standard Arabic understanding.

---

## 🧠 Model Details

### Model Description

- **Project name:** Lahja  
- **Version:** v0 (Initial public release)  
- **Purpose:** Build a truly Iraqi-aware conversational LLM  
- **Base model:** [google/gemma-3-4b](https://huggingface.co/google/gemma-3-4b)  
- **Languages:** Iraqi Arabic + MSA  
- **Parameters:** ~4 B  
- **Precision:** BF16 mixed precision  
- **Framework:** PyTorch / Transformers / PEFT / Unsloth  
- **License:** Apache-2.0  

### Model Sources

- **Repository:** [https://huggingface.co/yourusername/Lahja-iraqi-4B](https://huggingface.co/yourusername/Lahja-iraqi-4B)  
- **Demo:** Coming soon  

---

## 🔧 Intended Uses

### Direct Use
- Conversational agents fluent in Iraqi Arabic  
- Chatbots and assistants targeting Arabic dialect users  
- Educational and cultural preservation projects focused on Iraqi language usage  

### Downstream Use
- Additional fine-tuning for other dialects (e.g., Levantine, Gulf)  
- Domain adaptation for voice assistants, social-chat apps, and dialogue systems  

### Out-of-Scope
- Not intended for factual QA, medical, legal, or political decision-making.  
- Avoid using for generating harmful or biased outputs.

---

## ⚠️ Bias, Risks, and Limitations

- Regional dialect coverage may be uneven (Baghdadi dominates).  
- Informal vocabulary may appear in unintended contexts.  
- Not suitable for formal Arabic writing.  

**Recommendation:** Human review is required for critical deployments or production use.

---

## 🚀 Getting Started

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "yourusername/Lahja-iraqi-4B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)

prompt = "شلونك اليوم؟ الجو حار لو بارد؟"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=80)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🏋️ Training Details

### Dataset
- 200 K conversational pairs collected from Iraqi social and cultural contexts.  
- Covers colloquial expressions, idioms, and real-life dialogue forms.  
- Offensive and explicit data removed.  

### Training Setup
- **Hardware:** 1 × A100 40 GB GPU  
- **Optimizer:** AdamW  
- **Learning Rate:** 2e-4 (cosine decay)  
- **Batch Size:** 64 (global)  
- **Epochs:** 3  
- **Precision:** BF16 mixed  
- **Adapter Method:** LoRA (r = 8, α = 16)

---

## 📈 Evaluation

| Metric | Score | Description |
|---------|--------|-------------|
| Perplexity | 7.2 | On held-out Iraqi dialogue test set |
| Fluency (1-5) | 4.6 | Human evaluation for smoothness |
| Dialect Accuracy | 95 % | Correct use of Iraqi wording/structure |

---

## 🌿 Environmental Impact

- **Hardware:** NVIDIA A100 40 GB  
- **Runtime:** ≈ 5 hours  
- **Carbon Estimate:** ~1.8 kg CO₂eq (via [mlco2 calculator](https://mlco2.github.io/impact#compute))

---

## ⚙️ Technical Summary
**Frameworks:** PyTorch 2.3 / Transformers 4.55 / PEFT 0.11 / Unsloth 0.7  

---

## 📚 Citation

**APA:**
> Lahja-iraqi-4B (2025). An Arabic–Iraqi dialect language model for conversational understanding. Hugging Face Model Hub.

**BibTeX:**
```bibtex
@misc{lahjairaqi4b2025,
  title  = {Lahja-iraqi-4B: Arabic–Iraqi Dialect Large Language Model},
  year   = {2025},
  url    = {https://huggingface.co/yourusername/Lahja-iraqi-4B},
  note   = {First public release of the Lahja project, fine-tuned using Unsloth LoRA techniques}
}
```

---

## 🧩 Project Vision

Lahja-iraqi-4B is the **first step toward a family of open Arabic dialect models** — scalable, community-driven, and focused on realistic regional speech.  
Future releases (v1, v2...) aim to expand dialect coverage, improve factual grounding, and enable cross-dialect comprehension.

---

## 🧩 Model Card Authors
Anonymous Open-Source Contributor  

## 📬 Contact
For feedback or collaboration: open-source@protonmail.com  
