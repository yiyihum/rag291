---
base_model: ibm-granite/granite-4.0-micro
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- en
tags:
- medical
- instruction-tuned
- jepa-llm
- grpo
- dpo-like
- personas
- mergekit
- arcee-fusion
- openmed
- gguf
- q8
- q4
- q2
---

# openmed-community/granite-4.0-micro-OpenMed-GGUF

**Granite 4.0 Micro (≈3B) tuned for medical education & instruction following.**  
Recipe: **JEPA-LLM SFT on medmcqa-hard + personas augmentation → GRPO on medmcqa-hard**; finalized with **Arcee Fusion** merge back into the IBM base.

> ⚠️ **Medical safety**  
> This model is **not** a clinician and may hallucinate. **Do not** use for diagnosis or treatment. Use under qualified medical supervision only.

---

## TL;DR

- **Base:** [`ibm-granite/granite-4.0-micro`](https://huggingface.co/ibm-granite/granite-4.0-micro) — 3B long-context instruct model (Apache-2.0). Includes a structured chat template and tool-calling examples.
- **Training (high-level):**
  1) **JEPA-LLM SFT (400 steps, bs=64)** on **`mkurman/medmcqa-hard`** plus **instruction-following personas** from **`allenai/tulu-3-sft-personas-instruction-following`**.
  2) **GRPO** (group-relative PPO) on **`mkurman/medmcqa-hard`**, bs **64/128**, **8 generations per item** (critic-free RL optimizing verifiable correctness).
  3) **Model merge:** **Arcee MergeKit** with `merge_method: arcee_fusion` to preserve base calibration while keeping domain gains.
- **Infra:** Trained/evaluated on **AMD Instinct MI300X** via **Hot AISLE** credits — thanks!

---

## What’s inside

### 1) JEPA-LLM stage (supervised)
- **JEPA-LLM** objective, see repo: [mkurman/jepa-llm](https://github.com/mkurman/jepa-llm), used as an auxiliary signal during SFT to bias toward stable, representation-level learning rather than pure next-token fitting; run for **400 steps** on **MedMCQA-hard** with **Personas augmentation** from **Tulu-3 personas** (adds constraint-following behaviors and improves coverage of IFEval-style requirements).

### 2) GRPO stage (reinforcement learning)
- **GRPO** replaces the critic with group baselines, enabling efficient multi-sample training; we generate **8 candidates per item** and reward answer correctness / format checks.

### 3) Merge & finalize
- **Arcee Fusion** in **MergeKit** to selectively fuse with the original Granite 4.0 Micro (avoids over-averaging from naive merges and tends to keep base calibration).

---

## Intended use & limitations

**Intended:** medical **research**, concept review, exam-style Q&A, instruction-following research, and tool-augmented demos.  
**Out of scope:** autonomous clinical decisions, prescription generation, or guideline updates without retrieval/RAG.

---

## Results

| Metric                      | granite-4.0-micro-OpenMed  | granite-4.0-micro         |
| ----------------------------| -------------------------: | ------------------------: |
| mmlu                        |                  **63.17** |                     62.48 |
| leaderboard_mmlu_pro        |                  **33.06** |                     32.78 |

| leaderboard_ifeval          | granite-4.0-micro-OpenMed  | granite-4.0-micro         |
| ----------------------------| -------------------------: | ------------------------: |
| inst_level_loose_acc        |                  **85.97** |                     85.25 |
| inst_level_strict_acc       |                  **84.05** |                     82.97 |
| prompt_level_loose_acc      |                  **79.67** |                     78.74 |
| prompt_level_strict_acc     |                  **77.45** |                     76.16 |


**Author’s harness notes:** EleutherAI `lm-evaluation-harness` with Granite’s chat template and batch size 8. 

---

## Quickstart (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "openmed-community/granite-4.0-micro-OpenMed"
tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
  {"role": "system", "content": "You are a careful medical assistant. Cite sources and warn this is not medical advice."},
  {"role": "user", "content": "Cellulitis vs erysipelas: give 3 bullet differences and 1 caution."}
]
prompt = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0], skip_special_tokens=True))
````

> **Tool-calling:** Granite’s card includes function-calling examples;
> 
---

## Reproduce key evals (example)

```bash
# Classic MMLU (5-shot typical)
lm_eval --model hf \
  --model_args pretrained=openmed-community/granite-4.0-micro-OpenMed,parallelize=True \
  --tasks mmlu --batch_size 8 --apply-chat-template

# MMLU-Pro (10-choice, harder)
lm_eval --model hf \
  --model_args pretrained=openmed-community/granite-4.0-micro-OpenMed,parallelize=True \
  --tasks leaderboard_mmlu_pro --batch_size 8 --apply-chat-template

# IFEVAL (verifiable instruction following)
lm_eval --model hf \
  --model_args pretrained=openmed-community/granite-4.0-micro-OpenMed,parallelize=True \
  --tasks leaderboard_ifeval --batch_size 8 --apply-chat-template
```

---

## Data & training notes

* **MedMCQA-Hard (train split)** for domain supervision and RL rewards;.
* **Tulu-3 personas** for instruction-following with constraint taxonomy inspired by IFEVAL.
* **JEPA-LLM**: based on the emerging **LLM-JEPA** objective (representation-space training). See the paper for context and motivation.
* **GRPO**: efficient for multi-sample training.
* **Privacy:** no PHI to the best of our knowledge; please report issues.

---

## Commentary on results

> **Why gains are modest:** Granite-4.0-Micro is already a **well-calibrated, strongly aligned** 3B instruct model with robust instruction-following and tool-use out of the box. In that regime, **headroom on popular benchmarks is limited**, and naive tuning often **degrades** base behaviors (calibration, safety, IF). The combination used here—**JEPA-LLM** (to stabilize representations), **personas SFT** (to preserve IF constraints), **GRPO** with **verifiable rewards**, and **Arcee Fusion**—appears to **nudge** the model to measurable improvements **without sacrificing** base calibration, but the effect sizes remain small, which is consistent with Granite’s strong baseline. In short: *we’re operating near the model’s alignment ceiling; targeted gains are possible, sweeping jumps are unlikely without larger capacity or richer supervision.*

---

## Acknowledgments

* **IBM Granite** team for the base model & docs (Apache-2.0).
* **AllenAI Tulu-3** for personas datasets.
* **Arcee** for MergeKit and **Arcee Fusion**.
* **Hot Aisle** for MI300X credits :heart:, link: [https://hotaisle.xyz/](https://hotaisle.xyz/).

---

## Citation

* IBM Granite 4.0 Micro model card [1](https://huggingface.co/ibm-granite/granite-4.0-micro).
* MedMCQA-Hard [2](https://huggingface.co/datasets/mkurman/medmcqa-hard).
* Tulu-3 personas dataset [3](https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following).
* LLM-JEPA paper [4](https://arxiv.org/abs/2509.14252) and our implementation repository [5](https://github.com/mkurman/jepa-llm).
* MergeKit & Arcee Fusion [6](https://github.com/arcee-ai/mergekit).