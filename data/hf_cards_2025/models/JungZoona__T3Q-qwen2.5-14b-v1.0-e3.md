---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M/blob/main/LICENSE
language:
- en
- ko
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-14B-Instruct-1M
tags:
- chat
library_name: transformers
---

> Update @ 2025.03.14: The updated version, [**T3Q-qwen2.5-14b-v1.2-e2**](https://huggingface.co/JungZoona/T3Q-qwen2.5-14b-v1.2-e2) release  

## Model Summary
T3Q-qwen2.5-14b-v1.0-e3 is a post-trained version of the Qwen/Qwen2.5-14B-Instruct-1M model.  
(LoRA-8-4-0.0001-cosine-32-16 with train_data_v1.0)  
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63e05d54a98d931aa90a7e18/wcNgrnOUeuLnNTgSFsDzg.png)  
  
  
## Global Open LLM Leaderboard Performance
This model achieved **1st place in performance among models under 32b** in the [**Global Open LLM Leaderboard**](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/?params=0%2C32). [[**View Article**]](https://www.aitimes.com/news/articleView.html?idxno=168786)   
![image/png](https://cdn-uploads.huggingface.co/production/uploads/63e05d54a98d931aa90a7e18/8duj8OLlrVDqnMUDIO2WG.png)
<details>
  <summary>Page Capture</summary>
  <img src="https://cdn-uploads.huggingface.co/production/uploads/63e05d54a98d931aa90a7e18/r-YILW4uipdjTfEKAFG4i.png" alt="Page Capture">
</details>  
  
  
## Quick Start
Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "JungZoona/T3Q-qwen2.5-14b-v1.0-e3"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

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

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```