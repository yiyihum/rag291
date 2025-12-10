---
base_model:
- DreadPoor/Faber-12-Model_Stock
- ohyeah1/Violet-Lyra-Gutenberg-v2
- yamatazen/EtherealAurora-12B-v2
- yamatazen/EtherealAurora-12B-v3
- redrix/patricide-12B-Unslop-Mell-v2
library_name: transformers
tags:
- mergekit
- merge
---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [yamatazen/EtherealAurora-12B-v2](https://huggingface.co/yamatazen/EtherealAurora-12B-v2) as a base.

### Models Merged

The following models were included in the merge:
* [DreadPoor/Faber-12-Model_Stock](https://huggingface.co/DreadPoor/Faber-12-Model_Stock)
* [ohyeah1/Violet-Lyra-Gutenberg-v2](https://huggingface.co/ohyeah1/Violet-Lyra-Gutenberg-v2)
* [yamatazen/EtherealAurora-12B-v3](https://huggingface.co/yamatazen/EtherealAurora-12B-v3)
* [redrix/patricide-12B-Unslop-Mell-v2](https://huggingface.co/redrix/patricide-12B-Unslop-Mell-v2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: DreadPoor/Faber-12-Model_Stock
  - model: ohyeah1/Violet-Lyra-Gutenberg-v2
  - model: redrix/patricide-12B-Unslop-Mell-v2
  - model: yamatazen/EtherealAurora-12B-v3
merge_method: model_stock
base_model: yamatazen/EtherealAurora-12B-v2
normalize: false
int8_mask: true
dtype: bfloat16
```
