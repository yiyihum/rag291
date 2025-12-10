---
language:
- en
tags:
- text-generation
- conversational
- instruction-tuning
- corporate-communication
task_categories:
- text-generation
- text2text-generation
size_categories:
- 1K<n<10K
---

# Corporate Speak Dataset

A comprehensive dataset for training models to transform between casual and professional corporate communication.

## Dataset Description

This dataset contains bidirectional transformations between casual language and corporate speak, with domain and seniority awareness.

### Features

- **Bidirectional**: Both casual→corporate and corporate→casual translations
- **Domain-specific**: 6 industries (tech, finance, consulting, healthcare, retail, manufacturing)
- **Seniority levels**: 4 levels from junior to executive
- **Conversation support**: Multi-turn dialogue examples
- **Real-world scenarios**: Interviews, meetings, emails, presentations

## Dataset Structure

Each example contains:
- `instruction`: The task description
- `input`: The text to transform
- `output`: The transformed text
- `text`: Pre-formatted for instruction tuning
- `context` (optional): Domain, seniority, and scenario metadata

### Data Splits

- Training: 80%
- Validation: 10%
- Test: 10%

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("phxdev/corporate-speak-dataset")

# Example
print(dataset['train'][0])
# {
#   'instruction': 'Transform to corporate speak',
#   'input': 'let's meet',
#   'output': 'Let's sync up to align on our objectives',
#   'text': '### Instruction: Transform to corporate speak\n### Input: let's meet\n### Response: Let's sync up to align on our objectives'
# }
```

## Model Training

This dataset is designed for fine-tuning language models, particularly with LoRA or QLoRA for efficient training.

### Recommended Models
- Mistral-7B-Instruct
- Llama-2-7B-chat
- Microsoft/DialoGPT

## Citation

```bibtex
@dataset{corporate_speak_dataset,
  author = {phxdev},
  title = {Corporate Speak Dataset},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/phxdev/corporate-speak-dataset}
}
```

## License

Apache 2.0
