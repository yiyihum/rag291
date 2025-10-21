---
base_model:
- inflatebot/MN-12B-Mag-Mell-R1
- nbeerbower/mistral-nemo-gutenberg-12B-v4
- yamatazen/HMS-Slerp-12B-v2
- PocketDoc/Dans-PersonalityEngine-V1.1.0-12b
library_name: transformers
tags:
- mergekit
- merge
- chatml
language:
- en
- ja
---
![image/png](https://huggingface.co/yamatazen/SnowElf-12B/resolve/main/SnowElf-12B.png?download=true)
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [yamatazen/HMS-Slerp-12B-v2](https://huggingface.co/yamatazen/HMS-Slerp-12B-v2) as a base.

### Models Merged

The following models were included in the merge:
* [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)
* [nbeerbower/mistral-nemo-gutenberg-12B-v4](https://huggingface.co/nbeerbower/mistral-nemo-gutenberg-12B-v4)
* [PocketDoc/Dans-PersonalityEngine-V1.1.0-12b](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.1.0-12b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: yamatazen/HMS-Slerp-12B-v2
models:
  - model: nbeerbower/mistral-nemo-gutenberg-12B-v4
    parameters:
      density: 0.75
      weight: 0.8
  - model: inflatebot/MN-12B-Mag-Mell-R1
    parameters:
      density: 0.6
      weight: 0.6
  - model: PocketDoc/Dans-PersonalityEngine-V1.1.0-12b
    parameters:
      density: 0.5
      weight: 0.3
merge_method: ties
dtype: bfloat16
parameters:
  normalize: true
tokenizer:
  source: union
```