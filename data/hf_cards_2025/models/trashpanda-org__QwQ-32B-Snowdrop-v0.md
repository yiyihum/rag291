---
base_model:
- trashpanda-org/Qwen2.5-32B-Marigold-v0
- Qwen/QwQ-32B
- Qwen/Qwen2.5-32B
- trashpanda-org/Qwen2.5-32B-Marigold-v0-exp
library_name: transformers
tags:
- mergekit
- mergekitty
- merge
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/Tdn0PJBFnG3J6UcjO9G94.png)

<sup>QwQwQwQwQwQ and Marigold met at a party and hit it off...</sup>

# QwQ-32B-Snowdrop-v0

<p><b>Has's notes</b>: it's actually pretty damn good?!</p>

<p><b>Severian's notes</b>: R1 at home for RP, literally. Able to handle my cards with gimmicks and subtle tricks in them. With a good reasoning starter+prompt, I'm getting consistently-structured responses that have a good amount of variation across them still while rerolling. Char/scenario portrayal is good despite my focus on writing style, lorebooks are properly referenced at times. Slop doesn't seem to be too much of an issue with thinking enabled. Some user impersonation is rarely observed. Prose is refreshing if you take advantage of what I did (writing style fixation). I know I said Marigold would be my daily driver, but this one is that now, it's that good.</p>

## Recommended settings

<p><b>Context/instruct template</b>: ChatML. <s>Was definitely not tested with ChatML instruct and Mistral v7 template, nuh-uh.</s></p>

<p><b>Samplers</b>: temperature at 0.9, min_p at 0.05, top_a at 0.3, TFS at 0.75, repetition_penalty at 1.03, DRY if you have access to it. (or not, see below.)</p>

A virt-io derivative prompt worked best during our testing, but feel free to use what you like.

Master import for ST: https://files.catbox.moe/w812at.png

## Reasoning

Feel free to test whichever reasoning setup you're most comfortable with, but here's a recommendation from me. My prompt has a line that says:

```
Style Preference: Encourage the usage of a Japanese light novel writing style.
```

Deciding to fixate on that, my reasoning starter is:

```
<think>Okay, in this scenario, before responding I need to consider the writing style referenced in the prompt, which is
```

What this did for me, at least during testing is that it gave the reasoning a structure to follow across rerolls, seeking out that part of the prompt consistently.
See below:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/Mw6h-mmZ0TcQrtNPGdCsV.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/JeSEYwTJofYRqLHKm8glm.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/nDSAJK7HDc-bKFXe6ER_q.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/j2slz1hEKsEM3bVrR--xs.png)

But the responses were still varied, because the next few paragraphs after these delved into character details, so on and so forth. Might want to experiment and make your own thinking/reasoning starter that focuses on what you hope to get out of the responses for best results.

— Severian

## Thank you!

Big thanks to the folks in the trashpanda-org discord for testing and sending over some logs!

## Reviews

> PROS:
> 
> In 10 swipes, had only two minor instances of speaking for {{user}}. (Can probably be fixed with a good prompt, though.)
> 
> Creativity: 8/10 swipes provided unique text for 90% of the response, almost no cliché phrases.
>
> Takes personality of characters into account, sticking to it well. Even without a lorebook to support it was able to retain lore-specific terms and actually remember which meant which.
>
> NPCs: In 6/10 swipes NPC characters also partook in action, sticking to bits of information provided about them in opening message. Some of them even had their unique speech patterns. (Certain with a proper lorebook it would cook.)
>
> Unfiltered, graphic descriptions of fight scenes. Magic, physical attacks - everything was taken into account with no holding back.
>
> CONS:
>
> Some swipes were a bit OOC. Some swipes were bland, providing little to no input or any weight on the roleplay context.
>
> Out of all models I've tried recently, this one definitely has most potential. With proper prompting I think this beast would be genuinely one of the best models for unique scenarios.

— Sellvene

> It's one of the -maybe THE- best small thinking models right now. It sticks to character really well, slops are almost non-existent though they are still there of course, it proceeds with the story well and listens to the prompt. I LOVE R1 but I love snowdrop even more right now because answers feel more geniune and less agressive compared to R1.

— Carmenta

> Writes better than GPT 4.5. Overall, I think censorship is fucking up more unhinged bots and it's too tame for my liking. Another thing I noticed is that, it's sticking too much to being "right" to the character and too afraid to go off the rails.

— Myscell

> I'm fainting, the character breakdown in it's thinking is similar like R1 does. Character handling looks amazing. Broo if a merge this good then, I'm looking forward to that QwQ finetune.

— Sam

> Negligible slop, no positivity bias which is good though. I like the model so far, R1 at home.

— Raihanbook

> Overall, I think this is a real solid model. Cot is great, listens to my prompt extremely well. Number 1 for reasoning, honestly. And the way it portrays the character and persona details? Perfect. Narration, perfect. I have very little complaints about this model, ya'll cooked.

— Moothdragon

> On my end, posivity bias isn't really there 🤔 Character and scenario portrayal is good. The prose too, I like it. Between this and Marigold, I feel like I can lean into snowboard (I mean Snowdrop) more. For now though, it is still Marigold.

— Azula

> Honestly i am impressed and I like it.

— OMGWTFBBQ

> It's pretty damn good. Better than Mullein, I think.

— br

> So far, it fucking SLAPS. I don't think it's tried to pull POV once yet.

— Overloke

## Just us having fun, don't mind it

![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/ci-okzqZjNgk-CgYFVCNO.png)

## Some logs

![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/jMlZatm5wvN8KNRlWeNbK.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/o4PQb0FbPrU_PoIT5pzDu.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/jFTpiw65LHkel3EzR6IRV.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/vwdKSjICLqua98TXDsv-W.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/R7B7QsMjIdgzPT1-i4UI6.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/Xn2FPUPESWPjzOQQ4sdwp.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/tok2RfOE0BQHHkPOpVje3.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/vtkwpEEubUyZ3mYW6asru.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/4xWnSieopicxQtwjaO4Ri.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/dLlvlP4U_cWpd84e5Tqtd.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/8O7p_z6EN9Tf7Rr52RXm7.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/m_6B_uJAdaGlq8UlYIPIm.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/daEqb2Qi0pA6UobNsJota.png)
(After a session started with Gemini)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/DQMan-Ywm-meyFtJGVWlF.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/XKEp3p7UZ8mlBeOxAiXEa.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/wSA-eBIAh9Ru0BE5HeIJ-.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/qd1XFGtopRQxQqHrs98wh.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/AzGgKBtTBzwUSx0So4_pS.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/VyEZvFY6yL4OkTBioqdaP.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/675a77cf99ca23af9daacccc/cTgYWUmnLORfX1fZZw-1f.png)

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-32B](https://huggingface.co/Qwen/Qwen2.5-32B) as a base.

### Models Merged

The following models were included in the merge:
* [trashpanda-org/Qwen2.5-32B-Marigold-v0](https://huggingface.co/trashpanda-org/Qwen2.5-32B-Marigold-v0)
* [Qwen/QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)
* [trashpanda-org/Qwen2.5-32B-Marigold-v0-exp](https://huggingface.co/trashpanda-org/Qwen2.5-32B-Marigold-v0-exp)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: trashpanda-org/Qwen2.5-32B-Marigold-v0-exp
    parameters:
      weight: 1
      density: 1
  - model: trashpanda-org/Qwen2.5-32B-Marigold-v0
    parameters:
      weight: 1
      density: 1
  - model: Qwen/QwQ-32B
    parameters:
      weight: 0.9
      density: 0.9
merge_method: ties
base_model: Qwen/Qwen2.5-32B
parameters:
  weight: 0.9
  density: 0.9
  normalize: true
  int8_mask: true
tokenizer_source: Qwen/Qwen2.5-32B-Instruct
dtype: bfloat16


```
