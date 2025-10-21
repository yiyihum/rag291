---
language:
- ach
- adh
- alz
- bfa
- cgg
- en
- gwr
- kdi
- kdj
- keo
- kin
- koo
- kpz
- laj
- lgg
- lsm
- luc
- lug
- mhi
- myx
- nuj
- nyn
- nyo
- pok
- rub
- ruc
- rwm
- swa
- teo
- tlj
- ttj
- xog
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- multilingual
- african-languages
- ugandan-languages
- translation
- text-generation
base_model: Qwen/Qwen3-14B
datasets:
- Sunbird/ug40-instructions
- Sunbird/salt
model-index:
- name: Sunflower-14B
  results:
  - task:
      type: translation
      name: Machine Translation
    dataset:
      name: Sunflower Translation Eval
      type: Sunbird/sunflower-translation-eval
    metrics:
    - type: chrf
      value: 0.366
      name: chrF (eng→xx)
    - type: chrf
      value: 0.419
      name: chrF (xx→eng)
    - type: bleu
      value: 19.61
      name: BLEU (xx→eng)
arxiv: 2510.07203
---

# 🌻 Sunflower-14B Model Card

## Model Description

🌻 Sunflower-14B is a multilingual language model developed by Sunbird AI for Ugandan languages. Built on the Qwen 3-14B architecture, the model supports translation and text generation across 31 Ugandan languages plus English. The model achieves the highest translation accuracy among evaluated models in 24 of 31 language pairs.

**Developed by:** Sunbird AI  
**Model type:** Causal language model  
**Languages:** 31 Ugandan languages + English (see language codes above)  

## Intended Uses

### Primary Use Cases
- Translation between English and Ugandan languages
- Translation between Ugandan languages
- Text generation in Ugandan languages
- Question answering in Ugandan languages

### Example Usage

```python
import transformers
import torch

MODEL_PATH = 'Sunbird/Sunflower-14B'
SYSTEM_MESSAGE = 'You are Sunflower, a multilingual assistant made by Sunbird AI who understands all Ugandan languages. You specialise in accurate translations, explanations, summaries and other cross-lingual tasks.'

tokenizer = transformers.AutoTokenizer.from_pretrained(MODEL_PATH)
model = transformers.AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    device_map='auto',
)

instruction = "Translate from Luganda to English: Wano webawaaba?"

messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": instruction}
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

inputs = tokenizer([prompt], return_tensors="pt").to('cuda')
outputs = model.generate(
    **inputs,
    max_new_tokens=500,
    num_beams=5,
    do_sample=True,
    temperature=0.5,
)

response = tokenizer.decode(outputs[0][len(inputs['input_ids'][0]):], skip_special_tokens=True)
print(response)
```

### API Access

For production use, the model is available through the Sunbird AI API at [https://api.sunbird.ai/](https://api.sunbird.ai/)

## Training Details

### Training Data

The model was trained on approximately 750 million characters of text collected from:
- Digitized books and educational materials
- Radio transcripts (500+ hours transcribed)
- Web data from MADLAD-400 and Common Crawl
- Existing multilingual datasets (SALT, FLORES-200, MT560, TICO-19)
- Dictionaries, proverbs, and cultural documents

### Training Procedure

**Stage 1: Continued Pretraining**
- Base model: Qwen 3-14B
- Training time: ~6 hours on 4× H200 GPUs
- Objective: Next token prediction
- Configuration: DeepSpeed ZeRO-3, batch size 32,768 tokens, learning rate 1e-4

**Stage 2: Supervised Fine-Tuning**
- Dataset: ~700 instruction-response pairs
- Method: LoRA (rank 16, alpha 16)
- Training includes: translation, question-answering, summarization
- Loss computed only on response tokens

**Stage 3: Preference Optimization**
- Method: Iterative Reasoning Preference Optimization (RPO)
- Focus: Reducing glitching behavior and hallucinations
- Alpha parameter: 1.0

## Evaluation

### Translation Performance

The model was evaluated on a custom dataset with 100 sentences across 20 practical scenarios (healthcare, banking, education, agriculture, etc.) covering 31 Ugandan languages.

**Average scores across 31 languages:**
- chrF (xx→eng): 0.419
- chrF (eng→xx): 0.366
- BLEU (xx→eng): 19.61

Sunflower-14B achieves the highest accuracy in 24 of 31 languages when averaging bidirectional chrF scores.

### Comparison with Other Models

| Model | chrF (xx→eng) | chrF (eng→xx) |
|-------|---------------|---------------|
| Sunflower-14B | **0.419** | **0.366** |
| Gemini 2.5 Pro | 0.408 | 0.301 |
| GPT-4o | 0.354 | 0.235 |

## Limitations

- Performance varies across languages based on training data availability
- Limited evaluation on tasks beyond translation and basic question-answering
- May generate content that reflects biases present in training data
- Not suitable for critical applications (medical diagnosis, legal advice) without human oversight
- Works best with text similar to training distribution

## Bias and Ethical Considerations

The model was trained on data that includes historical texts, which may contain outdated views. Users should be aware that:
- Some translations use archaic language forms
- Training data filtering focused on removing harmful content but cannot guarantee absence of all biases
- Model outputs should be reviewed by speakers of the target language for critical applications

## Citation

```bibtex
@misc{sunflower2025,
  title={Sunflower: A Regional Approach to Large Language Models for Ugandan Languages},
  author={Akera, Benjamin and Nafula, Evelyn and Yiga, Gilbert and Natukunda, Phionah and Nsumba, Solomon and Muhanguzi, Joel and Namara, Janat and Sekalala, Imran and Walukagga, Patrick and Bainomugisha, Engineer and Mwebaze, Ernest and Quinn, John},
  year={2025},
  publisher={Sunbird AI}
}
```

## Model Card Contact

For questions or issues, contact: info@sunbird.ai