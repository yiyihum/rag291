---
license: apache-2.0
tags:
- des-reasoning
- chat
- chat-instruct
- synthetic
- conversational
- discrete-event-simulation
- simulation
- SimPy
- Python
- scripting
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
- manufacturing
- telecommunications
- transportation
- healthcare
- logistics
- energy
- retail
- construction
- agriculture
- information-technology
- environment
- software-engineering
- cybersecurity
- architecture
- energy
- politics
- problem-solving
- creative
- analytical
- reasoning
- rational
- deepseek
- v3.1
- deepseek-v3.1
- 685b
language:
- en
task_categories:
- text-generation
- feature-extraction
size_categories:
- 1K<n<10K
pretty_name: DES-Reasoning
---
**[Click here to support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**

**DES-Reasoning-DeepSeek-V3.1** is a dataset focused on analysis and reasoning, creating discrete event simulations testing the limits of [DeepSeek V3.1's](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) simulation, Python scripting, and analysis skills!

This dataset contains:

- 4.03k synthetically generated prompts to create discrete event simulations and analysis chat in response to user input, with all responses generated using [DeepSeek V3.1.](https://huggingface.co/deepseek-ai/DeepSeek-V3.1)
- All responses contain a multi-step thinking process to create a simulation and analysis strategy, followed by a user response that contains a SimPy Python script as immediate output in the AI response for the user to consume followed by suggestions for further analysis. The graph utilizes our DES Reasoning Format - easily readable and modifiable SimPy code followed by analysis in chat format.
- DES prompts utilize a variety of subjects to maximize general performance; prompt subjects include programming, science, business, economics, energy, finance, law, logistics, management, manufacturing, operations, supply chain, and a variety of others.
- Responses demonstrate the reasoning capabilities of DeepSeek's V3.1 reasoning skills, while providing a finetuning dataset for DES Reasoning Format.

The DES Reasoning dataset is an experimental reasoning modality. DES Reasoning is presented as-is to be used at your discretion.

Users should consider applying their own sub-filtering and manual examination of the dataset before use in training.

Do as you will.