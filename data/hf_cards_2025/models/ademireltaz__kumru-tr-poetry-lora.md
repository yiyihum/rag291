---
base_model: vngrs-ai/Kumru-2B-Base
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:vngrs-ai/Kumru-2B-Base
- lora
- transformers
- text-generation
- finetuned
- poetry
- turkish
---

# Model Card for ademireltaz/kumru-tr-poetry-lora

This is a **PEFT (Parameter-Efficient Fine-Tuning) adapter** for the **vngrs-ai/Kumru-2B-Base** model, fine-tuned using the **LoRA** (Low-Rank Adaptation) method for **Turkish poetry generation**.

---

## Model Details

### Model Description

This model is a LoRA adapter created by fine-tuning the base **Kumru-2B-Base** model. It uses the PEFT library and the LoRA method to efficiently update the model weights, specializing it for generating text that mimics the structure and style of Turkish poetry. This adapter must be loaded on top of the original `vngrs-ai/Kumru-2B-Base` model to enable its poetry generation capabilities.

- **Developed by:** **Ahmet Demirel**
- **Funded by :** **Taz Technology**
- **Shared by :** **Ahmet Demirel**
- **Model type:** **PEFT Adapter (LoRA)**
- **Language(s) (NLP):** **Turkish**
- **License:** **MIT License**
- **Finetuned from model :** **vngrs-ai/Kumru-2B-Base**

### Model Sources 

- **Repository:** **https://huggingface.co/ademireltaz/kumru-tr-poetry-lora**
- **Demo [optional]:** [More Information Needed] (Hugging Face Space address to be added later)
- **Organization Website:** **https://taztech.tr**

---

## Uses

### Direct Use

This model is intended to be used as a LoRA adapter loaded onto the base `vngrs-ai/Kumru-2B-Base` model to generate **Turkish poetry** based on given prompts or themes.

### Downstream Use 

This adapter can be used in creative writing tools, educational applications focused on Turkish literature, or as a component in a larger content generation system.

### Out-of-Scope Use

Using the model for generating harmful, illegal, or biased content is strictly out of scope. It is also not suitable for tasks requiring high numerical precision or factual recall outside of its specialized domain.

---

## Bias, Risks, and Limitations

The model inherits the **biases and risks** present in the base model (`vngrs-ai/Kumru-2B-Base`) and may also introduce stylistic biases based on the poetry dataset it was fine-tuned on. Limitations include potential hallucinations, factual errors, and the inability to perfectly replicate complex poetic techniques or specific authors' styles.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. **Thorough testing and human review** of the generated output are strongly recommended, especially if the output is used in a public or professional context.

---

## How to Get Started with the Model

Use the code below to load the LoRA adapter and the base model for inference.

## 📝 Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

base_model = "vngrs-ai/Kumru-2B-Base"
adapter_path = "KULLANICI_ADIN/kumru-poetry-lora"  # 👈 Buraya kendi repo adını yaz

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.float16,
    device_map="auto"
)
model = PeftModel.from_pretrained(model, adapter_path)

prompt = "Görev: Nazım Hikmet tarzında, deniz üzerine bir şiir yaz.\nYanıt:"
inputs = tokenizer(prompt, return_tensors="pt", return_token_type_ids=False)

outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.85,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```