---
base_model:
- Mantis2024/Dirty-Shirley-Writer-v2-9B-Uncensored
- IlyaGusev/gemma-2-9b-it-abliterated
- nerdigent/Darkest-muse-v1-lorablated-v2
library_name: transformers
tags:
- mergekit
- merge
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Mantis2024/Dirty-Shirley-Writer-v2-9B-Uncensored](https://huggingface.co/Mantis2024/Dirty-Shirley-Writer-v2-9B-Uncensored) as a base.

### Models Merged

The following models were included in the merge:
* [IlyaGusev/gemma-2-9b-it-abliterated](https://huggingface.co/IlyaGusev/gemma-2-9b-it-abliterated)
* [nerdigent/Darkest-muse-v1-lorablated-v2](https://huggingface.co/nerdigent/Darkest-muse-v1-lorablated-v2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Mantis2024/Dirty-Shirley-Writer-v2-9B-Uncensored
    # no parameters necessary for base model
  - model: nerdigent/Darkest-muse-v1-lorablated-v2
    parameters:
      density: 0.5
      weight: 0.5
  - model: IlyaGusev/gemma-2-9b-it-abliterated
    parameters:
      density: 0.5
      weight: 0.3
merge_method: ties
base_model: Mantis2024/Dirty-Shirley-Writer-v2-9B-Uncensored
parameters:
  normalize: true
dtype: float16
```
