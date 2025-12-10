---
base_model: unsloth/Qwen3-1.7B
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:unsloth/Qwen3-1.7B
- lora
- sft
- transformers
- trl
- unsloth
license: mit
datasets:
- az-llm/az_academic_qa-v1.0
- az-llm/az_creative-v1.0
- tahmaz/azerbaijani_text_math_qa1
- omar07ibrahim/Alpaca_Stanford_Azerbaijan
language:
- az
metrics:
- accuracy
---


<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Nizami_Rug_Crop.jpg" style="width: 350px; height:500px;"/> 
</p>

<h2 style="font-size: 32px; text-align: center;"> Nizami-1.7B</h2>
<p style="font-size: 21px; text-align: center;">A Lightweight Language Model</p>

<h3 style="font-size: 21px; color: #2980b9;">Model Description 📝</h3>

Nizami-1.7B is a fine-tuned version of Qwen3-1.7B in Azerbaijani. 
It was trained on a curated dataset of 35,916 examples from historical, legal, math, philosophical, and social science texts.


<h3 style="font-size: 21px; color: #2980b9;">Key Features ✨</h3>

* **Architecture**: Transformer-based language model 🏗️
* **Developed by**: Rustam Shiriyev
* **Language(s)**: Azerbaijani
* **License**: MIT
* **Fine-Tuning Method**: Supervised fine-tuning
* **Domain**: Academic texts (History, Math, Law, Philosophy, Social Sciences) 📚
* **Finetuned from model**: unsloth/Qwen3-1.7B

<h3 style="font-size: 21px; color: #2980b9;">Intended Use</h3>

* Academic research assistance in Azerbaijani 🏆
* Question answering on humanities/social science topics 🎯
* Knowledge exploration in Azerbaijani⚡

<h3 style="font-size: 21px; color: #2980b9;">Limitations ⚠️</h3>

* Generating factual statements without verification
* Limited dataset size (35,916 examples) → may not generalize perfectly outside training domains.
* Possible hallucinations if asked for factual details.


<h3 style="font-size: 21px; color: #2980b9;">Evaluation 📊</h3>

AARA: [khazarai/AARA_Azerbaijani_LLM_Benchmark](https://huggingface.co/datasets/khazarai/AARA_Azerbaijani_LLM_Benchmark)  

| Model Name                              |   AARA    |
| --------------------------------------- | --------- | 
| **khazarai/Nizami-1.7B**                | **40.0**  | 
| Qwen/Qwen3-1.7B                         |   39.0    | 
| google/gemma-2-2b-it                    |   34.5    |
| Qwen/Qwen2.5-1.5B-Instruct              |   13.5    |
| meta-llama/Llama-3.2-1B-Instruct        |   11.0    |          



<h3 style="font-size: 21px; color: #2980b9;">How to Get Started with the Model 💻</h3>

```python
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-1.7B",)
base_model = AutoModelForCausalLM.from_pretrained(
    "unsloth/Qwen3-1.7B",
    device_map={"": 0}
)

model = PeftModel.from_pretrained(base_model,"khazarai/Nizami-1.7B")

question = """
Əldə olunan arxeoloji qazıntı materiallarına əsasən, Eneolit dövründə Azərbaycanda metalın ilk istifadəsi ilə bağlı hansı konkret obyektlər tapılmışdır və bu obyektlər həmin dövrdə cəmiyyətin sosial strukturunun inkişafına necə təsir etmişdir? Əlavə olaraq, həmin dövrdə metallurgiya və metalişləmə sənətkarlığının inkişafının iqtisadi və mədəni aspektləri haqqında nə deyə bilərsiniz?
"""

messages = [
    {"role" : "user", "content" : question}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize = False,
    add_generation_prompt = True, 
    enable_thinking = False,
)

from transformers import TextStreamer
_ = model.generate(
    **tokenizer(text, return_tensors = "pt").to("cuda"),
    max_new_tokens = 1800,
    temperature = 0.7,
    top_p = 0.8,
    top_k = 20,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)
```
**For pipeline:**
```python
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

tokenizer = AutoTokenizer.from_pretrained("unsloth/Qwen3-1.7B")
base_model = AutoModelForCausalLM.from_pretrained("unsloth/Qwen3-1.7B")
model = PeftModel.from_pretrained(base_model, "khazarai/Nizami-1.7B")

question ="""
Əldə olunan arxeoloji qazıntı materiallarına əsasən, Eneolit dövründə Azərbaycanda metalın ilk istifadəsi ilə bağlı hansı konkret obyektlər tapılmışdır və bu obyektlər həmin dövrdə cəmiyyətin sosial strukturunun inkişafına necə təsir etmişdir? Əlavə olaraq, həmin dövrdə metallurgiya və metalişləmə sənətkarlığının inkişafının iqtisadi və mədəni aspektləri haqqında nə deyə bilərsiniz?
"""

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
messages = [
    {"role": "user", "content": question}
]
pipe(messages)
```

<h3 style="font-size: 21px; color: #2980b9;">Training Data </h3>

Dataset I: [az-llm/az_academic_qa-v1.0](https://huggingface.co/datasets/az-llm/az_academic_qa-v1.0)
Description:
A 7,000-example dataset for academic-style comprehension and reasoning in Azerbaijani. 

Dataset II: [az-llm/az_creative-v1.0](https://huggingface.co/datasets/az-llm/az_creative-v1.0)
Description: 
A 4,000-example creative dataset with imaginative Azerbaijani prompts and expressive responses. 
Includes role-based instructions (e.g., Galileo, interstellar assistant, detective), fictional narratives, poetic reasoning, and emotional simulations.

Dataset III: [tahmaz/azerbaijani_text_math_qa1](https://huggingface.co/datasets/tahmaz/azerbaijani_text_math_qa1)
Description: A dataset of 6,500 high school math examples in Azerbaijani.

Dataset IV: [omar07ibrahim/Alpaca_Stanford_Azerbaijan](https://huggingface.co/datasets/omar07ibrahim/Alpaca_Stanford_Azerbaijan)
Description: Azerbaijani version of the Alpaca dataset for instruction-following tasks. 


### Framework versions

- PEFT 0.16.0