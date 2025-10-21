---
license: mit
language:
- am
tags:
- amharic
- llm
- training
- ethiopia
- instruction-tuning
- african-languages
- deployment
- production
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- question-answering
- text2text-generation
- conversational
pretty_name: Amharic LLM Training Dataset
---

# Amharic LLM Training Dataset

**Complete production-ready Amharic dataset for large language model training and deployment.**

## 🚀 Quick Start for Deployment

```python
from datasets import load_dataset

# Load the complete dataset
dataset = load_dataset("YoseAli/amharic-llm-training-data")

# Access splits
train_data = dataset["train"]  # 761,501 samples
test_data = dataset["test"]    # 84,612 samples

print(f"Training samples: {len(train_data):,}")
print(f"Test samples: {len(test_data):,}")
```

## 📊 Dataset Information

- **Total samples**: 846,113
- **Training samples**: 761,501
- **Test samples**: 84,612
- **Language**: Amharic (am)
- **Format**: Instruction-response pairs
- **Quality**: Curated and validated
- **Sources**: Multi-source compilation (Walia-LLM, AYA, M2Lingual, AmQA, Masakhane)

## 🎯 Production Deployment

This dataset is optimized for:

- ✅ **LLM Fine-tuning**: Ready for transformer model training
- ✅ **Production Deployment**: Validated and production-ready
- ✅ **Scalable Training**: Supports distributed training
- ✅ **Quality Assured**: Curated from multiple high-quality sources

## 💻 Usage Examples

### Basic Loading
```python
from datasets import load_dataset

# Load dataset
dataset = load_dataset("YoseAli/amharic-llm-training-data")
training_data = dataset["train"]

# Convert to list for custom processing
train_list = training_data.to_list()
```

### Training Format
```python
# Format for instruction tuning
def format_for_training(example):
    if 'instruction' in example and 'output' in example:
        text = f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['output']}"
    elif 'text' in example:
        text = example['text']
    else:
        text = str(example)
    
    return {"text": text}

# Apply formatting
formatted_dataset = dataset.map(format_for_training)
```

### Streaming for Large Scale
```python
# For very large scale training
dataset = load_dataset("YoseAli/amharic-llm-training-data", streaming=True)
train_stream = dataset["train"]

# Process in batches
for batch in train_stream.iter(batch_size=1000):
    # Your training code here
    pass
```

## 🏗️ Model Training Pipeline

### 1. Data Preparation
```python
from datasets import load_dataset
from transformers import AutoTokenizer

# Load dataset
dataset = load_dataset("YoseAli/amharic-llm-training-data")
tokenizer = AutoTokenizer.from_pretrained("your-base-model")

# Tokenize
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)
```

### 2. Training Setup
```python
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer

# Load model
model = AutoModelForCausalLM.from_pretrained("your-base-model")

# Training arguments
training_args = TrainingArguments(
    output_dir="./amharic-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-5,
    save_steps=500,
    logging_steps=100,
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
)

# Start training
trainer.train()
```

## 📋 Data Format

Each sample contains:

```json
{
  "instruction": "Task or question in Amharic",
  "input": "Additional context (optional)",
  "output": "Expected response in Amharic",
  "source_dataset": "Original source (when available)"
}
```

## 🌍 Dataset Sources

This dataset combines multiple high-quality Amharic language resources:

1. **Walia-LLM**: Amharic instruction-following dataset
2. **AYA Amharic**: Cohere's multilingual dataset (Amharic subset)
3. **M2Lingual**: Cross-lingual dialogue dataset
4. **AmQA**: Amharic question-answering from Wikipedia
5. **Masakhane NLU**: African languages NLU benchmark

## 🚀 Deployment Ready

This dataset is ready for:

- **Production LLM training**
- **Commercial applications**
- **Research and development**
- **Community model building**
- **Educational purposes**

## 📈 Performance Expectations

Models trained on this dataset typically achieve:

- Strong Amharic language understanding
- Good instruction-following capabilities
- Diverse response generation
- Cultural and contextual awareness

## 📄 Citation

If you use this dataset in your work, please cite:

```bibtex
@dataset{amharic_llm_training_data,
  title={Amharic LLM Training Dataset},
  author={YoseAli},
  year={2024},
  url={https://huggingface.co/datasets/YoseAli/amharic-llm-training-data},
  note={Complete Amharic LLM training dataset from multiple curated sources}
}
```

## 📜 License

MIT License - Free for research and commercial use.

## 🤝 Acknowledgments

- EthioNLP community for Walia-LLM dataset
- Cohere for AYA multilingual dataset
- Masakhane community for African NLP resources
- All contributors to the original source datasets

## 📞 Contact

For questions, issues, or collaboration:
- Repository: [GitHub](https://github.com/Yosef-Ali/amharic-all-dataset-fine-tuning)
- Hugging Face: [@YoseAli](https://huggingface.co/YoseAli)

---

**Ready for production deployment! 🚀**
