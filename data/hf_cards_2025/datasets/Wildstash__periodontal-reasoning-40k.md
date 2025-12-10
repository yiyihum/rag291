---
tags:
- rlhf
- kto
- dpo
- preference-learning
- alignment
- medical
- healthcare
- dental
- periodontal
- clinical-reasoning
- text-generation
- jsonl
- english
task_categories:
- text-generation
language:
- en
size_categories:
- 10K<n<100K
license: cc-by-4.0
pretty_name: Periodontal-Reasoning-40k
---

# Periodontal-Reasoning-40k

40,000 periodontal clinical reasoning examples for off-policy RLHF (KTO/DPO).

## Schema

- `prompt`: instruction or question
- `completion`: model response
- `label`: {+1, -1} preference label

## Example

```json
{"prompt": "A patient's plaque score was 35% at baseline and 1% at follow-up. Determine whether the improvement is favourable according to BSP criteria (≤20% plaque or ≥50% reduction).", "completion": "The improvement is favourable.", "label": 1}
```

## Intended use

- KTO/DPO training; SFT warm-start from `label==1`.


