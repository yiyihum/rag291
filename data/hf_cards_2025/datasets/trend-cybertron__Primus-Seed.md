---
license: odc-by
task_categories:
- text-generation
language:
- en
pretty_name: Primus-Seed
tags:
- cybersecurity
- pretraining
- wikipedia
- MITRE
size_categories:
- 100K<n<1M
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
---

> ⭐ Please download the dataset from [here](https://huggingface.co/datasets/trendmicro-ailab/Primus-Seed).

# PRIMUS: A Pioneering Collection of Open-Source Datasets for Cybersecurity LLM Training

## 🤗 Primus-Seed

**Primus-Seed** is a high-quality🚀 cybersecurity text dataset composed of data crawled from reputable sources such as MITRE, Wikipedia, and well-known cybersecurity company websites, as well as CTI manually collected by our threat experts.


## Statistics

| **Category** | **Samples** | **Tokens** | **Avg.** |
|-------------|------------|------------|----------|
| **_Web Crawl / Official Dump_** | | | |
| Cybersecurity Blogs/News | 2,946 | 9,751,002 | 3,309.9 |
| Cybersecurity Books | 6,499 | 2,910,464 | 447.8 |
| Cybersecurity Companies Websites | 76,919 | 65,798,561 | 855.4 |
| Cybersecurity Wikipedia | 6,636 | 9,567,196 | 1,441.7 |
| MITRE | 3,432 | 2,435,118 | 709.5 |
| **_Expert Curation_** | | | |
| Campaigns | 136 | 37,106 | 272.8 |
| Intrusion Sets | 343 | 60,524 | 176.5 |
| Malware | 7,301 | 1,362,681 | 186.6 |
| Reports | 11,317 | 934,954 | 82.6 |
| Threat Actors | 27 | 2,264 | 83.9 |
| Tools | 238 | 19,926 | 83.7 |
| Vulnerabilities | 559,054 | 98,006,720 | 175.3 |
| **Total** | **674,848** | **190,886,516** | **282.9** |

❗❗Currently, we have only released **Cybersecurity Companies Websites, Cybersecurity Wikipedia, and MITRE**. Other categories are under review to ensure compliance and verify whether redistribution falls under "_fair use_."

## How Did We Collect Cybersecurity Wikipedia?
_Wikipedia_ does not provide a predefined cybersecurity subset, so we perform a custom filtering process. Each Wikipedia article is associated with one or more category tags, which can be further expanded into subcategory tags. Starting from the root category "_Computer Security_", we recursively traverse its subcategories, using GPT-4o to determine whether a category is cybersecurity-related. This process yields **375** relevant categories, from which we extract corresponding Wikipedia articles.

_Prompt_:
```
[System]
You are a helpful assistant.
[User]
Help me identify and mark the categories related to "cybersecurity", "information
security", "data protection", "cryptography", "hacker activity", "cyber attack",
"cybercrime" from a list of categories I have.
For each category, provide a reason for marking it as 'Y' (Yes) or 'N' (No) in relation to the
specified topics. Finally, output the results in JSON format with the fields: category,
reason, security.
{{category-list}
```


🚀🚀 For more details, see our paper:  
[https://arxiv.org/abs/2502.11191](https://arxiv.org/abs/2502.11191)

## License

This dataset is released under the **ODC-By** license.