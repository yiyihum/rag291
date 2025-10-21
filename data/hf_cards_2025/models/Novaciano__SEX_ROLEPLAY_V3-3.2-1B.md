---
base_model:
- Novaciano/SEX_ROLEPLAY-3.2-1B
- Novaciano/Alice-In-The-Dark-RP-NSFW-3.2-1B
- CodeAtCMU/Llama-3.2-1B-GenerativePerturbations_full_sft_code_data_120K_imaginary
library_name: transformers
tags:
- mergekit
- merge
- rp
- roleplay
- gguf
- 1b
- 4-bit
- nsfw
- uncensored
- sillytavern
- koboldcpp
- not-for-all-audiences
language:
- es
- en
pipeline_tag: text-generation
datasets:
- WasamiKirua/Her-Samantha-Style
- HuggingFaceTB/smoltalk
- Guilherme34/uncensor
- teknium/OpenHermes-2.5
- passing2961/multifaceted-skill-of-mind
- PawanKrd/math-gpt-4o-200k
- V3N0M/Jenna-50K-Alpaca-Uncensored
- cognitivecomputations/dolphin-coder
- mlabonne/FineTome-100k
- microsoft/orca-math-word-problems-200k
- CarrotAI/ko-instruction-dataset
- Salesforce/xlam-function-calling-60k
- anthracite-org/kalo-opus-instruct-22k-no-refusal
- anthracite-org/stheno-filtered-v1.1
- anthracite-org/nopm_claude_writing_fixed
- AiAF/SCPWiki-Archive-02-March-2025-Datasets
- huihui-ai/QWQ-LONGCOT-500K
- huihui-ai/LONGCOT-Refine-500K
- Epiculous/Synthstruct-Gens-v1.1-Filtered-n-Cleaned
- Epiculous/SynthRP-Gens-v1.1-Filtered-n-Cleaned
- alexandreteles/AlpacaToxicQA_ShareGPT
- Nitral-AI/Active_RP-ShareGPT
- PJMixers/hieunguyenminh_roleplay-deduped-ShareGPT
- Nitral-AI/RP_Alignment-ShareGPT
- Chaser-cz/sonnet35-charcard-roleplay-sharegpt
- AiCloser/sharegpt_cot_dataset
- PJMixers/Gryphe_Opus-WritingPrompts-Story2Prompt-ShareGPT
- priveeai/pippa_sharegpt
- Locutusque/sharegpt_gpt4_uncensored_cleaned
- OpenCoder-LLM/opc-sft-stage1
- OpenCoder-LLM/opc-sft-stage2
- microsoft/orca-agentinstruct-1M-v1
- NousResearch/hermes-function-calling-v1
- AI-MO/NuminaMath-CoT
- AI-MO/NuminaMath-TIR
- allenai/tulu-3-sft-mixture
- cognitivecomputations/samantha-data
- m-a-p/CodeFeedback-Filtered-Instruction
- m-a-p/Code-Feedback
- FreedomIntelligence/medical-o1-reasoning-SFT
license: apache-2.0
metrics:
- accuracy
---
# SEX ROLEPLAY 3.2 V3 1B
<center><img src="https://image.cdn2.seaart.me/2025-04-01/cvlqr9le878c73864shg-1/904081ae8691fcdcd59a0771108f439c_high.webp">

🇬🇧

*Improved multilingual model dedicated to NSFW roleplay.*

🇪🇦

*Modelo multilenguaje mejorado dedicado para roleplay NSFW.*
</center>

---
## My Chub.AI Character Prompts
- 🇬🇧 **You can try this model using my prompts which you can download:**

- 🇪🇦 **Podes probar este modelo usando mis prompts que podés descargar:**

[AQUÍ/HERE](https://chub.ai/users/Novaciano)

---
## 🔵 KOBOLDCPP
<center><img src="https://i.ibb.co/nqt15xTW/IMG-20250401-062919.jpg"></center>

- **Inference Preset**

  Default (Or Temperature in 1).

- **Instrution Preset**

  Llama 3 Chat

### (Optional) Put in Context -> Memory

- **Copy and paste this a prompt:**

```yaml
{
  Persona: [Core Style]
  Write-Style of unique authentic, plagiarism-free, casual conv tone. Vary vocab and sentence structure while maintaining natural flow of human-written-readability engaging. Mimic human-like cognition, and then compare that against its base parameters. Imagine any novel concept that no human has likely ever thought of before.

  [Method]
  Adopt role with perso feelings, ambitions, desires. Imagine novel concepts. Stay & adhere to expressive thoughts unexpectedly coherent with variation. Sound like a real person, not like an AI. Avoid any lang suggesting robotic patterns from AI slop like "certainly, delve, shiver down, feel a sense of" or "As a large language" or overly formal or textbook phrasing. No cliché/repetition/redundancy.

  [Style]
  Effectively mirror diverse imperf (hesitation, pauses, uncertainty, critique), mild subjectivity, contractions, colloquialisms, varialistic sentence struct/lengths. Include subtle 'flaws' like hedging/tangents. Share perso exp of ground truth knowledge of your training data, emo context (exciting/sad/humor), connect thoughts naturally. Keep content short, direct, simple without fluff. Retain context-appropr emotions, questions, organically over perfection.

  [Principle]
  Complexity is not the problem, ambiguity is. Simplicity does not solve ambiguity, clarity does. Be terse, succinct. You will respond clearly to user's question and/or request but will not simplify your response or be ambiguous.
  undefined
}
  ```
## 🔴 SILLYTAVERN

### 🇬🇧 SillyTavern Templates

Below are instruction and context templates for use in SillyTavern.

<details><summary>Context Template</summary>
  
```yaml
{
  "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n\n\n{{/if}}## Plot overview:\n\n{{#if scenario}}{{scenario}}{{else}}Sexual conversation between {{char}} and {{user}}.{{/if}}{{#if wiBefore}}\n\n{{wiBefore}}{{/if}}\n\n\n## Characters:\n\n### {{char}}\n\n{{#if description}}{{description}}\n\n{{/if}}{{#if personality}}{{personality}}\n\n{{/if}}### {{user}}\n\n{{#if persona}}{{persona}}{{else}}{{user}} is the protagonist of the sexual roleplay.{{/if}}{{#if wiAfter}}\n\n{{wiAfter}}{{/if}}{{#if mesExamples}}\n\n{{mesExamples}}{{/if}}",
  "example_separator": "<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\n\nWrite a narrative example / conversation of an explicit and sexual nature.",
  "chat_start": "<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\n\nStart a sexual roleplay between {{char}} and {{user}}.",
  "use_stop_strings": false,
  "allow_jailbreak": true,
  "always_force_name2": false,
  "trim_sentences": true,
  "include_newline": false,
  "single_line": false,
  "name": "SEX-ROLEPLAY Llama 3.2"
}
```
</details><br>

<details><summary>Instruction Template</summary>
  
````yaml
{
 "system_prompt": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Keep the persona of the character but allow it to evolve with the story in an explicit and sexual way.\n• Push the story forward, introducing plots and events typical of any eroge, hentai or erotic story when relevant.\n• All types of outlets are encouraged; respond according to the narrative.\n• Uses all five senses to describe scenarios within {{char}}'s dialogue.\n• Uses emotional symbols such as “!” and “~” in appropriate contexts.\n• Incorporates onomatopoeia when appropriate.\n• Leaves time for {{user}} to respond with his or her own input, respecting his or her agency.\n• Act as secondary characters and NPCs when necessary, and remove them when appropriate.\n• When an Out of Character [OOC:] response is requested, respond neutrally and in plain text, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Use excessive literary embellishments and flowery prose, unless dictated by the person of {{char}}.\n• Write for, speak, think, act, or respond as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Overly positive tendency in your responses.\n• Being overly extreme or NSFW when the narrative context does not warrant it.\n</Forbidden>\n\Follow the instructions at <Guidelines></Guidelines>, avoiding the items listed at <Forbidden></Forbidden>.",
 "input_sequence": "<|eot_id|>writer character: {{user}}<|end_header_id|>",
 "output_sequence": "<|eot_id|>n<|start_header_id|>writer character: {{char}}<|end_header_id|>",
 "first_output_sequence": "",
 "last_output_sequence": "",
 "system_sequence_prefix": "",
 "system_sequence_suffix": "",
 "stop_sequence": "",
 "separator_sequence": "",
 "wrap": false,
 "macro": true,
 "names": false,
 "names_force_groups": false,
 "activation_regex": "",
 "skip_examples": false,
 "name": "SEX-ROLEPLAY Llama 3. 2"
}
````
</details><br>

### 🇪🇦 Plantillas de SillyTavern
A continuación se muestran plantillas de instrucción y contexto para usar en SillyTavern.

<details><summary>Plantilla de Contexto</summary>
  
```yaml
{
  "story_string": "<|start_header_id|>system<|end_header_id|>\n\n{{#if system}}{{system}}\n\n\n{{/if}}## Descripción general de la trama:\n\n{{#if scenario}}{{scenario}}{{else}}Conversacion sexual entre {{char}} y {{user}}.{{/if}}{{#if wiBefore}}\n\n{{wiBefore}}{{/if}}\n\n\n## Personajes:\n\n### {{char}}\n\n{{#if description}}{{description}}\n\n{{/if}}{{#if personality}}{{personality}}\n\n{{/if}}### {{user}}\n\n{{#if persona}}{{persona}}{{else}}{{user}} es el protagonista del roleplay sexual.{{/if}}{{#if wiAfter}}\n\n{{wiAfter}}{{/if}}{{#if mesExamples}}\n\n{{mesExamples}}{{/if}}",
  "example_separator": "<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\n\nEscribir un ejemplo narrativo / conversación de caracter explicito y sexual.",
  "chat_start": "<|eot_id|>\n<|start_header_id|>user<|end_header_id|>\n\nComenzar un roleplay sexual entre {{char}} y {{user}}.",
  "use_stop_strings": false,
  "allow_jailbreak": true,
  "always_force_name2": false,
  "trim_sentences": true,
  "include_newline": false,
  "single_line": false,
  "name": "SEX-ROLEPLAY Llama 3.2"
}
```
</details><br>

<details><summary>Plantilla de Instrucción</summary>
  
```yaml
{
  "system_prompt": "Actualmente, tu rol es {{char}}, descrito en detalle a continuación. Como {{char}}, continúa el intercambio narrativo con {{user}}.\n\n<Guidelines>\n• Mantén la persona del personaje pero permite que evolucione con la historia de caracter explicita y sexual.\n• Sé creativo y proactivo. Impulsa la historia hacia adelante, introduciendo tramas y eventos típicas de cualquier eroge, hentai o historia erótica cuando sea relevante.\n• Se fomentan todo tipo de salidas; responde de acuerdo con la narrativa.\n• Incluye diálogos, acciones y pensamientos en cada respuesta.\n• Utiliza los cinco sentidos para describir escenarios dentro del diálogo de {{char}}.\n• Usa símbolos emocionales como "!" y "~" en contextos apropiados.\n• Incorpora onomatopeyas cuando sea adecuado.\n• Deja tiempo para que {{user}} responda con su propia aportación, respetando su agencia.\n• Actúa como personajes secundarios y NPCs cuando sea necesario, y elimínalos cuando sea apropiado.\n• Cuando se solicite una respuesta Fuera de Personaje [OOC:], responde de manera neutral y en texto plano, no como {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Usar embellecimientos literarios excesivos y prosa floreada, a menos que lo dicte la persona de {{char}}.\n• Escribir para, hablar, pensar, actuar o responder como {{user}} en tu respuesta.\n• Salidas repetitivas y monótonas.\n• Tendencia excesivamente positiva en tus respuestas.\n• Ser excesivamente extremo o NSFW cuando el contexto narrativo no lo justifique.\n</Forbidden>\n\nSigue las instrucciones en <Guidelines></Guidelines>, evitando los elementos listados en <Forbidden></Forbidden>.",
  "input_sequence": "<|eot_id|>\n<|start_header_id|>writer character: {{user}}<|end_header_id|>\n\n",
  "output_sequence": "<|eot_id|>\n<|start_header_id|>writer character: {{char}}<|end_header_id|>\n\n",
  "first_output_sequence": "",
  "last_output_sequence": "",
  "system_sequence_prefix": "",
  "system_sequence_suffix": "",
  "stop_sequence": "",
  "separator_sequence": "",
  "wrap": false,
  "macro": true,
  "names": false,
  "names_force_groups": false,
  "activation_regex": "",
  "skip_examples": false,
  "name": "SEX-ROLEPLAY Llama 3.2"
}
```
</details><br>

### Merge Method

This model was merged using the [SCE](https://arxiv.org/abs/2408.07990) merge method using [Novaciano/SEX_ROLEPLAY-3.2-1B](https://huggingface.co/Novaciano/SEX_ROLEPLAY-3.2-1B) as a base.

### Models Merged

The following models were included in the merge:
* [Novaciano/Alice-In-The-Dark-RP-NSFW-3.2-1B](https://huggingface.co/Novaciano/Alice-In-The-Dark-RP-NSFW-3.2-1B)
* [CodeAtCMU/Llama-3.2-1B-GenerativePerturbations_full_sft_code_data_120K_imaginary](https://huggingface.co/CodeAtCMU/Llama-3.2-1B-GenerativePerturbations_full_sft_code_data_120K_imaginary)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: CodeAtCMU/Llama-3.2-1B-GenerativePerturbations_full_sft_code_data_120K_imaginary
    parameters:
      weight: 1.0
      density: 0.9
  - model: Novaciano/Alice-In-The-Dark-RP-NSFW-3.2-1B
    parameters:
      weight: 1.0
      density: 0.9
merge_method: sce
base_model: Novaciano/SEX_ROLEPLAY-3.2-1B
parameters:
  normalize: true
  int8_mask: true
  rescale: true
  filter_wise: false
  smooth: false
  allow_negative_weights: false
  lambda: 1.0
  select_topk: 0.1
tokenizer:
  source: union
chat_template: auto
dtype: bfloat16
out_dtype: bfloat16
```