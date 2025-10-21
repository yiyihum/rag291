---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
base_model:
- PowerInfer/SmallThinker-21BA3B-Instruct
---
## SmallThinker-21BA3B-Instruct-GGUF

- GGUF models with `.gguf` suffix can used with [*llama.cpp*](https://github.com/ggml-org/llama.cpp) framework.

- GGUF models with `.powerinfer.gguf` suffix are integrated with fused sparse FFN operators and sparse LM head operators. These models are only compatible to [*powerinfer*](https://github.com/SJTU-IPADS/PowerInfer/tree/main/smallthinker) framework.

## Introduction

<p align="center">
       &nbsp&nbsp🤗 <a href="https://huggingface.co/PowerInfer">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/PowerInfer">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://github.com/SJTU-IPADS/SmallThinker/blob/main/smallthinker-technical-report.pdf">Technical Report</a> &nbsp&nbsp 
</p>

SmallThinker is a family of **on-device native** Mixture-of-Experts (MoE) language models specially designed for local deployment,
co-developed by the **IPADS** and **School of AI at Shanghai Jiao Tong University** and **Zenergize AI**.
Designed from the ground up for resource-constrained environments,
SmallThinker brings powerful, private, and low-latency AI directly to your personal devices,
without relying on the cloud.



## Performance

Note: The model is trained mainly on English.

| Model                        | MMLU  | GPQA-diamond | MATH-500 | IFEVAL | LIVEBENCH | HUMANEVAL | Average |
|------------------------------|-------|--------------|----------|--------|-----------|-----------|---------|
| **SmallThinker-21BA3B-Instruct** | 84.43 | <u>55.05</u> | 82.4     | **85.77** | **60.3**      | <u>89.63</u>     | **76.26**   |
| Gemma3-12b-it                | 78.52 | 34.85        | 82.4     | 74.68  | 44.5      | 82.93     | 66.31   |
| Qwen3-14B                    | <u>84.82</u> | 50 | **84.6** | <u>85.21</u>| <u>59.5</u> | 88.41     | <u>75.42</u>   |
| Qwen3-30BA3B                 | **85.1**  | 44.4     | <u>84.4</u> | 84.29  | 58.8      | **90.24**     | 74.54   |
| Qwen3-8B                     | 81.79 | 38.89        | 81.6     | 83.92  | 49.5      | 85.9      | 70.26   |
| Phi-4-14B                    | 84.58 | **55.45**    | 80.2     | 63.22  | 42.4      | 87.2      | 68.84   |

For the MMLU evaluation, we use a 0-shot CoT setting.

All models are evaluated in non-thinking mode.

## Speed
| Model                               | Memory(GiB)         | i9 14900 | 1+13 8ge4 | rk3588 (16G) | Raspberry PI 5 |
|--------------------------------------|---------------------|----------|-----------|--------------|----------------|
| SmallThinker 21B+sparse              | 11.47               | 30.19    | 23.03     | 10.84        | 6.61           |
| SmallThinker 21B+sparse+limited memory | limit 8G         | 20.30    | 15.50     | 8.56         | -              |
| Qwen3 30B A3B                        | 16.20               | 33.52    | 20.18     | 9.07         | -              |
| Qwen3 30B A3B+limited memory          | limit 8G            | 10.11    | 0.18      | 6.32         | -              |
| Gemma 3n E2B                         | 1G, theoretically   | 36.88    | 27.06     | 12.50        | 6.66           |
| Gemma 3n E4B                         | 2G, theoretically   | 21.93    | 16.58     | 7.37         | 4.01           |

Note: i9 14900, 1+13 8ge4 use 4 threads, others use the number of threads that can achieve the maximum speed. All models here have been quantized to q4_0.
You can deploy SmallThinker with offloading support using [PowerInfer](https://github.com/SJTU-IPADS/PowerInfer/tree/main/smallthinker)

## Model Card

<div align="center">

| **Architecture** | Mixture-of-Experts (MoE) |
|:---:|:---:|
| **Total Parameters** | 21B |
| **Activated Parameters** | 3B |
| **Number of Layers** | 52 |
| **Attention Hidden Dimension** | 2560 |
| **MoE Hidden Dimension** (per Expert) | 768 |
| **Number of Attention Heads** | 28 |
| **Number of KV Heads** | 4 |
| **Number of Experts** | 64 |
| **Selected Experts per Token** | 6 |
| **Vocabulary Size** | 151,936 |
| **Context Length** | 16K |
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

path = "PowerInfer/SmallThinker-21BA3B-Instruct"
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