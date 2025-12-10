---
base_model:
- taozi555/MN-12B-Mag-Mell-R1-KTO
- Vortex5/MegaMoon-Karcher-12B
- Vortex5/Scarlet-Ink-12B
- Vortex5/Harmonic-Moon-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00159_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/vD-4NFmlm4jytxBJCdI-g.png)
# Velvet-Orchid-12B

This is a multi-stage merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DELLA](https://arxiv.org/abs/2406.11617) merge method using [Vortex5/MegaMoon-Karcher-12B](https://huggingface.co/Vortex5/MegaMoon-Karcher-12B) as a base.

### Models Merged

The following models were included in the merge:
* ./intermediates/First
* [taozi555/MN-12B-Mag-Mell-R1-KTO](https://huggingface.co/taozi555/MN-12B-Mag-Mell-R1-KTO)
* [Vortex5/Scarlet-Ink-12B](https://huggingface.co/Vortex5/Scarlet-Ink-12B)
* [Vortex5/Harmonic-Moon-12B](https://huggingface.co/Vortex5/Harmonic-Moon-12B)
### Configuration

The following YAML configuration was used to produce this model:
<details>
<summary><b>Merge Config</b> (click to expand)</summary>

  ```yaml
name: First  
models:
  - model: Vortex5/Harmonic-Moon-12B
  - model: Vortex5/Scarlet-Ink-12B
merge_method: karcher
dtype: bfloat16
parameters:
  tol: 1e-10
  max_iter: 1200
tokenizer:
  source: union
```
  ```yaml
base_model: Vortex5/MegaMoon-Karcher-12B
dtype: bfloat16
merge_method: della_linear
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 40]
        model: ./intermediates/First
        parameters:
          density: 0.5
          epsilon: 0.4
          weight: [0.9, 0.2, 0.2, 0.2, 0.95, 0.8, 0.4, 0.2]
      - layer_range: [0, 40]
        model: taozi555/MN-12B-Mag-Mell-R1-KTO
        parameters:
          density: 0.5
          epsilon: 0.4
          weight: [0.1, 0.9, 1.0, 0.95, 0.4, 0.4, 0.5, 0.3]
      - layer_range: [0, 40]
        model: Vortex5/MegaMoon-Karcher-12B
parameters:
  lambda: 1.0
  normalize: 1.0
tokenizer: {}
```
</details>