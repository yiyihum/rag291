---
license: apache-2.0
datasets:
- nvidia/OpenCodeReasoning
- nvidia/OpenMathReasoning
- prithivMLmods/Helios-R-6M
language:
- en
base_model:
- Qwen/Qwen3-4B-Thinking-2507
pipeline_tag: text-generation
tags:
- trl
- math
- text-generation-inference
- code
library_name: transformers
---

![1](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/IObi572uIr3vg89VuZD5x.png)

# **Logics-Qwen3-Math-4B**

> **Logics-Qwen3-Math-4B** is a reasoning-focused model fine-tuned on **Qwen3-4B-Thinking-2507** for **mathematical reasoning** and **logical coding**, trained on **OpenMathReasoning**, **OpenCodeReasoning**, and **Helios-R-6M** datasets. It excels in structured **mathematical problem solving**, **algorithmic logic**, and **probabilistic reasoning**, making it ideal for educators, researchers, and developers focused on computational logic and math.

## **Key Features**

1. **Mathematical & Logical Reasoning**
   Fine-tuned for high-precision math reasoning, algorithmic problem-solving, and logical coding tasks.

2. **Event-Driven & Probabilistic Modeling**
   Performs probability-based simulations, structured decision-making, and multi-step logical reasoning with strong accuracy.

3. **Multilingual Problem Solving**
   Supports math and logic tasks across multiple languages, suitable for global research and education workflows.

4. **Hybrid Symbolic-Algorithmic Thinking**
   Combines structured logic, symbolic computation, and probabilistic inference to handle uncertainty-driven problems efficiently.

5. **Structured Output Mastery**
   Generates outputs in **LaTeX**, **Markdown**, **JSON**, **CSV**, and **YAML**, enabling smooth integration into technical and research workflows.

6. **Optimized 4B Parameter Footprint**
   Deployable on **mid-range GPUs**, **offline clusters**, and **edge devices**, maintaining high reasoning quality while being resource-efficient.

## **Quickstart with Transformers**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "prithivMLmods/Logics-Qwen3-Math-4B"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Solve the equation x^2 - 5x + 6 = 0 and show all reasoning steps."

messages = [
    {"role": "system", "content": "You are a math and logic tutor skilled in algebra, probability, and structured programming reasoning."},
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

## **Intended Use**

* High-precision mathematical reasoning and problem-solving
* Algorithmic logic, structured coding tasks, and probability analysis
* Educational and research-focused workflows
* Deployment on mid-resource environments with efficient reasoning
* Structured data and technical content generation

## **Limitations**

* Focused on math and logic—less suited for creative writing or casual conversation
* Very complex multi-hop reasoning may challenge the 4B parameter capacity
* Prioritizes structured reasoning over conversational tone
* Outputs may be inconsistent for extremely long or cross-domain multi-document contexts