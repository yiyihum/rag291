---
base_model:
- Nexesenex/Llama_3.x_70b_Smarteaz_0.2_R1
- Nexesenex/Llama_3.x_70b_Smarteaz_0.2_NMT
- Nexesenex/Llama_3.x_70b_Smarteaz_0.1
library_name: transformers
tags:
- mergekit
- merge
license: llama3.3
---
# about

The Teaz series is my third attempt at making merges, this time on L3.x 70b, after the L3.2 3b Costume and Kermes series.

This time, the goal was to make a smart model with a low perplexity, in accordance to the principles of the Kermes series, but with a merge of 3 merged models like on the Costume series.

Huihui's abliterated models were used:
- Llama 3.3 70b as the pivot of the first/main model.
- Nemotron 3.1 70b and Deepseek R1 Distill 70b as the pillars of the main model, and the interlaced pivots/pillar of the 2nd and 3rd models.
- and Tulu 3 70b as a second pillar of the 2nd and 3rd models.

Bingo again. I hit 3.45 ppl512 wikieng, 62+ or ARC-C, and 82+ on ARC-E. Absolute top of the class for L3.x 70b, like Kermes is for L3 3.2 3b.

No cheating, no contaminating, just the wonderful MergeKit model-stock merge technique leveraged to a new level (compared to what I already saw being done, at least).

Next projects will involve that model as the "smarts pillar/Block" of further merges, aimed at any use case.

I think that most models can be tweaked the same way, with triple stock merges interlacing intruct finetunes and base finetunes.
- This, gaining overall "intelligence" and "quality" at the cost of a bit of its initial instructions, flavor and "personality".

Edit : the mothodology I use is actually partly rediscovered hot water.

- Mixing (finetuned) base and (finetuned) instructs,
- and using 3 models (a base, 2 sidekicks),

have been described as optimal for Merge-Stock by some enthusiasts already.

The new thing is to leverage this into a tree of merges with interlaced combinations. That's the natural developpement of the 2 aforementioned "rules".

---
# further developpements

The adventure continues with Doberman_V1, a Hermes flavored Dobby on Smarteaz abliterated steroids (very good at being "in character") :
- Nexesenex/Llama_3.x_70b_Doberman_V1 : https://huggingface.co/Nexesenex/Llama_3.x_70b_Doberman_V1 (less than 3.40 ppl 512 wiki-eng, -0.07 compared to Smarteaz_V1)

And the saga continues again with 

Nemesis_V1.1 (ex Negames), a Hermes flavored Negative Llama on Smarteaz abliterated steroids
- (More stiff and less creative than Doberman, though. Note : A mistake corrected : Hermes lorablated replace the vanilla version in Nemesis V1.1) :
- https://huggingface.co/Nexesenex/Llama_3.x_70b_Nemesis_V1.1 (less than.. 3.35 ppl 512 wiki-eng, -0.05 compared to Doberman_V1)

Evasion_V1 (ex Hermeva), a Hermes flavored Eva_01 on Smarteaz abliterated steroids (the most creative) :
- https://huggingface.co/Nexesenex/Llama_3.x_70b_Evasion_V1 (less than 3.40 ppl 512 wiki-eng, -0.02 compared to Doberman_V1)

Trinity_V1, a merge of Evasion as base, Doberman and NegaTessTease to include a bit of Tess (to be tested) :
- https://huggingface.co/Nexesenex/Llama_3.x_70b_Trinity_V1 (less than 3.40 ppl 512 wiki-eng, -0.03 compared to Doberman_V1)

Alas, I don't have under hand a Tess R1 Limerick lorablated. On the other hand, Mlabonne lorablated Hermes 3 70b Lorablated, and..
- I found 2 other models to make a "Hermes Block" and boost the creativity of the next revisions of my models, and not only the smarts.
- Here it comes : https://huggingface.co/Nexesenex/Llama_3.x_70b_Harpies_V1

---
# request for help

I (and many of us mergers, I believe) would need the following models abliterated to improve our merges, if Huihui-ai or someone could help :

- https://huggingface.co/SicariusSicariiStuff/Negative_LLAMA_70B
- https://huggingface.co/SentientAGI/Dobby-Unhinged-Llama-3.3-70B

I also tried to Lorablatize L3.1 70b Tess R1 Limerick and L3.1 70b Calme 2.3, but I'm not able to do so successfully (if someone could do that, it would be fantastic!)

- https://huggingface.co/migtissera/Tess-R1-Limerick-Llama-3.1-70B
- https://huggingface.co/MaziyarPanahi/calme-2.3-llama3.1-70b
- The Lora : https://huggingface.co/mlabonne/Llama-3-70B-Instruct-abliterated-LORA
- The yaml I used:

```yaml
base_model: meta-llama/Meta-Llama-3.1-70B-Instruct+Llama-3-70B-Instruct-abliterated-LORA
dtype: bfloat16
merge_method: task_arithmetic
parameters:
  normalize: false
slices:
- sources:
  - layer_range: [0, 80]
    model: meta-llama/Meta-Llama-3.1-70B-Instruct+Llama-3-70B-Instruct-abliterated-LORA
    parameters:
      weight: 1.0
```

---
# credits

Kudos go to the model authors, and to the Arcee / MergeKit folks, as well as to HF hosting the MergeKit App.
Also a big-up to SteelSkull, observing him cooking Nevoria decided me to try to make some merges by myself.
And to all those inspiring finetuners who give time, sometimes their money, a good time and some inspiration to others by tuning models.

---
# historic

First : On the Kostume series started on the 11/02/0205 I tried to make a triple stock merge of 3 intermediary stock merges of a dozen of model or so.
This, to see if I could pile up their abilities.

- Not bad, but nothing special about it, it's a bit hard for me to judge at 3b.

Second : On the Kermes series started the day after, I defined a simpler approach:

- Perplexity is the main constraint. Usual L3.2 3b finetunes are around 10.5-11 ppl512wikieng, Hermes is around 9.5.
- I also measure in French and Serbian to observe the variances.
  
- Arc Challenge and Easy are the second constraint to judge its basic logics.
- Usual L3.2 3b finetunes hit 40 and 60-65 respectively, Hermes3 hits 47+ and 70+.

- Lack of censorship. I always keep in mind to pick models compatible with that AMAP.
- This, may it be through the picked models' abliteration or the datasets they use.

- And of course, the test, both In Kobold/Croco.CPP (spamming very offensive requests), and in ST (a 10k prompt with a big lorebook).

Kermes series are basically stock merges on the top of anothers.
- The goal was to maintain as much the qualities of the models used, so I stay on 1+2 models for the first merge, and 1+2 for the second as well.

And bingo. Perplexity goes down still, ARC remain stable, it's quite unhinged still, and.. quite coherent, event at 10k+ context.

---
# quantizations

GGUF static quantizations (Thanks Mradermacher!) :

https://huggingface.co/mradermacher/Llama_3.x_70b_Smarteaz_V1-GGUF

GGUF iMatrix quantizations (Thanks Mradermacher!) :

https://huggingface.co/mradermacher/Llama_3.x_70b_Smarteaz_V1-i1-GGUF

---
# merge
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [Nexesenex/Llama_3.x_70b_Smarteaz_0.1](https://huggingface.co/Nexesenex/Llama_3.x_70b_Smarteaz_0.1) as a base.

### Models Merged

The following models were included in the merge:
* [Nexesenex/Llama_3.x_70b_Smarteaz_0.2_R1](https://huggingface.co/Nexesenex/Llama_3.x_70b_Smarteaz_0.2_R1)
* [Nexesenex/Llama_3.x_70b_Smarteaz_0.2_NMT](https://huggingface.co/Nexesenex/Llama_3.x_70b_Smarteaz_0.2_NMT)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: model_stock
models:
  - model: Nexesenex/Llama_3.x_70b_Smarteaz_0.2_NMT
    parameters:
      weight: 1.0
  - model: Nexesenex/Llama_3.x_70b_Smarteaz_0.2_R1
    parameters:
      weight: 1.0
base_model: Nexesenex/Llama_3.x_70b_Smarteaz_0.1
dtype: bfloat16
normalize: true

```