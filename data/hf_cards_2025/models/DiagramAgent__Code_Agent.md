---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen2.5-Coder-7B
pipeline_tag: text-generation
tags:
- code
datasets:
- DiagramAgent/DiagramGenBenchmark
---

[📑paper link](https://arxiv.org/abs/2411.11916)



## Model Card: DiagramAgent/Code_Agent

### 1. Model Overview

-   **Name**: DiagramAgent/Code_Agent
-   **Description**:
     The Code_Agent is the core module responsible for converting processed user instructions—provided by the Plan Agent—into executable diagram-specific code. It supports both diagram generation and editing tasks by producing structured, logically coherent code that can be easily compiled into diagrams and further modified if needed.

### 2. Intended Use

-   Primary Tasks:
    -   Transform complete textual instructions into diagram code.
    -   Modify existing diagram code based on user-provided editing commands.
    -   Work in tandem with the Check Agent to ensure the generated code is syntactically correct and logically sound.
-   Application Scenarios:
    -   Automated generation of structured diagrams (e.g., flowcharts, model architecture diagrams, mind maps).
    -   Rapid prototyping and iterative editing of visual representations.
    -   Research, education, and industrial applications requiring precise and modifiable diagram construction.

### 3. Architecture and Training Details

-   **Base Model**: Built upon the Qwen2.5-Coder-7B model.
-   Training Process:
    -   Fine-tuned on the DiagramGenBenchmark dataset, which covers a variety of diagram types.
    -   Trained for 4 epochs with a maximum input length of 8192 tokens.
    -   The training objective is to minimize the discrepancy between the generated code and reference code using a tailored loss function.
-   **Module Interaction**:
     Collaborates closely with the Plan Agent (for interpreting instructions) and the Check Agent (for debugging and verification) to complete both diagram generation and editing workflows.


### 4.Usage Examples

```py
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "DiagramAgent/Code_Agent"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "user", "content": "your input"}
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

### 5. Citation

If you find our work helpful, feel free to give us a cite.


```
@inproceedings{wei2024wordsstructuredvisualsbenchmark,
  title={From Words to Structured Visuals: A Benchmark and Framework for Text-to-Diagram Generation and Editing},
  author={Jingxuan Wei and Cheng Tan and Qi Chen and Gaowei Wu and Siyuan Li and Zhangyang Gao and Linzhuang Sun and Bihui Yu and Ruifeng Guo},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year={2025}
}
```