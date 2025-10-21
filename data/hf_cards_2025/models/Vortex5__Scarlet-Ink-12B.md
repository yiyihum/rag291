---
base_model:
- Vortex5/Vermilion-Sage-12B
- Vortex5/MegaMoon-Karcher-12B
- Vortex5/Dark-Quill-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00155_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/KWJHSZF1k-0kKUjgnut5m.png)

# Scarlet-Ink-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DELLA](https://arxiv.org/abs/2406.11617) merge method using [Vortex5/MegaMoon-Karcher-12B](https://huggingface.co/Vortex5/MegaMoon-Karcher-12B) as a base.

### Models Merged

The following models were included in the merge:
* [Vortex5/Vermilion-Sage-12B](https://huggingface.co/Vortex5/Vermilion-Sage-12B)
* [Vortex5/Dark-Quill-12B](https://huggingface.co/Vortex5/Dark-Quill-12B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

models:
  - model: Vortex5/Vermilion-Sage-12B
    parameters:
      weight: [0.2, 0.5, 0.9, 1.0, 0.95, 0.8, 0.4, 0.2]
      density: 0.55
      epsilon: 0.4
  - model: Vortex5/Dark-Quill-12B
    parameters:
      weight: [0.8, 1.0, 0.9, 0.7, 0.5, 0.4, 0.2, 0.0]
      density: 0.5
      epsilon: 0.4     
merge_method: della_linear
base_model: Vortex5/MegaMoon-Karcher-12B
parameters:
  lambda: 0.94
  normalize: true
dtype: bfloat16
tokenizer:
  source: union

```