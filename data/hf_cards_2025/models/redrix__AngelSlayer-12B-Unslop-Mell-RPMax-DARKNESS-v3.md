---
base_model:
- inflatebot/MN-12B-Mag-Mell-R1
- TheDrummer/UnslopNemo-12B-v4.1
- ArliAI/Mistral-Nemo-12B-ArliAI-RPMax-v1.2
- DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS
library_name: transformers
tags:
- mergekit
- merge
- 12b
- chat
- roleplay
- creative-writing
- DELLA-linear
license: apache-2.0
---
# AngelSlayer-12B-Unslop-Mell-RPMax-DARKNESS-v3
> They say ‘He’ will bring the apocalypse. <span style="color:darkred">She</span> seeks understanding, not destruction.

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

This is more like a v2b, as I got the feedback that the output was boring. I agree, so I tuned up the parameters. I really like the base models by themselves, yet I tuned the parameters too low in v2 to introduce the 'spice' of more creative models. If your experience with this model is negative, try and compare it with v2. This model isn't supposed to be inherently better, just an alternative. Untested right now, as I'm working on new intriguing merges.

Ninth model.
## Merge Details
### Merge Method

This model was merged using the linear [DELLA](https://arxiv.org/abs/2406.11617) merge method using [TheDrummer/UnslopNemo-12B-v4](https://huggingface.co/TheDrummer/UnslopNemo-12B-v4) as a base.

### Models Merged

The following models were included in the merge:
* [DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS](https://huggingface.co/DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS)
* [ArliAI/Mistral-Nemo-12B-ArliAI-RPMax-v1.2](https://huggingface.co/ArliAI/Mistral-Nemo-12B-ArliAI-RPMax-v1.2)
* [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: ArliAI/Mistral-Nemo-12B-ArliAI-RPMax-v1.2
    parameters:
      weight:
        - filter: self_attn
          value: 0.35
        - filter: mlp
          value: 0.2
        - value: 0.25
      density: 0.65
  - model: TheDrummer/UnslopNemo-12B-v4
    parameters:
      weight:
        - filter: self_attn
          value: 0.3
        - filter: mlp
          value: 0.15
        - value: 0.2
      density: 0.6
  - model: inflatebot/MN-12B-Mag-Mell-R1
    parameters:
      weight:
        - filter: self_attn
          value: 0.2
        - filter: mlp
          value: 0.35
        - value: 0.3
      density: 0.75
  - model: DavidAU/MN-GRAND-Gutenberg-Lyra4-Lyra-12B-DARKNESS
    parameters:
      weight:
        - filter: mlp
          value: 0.35
        - value: 0.25
      density: 0.7
base_model: TheDrummer/UnslopNemo-12B-v4
merge_method: della_linear
dtype: bfloat16
chat_template: "chatml"
tokenizer_source: union
parameters:
  normalize: true
  int8_mask: true
  epsilon: 0.05
  lambda: 1


```
