---
license: apache-2.0
language:
- en
base_model:
- mistralai/Mistral-Nemo-Base-2407
tags:
- text adventure
- roleplay
library_name: transformers
---

![image/jpeg](muse.jpg)

# Muse-12B

Muse brings an extra dimension to any tale—whether you're exploring a fantastical realm, court intrigue, or slice-of-life scenarios where a conversation can be as meaningful as a quest. While it handles adventure capably, Muse truly shines when character relationships and emotions are at the forefront, delivering impressive narrative coherence over long contexts.

If you want to easily try this model for free, you can do so at [https://aidungeon.com](https://aidungeon.com/).

We plan to continue improving and open-sourcing similar models, so please share any and all feedback on how we can improve model behavior. Below we share more details on how Muse was created.

[Quantized GGUF weights can be downloaded here.](https://huggingface.co/LatitudeGames/Muse-12B-GGUF)

## Model details

Muse 12B was trained using Mistral Nemo 12B as its foundation, with training occurring in three stages: SFT (supervised fine-tuning), followed by two distinct DPO (direct preference optimization) phases.

**SFT** - Various multi-turn datasets from a multitude of sources, combining text adventures of the kind used to finetune [our Wayfarer 12B model](https://huggingface.co/LatitudeGames/Wayfarer-12B), long emotional narratives and general roleplay, each carefully balanced and rewritten to be free of common AI cliches. A small single-turn instruct dataset was included to send a stronger signal during finetuning.

**DPO 1** - Gutenberg DPO, [credit to Jon Durbin](https://huggingface.co/datasets/jondurbin/gutenberg-dpo-v0.1) - This stage introduces human writing techniques, significantly enhancing the model's potential outputs, albeit trading some intelligence for the stylistic benefits of human-created text.

**DPO 2** - Reward Model User Preference Data, [detailed in our blog](https://blog.latitude.io/all-posts/synthetic-data-preference-optimization-and-reward-models) - This stage refines the Gutenberg stage's "wildness," restoring intelligence while maintaining enhanced writing quality and providing a final level of enhancement due to the reward model samples.

The result is a model that writes like no other: versatile across genres, natural in expression, and suited to emotional depth.

## Inference

The Nemo architecture is known for being sensitive to higher temperatures, so the following settings are recommended as a baseline. Nothing stops you from experimenting with these, of course.

```
"temperature": 0.8,
"repetition_penalty": 1.05,
"min_p": 0.025
```

## Limitations

Muse was trained exclusively on second-person present tense data (using “you”) in a narrative style. Other styles will work as well but may produce suboptimal results.

Average response lengths tend toward verbosity (1000+ tokens) due to the Gutenberg DPO influence, though this can be controlled through explicit instructions in the system prompt.

## Prompt Format

ChatML was used during all training stages.

```
<|im_start|>system
You're a masterful storyteller and gamemaster. Write in second person present tense (You are), crafting vivid, engaging narratives with authority and confidence.<|im_end|>
<|im_start|>user
> You peer into the darkness.
<|im_start|>assistant
You have been eaten by a grue.

GAME OVER
```

## Credits

Thanks to [Gryphe Padar](https://huggingface.co/Gryphe) for collaborating on this finetune with us!