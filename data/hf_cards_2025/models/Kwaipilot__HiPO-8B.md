---
license: apache-2.0
base_model:
- Qwen/Qwen3-8B
library_name: transformers
---

<div align="center">

# HIPO: Hybrid Policy Optimization for Dynamic Reasoning in LLMs

<img src="https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/KIYEa1c_WJEWPpeS0L_k1.png" width="60%" alt="Kwaipilot"/>

---

<a href="https://huggingface.co/Kwaipilot/HIPO-8B" target="_blank">
  <img alt="Hugging Face" src="https://img.shields.io/badge/HuggingFace-fcd022?style=for-the-badge&logo=huggingface&logoColor=000&labelColor"/>
</a>
<a href="https://arxiv.org/abs/2509.23967" target="_blank">
  <img alt="arXiv" src="https://img.shields.io/badge/arXiv-2509.23967-b31b1b.svg?style=for-the-badge"/>
</a>

<br>

<a href="https://arxiv.org/abs/2509.23967"></a>

</div>

This work is a companion to our earlier report [**KAT-V1: Kwai-AutoThink Technical Report**](https://arxiv.org/abs/2509.23967), where we first introduced the **AutoThink paradigm** for controllable reasoning. While KAT-V1 outlined the overall framework of **SFT + RL** for adaptive reasoning, this paper provides the **detailed algorithmic design** of that training recipe.  

***

# Overview

We introduce **HiPO (Hybrid Policy Optimization for Dynamic Reasoning in LLMs)**, a novel RL framework designed to enable models to decide when to “think” (i.e., Think-on)and when to skip reasoning (i.e., Think-off), thereby striking a balance between correctness and efﬁciency. 

HIPO has two main components:

- **Hybrid Data Pipeline** – Collects both think-on and think-off responses, categorizes queries by difficulty, and uses a strong model (e.g., DeepSeek-V3) to generate explanations that justify mode choices.
- **Hybrid Reward System** – Combines rewards for both modes, with bias adjustment to prevent overuse of long reasoning and mode-aware advantage functions to align decisions with performance gains.

![Kim 2025-09-26 145531](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/ZUk76mhDiVITfUsLcvv6F.png)


# Experimental Findings

**Think-on Only (Overthinking).**  
Training only on Think-on data makes the model reason on all problems, causing inefficiency.  

**GRPO.**  
Improves accuracy by **+3.1%**, but increases token length on simple tasks.  

**Think-on/Think-off Mix.**  
Yields higher accuracy (**+4.0%**) while reducing token length (**–10.8%**) and thinking rate (**–22%**).  

**HiPO Advantage.**  
Achieves the best results: **+6.2% accuracy**, **–30% token length**, **–39% thinking rate**, outperforming existing methods in both **efficiency** and **accuracy**.

![Kim 2025-09-26 145349](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/_qzxhMRTL_NTfaGb13LHc.png)


# Data Format

**HiPO** produces responses in a **structured template** that makes the reasoning path explicit and machine-parsable. Two modes are supported:

![Kim 2025-09-26 145842](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/FXfAAN0WVpsaOn1wROInL.png)


# Quick Start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Kwaipilot/HiPO-8B"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768,
    temperature=0.6,
    top_p=0.95,
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 
content = tokenizer.decode(output_ids, skip_special_tokens=True).strip("\n")
print("prompt:\n", prompt)
print("content:\n", content)
```

***

# Citation

```
@article{Zhan2025HiPO,
  title={HiPO: Hybrid Policy Optimization for Dynamic Reasoning in LLMs},
  author={Ken Deng, Zizheng Zhan, Wen Xiang, Wenqiang Zhu and others},
  year={2025},
  institution={arXiv preprint arXiv:2509.23967},
  number={arXiv:2509.23967},
  url={https://arxiv.org/abs/2509.23967}
}
```