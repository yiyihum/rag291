---
library_name: transformers
pipeline_tag: text-generation
tags:
- 64k context
- reasoning
- thinking
- qwen3
- uncensored
base_model:
- Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1
---

<H2>Qwen3-8B-64k-Context-2X-Josiefied-Uncensored</H2>

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats. The source code can also be used directly.

This repo is for Goekdeniz-Guelmez's excellent "Josiefied-Qwen3-8B-abliterated-v1", modified from 32k (32768) context to 64 k (65536) context modified using YARN as per tech notes at Qwen repo.

NEO Imatrix dataset GGUF quants with maxed 16-bit output tensor are here:

[ https://huggingface.co/DavidAU/Qwen3-8B-64k-Josiefied-Uncensored-NEO-Max-GGUF ]

ORG model repo for this fine tune:

[ https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1 ]

Max context on this version is : 64k (65536)

Suggest min context limit of : 8k to 16k for "thinking" / "output".
 
Use Jinja Template or CHATML template.

Please refer the QWEN model card for details, benchmarks, how to use, settings, turning reasoning on/off/ system roles etc etc :

[ https://huggingface.co/Qwen/Qwen3-8B ]

<B>OPTIONAL SYSTEM ROLE: </B>

You may or may not need this, as most times Qwen3s generate their own reasoning/thinking blocks.

```
You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside <think> </think> tags, and then provide your solution or response to the problem.
```

See document "Maximizing-Model-Performance-All..." below for how to "set" system role in various LLM/AI apps below.

IMPORTANT: Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers

If you are going to use this model, (source, GGUF or a different quant), please review this document for critical parameter, sampler and advance sampler settings (for multiple AI/LLM aps).

This a "Class 1" (settings will enhance operation) model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) (especially for use case(s) beyond the model's design) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

REASON:

Regardless of "model class" this document will detail methods to enhance operations.

If the model is a Class 3/4 model the default settings (parameters, samplers, advanced samplers) must be set for "use case(s)" uses correctly. Some AI/LLM apps DO NOT have consistant default setting(s) which result in sub-par model operation. Like wise for Class 3/4 models (which operate somewhat to very differently than standard models) additional samplers and advanced samplers settings are required to "smooth out" operation, AND/OR also allow full operation for use cases the model was not designed for.

BONUS - Use these settings for ANY model, ANY repo, ANY quant (including source/full precision):

This document also details parameters, sampler and advanced samplers that can be use FOR ANY MODEL, FROM ANY REPO too - all quants, and of course source code operation too - to enhance the operation of any model.

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

NOTE:

I strongly suggest you also visit the DavidAU GGUF (below) repo too for more details in using this model ; especially if it is "Class 3" or "Class 4" to get maximum performance from the model.

For full information about this model, including:

- Details about this model and its use case(s).
- Context limits
- Special usage notes / settings.
- Any model(s) used to create this model.
- Template(s) used to access/use this model.
- Example generation(s)
- GGUF quants of this model

Please go to:

https://huggingface.co/DavidAU/Qwen3-8B-64k-Josiefied-Uncensored-NEO-Max-GGUF

[ Also see LEFT MENU under "Quantizations" ]

[[ model card updates to follow || GGUF repo(s) pending ... ]]

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
