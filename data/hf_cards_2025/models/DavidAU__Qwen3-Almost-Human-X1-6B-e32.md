---
license: apache-2.0
base_model:
- DavidAU/Qwen3-Jan-v1-256k-ctx-6B-Brainstorm20x
datasets:
- DavidAU/The-works-PK-Dick
language:
- en
pipeline_tag: text-generation
tags:
- programming
- code generation
- code
- coding
- coder
- chat
- code
- chat
- brainstorm
- qwen
- float32
- qwen3
- qwencoder
- brainstorm 20x
- all uses cases
- Jan-V1
- finetune
- thinking
- reasoning
- unsloth
- not-for-all-audiences
library_name: transformers
---

(examples to be added, quants pending...)

<h2>Qwen3-Almost-Human-X1-6B-e32</h2>

<img src="deckard.gif" style="float:right; width:300px; height:300px; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats. The source code can also be used directly.

A love letter to all things Philip K Dick, trained and fine tuned on an FIVE in house datasets via Unsloth.

"X1" is the first of the series, with imprinting level of 8 fold deeper during training.

This is mastered in float 32 - 32 bit precision.

(reg Series links below)

"Almost Human" is about adding (back) the humanity, the real person called Philip K Dick back into the model - with tone, thinking, and a touch of prose.

"Deckard" is the main character in Blade Runner.

---

<B>DECKARD SERIES:</b>

You may perfer light and/or heavy depending on your use case(s).

With "Light", 6% of the model is trained, whereas "Heavy" 13% of the model is trained, and the training is twice as long, and deeper than light.

"Large" versions are trained on 3x times the dataset.

"Almost Human" versions have an additional dataset (plus 3x dataset) containing the BIO of the author, letters, notes and such.

Each version will diff from each other, with "Light" vs "Heavy" having a large difference.

Light [6%]:
- https://huggingface.co/DavidAU/Qwen3-Deckard-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-Almost-Human-6B

Heavy [13%, 2x longer training]:
- https://huggingface.co/DavidAU/Qwen3-Deckard-Heavy-6B
- https://huggingface.co/DavidAU/Qwen3-Deckard-Large-Heavy-6B

---

This model requires:
- Jinja (embedded) or CHATML template
- Max context of 256k.

Settings used for testing (suggested):
- Temp .3 to .7 (but .8 to 1.5 for creative)
- Rep pen 1.05 to 1.1
- Topp .8 , minp .05
- Topk 20
- Min context of 8k for thinking / output.
- No system prompt.

This model will respond well to both detailed instructions and step by step refinement and additions to code.

Likewise for creative use cases.

Here is a review of this model's operations:

https://www.linkedin.com/posts/gchesler_nightmediaqwen3-jan-v1-256k-ctx-6b-brainstorm20x-q6-activity-7364301711529709570-CiAn

As this is an instruct model, it will also benefit from a detailed system prompt too.

For simpler coding problems, lower quants will work well; but for complex/multi-step problem solving suggest Q6 or Q8.

---

<B>QUANTS:</b>

---

GGUF? GGUF Imatrix? Other?

Special thanks to Team Mradermacher, Team Nightmedia and other quanters!

See under "model tree", upper right and click on "quantizations".

New quants will automatically appear.

---

<H2>What is Brainstorm?</H2>

---

<B>Brainstorm 20x</B>

The BRAINSTORM process was developed by David_AU.

Some of the core principals behind this process are discussed in this <a href="https://arxiv.org/pdf/2401.02415"> 
scientific paper : Progressive LLaMA with Block Expansion </a>. 

However I went in a completely different direction from what was outlined in this paper.

What is "Brainstorm" ?

The reasoning center of an LLM is taken apart, reassembled, and expanded.

In this case for this model: 20 times

Then these centers are individually calibrated. These "centers" also interact with each other. 
This introduces subtle changes into the reasoning process. 
The calibrations further adjust - dial up or down - these "changes" further. 
The number of centers (5x,10x etc) allow more "tuning points" to further customize how the model reasons so to speak.

The core aim of this process is to increase the model's detail, concept and connection to the "world", 
general concept connections, prose quality and prose length without affecting instruction following. 

This will also enhance any creative use case(s) of any kind, including "brainstorming", creative art form(s) and like case uses.

Here are some of the enhancements this process brings to the model's performance:

- Prose generation seems more focused on the moment to moment. 
- Sometimes there will be "preamble" and/or foreshadowing present.
- Fewer or no "cliches"
- Better overall prose and/or more complex / nuanced prose.
- A greater sense of nuance on all levels.
- Coherence is stronger.
- Description is more detailed, and connected closer to the content.
- Simile and Metaphors are stronger and better connected to the prose, story, and character.
- Sense of "there" / in the moment is enhanced.
- Details are more vivid, and there are more of them.
- Prose generation length can be long to extreme.
- Emotional engagement is stronger.
- The model will take FEWER liberties vs a normal model: It will follow directives more closely but will "guess" less.
- The MORE instructions and/or details you provide the more strongly the model will respond.
- Depending on the model "voice" may be more "human" vs original model's "voice".

Other "lab" observations:

- This process does not, in my opinion, make the model 5x or 10x "smarter" - if only that was true! 
- However, a change in "IQ" was not an issue / a priority, and was not tested or calibrated for so to speak.
- From lab testing it seems to ponder, and consider more carefully roughly speaking.
- You could say this process sharpens the model's focus on it's task(s) at a deeper level.

The process to modify the model occurs at the root level - source files level. The model can quanted as a GGUF, EXL2, AWQ etc etc.

---

For more information / other Qwen/Mistral Coders / additional settings see:

[ https://huggingface.co/DavidAU/Qwen2.5-MOE-2x-4x-6x-8x__7B__Power-CODER__19B-30B-42B-53B-gguf ]

---

<H2>Help, Adjustments, Samplers, Parameters and More</H2>

---

<B>CHANGE THE NUMBER OF ACTIVE EXPERTS:</B>

See this document:

https://huggingface.co/DavidAU/How-To-Set-and-Manage-MOE-Mix-of-Experts-Model-Activation-of-Experts

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

