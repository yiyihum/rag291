---
license: cc-by-4.0
language:
- tr
task_categories:
- text-classification
- text-generation
- summarization
- question-answering
tags:
- medical
size_categories:
- 10K<n<100K
configs:
- config_name: default
  data_files:
  - split: acibadem
    path: data/acibadem-*
  - split: anadolusaglik
    path: data/anadolusaglik-*
  - split: atlas
    path: data/atlas-*
  - split: baskentistanbul
    path: data/baskentistanbul-*
  - split: bayindir
    path: data/bayindir-*
  - split: florence
    path: data/florence-*
  - split: guven
    path: data/guven-*
  - split: liv
    path: data/liv-*
  - split: medicalpark
    path: data/medicalpark-*
  - split: medicalpoint
    path: data/medicalpoint-*
  - split: medicana
    path: data/medicana-*
  - split: medipol
    path: data/medipol-*
  - split: memorial
    path: data/memorial-*
  - split: yeditepe
    path: data/yeditepe-*
dataset_info:
  features:
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  - name: publish_date
    dtype: string
  - name: update_date
    dtype: string
  - name: scrape_date
    dtype: string
  splits:
  - name: acibadem
    num_bytes: 59871616
    num_examples: 6339
  - name: anadolusaglik
    num_bytes: 7711085
    num_examples: 1012
  - name: atlas
    num_bytes: 659835
    num_examples: 130
  - name: baskentistanbul
    num_bytes: 1632855
    num_examples: 394
  - name: bayindir
    num_bytes: 3985692
    num_examples: 690
  - name: florence
    num_bytes: 12815638
    num_examples: 1641
  - name: guven
    num_bytes: 4279987
    num_examples: 666
  - name: liv
    num_bytes: 19820891
    num_examples: 2836
  - name: medicalpark
    num_bytes: 3323029
    num_examples: 371
  - name: medicalpoint
    num_bytes: 2374940
    num_examples: 654
  - name: medicana
    num_bytes: 17090402
    num_examples: 2163
  - name: medipol
    num_bytes: 7876549
    num_examples: 1380
  - name: memorial
    num_bytes: 44864194
    num_examples: 5338
  - name: yeditepe
    num_bytes: 5203404
    num_examples: 998
  download_size: 89711227
  dataset_size: 191510117
---

# 🏥 Turkish Medical Articles from 14 Hospital Websites

This dataset contains Turkish-language medical articles scraped from **14 official hospital and healthcare provider websites** in Turkey. Each file corresponds to one source and is stored in efficient `.parquet` format.

It is designed for training and evaluating **Turkish NLP models in the medical domain**, including large language models (LLMs), health chatbots, summarizers, and classifiers.

> 🧾 Total articles: ~ 25,000  
> 📦 Total file size: ~95MB  
> 🗂️ Format: `.parquet`  
> 👤 Curated by: [umutertugrul](https://huggingface.co/umutertugrul)  
> 🔓 License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 🏷️ Included Sources

| Filename                  | Source Institution         |
|---------------------------|----------------------------|
| `acibadem.parquet`        | Acıbadem Hospital          |
| `anadolusaglik.parquet`   | Anadolu Sağlık             |
| `atlas.parquet`           | Atlas Hospital             |
| `baskentistanbul.parquet` | Başkent İstanbul           |
| `bayindir.parquet`        | Bayındır Hospital          |
| `florence.parquet`        | Florence Nightingale       |
| `guven.parquet`           | Güven Hospital             |
| `liv.parquet`             | Liv Hospital               |
| `medicalpark.parquet`     | Medical Park               |
| `medicalpoint.parquet`    | Medical Point              |
| `medicana.parquet`        | Medicana Hospitals         |
| `medipol.parquet`         | Medipol University Hospital|
| `memorial.parquet`        | Memorial Hospital          |
| `yeditepe.parquet`        | Yeditepe University        |

Each file contains articles specific to that institution, covering a wide range of medical topics and specialties.

---

## 🔤 Schema

Each `.parquet` file may contain the following fields:

- `url`: Original article URL  
- `title`: Title of the article  
- `headings`: Section headings or subtopics (if available)  
- `text`: Full body content of the article  
- `publish_date`: Date the article was originally published  
- `update_date`: Last updated date (if available)  
- `scrape_date`: Date when the article was collected  
- `__source`: Hospital/source name (automatically added during conversion)

---

## 🚀 Example Usage

```python
from datasets import load_dataset, Features, Value

files = {
    "acibadem": "acibadem.parquet",
    "anadolusaglik": "anadolusaglik.parquet",
    "atlas": "atlas.parquet",
    "baskentistanbul": "baskentistanbul.parquet",
    "bayindir": "bayindir.parquet",
    "florence": "florence.parquet",
    "guven": "guven.parquet",
    "liv": "liv.parquet",
    "medicalpark": "medicalpark.parquet",
    "medicalpoint": "medicalpoint.parquet",
    "medicana": "medicana.parquet",
    "medipol": "medipol.parquet",
    "memorial": "memorial.parquet",
    "yeditepe": "yeditepe.parquet"
}

features = Features({
    "url": Value("string"),
    "title": Value("string"),
    "headings": Value("string"),
    "text": Value("string"),
    "publish_date": Value("string"),
    "update_date": Value("string"),
    "scrape_date": Value("string"),
    "__source": Value("string") 
})

ds_healthcare_1 = load_dataset(
    "umutertugrul/turkish-hospital-medical-articles",
    data_files=files,
    features=features
)
```