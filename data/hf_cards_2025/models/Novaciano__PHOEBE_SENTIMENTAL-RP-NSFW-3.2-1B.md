---
datasets:
- syvai/emotion-reasoning
- marcuscedricridia/unAIthical-ShareGPT-deepclean-sharegpt
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

# Lucifer's Series: Phoebe Sentimental 3.2 1b

![image/png](https://mitologia.guru/wp-content/uploads/2019/02/phoebe-diosa.jpg)

# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details

This model is a sentimental variation of the model Lucifer 3.2 1B. Ideal for creative writing, roleplay games or teapeutic conversations without limitations.

### Merge Method

This model was merged using the [Arcee Fusion](https://arcee.ai) merge method using [Novaciano/LUCIFER-3.2-1B](https://huggingface.co/Novaciano/LUCIFER-3.2-1B) as a base.

### Models Merged

The following models were included in the merge:
* [syvai/emotion-reasoning-1b](https://huggingface.co/syvai/emotion-reasoning-1b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
dtype: float32
out_dtype: bfloat16
merge_method: arcee_fusion
base_model: Novaciano/LUCIFER-3.2-1B
models:
    - model: Novaciano/LUCIFER-3.2-1B
      parameters:
        weight:
          - filter: mlp
            value: [1, 2]
          - value: 1
    - model: syvai/emotion-reasoning-1b
      parameters:
        weight:
          - filter: lm_head
            value: 1
          - value: [1, 0.5]
```
