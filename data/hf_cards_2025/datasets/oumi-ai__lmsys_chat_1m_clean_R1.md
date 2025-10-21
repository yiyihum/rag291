---
task_categories:
- text-generation
language:
- en
size_categories:
- 100K<n<1M
license: apache-2.0
tags:
- general
---

[![oumi logo](https://oumi.ai/logo_lockup_black.svg)](https://github.com/oumi-ai/oumi)
[![Made with Oumi](https://badgen.net/badge/Made%20with/Oumi/%23085CFF?icon=https%3A%2F%2Foumi.ai%2Flogo_dark.svg)](https://github.com/oumi-ai/oumi)

[![Documentation](https://img.shields.io/badge/Documentation-oumi-blue.svg)](https://oumi.ai/docs/en/latest/index.html)
[![Blog](https://img.shields.io/badge/Blog-oumi-blue.svg)](https://oumi.ai/blog)
[![Discord](https://img.shields.io/discord/1286348126797430814?label=Discord)](https://discord.gg/oumi)

# oumi-ai/lmsys_chat_1m_clean_R1

**lmsys_chat_1m_clean_R1** is a text dataset designed to train Conversational Language Models with **DeepSeek-R1 level reasoning**.
Prompts were pulled from [LMSYS](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) and filtered to [lmsys_chat_1m_clean](https://huggingface.co/datasets/OpenLeecher/lmsys_chat_1m_clean), and responses were taken from **[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)** without additional filters present.
We release **lmsys_chat_1m_clean_R1** to help enable the community to develop the best fully open reasoning model!

[lmsys_chat_1m_clean](https://huggingface.co/datasets/OpenLeecher/lmsys_chat_1m_clean) queries with responses generated from [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)

- **Curated by:** [Oumi AI](https://oumi.ai/) using Oumi inference on [Parasail](https://www.parasail.io/)
- **Language(s) (NLP):** English
- **License:** [Apache 2.0](https://opensource.org/license/apache-2-0)
- **Demo:** [See the MiniMath notebook for a similar example](https://github.com/oumi-ai/oumi/blob/307436bd98706cb9ce7b0bbf31204770af2b7c8c/notebooks/Oumi%20-%20MiniMath-R1-1.5B.ipynb)

## Uses

<!-- This section describes suitable use cases for the dataset. -->
Use this dataset for supervised fine-tuning of LLMs by including it into a training mixture for creating an R1-like model.

## Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
This dataset covers a broad coverage of use-cases documented in the [original dataset](https://huggingface.co/datasets/OpenLeecher/lmsys_chat_1m_clean), but is likely reflective of only one particular set of users (LMSYS Chatbot Arena submissions)

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
```
{
  # Unique conversation identifier, tied back to lmsys_chat_1m_clean samples
  "conversation_id": str,

  # The user turn/prompt
  "prompt": str,

  # The assistant (DeepSeek R1) response
  # Includes the thought trace which is wrapped in <think> and </think> tags
  "response": str,  

  # Data formatted to user + assistant turns in chat format
  # Example: [{'role': 'user', 'content': ...}, {'role': 'assistant', 'content': ...}]
  "messages": list[dict[str, str]],

  # Metadata for sample
  "metadata": dict[str, ...],  
}
```

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->
To enable the community to develop a fully-open state-of-the-art Foundational Language Model, we've produced and released this dataset to serve as part of the foundation of reasoning data for the model. It was produced using the Oumi’s inference capabilities on Parasail.

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->
Queries were sourced from [lmsys_chat_1m_clean](https://huggingface.co/datasets/OpenLeecher/lmsys_chat_1m_clean) which is data filtered from the original LMSYS Chat 1M dataset.

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->
* Responses were collected via Oumi's batch inference support for [Parasail](https://parasail.io/).
* Samples which could not be parsed were discarded (<100).
* All other samples include metadata indicating if they are complete or not (which was determined by whether or not a `</think>` token is present)

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->
Data is not known or likely to contain any personal, sensitive, or private information, but it is possible due to the nature of the data (submitted queries from LMSYS Chatbot Arena)

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

1. The source prompts are from [lmsys_chat_1m_clean](https://huggingface.co/datasets/OpenLeecher/lmsys_chat_1m_clean) `conversations` column and may reflect any biases in the data filtration process.
2. Some prompts contained within may be adversarial or controversial in their queries or content.
3. The responses produced will likely be reflective of any biases or limitations produced by DeepSeek-R1.

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@misc{lmsysChat1mCleanR12025,
  author = {Jeremiah Greer},
  title = {lmsys_chat_1m_clean_R1 Dataset},
  month = {February},
  year = {2025},
  url = {https://huggingface.co/datasets/oumi-ai/lmsys_chat_1m_clean_R1}
}

@software{oumi2025,
  author = {Oumi Community},
  title = {Oumi: an Open, End-to-end Platform for Building Large Foundation Models},
  month = {January},
  year = {2025},
  url = {https://github.com/oumi-ai/oumi}
}
```