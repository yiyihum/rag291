---
license: apache-2.0
tags:
- dag-reasoning
- chat
- chat-instruct
- synthetic
- conversational
- directed-acyclic-graph
- graph
- logic
- analysis
- programming
- knowledge
- root-cause-analysis
- economics
- business
- business-management
- finance
- law
- supply-chain
- logistics
- software-engineering
- cybersecurity
- architecture
- energy
- politics
- problem-solving
- expert
- creative
- analytical
- reasoning
- rational
- deepseek
- r1
- r1-0528
- deepseek-r1-0528
- 685b
- music
- art
language:
- en
task_categories:
- text-generation
- feature-extraction
size_categories:
- 1K<n<10K
pretty_name: DAG-Reasoning
---
**[Click here to support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**

**DAG-Reasoning-DeepSeek-R1-0528** is a dataset focused on analysis and reasoning, creating directed acyclic graphs testing the limits of [DeepSeek R1 0528's](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) graph-reasoning skills!

This dataset contains:

- 4.08k synthetically generated prompts to create directed acyclic graphs in response to user input, with all responses generated using [DeepSeek R1 0528.](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)
- All responses contain a multi-step thinking process to perform effective analysis, followed by a user response that contains the DAG as immediate output in the AI response for the user to consume. The graph utilizes our DAG Reasoning Format - nodes, edges, and graph_metadata in JSON format.
- DAG prompts utilize a variety of subjects to maximize general performance; prompt subjects include programming, science, business, economics, finance, law, logistics, management, and a variety of others.
- Responses demonstrate the reasoning capabilities of DeepSeek's R1-0528 reasoning model, while providing a finetuning dataset for DAG Reasoning Format.

The DAG Reasoning dataset is an experimental reasoning modality. DAG Reasoning is presented as-is to be used at your discretion.

Users should consider applying their own sub-filtering and manual examination of the dataset before use in training.

Do as you will.