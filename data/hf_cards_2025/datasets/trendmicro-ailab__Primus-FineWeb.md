---
license: odc-by
task_categories:
- text-generation
language:
- en
pretty_name: Primus-FineWeb
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*
tags:
- cybersecurity
- pretraining
- FineWeb
size_categories:
- 1M<n<10M
extra_gated_fields:
  Affiliation: text
  Country: country
  I want to use this model for:
    type: select
    options:
    - Research
    - Commercial
    - label: Other
      value: other
  Job title:
    type: select
    options:
    - Student
    - Research graduate
    - AI researcher
    - AI developer/engineer
    - Cybersecurity researcher
    - Reporter
    - Other
  geo: ip_location
library_name: transformers
---

# PRIMUS: A Pioneering Collection of Open-Source Datasets for Cybersecurity LLM Training

## 🤗 Primus-FineWeb

The **Primus-FineWeb** dataset is constructed by filtering cybersecurity-related text from FineWeb, a refined version of Common Crawl. We began by leveraging _Primus-Seed_, a high-quality dataset of manually curated cybersecurity text, as positive samples. We then sampled ten times the amount of data from FineWeb as negative samples and trained a **binary cybersecurity classifier** based on TinyBERT. Using this classifier, we assigned each text in FineWeb a score between **0 and 1** and filtered out texts with a score greater than **0.003**, creating the Primus-FineWeb with 15.3 billion tokens. However, after discovering a significant amount of duplicate content, we performed deduplication, reducing the final dataset to **🔥 2.57 billion tokens of cybersecurity corpus**.

🚀🚀 For more details, see our paper:  
[https://arxiv.org/abs/2502.11191](https://arxiv.org/abs/2502.11191)

---

## Why was the threshold set at 0.003?

We divided the score range (0-1) into several bins and randomly sampled 50 examples from each bin. These samples were then scored by GPT-4o to determine the proportion of text that was "_truly_" cybersecurity-related. We found that if the score was below 0.003, the proportion of cybersecurity text fell below 50%.

<img src="https://i.imgur.com/XbqpmbI.png" alt="Threshold Selection" width="60%">


## FineWeb: Cybersecurity Score vs. Token Count

<img src="https://i.imgur.com/6twJL1p.png" alt="Cybersecurity Score vs. Token Count" width="65%">

---

## Data Cutoff

This dataset is derived from the FineWeb dataset, which itself is filtered and processed from Common Crawl web data. The latest Common Crawl shard included in this release is **CC-MAIN-2024-10**. No data from crawls after this snapshot are included.

## License

This dataset is released under the **ODC-By** license. However, users must comply with both the **FineWeb license** and the [Common Crawl Terms of Use](https://commoncrawl.org/terms-of-use/). By using this dataset, you acknowledge that its contents are sourced from public web data and are subject to the respective source licenses and terms. Please ensure your usage complies with all applicable laws and regulations.

## Personal and Sensitive Information and Opt-Out

While significant efforts have been made in the original FineWeb dataset to filter, anonymize, and deduplicate personal and sensitive information, due to the nature of large-scale web crawls, some personally identifiable information (PII) may still be present. If you find information related to yourself and wish to have it removed, please open an discussion on the HuggingFace dataset page and we will contact you for removal as soon as possible.

Similarly, Common Crawl respects robots.txt at crawl time, but if you are a webmaster and find your website content included in this dataset and would like to have it removed, please also open a discussion on the HuggingFace dataset page and we will contact you for prompt removal.
