---
language:
- en
license: cc-by-nc-4.0
tags:
- instruction-tuning
- text-summarization
- pros-cons-extraction
- e-commerce
- product-reviews
- llm-generated
- gpt-4o
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- summarization
source: https://www.amazon.com/
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    list: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 11714813
    num_examples: 10000
  download_size: 6753168
  dataset_size: 11714813
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

## Dataset Summary

This dataset was built from **Amazon product reviews** and curated into an **instruction-tuning format** for structured pros and cons extraction.

The pipeline includes:

1. **Raw data loading** → Extract `asin`, `reviewText`.
2. **Preprocessing** → Clean, filter, and truncate each (10–150 words).
3. **Grouping** → Aggregate reviews by product.
4. **Selection** → Shuffle and select 10
5. **Filtering** → Keep 5–15 reviews per product.
6. **Selection** → Shuffle and keep 10k rows to make final dataset.
7. **Summarization** → Shorten long reviews using facebook/bart-large-cnn.
8. **LLM distillation** → Generate concise JSON pros/cons from grouped reviews using GPT-4o-mini model (pros and cons keys only).
9. **Instruction dataset creation** → Final dataset aligned with instruction → input → output format.

This dataset is intended for fine-tuning instruction-following models on product review understanding and summarization (structured) tasks.

---

## Dataset Structure

- **Format**: Parquet

- **Fields**:

  - `instruction` → Natural language task prompt (fixed: `"Generate pros and cons from the following product reviews."`)

  - `input` → List of product reviews (preprocessed + summarized)

  - `answer` → JSON string with `pros` and `cons`

### Example record:

```json
{
  "instruction": "Generate pros and cons from the following product reviews.",
  "input": [
    "Great sound quality but the battery drains fast.",
    "Comfortable to wear for long hours.",
    "Bluetooth disconnects sometimes.",
    "Excellent value for the price."
  ],
  "answer": {
    "pros": [
      "Great sound quality",
      "Comfortable to wear",
      "Good value for price"
    ],
    "cons": [
      "Battery drains fast",
      "Bluetooth disconnects"
    ]
  }
}
```
---

## Size & Splits

- **Samples**: 10,000 (configurable in builder)
- **Split**: training set

## Languages

- **English**

---

## Intended Uses

- Fine-tuning LLMs for review understanding.

- Pros/cons extraction from customer feedback.

- Research on structured summarization.

Not suitable for:

- Automated decision-making in **medical**, **legal**, or **financial** contexts.

---

## How to Use

```python
from datasets import load_dataset

dataset = load_dataset("sdelowar2/product_reviews_insight_10k")

print(dataset[0])
# {
#   'instruction': 'Generate pros and cons from the following product reviews.',
#   'input': [...],
#   'answer': {...}
# }
```

---

## Citation

```bibtex
@misc{product_reviews_pros_cons_2025,
  title={Product Reviews Pros and Cons Dataset},
  author={Md Sayed Delowar},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/sdelowar2/product_reviews_insight_10k}}
}
```

---

