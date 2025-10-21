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

# SynLogic-32B: Advanced Logical Reasoning Model

* 🐙 **GitHub Repo:** [https://github.com/MiniMax-AI/SynLogic](https://github.com/MiniMax-AI/SynLogic)
* 📜 **Paper (arXiv):** [https://arxiv.org/abs/2505.19641](https://arxiv.org/abs/2505.19641)
* 🤗 **Dataset:** [SynLogic on Hugging Face](https://huggingface.co/datasets/MiniMaxAI/SynLogic)

## Model Overview

**SynLogic-32B** is a state-of-the-art reasoning model built on Qwen2.5-32B-Base and trained using reinforcement learning on our comprehensive SynLogic dataset. The model excels at logical reasoning tasks and demonstrates strong generalization to mathematical domains.

## Key Features

* **Comprehensive Logical Reasoning:** Trained on 35 diverse logical reasoning tasks including Sudoku, Game of 24, Cipher, Arrow Maze, and more
* **Verifiable Training:** All training data can be automatically verified, enabling effective reinforcement learning
* **Strong Generalization:** Transfers logical reasoning skills to mathematical problem-solving without explicit math training

## Performance Highlights

| Model | BBEH | KOR-Bench | BBH |
|-------|------|-----------|-----|
| Qwen2.5-32B-Instruct | 17.5 | 54.7 | 84.5 |
| DeepSeek-R1-Distill-Qwen-32B | 19.2 | **66.6** | **88.3** |
| **SynLogic-32B** | **25.5** | 62.2 | 85.8 |

**Key Achievement:** +6 points improvement over DeepSeek-R1-Distill-Qwen-32B on the challenging BBEH benchmark, establishing state-of-the-art performance among open-source logical reasoning models.

## Training Details

* **Base Model:** Qwen2.5-32B-Base
* **Training Algorithm:** GRPO (Group Relative Policy Optimization)
* **Dataset:** 33k SynLogic-Hard samples with controlled difficulty
* **Reward Design:** Binary rewards based on format adherence and correctness verification

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