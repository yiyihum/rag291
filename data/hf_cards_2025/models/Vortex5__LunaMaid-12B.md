---
base_model:
- Vortex5/Moonlit-Shadow-12B
- yamatazen/NeonMaid-12B-v2
- Vortex5/Vermilion-Sage-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![lunamaid](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/H8F9goeUxAl7u_JrXxGWz.png)
# 🩵 LunaMaid-12B

This is a multi-stage merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## 🧬 Merge Overview

**LunaMaid-12B** was produced through a **two-stage multi-model merge** using [MergeKit](https://github.com/arcee-ai/mergekit).  
Each stage fuses models with complementary linguistic and stylistic traits to create a cohesive, emotionally nuanced personality.

### 🩵 **Stage 1 — Slerp Merge (Intermediate Model `First`)**

- **Base Model:** [Vortex5/Vermilion-Sage-12B](https://huggingface.co/Vortex5/Vermilion-Sage-12B)  
- **Merged With:** [yamatazen/NeonMaid-12B-v2](https://huggingface.co/yamatazen/NeonMaid-12B-v2)  
- **Method:** Spherical Linear Interpolation (Slerp)  

<details>
<summary><b>Stage 1 Configuration</b></summary>

  ```yaml
name: First
base_model: Vortex5/Vermilion-Sage-12B
models:
  - model: yamatazen/NeonMaid-12B-v2
merge_method: slerp
dtype: bfloat16
parameters:
  normalize: true
  t: [0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.6, 0.5, 0.6, 0.6]
```
</details>



### 🌑 **Merge Method — Karcher Mean Merge (Final Model)**

- **Base Model:** Intermediate output from Stage 1 `./intermediates/First`  
- **Merged With:** [Vortex5/Moonlit-Shadow-12B](https://huggingface.co/Vortex5/Moonlit-Shadow-12B)  
- **Method:** [Karcher Mean](https://en.wikipedia.org/wiki/Karcher_mean) (Riemannian Barycenter)

<details>
<summary><b>Stage 2 Configuration</b></summary>

```yaml
dtype: bfloat16
merge_method: karcher
modules:
  default:
    slices:
      - sources:
          - layer_range: [0, 40]
            model: ./intermediates/First
          - layer_range: [0, 40]
            model: Vortex5/Moonlit-Shadow-12B
parameters:
  max_iter: 9999
  tol: 1e-9
```
</details>

### Models Merged

The following models were included in the merge:
* [Vortex5/Moonlit-Shadow-12B](https://huggingface.co/Vortex5/Moonlit-Shadow-12B)
* [Vortex5/Vermilion-Sage-12B](https://huggingface.co/Vortex5/Vermilion-Sage-12B)
* [yamatazen/NeonMaid-12B-v2](https://huggingface.co/yamatazen/NeonMaid-12B-v2)
* ./intermediates/First
