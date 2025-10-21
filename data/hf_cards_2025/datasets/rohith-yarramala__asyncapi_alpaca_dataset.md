---
dataset: rohith-yarramala/asyncapi_alpaca_dataset
language:
- en
license: mit
tags:
- asyncapi
- event-driven
- api
- yaml
- code-explanation
- instruction-tuning
- alpaca-format
size_categories:
- 1K<n<10K
task_categories:
- text-generation
- text2text-generation
- other
pretty_name: AsyncAPI Alpaca Dataset
description: 'A fine-tuning dataset based on the Alpaca format for training LLMs to
  understand and generate AsyncAPI-related content. The dataset includes prompts,
  instructions, and completions extracted and synthesized from AsyncAPI documentation,
  GitHub discussions, tutorials, and code examples. It is ideal for training models
  in event-driven API development, code generation, and instruction following within
  the AsyncAPI domain.

  '
dataset_info:
  features:
  - instruction: A task or request related to AsyncAPI (e.g., "Explain the difference
      between publish and subscribe in AsyncAPI.")
  - input: Optional context or YAML/JSON snippet to accompany the instruction.
  - output: The expected response or answer to the instruction.
  splits:
  - train: 8000
  - test: 2000
  dataset_size: 1.2MB
source_datasets:
- AsyncAPI Documentation
- GitHub AsyncAPI Discussions
- AsyncAPI Tutorials and Community Q&A
citation: "@misc{asyncapi-alpaca-dataset,\n  author = {Rohith Yarramala},\n  title\
  \ = {AsyncAPI Alpaca Dataset},\n  year = {2025},\n  url = {https://huggingface.co/datasets/rohith-yarramala/asyncapi_alpaca_dataset}\n\
  }"
---

# AsyncAPI Alpaca Dataset

A high-quality instruction-tuned dataset based on [AsyncAPI](https://www.asyncapi.com/) specifications and event-driven architecture tutorials, designed for training and fine-tuning large language models to understand, explain, and debug AsyncAPI-related content.

## ✨ Dataset Overview

This dataset contains **Alpaca-style instruction data** (`instruction`, `input`, `output`) generated from real-world AsyncAPI documentation, tutorials, and specifications.

Each entry is designed to help language models learn:
- AsyncAPI specification structure
- YAML configuration patterns
- Code explanation and debugging
- AsyncAPI best practices
- Interactive code correction and generation

Example entry:
```json
{
  "instruction": "Explain the 'channels' section from 'AsyncAPI 2.0 Pub/Sub Tutorial'",
  "input": "",
  "output": "The `channels` section defines available message paths for communication. In a pub/sub setup, channels represent topics the server can subscribe to or publish on..."
}
📁 Dataset Structure
Each entry in the dataset includes:

instruction: What the model is being asked to do.

input: Optional code or YAML input.

output: The expected answer from the model.

All examples are formatted for supervised fine-tuning and are compatible with LLaMA, Mistral, Falcon, Gemma, and other chat-tuned models.

🧠 Data Sources
The dataset was built from:

Scraped AsyncAPI documentation/tutorials

Extracted YAML code snippets

Generated explanation and debugging prompts using AI (e.g., Mistral 7B)

Manual and AI-assisted augmentation using instruction tuning patterns

🛠️ How It Was Built
Parsed AsyncAPI content (JSON tutorials, YAML blocks, question/answer pairs).

Created instruction, input, output triplets using:

Manual transformation

AI generation using mistralai/Mistral-7B-Instruct-v0.3 via Hugging Face Transformers

Validated output formatting

Saved as JSON and uploaded to Hugging Face

📊 Dataset Stats
🧾 Format: JSON (Alpaca-style)

📦 Entries: ~3,000+

🧠 Instruction Types:

Explain this section

Debug YAML spec

Fix errors in AsyncAPI file

Generate AsyncAPI code

Compare JSON vs YAML

🔍 Use Cases
Fine-tune LLMs to understand AsyncAPI and event-driven specs

Chatbots or developer assistants for real-time API guidance

Code explanation and correction in async communication systems

Academic or commercial research in developer LLMs

🧪 Recommended Models
mistralai/Mistral-7B-Instruct-v0.3

meta-llama/Llama-2-7b-chat

tiiuae/falcon-7b-instruct

HuggingFaceH4/zephyr-7b-alpha

📄 License
This dataset is licensed under the MIT License. Content and examples were derived from open and public AsyncAPI documentation.

🤝 Contributions
Created and maintained by @rohith-yarramala.
If you’d like to contribute additional examples or help expand the dataset, feel free to open an issue or pull request!

