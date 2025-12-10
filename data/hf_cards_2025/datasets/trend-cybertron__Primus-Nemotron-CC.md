---
license: odc-by
task_categories:
- text-generation
language:
- en
pretty_name: Primus-Nemotron-CC
configs:
- config_name: default
  data_files:
  - split: train
    path: data/*
tags:
- cybersecurity
- pretraining
- Nemotron-CC
size_categories:
- 10M<n<100M
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

## 🤗 Primus-Nemotron-CC
The Primus-Nemotron-CC dataset is constructed by filtering cybersecurity-related text from [Nemotron-CC](https://arxiv.org/abs/2412.02595), a refined version of Common Crawl. We began by leveraging Primus-Seed, a high-quality dataset of manually curated cybersecurity text, as positive samples. We then sampled ten times the amount of data from FineWeb as negative samples and trained a binary cybersecurity classifier based on TinyBERT. Using this classifier, we assigned each text in Nemotron-CC a score between 0 and 1, and filtered out texts with length greater than _500_ and scores between _0.98_ and _0.0175_, creating the Primus-Nemotron-CC with 8.31 billion tokens. After deduplication, the final dataset was reduced to 🔥 7.63 billion tokens of cybersecurity corpus. **For more details, please refer to Appendix B of the [Primus paper](https://arxiv.org/abs/2502.11191).**

## Why Only Select Texts Longer Than 500?
For each score interval, we sampled 1,000 examples, grouped them by length, sent them to GPT-4o-mini to verify whether they were truly cybersecurity-related, and then calculated the proportion of confirmed samples. As shown in the figure below, we observed that when the sample length is under 500, the proportion of cybersecurity-related samples falls below 50% in most cases.

<img src="https://i.imgur.com/NleD4D1.png" alt="Ratio of cybersecurity-related text across different score bins in NEMOTRON-CC, grouped by sample length" width="65%">

---

## Data Cutoff
This dataset is derived from the Nemotron-CC dataset, which itself is filtered and processed from Common Crawl web data. The latest Common Crawl shard included in this release is **CC-MAIN-2024-30**. No data from crawls after this snapshot are included.

## License
This dataset is released under the ODC-By license. However, users must comply with both the Nemotron-CC license and the Common Crawl Terms of Use. By using this dataset, you acknowledge that its contents are sourced from public web data and are subject to the respective source licenses and terms. Please ensure your usage complies with all applicable laws and regulations.

## Personal and Sensitive Information and Opt-Out
If you find information related to yourself and wish to have it removed, please open a discussion on the HuggingFace dataset page and we will contact you for removal as soon as possible.

Similarly, Common Crawl respects robots.txt at crawl time, but if you are a webmaster and find your website content included in this dataset and would like to have it removed, please also open a discussion on the HuggingFace dataset page and we will contact you for prompt removal.
