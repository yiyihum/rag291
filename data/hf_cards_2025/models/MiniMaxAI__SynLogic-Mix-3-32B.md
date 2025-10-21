---
base_model:
- Qwen/Qwen2.5-32B
datasets:
- MiniMaxAI/SynLogic
language:
- en
library_name: transformers
license: mit
tags:
- LLM
pipeline_tag: text-generation
---

# SynLogic Zero-Mix-3: Large-Scale Multi-Domain Reasoning Model

* 🐙 **GitHub Repo:** [https://github.com/MiniMax-AI/SynLogic](https://github.com/MiniMax-AI/SynLogic)
* 📜 **Paper (arXiv):** [https://arxiv.org/abs/2505.19641](https://arxiv.org/abs/2505.19641)
* 🤗 **Dataset:** [SynLogic on Hugging Face](https://huggingface.co/datasets/MiniMaxAI/SynLogic)

## Model Overview

**Zero-Mix-3** is an advanced multi-domain reasoning model trained using Zero-RL (reinforcement learning from scratch) on a diverse mixture of logical reasoning, mathematical, and coding data. Built on Qwen2.5-32B-Base, this model demonstrates the power of combining diverse verifiable reasoning tasks in a unified training framework.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "MiniMaxAI/SynLogic-Mix-3-32B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto")

prompt = "What is 2 + 2?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Key Features

* **Multi-Domain Training:** Jointly trained on logical reasoning (SynLogic), mathematics, and coding tasks
* **Zero-RL Training:** Trained from base model without instruction tuning, using pure reinforcement learning
* **Diverse Data Mixture:** 35k mathematical samples + 9k coding samples + 17k SynLogic samples
* **Enhanced Generalization:** Superior cross-domain transfer compared to single-domain training

## Performance Highlights

| Model | BBEH | KOR-Bench | LiveCodeBench | AIME 2024 | GPQA Diamond |
|-------|------|-----------|---------------|-----------|--------------|
| DeepSeek-R1-Distill-Qwen-32B | 19.2 | 66.6 | 57.2 | 72.6 | 63.1 |
| DeepSeek-R1-Zero-Qwen-32B | - | - | 40.2 | **47.0** | 55.0 |
| Zero-Mix-2 (Math+Coding) | 18.5 | 58.6 | 39.5 | 34.5 | 55.2 |
| **Zero-Mix-3 (SynLogic+Math+Coding)** | **28.6** | **65.0** | **40.7** | 35.8 | **57.5** |

**Key Achievements:**
- **Matches or Surpasses** DeepSeek-R1-Distill-Qwen-32B on KOR-Bench and BBEH (+9.4 points)
- **Outperforms** DeepSeek-R1-Zero-Qwen-32B on LiveCodeBench and GPQA-Diamond (+2.5 points)


## Training Details

* **Base Model:** Qwen2.5-32B-Base
* **Training Algorithm:** GRPO (Group Relative Policy Optimization)
* **Training Data:**
  - 35k mathematical reasoning samples
  - 9k coding problem samples  
  - 17k SynLogic logical reasoning samples


## Ablation Insights

Comparison with Zero-Mix-2 (Math+Coding only) demonstrates that adding SynLogic logical reasoning data:
- **+10.1 points** on logical reasoning (BBEH)
- **+6.4 points** on logical reasoning (KOR-Bench)
- **+2.3 points** on out-of-domain reasoning (GPQA-Diamond)
- **+1.2 points** on coding (LiveCodeBench)



## Citation

```bibtex
@misc{liu2025synlogic,
      title={SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond}, 
      author={Junteng Liu and Yuanxiang Fan and Zhuo Jiang and Han Ding and Yongyi Hu and Chi Zhang and Yiqi Shi and Shitong Weng and Aili Chen and Shiqi Chen and Yunan Huang and Mozhi Zhang and Pengyu Zhao and Junjie Yan and Junxian He},
      year={2025},
      eprint={2505.19641},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2505.19641}, 
}
```