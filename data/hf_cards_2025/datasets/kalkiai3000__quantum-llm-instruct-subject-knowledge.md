---
pretty_name: Quantum LLM Instruct with Subject Knowledge
license: mit
tags:
- quantum
- instruction-tuning
- llm
- physics
- knowledge-augmentation
size_categories:
- 1K<n<10K
---

# kalkiAI3000/quantum-llm-instruct-subject-knowledge

This dataset augments `BoltzmannEntropy/QuantumLLMInstruct` with a new field `subject_knowledge`,
automatically generated from each example’s `main_domain`, `sub_domain`, and `problem` using GPT-5.

## Contents

- `train.json` (rows: 5150): Preserves original fields and adds:
  - `subject_knowledge` (string): 3–6 concise lines summarizing definitions, governing equations,
    assumptions/scales, and a typical solution strategy relevant to the domain/sub-domain and the given problem.

## Motivation

- Improve instruction-tuning for quantum/physics reasoning by injecting targeted knowledge alongside each prompt.
- Help models acquire reusable conceptual scaffolding that can transfer to novel problems.

## Generation details

- Model: Azure OpenAI `gpt-4o`
- Prompt used the tuple (main_domain, sub_domain, problem) to produce short, non-markdown guidance.
- The knowledge is not a worked solution.

## Intended uses

- Fine-tuning LLMs for physics/quantum problem solving.
- Using `subject_knowledge` as auxiliary context during SFT/RLHF.

## License

MIT
