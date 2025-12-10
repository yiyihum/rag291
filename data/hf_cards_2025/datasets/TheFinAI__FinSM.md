---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: dqc_id
    dtype: string
  - name: answer
    dtype: string
  - name: id
    dtype: int64
  splits:
  - name: test
    num_bytes: 35959685
    num_examples: 330
  download_size: 2881818
  dataset_size: 35959685
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
task_categories:
- text-generation
license: cc-by-4.0
language:
- en
papers:
- title: 'FinAuditing: Taxonomy-Grounded Financial Auditing Benchmark for Evaluating
    Large Language Models'
  authors:
  - Yan Wang
  - Keyi Wang
  - Shanshan Yang
  - Jaisal Patel
  - Jeff Zhao
  - Fengran Mo
  - Xueqing Peng
  - Lingfei Qian
  - Jimin Huang
  - Guojun Xiong
  - Xiao-Yang Liu
  - Jian-Yun Nie
  url: https://arxiv.org/abs/2510.08886
  conference: arXiv preprint, 2025
tags:
- finance
- auditing
- xbrl
- gaap
- llm
- benchmark
- financial-reasoning
---

# 🧾 FinAuditing Benchmark

This dataset is introduced in the paper  
**[FinAuditing: Taxonomy-Grounded Financial Auditing Benchmark for Evaluating Large Language Models](https://arxiv.org/abs/2510.08886)**  
by Yan Wang, Keyi Wang, Shanshan Yang, Jaisal Patel, Jeff Zhao, Fengran Mo, Xueqing Peng, Lingfei Qian, Jimin Huang, Guojun Xiong, Xiao-Yang Liu, and Jian-Yun Nie (2025).