---
base_model:
- Nitral-AI/Captain-Eris_Violet-0.420-Rebased
- Nitral-AI/Captain-Eris_Violet-GRPO-Rebased
library_name: transformers
tags:
- merge
- finetune
- GRPO
- QLORA
- SFT
license: other
language:
- en
---
## Update: The model image itself is now available as an importable character card for SillyTavern. This serves as an example of how to prepare your own card for use with this model.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/nQeKD6pVuoxBfzPszgd8D.png)

## Training Notes: This model was developed using a combination of multi-stage supervised fine-tuning, pre-trained QLoRA adapters, and multi-stage RLHF optimized with GRPO. The final model was created by merging the most promising candidates identified during the process.

# Quants Here: Thanks to Mradermacher <3 [Regular GGUF](https://huggingface.co/mradermacher/Captain-Eris_Violet-GRPO-v0.420-GGUF) [Imatrix GGUF](https://huggingface.co/mradermacher/Captain-Eris_Violet-GRPO-v0.420-i1-GGUF) [4bpw Exl2](https://huggingface.co/Nitrals-Quants/Captain-Eris_Violet-GRPO-v0.420-4bpw-exl2)

### SillyTavern Reasoning Block Parsing Example:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/1dBoM9LYrTYour32oYORP.png)

### SillyTavern Mistral Formatting Example: [Master Import Preset Here](https://huggingface.co/Nitral-AI/Captain-Eris_Violet-GRPO-v0.420/tree/main/ST%20Presets)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/xLd651g-LFUszPhbT_7MA.png)

## Series Comparison:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/aXNoJZ0oc-fU4xyZyBTmk.png)

# The following YAML configuration was used to produce this final version of the model:
```yaml
slices:
  - sources:
      - model: Nitral-AI/Captain-Eris_Violet-0.420-Rebased
        layer_range: [0, 40]
      - model: Nitral-AI/Captain-Eris_Violet-GRPO-Rebased
        layer_range: [0, 40]
merge_method: slerp
base_model: Nitral-AI/Captain-Eris_Violet-0.420-Rebased
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.420
dtype: bfloat16

```