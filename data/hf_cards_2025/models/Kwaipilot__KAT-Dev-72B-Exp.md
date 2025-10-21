---
license: apache-2.0
library_name: transformers
---
<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/KIYEa1c_WJEWPpeS0L_k1.png" width="100%" alt="Kwaipilot" />
</div>

<hr>


# News

🔥 We’re thrilled to announce the release of **KAT-Dev-72B-Exp**, our latest and most powerful model yet!

🔥 You can now try our **strongest** proprietary coder model **KAT-Coder** directly on the [**StreamLake**](https://www.streamlake.ai/product/kat-coder) platform **for free**.

# Highlights
**KAT-Dev-72B-Exp**  is an open-source 72B-parameter model for software engineering tasks.

On SWE-Bench Verified, **KAT-Dev-72B-Exp** achieves **74.6%** accuracy ⚡ — **when evaluated strictly with the SWE-agent scaffold**.

**KAT-Dev-72B-Exp** is the experimental reinforcement-learning version of the KAT-Coder model. Through this open-source release, we aim to reveal the technical innovations behind KAT-Coder’s large-scale RL to developers and researchers.


![Kim 2025-10-10 165138](https://cdn-uploads.huggingface.co/production/uploads/61ee40a269351366e29972ad/-1nx5HYc-wTjUFNbf-GfO.png)

# Introduction
 
We rewrote the attention kernel and redesigned the training engine for shared prefix trajectories to achieve highly efficient RL training, especially for scaffolds leveraging context management. 

Furthermore, to prevent exploration collapse observed in RL training, we reshaped advantage distribution based on pass rates: amplifying the advantage scale of highly exploratory groups while reducing that of low-exploration ones.


# Quickstart

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "KAT-Dev-72B-Exp"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
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
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=65536
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

content = tokenizer.decode(output_ids, skip_special_tokens=True)

print("content:", content)
```

# SWE agent Evaluation Parameters

```
temperature: 0.6
max_turns: 150
history_processors.n: 100
```

For full settings please refer to inference.yaml