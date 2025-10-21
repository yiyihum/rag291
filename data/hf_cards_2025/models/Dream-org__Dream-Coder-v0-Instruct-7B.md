---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
---
# Dream-Coder-v0-Instruct-7B

Dream-Coder 7B is a **diffusion LLM for code** trained exclusively on open-source data across its development stages—adaptation, supervised fine-tuning, and reinforcement learning.
It achieves an impressive **21.4% pass@1 on LiveCodeBench (2410-2505)**, outperforming other open-source diffusion LLMs by a wide margin.
More details about the model and usage can be found in the blog and github bellow:

- **Blog:** https://hkunlp.github.io/blog/2025/dream-coder/
- **Github:** https://github.com/DreamLM/Dream-Coder

## Quickstart
To get start with,
please install `transformers==4.46.2` and `torch==2.5.1`. Here is an example to use Dream-Coder 7B:

```python
import torch
from transformers import AutoModel, AutoTokenizer

model_path = "Dream-org/Dream-Coder-v0-Instruct-7B"
model = AutoModel.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = model.to("cuda").eval()

messages = [
    {"role": "user", "content": "Write a quick sort algorithm."}
]
inputs = tokenizer.apply_chat_template(
    messages, return_tensors="pt", return_dict=True, add_generation_prompt=True
)
input_ids = inputs.input_ids.to(device="cuda")
attention_mask = inputs.attention_mask.to(device="cuda")

output = model.diffusion_generate(
    input_ids,
    attention_mask=attention_mask,
    max_new_tokens=768,
    output_history=True,
    return_dict_in_generate=True,
    steps=768,
    temperature=0.1,
    top_p=0.95,
    alg="entropy",
    alg_temp=0.,
)
generations = [
    tokenizer.decode(g[len(p) :].tolist())
    for p, g in zip(input_ids, output.sequences)
]

print(generations[0].split(tokenizer.eos_token)[0])
```