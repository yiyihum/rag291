---
base_model:
- ServiceNow-AI/Apriel-5B-Base
library_name: transformers
language:
- en
license: mit
---

# Apriel-5B

`/ˈɑː.pri.əl/`

## Table of Contents

1. [Model Summary](#model-summary)  
2. [Evaluation](#evaluation)  
3. [Intended Use](#intended-use)  
4. [Limitations](#limitations)  
5. [Security and Responsible Use](#security-and-responsible-use)  
6. [License](#license)  
7. [Citation](#citation)

## Model Summary

Apriel is a family of models built for versatility, offering high throughput and efficiency across a wide range of tasks.  

### Apriel-5B-Base
Apriel-5B-base is a decoder-only transformer trained on 4.5T+ tokens of data. It is the first release in the Apriel model family, designed to support research on foundation models. Apriel-5B-base achieves strong performance across common benchmarks for models under 5B parameters.

### Apriel-5B-Instruct
[Apriel-5B-Instruct](https://huggingface.co/ServiceNow-AI/Apriel-5B-Instruct) is built on top of [Apriel-5B-base](https://huggingface.co/ServiceNow-AI/Apriel-5B-base) using continual pretraining (CPT), supervised finetuning (SFT), and post-training alignment with DPO and RLVR.

Both CPT and SFT stages involved training multiple domain-biased variants with overlapping datasets (e.g., instruction, code, math). These were then merged to form a more general-purpose model before alignment. The final model is aligned for instruction following, reasoning, and safety-aware dialogue.

<img src="https://huggingface.co/ServiceNow-AI/Apriel-4.8B-base/resolve/main/eval_vs_latency.png" alt="graph" width="400"/>

The y-axis shows average downstream benchmark scores. Throughput (x-axis) was measured using [vLLM](https://github.com/vllm-project/vllm) with batch size 8, 256 input tokens, and 32 output tokens.

### How to Use

```bash
pip install transformers
```

#### Running the Base model
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "ServiceNow-AI/Apriel-5B-Base"
device = "cuda"  # or "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16).to(device)

inputs = tokenizer.encode("Snow is", return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

```bash
>>> print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
Memory footprint: 9664.14 MB
```

#### Running the Instruct model

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "ServiceNow-AI/Apriel-5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    checkpoint, 
    torch_dtype=torch.bfloat16 if device == "cuda" else torch.float32
).to(device)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant that provides accurate and concise information."},
    {"role": "user", "content": "Tell me about artificial intelligence"}
]

input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(input_text, return_tensors="pt").to(device)

generation_params = {
    "max_new_tokens": 512,
    "temperature": 0.2,
    "top_p": 0.9,
    "do_sample": True
}

outputs = model.generate(**inputs, **generation_params)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Chat Template

```
<|system|>
System message here (optional)
<|end|>
<|user|>
User message here
<|end|>
<|assistant|>
Assistant response here
<|end|>
```

If no system message is provided, the model inserts a blank system prompt to maintain format structure. The model supports structured interaction patterns, including tool calling and reasoning steps for more advanced workflows.

## Evaluation

Evaluations were conducted using [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) and [evalchemy](https://github.com/mlfoundations/evalchemy).

### Apriel-5B-Base

| Task Name           | Apriel-5B-Base | OLMo-2-1124-7B | Llama-3.1-8B | Mistral-Nemo-Base-2407 |
|---------------------|------------------|----------------|--------------|-------------------------|
| **Average**         | 58.7             | 58.71          | 61.72        | 66.01                    |
| **ARC Challenge**   | 56.7             | 62.7           | 58.2         | 62.9                    |
| **ARC Easy**        | 82.4             | 86.0           | 85.7         | 86.7                    |
| **MMMLU**           | 44.5             | 35.3           | 47.4         | 54.7                    |
| **Global MMLU**     | 57.4             | 52.4           | 61.1         | 68.4                    |
| **GSM8k**           | 64.2             | 63.2           | 54.8         | 58.5                    |
| **HellaSwag**       | 74.4             | 80.5           | 78.8         | 82.7                    |
| **MUSR**            | 39.1             | 39.6           | 38.0         | 39.9                    |
| **MBPP**            | 27.6             | 22.4           | 46.0         | 54.6                    |
| **MMLU**            | 61.3             | 63.9           | 66.0         | 69.6                    |
| **PIQA**            | 78.9             | 81.1           | 81.2         | 82.1                    |



### Apriel-5B-Instruct

| Task Name    | Apriel-5B-Instruct | OLMo-2-1124-7B-Instruct | Llama-3.1-8B-Instruct | Mistral-Nemo-Instruct-2407 |
|--------------|--------------------|--------------------------|------------------------|----------------------------|
| **Average**      | 49.64             | 43.91                   | 	52.60                 | 	48.63                      |
| **ARC Challenge** | 59.04              | 61.45                   | 64.25                 | 66.38                      |
| **GSM8k**        | 80.36              | 79.68                   | 82.63                 | 77.63                      |
| **Hellaswag**    | 74.52              | 80.21                   | 78.43                 | 81.71                      |
| **BBH**          | 39.82              | 39.95                   | 50.86                 | 50.06                      |
| **GPQA**         | 28.36              | 27.85                   | 29.19                 | 29.45                      |
| **IF Eval**      | 80.78              | 72.64                   | 79.67                 | 62.85                      |
| **MMLU Pro**     | 29.19              | 26.57                   | 37.74                 | 35.09                      |
| **MUSR**         | 36.77              | 34.39                   | 38.36                 | 39.02                      |
| **MBPP**         | 45.80              | 28.00                   | 59.00                 | 57.60                      |
| **TruthfulQA**   | 56.09              | 56.46                   | 55.05                 | 57.69                      |
| **Winogrande**   | 62.35              | 65.35                   | 67.01                 | 70.01                      |
| **Minerva Math** | 39.80              | 9.96                    | 36.72                 | 21.46                      |
| **MATH500**      | 53.00              | 31.4                    | 45.80                 | 34.40                      |
| **AMC23**        | 29.00              | 16.4                    | 21.00                 | 11.50                      |
| **MixEval Hard** | 29.70              | 28.40                   | 43.30                 | 34.60                      |

## Intended Use

The Apriel family of models are designed for a variety of general-purpose instruction tasks, including:

- Question answering and information retrieval  
- Content generation and summarization  
- Code assistance and generation  
- Logical reasoning and multi-step tasks  
- Creative writing and ideation  

They are **not intended** for use in safety-critical applications without human oversight or in scenarios requiring guaranteed factual accuracy.

## Limitations

- **Factual accuracy:** May produce incorrect, misleading, or outdated content. Outputs should be verified before use in critical contexts.  
- **Bias:** May reflect societal, cultural, or systemic biases present in training data.  
- **Ethics:** Do not use the model to produce harmful, unlawful, or unethical content.  
- **Language:** Strongest performance is in English. Output quality may degrade in underrepresented languages.  
- **Critical use:** Not suitable for medical, legal, financial, or other high-risk applications without safeguards.

## Security and Responsible Use

**Security Responsibilities:**  
Deployers and users are strongly encouraged to align their security practices with established frameworks and regulatory guidelines such as the EU AI Act and the NIST AI Risk Management Framework (RMF).

**Guidelines for Deployers:**

- Regularly conduct robustness assessments to identify and mitigate adversarial inputs.
- Implement validation and filtering processes to prevent harmful or biased outputs.
- Continuously perform data privacy checks to guard against unintended data leaks.
- Document and communicate the model's limitations, intended usage, and known security risks to all end-users.
- Schedule periodic security reviews and updates to address emerging threats and vulnerabilities.

**Guidelines for Users:**

- Follow established security policies and usage guidelines provided by deployers.
- Protect and manage sensitive information when interacting with the model.
- Report anomalies, suspicious behavior, or unsafe outputs to deployers or developers.
- Maintain human oversight and apply judgment to mitigate potential security or ethical risks during interactions.

**Disclaimer:**  
Users accept responsibility for securely deploying, managing, and using this open-source LLM. The model is provided "as-is," without explicit or implied warranty regarding security or fitness for any specific application or environment.

## Pretraining

### Model

- **Architecture:** Transformer decoder with grouped-query attention and YARN rotary embeddings  
- **Tokens:** 4.5T  
- **Precision:** bfloat16  
- **Knowledge cutoff:** April 2024  

### Hardware

- **Compute:** 480 × H100 GPUs  
- **GPU-hours:** ~91,000 H100-hours  

### Software

- **Training stack:** [Fast-LLM](https://github.com/ServiceNow/Fast-LLM)

## License

MIT

## Citation

```bibtex
@misc{Apriel-small-language-models,  
    author = {Slam labs team},  
    title = {{Apriel - a Family of performant small language models}},  
    howpublished = {https://huggingface.co/ServiceNow-AI/Apriel-5B-Instruct},
    publisher = {SLAM - ServiceNow Language Models Lab}  
    year = {2025}
}
```
