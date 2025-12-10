---
task_categories:
- fill-mask
language:
- ro
pretty_name: ro-sentences
tags:
- ro
- romanian
- text
- sentences
- corpus
- monolingual
- language-modeling
- masked-language-modeling
- pretraining
- large
size_categories:
- 100M<n<1B
---


# Romanian Sentences (BlackKakapo/ro-sentences)

A large-scale corpus of Romanian sentences, created by processing and splitting public text datasets into sentence-level units.  
The main purpose of this dataset is to support **Masked Language Modeling (MLM)**, **continual pretraining**, **semantic textual similarity (STS)**, and other NLP tasks in Romanian.

---

## 📚 Data Sources

This corpus was built from the following datasets:

- [`statmt/cc100`](https://huggingface.co/datasets/statmt/cc100) – large-scale web crawl.  
- [`wikimedia/wikipedia`](https://huggingface.co/datasets/wikimedia/wikipedia) – Romanian Wikipedia articles.  
- [`dumitrescustefan/diacritic`](https://huggingface.co/datasets/dumitrescustefan/diacritic) – cleaned and re-diacritized Romanian text.  
- [`agentlans/multilingual-sentences`](https://huggingface.co/datasets/agentlans/multilingual-sentences) – multilingual sentences including Romanian subsets.

### Processing
- All text was **split into sentences** using simple segmentation rules.  
- Only **clean sentences** were kept, with normalized Unicode characters.  
- Very short sentences (e.g. one word) were removed.  
- Whitespace and separators were standardized.  

---

## 📊 Statistics

- **Disk size**: ~70GB (available in Parquet shards [47GB]).  
- **Total number of sentences**: 708,341,932.  
- **Total number of words**: 11,224,484,077.  
- **Average sentence length**: 15.85 words/sentence.  
---

## 🧾 Schema

Each row contains a single sentence:  

```json
{
  "text": "This is an example sentence in Romanian."
}
