---
license: apache-2.0
license_link: https://huggingface.co/Gensyn/Qwen2.5-0.5B-Instruct/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-0.5B
tags:
- chat
- rl-swarm
- gensyn
library_name: transformers
---

# Qwen2.5-0.5B-Instruct

## Introduction
This model is intended for use in the [Gensyn RL Swarm](https://www.gensyn.ai/articles/rl-swarm), to finetune locally using peer-to-peer reinforcement learning post-training.

Once finetuned, the model can be used as normal in any workflow, for details on how to do this please refer to the [original model documentation](https://qwen.readthedocs.io/en/latest/).

For more details on the original model, please refer to the original repository [here](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct).

This repo contains an **unmodified version** of the instruction-tuned 0.5B Qwen2.5 model, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias and tied word embeddings
- Number of Parameters: 0.49B
- Number of Paramaters (Non-Embedding): 0.36B
- Number of Layers: 24
- Number of Attention Heads (GQA): 14 for Q and 2 for KV
- Context Length: Full 32,768 tokens and generation 8192 tokens

## Requirements

This model is intended for use in the [Gensyn RL Swarm](https://www.gensyn.ai/articles/rl-swarm) system, for details on model requirements when using outside of a swarm, refer to the original Qwen repo [here](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct).

## Quickstart

To deploy this model into a swarm and/or participate in the Gensyn Testnet, follow the instructions in the [RL Swarm repository](https://github.com/gensyn-ai/rl-swarm), read about the [testnet](https://www.gensyn.ai/testnet), read the [RL Swarm overview](https://www.gensyn.ai/articles/rl-swarm), and/or read the [RL Swarm technical report](https://github.com/gensyn-ai/paper-rl-swarm/blob/main/latest.pdf).
