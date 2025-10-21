---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- ko
tags:
- korean
- translation
- distilqwen
- instruction-tuning
- conversation
size_categories:
- 100K<n<1M
---

# DistilQwen 100k Korean

This dataset is a Korean translation of the original [alibaba-pai/DistilQwen_100k](https://huggingface.co/datasets/alibaba-pai/DistilQwen_100k) dataset.

## Dataset Description

- **Original Dataset**: [alibaba-pai/DistilQwen_100k](https://huggingface.co/datasets/alibaba-pai/DistilQwen_100k)
- **Language**: Korean (ko)
- **Size**: ~100,000 samples
- **Format**: JSONL (JSON Lines)
- **Task**: Instruction tuning, conversational AI, question answering

## Dataset Structure

The dataset contains both English and Korean versions of instruction-response pairs:

```json
{
  "instruction": "Original English instruction text",
  "output": "Original English response/answer",
  "instruction_kr": "Korean translation of the instruction",
  "output_kr": "Korean translation of the response/answer",
  "_dataset_index": 30000
}
```

Each record contains:
- **instruction**: Original English instruction from the source dataset
- **output**: Original English response from the source dataset  
- **instruction_kr**: Korean translation of the instruction
- **output_kr**: Korean translation of the response
- **_dataset_index**: Index number from the original DistilQwen_100k dataset

## Translation Process

This dataset was created by translating the original English DistilQwen_100k dataset into Korean. The translation maintains the original structure and intent while adapting the content for Korean language use.

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("lcw99/DistilQwen_100k_korean")

# Access Korean translations
for example in dataset['train']:
    korean_instruction = example['instruction_kr']
    korean_response = example['output_kr']
    # Original English versions are also available
    english_instruction = example['instruction']
    english_response = example['output']
```

## Original Dataset Citation

If you use this dataset, please also cite the original DistilQwen_100k dataset:

```bibtex
@misc{distilqwen_100k,
  title={DistilQwen_100k},
  author={Alibaba PAI Team},
  year={2024},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/alibaba-pai/DistilQwen_100k}}
}
```

## License

This dataset follows the same license as the original dataset (Apache 2.0).

## Acknowledgments

- Original dataset creators: Alibaba PAI Team
- Translation: lcw99

## Contact

For questions or issues related to this Korean translation, please contact the repository maintainer.