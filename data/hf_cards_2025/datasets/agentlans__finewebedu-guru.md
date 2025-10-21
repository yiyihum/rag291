---
language:
- en
pretty_name: FineWebEdu-Guru
tags:
- educational
- instruction-tuning
- expert-model
- llm-training
- fineweb
task_categories:
- text-generation
- question-answering
configs:
- config_name: pretrain
  data_files:
  - path:
    - pretrain.jsonl.zst
    split: train
  default: true
- config_name: sft
  data_files:
  - path:
    - sft.jsonl.zst
    split: train
- config_name: multiple-choice
  data_files:
  - path:
    - multiple-choice.jsonl.zst
    split: train
- config_name: short-answer
  data_files:
  - path:
    - short-answer.jsonl.zst
    split: train
license: odc-by
---

# FineWebEdu-Guru

- A high-quality dataset collection for training interactive expert large language models (LLMs)
- These are general educational web content with no specific focus
- To specialize the LLMs for your own data, you'll need other models to generate the training data such as
  - [agentlans/Qwen2.5-1.5B-Refiner](https://huggingface.co/agentlans/Qwen2.5-1.5B-Refiner)
  - [agentlans/Qwen2.5-1.5B-Instruct-Conversation-Maker](https://huggingface.co/agentlans/Qwen2.5-1.5B-Instruct-Conversation-Maker)
  - [agentlans/Qwen2.5-1.5B-Instruct-Multiple-Choice-Maker](https://huggingface.co/agentlans/Qwen2.5-1.5B-Instruct-Multiple-Choice-Maker)
  - [agentlans/Qwen2.5-1.5B-Instruct-Short-Answer-Maker](https://huggingface.co/agentlans/Qwen2.5-1.5B-Instruct-Short-Answer-Maker)

## Dataset Description

This collection contains:
1. **Pretraining data**: An edited subset of [FineWebEdu](https://huggingface.co/datasets/agentlans/finewebedu-refinement) educational texts.
2. **Supervised fine-tuning data (SFT)**: 
   - Expert-style conversational data from [FineWebEdu-Conversation](https://huggingface.co/datasets/agentlans/finewebedu-conversation) with randomly selected system prompts directing AI to respond as domain experts.
   - ShareGPT-like format
3. **Short answer and multiple choice questions and answers**:
   - From [agentlans/finewebedu-multiple-choice](https://huggingface.co/datasets/agentlans/finewebedu-multiple-choice) and [agentlans/finewebedu-short-answer](https://huggingface.co/datasets/agentlans/finewebedu-short-answer)
   - In the style of [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
   - To familiarize the LLM with the evaluation format

## Intended Use
- Training expert-style LLMs
- Instruction tuning for domain-specific applications
- Developing interactive educational assistants

## How to Use
```python
from datasets import load_dataset

# Load pretraining data
pretrain = load_dataset("agentlans/FineWebEdu-Guru", "pretrain")

# Load fine-tuning data
sft = load_dataset("agentlans/FineWebEdu-Guru", "sft")
```

## Ethical Considerations
While the data has been filtered for quality, users should:
- Evaluate potential biases in model outputs
- Consider domain-specific accuracy requirements
- Review generated content for factual correctness

## Citation
If using this dataset, please reference both:
1. The original FineWebEdu dataset
2. This refinement work
3. Other models that you may have used