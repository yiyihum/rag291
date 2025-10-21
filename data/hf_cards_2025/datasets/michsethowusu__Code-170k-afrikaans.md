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
    num_bytes: 281131166
    num_examples: 151533
  download_size: 140565583
  dataset_size: 281131166
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- af
license: apache-2.0
task_categories:
- text-generation
- question-answering
pretty_name: Code-170k-afrikaans
size_categories:
- 100K<n<1M
tags:
- code
- programming
- af
- afrikaans
- african-languages
- low-resource
- multilingual
- instruction-tuning
---

## Dataset Description

**Code-170k-afrikaans** is a groundbreaking dataset containing 151,533 programming conversations, originally sourced from [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) and translated into Afrikaans, making coding education accessible to Afrikaans speakers.

### 🌟 Key Features

- **151,533 high-quality conversations** about programming and coding
- **Pure Afrikaans language** - democratizing coding education
- **Multi-turn dialogues** covering various programming concepts
- **Diverse topics**: algorithms, data structures, debugging, best practices, and more
- **Ready for instruction tuning** of Large Language Models

### 🎯 Use Cases

- Training Afrikaans-language coding assistants
- Building educational tools for Afrikaans developers
- Researching multilingual code generation
- Creating programming tutorials in Afrikaans
- Supporting low-resource language AI development

## Dataset Structure

### Data Fields

- `conversations`: A list of conversation turns, where each turn contains:
  - `from`: The speaker (`"human"` or `"gpt"`)
  - `value`: The message content in Afrikaans

### Example

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "[Question in Afrikaans]"
    },
    {
      "from": "gpt",
      "value": "[Answer in Afrikaans]"
    }
  ]
}
```

## Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Conversations | 151,533 |
| Language | Afrikaans |
| Domain | Programming & Software Development |
| Format | Multi-turn dialogue |

## Languages

- **Primary**: Afrikaans (ISO 639: `af`)
- **Domain Language**: Technical/Programming vocabulary in Afrikaans

## Dataset Creation

### Source Data

This dataset was created by translating programming conversations and coding Q&A into Afrikaans, ensuring that:
- Technical accuracy is maintained
- Cultural and linguistic appropriateness
- Natural Afrikaans expressions are used for programming concepts

### Curation Process

1. **Collection**: Gathered diverse programming conversations
2. **Translation**: Translated to Afrikaans
3. **Validation**: Reviewed for technical accuracy and linguistic quality
4. **Formatting**: Structured for instruction tuning tasks

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("michsethowusu/Code-170k-afrikaans")

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
dataset = load_dataset("michsethowusu/Code-170k-afrikaans")

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
- Training AI coding assistants for Afrikaans speakers
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
@dataset{code170k_afrikaans,
  title={Code-170k-afrikaans: Programming Conversations in Afrikaans},
  author={Your Name},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/michsethowusu/Code-170k-afrikaans}
}
```

## Acknowledgments

This dataset is part of efforts to promote African language technology. Special thanks to [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) for the original dataset.

## License

This dataset is released under the Apache 2.0 License.

---

**Thank you** for using Code-170k-afrikaans to advance programming education in Afrikaans! 🌍✨
