---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
base_model:
- PowerInfer/SmallThinker-4BA0.6B-Instruct
---
## SmallThinker-4BA0.6B-Instruct-GGUF

- GGUF models with `.gguf` suffix can used with [*llama.cpp*](https://github.com/ggml-org/llama.cpp) framework.

- GGUF models with `.powerinfer.gguf` suffix are integrated with fused sparse FFN operators and sparse LM head operators. These models are only compatible to [*powerinfer*](https://github.com/SJTU-IPADS/PowerInfer/tree/main/smallthinker) framework.


## Introduction

<p align="center">
       &nbsp&nbsp🤗 <a href="https://huggingface.co/PowerInfer">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/PowerInfer">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://github.com/SJTU-IPADS/SmallThinker/blob/main/smallthinker-technical-report.pdf">Technical Report</a> &nbsp&nbsp 
</p>

SmallThinker is a family of **on-device native** Mixture-of-Experts (MoE) language models specially designed for local deployment,
co-developed by the **IPADS and School of AI at Shanghai Jiao Tong University** and **Zenergize AI**.
Designed from the ground up for resource-constrained environments,
SmallThinker brings powerful, private, and low-latency AI directly to your personal devices,
without relying on the cloud.

## Performance

Note: The model is trained mainly on English.

| Model | MMLU | GPQA-diamond | GSM8K | MATH-500 | IFEVAL | LIVEBENCH | HUMANEVAL | Average |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SmallThinker-4BA0.6B-Instruct** | **66.11** | **31.31** | 80.02 | <u>60.60</u> | 69.69 | **42.20** | **82.32** | **61.75** |
| Qwen3-0.6B | 43.31 | 26.77 | 62.85 | 45.6 | 58.41 | 23.1 | 31.71 | 41.67 |
| Qwen3-1.7B | <u>64.19</u> | <u>27.78</u> | <u>81.88</u> | **63.6** | 69.50 | <u>35.60</u> | 61.59 | <u>57.73</u> |
| Gemma3nE2b-it | 63.04 | 20.2 | **82.34** | 58.6 | **73.2** | 27.90 | <u>64.63</u> | 55.70 |
| Llama-3.2-3B-Instruct | 64.15 | 24.24 | 75.51 | 40 | <u>71.16</u> | 15.30 | 55.49 | 49.41 |
| Llama-3.2-1B-Instruct | 45.66 | 22.73 | 1.67 | 14.4 | 48.06 | 13.50 | 37.20 | 26.17 |

For the MMLU evaluation, we use a 0-shot CoT setting.

All models are evaluated in non-thinking mode.


## Speed
| Model                                         | Memory(GiB)         | i9 14900 | 1+13 8gen4 | rk3588 (16G) | rk3576 | Raspberry PI 5 | RDK X5 | rk3566 |
|-----------------------------------------------|---------------------|----------|------------|--------------|--------|----------------|--------|--------|
| SmallThinker 4B+sparse ffn +sparse lm_head    | 2.24                | 108.17   | 78.99      | 39.76        | 15.10  | 28.77          | 7.23   | 6.33   |
| SmallThinker 4B+sparse ffn +sparse lm_head+limited memory | limit 1G| 29.99    | 20.91      | 15.04        | 2.60   | 0.75           | 0.67   | 0.74   |
| Qwen3 0.6B                                    | 0.6                 | 148.56   | 94.91      | 45.93        | 15.29  | 27.44          | 13.32  | 9.76   |
| Qwen3 1.7B                                    | 1.3                 | 62.24    | 41.00      | 20.29        | 6.09   | 11.08          | 6.35   | 4.15   |
| Qwen3 1.7B+limited memory                     | limit 1G            | 2.66     | 1.09       | 1.00         | 0.47   | -              | -      | 0.11   |
| Gemma3n E2B                                   | 1G, theoretically   | 36.88    | 27.06      | 12.50        | 3.80   | 6.66           | 3.46   | 2.45   |

Note: i9 14900, 1+13 8ge4 use 4 threads, others use the number of threads that can achieve the maximum speed. All models here have been quantized to q4_0.

You can deploy SmallThinker with offloading support using [PowerInfer](https://github.com/SJTU-IPADS/PowerInfer/tree/main/smallthinker)

## Model Card

<div align="center">

| **Architecture** | Mixture-of-Experts (MoE) |
|:---:|:---:|
| **Total Parameters** | 4B |
| **Activated Parameters** | 0.6B |
| **Number of Layers** | 32 |
| **Attention Hidden Dimension** | 1536 |
| **MoE Hidden Dimension** (per Expert) | 768 |
| **Number of Attention Heads** | 12 |
| **Number of Experts** | 32 |
| **Selected Experts per Token** | 4 |
| **Vocabulary Size** | 151,936 |
| **Context Length** | 32K |
| **Attention Mechanism** | GQA |
| **Activation Function** | ReGLU |
</div>

## How to Run

### Transformers

`transformers==4.53.3` is required, we are actively working to support the latest version.
The following contains a code snippet illustrating how to use the model generate content based on given inputs.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

path = "PowerInfer/SmallThinker-4BA0.6B-Instruct"
device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(path, torch_dtype=torch.bfloat16, device_map=device, trust_remote_code=True)

messages = [
    {"role": "user", "content": "Give me a short introduction to large language model."},
]
model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(device)

model_outputs = model.generate(
    model_inputs,
    do_sample=True,
    max_new_tokens=1024
)

output_token_ids = [
    model_outputs[i][len(model_inputs[i]):] for i in range(len(model_inputs))
]

responses = tokenizer.batch_decode(output_token_ids, skip_special_tokens=True)[0]
print(responses)

```

### ModelScope

`ModelScope` adopts Python API similar to (though not entirely identical to) `Transformers`. For basic usage, simply modify the first line of the above code as follows:

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer
```
## Statement
- Due to the constraints of its model size and the limitations of its training data, its responses may contain factual inaccuracies, biases, or outdated information.
- Users bear full responsibility for independently evaluating and verifying the accuracy and appropriateness of all generated content.
- SmallThinker does not possess genuine comprehension or consciousness and cannot express personal opinions or value judgments.