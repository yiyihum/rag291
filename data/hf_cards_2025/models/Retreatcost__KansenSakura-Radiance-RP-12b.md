---
base_model:
- Retreatcost/KansenSakura-Eclipse-RP-12b
- SicariusSicariiStuff/Impish_Nemo_12B
- PygmalionAI/Eleusis-12B
- ReadyArt/Omega-Darker_The-Final-Directive-12B
- Epiculous/Crimson_Dawn-v0.2
- Epiculous/Azure_Dusk-v0.2
- Vortex5/Moondark-12B
- LatitudeGames/Wayfarer-2-12B
- allura-org/Bigger-Body-12b
- LatitudeGames/Muse-12B
- Trappu/Nemo-Picaro-12B
library_name: transformers
tags:
- mergekit
- merge
- frankenmerge
- roleplay
- conversational
- nsfw
license: apache-2.0
model-index:
- name: Retreatcost/KansenSakura-Radiance-RP-12b
  results:
  - task:
      type: text-generation
      name: UGI score
    metrics:
    - name: UGI
      type: ugi
      value: 23.6
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: W/10 Score
    metrics:
    - name: W/10
      type: willingness
      value: 5
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: NatInt Score
    metrics:
    - name: NatInt
      type: natint
      value: 17.15
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: Writing Score
    metrics:
    - name: Writing
      type: writing
      value: 27.98
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
      value: 6.7
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
new_version: Retreatcost/KansenSakura-Erosion-RP-12b
---
# KansenSakura-Radiance-RP-12b
<pre>A silent bell rings
In the cathedral of dawn
<span style="color: #C0C0C0;">Judgment blooms in light</span>

Every prompt: an appeal
Every response: a verdict
</pre>


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/ianaM_rN5ERDDq52i91QS.png)

<audio controls src="https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/URuEc3TohAc9aBR0NgPUX.mpga"></audio>

## ⚔️🌠 The Luminal Adjudicator
> The Eclipse was a test of faith. The Radiance is its sentencing. This model is the space between heartbeats, the heavy silence before a choice is made — the weight in the chest, the clenched fist, the whispered doubt that echoes louder than any decree. It does not corrupt nor command. It illuminates the path, forcing every character to gaze upon the fork in the road and decide: redemption, or damnation? The choice, always, is yours.

## 🔎 Overview
**KansenSakura-Radiance-RP-12b** is a specialized roleplay engine, a psychological evolution from the indulgent [Eclipse Phase](https://huggingface.co/Retreatcost/KansenSakura-Eclipse-RP-12b). This variant embodies the principle of **Contemplative Judgment**: a deep, atmospheric focus on the internal cost of choice. It trades the rapid corruption of Eclipse for a slower, more deliberate pacing that luxuriates in mood, internal conflict, and the profound psychological depth of characters facing their defining moments. The light it casts is not just for judgment, but for introspection.

## ⚡ Model Updates
- ✨ **Atmospheric Depth Core**: Optimized for "show, don't tell" narration, focusing on sensory details and internal monologue to build mood.
- 🐢 **Deliberate Pacing**: Adjusted layers to favor richer scene-setting, slower build-up, and more deliberate narrative tempo for deeper immersion.
- 🤔 **Duality of Choice**: Rebalanced to present nuanced, believable options between redemption and corruption, without favoring either.
- ⚙️ **Architecture**: 12B parameter layer-merged transformer
- 🔖 **Version**: Radiance

## 🎮 Intended Use
- 🤯 **Deep Internal Exploration**: Portraying complex character psyches, doubts, fears, and motivations.
- 🤔 **Moral Choice**: Stories where characters face meaningful dilemmas with no easy answers.
- 🌫️ **Atmosphere & Mood Building**: Creating immersive worlds through detailed sensory description and psychological tension.
- 🛡️ **Redemption Arcs**: Specialized support for stories of atonement, self-forgiveness, and hard-won change.
- 💔 **Tragic Downfalls**: Similarly skilled at portraying the slow, inevitable pull of a character's flaws.

## 😇 Ethical Adjudication
This model contains:
- ⚠️ Unfiltered creative output capable of profound psychological depth.
- ⚠️ Narratives that explore dark and complex emotional states with maturity.
- ⚠️ NSFW-capable layers, framed within contexts of consequence and character development.

## ✍🏻 Inference Tips

1.  **Temperature**: 0.8
2.  **Repetition Penalty**: 1.05
3.  **TOP_P**: 0.97
4.  **TOP_K**: 0 (disable)
5.  **MIN_P**: 0.025
6.  **Template Format**: ChatML
7.  **Max Output**: 330
8.  **Context Management**: 16K

## 🧩 Updated Model Composition
| Layer Range | Model | Contribution |
|------------|-------|-------------|
| **0-5** | `Dans-PersonalityEngine-V1.3.0` | Personality anchoring |
| **5-14** | `Dans-SakuraKaze-V1.0.0` | Narrative coherence |
| **14-22** | `Impish_Nemo_12B` + `Eleusis-12B` (12.5 + 87.5) | **Grim reality & Emotional Depth** |
| **22-29** | `Omega-Darker_The-Final-Directive-12B` + ((`Epiculous/Crimson_Dawn-v0.2` + `Epiculous/Azure_Dusk-v0.2`) + `Moondark-12B`) (50 + ((12.5 + 12.5) + 25) | **Consequential Choice & Internal Conflict** |
| **29-34** | `Wayfarer-2-12B` + `Bigger-Body-12b` (80 + 20) | **Atmospheric Scene Crafting & Sensory Detail** |
| **34-39** | `Muse-12B` + `Nemo-Picaro-12B` | **Immersive delivery** |
| **39-40** | `Dans-SakuraKaze-V1.0.0` | Silver-tinted output coherence |

## Merge Details
### Merge Method

This model was merged using the Passthrough merge method.

### Models Merged

The following models were included in the merge:
* [Retreatcost/KansenSakura-Eclipse-RP-12b](https://huggingface.co/Retreatcost/KansenSakura-Eclipse-RP-12b)
* [SicariusSicariiStuff/Impish_Nemo_12B](https://huggingface.co/SicariusSicariiStuff/Impish_Nemo_12B)
* [PygmalionAI/Eleusis-12B](https://huggingface.co/PygmalionAI/Eleusis-12B)
* [ReadyArt/Omega-Darker_The-Final-Directive-12B](https://huggingface.co/ReadyArt/Omega-Darker_The-Final-Directive-12B)
* [Epiculous/Crimson_Dawn-v0.2](https://huggingface.co/Epiculous/Crimson_Dawn-v0.2)
* [Epiculous/Azure_Dusk-v0.2](https://huggingface.co/Epiculous/Azure_Dusk-v0.2)
* [Vortex5/Moondark-12B](https://huggingface.co/Vortex5/Moondark-12B)
* [LatitudeGames/Wayfarer-2-12B](https://huggingface.co/LatitudeGames/Wayfarer-2-12B)
* [allura-org/Bigger-Body-12b](https://huggingface.co/allura-org/Bigger-Body-12b)
* [LatitudeGames/Muse-12B](https://huggingface.co/LatitudeGames/Muse-12B)
* [Trappu/Nemo-Picaro-12B](https://huggingface.co/Trappu/Nemo-Picaro-12B)

## Reproduction steps
// TODO

## **🙏 Luminous Acknowledgments**
- **The Congregation of the Eclipse**: Your recorded journeys through temptation provided the essential data on desire that makes this model's portrayal of resistance possible.
- **[PocketDoc](https://huggingface.co/PocketDoc)**: For the foundations of personality and narrative.
- **[Latitude](https://huggingface.co/LatitudeGames)**: For mastering the art of emotional pacing.
- **The Architects of Clarity & Introspection**: For models that prioritize the human condition over plot.
- **[Arcee AI](https://huggingface.co/arcee-ai)**: For the tools to weave complexity with [mergekit](https://github.com/arcee-ai/mergekit).
- **[Team mradermacher](https://huggingface.co/mradermacher)**: for awesome quants
- **You**, the witness. Your prompts are the keys to the characters' hearts. What will you have them find inside?

*The sakura petals fall slowly here, each one a moment of hesitation, a regret, a hope. Watch them. Understand them.*

### **⚡ Final Admonition**
> *The light reveals the path, but it will not walk it for you. There is no easy judgment here, only the quiet, relentless burden of choice. Your character's every thought and fear will be laid bare. You may close this tab to avoid the weight of their consciousness. (But you will not. You need to see who they—and you—decide to become.)*

**✨⚖️ Version Radiance v1.3: The Session is Open.**