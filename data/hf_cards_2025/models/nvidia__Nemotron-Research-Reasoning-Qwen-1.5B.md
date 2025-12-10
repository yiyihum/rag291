---
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
language:
- en
license: cc-by-nc-4.0
pipeline_tag: text-generation
library_name: transformers
---

<div align="center">
<span style="font-family: default; font-size: 1.5em;">Nemotron-Research-Reasoning-Qwen-1.5B</span>
<div>
🚀 The leading generalist reasoning model for cutting-edge research and development 🌟
</div>
</div>

![Comparison between DeepSeek-R1-1.5B and Nemotron-Research-Reasoning-Qwen-1.5B](./assets/deepseek_vs_nvidia102.png)

## News
- [2025-08-11] ProRL V2 blog post is released: [ProRL V2 - Prolonged Training Validates RL Scaling Laws](https://research.nvidia.com/labs/lpr/prorlv2/).
- [2025-07-23] Nemotron-Research-Reasoning-Qwen-1.5B-v2 is released.
- [2025-05-29] Nemotron-Research-Reasoning-Qwen-1.5B is released.

## Introduction
Nemotron-Research-Reasoning-Qwen-1.5B is the world’s leading 1.5B open-weight model for complex reasoning tasks such as mathematical problems, coding challenges, scientific questions, and logic puzzles.
It is trained using the ProRL algorithm on a diverse and comprehensive set of datasets.
Our model has achieved impressive results, outperforming Deepseek’s 1.5B model by a large margin on a broad range of tasks, including math, coding, and GPQA.

This model is for research and development only.

## ProRL: Prolonged Reinforcement Learning
ProRL is designed to enable extended RL training periods that facilitate deeper exploration of reasoning strategies. 
It enables more than 2k training steps and scale the training data across diverse tasks—from traditional math and code tasks to STEM problems, logical puzzles, and instruction following, which, we hypothesize, are crucial for generalization. 
Based on Group Relative Policy Optimization (GRPO), ProRL introduces three key techniques:
1. Mitigating Entropy Collapse
2. Decoupled clip and dynamic sampling policy optimization (DAPO)
3. KL regularization and reference policy reset 

Using ProRL, we developed the world's best 1.5B reasoning model that significantly outperforms its base model, DeepSeek-R1-1.5B, and matches or even surpasses the performance of DeepSeek-R1-7B across a diverse range of benchmarks. 
Notably, compared to DeepSeek-R1-1.5B, we achieve average pass@1 improvements of 14.7\% on math benchmarks, 13.9\% on coding, 54.8\% on logic puzzles, 25.1\% on STEM reasoning, and 18.1\% on instruction-following tasks. 

## Training Datasets
| Dataset                      | Link                                                                                         |
|---------------------------|-------------------------------------------------------------------------------------------|
| DeepScaleR-Preview-Dataset  | [Link](https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset)                   |
| Eurus-2-RL-Data           | [Link](https://huggingface.co/datasets/PRIME-RL/Eurus-2-RL-Data)                             |
| Reasoning-gym            | [Link](https://github.com/open-thought/reasoning-gym)                                        |
| IFEval                     | [Link](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset)   |
| SCP-116K                   | [Link](https://huggingface.co/datasets/EricLu/SCP-116K)                                  |


## Evaluation Results

Table 1: Performance (pass@1) comparison for benchmarks across Math domain. 
| Model                          | AIME24 | AIME25 | AMC   | Math  | Minerva | Olympiad | Avg   |
|-------------------------------|--------|--------|-------|-------|----------|----------|--------|
| DeepSeek-R1-Distill-Qwen-1.5B | 28.54  | 22.71  | 62.58 | 82.90 | 26.38    | 43.58    | 44.45  |
| DeepScaleR-1.5B               | 40.21  | 31.46  | 73.04 | 89.36 | 41.57    | 51.63    | 54.54  |
| *DeepSeek-R1-Distill-Qwen-7B* | 53.54  | 40.83  | 82.83 | 93.68 | 50.60    | 57.66    | 63.19  |
| **Nemotron-Research-Reasoning-Qwen-1.5B**                 | 48.13 | 33.33 | 79.29 | 91.89 | 47.98 | 60.22 | 60.14 |
| **Nemotron-Research-Reasoning-Qwen-1.5B-v2**                 | **49.58** | **36.04** | **82.53** | **92.49** | **49.03** | **60.44** | **61.69** |

Table 2: Performance (pass@1) comparison across benchmarks for Code. We abbreviate benchmarks names for codecontests (cc), codeforces (cf), humanevalplus (human), and livecodebench (LCB).
| Model                          | apps  | cc    | cf    | taco  | human | LCB   | Avg    |
|-------------------------------|--------|--------|--------|--------|--------|--------|--------|
| DeepSeek-R1-Distill-Qwen-1.5B | 20.95  | 16.79 | 14.13 | 8.03  | 61.77 | 16.80 | 23.08  |
| DeepCoder-1.5B                | 30.37  | 23.76 | 21.70 | 13.76 | 73.40 | 22.76 | 30.96  |
| *DeepSeek-R1-Distill-Qwen-7B* | 42.08  | 32.76 | 33.08 | 19.08 | 83.32 | 38.04 | 41.39  |
| **Nemotron-Research-Reasoning-Qwen-1.5B**                 | 41.99 | 31.80 | 34.50 | 20.81 | 72.05 | 23.81 | 37.49 |
| **Nemotron-Research-Reasoning-Qwen-1.5B-v2**                 | **46.39** | **35.59** | **40.75** | **22.89** | 72.89 | **27.69** | **41.03** |

Table 3: Performance comparison on STEM reasoning (GPQA Diamond), instruction following (IFEval), and logic puzzles (Reasoning Gym) tasks. We also present results on OOD tasks: acre, boxnet, and game_of_life_halting (game).
| Model                          | GPQA  | IFEval | Reasoning | acre  | boxnet | game  |
|-------------------------------|--------|--------|-----------|--------|--------|--------|
| DeepSeek-R1-Distill-Qwen-1.5B | 15.86  | 44.05  | 4.24      | 5.99  | 0.00   | 3.49  |
| *DeepSeek-R1-Distill-Qwen-7B* | 35.44  | 58.01  | 28.55     | 20.21 | 1.71   | 12.94 |
| **Nemotron-Research-Reasoning-Qwen-1.5B**                 | **41.78** | 66.02 | 59.06 | **58.57** | **7.91** | **52.29** |
| **Nemotron-Research-Reasoning-Qwen-1.5B-v2**                 | 41.32 | **70.85** | **62.49** | - | - | - |


## Nemotron-Research-Reasoning-Qwen-1.5B-v2

In the wake of the release of Nemotron-Research-Reasoning-Qwen-1.5B, we scaling the training steps from 2000 to 3000, resulting in Nemotron-Research-Reasoning-Qwen-1.5B-v2.
Nemotron-Research-Reasoning-Qwen-1.5B-v2 builds on top of REINFORCE++-baseline with dynamic sampling and clip-higher, and proposes several critical enhancements such as periodically refreshing the reference model with the current best checkpoint and imposing the length penalty only in scheduled cycles. 
Together, these techniques allow model performance to continually improve with more RL training steps and expand LLMs' reasoning boundaries. 
Our latest checkpoint, Nemotron-Research-Reasoning-Qwen-1.5B-v2, trained for 3000 steps, sets a new state-of-the-art (SOTA) among 1.5B reasoning models.

For the Nemotron-Research-Reasoning-Qwen-1.5B-v2, you can use the following code to load the model:
```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("nvidia/Nemotron-Research-Reasoning-Qwen-1.5B")
model = AutoModelForCausalLM.from_pretrained("nvidia/Nemotron-Research-Reasoning-Qwen-1.5B")
```

For the original Nemotron-Research-Reasoning-Qwen-1.5B, you can use the following code to load the model:
```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("nvidia/Nemotron-Research-Reasoning-Qwen-1.5B", revision="v1")
model = AutoModelForCausalLM.from_pretrained("nvidia/Nemotron-Research-Reasoning-Qwen-1.5B", revision="v1")
```


## License/Terms of Use
cc-by-nc-4.0

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Citation
If you find our dataset helpful, please cite the following [paper](https://arxiv.org/abs/2505.24864):

```
@article{liu2025prorl,
  author    = {Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, Yi Dong},
  title={ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models}, 
  journal   = {arXiv preprint},
  year      = {2025},
  archivePrefix = {arXiv},
  primaryClass = {cs.CL},
  url={https://arxiv.org/abs/2505.24864}, 
}
```