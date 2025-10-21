---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
language:
- ru
- kk
pretty_name: Telegram Corpus KAZ_RU
size_categories:
- 10M<n<100M
---

# 📦 Telegram Corpus KAZ_RU

**Telegram Corpus KAZ_RU** is a raw multilingual dataset of Telegram messages in Russian and Kazakh, collected and assembled by **Kurumikz**. It contains over 1.4 million lines of informal, user-generated text extracted from a large `.txt` dump. The corpus is intended for experimentation in text generation, language modeling, and dialogue research.

---

## 📊 Dataset Statistics

| Metric                      | Value        | Description |
|----------------------------|--------------|-------------|
| 📄 Lines                   | 1,493,124    | Total number of lines/messages |
| 📦 Characters              | 33,753,922   | All characters including spaces and punctuation |
| 🅰️ Letters (total)        | 22,867,523   | All alphabetic characters |
| 🔠 Latin letters           | 3,997,388    | English and other Latin-based letters |
| 🔡 Cyrillic letters        | 18,761,717   | Russian, Kazakh, and other Cyrillic letters |
| 🌐 Other alphabets         | 108,418      | Non-Latin/Cyrillic (e.g. Arabic, emoji, etc.) |
| 🔢 Digits                  | 1,730,772    | All numeric characters |
| ␣ Spaces                  | 3,904,045    | Whitespace characters |
| • Periods                 | 456,884      | Sentence-ending punctuation |
| , Commas                  | 203,237      | Mid-sentence punctuation |
| 🧩 Tokens (space-split)    | 4,623,188    | Approximate token count using space delimiter |

---

## ⚠️ Notes & Warnings

This dataset is a **raw prototype** and has not been manually cleaned or annotated. It may contain:

- Profanity, offensive language, and slang
- Excessive whitespace and empty lines
- Unstructured formatting, broken links, usernames, emojis
- Mixed language usage (primarily Russian and Kazakh)
- Repetitive or low-quality content

Use with caution for downstream tasks. Preprocessing is recommended before training or evaluation.

---

## 🧠 Intended Use

This corpus is suitable for:

- Pretraining or fine-tuning LLMs (e.g. CompactLLM)
- Studying informal multilingual text
- Dialogue modeling and Telegram-style generation
- Feature extraction and embedding training
- Language modeling in Russian and Kazakh

---

## 📄 License

This dataset is licensed under **CC BY-NC-SA 4.0**.

- You must credit the author: **Kurumikz**
- Commercial use is **not allowed**
- Any derivative work must be shared under the same license

Full license text: [Creative Commons Attribution-NonCommercial-ShareAlike 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)