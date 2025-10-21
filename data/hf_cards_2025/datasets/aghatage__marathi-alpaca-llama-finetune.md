---
language:
- mr
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- question-answering
- conversational
pretty_name: Marathi Alpaca for llama-finetune
tags:
- marathi
- instruction-tuning
- alpaca
- llama
- finetune
---

# Marathi Alpaca Dataset for llama-finetune

This dataset contains **48,897** high-quality Marathi instruction-following examples, converted to the llama-finetune format.

## Dataset Description

- **Language**: Marathi (मराठी)
- **Size**: 48,897 examples
- **Format**: JSONL with messages structure
- **Source**: Converted from [smallstepai/marathi-instruction-tuning-alpaca](https://huggingface.co/datasets/smallstepai/marathi-instruction-tuning-alpaca)
- **Use Case**: Supervised fine-tuning (SFT) for language models

## Format

Each line in the JSONL file contains:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "निरोगी राहण्यासाठी तीन टिपा द्या."
    },
    {
      "role": "assistant",
      "content": "1. संतुलित आणि पौष्टिक आहार घ्या..."
    }
  ]
}
```

## Usage

### Download

```python
from datasets import load_dataset

dataset = load_dataset("aghatage/marathi-alpaca-llama-finetune")
```

### With llama-finetune

```bash
# Download the JSONL file
wget https://huggingface.co/datasets/aghatage/marathi-alpaca-llama-finetune/resolve/main/marathi_alpaca_finetune.jsonl

# Use with llama-finetune
./llama-finetune \
    --model-base lfm2-350m \
    --train-data marathi_alpaca_finetune.jsonl \
    --output-dir ./output
```

## Data Quality

The dataset is translated from the high-quality Alpaca-Cleaned dataset, ensuring:
- ✅ Diverse instruction-following tasks
- ✅ Clean and well-formatted data
- ✅ Suitable for supervised fine-tuning
- ✅ Covers general knowledge and reasoning tasks

## Original Dataset

This dataset is a format conversion of [smallstepai/marathi-instruction-tuning-alpaca](https://huggingface.co/datasets/smallstepai/marathi-instruction-tuning-alpaca), which is a Marathi translation of the Alpaca dataset.

## Citation

If you use this dataset, please cite the original Alpaca and Marathi translation work:

```bibtex
@misc{marathi-alpaca-2024,
  author = {SmallStepAI},
  title = {Marathi Instruction Tuning Alpaca Dataset},
  year = {2024},
  publisher = {HuggingFace},
  url = {https://huggingface.co/datasets/smallstepai/marathi-instruction-tuning-alpaca}
}
```

## License

Apache 2.0 - Same as the original dataset

## Conversion

This dataset was converted using the conversion script available at the repository.
