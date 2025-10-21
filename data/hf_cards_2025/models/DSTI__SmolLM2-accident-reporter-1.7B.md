---
base_model: unsloth/SmolLM2-1.7B-Instruct
library_name: peft
license: apache-2.0
datasets:
- DSTI/traffic-accidents-reports-kd-smollm2-360M-7k
language:
- en
pipeline_tag: text-generation
tags:
- sft
- trl
- unsloth
- transformers
---

# DSTI/SmolLM2-accident-reporter-1.7B · Accident Reporter


## Model Details

SmolLM2-accident-reporter-1.7B is a LoRA fine-tuned variant of SmolLM2-1.7B-Instruct, trained for knowledge-distilled accident reporting.
The model generates concise, neutral one-paragraph traffic accident/incident reports from structured facts. Each output is designed to cover the key aspects of an event: What, When, Where, Who, How, Why, and Contingency Actions.
This model is intended for tasks in structured event-to-text generation, summarization of incidents, and training student models with KD signals.

### Model Description

- **Base Model:** unsloth/SmolLM2-1.7B-Instruct
- **Language(s) (NLP):** English
- **License:** apache-2.0
- **Dataset:**  [DSTI/traffic-accidents-reports-kd-smollm2-360M-7k](https://huggingface.co/datasets/DSTI/traffic-accidents-reports-kd-smollm2-360M-7k)


## Uses

### Direct Use

- Automatic generation of one-paragraph traffic accident reports.
- Knowledge distillation research for event-to-text tasks.
- Supporting structured-to-freeform NLP generation benchmarks.

## Bias, Risks, and Limitations

- The model follows a neutral reporting tone, but may omit minor details not emphasized in training.
- Not suitable for real-time or legal use cases without human verification.
- Performance is limited to traffic/incident report style and may not generalize to unrelated domains.

## How to Get Started with the Model

Use the code below to get started with the model.

```python 
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


tokenizer = AutoTokenizer.from_pretrained("unsloth/SmolLM2-1.7B-Instruct",)
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/unsloth/SmolLM2-1.7B-Instruct",
    device_map={"": 0}
)

model = PeftModel.from_pretrained(base_model,"DSTI/SmolLM2-accident-reporter-1.7B")


question ="""
What: Minor collision between Vehicle A (compact car) and Vehicle B (minivan) in parking lot
When: Occurrence: December 9, 2025, 13:00; Discovery: December 9, 2025, 13:01
Where: Shopping center parking lot, Lot B
Who: Ms. Karen Liu – compact car driver (Vehicle A), Mr. Thomas Barnes – minivan driver (Vehicle B)
How: Vehicle A misjudged turning space and touched Vehicle B
Why: Driver inattention during parking maneuver
ContingencyActions: Drivers exchanged info, no injuries reported, security cameras documented accident
"""

messages = [
    {"role" : "user", "content" : question}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, 
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 512,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```
**For pipeline:** 

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("unsloth/SmolLM2-1.7B-Instruct")
base_model = AutoModelForCausalLM.from_pretrained("unsloth/SmolLM2-1.7B-Instruct")

model = PeftModel.from_pretrained(base_model, "DSTI/SmolLM2-accident-reporter-1.7B")

question ="""
What: Minor collision between Vehicle A (compact car) and Vehicle B (minivan) in parking lot
When: Occurrence: December 9, 2025, 13:00; Discovery: December 9, 2025, 13:01
Where: Shopping center parking lot, Lot B
Who: Ms. Karen Liu – compact car driver (Vehicle A), Mr. Thomas Barnes – minivan driver (Vehicle B)
How: Vehicle A misjudged turning space and touched Vehicle B
Why: Driver inattention during parking maneuver
ContingencyActions: Drivers exchanged info, no injuries reported, security cameras documented accident
"""

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
messages = [
    {"role": "user", "content": question}
]
pipe(messages)
```

## Training Details

### Accident Reporting KD Dataset (One-Paragraph)

The model was fine-tuned on the Accident Reporting KD Dataset, which consists of:

- Gold human-written targets from zBotta/traffic-accidents-reports-5k
- Teacher-generated reports from zBotta/smollm2-accident-reporter-360m, providing soft targets for knowledge distillation (KD).

Dataset size: ~6K samples.

Language: English.

## Result 

- Training Loss: 2.43 >> 0.70
- Eval Loss: 2.41 >> 0.71

## Citation 

If you use this model, please cite:

The source dataset: DSTI/traffic-accidents-reports-kd-smollm2-360M-7k

```csharp
@misc{SmolLM2-accident-reporter-1.7B,
  title  = {Accident Reporting model (One-Paragraph)},
  author = {Rustam Shiriyev},
  year   = {2025}
}
```

### Framework versions

- PEFT 0.15.2