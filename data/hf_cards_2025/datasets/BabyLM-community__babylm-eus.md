---
task_categories:
- text-generation
language:
- eus
license: unknown
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: text
    dtype: string
  - name: doc-id
    dtype: string
  - name: category
    dtype: string
  - name: data-source
    dtype: string
  - name: script
    dtype: string
  - name: age-estimate
    dtype: string
  - name: license
    dtype: string
  - name: misc
    dtype: string
  - name: num-tokens
    dtype: int64
  - name: language
    dtype: string
---

# BabyLM Dataset

## Dataset Description

This dataset is part of the BabyLM multilingual collection.   
More information at: [babylm.github.io/babybabellm](https://babylm.github.io/babybabellm/)

### Dataset Summary

- **Language:** eus
- **Script:** Latn
- **Tier:** 10M
- **Byte Premium Factor:** 1.059584
- **Size (MB):** 57.06
- **Expected Size (MB):** 57.54
- **Number of Documents:** 13,421
- **Total Tokens:** 8,189,297
- **Tokenizer:** separate by whitespace

### Tokens Per Category

- **child-directed-speech:** 201,402 tokens
- **child-wiki:** 1,716,026 tokens
- **padding-fineweb-c:** 40,654 tokens
- **padding-opensubtitles:** 3,176,681 tokens
- **padding-wikipedia:** 3,054,534 tokens

### Tokens Per Group

- **Transcription:** 201,402 tokens
- **Education:** 0 tokens
- **Books, Wiki, News:** 1,716,026 tokens
- **Subtitles:** 0 tokens
- **Padding:** 6,271,869 tokens


### Data Fields

- `text`: The document text
- `doc-id`: Unique identifier for the document
- `category`: Type of content (e.g., child-directed-speech, educational, etc.)
- `data-source`: Original source of the data
- `script`: Writing system used (ISO 15924)
- `age-estimate`: Target age or age range
- `license`: Data license
- `misc`: Additional metadata (JSON string)
- `num-tokens`: Number of tokens per item (based on white-space split)
- `language`: Language code (ISO 639-3)

### Licensing Information

Please see license in individual documents

### Data Sources & Attribution

n/a

### Data Curators

* Julen Etxaniz



### Comments 

None