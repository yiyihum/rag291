---
base_model:
- inflatebot/MN-12B-Mag-Mell-R1
- NeverSleep/Lumimaid-v0.2-12B
- Elizezen/Himeyuri-v0.1-12B
- PocketDoc/Dans-PersonalityEngine-V1.1.0-12b
- nbeerbower/Mistral-Nemo-12B-abliterated-LORA
- cyberagent/Mistral-Nemo-Japanese-Instruct-2408
- nbeerbower/mistral-nemo-gutenberg-12B-v4
library_name: transformers
tags:
- mergekit
- merge
- chatml
language:
- en
- ja
---
![image/png](https://huggingface.co/yamatazen/Aurora-SCE-12B-v2/resolve/main/Aurora-SCE-12B-v2.png?download=true)
This is a ChatML model.
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [SCE](https://arxiv.org/abs/2408.07990) merge method using [PocketDoc/Dans-PersonalityEngine-V1.1.0-12b](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.1.0-12b) + [nbeerbower/Mistral-Nemo-12B-abliterated-LORA](https://huggingface.co/nbeerbower/Mistral-Nemo-12B-abliterated-LORA) as a base.

### Models Merged

The following models were included in the merge:
* [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)
* [NeverSleep/Lumimaid-v0.2-12B](https://huggingface.co/NeverSleep/Lumimaid-v0.2-12B)
* [Elizezen/Himeyuri-v0.1-12B](https://huggingface.co/Elizezen/Himeyuri-v0.1-12B)
* [cyberagent/Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408)
* [nbeerbower/mistral-nemo-gutenberg-12B-v4](https://huggingface.co/nbeerbower/mistral-nemo-gutenberg-12B-v4)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: PocketDoc/Dans-PersonalityEngine-V1.1.0-12b+nbeerbower/Mistral-Nemo-12B-abliterated-LORA
models:
  - model: nbeerbower/mistral-nemo-gutenberg-12B-v4
  - model: Elizezen/Himeyuri-v0.1-12B
  - model: inflatebot/MN-12B-Mag-Mell-R1
  - model: NeverSleep/Lumimaid-v0.2-12B
  - model: cyberagent/Mistral-Nemo-Japanese-Instruct-2408
merge_method: sce
dtype: bfloat16
parameters:
  normalize: true
  select_topk: 0.5
```