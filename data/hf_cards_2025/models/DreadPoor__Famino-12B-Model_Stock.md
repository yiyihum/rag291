---
library_name: transformers
license: apache-2.0
tags:
- merge
- mergekit
- lazymergekit
base_model:
- cgato/Nemo-12b-Humanize-SFT-v0.2.5-KTO
- DreadPoor/Irix-12B-Model_Stock
- redrix/GodSlayer-12B-ABYSS
- PygmalionAI/Pygmalion-3-12B
---

# Famino

Famino is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [cgato/Nemo-12b-Humanize-SFT-v0.2.5-KTO](https://huggingface.co/cgato/Nemo-12b-Humanize-SFT-v0.2.5-KTO)
* [DreadPoor/Irix-12B-Model_Stock](https://huggingface.co/DreadPoor/Irix-12B-Model_Stock)
* [redrix/GodSlayer-12B-ABYSS](https://huggingface.co/redrix/GodSlayer-12B-ABYSS)
* [PygmalionAI/Pygmalion-3-12B](https://huggingface.co/PygmalionAI/Pygmalion-3-12B)

## 🧩 Configuration

```yamly
models:
  - model: cgato/Nemo-12b-Humanize-SFT-v0.2.5-KTO
  - model: DreadPoor/Irix-12B-Model_Stock
  - model: redrix/GodSlayer-12B-ABYSS
  - model: PygmalionAI/Pygmalion-3-12B
merge_method: model_stock
base_model: DreadPoor/Ward-12B-Model_Stock
normalize: false
int8_mask: true
dtype: bfloat16
```