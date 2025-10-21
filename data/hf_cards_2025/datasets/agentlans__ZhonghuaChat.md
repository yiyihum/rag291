---
configs:
- config_name: all
  data_files:
  - path:
    - all.jsonl.zst
    split: train
  default: true
- config_name: zhcn
  data_files:
  - path:
    - zhcn.jsonl.zst
    split: train
- config_name: zhtw
  data_files:
  - path:
    - zhtw.jsonl.zst
    split: train
- config_name: yue
  data_files:
  - path:
    - yue.jsonl.zst
    split: train
- config_name: en
  data_files:
  - path:
    - en.jsonl.zst
    split: train
license: agpl-3.0
language:
- zh
- en
task_categories:
- text-generation
- text-classification
- text2text-generation
- translation
tags:
- Chinese
- China
- Taiwan
- Hong Kong
- dialogue
- conversation
- chat
---
# Zhonghua Chat

## Overview

**Zhonghua Chat** is a multilingual dataset featuring questions and answers in:

- **Mandarin** (Simplified Chinese and Traditional Chinese)
- **Cantonese**
- **English**

The dataset is designed to support research and development in conversational AI, natural language understanding, and multilingual language modeling for Chinese dialects and writing systems.

## Composition

Rows were sampled in roughly equal proportions from the following high-quality, open-source datasets:

- [Mxode/Chinese-Instruct](https://huggingface.co/datasets/Mxode/Chinese-Instruct) (various configurations, sampled equally)
- [yentinglin/TaiwanChat](https://huggingface.co/datasets/yentinglin/TaiwanChat)
- [stvlynn/Cantonese-Dialogue](https://huggingface.co/datasets/stvlynn/Cantonese-Dialogue)
- [vicgalle/alpaca-gpt4](https://huggingface.co/datasets/vicgalle/alpaca-gpt4)

### Example Entry

```json
{
  "input": "请评估一下CRISPR-Cas9对遗传疾病的治疗前景和应用风险",
  "output": "CRISPR-Cas9技术在遗传疾病治疗方面展现出巨大的潜力……（完整答案略）",
  "source": "Mxode/Chinese-Instruct",
  "config": "stem_zh"
}
```

## Features

- **Linguistic diversity:** Includes both written and spoken forms (for example, Cantonese is primarily represented in its spoken form).
- **Regional coverage:** Content spans knowledge and topics relevant to Mainland China, Taiwan, and Hong Kong.
- **Balanced sampling:** Ensures fair representation from each source and configuration.

## Limitations

- **Source dataset imbalance:** The original datasets vary significantly in size, which affects topic and style diversity.
- **Content variability:** Differences in regional knowledge, language style, and formality.
- **Licensing restrictions:** All source datasets are under restrictive licences which limit downstream use.

## Licence

- **AGPL-3.0, Noncommercial, Attribution Share Alike**
  - Usage is restricted to noncommercial research and development.
  - Please review individual source dataset licences.