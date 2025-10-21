---
license: mit
task_categories:
- text-generation
- question-answering
- instruction-following
language:
- en
tags:
- reasoning
- chain-of-thought
- cot
- synthetic
- instruction-tuning
- thinking
- openhermes
- gemini
size_categories:
- 100K<n<1M
pretty_name: OpenHermes Reasoning 377K
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: thinking
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 115572000
    num_examples: 231144
  download_size: 92457600
  dataset_size: 115572000
---

# 🧠 OpenHermes Reasoning 231K

<div align="center">

![Dataset Size](https://img.shields.io/badge/examples-231,144-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Quality](https://img.shields.io/badge/quality-high-brightgreen)
![Format](https://img.shields.io/badge/format-JSONL-orange)

**High-quality instruction dataset with chain-of-thought reasoning**

[🤗 Dataset](https://huggingface.co/datasets/limeXx/openhermes-reasoning-231k) • [💬 Discussions](https://huggingface.co/datasets/limeXx/openhermes-reasoning-231k/discussions)

</div>

---

## 📊 Dataset Overview

This dataset contains **231,144** high-quality instruction-response pairs with explicit chain-of-thought reasoning. Each example includes:

- **Prompt**: Original instruction or question
- **Thinking**: Explicit reasoning process and logical steps
- **Answer**: Final comprehensive response

### Key Features

✅ **Quality Filtered**: Rigorous validation and deduplication  
✅ **Reasoning Chains**: Explicit thinking process for each response  
✅ **Diverse Topics**: Wide range of instruction types  
✅ **Clean Format**: Standardized JSONL with consistent structure  
✅ **Production Ready**: Validated, deduplicated, and quality-checked

---

## 📈 Dataset Statistics

### Size Metrics
- **Total Examples**: 231,144
- **Average Prompt Length**: 258 chars (~64 tokens)
- **Average Thinking Length**: 873 chars (~218 tokens)
- **Average Answer Length**: 986 chars (~246 tokens)

### Question Type Distribution (estimated)
| Type | Count | Percentage |
|------|-------|------------|
| Factual | 151,653 | 65.6% |
| Explanatory | 20,017 | 8.7% |
| Reasoning | 11,094 | 4.8% |
| Creative | 4,206 | 1.8% |
| Coding | 508 | 0.2% |
| Other | 43,663 | 18.9% |

---

## 🏗️ Dataset Structure

### Data Fields

```python
{
    "prompt": str,     # Input instruction/question
    "thinking": str,   # Chain-of-thought reasoning
    "answer": str      # Final response
}
```

### Example

```json
{
  "prompt": "What is the capital of France and why is it historically significant?",
  "thinking": "France is a Western European country. Its capital is Paris, which has been the capital since the late 10th century. Paris is historically significant as a center of art, culture, philosophy, and politics. It played crucial roles in the French Revolution, the Enlightenment, and continues to be a global cultural hub.",
  "answer": "The capital of France is Paris. It is historically significant as a major center of art, culture, and politics for over a millennium. Paris was central to the French Revolution, the Enlightenment era, and has influenced global culture, fashion, cuisine, and philosophy. Today it remains one of the world's most important cultural and economic centers."
}
```

---

## 🚀 Quick Start

### Load Dataset

```python
from datasets import load_dataset

# Load full dataset
dataset = load_dataset("limeXx/openhermes-reasoning-231k")

# Access examples
for example in dataset['train'][:5]:
    print("Prompt:", example['prompt'])
    print("Thinking:", example['thinking'])
    print("Answer:", example['answer'])
    print("-" * 80)
```

### Fine-tuning Format

```python
# Convert to instruction format
def format_example(example):
    return f"""<|im_start|>user
{example['prompt']}<|im_end|>
<|im_start|>assistant
Thinking: {example['thinking']}

Answer: {example['answer']}<|im_end|>"""

# Or separate thinking/answer
formatted = dataset.map(lambda x: {"text": format_example(x)})
```

### Using with Training Frameworks

```python
# Hugging Face Transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

tokenizer = AutoTokenizer.from_pretrained("your-base-model")
model = AutoModelForCausalLM.from_pretrained("your-base-model")

# Tokenize dataset
def tokenize(example):
    return tokenizer(
        format_example(example),
        truncation=True,
        max_length=2048
    )

tokenized_dataset = dataset.map(tokenize, remove_columns=dataset['train'].column_names)

# Train
trainer = Trainer(
    model=model,
    args=TrainingArguments(
        output_dir="./output",
        per_device_train_batch_size=4,
        learning_rate=2e-5,
        num_train_epochs=3,
    ),
    train_dataset=tokenized_dataset['train'],
)
trainer.train()
```

---

## 🎯 Use Cases

### 1. Training Reasoning Models
Fine-tune language models to produce explicit reasoning chains before answers.

### 2. Instruction Following
Improve model capability to follow diverse instructions across domains.

### 3. Chain-of-Thought Research
Study and develop chain-of-thought prompting techniques.

### 4. Data Augmentation
Use as additional training data for instruction-tuned models.

### 5. Evaluation Benchmarks
Create evaluation sets for reasoning and instruction-following capabilities.

---

## 🔬 Dataset Creation

### Source Data
- **Base Prompts**: Curated from OpenHermes 2.5 and WizardLM Instruct datasets
- **Selection Criteria**: Quality-based filtering for diverse, well-formed instructions
- **Deduplication**: Removed duplicate prompts to ensure uniqueness

### Generation Process
1. **Prompt Selection**: High-quality prompts from trusted instruction datasets
2. **Reasoning Generation**: Google Gemini 2.5 Flash with specialized prompting
3. **Quality Control**: Multi-stage validation and filtering
4. **Deduplication**: Hash-based duplicate removal
5. **Final Validation**: Format checking and edge case handling

### Quality Assurance
- ✅ Valid JSON format verification
- ✅ Length validation (minimum/maximum bounds)
- ✅ Error entry removal
- ✅ Placeholder text detection
- ✅ Duplicate prompt elimination
- ✅ Special character ratio checks
- ✅ Reasoning quality validation

---

## 📝 Citation

If you use this dataset, please cite:

```bibtex
@dataset{openhermes_reasoning_231k,
  title={OpenHermes Reasoning 231K},
  author={limeXx},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/limeXx/openhermes-reasoning-231k}}
}
```

### Acknowledgments

This dataset builds upon:
- **OpenHermes 2.5** by Teknium ([dataset](https://huggingface.co/datasets/teknium/OpenHermes-2.5))
- **WizardLM** by WizardLM Team ([dataset](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2))
- **Google Gemini 2.5 Flash** for reasoning generation

---

## ⚖️ License

MIT License - Free for commercial and research use

---

## 🤝 Contributing

Found an issue? Have suggestions? 
- Open an issue in the [Discussions](https://huggingface.co/datasets/limeXx/openhermes-reasoning-231k/discussions) tab
- Report data quality concerns
- Suggest improvements

---

## 📧 Contact

For questions or collaborations:
- 🤗 HuggingFace: [@limeXx](https://huggingface.co/limeXx)
- 💬 Discussions: [Dataset Discussions](https://huggingface.co/datasets/limeXx/openhermes-reasoning-231k/discussions)

---

<div align="center">

**⭐ If you find this dataset useful, please star the repository! ⭐**

Made with ❤️ by [limeXx](https://huggingface.co/limeXx)

</div>
