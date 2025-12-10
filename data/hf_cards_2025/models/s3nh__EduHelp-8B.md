---
license: mit
language:
- en
base_model:
- Qwen/Qwen3-8B
library_name: transformers
tags:
- writing
- creative-writing
---
# EduHelper

EduHelper is a child-friendly tutoring assistant fine-tuned from the Qwen3-8B base model using parameter-efficient fine-tuning (PEFT) with LoRA on the [ajibawa-2023/Education-Young-Children](https://huggingface.co/datasets/ajibawa-2023/Education-Young-Children) dataset.

---

## TL;DR

- Base model: Qwen3-8B
- Method: PEFT (LoRA), adapters merged into the final weights
- Training data: [Education-Young-Children](https://huggingface.co/datasets/ajibawa-2023/Education-Young-Children)
- Intended use: Gentle, age-appropriate explanations and basic tutoring for young learners
- Language: Primarily English
- Safety: Requires adult supervision; not a substitute for professional advice

---

## Model Details

- Architecture: Decoder-only LLM (chat/instruction style), based on Qwen3-8B
- Training approach: Supervised fine-tuning with LoRA (via PEFT), adapters merged into the base model for standalone deployment
- Focus: Clear, simple, supportive answers for early-learning contexts (e.g., basic reading, counting, everyday knowledge)

Please refer to the Qwen3-8B base model card for detailed architecture and licensing.

---

## Intended Use and Limitations

- Suitable for:
  - Simple explanations and step-by-step guidance
  - Basic arithmetic and counting practice
  - Short reading comprehension and vocabulary support
  - Everyday factual knowledge for children

- Not suitable for:
  - Medical, legal, or emergency advice
  - Unsupervised use by children
  - High-stakes or specialized professional tasks

The model can make mistakes or produce content that may not be perfectly age-appropriate. Always supervise and review outputs.

---

## Training Data

- Dataset: [ajibawa-2023/Education-Young-Children](https://huggingface.co/datasets/ajibawa-2023/Education-Young-Children)
- Description: Educational prompts and responses oriented toward young children
- Notes: Review the dataset card for curation details and license. Ensure compliance when redistributing or deploying.

---

## How to Use 


```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "s3nh/EduHelper_Qwen3_8B_6500steps"

tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

messages = [
    {"role": "system", "content": "You are a kind and patient tutor for young children. Use simple words and a friendly tone."},
    {"role": "user", "content": "Can you explain what a verb is with two examples?"}
]

inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=200,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Tips:
- For more focused answers, try `temperature=0.2–0.5`.
- Add a clear system prompt to reinforce gentle, age-appropriate behavior.

---

## Safety and Responsible Use

- Supervision: Children should use this model under adult supervision.
- Content filtering: Consider additional filtering or guardrails to ensure age-appropriate outputs.
- Biases: The model may reflect biases present in training data. Review outputs in your application context.
---

## Limitations

- Knowledge breadth and factuality are bounded by the base model and dataset.
- Not optimized for advanced reasoning or specialized domains.
- May occasionally produce overly complex or off-topic responses.

---

## Citation

If you use EduHelper, please cite the model and its components:

- The Qwen3-8B base model (per its model card)
- The ajibawa-2023/Education-Young-Children dataset

---

## Acknowledgements

- Base model: Qwen3-8B by the Qwen team
- Dataset: [ajibawa-2023/Education-Young-Children](https://huggingface.co/datasets/ajibawa-2023/Education-Young-Children)


## Credits

Thanks for lium.io for generous grant
Thanks for basilica.ai for access to hardware
