---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- RolePlay
size_categories:
- 1K<n<10K
---

# Sonnet-RolePlay

#### This dataset is the processed version of [Gryphe/Sonnet3.5-Charcard-Roleplay](https://huggingface.co/datasets/Gryphe/Sonnet3.5-Charcard-Roleplay).   
As the orginal dataset README described, many of the conversations are highly NSFW, so be warned

---

#### Processing Steps:

1. Converted from ShareGPT to ChatML
2. Replaced all `{{user}}` with a random first name, similar to how we processed [PIPPA](https://huggingface.co/datasets/chimbiwide/pippa).

---

This dataset is now ready to be used as a finetuning dataset.