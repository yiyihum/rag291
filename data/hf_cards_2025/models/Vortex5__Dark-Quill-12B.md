---
base_model:
- ReadyArt/Omega-Darker_The-Final-Directive-12B
- Vortex5/MegaMoon-Karcher-12B
- yamatazen/LinearWriter-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00147_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/rPqRFWVR3An1vPgaTS5nv.png)

# Dark-Quill-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DELLA](https://arxiv.org/abs/2406.11617) merge method using [Vortex5/MegaMoon-Karcher-12B](https://huggingface.co/Vortex5/MegaMoon-Karcher-12B) as a base.

### Models Merged

The following models were included in the merge:
* [ReadyArt/Omega-Darker_The-Final-Directive-12B](https://huggingface.co/ReadyArt/Omega-Darker_The-Final-Directive-12B)
* [yamatazen/LinearWriter-12B](https://huggingface.co/yamatazen/LinearWriter-12B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

models:
  - model: yamatazen/LinearWriter-12B
    parameters:
      weight: [0.5, 0.4, 0.4, 0.8, 0.8]
      density: 0.6
      epsilon: 0.2
  - model: ReadyArt/Omega-Darker_The-Final-Directive-12B
    parameters:
      weight: [0.7, 0.7, 0.5, 0.5, 0.5]
      density: 0.5
      epsilon: 0.2
merge_method: della_linear
base_model: Vortex5/MegaMoon-Karcher-12B
parameters:
  lambda: 0.9
  normalize: true
dtype: bfloat16
tokenizer:
 source: yamatazen/LinearWriter-12B

```