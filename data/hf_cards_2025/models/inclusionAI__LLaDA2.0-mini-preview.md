---
license: apache-2.0
library_name: transformers
tags:
- dllm
- diffusion
- llm
- text_generation
---
# LLaDA2-mini-preview
**LLaDA2-mini-preview** is a diffusion language model featuring a 16BA1B Mixture-of-Experts (MoE) architecture. As an enhanced, instruction-tuned iteration of the LLaDA series, it is optimized for practical applications.

<div align="center">
  <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*DeZ9RKxU-LoAAAAAgQAAAAgAemJ7AQ/original" width="800" />
</div>


---

| Benchmark | Ling-mini-2.0 | LLaDA-MoE-7B-A1B-Instruct | LLaDA2.0-mini-preview |
| :------------------------------ | :-------------: | :-------------------------: | :---------------------: |
| **Average** | 60.67 | 52.39 | 58.71 |
| **Knowledge** | | | |
| MMLU | 78.75 | 67.18 | 72.49 |
| MMLU-PRO | 56.40 | 44.64 | 49.22 |
| GPQA | 37.99 | 31.09 | 31.82 |
| CMMLU | 77.84 | 64.30 | 67.53 |
| C-EVAL | 77.85 | 63.93 | 66.54 |
| **Reasoning** | | | |
| squad2.0 | 69.14 | 86.81 | 85.61 |
| drop | 76.35 | 79.77 | 79.49 |
| korbench | 51.04 | 38.40 | 37.26 |
| **Coding** | | | |
| CruxEval-O | 71.12 | 42.38 | 61.88 |
| mbpp | 81.03 | 70.02 | 77.75 |
| MultiPL-E | 62.23 | 52.53 | 62.43 |
| humaneval | 77.44 | 61.59 | 80.49 |
| livecodebench_v6 | 30.18 | 13.27 | 19.93 |
| Bigcodebench-Full | 35.88 | 20.44 | 30.44 |
| **Math** | | | |
| GSM8K | 91.58 | 82.41 | 89.01 |
| math | 82.22 | 58.68 | 73.50 |
| OlympiadBench | 49.93 | 21.04 | 36.67 |
| **Agent & Alignment** | | | |
| BFCL_Live | 45.74 | 63.09 | 74.11 |
| IFEval-strict -prompt | 69.13 | 59.33 | 62.50 |
| SyllogEval<sup>*</sup> | 33.28 | 64.22 | 47.34 |
| IXRB<sup>*</sup> | 19.00 | 15.00 | 27.00 |


**SyllogEval**<sup>*</sup> is a logic benchmark designed to evaluate the formal reasoning capabilities of Large Language Models (LLMs).

**IXRB**<sup>*</sup> is a novel benchmark for evaluating the abductive reasoning and creativity of LLMs.

We'll release these two benchmarks in ABench (https://github.com/inclusionAI/ABench).


## 🚀 Performance Highlights
+ **Leading MoE Architecture**:
The open-source **Mixture-of-Experts (MoE) diffusion large language model**, pre-trained from scratch on approximately **20 trillion tokens**.
+ **Efficient Inference**:
With **16 billion total parameters**, only **1.4 billion** are activated during inference. LLaDA-mini-preview significantly reduces computational costs while outperforming open-source dense models of similar scale.
+ **Impressive Performance on Code & Complex Reasoning**:
Excels in tasks such as **code generation** and **advanced mathematical reasoning**, demonstrating strong reasoning capabilities.
+ **Tool Use**:
Supports **tool calling** and achieves excellent performance in complex agent-based tasks.
+ **Open & Extensible**:
Fully open-source with commitment to transparency. We plan to release a **leading inference framework** in the future and continue investing in cutting-edge areas like **diffusion LLMs (dLLM)** to drive disruptive innovation.

---

## 📦 Model Variants
| Model ID | Description | Hugging Face Link |
| --- | --- | --- |
| `inclusionAI/LLaDA2-mini-preview` | Instruction-tuned model, ready for downstream applications. | [🤗 Model Card](https://huggingface.co/inclusionAI/LLaDA2.0-mini-preview) |


---

## 🔍 Model Overview
**LLaDA2-mini-preview** has the following specifications:

+ **Type**: Mixture-of-Experts (MoE) Diffusion Language Model
+ **Total Parameters (Non-Embedding)**: 16B
+ **Number of Layers**: 20
+ **Attention Heads**: 16
+ **Context Length**: 4,096 tokens
+ **Position Embedding**: Rotary (RoPE)
+ **Vocabulary Size**: 157,184

---

### 🤗 Hugging Face Transformers
Make sure you have `transformers` and its dependencies installed:

```python
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

model_path = "/path/to/LLaDA2-mini-preview"
device = "cuda:0"
model = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True, device_map=device
)
model = model.to(torch.bfloat16)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

prompt = "Why does Camus think that Sisyphus is happy?"
input_ids = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt",
)
generated_tokens = model.generate(
    inputs=input_ids,
    eos_early_stop=True,
    gen_length=512,
    block_length=32,
    steps=32,
    temperature=0.0,
)
generated_answer = tokenizer.decode(
    generated_tokens[0],
    skip_special_tokens=True,
)
print(generated_answer)
```

### Best Practices
To achieve optimal performance, we recommend the following settings:

1. **Sampling Parameters**:
   We suggest using `Temperature=0.0`, `block_length=32`, and `steps=32`. Using a higher temperature value may occasionally result in language mixing and a slight decrease in model performance.

2. **Adequate Output Length**:
   We recommend using an output length of 2048 tokens for most queries. For benchmarking on problems require more output length, such as those found in math and programming competitions, we suggest setting the max output length to 4096 tokens.


---

## 🌐 License
This project is licensed under the terms of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

## 🤝 Contact & Collaboration
For questions, collaborations, or feedback, please reach out via [Hugging Face](https://huggingface.co/inclusionAI/LLaDA2.0-mini-preview) or open an issue in the [repository](https://github.com/inclusionAI).

👉 Join us in advancing open, efficient, and intelligent language models!