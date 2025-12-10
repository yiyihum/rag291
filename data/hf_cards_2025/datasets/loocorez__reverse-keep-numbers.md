---
license: mit
language:
- en
tags:
- sft
- chat
- synthetic
- reverse-text
- keep-numbers
task_categories:
- text-generation
---

# Reverse Keep Numbers

Synthetic chat-style SFT dataset where the assistant reverses non-digit characters while keeping digits in-place and unchanged.

- Input format: OpenAI-style chat messages in `prompt` and `completion`.
- Per-token reversal: whitespace-delimited tokens; each token reversed independently (digits fixed).
- Splits: `train` (2596 rows), `validation` (251 rows).