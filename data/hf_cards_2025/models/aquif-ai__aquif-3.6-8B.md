---
license: apache-2.0
base_model: aquif-ai/aquif-3.5-8B-Think
tags:
- text-generation-inference
- reasoning
- thinking
- hybrid
- efficient
- dynamic
- transformers
- aquif
- math
- coding
- small
- aquif-3.5
- aquif-3.6
- aquif
- llm
language:
- en
- de
- it
- pt
- fr
- hi
- es
- th
- zh
- ja
library_name: transformers
pipeline_tag: text-generation
---

# aquif-3.6-8B

## Summary

**aquif-3.6-8B** is a hybrid reasoning model that automatically determines when and how deeply to think based on query complexity. Built on aquif-3.5-8B-Think with AutoThink RL data, it achieves 28% better token efficiency and 4% performance improvement across benchmarks.

### Contents

- [Key Features](#key-features) - Dynamic reasoning, efficiency gains, and smart resource allocation
- [Performance](#performance) - Benchmark results showing 4% average improvement
- [Token Efficiency](#token-efficiency) - 28% reduction in token usage
- [Thinking Ratio](#thinking-ratio) - 12% reduction in thinking frequency
- [Benchmark Highlights](#benchmark-highlights) - Detailed results for AIME, LiveCodeBench, and GPQA Diamond
- [Model Details](#model-details) - Architecture and specifications
- [Usage](#usage) - Code examples for implementation
- [Previous Versions](#previous-versions) - Links to earlier models

**Automatic Thinking**

aquif-3.6-8B is a hybrid reasoning model that dynamically decides if and how much to think based on query complexity. Inspired by KAT-V1's approach of automatic thinking using AutoThink RL data on top of aquif-3.5-8B-Think, the model uses the following format:
```
<judge>
[analyzes whether to think or not]
</judge>

<think_on/off>
<think>
[thinking content]
</think>

<answer>
</answer>
```
This is the same format as KAT-V1-40B. Unlike something like DeepSeek-V3.1's toggleable reasoning that requires manual control (thinking_on/off), aquif-3.6's judge autonomously allocates reasoning depth - intelligently adapting its cognitive effort to each task automatically.

## Key Features

- 🧠 **Dynamic Reasoning**: Automatically determines when and how deeply to think
- ⚡ **28% More Efficient**: Significant token reduction while improving performance
- 📈 **Better Performance**: 4% average improvement across benchmarks
- 🎯 **Smart Resource Allocation**: 12% reduction in thinking ratio on average

## Performance
<img src="https://cdn-uploads.huggingface.co/production/uploads/6747320df82ae35f0327cdd3/Jxv_kthSTqEiKdygHyVNl.png" alt="Chart 1" width="512"/>

Benchmark | aquif-3.6-8B | aquif-3.5-8B | Improvement |
|-----------|--------------|--------------|-------------|
| AIME 2025 | 82.5 | 81.4 | +1% |
| LiveCodeBench | 64.2 | 61.5 | +4% |
| GPQA Diamond | 71.0 | 66.8 | +6% |
| **Average** | **72.6** | **69.9** | **+4%** |

## Token Efficiency
<img src="https://cdn-uploads.huggingface.co/production/uploads/6747320df82ae35f0327cdd3/4k3HCx-LUigoGP51q_sdB.png" alt="Chart 2" width="512"/>

| Benchmark | aquif-3.6-8B | aquif-3.5-8B | Reduction |
|-----------|--------------|--------------|-----------|
| AIME 2025 | 15,670 | 21,265 | -26% |
| LiveCodeBench | 13,240 | 19,460 | -32% |
| GPQA Diamond | 8,760 | 11,560 | -24% |
| **Average** | **12,557** | **17,428** | **-28%** |

## Thinking Ratio
<img src="https://cdn-uploads.huggingface.co/production/uploads/6747320df82ae35f0327cdd3/EkrkynHLQasZ3CRxySYsp.png" alt="Chart 3" width="512"/>

| Benchmark | aquif-3.6-8B | aquif-3.5-8B | Reduction |
|-----------|--------------|--------------|-----------|
| AIME 2025 | 93.0% | 100.0% | -7% |
| LiveCodeBench | 82.0% | 100.0% | -18% |
| GPQA Diamond | 89.0% | 100.0% | -11% |
| **Average** | **88.0%** | **100.0%** | **-12%** |

## Benchmark Highlights

- **AIME 2025**: 26% fewer tokens, +1% performance, -7% thinking ratio
- **LiveCodeBench**: 32% fewer tokens, +4% performance, -18% thinking ratio  
- **GPQA Diamond**: 24% fewer tokens, +6% performance, -11% thinking ratio

## Model Details

- **Base Model**: 8B parameters
- **Architecture**: Hybrid reasoning with dynamic thinking allocation
- **Context Length**: 40K tokens
- **License**: Apache 2.0

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "aquif-ai/aquif-3.6-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Solve this problem: What is the sum of all prime numbers between 1 and 100?"}
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=2048,
    temperature=0.7,
    do_sample=True
)

response = tokenizer.decode(outputs[0][input_ids.shape[-1]:], skip_special_tokens=True)
print(response)
```

## Previous Versions

- [aquif-3.5-8B-Think](https://huggingface.co/aquif-ai/aquif-3.5-8B-Think)

---

Built by [aquif-ai](https://huggingface.co/aquif-ai)