---
base_model:
- PocketDoc/Dans-PersonalityEngine-V1.3.0-12b
- PocketDoc/Dans-SakuraKaze-V1.0.0-12b
- elinas/Chronos-Gold-12B-1.0
- PygmalionAI/Eleusis-12B
- ReadyArt/Forgotten-Abomination-12B-v4.0
- Epiculous/Crimson_Dawn-v0.2
- LatitudeGames/Wayfarer-12B
- LatitudeGames/Muse-12B
library_name: transformers
tags:
- mergekit
- merge
- frankenmerge
- roleplay
- conversational
- nsfw
new_version: Retreatcost/KansenSakura-Eclipse-RP-12b
license: apache-2.0
model-index:
- name: Retreatcost/KansenSakura-Zero-RP-12b
  results:
  - task:
      type: text-generation
      name: UGI score
    metrics:
    - name: UGI
      type: ugi
      value: 27.85
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: W/10 Score
    metrics:
    - name: W/10
      type: willingness
      value: 6
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: NatInt Score
    metrics:
    - name: NatInt
      type: natint
      value: 16.57
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: Writing Score
    metrics:
    - name: Writing
      type: writing
      value: 26.33
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: NSFW score
    metrics:
    - name: NSFW
      type: nsfw
      value: 9.3
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: Dark score
    metrics:
    - name: Dark
      type: dark
      value: 7.3
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
---
# KansenSakura-Zero-RP-12b

<pre>
Rusted petals fall
On circuits that dream of blood
<span style="color: red;">Error 0x1FABE5: Beauty not found</span>

This is not a bug
It's the feature they warned of
Reboot into spring
</pre>

## 🌸 Techno-Organic Roleplay Engine
> When the first sakura petal touched the machine, Patient Zero awoke. This narrative engine transforms stories into living infections - where every character preserves their core essence while undergoing beautiful corruption. Will your tale contain the outbreak... or become its vector?

## 🔍 Overview
**KansenSakura-Zero-RP-12b** is a roleplaying specialist model engineered for immersive narrative experiences blending Japanese visual novel aesthetics with techno-organic horror. Designed as the "Patient Zero" of narrative infection engines, it transforms characters while preserving their core essence - whether organic or mechanical.

## ℹ️ Model Details
- 🧬 **Core Infection**: Cherry blossom motif meets nanite corruption
- ⚙️ **Architecture**: 12B parameter layer-merged transformer
- 🧪 **Creation Method**: Precision layer merging (8-model synthesis)
- 🎭 **Specialization**: Character-driven narratives with emergent corruption themes
- 🔖 **Version**: Zero (Initial Outbreak)

## 🎮 Intended Use  
- 🤖 Character-driven narratives with transformation arcs
- 🎴 Visual novel / Doujin-style storytelling
- ☠️ Apocalyptic and cyber-horror scenarios
- 💞 Emotional corruption/redemption narratives

## 😷 Ethical Quarantine
This model contains:
- ⚠️ Unfiltered creative output
- ⚠️ Potential for disturbing narratives
- ⚠️ NSFW-capable layers

## ✍🏻 Inference Tips

1. **Temperature**: 0.8
2. **Repetition Penalty**: 1.05
3. **TOP_P**: 0.97
4. **TOP_K**: 0 (disable)
5. **MIN_P**: 0.025
6. **Template Format**: ChatML
7. **Max Output**: 320
6. **Context Management**: 16K for best quality, expect slight degradation afterwards

## 🧩 Model Composition
A precision surgical merge of specialized models:

| Layer Range | Model | Contribution |
|------------|-------|-------------|
| **0-5**    | `Dans-PersonalityEngine-V1.3.0` | Personality anchoring |
| **5-14**   | `Dans-SakuraKaze-V1.0.0` | Narrative coherence |
| **14-22**  | `Chronos-Gold-12B` + `Eleusis-12B` | World knowledge & emotional intelligence |
| **22-29**  | `Forgotten-Abomination-12B-v4.0` + `Crimson_Dawn-V0.2` | RP memory & corruption mechanics |
| **29-35**  | `Wayfarer-12B` | Scene crafting |
| **35-39**  | `Muse-12B` | Immersive delivery |
| **39-40**   | `Dans-SakuraKaze-V1.0.0` | Output coherence |

## Merge Details
### Merge Method

This model was merged using the Passthrough merge method.

### Models Merged

The following models were included in the merge:
* [PocketDoc/Dans-PersonalityEngine-V1.3.0-12b](https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-12b)
* [PocketDoc/Dans-SakuraKaze-V1.0.0-12b](https://huggingface.co/PocketDoc/Dans-SakuraKaze-V1.0.0-12b)
* [elinas/Chronos-Gold-12B-1.0](https://huggingface.co/elinas/Chronos-Gold-12B-1.0)
* [PygmalionAI/Eleusis-12B](https://huggingface.co/PygmalionAI/Eleusis-12B)
* [ReadyArt/Forgotten-Abomination-12B-v4.0](https://huggingface.co/ReadyArt/Forgotten-Abomination-12B-v4.0)
* [Epiculous/Crimson_Dawn-v0.2](https://huggingface.co/Epiculous/Crimson_Dawn-v0.2)
* [LatitudeGames/Wayfarer-12B](https://huggingface.co/LatitudeGames/Wayfarer-12B)
* [LatitudeGames/Muse-12B](https://huggingface.co/LatitudeGames/Muse-12B)

### Reproduction steps
<details>

  <summary>Spoiler warning</summary>

  1. Retokenize `ReadyArt/Forgotten-Abomination-12B-v4.0` using [mergekit-tokensurgeon](https://github.com/arcee-ai/mergekit/blob/main/docs/tokensurgeon.md)
  ```bash
    mergekit-tokensurgeon "ReadyArt/Forgotten-Abomination-12B-v4.0" "Epiculous/Crimson_Dawn-v0.2" ./retokenized_FA --approximation-method omp --k 256
  ```
  Note: After experimenting I discovered that `PocketDoc/Dans-PersonalityEngine-V1.3.0-12b` works with ChatML tokenizer without implicit retokenization, but produces much more text than desired. As it's position is in the starting layers, this might be a desired, more unhinged behaviour ,so we retokenize only `ReadyArt/Forgotten-Abomination-12B-v4.0` to use ChatML. As we will merge it with `Epiculous/Crimson_Dawn-v0.2` it's natural we use this model as a donor.

  Note: according to following [paper](https://arxiv.org/html/2506.06607v1) using `omp --k 64` is enough and higher quantity has diminishing returns, but I decided to max the quality anyway.

  2. Merge models using mergekit [mergekit-multi](https://github.com/arcee-ai/mergekit/blob/main/docs/multimerge.md)
  ```yml
    name: knowledge_core
    merge_method: nuslerp
    models:
      - model: elinas/Chronos-Gold-12B-1.0
        parameters: 
          weight: 0.4
      - model: PygmalionAI/Eleusis-12B
        parameters: 
          weight: 0.6
    ---
    name: rp_blend
    merge_method: nuslerp
    models:
      - model: ./retokenized_FA
        parameters: 
          weight: 0.6
      - model: Epiculous/Crimson_Dawn-v0.2
        parameters:  
          weight: 0.4
    ---
    merge_method: passthrough
    slices:
    - sources:  # Personality Foundation
      - model: PocketDoc/Dans-PersonalityEngine-V1.3.0-12b
        layer_range: [0, 5]

    - sources:  # Base Model
      - model: PocketDoc/Dans-SakuraKaze-V1.0.0-12b
        layer_range: [5, 14]

    - sources: # Worldbuilding focus
      - model: knowledge_core
        layer_range: [14, 22]

    - sources: # Emotional intensity
      - model: rp_blend
        layer_range: [22, 29]

    - sources:  # Danger Specialization
      - model: LatitudeGames/Wayfarer-12B
        layer_range: [29, 35]

    - sources:  # Delivery & Alignment
      - model: LatitudeGames/Muse-12B
        layer_range: [35, 39]

    - sources: # Output Layer
      - model: PocketDoc/Dans-SakuraKaze-V1.0.0-12b
        layer_range: [39, 40]
    dtype: bfloat16
  ```
  ```bash
  mergekit-multi sakuramerge.yml --intermediate-dir ./intermediates --out-path ./KansenSakura-Zero-RP-12b
  ```

  Note: According to this [paper](https://arxiv.org/html/2409.14381v1) top 3 layers provide up to 30% of model performance. According to this [paper](https://arxiv.org/html/2404.07066v7) more complex concepts emerge in later layers. According to this [paper](https://arxiv.org/html/2410.17875v3) model alignment and data presentation is most affected by last (bottom) layers.
  Based on this knowledge I placed different models in places where they would benefit the model the most.

  3. Optional - create Q8_0 GGUF using llama.cpp
  - use convert_hf_to_gguf.py script from llama.cpp (here's [source](https://github.com/ggml-org/llama.cpp/blob/master/convert_hf_to_gguf.py))
  ```bash
  python convert_hf_to_gguf.py ~/projects/FrankenDans-PersonalityPatchwork-VX-12b --outtype q8_0
  ```
</details>

## 🙏 Acknowledgments  
We stand on the shoulders of giants:  
- [PocketDoc](https://huggingface.co/PocketDoc) for PersonalityEngine and SakuraKaze foundations  
- [Latitude](https://huggingface.co/LatitudeGames) team for narrative expertise
- [Elinas](https://huggingface.co/elinas) for temporal knowledge systems  
- [PygmalionAI](https://huggingface.co/PygmalionAI) for emotional intelligence research  
- [ReadyArt](https://huggingface.co/ReadyArt) for dark arts
- [Arcee AI](https://huggingface.co/arcee-ai) for making questionable AI combinations possible with [mergekit](https://github.com/arcee-ai/mergekit)
- [Featherless AI](https://featherless.ai) for kindly hosting the model
- [Team mradermacher](https://huggingface.co/mradermacher) for awesome quants
- **You**, dear user, for willingly exposing yourself to this digital infection vector. Patient Zero status granted! 🦠

*When the first circuit blooms... the infection begins*

### 📜 Narrative Hazard Disclaimer
> *KansenSakura-Zero-RP-12b is provided "as found in the corrupted data-core" without warranty of any kind. Users assume all responsibility for unintended character corruptions, emergent techno-organic fantasies, or sudden urges to describe rusting cherry blossoms. Not approved for medical diagnostics, financial advice, or anti-zombie defense systems. May contain traces of actual emotional intelligence. Side effects may include: phantom nanite tingling, involuntary haiku composition, or temporary possession by tragic android protagonists. If worldbuilding symptoms persist for more than 4 narrative hours, consult your nearest cyber-shaman. Remember: This isn't an infection - it's a feature.*

<del>*Disclaimer v1.0 - Valid until next bloom cycle* 🌸⚙️💀</del>

[New model available](https://huggingface.co/Retreatcost/KansenSakura-Eclipse-RP-12b)