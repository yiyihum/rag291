---
tags:
- vedic-philosophy
- sanskrit
- instruction-tuning
- synthetic-dataset
- question-answering
license: apache-2.0
language:
- en
- sa
pretty_name: Bhagwat Corpus
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: original_hf_id
    dtype: string
  - name: sanskrit_shloka
    dtype: string
  - name: english_translation
    dtype: string
  - name: generated_question
    dtype: string
  - name: generated_explanation
    dtype: string
  - name: generation_status
    dtype: string
  splits:
  - name: train
  - name: test
  - name: validation
---

# Bhagwat Corpus

## Dataset Summary
The **Bhagwat Corpus** is a synthetic dataset of approximately 90,000 examples designed for instruction-tuning large language models (LLMs) to generate Vedic philosophical responses grounded in scriptural tradition. Each example consists of:
- A synthetic user question
- A relevant Sanskrit shloka (verse) from the Mahabharata or Ramayana
- An English translation of the shloka
- A generated explanation and status for the response

The dataset is based on the Itihasa corpus (Aralikatte et al., 2021), which provides Sanskrit-English shloka pairs from the Mahabharata and Ramayana. The Bhagwat Corpus augments this with synthetic questions and explanations, making it suitable for culturally aware, spiritually aligned conversational AI.

## Supported Tasks and Leaderboards
- **Instruction-tuning** of LLMs for Vedic/Indian philosophy
- **Question answering** with scriptural grounding
- **Text generation** (structured JSON output)

## Languages
- Sanskrit (`sa`)
- English (`en`)

## Usage Example
You can load the dataset using the HuggingFace Datasets library:

```python
from datasets import load_dataset

dataset = load_dataset("PyPranav/Bhagwat-Corpus-Data")
print(dataset["train"][0])
# Example output:
# {
#   'original_hf_id': 'test_idx_0',
#   'sanskrit_shloka': '...',
#   'english_translation': '...',
#   'generated_question': '...',
#   'generated_explanation': '...',
#   'generation_status': 'success'
# }
```

## License
Apache 2.0 