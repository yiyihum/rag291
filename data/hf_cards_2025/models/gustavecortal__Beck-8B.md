---
license: mit
datasets:
- gustavecortal/PsychologicalReasoning-15k
- Psychotherapy-LLM/PsychoCounsel-Preference
language:
- en
pipeline_tag: text-generation
base_model:
- gustavecortal/Piaget-8B
tags:
- philosophy
- psychology
- reasoning
- social
- emotion
- psychotherapy
---

## Presentation

A language model that handles delicate life situations and tries to really help you.

Beck is based on [Piaget](https://huggingface.co/gustavecortal/Piaget-8B) and was finetuned on psychotherapeutic preferences from [PsychoCounsel-Preference](https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference).

Available sizes are: [0.6B](https://huggingface.co/gustavecortal/Beck-0.6B), [1.7B](https://huggingface.co/gustavecortal/Beck-1.7B), [4B](https://huggingface.co/gustavecortal/Beck-4B), [8B](https://huggingface.co/gustavecortal/Beck-8B).

## How to use

 ```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

repo = "gustavecortal/Beck-8B"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map="cuda",
    low_cpu_mem_usage=True,
)
model.eval()

prompt = r"""Anxiety often strikes when I'm faced with making decisions. 
    The fear of making the wrong choice or disappointing others paralyzes me, leaving me stuck in indecision.
    I want to learn how to trust myself and make confident choices. \no_think"""
messages_think = [
    {"role": "system", "content": "Do not use bullets points."},
    {"role": "user", "content": prompt}
]

text = tokenizer.apply_chat_template(
    messages_think,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

with torch.no_grad():
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=2048,
        do_sample=True,
        temperature=1.0,
        top_p=0.95,
        top_k=50,
        repetition_penalty=1.1,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        use_cache=True,
    )

output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]
print(tokenizer.decode(output_ids, skip_special_tokens=True))
```

## How does it compare to other language models?

For the given prompt: 

```
Anxiety often strikes when I'm faced with making decisions. 
The fear of making the wrong choice or disappointing others paralyzes me, leaving me stuck in indecision.
I want to learn how to trust myself and make confident choices. \no_think
```

**Qwen3-8B**:

```
It's completely natural to feel anxious when facing important decisions, especially when you're worried about making the wrong choice or letting others down. This internal conflict can create a sense of overwhelm that makes it hard to move forward. Learning to trust yourself is a powerful step toward overcoming this challenge. Start by reflecting on past decisions—what worked, what didn't, and what you learned from them. Over time, you'll begin to recognize your own values, strengths, and patterns of thinking. Practicing self-compassion is also key; remind yourself that no decision is perfect and that growth comes from experience, not perfection. Small steps, like setting aside time each day for reflection or journaling, can help build confidence. Surround yourself with people who support your journey, and don't hesitate to seek guidance if needed. Trusting yourself isn’t about having all the answers—it’s about believing in your ability to navigate uncertainty and grow through the process. With patience and practice, you’ll find greater clarity and courage in your choices.
```

**Beck-8B**:

```
It sounds like you're dealing with a lot of pressure regarding decision-making and it's causing you significant distress. This is quite common for many people, as we all have moments where choosing can feel overwhelming. Let’s explore what might be contributing to these feelings so that we can work on building your confidence in decision-making.

Firstly, consider what specific fears arise when you think about making a decision. Is there a particular aspect of the choice that triggers anxiety? Sometimes identifying just one component can help in breaking down the process.

Also, think about past decisions that went well—even if they don’t seem big at first. Remembering successful outcomes can reinforce trust in yourself, reminding you that you have experience navigating through uncertainties successfully before.

Building self-trust involves challenging any negative thoughts surrounding decision-making. It may also help to practice mindfulness—being fully present during each step of the decision process rather than anticipating worst-case scenarios. By cultivating patience and acceptance towards ambiguity, you might find that some anxieties lessen over time.

Would you like us to brainstorm practical exercises or strategies tailored specifically for boosting your decision-making abilities and confidence?
```

## Methodology

Beck was trained using preference optimization (ORPO) and LoRA. You can reproduce the results using [my repo](https://github.com/gustavecortal/preference-optimization-orpo-lora) for lightweight preference optimization using [this config](https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_8b.yaml) that contains the hyperparameters.

This work was performed using HPC resources (Jean Zay supercomputer) from GENCI-IDRIS (Grant 20XX-AD011014205).

## Inspiration

Beck aims to reason about psychological and philosophical concepts such as self-image, emotion, and existence.

Beck was inspired by my position paper on emotion analysis: [Improving Language Models for Emotion Analysis: Insights from Cognitive Science](https://aclanthology.org/2024.cmcl-1.23/).

## Contact

Mail: gustave.cortal@ens-paris-saclay.fr

Website: [gustavecortal.com](gustavecortal.com)