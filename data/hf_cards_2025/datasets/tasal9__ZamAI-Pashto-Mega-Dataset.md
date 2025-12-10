---
license: apache-2.0
language:
- ps
pretty_name: ZamAI Pashto Mega Dataset
size_categories:
- 1M<n<10M
tags:
- pashto
- nlp
- instruction-tuning
- mt5
- zamai
- ai
- dataset
---

# 📚 ZamAI-Pashto-Mega-Dataset

**Author:** [Yaqoob Tasal](https://huggingface.co/tasal9)  
**Organization:** [ZamAI](https://huggingface.co/ZamAI) — AI for Pashto, Dari, and Afghan Languages  
**License:** Apache-2.0  

---

## 🌍 Overview

The **ZamAI-Pashto-Mega-Dataset** is the largest unified **Pashto language dataset** curated and cleaned by [ZamAI](https://huggingface.co/ZamAI).  
It merges multiple high-quality corpora into a single instruction-based format, designed to supercharge **Pashto NLP** — from translation and summarization to dialogue and content generation.

---

## 📦 Dataset Details

- **Language:** Pashto (`ps`)
- **Total Samples:** 4,903,859
- **Size Category:** 1M < n < 10M
- **Format:** Instruction-tuning JSONL
  - `instruction` → Task prompt or instruction (can be empty for raw text)
  - `input` → Source text (optional)
  - `response` → Target output text
  - `category` → Source label (`mc4`, `local_ps`, `packaged_ps`, `zamai`)
- **Data Quality:** Deduplicated, cleaned, and tokenized for large language model training.

---

## 🗂 Sources

1. **Pashto subset of mC4 dataset** (streamed & sampled)  
2. **Local Pashto corpora** (`data/ps.txt`)  
3. **Packaged Pashto corpora** (`packaged/ps/ps.txt`)  
4. **ZamAI’s curated instruction-tuning data** (covering education, religion, culture, business, and general QA)

---

## 🚀 Use Cases

This dataset is ideal for:

- Fine-tuning **mT5**, **BLOOM**, **LLaMA**, and other multilingual models in Pashto  
- Instruction-tuning for:
  - Text generation
  - Summarization
  - Machine translation
  - Question answering
  - Cultural and educational assistants
- Building **Pashto-first AI applications** with high fluency & contextual understanding

---

## 🏢 About ZamAI

**ZamAI** is an AI initiative building state-of-the-art tools for **Pashto, Dari, and Afghan languages**.  
We focus on:
- AI tutoring systems for Afghan students
- Cultural preservation through AI
- Language models, datasets, and open-source contributions

**Founder:** [Yaqoob Tasal](https://huggingface.co/tasal9) — Software Engineer & AI Innovator

---

## 📜 License

Released under **Apache 2.0 License**.  
Check individual source datasets for any additional restrictions.

---

## 📖 Citation

If you use this dataset, please cite:

```bibtex
@dataset{zamai_pashto_mega_2025,
  author       = {Yaqoob Tasal},
  organization = {ZamAI},
  title        = {ZamAI-Pashto-Mega-Dataset},
  year         = {2025},
  url          = {https://huggingface.co/datasets/tasal9/ZamAI-Pashto-Mega-Dataset},
  license      = {Apache-2.0}
}