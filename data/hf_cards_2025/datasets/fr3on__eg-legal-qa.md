---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- ar
tags:
- legal
- arabic
- egypt
- egyptian-law
- qa
- legal-qa
- instruction-tuning
size_categories:
- 1K<n<10K
---

# Arabic Legal Dataset - Legal Question-Answering

## Dataset Description

Question-answering dataset for Arabic legal texts with instruction-following format for training conversational AI models.

This dataset contains 5,230 examples of qa data derived from Egyptian legal texts, including criminal law, civil law, procedural law, and personal status law. The dataset is designed for training and evaluating Arabic legal AI models.

### Dataset Summary

- **Language**: Arabic (Egyptian Legal)
- **Domain**: Legal texts and jurisprudence
- **Task**: question-answering, text-generation
- **Size**: 5,230 examples (6.5 MB)
- **Source**: Egyptian legal codes and statutes

## Dataset Structure

### Data Fields

- **instruction**: Task instruction in Arabic
- **input**: Legal question or query
- **output**: Expected answer or response
- **system**: System prompt defining the assistant's role
- **category**: Legal domain (criminal, civil, etc.)
- **difficulty**: Complexity level (basic, intermediate, advanced, expert)

### Data Example

```json
{
  "instruction": "أجب على السؤال القانوني التالي بناءً على القانون المصري",
  "input": "ما هي شروط صحة عقد الزواج؟",
  "output": "يشترط لصحة عقد الزواج في القانون المصري عدة شروط أساسية...",
  "system": "أنت مساعد قانوني متخصص في القانون المصري",
  "category": "personal_status",
  "difficulty": "intermediate"
}
```

### Data Statistics

| Statistic | Value |
|-----------|-------|
| Total Examples | 5,230 |
| Average Text Length | 77 characters |
| Vocabulary Size | ~9,294 unique terms |
| Dataset Size | 6.5 MB |


### Legal Domain Coverage

This dataset covers the following areas of Egyptian law: Criminal Law, Labor Law, Civil Law.


## Usage

### Loading the Dataset

```python
from datasets import load_dataset

dataset = load_dataset("fr3on/eg-legal-qa")

# Print basic info
print(f"Number of examples: {len(dataset['train'])}")
print(f"Features: {dataset['train'].features}")

# View first example
print(dataset['train'][0])
```

### Example Use Cases

- Fine-tuning Arabic language models for legal question-answering
- Training legal chatbots and virtual assistants
- Building conversational AI for legal consultation
- Educational tools for law students and professionals

## Dataset Creation

### Source Data

This dataset was created from Egyptian legal texts including:

- **Criminal Procedure Law** (قانون الإجراءات الجنائية) - 498 articles
- **Personal Status Law** (قانون الأحوال الشخصية) - 51 articles
- **Penal Code** (قانون العقوبات) - 497 articles

### Data Processing

1. **Text Extraction**: Legal articles extracted from official JSON sources
2. **Structure Parsing**: Hierarchical legal structure preserved
3. **Schema Conversion**: Converted to qa format
4. **Quality Control**: Validated for consistency and proper Arabic encoding

## Considerations for Use

### Intended Use

This dataset is intended for:
- Research in Arabic natural language processing
- Training legal AI models for Arabic text
- Educational purposes in computational linguistics
- Development of legal technology applications

### Limitations

- Contains only Egyptian legal texts (may not generalize to other Arabic legal systems)
- Reflects the specific legal framework and language of Egyptian law
- Should not be used as a substitute for professional legal advice
- May contain biases present in the original legal texts

## Citation

```bibtex
@dataset{arabic_legal_qa_2025,
  title={Arabic Legal Dataset - Legal Question-Answering},
  author={fr3on},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/fr3on/eg-legal-qa}
}
```

## License

This dataset is released under the Apache 2.0 License. The original legal texts are public domain.

## Acknowledgments

Created by [fr3on](https://huggingface.co/fr3on) as part of efforts to advance Arabic legal AI research.