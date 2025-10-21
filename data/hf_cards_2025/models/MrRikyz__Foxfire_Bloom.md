---
base_model:
- SicariusSicariiStuff/Impish_Nemo_12B
- D1rtyB1rd/Egregore-Alice-RP-NSFW-12B
- MrRikyz/Impish-Irix-Kitsune
- Retreatcost/KansenSakura-Radiance-RP-12b
library_name: transformers
tags:
- mergekit
- merge
- RP
- NSFW
- roleplay
---
# merged
# 🛑 Premise

Ah, another one escapes the workshop! Greetings, fellow roleplayer or... whatever you are. Foxfire Bloom my third public creation, i hope you like it and it satisfies your roleplay needs
i merge models for myself but hope they are good and you find them good too

# Data
i didn't add any new data so nothing, I just merged the models

# 🧪 Intended Use

This model is designed mainly for:

- Roleplay and creative writing

# 😷 Ethical Containment
This model can:

- ⚠️ Generating unfiltered creative content
- ⚠️ Producing potentially disturbing narratives
- ⚠️ Creating NSFW content


# Quants
Static GGUF Quant here [Static](https://huggingface.co/mradermacher/Foxfire_Bloom-GGUF)

imatrix quants are available here [Imatrix]( https://huggingface.co/mradermacher/Foxfire_Bloom-i1-GGUF)

Many thanks to [mradermacher](https://huggingface.co/mradermacher) for providing them!
## Merge Details

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using SicariusSicariiStuff/Impish_Nemo_12B as a base.

### Models Merged

The following models were included in the merge:
* SicariusSicariiStuff/Impish_Nemo_12B
* D1rtyB1rd/Egregore-Alice-RP-NSFW-12B
* Retreatcost/KansenSakura-Radiance-RP-12b
* MrRikyz/Impish-Irix-Kitsune

# ⚖️ License
Follow the licensing terms of each merged model:

Each source model’s license applies

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: SicariusSicariiStuff/Impish_Nemo_12B
dtype: bfloat16
merge_method: ties
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 40]
        model: Retreatcost/KansenSakura-Radiance-RP-12b
        parameters:
          density: 0.4
          weight: 0.25
      - layer_range: [0, 40]
        model: MrRikyz/Impish-Irix-Kitsune
        parameters:
          density: 0.5
          weight: 0.35
      - layer_range: [0, 40]
        model: SicariusSicariiStuff/Impish_Nemo_12B
        parameters:
          density: 0.5
          weight: 0.3
      - layer_range: [0, 40]
        model: D1rtyB1rd/Egregore-Alice-RP-NSFW-12B
        parameters:
          density: 0.6
          weight: 0.45
parameters:
  lamda: 0.85
  normalize: 1.0
tokenizer:
  source: base
```

# ✨ Acknowledgements

Thanks to the authors of the original models for their incredible work:

- SicariusSicariiStuff for Impish Nemo 12B

- Retreatcost for KansenSakura-Radiance-RP-12b

- D1rtyB1rd for Egregore-Alice-RP-NSFW-12B

- MrRikyz for Impish-Irix-Kitsune (don't know why i add myself but okay)