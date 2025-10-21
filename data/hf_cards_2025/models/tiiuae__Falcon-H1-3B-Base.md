---
library_name: transformers
language:
- ar
- cs
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ro
- ru
- sv
- ur
- zh
tags:
- falcon-h1
license: other
license_name: falcon-llm-license
license_link: https://falconllm.tii.ae/falcon-terms-and-conditions.html
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

Currently to use this model you can either rely on Hugging Face `transformers`, `vLLM` or our custom fork of `llama.cpp` library.

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

While we are working on integrating our architecture directly into `llama.cpp` library, you can install our fork of the library and use it directly: https://github.com/tiiuae/llama.cpp-Falcon-H1 
Use the same installing guidelines as `llama.cpp`.

# Evaluation

Falcon-H1 series perform very well on a variety of tasks, including reasoning tasks. 

| Tasks | Falcon-H1-3B | Qwen3-4B | Qwen2.5-3B | Gemma3-4B | Llama3.2-3B | Falcon3-3B |
| --- | --- | --- | --- | --- | --- | --- |
| **General**  | | | | | |
| BBH | 53.17 | **56.88** | 46.4 | 40.41 | 39.45 | 44.02 |
| MMLU | 68.39 | **72.92** | 65.56 | 59.41 | 55.94 | 56.77 |
| ARC-C | 61.35 | **64.33** | 56.57 | 58.36 | 51.02 | 55.12 |
| HellaSwag | 73.85 | 75.74 | 74.6 | **77.62** | 76.39 | 67.13 |
| Winogrande | 68.11 | 72.3 | 71.03 | **72.77** | 72.22 | 65.11 |
| **Math**  | | | | | |
| GSM8k | 68.31 | **81.65** | 74.6 | 37.6 | 27.82 | 64.67 |
| MATH lvl5 | **25.83** | 24.47 | 16.09 | 6.95 | 1.74 | 11.56 |
| **Science**  | | | | | |
| GPQA | 32.63 | **34.9** | 28.44 | 29.78 | 28.78 | 29.78 |
| MMLU-Pro | 40.58 | **46.18** | 32.12 | 28.34 | 25.08 | 29.03 |
| MMLU-stem | 69.55 | **75.58** | 62.23 | 51.7 | 47.67 | 55.34 |
| **Code**  | | | | | |
| HumanEval | 59.15 | **74.39** | 42.68 | 33.54 | 29.27 | 36.59 |
| HumanEval+ | 53.66 | **68.9** | 35.37 | 28.05 | 26.22 | 31.71 |
| MBPP | 71.43 | **74.6** | 59.52 | 60.05 | 48.94 | 51.85 |
| MBPP+ | 57.94 | **63.76** | 50.53 | 51.32 | 39.42 | 42.06 |

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