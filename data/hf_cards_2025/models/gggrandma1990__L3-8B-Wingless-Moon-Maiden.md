---
base_model:
- NeverSleep/Lumimaid-v0.2-8B
- Sao10K/L3-8B-Lunaris-v1
- SicariusSicariiStuff/Wingless_Imp_8B
library_name: transformers
tags:
- merge
- not-for-all-audiences
---
# gggrandma1990/L3-8B-Wingless-Moon-Maiden
![wmm](https://cdn-uploads.huggingface.co/production/uploads/63c5cab8d5a5cd2043e6178e/hX0YLRVC6Uz20RnHEComb.jpeg)
## Merge Details
My virginal merge of three amazing models using mergekit.
### Merge Method

This model was merged using the [DELLA](https://arxiv.org/abs/2406.11617) merge method using [SicariusSicariiStuff/Wingless_Imp_8B](https://huggingface.co/SicariusSicariiStuff/Wingless_Imp_8B) as a base.

### Models Merged

The following models were included in the merge:
* [NeverSleep/Lumimaid-v0.2-8B](https://huggingface.co/NeverSleep/Lumimaid-v0.2-8B)
* [Sao10K/L3-8B-Lunaris-v1](https://huggingface.co/Sao10K/L3-8B-Lunaris-v1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model:  SicariusSicariiStuff/Wingless_Imp_8B
merge_method: della
models:
  - model: NeverSleep/Lumimaid-v0.2-8B
    parameters:
      weight: 0.5
  - model: Sao10K/L3-8B-Lunaris-v1
    parameters:
      weight: 0.5
parameters:
  density: 0.5
  normalize: true
  epsilon: 0.4
  lambda: 1
tokenizer_source: union
chat_template: "llama3"

```