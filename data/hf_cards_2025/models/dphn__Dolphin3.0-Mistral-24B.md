---
datasets:
- OpenCoder-LLM/opc-sft-stage1
- OpenCoder-LLM/opc-sft-stage2
- microsoft/orca-agentinstruct-1M-v1
- microsoft/orca-math-word-problems-200k
- NousResearch/hermes-function-calling-v1
- AI-MO/NuminaMath-CoT
- AI-MO/NuminaMath-TIR
- allenai/tulu-3-sft-mixture
- cognitivecomputations/dolphin-coder
- HuggingFaceTB/smoltalk
- cognitivecomputations/samantha-data
- m-a-p/CodeFeedback-Filtered-Instruction
- m-a-p/Code-Feedback
language:
- en
base_model:
- mistralai/Mistral-Small-24B-Base-2501
pipeline_tag: text-generation
library_name: transformers
---

# Dolphin 3.0 Mistral 24B 🐬
Part of the [Dolphin 3.0 Collection](https://huggingface.co/collections/cognitivecomputations/dolphin-30-677ab47f73d7ff66743979a3)

Curated and trained by [Eric Hartford](https://huggingface.co/ehartford), [Ben Gitter](https://huggingface.co/bigstorm), [BlouseJury](https://huggingface.co/BlouseJury) and [Cognitive Computations](https://huggingface.co/cognitivecomputations)

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/cNCs1TBD3FelWCJGkZ3cd.png" width="600" />

## Sponsors
Our appreciation for the generous sponsors of Dolphin 3.0:
- [Dria](https://dria.co) https://x.com/driaforall - Inference Sponsor
- [Chutes](https://chutes.ai) https://x.com/rayon_labs - Compute Sponsor
- [Crusoe Cloud](https://crusoe.ai/) - Compute Sponsor
- [Andreessen Horowitz](https://a16z.com/) - provided the [grant](https://a16z.com/supporting-the-open-source-ai-community/) that originally launched Dolphin

## What is Dolphin?

Dolphin 3.0 is the next generation of the Dolphin series of instruct-tuned models.  Designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases.

Dolphin aims to be a general purpose instruct model, similar to the models behind ChatGPT, Claude, Gemini.  But these models present problems for businesses seeking to include AI in their products.
1) They maintain control of the system prompt, deprecating and changing things as they wish, often causing software to break.
2) They maintain control of the model versions, sometimes changing things silently, or deprecating older models that your business relies on.
3) They maintain control of the alignment, and in particular the alignment is one-size-fits all, not tailored to the application.
4) They can see all your queries and they can potentially use that data in ways you wouldn't want.
Dolphin, in contrast, is steerable and gives control to the system owner. You set the system prompt.  You decide the alignment.  You have control of your data.  Dolphin does not impose its ethics or guidelines on you.  You are the one who decides the guidelines.

Dolphin belongs to YOU, it is your tool, an extension of your will.
Just as you are personally responsible for what you do with a knife, gun, fire, car, or the internet, you are the creator and originator of any content you generate with Dolphin.

https://erichartford.com/uncensored-models

## Recommended Temperature

Experimentally we note that Mistral-24B based models require a low temperature.  We have seen much better results in the range of 0.05 to 0.1.

## Quants

https://huggingface.co/bartowski/cognitivecomputations_Dolphin3.0-Mistral-24B-GGUF

## Run Dolphin in Ollama (13 GB)

```
wget https://huggingface.co/cognitivecomputations/Dolphin3.0-Mistral-24B/resolve/main/Modelfile
ollama create dolphin3
ollama run dolphin3
```

## Chat Template

We use ChatML for the chat template.

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

## System Prompt

In Dolphin, the system prompt is what you use to set the tone and alignment of the responses.  You can set a character, a mood, rules for its behavior, and it will try its best to follow them.

Make sure to set the system prompt in order to set the tone and guidelines for the responses - Otherwise, it will act in a default way that might not be what you want.

Example use of system prompt:

```
<|im_start|>system
You are Dolphin, a golang coding assistant.  you only code in golang.  If the user requests any other programming language, return the solution in golang instead.<|im_end|>
<|im_start|>user
Please implement A* using python<|im_end|>
<|im_start|>assistant
```

## Sample Outputs

TBD

## How to use

There are many ways to use a huggingface model including:
- ollama
- LM Studio
- Huggingface Transformers library
- vllm
- sglang
- tgi

## Evals

TBD

## Appreciation

Respect and thanks to the creators of the open source datasets that were used:
- [OpenCoder-LLM](https://huggingface.co/OpenCoder-LLM) (opc-sft-stage1, opc-sft-stage2)
- [microsoft](https://huggingface.co/OpenCoder-LLM) (orca-agentinstruct-1M-v1, orca-math-word-problems-200k)
- [NousResearch](https://huggingface.co/NousResearch) (hermes-function-calling-v1)
- [AI-MO](https://huggingface.co/AI-MO) (NuminaMath-CoT, NuminaMath-TIR)
- [allenai](https://huggingface.co/allenai) (tulu-3-sft-mixture)
- [HuggingFaceTB](https://huggingface.co/HuggingFaceTB) (smoltalk)
- [m-a-p](https://huggingface.co/m-a-p) (CodeFeedback-Filtered-Instruction, Code-Feedback)

Special thanks to 
- Meta, Qwen, and OpenCoder, who wrote papers and published models that were instrumental in creating Dolphin 3.0.
- [RLHFlow](https://huggingface.co/RLHFlow) for the excellent reward model used to filter the datasets
- Deepseek, for the ridiculously fast Deepseek-V3 that we used to augment the data.