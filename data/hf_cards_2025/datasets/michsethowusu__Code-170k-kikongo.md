---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 207135866
    num_examples: 111609
  download_size: 103567933
  dataset_size: 207135866
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- kg
license: apache-2.0
task_categories:
- text-generation
- question-answering
pretty_name: Code-170k-kikongo
size_categories:
- 100K<n<1M
tags:
- code
- programming
- kg
- kikongo
- african-languages
- low-resource
- multilingual
- instruction-tuning
---

## Dataset Description

**Code-170k-kikongo** is a groundbreaking dataset containing 111,609 programming conversations, originally sourced from [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) and translated into Kikongo, making coding education accessible to Kikongo speakers.

### 🌟 Key Features

- **111,609 high-quality conversations** about programming and coding
- **Pure Kikongo language** - democratizing coding education
- **Multi-turn dialogues** covering various programming concepts
- **Diverse topics**: algorithms, data structures, debugging, best practices, and more
- **Ready for instruction tuning** of Large Language Models

### 🎯 Use Cases

- Training Kikongo-language coding assistants
- Building educational tools for Kikongo developers
- Researching multilingual code generation
- Creating programming tutorials in Kikongo
- Supporting low-resource language AI development

## Dataset Structure

### Data Fields

- `conversations`: A list of conversation turns, where each turn contains:
  - `from`: The speaker (`"human"` or `"gpt"`)
  - `value`: The message content in Kikongo

### Example

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "[Question in Kikongo]"
    },
    {
      "from": "gpt",
      "value": "[Answer in Kikongo]"
    }
  ]
}
```

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Conversations | 111,609 |
| Language | Kikongo |
| Domain | Programming & Software Development |
| Format | Multi-turn dialogue |

## Languages

- **Primary**: Kikongo (ISO 639: `kg`)
- **Domain Language**: Technical/Programming vocabulary in Kikongo

## Dataset Creation

### Source Data

This dataset was created by translating programming conversations and coding Q&A into Kikongo, ensuring that:
- Technical accuracy is maintained
- Cultural and linguistic appropriateness
- Natural Kikongo expressions are used for programming concepts

### Curation Process

1. **Collection**: Gathered diverse programming conversations
2. **Translation**: Translated to Kikongo
3. **Validation**: Reviewed for technical accuracy and linguistic quality
4. **Formatting**: Structured for instruction tuning tasks

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("michsethowusu/Code-170k-kikongo")

# Access training data
train_data = dataset['train']

# Example: Print first conversation
print(train_data[0]['conversations'])
```

### Training Example

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

# Load dataset
dataset = load_dataset("michsethowusu/Code-170k-kikongo")

# Load model and tokenizer
model_name = "your-base-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Format conversation for training
def format_conversation(example):
    conversation = example['conversations']
    formatted = ""
    for turn in conversation:
        role = "User" if turn['from'] == 'human' else "Assistant"
        formatted += f"{role}: {turn['value']}\n\n"
    return {"text": formatted}

# Apply formatting
formatted_dataset = dataset.map(format_conversation)
```

## Ethical Considerations

### Intended Use

✅ **Recommended Uses:**
- Training AI coding assistants for Kikongo speakers
- Educational programming tools
- Research in multilingual code generation
- Promoting digital literacy

❌ **Not Recommended:**
- Training models for harmful or unethical purposes
- Use without proper attribution
- Commercial use without reviewing license terms

### Limitations

- The dataset focuses on programming/coding domain
- May not cover all programming languages or frameworks equally
- Translation quality may vary across technical complexity levels

## Citation

If you use this dataset in your research or projects, please cite:

```bibtex
@dataset{code170k_kikongo,
  title={Code-170k-kikongo: Programming Conversations in Kikongo},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/michsethowusu/Code-170k-kikongo}
}
```

## Acknowledgments

This dataset is part of efforts to promote African language technology. Special thanks to [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) for the original dataset.

## License

This dataset is released under the Apache 2.0 License.

---

**Thank you** for using Code-170k-kikongo to advance programming education in Kikongo! 🌍✨
