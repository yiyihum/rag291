---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.3
tags:
- nutrition
- health
- fine-tuned
- mistral
- dietary-advice
- meal-planning
language:
- en
pipeline_tag: text-generation
---

# Mistral-7B Nutritionist

A fine-tuned version of Mistral-7B-Instruct-v0.3 specialized for nutrition and dietary advice.

## Model Description

This model has been fine-tuned specifically for providing nutritional guidance, meal planning, and dietary recommendations. It's trained to give helpful, accurate advice about food choices, meal preparation, and nutritional needs.

## Usage

### Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained("RaghavM12/mistral-7b-nutritionist")
tokenizer = AutoTokenizer.from_pretrained("RaghavM12/mistral-7b-nutritionist")

prompt = "<s>[INST] What should I eat for breakfast to build muscle? [/INST]"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=150, temperature=0.7)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response.split("[/INST]")[-1].strip())
```

### For LM Studio

1. Open LM Studio
2. Go to "Search" tab
3. Search for "RaghavM12/mistral-7b-nutritionist"
4. Download and use!

## Training Details

- **Base Model**: mistralai/Mistral-7B-Instruct-v0.3
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Training Data**: Custom nutrition dataset
- **Specialization**: Nutrition advice, meal planning, dietary recommendations

## Capabilities

- Meal planning for specific goals (muscle building, weight loss, etc.)
- Nutritional advice for different dietary preferences
- Food recommendations and cooking suggestions
- Macro and micronutrient guidance

## Example Queries

- "What should I eat for breakfast to build muscle?"
- "Plan a healthy meal for weight loss"
- "What are good protein sources for vegetarians?"
- "How can I meal prep for the week?"

## License

Apache 2.0

## Disclaimer

This model provides general nutritional information and should not replace professional medical or dietary advice. Always consult with healthcare professionals for personalized nutrition plans.
