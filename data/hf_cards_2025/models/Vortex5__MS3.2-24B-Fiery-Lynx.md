---
base_model:
- ConicCat/Mistral-Small-3.2-AntiRep-24B
- CrucibleLab/M3.2-24B-Loki-V1.3
- zerofata/MS3.2-PaintedFantasy-v2-24B
- Gryphe/Codex-24B-Small-3.2
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00151_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/5Navdd8CgnhevaBlzT0sZ.png)

# MS3.2-24B-Fiery-Lynx

Instruct template: Mistral V7

## Merge Details
### Merge Method

This model was merged using the [Linear DELLA](https://arxiv.org/abs/2406.11617) merge method using [ConicCat/Mistral-Small-3.2-AntiRep-24B](https://huggingface.co/ConicCat/Mistral-Small-3.2-AntiRep-24B) as a base.

### Models Merged

The following models were included in the merge:
* [CrucibleLab/M3.2-24B-Loki-V1.3](https://huggingface.co/CrucibleLab/M3.2-24B-Loki-V1.3)
* [zerofata/MS3.2-PaintedFantasy-v2-24B](https://huggingface.co/zerofata/MS3.2-PaintedFantasy-v2-24B)
* [Gryphe/Codex-24B-Small-3.2](https://huggingface.co/Gryphe/Codex-24B-Small-3.2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

models:
  - model: zerofata/MS3.2-PaintedFantasy-v2-24B
    parameters:
      weight: 0.2
      density: 0.5
      epsilon: 0.4
  - model: Gryphe/Codex-24B-Small-3.2
    parameters:
      weight: 0.2 
      density: 0.5
      epsilon: 0.4
  - model: CrucibleLab/M3.2-24B-Loki-V1.3
    parameters:
      weight: 0.4
      density: 0.4
      epsilon: 0.3
merge_method: della_linear
base_model: ConicCat/Mistral-Small-3.2-AntiRep-24B
parameters:
  lambda: 0.9
  normalize: true
dtype: bfloat16
tokenizer:
 source: union

```