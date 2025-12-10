---
license: mit
language:
- zh
- en
base_model:
- inclusionAI/Ling-lite
pipeline_tag: text-generation
library_name: transformers
---

# Ring-lite-distill-preview

<p align="center">
    <img src="https://huggingface.co/inclusionAI/Ring-lite-distill-preview/resolve/main/ant-bailing.png" width="100"/>
<p>

<p align="center">
          🤗 <a href="https://huggingface.co/inclusionAI">Hugging Face</a>
<p>

## Introduction

Ring-lite-distill-preview is an MoE LLM provided and open-sourced by InclusionAI, which has 16.8B parameters with 2.75B activated parameters. It was fine-tuned from [Ling-lite](https://modelscope.cn/models/inclusionAI/Ling-lite) using extensive reasoning-focused instruction data. This model delivers performance comparable to DeepSeek-R1-Distill-Qwen-7B on reasoning benchmarks while achieving better results on general benchmarks, especially superior performance on function-calling evaluation benchmarks (e.g., TEval, BFCl_v2) and instruction-following benchmarks (e.g., IFEval). This demonstrates that Ring-lite-distill is a more balanced and versatile model. Additionaly, it maintains competitive latency and throughput compared to other reasoning LLMs of similar size.

## Model Downloads

<div align="center">

|     **Model**      | **#Total Params** | **#Activated Params** | **Context Length** | **Download** |
| :----------------: | :---------------: | :-------------------: | :----------------: | :----------: |
| Ring-lite-distill-preview |       16.8B       |         2.75B         |        64K         |      [🤗 HuggingFace](https://huggingface.co/inclusionAI/Ring-lite-distill) |

</div>

## Evaluation
In order to fully evaluate the model's performance, we examined Ring-lite-distill-preview in terms of both reasoning ability and general ability.
### Reasoning ability

<div align="center">

|     **Model**      | **AIME24** | **MATH-500** | **GPQA-diamond** | **LiveCodeBench** |
| :----------------: | :---------------: | :-------------------: | :----------------: | :----------: |
| DeepSeek-R1-Distill-Qwen-7B (reported) |       55.5       |         92.8         |        49.1           |          37.6       |
| DeepSeek-R1-Distill-Qwen-7B (reproduce)  |       53.2       |         93.7         |        50.4         |         36.5       |
| Ring-lite-distill-preview |       56.3       |         93.7         |        46.2        |        31.9       |

</div>

### General ability

<div align="center">

|     **Model**      | **IFEval**  | **T-eval** | **BFCL_v2** | **MMLU** |
| :----------------: | :---------------: | :-------------------: | :----------------: | :----------: |
| DeepSeek-R1-Distill-Qwen-7B (reproduce)  |       39.3       |         26.9          | 38.9 | 44.1 |
| Ring-lite-distill-preview |      75.3 | 81.3 | 63.0 | 63.3 |

</div>

More details will be reported in our [technical report](https://github.com/inclusionAI/Ring/blob/main/Ring_Lite_Distill_Preview.pdf).

## Quickstart

### 🤗 Hugging Face Transformers
Here is a code snippet to show you how to use the chat model with `transformers`:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "inclusionAI/Ring-lite-distill-preview"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language models."
messages = [
    {"role": "system", "content": "You are Ring, an assistant created by inclusionAI"},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=8192
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Dataset
The training data of Ring-lite-distill-preview will be released soon. 

## Deployment
Please refer to [GitHub](https://github.com/inclusionAI/Ring/blob/main/README.md)

## License
This code repository is licensed under [the MIT License](https://huggingface.co/inclusionAI/Ring-lite-distill/blob/main/LICENSE).

## Citation
[TBD]