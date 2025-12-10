---
base_model:
- Ewere/Qwen3-30B-A3B-abliterated-erotic
- unsloth/Qwen3-30B-A3B-Thinking-2507
tags:
- merge
- mergekit
- lazymergekit
- Ewere/Qwen3-30B-A3B-abliterated-erotic
- unsloth/Qwen3-30B-A3B-Thinking-2507
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
---
# 🧠 Qwen3-30B-A3B-Thinking-2507-Amoral-Edition
**Qwen3-30B-A3B-Thinking-2507-Amoral-Edition** is a fusion of specialized models using the **DARE TIES** technique, creating a versatile solution for natural language applications.

## 📋 Overview
This model was developed using the **DARE TIES** method (Drop And REscale with Ties-Elimination), combining specialized models to create a compact and efficient solution for natural language conversations.

### 🔧 Base Models Used
**Qwen3-30B-A3B-Thinking-2507-Amoral-Edition** is the result of merging the following models:
  - **[Ewere/Qwen3-30B-A3B-abliterated-erotic](https://huggingface.co/Ewere/Qwen3-30B-A3B-abliterated-erotic)**
  - **[unsloth/Qwen3-30B-A3B-Thinking-2507](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507)**

### 🛠️ Merge Tool
The merge was performed using **[LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing)**, simplifying the process of merging language models with advanced configurations.

## 🧩 Technical Configuration
### Merge Parameters
```yaml
models:
  - model: Ewere/Qwen3-30B-A3B-abliterated-erotic
    parameters:
      density: 0.6
      weight: 0.6
  - model: unsloth/Qwen3-30B-A3B-Thinking-2507
    parameters:
      density: 0.6
      weight: 0.4
merge_method: dare_ties
base_model: unsloth/Qwen3-30B-A3B-Thinking-2507
parameters:
  normalize: true
  int8_mask: false
dtype: bfloat16
````

### Technical Specs

* **Architecture:** Qwen3 30B
* **Merge Method:** DARE TIES
* **Precision:** BFloat16
* **Normalization:** Enabled
* **Int8 Mask:** Disabled
* **Language:** English

## 💻 How to Use

### Dependency Installation

```bash
pip install -qU transformers accelerate torch
```

### Basic Example

```python
from transformers import AutoTokenizer
import transformers
import torch

model = "rodrigomt/Qwen3-30B-A3B-Thinking-2507-Amoral-Edition"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

### English Conversation Example

```python
conversation = [
    {"role": "user", "content": "Hello! How are you?"},
    {"role": "assistant", "content": "Hi! I’m doing well, thanks for asking. How can I help you today?"}
]
prompt = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
outputs = pipeline(prompt, max_new_tokens=128, temperature=0.7)
print(outputs[0]["generated_text"])
```

## ⚠️ Minimum Requirements

* **RAM:** 16GB
* **VRAM:** 24GB+ (GPUs with less will not run this model properly)
* **Storage:** 20GB available
* **GPU:** RTX 3090 / A6000 / H100 or higher