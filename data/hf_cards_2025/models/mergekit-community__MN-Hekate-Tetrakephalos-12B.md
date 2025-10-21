---
base_model:
- mergekit-community/MN-Hekate-Pyrtania-12B
- mergekit-community/MN-Hekate-Pandamateira-12B
- mergekit-community/MN-Hekate-Noctiluca-12B-v2
- mergekit-community/MN-Hekate-Limenoskopos-12B
- mergekit-community/MN-Nyx-Chthonia-12B
- mistralai/Mistral-Nemo-Instruct-2407
library_name: transformers
tags:
- mergekit
- merge
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) as a base.

### Models Merged

The following models were included in the merge:
* [mergekit-community/MN-Hekate-Pyrtania-12B](https://huggingface.co/mergekit-community/MN-Hekate-Pyrtania-12B)
* [mergekit-community/MN-Hekate-Pandamateira-12B](https://huggingface.co/mergekit-community/MN-Hekate-Pandamateira-12B)
* [mergekit-community/MN-Hekate-Noctiluca-12B-v2](https://huggingface.co/mergekit-community/MN-Hekate-Noctiluca-12B-v2)
* [mergekit-community/MN-Hekate-Limenoskopos-12B](https://huggingface.co/mergekit-community/MN-Hekate-Limenoskopos-12B)
* [mergekit-community/MN-Nyx-Chthonia-12B](https://huggingface.co/mergekit-community/MN-Nyx-Chthonia-12B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float32
out_dtype: bfloat16
merge_method: model_stock
base_model: mistralai/Mistral-Nemo-Instruct-2407
models:
    - model: mergekit-community/MN-Hekate-Limenoskopos-12B
      parameters:
        weight:
          - filter: mlp
            value: [2, 1]
          - value: 1
    - model: mergekit-community/MN-Hekate-Noctiluca-12B-v2
      parameters:
        weight:
          - filter: mlp
            value: [1, 2]
          - value: 1
    - model: mergekit-community/MN-Hekate-Pandamateira-12B
      parameters:
        weight:
          - filter: mlp
            value: [1, 2]
          - value: 1
    - model: mergekit-community/MN-Hekate-Pyrtania-12B
      parameters:
        weight:
          - filter: mlp
            value: [2, 1]
          - value: 1
    - model: mergekit-community/MN-Nyx-Chthonia-12B
      parameters:
        weight:
          - filter: lm_head
            value: 0
          - value: [1, 0.5]
```
