---
library_name: transformers
tags:
- text-generation-inference
license: apache-2.0
language:
- en
base_model:
- NousResearch/DeepHermes-3-Llama-3-3B-Preview
pipeline_tag: text-generation
---
# **DeepHermes-3-Llama-3-3B-Preview-Abliterated**  

>  DeepHermes 3 Preview Abliterated is the latest version of our flagship Hermes series of LLMs by Nous Research, and one of the first models in the world to unify Reasoning (long chains of thought that improve answer accuracy) and normal LLM response modes into one model. We have also improved LLM annotation, judgment, and function calling. DeepHermes 3 Preview Abliterated is a hybrid reasoning model, and one of the first LLM models to unify both "intuitive", traditional mode responses and long chain of thought reasoning responses into a single model, toggled by a system prompt.  


### **Example Usage**  

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import flash_attn
import time

tokenizer = AutoTokenizer.from_pretrained("prithivMLmods/DeepHermes-3-Llama-3-3B-Preview-Abliterated")

model = AutoModelForCausalLM.from_pretrained(
    "prithivMLmods/DeepHermes-3-Llama-3-3B-Preview-Abliterated",
    torch_dtype=torch.float16,
    device_map="auto",
    attn_implementation="flash_attention_2",
)

messages = [
    {
        "role": "system",
        "content": "You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem."
    },
    {
        "role": "user",
        "content": "What is y if y=2*2-4+(3*2)"
    }
]

input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors='pt').to("cuda")
generated_ids = model.generate(input_ids, max_new_tokens=2500, temperature=0.8, repetition_penalty=1.1, do_sample=True, eos_token_id=tokenizer.eos_token_id)
print(f"Generated Tokens: {generated_ids.shape[-1:]}")
response = tokenizer.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_space=True)
print(f"Response: {response}")
```
# **Intended Use**

>  DeepHermes-3-Llama-3-3B-Preview-Abliterated is designed for advanced reasoning, problem-solving, and structured thought generation. It seamlessly integrates both intuitive response generation and deep chain-of-thought reasoning, making it ideal for tasks requiring logical deduction, complex problem analysis, and AI-assisted decision-making. With improved annotation, judgment, and function-calling capabilities, this model is well-suited for research, automation, coding assistance, and AI-driven academic or professional applications where accuracy and interpretability are critical.
