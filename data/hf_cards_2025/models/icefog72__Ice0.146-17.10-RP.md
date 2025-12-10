---
license: cc-by-nc-4.0
base_model: []
library_name: transformers
tags:
- mergekit
- merge
---
# Ice0.146-17.10-RP

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Breadcrumbs](https://arxiv.org/abs/2312.06795) merge method using H:\FModels\Mistral-7B-v0.2 as a base.

### Models Merged

The following models were included in the merge:
* F:\FModels\Ice0.143-15.10-RP
* G:\FModels\Ice0.128-15.06-RP
* F:\FModels\Ice0.144-15.10-RP
* H:\FModels\Ice0.130-16.06

### Configuration

The following YAML configuration was used to produce this model:

```yaml

models:
  - model: G:\FModels\Ice0.128-15.06-RP
    parameters:
      weight: 0.5
  - model: F:\FModels\Ice0.144-15.10-RP
    parameters:
      weight: 0.3
  - model: H:\FModels\Ice0.130-16.06
    parameters:
      weight: 0.5
  - model: F:\FModels\Ice0.143-15.10-RP
    parameters:
      weight: 0.7
merge_method: breadcrumbs
base_model: H:\FModels\Mistral-7B-v0.2
parameters:
  lambda: 0.5
  density: 0.9
  gamma: 0.01

dtype: bfloat16
chat_template: "alpaca"


```
