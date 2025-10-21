---
base_model: unsloth/Qwen3-1.7B
library_name: peft
license: mit
datasets:
- moremilk/CoT_Medical_Diagnosis
language:
- en
pipeline_tag: text-generation
tags:
- sft
- trl
- unsloth
- transformers
- medical
- clinical
---

# Model Card for Med-o1-1.7B

## Model Details

Med-o1-1.7B is fine-tuned specifically for medical diagnostic reasoning. Using the CoT_Medical_Diagnosis dataset, the model has learned to not only provide medical diagnoses but also to explain the step-by-step clinical reasoning that leads to its conclusions.

Key features of Med-o1-1.7B include:

- Chain-of-Thought (CoT) reasoning: Generates transparent and structured reasoning for diagnostic decisions.
- Clinical logic and evidence synthesis: Mimics human-style differential diagnosis and evaluates patient information systematically.
- Medical domain specialization: Focused entirely on clinical scenarios, from symptom analysis to medical history interpretation.
- Trust and explainability: Designed to build confidence in AI-driven medical assistance by clearly showing how conclusions are reached.

This model is ideal for researchers, educators, and developers aiming to study, demonstrate, or integrate AI-assisted medical reasoning.


## Uses

### Intended Use

- Educational purposes: Teaching clinical reasoning and differential diagnosis.
- Research applications: Exploring AI in medical decision support and diagnostic logic.
- Prototyping healthcare AI tools: Generating interpretable diagnostic reasoning.

⚠️ Important: This model is not intended for actual medical diagnosis or treatment decisions. Outputs should not be relied upon as a substitute for professional medical judgment. Always consult licensed healthcare professionals.


## Bias, Risks, and Limitations

- Not a substitute for professional medical advice or diagnosis
- Trained on a limited dataset (3000+ cases); performance may vary with novel or complex clinical scenarios

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel


tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-1.7B",)
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/Qwen3-1.7B",
    device_map={"": 0}
)

model = PeftModel.from_pretrained(base_model,"khazarai/Med-o1-1.7B")

question = """
Explain the physiological significance of a high hematocrit level, the common medical term used to describe this condition, and list three potential underlying causes.
"""

messages = [
    {"role" : "user", "content" : question}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True,
    enable_thinking = True,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 2048,
    temperature = 0.6,
    top_p = 0.95,
    top_k = 20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```
**For pipeline:** 

```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-1.7B")
base_model = AutoModelForCausalLM.from_pretrained("unsloth/Qwen3-1.7B")
model = PeftModel.from_pretrained(base_model, "khazarai/Med-o1-1.7B")

question = """
Explain the physiological significance of a high hematocrit level, the common medical term used to describe this condition, and list three potential underlying causes.
"""

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
messages = [
    {"role": "user", "content": question}
]
pipe(messages)
```


## Training Details

### Training Data

The model was fine-tuned on the [moremilk/CoT_Medical_Diagnosis](https://huggingface.co/datasets/moremilk/CoT_Medical_Diagnosis) dataset:

- Over 3007 detailed medical scenarios
- Each entry includes: patient symptoms, history, reasoning steps (CoT), and final diagnosis
- Scenarios cover a wide range of clinical cases, ensuring broad exposure to medical reasoning patterns

The dataset emphasizes transparent reasoning, helping the model learn to articulate logical steps for arriving at conclusions.



### Framework versions

- PEFT 0.15.2