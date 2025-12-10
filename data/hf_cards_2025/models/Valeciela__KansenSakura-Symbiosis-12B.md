---
license: apache-2.0
language:
- en
base_model:
- Retreatcost/KansenSakura-Erosion-RP-12b
- Retreatcost/KansenSakura-Zero-RP-12b
- Retreatcost/KansenSakura-Eclipse-RP-12b
- Retreatcost/KansenSakura-Radiance-RP-12b
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
# KansenSakura-Symbiosis-12B

![image/png](https://huggingface.co/Valeciela/KansenSakura-Symbiosis-12B/resolve/main/Symbiosis.png)

<audio controls src="https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/-dqfy9EV2T9HxT8NfWq78.mpga"></audio>

You know how in some video games your starting gear or character can get a huge upgrade if you bring it all the way to the end of the game? This is sort of like that.

> Experimental. Use at your own risk.

# GGUF:
[Standard](https://huggingface.co/Valeciela/KansenSakura-Symbiosis-12B-GGUF)<br>
[Q6_K_XL](https://huggingface.co/Valeciela/KansenSakura-Symbiosis-12B-Q6_K_XL-GGUF)

-----------------------


## Merge Details
### Merge Method

This model was merged using the [Multi-SLERP](https://goddard.blog/posts/multislerp-wow-what-a-cool-idea) merge method using [Retreatcost/KansenSakura-Zero-RP-12b](https://huggingface.co/Retreatcost/KansenSakura-Zero-RP-12b) as a base.

### Models Merged

The following models were included in the merge:
* [Retreatcost/KansenSakura-Erosion-RP-12b](https://huggingface.co/Retreatcost/KansenSakura-Erosion-RP-12b)
* [Retreatcost/KansenSakura-Eclipse-RP-12b](https://huggingface.co/Retreatcost/KansenSakura-Eclipse-RP-12b)
* [Retreatcost/KansenSakura-Radiance-RP-12b](https://huggingface.co/Retreatcost/KansenSakura-Radiance-RP-12b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Retreatcost/KansenSakura-Eclipse-RP-12b
    parameters:
      weight: 0.5
  - model: Retreatcost/KansenSakura-Radiance-RP-12b
    parameters:
      weight: 0.5
  - model: Retreatcost/KansenSakura-Erosion-RP-12b
    parameters:
      weight: 0.5
base_model: Retreatcost/KansenSakura-Zero-RP-12b
merge_method: multislerp
tokenizer:
  source: base
chat_template: chatml
parameters:
  normalize: true
dtype: bfloat16
```
