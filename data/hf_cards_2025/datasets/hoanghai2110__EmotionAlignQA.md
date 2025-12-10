---
license: apache-2.0
language:
- en
tags:
- empathy
- alignment
- rlhf
- dialogue
- ai-chatbot
- preference-ranking
pretty_name: Empathic Dialogue Choices
task_categories:
- text-generation
- reinforcement-learning
dataset_type: dataset
size_categories:
- 1K<n<10K
---

# Empathic Dialogue Choices

This is a small dataset to support training and evaluation of conversational AI in emotionally sensitive contexts.

Each sample contains:
- a user input
- two assistant responses
- a human preference
- optional rubric scoring
- metadata such as tone, formality, and topic

Useful for tasks like:
- supervised fine-tuning (SFT)
- preference modeling (for RLHF or DPO)
- safe response generation
- tone- or style-controlled generation

## License

Apache 2.0 — free for research and commercial use.  
Attribution appreciated: [@hoanghai2110](https://huggingface.co/hoanghai2110)