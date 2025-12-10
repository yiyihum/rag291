---
dataset_info:
  features:
  - name: uuid
    dtype: string
  - name: category
    dtype: string
  - name: version
    dtype: string
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: translation_metadata
    struct:
    - name: durations_ms
      list: float64
    - name: translation_ids
      list: string
  splits:
  - name: train
    num_bytes: 2443554127
    num_examples: 445287
  download_size: 1240111151
  dataset_size: 2443554127
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: odc-by
size_categories:
- 100K<n<1M
language:
- nl
- en
tags:
- machine-translation
- conversational-ai
- dutch
- chat
- nemotron
task_categories:
- text-generation
---

# Nemotron Post-Training Dataset (Dutch Translation)

Machine-translated Dutch version of NVIDIA's Nemotron Post-Training Dataset, specifically the chat conversations.

## Dataset Details

- **Source**: [`nvidia/Nemotron-Post-Training-Dataset-v2`](https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2) (chat split)
- **Translation**: English → Dutch using [`Unbabel/Tower-Plus-9B`](https://huggingface.co/Unbabel/Tower-Plus-9B)
- **Size**: 445,287 conversations with 1,327,548 total messages
- **Format**: Conversational data with original structure preserved

## Dataset Statistics

- **Total conversations**: 445,287
- **Total messages**: 1,327,548  
- **Average messages per conversation**: 2.98
- **Message role distribution**:
  - System: 444,567 messages
  - User: 443,054 messages  
  - Assistant: 439,927 messages

## Schema

Each conversation contains:
- `uuid`: Unique conversation identifier from original dataset
- `category`: Content category (all "chat" for this split)
- `version`: Dataset version ("v2")
- `messages`: Array of message objects with:
  - `role`: Message role (system/user/assistant)
  - `content`: Machine-translated Dutch message content
- `translation_metadata`: Translation process metadata including job IDs and durations

## Quality Notice

⚠️ **This is machine-translated content.** Translation quality varies and has not been manually reviewed. While the Tower-Plus-9B model provides high-quality translations, some artifacts or inconsistencies may remain. The original thinking tokens (`<think></think>`) have been preserved and cleaned from any Dutch translation artifacts.

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("pdelobelle/nemotron-translated-conversations")

# Access a conversation
conversation = dataset['train'][0]
print(f"Conversation {conversation['uuid']} has {len(conversation['messages'])} messages")

# Iterate through messages
for message in conversation['messages']:
    print(f"{message['role']}: {message['content']}")
```

## Translation Process

The translation was performed by:
1. Extracting individual messages from the original conversation format
2. Translating each message using the Tower-Plus-9B model
3. Reconstructing conversations while preserving original metadata
4. Cleaning translation artifacts (Dutch `<denk>` tokens replaced with English `<think>`)

## License

This dataset inherits the ODC-By license from the original Nemotron dataset. You are free to:
- Share and use the dataset for any purpose
- Create works based on the dataset  
- Modify, transform and build upon the dataset

With the requirement to:
- Give appropriate credit to the original NVIDIA Nemotron creators
- Indicate if changes were made

## Citation

If you use this dataset, please cite both the original Nemotron dataset and acknowledge the translation work:

```bibtex
@misc{nemotron-dutch-translation,
  title={Nemotron Post-Training Dataset (Dutch Translation)},
  author={Pieter Delobelle},
  year={2025},
  note={Dutch translation of NVIDIA Nemotron Post-Training Dataset using Tower-Plus-9B}
}
```

Original Nemotron dataset:
```bibtex
@misc{nvidia-nemotron-dataset,
  title={Nemotron Post-Training Dataset v2},
  author={NVIDIA},
  year={2024},
  url={https://huggingface.co/datasets/nvidia/Nemotron-Post-Training-Dataset-v2}
}
```
```