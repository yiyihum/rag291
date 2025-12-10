---
language:
- en
license: apache-2.0
pipeline_tag: text-generation
tags:
- text-generation
- agent
- tool-use
- long-context
library_name: transformers
---

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="assets/sii.jpg" alt="SII" width="100px">
  <img src="assets/asi.png" alt="ASI" width="100px">
</div>

<div align="center">  
  

<a href="https://github.com/GAIR-NLP/LIMI" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="assets/teaser.jpg" style="display: inline-block; vertical-align: middle;"/>
</a>
</div>

# LIMI‑Air: Less is More for Agency

[![arXiv](https://img.shields.io/badge/arXiv-2509.17567-b31b1b.svg)](https://arxiv.org/pdf/2509.17567)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/GAIR-NLP/LIMI)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-blue)](https://huggingface.co/datasets/GAIR/LIMI)

---
To learn more about LIMI-Air, feel free to explore our documentation and resources. Our release consists of the following sections:

- **Model Zoo && Quick Start**: Basic usage and demonstrations with Transformers, vLLM, and SGLang for LIMI and LIMI-Air;
- **Evaluation**: Comprehensive evaluation suite with metrics for agentic capabilities assessment;
- **Prompting**: Usage of LIMI with frameworks for agentic applications, tool use, and reasoning tasks.

## Overview

LIMI‑Air is a smaller, faster agentic variant built on [GLM‑4.5‑Air](https://huggingface.co/zai-org/GLM-4.5-Air) (~106B), fine‑tuned with the same compact, high‑quality agentic data as LIMI.

## Model Details

- Base model: `zai-org/GLM-4.5-Air`
- Params: ~106B
- Framework: slime; Data: [GAIR/LIMI](https://huggingface.co/datasets/GAIR/LIMI)

## Model Zoo

Our LIMO model is available on Hugging Face 🤗:

| Model | Backbone | Size | Link |
|---|---|---|---|
| LIMI | [GLM‑4.5](https://huggingface.co/zai-org/GLM-4.5) | 353B | https://huggingface.co/GAIR/LIMI |
| LIMI‑Air | [GLM‑4.5‑Air](https://huggingface.co/zai-org/GLM-4.5-Air) | 107B | https://huggingface.co/GAIR/LIMI-Air |

## Performance on AgencyBench

Our models achieve state-of-the-art performance across multiple agentic evaluation tasks:

| Model | FTFC (↑) | RC@3 (↑) | SR@3 (↑) | Avg. |
|-------|----------|----------|----------|-----------------|
| GLM-4.5-Air | 15.0 | 16.1 | 20.0 | 17.0 |
| GLM-4.5 | 37.8 | 50.0 | 47.4 | 45.1 |
|GLM-4.5-Code| 48.0 | 48.0|47.5| 47.8|
| **LIMI-Air** | **35.4** | **34.3** | **33.1** | **34.3** |
| **LIMI** | **71.7** | **74.2** | **74.6** | **73.5** |


For detailed benchmark results, experimental setup, and comprehensive comparisons, please refer to our [paper](https://arxiv.org/pdf/2509.17567). 

## Datasets

We release our datasets through Hugging Face 🤗:
- Name: `GAIR/LIMI`
- Summary: curated agentic SFT data (OpenAI `messages`, optional `tools`, normalized tool‑call arguments); current release contains 78 high‑quality samples.
- Link: https://huggingface.co/datasets/GAIR/LIMI

## Quick Start

<details>
<summary>Start with HF Transformers</summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
model = AutoModelForCausalLM.from_pretrained(
    "GAIR/LIMI-Air", torch_dtype="auto", device_map="auto", trust_remote_code=True
)
tok = AutoTokenizer.from_pretrained("GAIR/LIMI-Air", trust_remote_code=True)
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
out = model.generate(
    **tok(text, return_tensors="pt").to(model.device),
    max_new_tokens=4096,
    temperature=0.6,
    top_p=0.95,
    do_sample=True,
)
```

</details>

<details>
<summary>Start with VLLM</summary>

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
llm = LLM(model="GAIR/LIMI-Air", trust_remote_code=True)
tok = AutoTokenizer.from_pretrained("GAIR/LIMI-Air", trust_remote_code=True)
text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
out = llm.generate(text, SamplingParams(temperature=0.6, max_tokens=4096, top_p=0.95))
```

</details>

## Prompting

Same as LIMI; provide messages in OpenAI chat format, optionally with `tools`. Include a grounding system message when helpful.

## Evaluation

Uses the same metrics (FTFC, SR@R, RC@R at R=3) and protocol as LIMI; see the paper for comparative results.

## Limitations

- Inherits base model constraints; validated on curated agentic tasks only
- Lower compute cost with potential performance trade‑offs on complex tasks

## License

- Inherits GLM‑4.5‑Air terms; verify upstream license before deployment

## Citation

```bibtex
@misc{xiao2025limiagency,
      title={LIMI: Less is More for Agency}, 
      author={Yang Xiao and Mohan Jiang and Jie Sun and Keyu Li and Jifan Lin and Yumin Zhuang and Ji Zeng and Shijie Xia and Qishuo Hua and Xuefeng Li and Xiaojie Cai and Tongyu Wang and Yue Zhang and Liming Liu and Xia Wu and Jinlong Hou and Yuan Cheng and Wenjie Li and Xiang Wang and Dequan Wang and Pengfei Liu},
      year={2025},
      eprint={2509.17567},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2509.17567}, 
}
```