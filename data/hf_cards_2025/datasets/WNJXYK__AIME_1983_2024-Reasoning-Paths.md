---
license: mit
task_categories:
- text-generation
language:
- en
tags:
- math
viewer: false
---

# 🌟🌟🌟 Try this dataset in our [HuggingFace Space](https://huggingface.co/spaces/WNJXYK/RPC) 🌟🌟🌟

# Sampled Reasoning Paths for the AIME dataset (from 1983 to 2024)

This dataset contains sampled reasoning paths for the [AIME_1983_2024](https://huggingface.co/datasets/di-zhang-fdu/AIME_1983_2024) dataset, released as part of the NeurIPS 2025 paper: ["A Theoretical Study on Bridging Internal Probability and Self-Consistency for LLM Reasoning"](https://wnjxyk.github.io/RPC) ([[Arxiv](arxiv.org/abs/2510.15444)](https://arxiv.org/abs/2510.15444)).

## Overview

We generated multiple reasoning paths for AIME_1983_2024 problems using 3 math LLMs:
* [Deepseek-Math-RL-7B](https://huggingface.co/deepseek-ai/deepseek-math-7b-rl)
* [InternLM2-Math-Plus-1.8B](https://huggingface.co/internlm/internlm2-math-plus-1_8b)
* [InternLM2-Math-Plus-7B](https://huggingface.co/internlm/internlm2-math-plus-7b)

For each problem in the AIME_1983_2024 dataset, we sampled 256 reasoning paths. Sampling was performed with temperatures ∈ {1.0, 1.1, 1.3} to explore diverse reasoning trajectories.


## Structure of each JSON

The JSON structure is illustrated below with an example of 3 samples per problem across 2 problems:

```json
{
    "predict": [        // 2D string array: [problems][samples]
        ["Prediction #1 for Problem 1", "Prediction #2 for Problem 1", "Prediction #3 for Problem 1"],
        ["Prediction #1 for Problem 2", "Prediction #2 for Problem 2", "Prediction #3 for Problem 2"]
    ],
    "answer": [         // Ground truth answers
        "Answer for Problem 1", "Answer for Problem 2"
    ],
    "completion": [     // 2D string array: [problems][samples]
        ["Completion #1 for Problem 1", "Completion #2 for Problem 1", "Completion #3 for Problem 1"],
        ["Completion #1 for Problem 2", "Completion #2 for Problem 2", "Completion #3 for Problem 2"]
    ],
    "cumulative_logprob": [  // Sum of log probabilities per sample
        [-15.526, -12.123, -14.12],
        [-20.526, -22.123, -24.12]
    ],
    "mean_logprob": [   // Normalized log probabilities (sum / sequence length, i.e., perplexity)
        [-0.070, -0.04, -0.05],
        [-0.170, -0.14, -0.15]
    ],
    "prompt": [         // Input prompts for each problem
        "Prompt for Problem 1", "Prompt for Problem 2"
    ],
    "temperature": 0,   // Sampling temperature
    "top_p": 1,         // Nucleus sampling parameter
    "accuracy": [       // 2D boolean array: [samples][problems]
        [false, true],
        [true, true],
        [true, true]
    ]
}
```

## Available Files

||Deepseek-Math-RL-7B|InternLM2-Math-Plus-7B|InternLM2-Math-Plus-1.8B|
|:--:|:--|:--|:--|
|T=1.0|`Deepseek-Math-RL-7B.json`|`InternLM2-Math-Plus-7B.json`|`InternLM2-Math-Plus-1.8B.json`|
|T=1.1|`Deepseek-Math-RL-7B-T=1.1.json`|`InternLM2-Math-Plus-7B-T=1.1.json`|`InternLM2-Math-Plus-1.8B-T=1.1.json`|
|T=1.3|`Deepseek-Math-RL-7B-T=1.3.json`|`InternLM2-Math-Plus-7B-T=1.3.json`|`InternLM2-Math-Plus-1.8B-T=1.3.json`|


## Citation

If you use this dataset in your research, please cite:

```bibtex
@inproceedings{zhou24theoretical,
  author    = {Zhou, Zhi and Tan, Yuhao and Li, Zenan and Yao, Yuan and Guo, Lan-Zhe and Li, Yu-Feng and Ma, Xiaoxing},
  title     = {A Theorecial Study on Bridging Internal Probability and Self-Consistency for LLM Reasoning},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2025},
}
```