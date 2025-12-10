---
license: cc0-1.0
datasets:
- HuggingFaceFW/fineweb
- HuggingFaceFW/fineweb-2
- bigcode/the-stack-v2
language:
- en
- zh
- ru
- de
- ja
- es
- fr
- it
- pt
- pl
- nl
- id
- tr
- cs
- ko
- ar
- hu
- fa
- ro
- vi
- uk
- 'no'
- th
- el
- sv
- da
- sk
- hr
- hi
- lt
- bs
- he
- bn
- sl
- et
- ca
- lv
pipeline_tag: text-generation
---

Nous Consilience 40B is a generative text model, pretrained from scratch in a decentralized fashion over the internet.  
This model is automatically updated every 500 training steps, with the latest checkpoint uploaded here from the [ongoing pretraining dashboard](https://psyche.network/).  

For more information, read the [blog post](https://nousresearch.com/nous-psyche/).

# Model Details

**Model Type:** Decoder-only transformer  
**Parameters:** 40 billion  
**Architecture:** DeepSeek v3 + MLA (Dense version without MoE routers)  
**Pretraining Data:** 20T tokens, Merge of [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb), [FineWeb 2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) and [The Stack v2](https://huggingface.co/datasets/bigcode/the-stack-v2)  
**Training Duration:** TBD  
**Optimizer:** [DisTrO](https://github.com/NousResearch/DisTrO), decentralized version  

# Pretraining Dataset
For training data, we combined FineWeb (14T), FineWeb-2 with some less common languages removed (4T), and The Stack V2 (~.2T, upsampled to 1T tokens). We chose these datasets over more specialized pre-training datasets that aim to purely increase benchmark performance. Our goal with Consilience is to make a true "base" model -- one representative of the entirety of the creative output of humanity, and not merely trying to win the benchmaxxing game.

Additionally, we're training this model continuously without a final data "annealing" step. While annealing helps base models respond more accurately to benchmarks and improves usability, it may potentially constrain creativity and interesting behaviors. Our solution is to simply release both versions: the raw, un-annealed base model first, followed by an annealed version to aid in usability.

# License
As the model representing the vast and diverse creative output of humankind, we choose to release it under a dual license: [**CC0**](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/cc0-1.0.md) by default -- to dedicate it to the public domain -- while also allowing it to be used under the [**MIT** license](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/mit.md) for users who require permissive terms with attribution and warranty disclaimers.