---
base_model:
- DreadPoor/Famino-12B-Model_Stock
- TheDrummer/UnslopNemo-12B-v4
- natong19/Mistral-Nemo-Instruct-2407-abliterated
- allura-org/Tlacuilo-12B
- Trappu/Magnum-Picaro-0.7-v2-12b
library_name: transformers
tags:
- mergekit
- merge
license: apache-2.0
---
# VerbaMaxima-12B

![00011-3086291688](https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/-cf4t_CuKPI7iqC9j4aAe.png)

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

An experimental merge for creating a model with solid writing, but with limited "purple" prose.

I've used natong19/Mistral-Nemo-Instruct-2407-abliterated as a base and created an intermediate model using **model_stock**, combining:

- TheDrummer/UnslopNemo-12B-v4
- allura-org/Tlacuilo-12B
- Trappu/Magnum-Picaro-0.7-v2-12b

After that I used **task_arithmetic** to combine this model with DreadPoor/Famino-12B-Model_Stock, but applied a negative lambda as an experiment.

As a result I've got this model that deviates from predictable structure and creates less theatrical experience.
While not immediately punchy, it delivers more nuanced and believable interactions with improved world building.

It's still a highly experimental merge in realm of Mad Science™, so expect some aspects not working as intended, but it may actually have some potential in roleplaying and co-writing, so might be worth trying out.

## Merge Details
### Merge Method

This model was merged using the [Task Arithmetic](https://arxiv.org/abs/2212.04089) merge method using ./verba_medium as a base.

### Models Merged

The following models were included in the merge:
* [DreadPoor/Famino-12B-Model_Stock](https://huggingface.co/DreadPoor/Famino-12B-Model_Stock)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: model_stock
base_model: retokenized_NIA 
models:
  - model: retokenized_UN
  - model: retokenized_TLA
  - model: retokenized_MP
normalize: false
dtype: bfloat16
```

```yaml
merge_method: task_arithmetic
base_model: ./verba_medium
models:
  - model: DreadPoor/Famino-12B-Model_Stock
    parameters: 
      weight: 1.0
parameters:
  lambda: -1.25
normalize: false
dtype: bfloat16
```