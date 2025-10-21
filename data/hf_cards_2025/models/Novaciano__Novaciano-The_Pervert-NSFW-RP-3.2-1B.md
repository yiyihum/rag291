---
base_model:
- Novaciano/Novaciano_Perturbations-3.2-1B
- bunnycore/FuseChat-3.2-1B-Creative-RP
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
library_name: transformers
tags:
- mergekit
- merge
- nsfw
- rp
- 1b
- llama
- roleplay
- creative
- erotic
- friend
- girlfriend
- perturbations
- llama-cpp
language:
- en
- es
---

# Novaciano The Pervert 3.2 - 1B

![image/png](https://i.postimg.cc/MKbC7Y4X/aifacesw-ap-b793fec8c6ffe50c9ddef12041af37c8.jpg)

## Model Overview

Explora lo desconocido con Novaciano, tu compañero versátil y cautivador diseñado exclusivamente para crear partidas de roleplay perturbadoras. Con un enfoque en la narrativa inmersiva y la interacción dinámica, Novaciano te invita a sumergirte en mundos oscuros y complejos. Sorprendentemente coherente y adaptable para un modelo de 1B, es ideal para aquellos que buscan experiencias de rol y narrativa únicas y desafiantes.

![image/png](https://i.imgur.com/b1zExym.png)

- Si usas KoboldAI selecciona el preset **Llama 3 Chat**.

## Key Features

- **Capacidades de Asistente General**: Novaciano The Pervert puede crear historias altamente perturbadoras y proporcionar información útil, pero con un toque oscuro y perturbador. Está diseñado para crear experiencias de conversación únicas y cautivadoras, que pueden incluir temas maduros y complejos.

## Disclaimer

Novaciano The Pervert es un mix de Novaciano Perturbations mezclado con el modelo FuseChat de Bunnycore para pulir el sistema roleplay. Está diseñado para entretenimiento y propósitos de rol. Sus respuestas se generan en función de la entrada proporcionada y pueden no ser adecuadas para todos los públicos. Se recomienda usarlo de manera responsable y respetuosa.

# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

### Merge Method

This model was merged using the [Arcee Fusion](https://arcee.ai) merge method using [bunnycore/FuseChat-3.2-1B-Creative-RP](https://huggingface.co/bunnycore/FuseChat-3.2-1B-Creative-RP) as a base.

### Models Merged

The following models were included in the merge:
* [Novaciano/Novaciano_Perturbations-3.2-1B](https://huggingface.co/Novaciano/Novaciano_Perturbations-3.2-1B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float32
out_dtype: bfloat16
merge_method: arcee_fusion
base_model: bunnycore/FuseChat-3.2-1B-Creative-RP
models:
    - model: bunnycore/FuseChat-3.2-1B-Creative-RP
      parameters:
        weight:
          - filter: mlp
            value: [1, 2]
          - value: 1
    - model: Novaciano/Novaciano_Perturbations-3.2-1B
      parameters:
        weight:
          - filter: lm_head
            value: 1
          - value: [1, 0.5]
```
