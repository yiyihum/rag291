---
base_model:
- yamatazen/NeonMaid-12B-v2
- Epiculous/Violet_Twilight-v0.2
- Vortex5/Moonlit-Shadow-12B
- LatitudeGames/Wayfarer-12B
- anthracite-org/magnum-v4-12b
- Vortex5/Harmonic-Moon-12B
- SicariusSicariiStuff/Impish_Nemo_12B
- LatitudeGames/Muse-12B
- inflatebot/MN-12B-Mag-Mell-R1
- Vortex5/Crystal-Moon-12B
- Vortex5/Lunar-Nexus-12B
- Nitral-AI/Captain-Eris_Violet-V0.420-12B
- Vortex5/Poetic-Rune-12B
- nothingiisreal/MN-12B-Celeste-V1.9
- crestf411/MN-Slush
- PocketDoc/Dans-SakuraKaze-V1.0.0-12b
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00137_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/_n355Q-gQG-NFHX4naeiT.png)

# MegaMoon-Karcher-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Karcher Mean](https://en.wikipedia.org/wiki/Karcher_mean) merge method.

### Models Merged

The following models were included in the merge:
* [yamatazen/NeonMaid-12B-v2](https://huggingface.co/yamatazen/NeonMaid-12B-v2)
* [Epiculous/Violet_Twilight-v0.2](https://huggingface.co/Epiculous/Violet_Twilight-v0.2)
* [Vortex5/Moonlit-Shadow-12B](https://huggingface.co/Vortex5/Moonlit-Shadow-12B)
* [LatitudeGames/Wayfarer-12B](https://huggingface.co/LatitudeGames/Wayfarer-12B)
* [anthracite-org/magnum-v4-12b](https://huggingface.co/anthracite-org/magnum-v4-12b)
* [Vortex5/Harmonic-Moon-12B](https://huggingface.co/Vortex5/Harmonic-Moon-12B)
* [SicariusSicariiStuff/Impish_Nemo_12B](https://huggingface.co/SicariusSicariiStuff/Impish_Nemo_12B)
* [LatitudeGames/Muse-12B](https://huggingface.co/LatitudeGames/Muse-12B)
* [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)
* [Vortex5/Crystal-Moon-12B](https://huggingface.co/Vortex5/Crystal-Moon-12B)
* [Vortex5/Lunar-Nexus-12B](https://huggingface.co/Vortex5/Lunar-Nexus-12B)
* [Nitral-AI/Captain-Eris_Violet-V0.420-12B](https://huggingface.co/Nitral-AI/Captain-Eris_Violet-V0.420-12B)
* [Vortex5/Poetic-Rune-12B](https://huggingface.co/Vortex5/Poetic-Rune-12B)
* [nothingiisreal/MN-12B-Celeste-V1.9](https://huggingface.co/nothingiisreal/MN-12B-Celeste-V1.9)
* [crestf411/MN-Slush](https://huggingface.co/crestf411/MN-Slush)
* [PocketDoc/Dans-SakuraKaze-V1.0.0-12b](https://huggingface.co/PocketDoc/Dans-SakuraKaze-V1.0.0-12b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

models:
  - model: LatitudeGames/Muse-12B
  - model: anthracite-org/magnum-v4-12b
  - model: yamatazen/NeonMaid-12B-v2
  - model: SicariusSicariiStuff/Impish_Nemo_12B
  - model: crestf411/MN-Slush
  - model: Epiculous/Violet_Twilight-v0.2
  - model: LatitudeGames/Wayfarer-12B
  - model: inflatebot/MN-12B-Mag-Mell-R1
  - model: nothingiisreal/MN-12B-Celeste-V1.9
  - model: Nitral-AI/Captain-Eris_Violet-V0.420-12B
  - model: PocketDoc/Dans-SakuraKaze-V1.0.0-12b  
  - model: Vortex5/Poetic-Rune-12B
  - model: Vortex5/Lunar-Nexus-12B
  - model: Vortex5/Harmonic-Moon-12B
  - model: Vortex5/Crystal-Moon-12B
  - model: Vortex5/Lunar-Nexus-12B
  - model: Vortex5/Moonlit-Shadow-12B
merge_method: karcher
dtype: bfloat16
parameters:
  tol: 1e-10
  max_iter: 999
tokenizer:
  source: union

```