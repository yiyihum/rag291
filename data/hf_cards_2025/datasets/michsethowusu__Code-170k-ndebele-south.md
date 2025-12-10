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
    num_bytes: 93344984
    num_examples: 176994
  download_size: 46672492
  dataset_size: 93344984
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- nr
license: apache-2.0
task_categories:
- text-generation
- question-answering
pretty_name: Code-170k-ndebele-south
size_categories:
- 100K<n<1M
tags:
- code
- programming
- nr
- ndebele-(south)
- african-languages
- low-resource
- multilingual
- instruction-tuning
---

## Dataset Description

**Code-170k-ndebele-south** is a groundbreaking dataset containing 176,994 programming conversations, originally sourced from [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) and translated into Ndebele (South), making coding education accessible to Ndebele (South) speakers.

### 🌟 Key Features

- **176,994 high-quality conversations** about programming and coding
- **Pure Ndebele (South) language** - democratizing coding education
- **Multi-turn dialogues** covering various programming concepts
- **Diverse topics**: algorithms, data structures, debugging, best practices, and more
- **Ready for instruction tuning** of Large Language Models

### 🎯 Use Cases

- Training Ndebele (South)-language coding assistants
- Building educational tools for Ndebele (South) developers
- Researching multilingual code generation
- Creating programming tutorials in Ndebele (South)
- Supporting low-resource language AI development

## Dataset Structure

### Data Fields

- `conversations`: A list of conversation turns, where each turn contains:
  - `from`: The speaker (`"human"` or `"gpt"`)
  - `value`: The message content in Ndebele (South)

### Example

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "[Question in Ndebele (South)]"
    },
    {
      "from": "gpt",
      "value": "[Answer in Ndebele (South)]"
    }
  ]
}
```

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Conversations | 176,994 |
| Language | Ndebele (South) |
| Domain | Programming & Software Development |
| Format | Multi-turn dialogue |

## Languages

- **Primary**: Ndebele (South) (ISO 639: `nr`)
- **Domain Language**: Technical/Programming vocabulary in Ndebele (South)

## Dataset Creation

### Source Data

This dataset was created by translating programming conversations and coding Q&A into Ndebele (South), ensuring that:
- Technical accuracy is maintained
- Cultural and linguistic appropriateness
- Natural Ndebele (South) expressions are used for programming concepts

### Curation Process

1. **Collection**: Gathered diverse programming conversations
2. **Translation**: Translated to Ndebele (South)
3. **Validation**: Reviewed for technical accuracy and linguistic quality
4. **Formatting**: Structured for instruction tuning tasks

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("michsethowusu/Code-170k-ndebele-south")

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
dataset = load_dataset("michsethowusu/Code-170k-ndebele-south")

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
- Training AI coding assistants for Ndebele (South) speakers
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
@dataset{code170k_ndebele_south,
  title={Code-170k-ndebele-south: Programming Conversations in Ndebele (South)},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/michsethowusu/Code-170k-ndebele-south}
}
```

## Acknowledgments

This dataset is part of efforts to promote African language technology. Special thanks to [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) for the original dataset.

## License

This dataset is released under the Apache 2.0 License.

---

**Thank you** for using Code-170k-ndebele-south to advance programming education in Ndebele (South)! 🌍✨
