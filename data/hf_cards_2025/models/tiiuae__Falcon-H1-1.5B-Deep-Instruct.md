---
library_name: transformers
tags:
- falcon-h1
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
base_model: tiiuae/Falcon-H1-1.5B-Deep-Base
inference: true
---

<img src="https://huggingface.co/datasets/tiiuae/documentation-images/resolve/main/falcon_mamba/falcon-h1-logo.png" alt="drawing" width="800"/>

#  Table of Contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Training Details](#training-details)
3. [Usage](#usage)
4. [Evaluation](#evaluation)
5. [Citation](#citation)

# TL;DR

# Model Details

## Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae)
- **Model type:** Causal decoder-only
- **Architecture:** Hybrid Transformers + Mamba architecture
- **Language(s) (NLP):** English, Multilingual
- **License:** Falcon-LLM License

# Training details

For more details about the training protocol of this model, please refer to the [Falcon-H1 technical blogpost](https://falcon-lm.github.io/blog/falcon-h1/) and [Technical Report](https://arxiv.org/abs/2507.22448).

# Usage

Currently to use this model you can either rely on Hugging Face `transformers`, `vLLM` or `llama.cpp` library.

## Inference

Make sure to install the latest version of `transformers` or `vllm`, eventually install these packages from source:

```bash
pip install git+https://github.com/huggingface/transformers.git
```

For vLLM, make sure to install `vllm>=0.9.0`:

```bash
pip install "vllm>=0.9.0"
```
### 🤗 transformers

Refer to the snippet below to run H1 models using 🤗 transformers:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "tiiuae/Falcon-H1-1B-Base"

model = AutoModelForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.bfloat16,
  device_map="auto"
)

# Perform text generation
```

### vLLM

For vLLM, simply start a server by executing the command below:

```
# pip install vllm>=0.9.0
vllm serve tiiuae/Falcon-H1-1B-Instruct --tensor-parallel-size 2 --data-parallel-size 1
```

### `llama.cpp`

You can find all GGUF files compatible with `llama.cpp` under [our official collection](https://huggingface.co/collections/tiiuae/falcon-h1-6819f2795bc406da60fab8df)

# Evaluation

Falcon-H1 series perform very well on a variety of tasks, including reasoning tasks. 

| Tasks | Falcon-H1-1.5B-deep | Qwen3-1.7B | Qwen2.5-1.5B | Gemma3-1B | Llama3.2-1B | Falcon3-1B |
| --- | --- | --- | --- | --- | --- | --- |
| **General**  | | | | | |
| BBH | **54.43** | 35.18 | 42.41 | 35.86 | 33.21 | 34.47 |
| ARC-C | **43.86** | 34.81 | 40.53 | 34.13 | 34.64 | 43.09 |
| TruthfulQA | **50.48** | 49.39 | 47.05 | 42.17 | 42.08 | 42.31 |
| HellaSwag | **65.54** | 49.27 | 62.23 | 42.24 | 55.3 | 58.53 |
| MMLU | **66.11** | 57.04 | 59.76 | 40.87 | 45.93 | 46.1 |
| **Math**  | | | | | |
| GSM8k | **82.34** | 69.83 | 57.47 | 42.38 | 44.28 | 44.05 |
| MATH-500 | **77.8** | 73.0 | 48.4 | 45.4 | 13.2 | 19.8 |
| AMC-23 | **56.56** | 46.09 | 24.06 | 19.22 | 7.19 | 6.87 |
| AIME-24 | **14.37** | 12.5 | 2.29 | 0.42 | 1.46 | 0.41 |
| AIME-25 | **11.04** | 8.12 | 1.25 | 1.25 | 0.0 | 0.21 |
| **Science**  | | | | | |
| GPQA | **33.22** | 27.68 | 26.26 | 28.19 | 26.59 | 26.76 |
| GPQA_Diamond | **40.57** | 33.33 | 25.59 | 21.55 | 25.08 | 31.31 |
| MMLU-Pro | **41.89** | 23.54 | 28.35 | 14.46 | 16.2 | 18.49 |
| MMLU-stem | **67.3** | 54.3 | 54.04 | 35.39 | 39.16 | 39.64 |
| **Code**  | | | | | |
| HumanEval | **73.78** | 67.68 | 56.1 | 40.85 | 34.15 | 22.56 |
| HumanEval+ | **68.9** | 60.96 | 50.61 | 37.2 | 29.88 | 20.73 |
| MBPP | **68.25** | 58.73 | 64.81 | 57.67 | 33.6 | 20.63 |
| MBPP+ | **56.61** | 49.74 | 56.08 | 50.0 | 29.37 | 17.2 |
| LiveCodeBench | **23.87** | 14.87 | 12.52 | 5.09 | 2.35 | 0.78 |
| CRUXEval | **52.32** | 18.88 | 34.76 | 12.7 | 0.06 | 15.58 |
| **Instruction Following**  | | | | | |
| IFEval | **83.5** | 70.77 | 45.33 | 61.48 | 55.34 | 54.26 |
| Alpaca-Eval | **27.12** | 21.89 | 9.54 | 17.87 | 9.38 | 6.98 |
| MTBench | **8.53** | 7.61 | 7.1 | 7.03 | 6.37 | 6.03 |
| LiveBench | 36.83 | **40.73** | 21.65 | 18.79 | 14.97 | 14.1 |

You can check more in detail on our [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/), detailed benchmarks.

# Useful links

- View [our release blogpost](https://falcon-lm.github.io/blog/falcon-h1/).
- View [our technical report](https://arxiv.org/abs/2507.22448).
- Feel free to join [our discord server](https://discord.gg/trwMYP9PYm) if you have any questions or to interact with our researchers and developers.

# Citation

If the Falcon-H1 family of models were helpful to your work, feel free to give us a cite.

```
@article{falconh1,
    title={Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance},
    author={Jingwei Zuo and Maksim Velikanov and Ilyas Chahed and Younes Belkada and Dhia Eddine Rhayem and Guillaume Kunsch and Hakim Hacid and Hamza Yous and Brahim Farhat and Ibrahim Khadraoui and Mugariya Farooq and Giulia Campesan and Ruxandra Cojocaru and Yasser Djilali and Shi Hu and Iheb Chaabane and Puneesh Khanna and Mohamed El Amine Seddik and Ngoc Dung Huynh and Phuc Le Khac and Leen AlQadi and Billel Mokeddem and Mohamed Chami and Abdalgader Abubaker and Mikhail Lubinets and Kacper Piskorski and Slim Frikha},
    journal = {arXiv preprint arXiv:2507.22448},
    year={2025}
}
```