---
license: apache-2.0
base_model: ContactDoctor/Bio-Medical-Llama-3-2-1B-CoT-012025
tags:
- medical
- llama
- biomedical
- finetuned
- reasoning
- lora
pipeline_tag: text-generation
language:
- en
---

<p align="center">
  <img src="https://huggingface.co/front/assets/huggingface_logo.svg" width="200" alt="Hugging Face Logo"/>
</p>

<h1 align="center">🧠 BioLLama LLM Adapters</h1>
<h3 align="center">Fine tuned medical reasoning adapters for Llama 3 based biomedical systems</h3>
<p align="center">
  <b>Developed by <a href="https://huggingface.co/calender">calender</a></b>  
  <br>
  <a href="https://github.com/jikaan/BioLLama-LLM">🌐 View source on GitHub</a>
</p>

---

### 🌿 Overview

BioLLama LLM Adapters are specialized lightweight components built for enhancing **clinical reasoning**, **diagnostic interpretation**, and **medical chain of thought**.  
These adapters extend the base model **ContactDoctor Bio Medical Llama 3 2 1B CoT 012025** using **LoRA** for focused supervised fine tuning on medical question answering.

---

### ⚙️ Model Details

| Property | Description |
|-----------|-------------|
| Base Model | ContactDoctor Bio Medical Llama 3 2 1B CoT 012025 |
| Method | LoRA (rank 16, alpha 32) |
| Precision | 4 bit QLoRA |
| Dataset | MedMCQA |
| Epochs | 3 |
| Objective | Chain of thought reasoning |
| Framework | Transformers, PEFT |
| License | Apache 2.0 |

---

### 🧬 Example Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, PeftModel

base_model = "ContactDoctor/Bio-Medical-Llama-3-2-1B-CoT-012025"
adapter = "calender/BioLLama-LLM-Adapters"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model)
model = PeftModel.from_pretrained(model, adapter)

query = "A 45 year old presents with fatigue and low hemoglobin. Suggest initial line of management."
inputs = tokenizer(query, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

📊 Evaluation
Metric	Value
Validation Accuracy	40 percent
NEET PG Clinical Subset	72.7 percent
Reasoning Coherence	Improved
Inference	Greedy decoding

🧠 Related Work
🩺 ContactDoctor Bio Medical Llama 3 2 1B CoT 012025

💻 GitHub Repository

📚 Citation
@misc{calendar2025biollama,
  title = {BioLLama LLM Adapters},
  author = {Calendar, S.},
  year = {2025},
  publisher = {Hugging Face},
  note = {https://huggingface.co/calender/BioLLama-LLM-Adapters}
}