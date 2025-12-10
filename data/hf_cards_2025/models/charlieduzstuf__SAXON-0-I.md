---
base_model:
- brianmatzelle/llama3.1-8b-instruct-political-subreddits
- EryriLabs/DeepSeek-R1-Distill-Llama-UK-Legislation-8B
- charlieduzstuf/SAXON-0
library_name: transformers
tags:
- mergekit
- merge
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64de406ce437d02ce69630b5/voK3ki1j_1EGQeYxc1jAa.png)

# SAXON 0 I

This is an iteration of the SAXON 0 model, I am attempting to minimise the amount of finetuning I need to do by using [mergekit](https://github.com/cg123/mergekit) to let SAXON 0 absorb models trained on Politics and specifically UK Laws etc, since I want the model to be good a those.

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [charlieduzstuf/SAXON-0](https://huggingface.co/charlieduzstuf/SAXON-0) as a base.

### Models Merged

The following models were included in the merge:
* [Llama 3.1 Politics (Dataset scraped from Reddit)](https://huggingface.co/brianmatzelle/llama3.1-8b-instruct-political-subreddits)
* [Deepkseek R1 Llama Distill UK Legislation Expert](https://huggingface.co/EryriLabs/DeepSeek-R1-Distill-Llama-UK-Legislation-8B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: charlieduzstuf/SAXON-0
    #no parameters necessary for base model
  - model: EryriLabs/DeepSeek-R1-Distill-Llama-UK-Legislation-8B
    parameters:
      density: 0.5
      weight: 0.5
  - model: brianmatzelle/llama3.1-8b-instruct-political-subreddits
    parameters:
      density: 0.5
      weight: 0.5

merge_method: ties
base_model: charlieduzstuf/SAXON-0
parameters:
  normalize: false
  int8_mask: true
dtype: float16
```
