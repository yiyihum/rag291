---
language:
- en
license: cc-by-nc-4.0
size_categories:
- 1K<n<10K
task_categories:
- question-answering
- text-generation
- reinforcement-learning
pretty_name: APIGen-MT-5k
extra_gated_heading: Acknowledge to follow the corresponding license and cite APIGen-MT
  to access the repository
extra_gated_button_content: Agree and access repository
extra_gated_fields:
  First Name: text
  Last Name: text
  Country: country
  Affiliation: text
tags:
- function-calling
- agent
- Synthetic
- benchmark
library_name: datasets
configs:
- config_name: dataset
  data_files:
  - split: train
    path: apigen-mt_5k.json
---

## Summary

- [APIGen-MT](https://apigen-mt.github.io/) is an automated agentic data generation pipeline designed to synthesize *verifiable, high-quality, realistic datasets* for agentic applications
- This dataset was released as part of [APIGen-MT: Agentic PIpeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay](https://arxiv.org/abs/2504.03601)
- Code: [https://github.com/apigen-mt/apigen-mt.github.io](https://github.com/apigen-mt/apigen-mt.github.io)
- The repo contains **5000** multi-turn trajectories collected by APIGen-MT
- This dataset is a subset of the data used to train the [xLAM-2](https://huggingface.co/collections/Salesforce/xlam-2-67ef5be12949d8dcdae354c4) model series

## Overview

Agentic data consists of realistic trajectories in which an AI agent gradually comprehends the human's intent and interacts with tools and the environment step-by-step to complete the task. APIGen-MT builds on [APIGen](https://apigen-pipeline.github.io/), which focuses on generating single-turn function calling data. It addresses the lack of high-quality multi-turn agent interaction data in public datasets and the high cost of manually collecting such data for domain-specific applications. 
Each task in our dataset is verified through three hierarchical stages: format checking, function executions and domain policy check, and semantic verification, ensuring its reliability and correctness. We conducted a human evaluation over 200 sampled trajectories, and the success rate is 99%.
The overall framework for the dataset collection procedure is shown below. See more details at our project [website](https://apigen-mt.github.io/).


<div style="text-align: center;">
    <img src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/pipeline.png?raw=true" alt="APIGen-MT Overview" width="620" style="margin: auto;">
</div>


## Dataset Details

- **Models Used**: [GPT-4o](https://platform.openai.com/docs/models/gpt-4o), [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)
- **Domains**: Retail and Airline (via [τ-bench](https://github.com/sierra-research/tau-bench))
- **Size**: 5000 multi-turn dialogues
- **Format**: ShareGPT-like JSON, with structured conversation turns

The dataset is at `apigen-mt_5k.json`. After accepting the usage terms and login in your HuggingFace account, you can simply access the dataset using

```python
from datasets import load_dataset
datasets = load_dataset("Salesforce/APIGen-MT-5k")
```


The data is released in *ShareGPT* format shown below

```json
[
  {
    "conversations": [
      { "from": "human", "value": "human query" },
      { "from": "function_call", "value": "tool arguments" },
      { "from": "observation", "value": "tool result" },
      { "from": "gpt", "value": "agent response" }
    ],
    "system": "system prompt (having domain policy)",
    "tools": "tool description"
  }
]
```

## Benchmark Results

### Berkeley Function-Calling Leaderboard (BFCL v3)
<p align="center">
<img width="80%" alt="BFCL Results" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/bfcl-result.png?raw=true">
<br>
<small><i>Performance comparison of different models on [BFCL leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html). The rank is based on the overall accuracy, which is a weighted average of different evaluation categories. "FC" stands for function-calling mode in contrast to using a customized "prompt" to extract the function calls.</i></small>
</p>

### τ-bench Benchmark

<p align="center">
<img width="80%" alt="Tau-bench Results" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/taubench-result.png?raw=true">
<br>
<small><i>Success Rate (pass@1) on τ-bench benchmark averaged across at least 5 trials. Our xLAM-2-70b-fc-r model achieves an overall success rate of 56.2% on τ-bench, significantly outperforming the base Llama 3.1 70B Instruct model (38.2%) and other open-source models like DeepSeek v3 (40.6%). Notably, our best model even outperforms proprietary models such as GPT-4o (52.9%) and approaches the performance of more recent models like Claude 3.5 Sonnet (new) (60.1%).</i></small>
</p>

<p align="center">
<img width="80%" alt="Pass^k curves" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/pass_k_curves_retail_airline.png?raw=true">
<br>
<small><i>Pass^k curves measuring the probability that all 5 independent trials succeed for a given task, averaged across all tasks for τ-retail (left) and τ-airline (right) domains. Higher values indicate better consistency of the models.</i></small>
</p>


## Ethical Considerations

This release is for research purposes only in support of an academic paper. Our models, datasets, and code are not specifically designed or evaluated for all downstream purposes. We strongly recommend users evaluate and address potential concerns related to accuracy, safety, and fairness before deploying this model. We encourage users to consider the common limitations of AI, comply with applicable laws, and leverage best practices when selecting use cases, particularly for high-risk scenarios where errors or misuse could significantly impact people's lives, rights, or safety. For further guidance on use cases, refer to our AUP and AI AUP. 

### Data Licenses

A part of this dataset was generated using GPT-4 and should not be used to develop models that compete with OpenAI.

## Citation

If you use our model or dataset in your work, please cite our paper:

```bibtex
@article{prabhakar2025apigen,
  title={APIGen-MT: Agentic PIpeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay},
  author={Prabhakar, Akshara and Liu, Zuxin and Zhu, Ming and Zhang, Jianguo and Awalgaonkar, Tulika and Wang, Shiyu and Liu, Zhiwei and Chen, Haolin and Hoang, Thai and others},
  journal={arXiv preprint arXiv:2504.03601},
  year={2025}
}
```