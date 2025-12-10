---
language:
- ur
license: cc-by-sa-4.0
pretty_name: ALIF Urdu Corpus
tags:
- urdu
- alif
- orature-ai
- text-corpus
- pretraining
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: Data
    dtype: string
  - name: Category
    dtype: string
  - name: Source
    dtype: string
  splits:
  - name: train
    num_bytes: 14548389
    num_examples: 5000
  download_size: 6755924
  dataset_size: 14548389
---

# ALIF_Urdu_Corpus (Preview)

This dataset, **ALIF_Urdu_Corpus**, is part of the **ALIF الف** project by **Orature AI**. It was curated for pretraining Urdu language models. It serves as a preview to our entire 33GB Dataset.

## Dataset Description
*   **Curated by:** Orature AI (S.M Ali Naqvi, Zainab Haider, Haya Fatima, Ali M Asad, Hammad Sajid)
*   **Supervised by:** Dr. Abdul Samad (Habib University)
*   **Language(s):** Urdu (ur).
*   **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

**Purpose of the Dataset:**
* (preview) To serve as a large-scale, diverse, and high-quality foundation for pretraining generative language models for Urdu.

## Languages

The data is in **Urdu**.

## Dataset Structure

**(For Pretraining Corpus - ALIF-Urdu-Corpus):**
The dataset is structured as a collection of text entries, in CSV format, with the following columns:

| Data | Category | Source |
| --- | --- | --- |

* **Data:** The `Data` column contains the actual Urdu data
* **Category:** The `Category` column refers to the type of data it is, for example CommonCrawl, Fineweb, etc.
* **Source:** The `Source` column contains the actual source from where the data was taken. 

## Data Collection and Preprocessing

**The Complete ALIF-Urdu-Corpus:**
The dataset was meticulously collected from a variety of sources to ensure diversity and coverage:
*   **Common Crawl Dumps:** 11.3 GB (Dump 1) and 8.1 GB (Dump 2) of filtered Urdu text.
*   **Translation Data:** 5.5 GB of educational content from the English FineWeb dataset, translated to Urdu using Google Translate API.
*   **News Websites:** 3.3 GB scraped from various Urdu news websites.
*   **Existing Datasets:** 2.9 GB from public Urdu corpora (e.g., UrduHack, other open-source).
*   **Books (OCR Processed):** 1.3 GB of text extracted from scanned Urdu books using Google Vision OCR, followed by post-OCR cleaning.
*   **Blog Sites:** 0.6 GB from various Urdu blogs.

**Preprocessing Steps:**
1.  **Cleaning:** Removal of HTML tags, links, numbers (unless contextually relevant), email addresses, and other non-linguistic noise.
2.  **Encoding Normalization:** Ensured consistent UTF-8 encoding.
3.  **Language Filtering:** Non-Urdu content was filtered out using language detection tools.
4.  **Deduplication:** Rigorous deduplication was performed using MinHash-based Locality Sensitive Hashing (LSH) to identify and remove near-duplicate documents and paragraphs, both within and across source datasets. Exact duplicates were also removed.
5.  **Formatting:** Final data organized into a structured format (e.g., CSV), with End-of-Text (EOT) tokens used to delineate documents/segments during training.


## Dataset Size

*   **ALIF_Urdu_Corpus:**
    *   Total Size: ~33 GB for ALIF-Urdu-Corpus, however, this dataset preview contains about 13.7MB of that data.
    *   Number of Rows/Examples: 5000 rows
    <!-- *   Estimated Tokens: [e.g., 5-6 billion tokens for ALIF-Urdu-Corpus / Specify for instruct set] -->

## Intended Uses

*   **Pretraining Language Models:** The ALIF-Urdu-Corpus is primarily intended for pretraining large-scale generative language models for Urdu.
*   **Instruction Fine-tuning:** The ALIF-Urdu-Instruct dataset is designed for fine-tuning pretrained models to follow instructions in Urdu.
*   **NLP Research:** Can be used for various research tasks in Urdu NLP, such as studying linguistic phenomena, bias in text, or developing new preprocessing techniques.
*   **Benchmarking:** Subsets can be used for creating benchmarks for Urdu language understanding or generation.

<!-- ## How to Use with `datasets` library

```python
from datasets import load_dataset

# For the pretraining corpus
# dataset = load_dataset("OratureAI/[HF_DATASET_NAME_PRETRAINING]") # e.g., OratureAI/alif_urdu_corpus
# print(dataset['train'][0])

# For an instruction dataset
# dataset_instruct = load_dataset("OratureAI/[HF_DATASET_NAME_INSTRUCT]") # e.g., OratureAI/alif_urdu_instruct
# print(dataset_instruct['train'][0])
``` -->