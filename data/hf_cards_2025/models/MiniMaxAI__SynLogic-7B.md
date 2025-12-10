---
base_model:
- Qwen/Qwen2.5-7B
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

# SynLogic-7B: Logical Reasoning Model

* 🐙 **GitHub Repo:** [https://github.com/MiniMax-AI/SynLogic](https://github.com/MiniMax-AI/SynLogic)
* 📜 **Paper (arXiv):** [https://arxiv.org/abs/2505.19641](https://arxiv.org/abs/2505.19641)
* 🤗 **Dataset:** [SynLogic on Hugging Face](https://huggingface.co/datasets/MiniMaxAI/SynLogic)

## Model Overview

**SynLogic-7B** is a logical reasoning model built on Qwen2.5-7B-Base and trained using reinforcement learning on our SynLogic dataset. Despite its smaller size, the model demonstrates strong logical reasoning capabilities and effective generalization to mathematical domains.

## Key Features

* **Comprehensive Logical Reasoning:** Trained on 27 diverse logical reasoning tasks (adapted for 7B scale) including Sudoku, Game of 24, Cipher, and more
* **Verifiable Training:** All training data can be automatically verified, enabling effective reinforcement learning
* **Strong Generalization:** Transfers logical reasoning skills to mathematical problem-solving without explicit math training
* **Efficient Scale:** Achieves strong performance with a more compact 7B parameter model

## Performance Highlights

### Logical Reasoning Benchmarks
| Model | KOR-Bench | BBH | BBEH |
|-------|-----------|-----|------|
| Qwen2.5-7B-Instruct | 38.6 | 62.7 | 12.4 |
| **SynLogic-7B** | **48.1** | **66.5** | 8.0 |

### Mathematical Benchmarks
| Model | AIME 2024 | MATH 500 | AMC 2023 |
|-------|-----------|----------|----------|
| Qwen2.5-7B-Base | 0.3 | 64.6 | 30.0 |
| Qwen2.5-7B-Instruct | 6.3 | 76.4 | 52.5 |
| **SynLogic-7B** | **10.0** | 71.8 | **55.0** |

**Key Achievements:**
- **+9.5 points** improvement over Qwen2.5-7B-Instruct on KOR-Bench
- Strong mathematical generalization with **10.0%** on AIME 2024 (vs 6.3% for instruct model)
- Effective logical reasoning training despite smaller model size

## Training Details

* **Base Model:** Qwen2.5-7B-Base
* **Training Algorithm:** GRPO (Group Relative Policy Optimization)
* **Dataset:** 16k SynLogic-Easy samples with controlled difficulty optimized for 7B scale
* **Reward Design:** Binary rewards based on format adherence and correctness verification
* **Response Length:** Achieves average response lengths of ~2,500 tokens with emerging reflection behaviors

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