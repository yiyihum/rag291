---
license: apache-2.0
language:
- en
base_model:
- mistralai/Mistral-Small-3.2-24B-Instruct-2506
pipeline_tag: text-generation
library_name: transformers
tags:
- code
- mistral3
- mistral-common
- quantum
- qiskit
- Mistral-Small-3.2-24B-Qiskit
---


# Mistral-Small-3.2-24B-Qiskit

## Introduction

Mistral-Small-3.2-24B-Qiskit is a model specialized in Qiskit coding and based on the Mistral-Small-3.2-24B-Instruct-2506 model. With 24 billion parameters, this model achieves top-tier capabilities in both text and vision tasks. Using Qiskit code and instruction tuning data, we improve it's capabilities at writing high-quality and non-deprecated Qiskit code. We used only data with the following licenses: Apache 2.0, MIT, the Unlicense, Mulan PSL Version 2, BSD-2, BSD-3, and Creative Commons Attribution 4.0.


Main features compared to previous models specialized on Qiskit code:

- Significant improvements in **code generation** and **understanding** of the latest Qiskit versions.
- **Long-context Support** up to 128K tokens.


## Requirements

Mistral-Small-3.2-24B-Qiskit is compatible with the latest HuggingFace `transformers` and we advise you to use the latest version of `transformers`.


## Quickstart

Here we provide a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate content.

```python
from transformers import Mistral3ForConditionalGeneration, AutoTokenizer

model_name = "Qiskit/mistral-small-3.2-24b-qiskit"

model = Mistral3ForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Generate a random quantum circuit with 5 qubits."
messages = [
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
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```


## Training Data

- **Data Collection and Filtering:** Our code data is sourced from a combination of publicly available datasets (e.g., Code available on <https://github.com>), and additional synthetic data generated at IBM Quantum. We exclude code that is older than 2023.
- **Exact and Fuzzy Deduplication:** We use both exact and fuzzy deduplication to remove documents having (near) identical code content.
- **PII:** We redact Personally Identifiable Information (PII) in our datasets by replacing PII content (e.g., names, email addresses, keys, passwords) with corresponding tokens (e.g., ⟨NAME⟩, ⟨EMAIL⟩, ⟨KEY⟩, ⟨PASSWORD⟩).

## Infrastructure

We train Mistral-Small-3.2-24B-Qiskit using IBM's super computing cluster (Vela) using NVIDIA A100 GPUs. The cluster provides a scalable and efficient infrastructure for training.

## Ethical Considerations and Limitations

The use of Large Language Models involves risks and ethical considerations people must be aware of. Regarding code generation, caution is urged against complete reliance on specific code models for crucial decisions or impactful information as the generated code is not guaranteed to work as intended. **Mistral-Small-3.2-24B-Qiskit** model is not the exception in this regard. Even though this model is suited for multiple code-related tasks, it has not undergone any safety alignment, there it may produce problematic outputs. Additionally, it remains uncertain whether smaller models might exhibit increased susceptibility to hallucination in generation scenarios by copying source code verbatim from the training dataset due to their reduced sizes and memorization capacities. This aspect is currently an active area of research, and we anticipate more rigorous exploration, comprehension, and mitigations in this domain. Regarding ethics, a latent risk associated with all Large Language Models is their malicious utilization. We urge the community to use **Mistral-Small-3.2-24B-Qiskit** model with ethical intentions and in a responsible way.