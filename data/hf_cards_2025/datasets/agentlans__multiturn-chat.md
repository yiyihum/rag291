---
language:
- en
configs:
- config_name: chats_k1000
  data_files:
  - path:
    - chats_k1000.jsonl.zst
    split: train
  default: true
- config_name: chats_k10000
  data_files:
  - path:
    - chats_k10000.jsonl.zst
    split: train
- config_name: chats_k30000
  data_files:
  - path:
    - chats_k30000.jsonl.zst
    split: train
- config_name: chats_k50000
  data_files:
  - path:
    - chats_k50000.jsonl.zst
    split: train
- config_name: magpie-ultra
  data_files:
  - path:
    - magpie-ultra.jsonl.zst
    split: train
- config_name: ultrachat
  data_files:
  - path:
    - ultrachat.jsonl.zst
    split: train
- config_name: wildchat
  data_files:
  - path:
    - wildchat.jsonl.zst
    split: train
- config_name: infinity-instruct
  data_files:
  - path:
    - infinity-instruct.jsonl.zst
    split: train
task_categories:
- text-generation
---
