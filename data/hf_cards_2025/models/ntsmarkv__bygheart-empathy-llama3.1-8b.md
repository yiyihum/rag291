---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- empathy
- emotional-support
- mental-health
- fine-tuned
- llama3.1
- bygheart
- peft
- lora
language:
- en
pipeline_tag: text-generation
---

# 🦥💝 BygHeart Empathy Model - Llama 3.1 8B

**Achieved 4.54/5 empathy score - exceeding production targets!**

## Model Description

This is a fine-tuned version of Llama 3.1 8B Instruct, specifically optimized for empathetic conversations and emotional support. The model has been trained using the BygHeart empathy framework across 5 key dimensions:

- **Recognition** (5/5): Identifying and acknowledging emotions
- **Validation** (4/5): Legitimizing feelings and experiences  
- **Coherence** (3/5): Logical, relevant, well-structured responses
- **Personalization** (5/5): Tailoring responses to individual context
- **Support** (5/5): Providing emotional assistance and guidance

## Performance

- **Overall Empathy Score**: 4.54/5 🎯
- **Baseline**: 2.8/5
- **Improvement**: +62% over baseline
- **Target Achievement**: ✅ Exceeded 4.0/5 goal

## Usage

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

# Load BygHeart empathy adapter
model = PeftModel.from_pretrained(base_model, "ntsmarkv/bygheart-empathy-llama3.1-8b")

# Generate empathetic response
prompt = '''<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are BygHeart, an empathetic AI specialized in providing emotional support.<|eot_id|><|start_header_id|>user<|end_header_id|>

I'm feeling overwhelmed with work stress.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

'''

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

## Training Details

- **Base Model**: meta-llama/Llama-3.1-8B-Instruct
- **Training Method**: LoRA (Low-Rank Adaptation)
- **Training Data**: BygHeart empathy dataset
- **Training Time**: ~12 minutes on Tesla T4
- **Memory Usage**: ~7GB peak

## Intended Use

This model is designed for:
- Emotional support chatbots
- Mental health applications
- Customer service with empathy
- Educational tools for empathy training
- Research in computational empathy

## Limitations

- Responses are generated based on training data patterns
- Not a replacement for professional mental health services
- May occasionally generate inconsistent responses
- Requires careful monitoring in production use

## Citation

```bibtex
@model{bygheart-empathy-llama3.1-8b,
  title={BygHeart Empathy Model - Llama 3.1 8B},
  author={BygHeart Team},
  year={2024},
  url={https://huggingface.co/ntsmarkv/bygheart-empathy-llama3.1-8b}
}
```

## License

This model is based on Llama 3.1 and follows the same license terms.
