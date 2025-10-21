---
license: apache-2.0
tags:
- merge
- mergekit
- lazymergekit
language:
- en
base_model:
- rootxhacker/Apollo-exp-8B
- mergekit-community/L3.1-Athena-k-8B
- mergekit-community/L3.1-Athena-l2-8B
- mergekit-community/L3.1-Athena-l-8B
- mergekit-community/L3.1-Athena-l3-8B
pipeline_tag: text-generation
library_name: transformers
---

# 🧠 ZeroXClem-Llama-3.1-8B-Athena-Apollo-exp

## Overview

**ZeroXClem-Llama-3.1-8B-Athena-Apollo-exp** is a powerful AI model built through **Model Stock merging** using [MergeKit](https://github.com/cg123/mergekit). It merges several of the most capable and nuanced Llama-3.1-based models available on **Hugging Face**, optimized for performance across **instruction-following, roleplay, logic, coding, and creative writing** tasks.

By fusing diverse fine-tuned architectures into a cohesive blended model, this creation delivers excellent generalist abilities while retaining specialized strengths.

---

## 🔧 Merge Details

- **Merge Method:** `model_stock`
- **Base Model:** [`mergekit-community/L3.1-Athena-l3-8B`](https://huggingface.co/mergekit-community/L3.1-Athena-l3-8B)
- **Dtype:** `bfloat16`
- **Tokenizer Source:** `mergekit-community/L3.1-Athena-l3-8B`

---

## 💡 Models Merged

The following models contribute to this powerful fusion:

- [`rootxhacker/Apollo-exp-8B`](https://huggingface.co/rootxhacker/Apollo-exp-8B) — A rich blend focused on alignment, DPO, and SFT instruction tuning across Llama-3.1 variants.
- [`mergekit-community/L3.1-Athena-k-8B`](https://huggingface.co/mergekit-community/L3.1-Athena-k-8B) — Roleplay and safety-aligned merge based on Meta's Llama-3.1 foundation.
- [`mergekit-community/L3.1-Athena-l2-8B`](https://huggingface.co/mergekit-community/L3.1-Athena-l2-8B) — LoRA-enhanced with long-context and creative capability merges.
- [`mergekit-community/L3.1-Athena-l-8B`](https://huggingface.co/mergekit-community/L3.1-Athena-l-8B) — Deeply infused with LoRA-based domain-specific models in logic, psychology, storytelling, and more.

---

## 🧪 Configuration

```yaml
name: ZeroXClem-Llama-3.1-8B-Athena-Apollo-exp
base_model: mergekit-community/L3.1-Athena-l3-8B
dtype: bfloat16
merge_method: model_stock
models:
  - model: rootxhacker/Apollo-exp-8B
  - model: mergekit-community/L3.1-Athena-k-8B
  - model: mergekit-community/L3.1-Athena-l2-8B
  - model: mergekit-community/L3.1-Athena-l-8B
tokenizer_source: mergekit-community/L3.1-Athena-l3-8B
```

---

## ✨ Features & Highlights

🔹 **Instruction-Following Prowess** — Merged from Tulu-aligned and instruct-tuned models like Apollo-exp and Athena-k for high-quality, context-aware responses.

🔹 **Immersive Roleplay & Personality** — Strong roleplay personas and emotional nuance thanks to Athena's diverse RP blends.

🔹 **Creative & Structured Generation** — Support for creative writing, long-context novelization, and formal logic modeling from l2/l3 integrations.

🔹 **Depth in Dialogue** — Enhanced ability to carry layered and philosophical conversation from Claude-style fine-tunes in Apollo-exp.

---

## 🎯 Use Cases

- **Conversational AI & Roleplay Bots**  
- **Formal Reasoning & Chain-of-Thought Tasks**  
- **Creative Writing & Storytelling Tools**  
- **Coding Assistants**  
- **Educational and Research Applications**

---

## 🛠️ Usage Instructions

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "ZeroXClem/Llama-3.1-8B-Athena-Apollo-exp"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

prompt = "Explain quantum entanglement like I'm 10 years old."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


### 🦙 Ollama Instructions

```bash
ollama run hf.co/ZeroXClem/Llama-3.1-8B-Athena-Apollo-exp-Q4_K_M-GGUF
```

---

## 🧭 Alignment & Ethics

⚠️ **Unfiltered Output**: This model is uncensored and may generate content outside of alignment norms. Please implement your own **moderation layers** when deploying in production environments.

⚠️ **Responsible Use**: Developers are encouraged to audit outputs and maintain ethical usage policies for downstream applications.

📜 **License**: Usage governed by the [Meta Llama 3.1 Community License](https://huggingface.co/meta-llama/Llama-3.1-8B).

---

## 💌 Feedback & Contributions

We welcome your feedback, benchmarks, and improvements! Please open an issue or PR to contribute or tag us in your results and projects.

---

**ZeroXClem Team | 2025**