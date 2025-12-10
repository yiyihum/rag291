---
base_model:
- LatitudeGames/Wayfarer-Large-70B-Llama-3.3
- Sao10K/L3.3-70B-Euryale-v2.3
- crestf411/L3.1-nemotron-sunfall-v0.7.0
- SicariusSicariiStuff/Negative_LLAMA_70B
- EVA-UNIT-01/EVA-LLaMA-3.33-70B-v0.1
- meta-llama/Llama-3.3-70B-Instruct
- OpenBuddy/openbuddy-llama3.3-70b-v24.1-131k
- nbeerbower/llama3.1-kartoffeldes-70B
- tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3
library_name: transformers
tags:
- mergekit
- merge
license: llama3
---
# Genetic Lemonade Final

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65b19c6c638328850e12d38c/0-pxxp_xcaIecQFcaIzFI.png)

Inspired to learn how to merge by the Nevoria series from [SteelSkull](https://huggingface.co/Steelskull).

This model is the second result of the Genetic Lemonade series.

## Model Comparison

Designed for RP and creative writing, all three models are focused around striking a balance between writing style, creativity and intelligence. The basic differences between the models are below.

| Version | Strength | Weakness |
|---------|----------------|----|
| Unleashed | Well balanced | Somewhat censored |
| **Final** | Fully uncensored | Least intelligent |
| Sunset | Well balanced, most intelligent | GPTisms / weakest writing style |

## SillyTavern Settings

[Llam@ception](https://huggingface.co/Konnect1221/The-Inception-Presets-Methception-LLamaception-Qwenception/tree/main/Llam%40ception) recommended for sane defaults if unsure, import them to SillyTavern and they're plug n play.

### Sampler Settings
- Temp: 0.9-1.0
- MinP: 0.03-0.05
- Dry: 0.8, 1.75, 4

Temperature last, neutralize other samplers. This model natively strikes a balance of creativity & intelligence.

### Instruct

Llama-3-Instruct-Names but you will need to uncheck "System same as user".

## Quants

### GGUF

- [Static quants by mradermacher](https://huggingface.co/mradermacher/L3.3-GeneticLemonade-Final-70B-GGUF)
- [iMatrix quants by mradermacher](https://huggingface.co/mradermacher/L3.3-GeneticLemonade-Final-70B-i1-GGUF)

### EXL2

- [4bpw](https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-70B-4bpw-h6-exl2)
- [4.5bpw](https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-70B-4.5bpw-h6-exl2)
- [6bpw](https://huggingface.co/zerofata/L3.3-GeneticLemonade-Final-70B-6bpw-h8-exl2)

## Merge Details
### Merge Method

This model was merged using the [SCE](https://arxiv.org/abs/2408.07990) merge method.

The base aims to build a strong general purpose model using high performing models that are trained on various datasets from different languages / cultures. This is to reduce the chance of the same datasets appearing multiple times to build natural creativity into L3.3
The second merge aims to impart specific RP / creative writing knowledge, again focusing on trying to find high performing models that use or likely use different datasets.

### Base_6_v2
```yaml
models:
  - model: OpenBuddy/openbuddy-llama3.3-70b-v24.1-131k
  - model: nbeerbower/llama3.1-kartoffeldes-70B
  - model: tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3
  - model: SicariusSicariiStuff/Negative_LLAMA_70B
select_topk: .15
merge_method: sce
base_model: meta-llama/Llama-3.3-70B-Instruct
out_dtype: bfloat16
dype: float32
tokenizer:
  source: base
```

### Genetic Lemonade Final

```yaml
models:
  - model: EVA-UNIT-01/EVA-LLaMA-3.33-70B-v0.1
  - model: LatitudeGames/Wayfarer-Large-70B-Llama-3.3
  - model: crestf411/L3.1-nemotron-sunfall-v0.7.0
  - model: SicariusSicariiStuff/Negative_LLAMA_70B
  - model: Sao10K/L3.3-70B-Euryale-v2.3
merge_method: sce
base_model: ./Base_6_v2
select_topk: 0.15
out_dtype: bfloat16
dype: float32
tokenizer:
  source: union
```