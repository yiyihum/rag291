---
license: apache-2.0
base_model:
- Qwen/Qwen3-4B
pipeline_tag: text-generation
tags:
- NEO Imatrix
- 32 k context
- reasoning
- thinking
- qwen3
---

<H2>Qwen3-4B-NEO-Imatrix-Max-GGUF</H2>

NEO Imatrix Quants of new "Qwen 3 - 4B" model with MAX "output tensor" at BF16 to improve reasoning / output generation.

NEO Imatrix dataset was generated in house. 

Imatrix effect will be stronger, the lower the quant you use with IQ4XS/IQ4NL being the best balanced quant for quality and Imatrix effect.

These quants will also be the strongest for creative use cases.

For stronger reasoning use higher quants.

Q8_0 quant is maxed only, as Imatrix has no effect on this quant.

F16 is full precision.

Context Length: 32 K + 8K output generation (can be extended to 128k). 

<B>For 65k, 128k or 256K context - 4B model:</B>

[ https://huggingface.co/DavidAU/Qwen3-4B-Q8_0-65k-128k-256k-context-GGUF ]

<B>NOTE - Jinja Template / Template to Use with this Model:</B>

If you are having issues with Jinja "auto template", use CHATML template.

OR (LMSTUDIO users / option)

Update the Jinja Template (go to this site, template-> copy the "Jinja template" and then paste.) 

[ https://lmstudio.ai/neil/qwen3-thinking ]

<b>System Role - Suggested:</B>

You may or may not need this, as most times Qwen3s generate their own reasoning/thinking blocks.

```
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem.
```

See document "Maximizing-Model-Performance-All..." below for how to "set" system role in various LLM/AI apps below.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<b>Optional Enhancement:</B>

The following can be used in place of the "system prompt" or "system role" to further enhance the model.

It can also be used at the START of a NEW chat, but you must make sure it is "kept" as the chat moves along.
In this case the enhancements do not have as strong effect at using "system prompt" or "system role".

Copy and paste EXACTLY as noted, DO NOT line wrap or break the lines, maintain the carriage returns exactly as presented.

<PRE>
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
</PRE>

You do not need to use this, it is only presented as an additional enhancement which seems to help scene generation
and scene continue functions.

This is another system prompt you can use, and you can change the "names" to alter it's performance.

This creates a quasi "reasoning" window/block.

Your prompt will directly impact how strong this system prompt reacts.

```
You are a deep thinking AI composed of 4 AIs - [MODE: Spock], [MODE: Wordsmith], [MODE: Jamet] and [MODE: Saten], - you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself (and 4 partners) via systematic reasoning processes (display all 4 partner thoughts) to help come to a correct solution prior to answering. Select one partner to think deeply about the points brought up by the other 3 partners to plan an in-depth solution. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem.
```

<B>Other Notes:</B>

Reasoning is ON by default in this model, and model will auto-generate "think" block(s).

For benchmarks, usage info, settings please see org model card here:

[ https://huggingface.co/Qwen/Qwen3-4B ]

[ Model card, and examples to follow. ]

---

<h2>Special Thanks:</h2>

---

Special thanks to all the following, and many more...

All the model makers, fine tuners, mergers, and tweakers:
- Provides the raw "DNA" for almost all my models.
- Sources of model(s) can be found on the repo pages, especially the "source" repos with link(s) to the model creator(s).

Huggingface [ https://huggingface.co ] :
- The place to store, merge, and tune models endlessly.
- THE reason we have an open source community.

LlamaCPP [ https://github.com/ggml-org/llama.cpp ] :
- The ability to compress and run models on GPU(s), CPU(s) and almost all devices.
- Imatrix, Quantization, and other tools to tune the quants and the models.
- Llama-Server : A cli based direct interface to run GGUF models.
- The only tool I use to quant models.

Quant-Masters: Team Mradermacher, Bartowski, and many others:
- Quant models day and night for us all to use.
- They are the lifeblood of open source access.

MergeKit [ https://github.com/arcee-ai/mergekit ] :
- The universal online/offline tool to merge models together and forge something new.
- Over 20 methods to almost instantly merge model, pull them apart and put them together again.
- The tool I have used to create over 1500 models.

Lmstudio [ https://lmstudio.ai/ ] :
- The go to tool to test and run models in GGUF format.
- The Tool I use to test/refine and evaluate new models.
- LMStudio forum on discord; endless info and community for open source.

Text Generation Webui // KolboldCPP // SillyTavern:
- Excellent tools to run GGUF models with - [  https://github.com/oobabooga/text-generation-webui ] [ https://github.com/LostRuins/koboldcpp ] .
- Sillytavern [ https://github.com/SillyTavern/SillyTavern ] can be used with LMSTudio [ https://lmstudio.ai/ ] , TextGen [ https://github.com/oobabooga/text-generation-webui ], Kolboldcpp [ https://github.com/LostRuins/koboldcpp ], Llama-Server [part of LLAMAcpp] as a off the scale front end control system and interface to work with models.
