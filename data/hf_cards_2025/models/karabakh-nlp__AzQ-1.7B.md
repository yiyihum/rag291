---
base_model: unsloth/Qwen3-1.7B
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:unsloth/Qwen3-1.7B
- lora
- sft
- transformers
- trl
- unsloth
- reasoning
license: apache-2.0
datasets:
- karabakh-nlp/Aze-Instruct-2K
language:
- az
metrics:
- accuracy
---


<p align="center">
  <img src="https://t3.ftcdn.net/jpg/04/59/43/10/360_F_459431060_VFZqbsIB1F1bAPV8cQwBGsqVNvRHoLr7.jpg" style="width: 360px; height:360px;"/> 
</p>

# AzQ-1.7B 🧠🇦🇿

**AzQ-1.7B** is a fine-tuned Azerbaijani **reasoning and instruction-following model**, trained on the **Aze-Instruct-2K** dataset — a 2,001-sample, expert-curated dataset across 12 reasoning and problem-solving domains.  
It is based on **Qwen3-1.7B** and optimized for **logical, mathematical, scientific, and analytical reasoning** in the Azerbaijani language.


## 🧩 Model Details

| Attribute | Description |
|------------|-------------|
| **Base Model** | Qwen3-1.7B
| **Fine-tuning Type** | Supervised Fine-Tuning (SFT) |
| **Framework** | PEFT (LoRA) |
| **Language** | Azerbaijani (az) |
| **Dataset** | Aze-Instruct-2K |
| **Dataset Size** | 2,001 samples |
| **Epochs** | 5 |
| **Learning Rate** | 5e-5 |
| **Training Time** | ~1 hours on 1×T4 GPU |
| **License** | apache-2.0 |


## 🎯 Objective

The goal of **AzQ-1.7B** is to strengthen Azerbaijani LLM/SLM capabilities in:
- Analytical and logical reasoning  
- Mathematical problem-solving  
- Scientific explanation and hypothesis evaluation  
- Code and SQL generation  
- Philosophical and ethical inference  
- Contextual scenario analysis


## 💬 Example Usage

```python
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-1.7B",)
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/Qwen3-1.7B",
    device_map={"": 0}
)

model = PeftModel.from_pretrained(base_model,"karabakh-nlp/AzQ-1.7B")

question = """
f(x) = 1/(1 - x) funksiyasının Maclaurin silsiləsini yazın və onun yığılma intervalını təyin edin.
"""

messages = [
    {"role" : "user", "content" : question}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, 
    enable_thinking = False,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 1200,
    temperature = 0.7,
    top_p = 0.8,
    top_k = 20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```

## Citation 

```misc
@model{AzQ-1.7B,
  title={AzQ-1.7B: Azerbaijani Reasoning and Instruction Model},
  author={Rustam Shiriyev},
  year={2025},
  publisher={Hugging Face},
  howpublished={https://huggingface.co/karabakh-nlp/AzQ-1.7B}
}
```
### Framework versions

- PEFT 0.16.0