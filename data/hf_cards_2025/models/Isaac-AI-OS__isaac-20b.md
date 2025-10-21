---
license: apache-2.0
tags:
- evaluation
- reproducibility
- agentic-lite
- code
- swe-bench
pipeline_tag: text-generation
---

# ISAAC OS — Neural v1 (Deterministic Eval, Agentic-Lite)

**Model ID:** `isaac-20b`
**Policy Version:** `agentic-lite-v1`
**Docker Digest:** `isaac-hf@sha256:6fc9f0d85dfe56daba8fc92496718226f056014b3e84ee7a823df1d9271a57c0`

## Results (subset scale)
| Benchmark | Split | Metric | Score |
|---|---|---:|---:|
| HumanEval | N=5 | pass@1 | **0.60** |
| MBPP | N=5 | pass@1 | **0.80** |
| SWE-Bench Lite | 1/1 resolved | model pass@1 | — |
|  |  | resolved via **fallback_dataset_patch** | **1 / 1** |

## Reproducibility
Agentic-Lite clamps (temperature=0, top_p=0, top_k=1, n=1, seed=7), deterministic tools (no concurrency, max_steps=6), first-line QA & code-only normalization; one-node eval.

## Artifacts & Manifest
- LM: https://huggingface.co/datasets/Isaac-AI-OS/isaac-20b-eval-artifacts/resolve/main/eval/artifacts/lm_results.norm.json
- Code summary: https://huggingface.co/datasets/Isaac-AI-OS/isaac-20b-eval-artifacts/resolve/main/eval/artifacts/code/summary.json
- SWE-Lite: https://huggingface.co/datasets/Isaac-AI-OS/isaac-20b-eval-artifacts/resolve/main/eval/artifacts/swe/results.json
- Manifest: https://huggingface.co/datasets/Isaac-AI-OS/isaac-20b-eval-artifacts/resolve/main/eval/artifacts/manifest.json
