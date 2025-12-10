---
base_model: []
library_name: transformers
tags:
- mergekit
- merge
---
# WeirdCompound-v1.6-24b

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Notes

This is a multi-stage merge. There's little method to my madness and I just stopped when I arrived at something that I liked.

Starting point was DepravedCartographer-v1.0-24b with slight changes.

### Changelog

v1.1
* /intermediate/model/B: replaced anthracite-core/Mistral-Small-3.1-24B-Instruct-2503-HF with anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-ChatML

v1.2
* /intermediate/model/B: replaced anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-ChatML with [anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only](https://huggingface.co/anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only) for default tokenizer config.

v1.3
* /intermediate/model/A: replaced TheDrummer/Cydonia-24B-v3 with TheDrummer/Cydonia-24B-v4
* /intermediate/model/A: replaced Doctor-Shotgun/MS3.1-24B-Magnum-Diamond with Doctor-Shotgun/MS3.2-24B-Magnum-Diamond
* /intermediate/model/A: replaced Delta-Vector/Austral-24B-Winton with Delta-Vector/MS3.2-Austral-Winton

v1.4
* /intermediate/model/C: change recipe to use Doctor-Shotgun/MS3.2-24B-Magnum-Diamond and Delta-Vector/MS3.2-Austral-Winton

v1.5

didn't particularly care for v1.4. IMHO v1.3 was better

* /intermediate/model/A: replaced Doctor-Shotgun/MS3.2-24B-Magnum-Diamond with zerofata/MS3.2-PaintedFantasy-24B
* /intermediate/model/C: change recipe to use PocketDoc/Dans-PersonalityEngine-V1.3.0-24b and zerofata/MS3.2-PaintedFantasy-24B

v1.6
* /intermediate/model/A: updated Cydonia to TheDrummer/Cydonia-24B-v4.1
* /intermediate/model/A: updated MS3.2-PaintedFantasy-24B to zerofata/MS3.2-PaintedFantasy-v2-24B
* /intermediate/model/A: removed Delta-Vector/MS3.2-Austral-Winton
* /intermediate/model/A: added Doctor-Shotgun/MS3.2-24B-Magnum-Diamond and CrucibleLab/M3.2-24B-Loki-V1.3
* /intermediate/model/B: changed weight to 0.45
* /intermediate/model/C: replaced zerofata/MS3.2-PaintedFantasy-24B with CrucibleLab/M3.2-24B-Loki-V1.3 and fiddled with weights

### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [TheDrummer/Cydonia-24B-v4](https://huggingface.co/TheDrummer/Cydonia-24B-v4) as a base.

This model was merged using the [SLERP](https://en.wikipedia.org/wiki/Slerp) merge method.

This model was merged using the NuSLERP merge method using /intermediate/model/B as a base.

### Models Merged

* [TheDrummer/Cydonia-24B-v4.1](https://huggingface.co/TheDrummer/Cydonia-24B-v4.1)
* [aixonlab/Eurydice-24b-v3.5](https://huggingface.co/aixonlab/Eurydice-24b-v3.5)
* [PocketDoc/Dans-PersonalityEngine-V1.3.0-24b](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b)
* [zerofata/MS3.2-PaintedFantasy-v2-24B](https://huggingface.co/zerofata/MS3.2-PaintedFantasy-v2-24B)
* [CrucibleLab/M3.2-24B-Loki-V1.3](https://huggingface.co/CrucibleLab/M3.2-24B-Loki-V1.3)
* [Doctor-Shotgun/MS3.2-24B-Magnum-Diamond](https://huggingface.co/Doctor-Shotgun/MS3.2-24B-Magnum-Diamond)
* [anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only](https://huggingface.co/anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only)
* /intermediate/model/A
* /intermediate/model/B
* /intermediate/model/C

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: TheDrummer/Cydonia-24B-v4.1 # Cydonia v4.1
merge_method: model_stock
dtype: bfloat16
models:
  - model: aixonlab/Eurydice-24b-v3.5 # storytelling / RP
  - model: TheDrummer/Cydonia-24B-v4.1 # sprinkle in some extra Cydonia
  - model: PocketDoc/Dans-PersonalityEngine-V1.3.0-24b # Prompt Adherence
  - model: CrucibleLab/M3.2-24B-Loki-V1.3 # Loki
  - model: zerofata/MS3.2-PaintedFantasy-v2-24B  # animu
  - model: Doctor-Shotgun/MS3.2-24B-Magnum-Diamond # claude opus
```
&rarr; `/intermediate/model/A` &rarr;

```yaml
merge_method: slerp
dtype: bfloat16
base_model: anthracite-core/Mistral-Small-3.2-24B-Instruct-2506-Text-Only
models:
  - model: /intermediate/model/A
parameters:
  t: 0.45

```

&rarr; `/intermediate/model/B` &rarr;

```yaml
merge_method: nuslerp
dtype: bfloat16
base_model: /intermediate/model/B
  - model: PocketDoc/Dans-PersonalityEngine-V1.3.0-24b
    parameters:
      weight: 0.4
  - model: CrucibleLab/M3.2-24B-Loki-V1.3
    parameters:
      weight: 0.6
```

&rarr; `/intermediate/model/C` &rarr;

```yaml
merge_method: slerp
dtype: bfloat16
base_model: /intermediate/model/B
models:
  - model: /intermediate/model/C
parameters:
  t: 0.5

```

&rarr; WeirdCompound-v1.6-24b
