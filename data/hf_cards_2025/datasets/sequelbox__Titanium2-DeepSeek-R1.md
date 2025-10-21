---
license: apache-2.0
tags:
- titanium
- chat
- chat-instruct
- synthetic
- conversational
- python
- dev-ops
- devops
- terraform
- docker
- jenkins
- shell
- bash
- azure
- aws
- gcp
- cloud
- problem-solving
- expert
- architect
- engineer
- developer
- instruct
- titanium
- creative
- analytical
- reasoning
- rational
- deepseek
- r1
- 685b
language:
- en
task_categories:
- text-generation
size_categories:
- 10K<n<100K
---
**[Click here to support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**

**Titanium2-DeepSeek-R1** is a dataset focused on architecture and DevOps, testing the limits of [DeepSeek R1's](https://huggingface.co/deepseek-ai/DeepSeek-R1) architect and coding skills!

This dataset contains:

- 32.4k synthetically generated prompts focused on architecture, cloud, and DevOps. All responses are generated using [DeepSeek R1.](https://huggingface.co/deepseek-ai/DeepSeek-R1) Primary areas of expertise are architecture (problem solving, scenario analysis, coding, full SDLC) and DevOps (Azure, AWS, GCP, Terraform, shell scripts) 
- Synthetic prompts are generated using [Llama 3.1 405b Instruct.](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct)
- Responses demonstrate the reasoning capabilities of DeepSeek's 685b parameter R1 reasoning model.

Thinking tags have been removed for response consistency; otherwise, **responses have not been filtered or edited at all:** the Titanium dataset strives to accurately represent the R1 model. Potential issues may include inaccurate answers and infinite thought loops. Titanium is presented as-is to be used at your discretion.

Users should consider applying their own sub-filtering and manual examination of the dataset before use in training.

Do as you will.