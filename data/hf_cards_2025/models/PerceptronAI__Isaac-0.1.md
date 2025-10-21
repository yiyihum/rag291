---
license: cc-by-nc-4.0
base_model:
- Qwen/Qwen3-1.7B
- google/siglip2-so400m-patch14-384
library_name: transformers
tags:
- perceptron
- issac-0.1
---

# [Isaac-0.1 by Perceptron](https://www.perceptron.inc/blog/introducing-isaac-0-1)
*Note this is the Post-trained model* [Try out the model on our playground](https://www.perceptron.inc/demo)

We're introducing Isaac 0.1, our first perceptive-language model and a major step toward building AI systems that can understand and interact with the physical world. Isaac 0.1 is an open-source, 2B-parameter model built for real-world applications. It sets a new standard for efficiency, delivering capabilities that meet or exceed those of models over 50 times its size.

Founded by the team behind Meta's Chameleon multimodal models, Perceptron is tackling a fundamental challenge: bringing the power of physical AI to the dynamic, multimodal, and real-time environments we live and work in.

Isaac 0.1 is the first in our family of models built to be the intelligence layer for the physical world. It's now available open source for researchers and developers everywhere.

## What’s new in Isaac 0.1
**Visual QA, simply trained**
Strong results on standard understanding benchmarks with a straightforward, reproducible training recipe.

**Grounded spatial intelligence**
Precise pointing and localization with robust spatial reasoning. Ask “what’s broken in this machine?” and get grounded answers with highlighted regions—handling occlusions, relationships, and object interactions.

**In-context learning for perception**
Show a few annotated examples (defects, safety conditions, etc.) in the prompt and the model adapts—no YOLO-style fine-tuning or custom detector stacks required.

**OCR & fine-grained detail**
Reads small text and dense scenes reliably, across resolutions, with dynamic image handling for tiny features and cluttered layouts.

**Conversational Pointing**
A new interaction pattern where language and vision stay in lockstep: every claim is grounded and visually cited, reducing hallucinations and making reasoning auditable.


## Benchmarks

![visual_qa](https://framerusercontent.com/images/WFsL5CWqxvsmJrlUuMXA5T8LdVY.png?width=2216&height=1610)
![grounding](https://framerusercontent.com/images/2T1Th5SaXdYhNKyxzd2ge61diA.png?width=1736&height=1260)

## Example 

```bash
pip install perceptron
```

## Example using transformers

Learn more: [Huggingface Example Repo](https://github.com/perceptron-ai-inc/perceptron/tree/main/huggingface)

```bash
!git clone https://github.com/perceptron-ai-inc/perceptron.git
!cp -r perceptron/huggingface ./huggingface
```

```python
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM
from huggingface.modular_isaac import IsaacProcessor

tokenizer = AutoTokenizer.from_pretrained("PerceptronAI/Isaac-0.1", trust_remote_code=True, use_fast=False)
config = AutoConfig.from_pretrained("PerceptronAI/Isaac-0.1", trust_remote_code=True)
processor = IsaacProcessor(tokenizer=tokenizer, config=config)
model = AutoModelForCausalLM.from_pretrained("PerceptronAI/Isaac-0.1", trust_remote_code=True)
```