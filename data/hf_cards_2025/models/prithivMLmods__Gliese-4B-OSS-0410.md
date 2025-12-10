---
license: apache-2.0
language:
- en
- zh
base_model:
- prithivMLmods/Kepler-Qwen3-4B-Super-Thinking
pipeline_tag: text-generation
library_name: transformers
tags:
- trl
- text-generation-inference
- thinking
- gpt_oss
- math
- code
- smoothing
- agent
---

![1](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/xwNz8R9cHHBArUKbTKs6U.png)

# **Gliese-4B-OSS-0410**

> **Gliese-4B-OSS-0410** is a reasoning-focused model fine-tuned on **Qwen-4B** for enhanced **reasoning** and **polished token probability distributions**, delivering balanced **multilingual generation** across mathematics and general-purpose reasoning tasks.
> The model is fine-tuned on curated **GPT-OSS synthetic dataset entries**, improving its ability to handle structured reasoning, probabilistic inference, and multilingual tasks with precision.

> [!note]
> GGUF: [https://huggingface.co/prithivMLmods/Gliese-4B-OSS-0410-GGUF](https://huggingface.co/prithivMLmods/Gliese-4B-OSS-0410-GGUF)

---

## Key Features

1. **Enhanced Reasoning Precision**
   Refined token probability distributions improve reasoning quality and ensure balanced, context-aware outputs.

2. **Event Simulation and Logical Analysis**
   Capable of modeling random events, probability-driven reasoning, and structured decision-making with strong logical consistency.

3. **Multilingual Mathematical and General-Purpose Problem Solving**
   Delivers robust performance in **mathematics**, **probability**, and **structured multilingual tasks**, enabling broad applicability in research and education.

4. **Hybrid Symbolic–Probabilistic Thinking**
   Combines structured logic, probabilistic inference, and reasoning fluency to improve performance on uncertainty-driven tasks.

5. **Structured Output Generation**
   Generates well-formatted outputs in **LaTeX**, **Markdown**, **JSON**, **CSV**, and **YAML**, supporting technical workflows and data-oriented research.

6. **Optimized Lightweight Footprint**
   With **4B parameters**, it runs efficiently on **mid-range GPUs**, **offline clusters**, and **edge devices** without compromising reasoning performance.

---

## Quickstart with Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prithivMLmods/Gliese-4B-OSS-0410"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Simulate the probability of rolling two dice and getting a sum greater than 9. Show the reasoning."

messages = [
    {"role": "system", "content": "You are a reasoning tutor skilled in probability, logic, and multilingual problem-solving."},
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
print(response)
```

---

## Intended Use

* Balanced multilingual reasoning and probability modeling
* Event simulation, uncertainty analysis, and structured problem solving
* Educational and research-focused reasoning tasks
* Deployment in mid-resource environments with efficient inference
* Structured technical content and data format generation

---

## Limitations

* Primarily focused on reasoning and mathematics; less suited for creative writing
* Despite its 4B size, extremely complex multi-hop reasoning tasks may remain challenging
* Prioritizes structured reasoning and probabilistic accuracy over conversational tone
* May produce inconsistent results with **very long contexts** or **cross-domain multi-document inputs**