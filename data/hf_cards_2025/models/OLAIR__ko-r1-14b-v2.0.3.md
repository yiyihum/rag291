---
library_name: transformers
license: mit
datasets:
- OLAIR/Open-R1-Ko-SFT-v2.0
language:
- ko
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Qwen-14B
---


## 1. Overview

**Model Name:** OLAIR/ko-r1-14b-v2.0.3  
**Model Type:** Large Language Model (LLM) for Korean language understanding and reasoning  
**Version:** 2.0.3

This model is designed to provide Korean language capabilities with a focus on reasoning tasks. It is a scaled-up version of [OLAIR/ko-r1-7b-v2.0.3](https://huggingface.co/OLAIR/ko-r1-7b-v2.0.3) for experimental purposes.


## 2. Benchmark Performance

The model's performance has been evaluated using the HAE-RAE Reasoning Challenge (HRC), which measures reasoning abilities across five domains.


| Model                                 | Chemistry | Math   | Physics | Physics Word Puzzles | Puzzles | Average |
|---------------------------------------|-----------|--------|---------|----------------------|---------|---------|
| o1-2024-12-17                         | 57.14     | 78.18  | 77.78   | 80.00                | 84.62   | 75.54   |
| o3-mini-high                          | 57.14     | 81.82  | 77.78   | 70.00                | 69.23   | 71.19   |
| o3-mini-2025-01-31                     | 50.00     | 80.00  | 70.37   | 50.00                | 76.92   | 65.46   |
| o1-mini-2024-09-12                     | 42.86     | 56.36  | 70.37   | 60.00                | 15.38   | 48.99   |
| Deepseek-R1                           | 50.00     | 54.55  | 62.96   | 70.00                | 7.69    | 49.04   |
| gpt-4o-2024-11-20                      | 35.71     | 32.73  | 51.85   | 50.00                | 53.85   | 44.83   |
| **Ko-R1-14B-v2.0.3**                   | 28.57      | 50.9  | 48.14  | 30.00                | 30.77   | 37.68   |
| Exaone-3.5-32B-Instruct               | 21.43     | 30.91  | 25.93   | 50.00                | 38.46   | 33.35   |
| Qwen2.5-72B-Instruct                  | 35.71     | 30.91  | 51.85   | 20.00                | 23.08   | 32.31   |
| **Ko-R1-7B-v2.0.3**                   | 7.14      | 61.82  | 40.74   | 40.00                | 0.00    | 29.94   |
| Ko-R1-7B-v1                           | 7.14      | 63.64  | 37.04   | 40.00                | 0.00    | 29.56   |
| gpt-4o-mini-2024-07-18                 | 21.43     | 29.09  | 37.04   | 50.00                | 0.00    | 27.51   |
| UNIVA-Bllossom_DeepSeek-llama3.1-Bllossom-8B | 28.57     | 16.36  | 33.33   | 10.00                | 15.38   | 20.73   |


**Comparison of Average Scores**
Ko-R1-14B-v2.0.3 outperforms non-reasoning models of way bigger size like Exaone-3.5-32B-Instruct, Qwen2.5-72B-Instruct, and gpt-4o-mini-2024-07-18. 
<p align="center"><img src="https://cdn-uploads.huggingface.co/production/uploads/60d3e619b8448e1785bbda2a/GA8UI4jr4GlSRrFJBa8nl.png" width="525"/>

**Training Rewards**
Even when trained with the same datasets, bigger models just learn MORE.
<p align="center"><img src="https://cdn-uploads.huggingface.co/production/uploads/60d3e619b8448e1785bbda2a/XAeOlEBnMSp9pQP0I1IU7.png" width="525"/> 



## 3. Limitations

- The model is still vulnerable to Korean-related inputs, leading to endless loops of thinking. We are working to fix it.

## ETC
How to Cite

```
To be added
```

Contact 
```
spthsrbwls123@yonsei.ac.kr
```