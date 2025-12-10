---
pretty_name: WildChat Reversed (OpenPipe format)
tags:
- text-generation
- instruction-finetuning
- chat
- openpipe
dataset_info:
  features:
  - name: conversations
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: conversation_hash
    dtype: string
  - name: model
    dtype: string
  - name: timestamp
    dtype: string
  - name: turn
    dtype: int64
  - name: language
    dtype: string
  - name: toxic
    dtype: bool
  - name: redacted
    dtype: bool
  - name: state
    dtype: string
  - name: country
    dtype: string
  - name: hashed_ip
    dtype: string
  - name: header
    dtype: string
  splits:
  - name: train
    num_bytes: 3063931.2
    num_examples: 450
  - name: test
    num_bytes: 340436.8
    num_examples: 50
  download_size: 1620467
  dataset_size: 3404368.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# deepfates/wildchat-reversed-500

This dataset is a role-reversed transformation of `allenai/WildChat-4.8M` for OpenPipe-style chat fine-tuning:
- Drops conversations where any user/human message is empty (to avoid empty assistant messages post-flip)
- Removes empty messages and single-exchange conversations
- Flips user/human ↔ assistant/ai/bot (system stays system)
- Ensures each conversation ends with an assistant message
- Outputs entries as JSONL with a `messages` array compatible with OpenPipe

## Schema

Each line is a JSON object with:
- `messages`: list of `{ "role": "system|user|assistant", "content": "..." }`
- optional `metadata` (e.g., `conversation_hash`, `model`)

## Source and License

Derived from `allenai/WildChat-4.8M` (License: ODC-BY). Please attribute the original authors as required by ODC-BY.
