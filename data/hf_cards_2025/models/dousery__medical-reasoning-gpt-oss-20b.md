---
language:
- en
license: apache-2.0
base_model: unsloth/gpt-oss-20b
tags:
- medical
- reasoning
- healthcare
- fine-tuned
- gpt-oss
- clinical
- diagnosis
- unsloth
datasets:
- Freedomintelligence/medical-o1-reasoning-SFT
pipeline_tag: text-generation
library_name: transformers
widget:
- text: A patient presents with fever of 39°C, severe headache, and neck stiffness.
    What could be the possible diagnosis?
  example_title: Medical Diagnosis
- text: Explain the pathophysiology of myocardial infarction and its treatment options.
  example_title: Medical Education
- text: A 45-year-old patient with chest pain and shortness of breath. Analyze the
    differential diagnosis.
  example_title: Clinical Reasoning
model-index:
- name: medical-reasoning-gpt-oss-20b
  results:
  - task:
      type: text-generation
      name: Medical Text Generation
    dataset:
      type: medical-reasoning
      name: Medical O1 Reasoning SFT
    metrics:
    - type: perplexity
      name: Training Loss
      value: 0.88
---

# Medical Reasoning GPT-OSS-20B

## Model Description

This is a fine-tuned version of [unsloth/gpt-oss-20b](https://huggingface.co/unsloth/gpt-oss-20b) specifically optimized for medical reasoning and clinical decision-making. The model has been trained on high-quality medical reasoning datasets to provide accurate and thoughtful responses to medical queries.

## 🏥 Key Features

- **Medical Expertise**: Specialized in medical reasoning, diagnosis, and clinical decision-making
- **Complex Reasoning**: Uses chain-of-thought reasoning for medical problems
- **Safety-Focused**: Trained with responsible AI practices for healthcare applications
- **Large Scale**: 20B parameters for comprehensive medical knowledge
- **Ready-to-Use**: Full model (not just LoRA adapter) - no additional setup required

## 🚀 Quick Start

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

model_id = "dousery/medical-reasoning-gpt-oss-20b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto"
)

prompt = "A patient has symptoms of fever and cough. What could be the diagnosis?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    do_sample=True,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.eos_token_id
)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
```

## 📊 Training Details

### Training Data
- **Dataset**: [Freedomintelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/Freedomintelligence/medical-o1-reasoning-SFT)
- **Language**: English
- **Size**: 19,704 medical reasoning examples
- **Format**: Question-Answer pairs with complex chain-of-thought reasoning

### Training Configuration
- **Base Model**: unsloth/gpt-oss-20b (20B parameters)
- **Training Method**: LoRA (Low-Rank Adaptation) fine-tuning
- **LoRA Rank**: 8
- **Learning Rate**: 2e-4
- **Batch Size**: 4 (effective)
- **Epochs**: 1
- **Hardware**: NVIDIA B200 (4x GPUs)
- **Framework**: Unsloth + TRL
- **Final Training Loss**: 0.88

### Model Architecture
- **Parameters**: 20.9 billion
- **Architecture**: GPT-OSS (Transformer-based)
- **Context Length**: 1,024 tokens
- **Trainable Parameters**: 3.98M (0.02% of total)

## 🎯 Intended Use

### Primary Use Cases
- **Medical Education**: Explaining medical concepts and procedures
- **Clinical Reasoning**: Analyzing symptoms and differential diagnosis
- **Research Support**: Assisting in medical research and literature review
- **Decision Support**: Providing reasoning for clinical decisions (with human oversight)


## ⚠️ Important Disclaimers

- **Not a Medical Device**: This model is for educational and research purposes only
- **Human Oversight Required**: All medical decisions should involve qualified healthcare professionals
- **Accuracy Not Guaranteed**: Model outputs should be verified against current medical literature
- **Regional Variations**: Training data may not reflect all regional medical practices

## 🔍 Evaluation

The model demonstrates strong performance in:
- Medical concept explanation
- Differential diagnosis reasoning
- Treatment option analysis
- Pathophysiology understanding

**Note**: Comprehensive clinical evaluation is ongoing. Always validate outputs with current medical guidelines.

## 📈 Performance Metrics

- **Training Loss**: 10.78 → 0.88 (significant improvement)
- **Convergence**: Stable training with consistent loss reduction
- **Reasoning Quality**: Maintains logical chain-of-thought structure

## 🛠️ Technical Requirements

### Minimum Requirements
- **GPU Memory**: 16GB+ VRAM recommended
- **RAM**: 32GB+ system memory
- **Storage**: 40GB+ free space

### Optimized for
- **Inference**: FP16/BF16 precision
- **Frameworks**: Transformers, Unsloth, TRL
- **Hardware**: NVIDIA GPUs with Compute Capability 7.0+

## 📜 License

This model is released under the Apache 2.0 license. Please review the license terms before commercial use.

## 🙏 Acknowledgments

- **Base Model**: [unsloth/gpt-oss-20b](https://huggingface.co/unsloth/gpt-oss-20b)
- **Training Framework**: [Unsloth](https://github.com/unslothai/unsloth)
- **Dataset**: [Freedomintelligence](https://huggingface.co/Freedomintelligence)
- **Infrastructure**: Modal Labs for GPU compute

## 📞 Contact

For questions, issues, or collaboration opportunities, please reach out through the HuggingFace community discussions or my Linkedin account : 
[Linkedin](https://www.linkedin.com/in/doguser-yarar)
