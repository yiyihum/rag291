---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- rp
- roleplay
- creative
- creative writing
- writing
- deslop
- prose
- flesch
- gemini
---
# Qwill RP CreativeWriting Reasoning Dataset

## 📝 Dataset Summary

**Qwill-RP-CreativeWriting-Reasoning** is a creative writing dataset focused on structured reasoning. Each row contains a fictional or narrative prompt sourced from [`nothingiisreal/Reddit-Dirty-And-WritingPrompts`](https://huggingface.co/datasets/nothingiisreal/Reddit-Dirty-And-WritingPrompts), along with an AI-generated response that includes:

- **Reasoning**, wrapped in `<think>...</think>`
- **Final Answer**, wrapped in `<answer>...</answer>`

The goal is to train or evaluate models on chain-of-thought prompting within creative or storytelling domains.

---

## 📊 Dataset Preview

- **Total Rows:** ~3,000  
- **Columns:**
  - `prompt`: The prompt given to the model.
  - `model_used`: The model that generated the response.
  - `gemini`: The structured response, with reasoning and final answer.
  - `temperature`: Temperature used in generation (randomly sampled, 0.1–1.2).
  - `top_k`: Top-k value used (sampled from: 20, 40, 50, 64, 80, 90, 100).
  - `top_p`: Top-p value used (sampled from: 0.8, 0.85, 0.9, 0.95, 1.0).

---

## ⚙️ Generation Methodology

We employed **random sampling** of generation parameters to avoid overly deterministic or excessively creative outputs:

- **Temperature:** Sampled from a continuous range between `0.1` and `1.3`.
- **Top-k:** Randomly chosen from `[20, 40, 50, 64, 80, 90, 100]`.
- **Top-p:** Randomly chosen from `[0.8, 0.85, 0.9, 0.95, 1.0]`.

This encourages stylistic and logical variety across responses while maintaining narrative relevance and coherence.

---

## 🎯 Purpose

The dataset aims to:

- Explore creative generation grounded in step-by-step reasoning.
- Provide training material for models that simulate internal thought before output.
- Serve as a benchmark or augmentation resource for CoT (Chain of Thought) based generation tasks.

---

## ⚠️ Limitations
- Prompts were inherited from a public Reddit-based dataset, and may include adult or NSFW content. Filtering is advised for sensitive applications.

---

## 💡 Use Cases

- Fine-tuning or evaluating models on **reasoning-augmented creative generation**.
- Developing **storytelling models** with logical structure.
- Research in **narrative reasoning** and **step-by-step AI output planning**.

---