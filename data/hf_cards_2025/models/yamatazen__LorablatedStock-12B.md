---
library_name: transformers
tags:
- mergekit
- merge
- lorablated
language:
- en
- ja
base_model:
- yamatazen/HMS-Fusion-12B-Lorablated
- yamatazen/ForgottenMaid-12B-Lorablated
- yamatazen/FusionEngine-12B-Lorablated
---
![image/png](https://huggingface.co/yamatazen/LorablatedStock-12B/resolve/main/LorablatedStock-12B.png?download=true)
# LorablatedStock-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using C:\Users\yamat\Desktop\text-generation-webui\user_data\models\HMS-Fusion-12B-Lorablated as a base.

### Models Merged

The following models were included in the merge:
* C:\Users\yamat\Desktop\text-generation-webui\user_data\models\ForgottenMaid-12B-Lorablated
* C:\Users\yamat\Desktop\text-generation-webui\user_data\models\FusionEngine-12B-Lorablated

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: model_stock
dtype: bfloat16
out_dtype: bfloat16
base_model: C:\Users\yamat\Desktop\text-generation-webui\user_data\models\HMS-Fusion-12B-Lorablated
models:
  - model: C:\Users\yamat\Desktop\text-generation-webui\user_data\models\ForgottenMaid-12B-Lorablated
  - model: C:\Users\yamat\Desktop\text-generation-webui\user_data\models\FusionEngine-12B-Lorablated
```