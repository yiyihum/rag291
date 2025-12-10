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

A small but carefully-curated dataset for **binary text-classification**:
> _“Is this Discord message trying to scam / spam users?”_

It is intended as a starting point for fine-tuning lightweight BERT-style models that moderate real-time chat servers.

---

## 1 Origin & Collection

* **Source servers** – private Discord communities (11 k members in total) run by the author.
* **Period** – 2024-01-01 → 2025-06-01.
* **Extraction** – Discord.py script iterated channel history
* **Initial pool** – ≈ 80 000 raw messages.

### 1.1 Filtering rules

| rule | rationale |
|------|-----------|
| `len(msg.content.split()) > 3` | drop 1-word noise / reactions |
| `m.author.bot == False` | skip bot output |
| `m.type == DEFAULT` | ignore system, embeds, stickers |
| deduplicate **identical text _by the same user_** | keep only first occurrence |
| **Unicode sanity** | drop messages whose code-points are > 70 % symbols / emoji |

After rules ⇒ **~20 k** candidate messages.

### 1.2 Labelling

* **Classes**
* `0 = clean` – ordinary human chat.
* `1 = scam` – phishing, fake giveaways, Nitro scams, crypto “airdrops”, credential-stealers, classic spam bursts, etc.
* **Class balance** – 1722 clean / 278 scam (≈ 13.81 % positives).
---

## 2 Features
- name: msg_content # original message text
type: string
- name: msg_timestamp # message epoch-ms (int64)
type: int64
- name: usr_joined_at # author join epoch-ms (int64, blank ↔ unknown)
type: int64
- name: time_since_join # seconds between join & message
type: float32
- name: message_length # raw character count
type: int32
- name: word_count # tokenised by whitespace
type: int32
- name: has_link # 1 if “http” substring
type: int8
- name: has_mention # 1 if any <@…> mention
type: int8
- name: num_roles # number of Discord roles (blank ↔ not a member obj)
type: int32
- name: label # 0 = clean • 1 = scam / spam
type: class_label

There are missing values in this dataset.