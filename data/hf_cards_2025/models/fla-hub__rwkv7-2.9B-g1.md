---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- ar
- es
- pt
metrics:
- accuracy
base_model:
- BlinkDL/rwkv7-g1
pipeline_tag: text-generation
---

# rwkv7-2.9B-g1

<!-- Provide a quick summary of what the model is/does. -->

This is RWKV-7 model under flash-linear attention format.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Bo Peng, Yu Zhang, Songlin Yang, Ruichong Zhang, Zhiyuan Li
- **Funded by:** RWKV Project (Under LF AI & Data Foundation)
- **Model type:** RWKV7
- **Language(s) (NLP):** Multilingual
- **License:** Apache-2.0
- **Parameter count:** 2.9B
- **Tokenizer:** RWKV World tokenizer
- **Vocabulary size:** 65,536

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/fla-org/flash-linear-attention ; https://github.com/BlinkDL/RWKV-LM
- **Paper:** https://arxiv.org/abs/2503.14456
- **Model:** https://huggingface.co/BlinkDL/rwkv7-g1/resolve/main/rwkv7-g1-2.9b-20250519-ctx4096.pth

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Install `flash-linear-attention` and the latest version of `transformers` before using this model:

```bash
pip install git+https://github.com/fla-org/flash-linear-attention
pip install 'transformers>=4.48.0'
```

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
You can use this model just as any other HuggingFace models:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('fla-hub/rwkv7-2.9B-g1', trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained('fla-hub/rwkv7-2.9B-g1', trust_remote_code=True) 
model = model.cuda() # Supported on Nvidia/AMD/Intel eg. model.xpu()
prompt = "What is a large language model?"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True  # Default is True, set to False to disable thinking
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=1024,
    do_sample=True,
    temperature=1.0,
    top_p=0.3,
    repetition_penalty=1.2
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]
print(response)

```


## FAQ
Q: safetensors metadata is none.

A: upgrade transformers to >=4.48.0: `pip install 'transformers>=4.48.0'`
