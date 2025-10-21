---
license: mit
datasets:
- cognitivecomputations/dolphin-r1
- GeneralReasoning/GeneralThought-430K
- gustavecortal/PsychologicalReasoning-15k
language:
- en
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-8B
tags:
- philosophy
- psychology
- reasoning
- social
- emotion
---

## Presentation

Piaget, a language model finetuned on 15k psychological and philosophical reasoning traces.

Piaget is based on Qwen3 and was finetuned on a subset of open reasoning traces from [Dolphin R1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1) and [General Reasoning](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K).

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Piaget-0.6B), [1.7B](https://huggingface.co/gustavecortal/Piaget-1.7B), [4B](https://huggingface.co/gustavecortal/Piaget-4B), [8B](https://huggingface.co/gustavecortal/Piaget-8B).

## How to use

 ```py
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.pipelines import pipeline
import torch

repo = "gustavecortal/Piaget-8B"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True
)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = tokenizer.apply_chat_template(
    [
        {
            "role": "user",
            "content": "Create a new psychotherapeutic technique based on cybernetic principles",
        }
    ],
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True,
)

print(pipe(prompt, max_new_tokens=2048, do_sample=True)[0]["generated_text"])
```

## Methodology

We performed domain filtering on [Dolphin R1](https://huggingface.co/datasets/cognitivecomputations/dolphin-r1) and [General Reasoning](https://huggingface.co/datasets/GeneralReasoning/GeneralThought-430K). 

Prompts were embedded, clustered with k-means (k=20 000) and majority-voted for domain labels using [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B), following the [Intelligent Internet pipeline](https://huggingface.co/Intelligent-Internet/II-Medical-8B-1706). 

Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16).

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Inspiration

Piaget aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Piaget was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)