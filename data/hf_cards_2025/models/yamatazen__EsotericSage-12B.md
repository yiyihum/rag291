---
base_model:
- yamatazen/ForgottenMaid-12B
- yamatazen/LinearWriter-12B
library_name: transformers
tags:
- mergekit
- merge
- nearswap
language:
- en
- ja
---
![image/png](https://huggingface.co/yamatazen/EsotericSage-12B/resolve/main/EsotericSage-12B.png?download=true)
# EsotericSage-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [NearSwap](https://huggingface.co/alchemonaut/QuartetAnemoi-70B-t0.0001) merge method using [yamatazen/LinearWriter-12B](https://huggingface.co/yamatazen/LinearWriter-12B) as a base.

### Models Merged

The following models were included in the merge:
* [yamatazen/ForgottenMaid-12B](https://huggingface.co/yamatazen/ForgottenMaid-12B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: nearswap
dtype: bfloat16
out_dtype: bfloat16
base_model: yamatazen/LinearWriter-12B
models:
  - model: yamatazen/ForgottenMaid-12B
parameters:
  t: [0.0001, 0.0003, 0.0005, 0.0003, 0.0001]
```