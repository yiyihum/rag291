---
language:
- en
license: apache-2.0
pipeline_tag: text-generation
tags:
- agent
- communication
arxiv: 2510.03215
library_name: transformers
---

This is the C2C Fuser, presented in the paper [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](https://huggingface.co/papers/2510.03215).

Cache-to-Cache (C2C) enables Large Language Models to communicate directly through their KV-Caches, bypassing text generation. By projecting and fusing KV-Caches between models, C2C achieves 8.5–10.5% higher accuracy than individual models and 3.0–5.0% better performance than text-based communication, with 2.0× speedup in latency.

Please visit our [GitHub repo](https://github.com/thu-nics/C2C) for more information.

Project page: [https://fuvty.github.io/C2C_Project_Page/](https://fuvty.github.io/C2C_Project_Page/)

### Sample Usage

Here's how to load the published C2C weights from the Hugging Face collection and run an inference example:

```python
import torch
from huggingface_hub import snapshot_download
from script.playground.inference_example import load_rosetta_model, run_inference_example

checkpoint_dir = snapshot_download(
    repo_id="nics-efc/C2C_Fuser",
    allow_patterns=["qwen3_0.6b+qwen2.5_0.5b_Fuser/*"],
)

model_config = {
    "rosetta_config": {
        "base_model": "Qwen/Qwen3-0.6B",
        "teacher_model": "Qwen/Qwen2.5-0.5B-Instruct",
        "checkpoints_dir": f"{checkpoint_dir}/qwen3_0.6b+qwen2.5_0.5b_Fuser/final",
    }
}

rosetta_model, tokenizer = load_rosetta_model(model_config, eval_config={}, device=torch.device("cuda"))
device = rosetta_model.device

prompt = [{"role": "user", "content": "Say hello in one short sentence."}]
input_text = tokenizer.apply_chat_template(prompt, tokenize=False, add_generation_prompt=True, enable_thinking=False)
inputs = tokenizer(input_text, return_tensors="pt").to(device)

instruction_index = torch.tensor([1, 0], dtype=torch.long).repeat(inputs['input_ids'].shape[1] - 1, 1).unsqueeze(0).to(device)
label_index = torch.tensor([-1, 0], dtype=torch.long).repeat(1, 1).unsqueeze(0).to(device)
kv_cache_index = [instruction_index, label_index]

with torch.no_grad():
    sampling_params = {
        'do_sample': False,
        'max_new_tokens': 256
    }
    outputs = rosetta_model.generate(**inputs, kv_cache_index=kv_cache_index, **sampling_params)
    output_text = tokenizer.decode(outputs[0, instruction_index.shape[1] + 1:], skip_special_tokens=True)
    print(f"C2C output text: {output_text}")
```