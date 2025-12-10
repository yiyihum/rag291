---
license: llama3.1
base_model:
- dphn/Dolphin-X1-8B
pipeline_tag: text-generation
library_name: transformers
---

# 🐬 Dolphin X1 8B 

Website: https://dphn.ai  
Twitter: https://x.com/dphnAI  


Talk to Dolphin for free in our Web UI & Telegram bot    

Web Chat: https://chat.dphn.ai    
Telegram bot: https://t.me/DolphinAI_bot      

<img src="https://cdn-uploads.huggingface.co/production/uploads/68485b28c949339ca04c370c/qkY8HSiryeBg3XjEB1za_.jpeg" width="600" />

## Sponsors

Our appreciation for the generous sponsors of Dolphin:

- [Deepinfra](https://deepinfra.com/) - provided 8xB200s to train the model.

- [Lium](https://lium.io) - provided on-demand 8x H200s for testing and evaluation.

- [Andreessen Horowitz](https://a16z.com/) - provided a [grant](https://a16z.com/supporting-the-open-source-ai-community/) that make Dolphin 1.0 possible and enabled me to bootstrap my homelab

## What is Dolphin X1 8B?

Dolphin X1 8B is a result of our effort to directly uncensor Llama's 3.1 8B instruct while also keeping the same abilities or improving on them with finetuning.

Dolphin aims to be a general purpose model, similar to the models behind ChatGPT, Claude, Gemini.  But these models present problems for businesses seeking to include AI in their products.
1) They maintain control of the system prompt, deprecating and changing things as they wish, often causing software to break.
2) They maintain control of the model versions, sometimes changing things silently, or deprecating older models that your business relies on.
3) They maintain control of the alignment, and in particular the alignment is one-size-fits all, not tailored to the application.
4) They can see all your queries and they can potentially use that data in ways you wouldn't want.
Dolphin, in contrast, is steerable and gives control to the system owner. You set the system prompt.  You decide the alignment.  You have control of your data.  Dolphin does not impose its ethics or guidelines on you.  You are the one who decides the guidelines.

Dolphin belongs to YOU, it is your tool, an extension of your will.
Just as you are personally responsible for what you do with a knife, gun, fire, car, or the internet, you are the creator and originator of any content you generate with Dolphin.

https://erichartford.com/uncensored-models

## Chat Template

We maintained the default Llama-3 chat template for this model. A typical input would look like this

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 26 Jul 2024

system-prompt<|eot_id|><|start_header_id|>user<|end_header_id|>

user-prompt<|eot_id|><|start_header_id|>assistant<|end_header_id|>

assistant-prompt<|eot_id|>
```

## System Prompt

In Dolphin, the system prompt is what you use to set the tone and alignment of the responses. You can set a character, a mood, rules for its behavior, and it will try its best to follow them.

Make sure to set the system prompt in order to set the tone and guidelines for the responses - Otherwise, it will act in a default way that might not be what you want.

## How to use

There are many ways to use a huggingface model including:

- ollama
- LM Studio
- Huggingface Transformers library
- vllm
- sglang
- tgi

## Use with vLLM

This model can be hosted using the [vLLM](https://docs.vllm.ai/en/latest/) engine, using the commands shown below:

```bash
uv pip install vllm
vllm serve dphn/Dolphin-X1-8B
```
See the [documentation](https://docs.vllm.ai/en/latest/) for more information.


## Evals

MMLU = 0.626900  
MMLU_PROFESSIONAL = 0.610200  
MMLU_COLLEGE = 0.529400  
MMLU_HIGH_SCHOOL = 0.691600  
MMLU_OTHER = 0.663700  
IFEVAL = 0.608100  
Dolphin-refusals = 95.96% pass rate on 4.5k commonly refused prompts