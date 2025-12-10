---
license: mit
task_categories:
- text-classification
language:
- en
- hi
pretty_name: discord-phishing-scam-detection
tags:
- discord
- moderation
- chat
- user-generated-content
- nlp
- scam
- phishing
- messages
size_categories:
- 1K<n<10K
---

# Discord Scam / Clean Messages Dataset

## 📌 Context  
This dataset contains real-world messages from my Discord server, labeled to support the fine-tuning of BERT/DistilBERT base models for phishing and scam detection.

---

## 💡 Inspiration  
Traditional Discord moderation bots rely on static keyword rules set by server owners, but scammers easily evade these filters by subtly altering spellings, using homoglyphs, and other tricks.  
To address this, I built an NLP-powered moderation bot by fine-tuning DistilBERT (base uncased) on labeled chat data to recognize scam and phishing messages beyond simple keywords.  
The model is deployed as a real-time bot that actively monitors and filters malicious content.  
You can find out more here → [GitHub Repository](https://github.com/wang-yuancheng/shibemod)

---

## 📥 Origin & Collection

- **Source**: Private Discord community  
- **Extraction**: Collected using a `discord.py` script crawling channel histories  
- **Initial pool**: ~80,000 raw messages

---

## 🧹 Content & Filtering  
Messages were collected and filtered using the following rules:

- Messages with fewer than 3 words were dropped  
- Messages sent by bots were excluded  
- System messages, embeds, and stickers were ignored  
- Duplicate messages from the same user were deduplicated (only the first kept)  
- Messages with over 70% Unicode symbols or emoji were removed

This process reduced the dataset to under 20,000 high-quality messages.  
Additional scam messages were then manually added to improve coverage of common phishing patterns and tactics.

---

## 🔧 Pre-processing

To preserve structure while ensuring privacy and model robustness, certain tokens were normalized:

- External links → `<URL>`  
- User mentions → `<USER>`  
- Custom emojis → `<EMOJI>`  
- Discord invite links → `<DISCORD_INVITE>`

---

## 🏷️ Labelling

- `label`  
  - `0` = clean (normal user messages)  
  - `1` = scam (phishing links, fake Nitro, crypto scams, spam bursts)

**Class Balance**:  
- Clean messages: 1630  
- Scam messages: 201 
- Positive rate: ~11%

---

## 📊 Features

| Name         | Type   | Description                       |
|--------------|--------|-----------------------------------|
| `label`      | int    | 0 = clean, 1 = scam               |
| `msg_content`| string | Cleaned Discord message content   |

There are **no missing values** in this dataset.

---

## 📈 Intended Use

This dataset is suitable for:

- Binary text classification (clean vs scam)
- Fine-tuning transformer models (e.g. BERT, DistilBERT)
- Real-time moderation tools and bot development
- Experimenting with threshold-based softmax post-processing

---

## 🔒 License

MIT License
