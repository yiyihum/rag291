---
base_model: DoppelReflEx/L3-8B-R1-WolfCore
library_name: transformers
model_name: Looking_Glass-llama
tags:
- generated_from_trainer
- sft
- unsloth
- trl
licence: license
---

# Model Card for Looking_Glass-llama

This was an interm model meant for testing and planned on back merging and continued training. 
I had it on public for a very short time and Quants were made. So keeping it public I guess. 
Trained for thinking but this model is a bit repetative.
There will be another version of it coming when I get my eq back up and running.
Recomendation for now. Use a high temp and repetition penalty.
Uses llama 3 template. Check out my Looking Glass system prompts dataset for example system prompts to use.

This model is a fine-tuned version of [DoppelReflEx/L3-8B-R1-WolfCore](https://huggingface.co/DoppelReflEx/L3-8B-R1-WolfCore).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="None", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with SFT.

### Framework versions

- TRL: 0.23.0
- Transformers: 4.56.2
- Pytorch: 2.8.0
- Datasets: 3.6.0
- Tokenizers: 0.22.1

## Citations



Cite TRL as:
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallou{\'e}dec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```