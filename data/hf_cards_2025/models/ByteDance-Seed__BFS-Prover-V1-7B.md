---
base_model:
- Qwen/Qwen2.5-Math-7B
datasets:
- internlm/Lean-Workbook
- internlm/Lean-Github
- AI-MO/NuminaMath-CoT
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- lean4
- theorem-proving
- formal-mathematics
---

<div align="center">
  <h1 style="font-size: 2.0em;">🚀 BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving</h1>
  <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;">
    <a href="https://arxiv.org/abs/2502.03438"><img src="https://img.shields.io/badge/arXiv-2502.03438-b31b1b.svg" alt="arXiv"></a>
    <a href="https://github.com/ByteDance-Seed/BFS-Prover-V2"><img src="https://img.shields.io/badge/GitHub-Code-blue.svg?logo=github" alt="GitHub Code"></a>
    <a href="https://choosealicense.com/licenses/apache-2.0/"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
    <a href="https://github.com/leanprover-community/mathlib4"><img src="https://img.shields.io/badge/Lean-4-orange" alt="Lean 4"></a>
  </div>
  <h2>State-of-the-art tactic generation model in Lean4</h2>
</div>

This repository contains the latest tactic generator model checkpoint from BFS-Prover, a state-of-the-art theorem proving system in Lean4. While the full BFS-Prover system integrates multiple components for scalable theorem proving, we are releasing the core tactic generation model here. Given a proof state in Lean4, the model generates a tactic that transforms the current proof state into a new state, progressively working towards completing the proof.

**📑 Paper: [BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving](https://arxiv.org/abs/2502.03438)**

**💻 Code: [GitHub Repository](https://github.com/ByteDance-Seed/BFS-Prover-V2)**

## ✨ Model Details

- Base Model: Qwen2.5-Math-7B
- Training Approach: 
  - Supervised Fine-Tuning (SFT) on state-tactic pairs
  - Direct Preference Optimization (DPO) using compiler feedback
- Training Data Sources:
  - Mathlib (via LeanDojo)
  - Lean-Github repositories
  - Lean-Workbook
  - Autoformalized NuminaMath-CoT dataset

## 📈 Performance
BFS-Prover achieves state-of-the-art performance on the MiniF2F test benchmark. Here's a detailed comparison:

### 🔍 MiniF2F Test Benchmark Results

| Prover System | Search Method | Critic Model | Tactic Budget | Score |
|---------------|---------------|--------------|---------------|--------|
| BFS-Prover  | BFS | No | Accumulative | **72.95%** |
| BFS-Prover  | BFS | No | 2048×2×600 | **70.83% ± 0.89%** |
| HunyuanProver | BFS | Yes | 600×8×400 | 68.4% |
| InternLM2.5-StepProver | BFS | Yes | 256×32×600 | 65.9% |
| DeepSeek-Prover-V1.5 | MCTS | No | 32×16×400 | 63.5% |


### 🔑 Key Advantages
- ✅ Achieves better performance without requiring a critic model (value function)
- ✅ Combined with simpler search method (BFS) rather than MCTS

## ⚙️ Usage
- The model expects Lean4 tactic states in the format `"{state}:::"`
- `:::` serves as a special indicator to signal the model to generate a tactic for the given state. 
- The model will echo back the input state followed by the generated tactic.


```python
# Example code for loading and using the tactic generator model
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("bytedance-research/BFS-Prover")
tokenizer = AutoTokenizer.from_pretrained("bytedance-research/BFS-Prover")
state = "h : x = y + 2 ⊢ x - 1 = y + 1" 
sep = ":::"
prompt = state + sep  # Creates "h : x = y + 2 ⊢ x - 1 = y + 1:::"

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs)
tactic = tokenizer.decode(outputs[0], skip_special_tokens=True).split(sep)[1]
print(tactic)

# Complete example:
# Input state:  "h : x = y + 2 ⊢ x - 1 = y + 1"
# Full prompt:  "h : x = y + 2 ⊢ x - 1 = y + 1:::"
# Model output: "h : x = y + 2 ⊢ x - 1 = y + 1:::simp [h]"
# Final tactic: "simp [h]"
```

## 📚 Citation

If you use this model in your research, please cite our paper:

```bibtex
@article{xin2025bfs,
  title={BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving},
  author={Xin, Ran and Xi, Chenguang and Yang, Jie and Chen, Feng and Wu, Hang and Xiao, Xia and Sun, Yifan and Zheng, Shen and Shen, Kai},
  journal={arXiv preprint arXiv:2502.03438},
  year={2025}
}
```

## 📄 License

https://choosealicense.com/licenses/apache-2.0/

## 📧 Contact

For questions and feedback about the tactic generator model, please contact:
- Ran Xin (ran.xin@bytedance.com)
- Kai Shen (shen.kai@bytedance.com)