---
license: apache-2.0
tags:
- text-generation
- causal-lm
- reasoning
library_name: transformers
---
# JET-7B

JET-7B is designed to improve the efficient reasoning of LLMs by training the base **DeepSeek-Distill-Qwen-7B**  model with a reinforcement learning framework. Through this training, the model learns to generate high-quality reasoning steps while minimizing unnecessary computation and token usage.


## Chat Template

```python
def build_JET_chat_template(question, tokenizer):
    system_prompt = (
        "You are a helpful AI assistant. A conversation takes place between the User "
        "and the Assistant. The User asks a question, and the Assistant solves it.\n"
        "Please help me solve this question. Wrap only the final answer in \\boxed{}."
    )
    return tokenizer.apply_chat_template(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        tokenize=False,
        add_generation_prompt=True
    )
