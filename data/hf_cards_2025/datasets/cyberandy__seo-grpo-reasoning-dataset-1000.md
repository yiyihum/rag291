---
license: cc-by-nc-4.0
language:
- en
tags:
- seo
- reasoning
- instruction-tuning
- grpo
- rlft
- synthetic
- llm-as-judge
- wordlift
- seontology
pretty_name: SEO GRPO Reasoning Dataset (1k Examples)
---

# SEO GRPO Reasoning Dataset (1k Examples)

## Dataset Description

This dataset contains 1,000 examples designed for fine-tuning language models using Reinforcement Learning (specifically Group Policy Optimization - GRPO) on Search Engine Optimization (SEO) reasoning tasks. It was created as part of research within the **WordLift Lab** to explore teaching models structured reasoning guided by SEO principles.

The dataset focuses on prompting a model to generate both a step-by-step `<reasoning>` process and a final `<answer>` for various SEO scenarios. Crucially, it includes a pre-computed `reward` score for each example, intended for use in RL fine-tuning algorithms like GRPO or PPO.

**Connection to SEOntology:** The generation prompts and the evaluation criteria used to create the reward scores were informed by concepts and vocabulary from the **SEOntology project (https://github.com/seontology/)**, specifically the `seovoc` vocabulary ([https://w3id.org/seovoc/](https://w3id.org/seovoc/)).

## Dataset Creation

The dataset was generated using a multi-stage process:

1.  **Scenario Definition:** A diverse set of SEO task templates was created, covering areas such as:
    *   Meta Description Optimization
    *   Internal Link Suggestion
    *   Query Trend Analysis
    *   Schema.org Type Suggestion
    *   Named Entity Identification (SEO context)
    *   Title Tag Optimization
    *   Keyword Intent Classification
    *   Content Gap Analysis (Keywords)
    *   Robots.txt Suggestion
    *   Canonical Tag Decision
    *   SERP Feature Analysis
    *   E-E-A-T Assessment/Suggestion
    *   GMB Optimization Suggestion
    *   Product Schema Enhancement
    *   *(Potentially others, like Content Revision based on QA)*
2.  **Synthetic Generation:** The Gemini 1.5 Pro API was used to generate initial responses (including `<reasoning>` and `<answer>` sections) based on prompts derived from the templates.
3.  **LLM-as-a-Judge Evaluation:** Each generated response was evaluated by Gemini 1.5 Pro, acting as an SEO expert judge. The judge used criteria assessing format correctness, accuracy, relevance, logical reasoning, and appropriate use of SEO/SEOntology concepts (with `seovoc.owl` provided as context) to assign a single `reward_score` between 0.0 and 1.0.
4.  **Final Formatting:** The data was processed into the final format suitable for `trl.GRPOTrainer`.

## Dataset Structure

The dataset contains two main columns:

*   `prompt` (string): The fully formatted input prompt string intended for the language model. This typically includes a system prompt defining the task and expected output format (`<reasoning>`, `<answer>`), followed by the user's specific request based on one of the SEO task templates. The string is ready to be tokenized, including necessary control tokens (e.g., `<bos>`, `<start_of_turn>`, `<end_of_turn>`) based on the chat template used during preparation (likely Gemma 3).
*   `reward` (float64): The pre-computed reward score assigned by the LLM-as-a-Judge during dataset creation, ranging from 0.0 (poor) to 1.0 (excellent).

## Intended Use

This dataset is primarily intended for **training language models using Reinforcement Learning algorithms like GRPO or PPO**. The goal is to teach models to generate structured, reasoned responses for SEO tasks.

It is **not** designed for standard Supervised Fine-Tuning (SFT), as it lacks the "ground truth" completions paired with prompts; instead, it provides prompts and the *reward* associated with completions generated during the dataset creation phase.

## Limitations

*   **Synthetic Data:** The prompts and initial responses are synthetically generated and may not perfectly reflect all real-world complexities.
*   **LLM-as-a-Judge:** Reward scores are based on the evaluation capabilities of the specific judge model (Gemini 1.5 Pro) and the defined prompt/criteria. These scores are subjective and might not perfectly capture all nuances of SEO quality.
*   **Dataset Size:** While larger than the initial 100-example version, 1000 examples may still be relatively small for achieving high levels of generalization across all covered SEO tasks.
*   **Bias:** Inherits biases from the models used in generation (Gemini 1.5 Pro) and evaluation (Gemini 1.5 Pro).

## Citation

If you use this dataset, please cite [WordLift](https://wordlift.io) and the SEOntology project.