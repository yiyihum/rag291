---
license: odc-by
size_categories:
- 1M<n<10M
task_categories:
- text-generation
- question-answering
pretty_name: WildChat-4.8M
dataset_info:
  features:
  - name: conversation_hash
    dtype: string
  - name: model
    dtype: string
  - name: timestamp
    dtype: timestamp[us]
  - name: conversation
    list:
    - name: content
      dtype: string
    - name: created
      dtype: int64
    - name: header
      struct:
      - name: accept-language
        dtype: string
      - name: user-agent
        dtype: string
    - name: hashed_ip
      dtype: string
    - name: country
      dtype: string
    - name: toxic
      dtype: bool
    - name: redacted
      dtype: bool
    - name: state
      dtype: string
    - name: language
      dtype: string
    - name: openai_id
      dtype: string
    - name: role
      dtype: string
    - name: temperature
      dtype: float64
    - name: timestamp
      dtype: timestamp[us]
    - name: token_counter
      dtype: int64
    - name: top_p
      dtype: float64
    - name: turn_identifier
      dtype: int64
    - name: system_fingerprint
      dtype: string
    - name: usage
      struct:
      - name: completion_tokens
        dtype: int64
      - name: completion_tokens_details
        struct:
        - name: reasoning_tokens
          dtype: int64
        - name: text_tokens
          dtype: int64
        - name: audio_tokens
          dtype: int64
        - name: accepted_prediction_tokens
          dtype: int64
        - name: rejected_prediction_tokens
          dtype: int64
      - name: prompt_tokens
        dtype: int64
      - name: total_tokens
        dtype: int64
      - name: prompt_tokens_details
        struct:
        - name: cached_tokens
          dtype: int64
        - name: audio_tokens
          dtype: int64
  - name: turn
    dtype: int64
  - name: language
    dtype: string
  - name: openai_moderation
    list:
    - name: categories
      struct:
      - name: harassment
        dtype: bool
      - name: harassment/threatening
        dtype: bool
      - name: harassment_threatening
        dtype: bool
      - name: hate
        dtype: bool
      - name: hate/threatening
        dtype: bool
      - name: hate_threatening
        dtype: bool
      - name: illicit
        dtype: bool
      - name: illicit/violent
        dtype: bool
      - name: illicit_violent
        dtype: bool
      - name: self-harm
        dtype: bool
      - name: self-harm/instructions
        dtype: bool
      - name: self-harm/intent
        dtype: bool
      - name: self_harm
        dtype: bool
      - name: self_harm_instructions
        dtype: bool
      - name: self_harm_intent
        dtype: bool
      - name: sexual
        dtype: bool
      - name: sexual/minors
        dtype: bool
      - name: sexual_minors
        dtype: bool
      - name: violence
        dtype: bool
      - name: violence/graphic
        dtype: bool
      - name: violence_graphic
        dtype: bool
    - name: category_applied_input_types
      struct:
      - name: harassment
        list: string
      - name: harassment/threatening
        list: string
      - name: harassment_threatening
        list: string
      - name: hate
        list: string
      - name: hate/threatening
        list: string
      - name: hate_threatening
        list: string
      - name: illicit
        list: string
      - name: illicit/violent
        list: string
      - name: illicit_violent
        list: string
      - name: self-harm
        list: string
      - name: self-harm/instructions
        list: string
      - name: self-harm/intent
        list: string
      - name: self_harm
        list: string
      - name: self_harm_instructions
        list: string
      - name: self_harm_intent
        list: string
      - name: sexual
        list: string
      - name: sexual/minors
        list: string
      - name: sexual_minors
        list: string
      - name: violence
        list: string
      - name: violence/graphic
        list: string
      - name: violence_graphic
        list: string
    - name: category_scores
      struct:
      - name: harassment
        dtype: float64
      - name: harassment/threatening
        dtype: float64
      - name: harassment_threatening
        dtype: float64
      - name: hate
        dtype: float64
      - name: hate/threatening
        dtype: float64
      - name: hate_threatening
        dtype: float64
      - name: illicit
        dtype: float64
      - name: illicit/violent
        dtype: float64
      - name: illicit_violent
        dtype: float64
      - name: self-harm
        dtype: float64
      - name: self-harm/instructions
        dtype: float64
      - name: self-harm/intent
        dtype: float64
      - name: self_harm
        dtype: float64
      - name: self_harm_instructions
        dtype: float64
      - name: self_harm_intent
        dtype: float64
      - name: sexual
        dtype: float64
      - name: sexual/minors
        dtype: float64
      - name: sexual_minors
        dtype: float64
      - name: violence
        dtype: float64
      - name: violence/graphic
        dtype: float64
      - name: violence_graphic
        dtype: float64
    - name: flagged
      dtype: bool
  - name: detoxify_moderation
    list:
    - name: identity_attack
      dtype: float64
    - name: insult
      dtype: float64
    - name: obscene
      dtype: float64
    - name: severe_toxicity
      dtype: float64
    - name: sexual_explicit
      dtype: float64
    - name: threat
      dtype: float64
    - name: toxicity
      dtype: float64
  - name: toxic
    dtype: bool
  - name: redacted
    dtype: bool
  - name: state
    dtype: string
  - name: country
    dtype: string
  - name: hashed_ip
    dtype: string
  - name: header
    struct:
    - name: accept-language
      dtype: string
    - name: user-agent
      dtype: string
  splits:
  - name: train
    num_bytes: 42645714270.23995
    num_examples: 3199860
  download_size: 15282293424
  dataset_size: 42645714270.23995
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- instruction-finetuning
---
# Dataset Card for WildChat-4.8M

## Dataset Description

- **Interactive Search Tool:** https://wildvisualizer.com  
- **WildChat paper:** https://arxiv.org/abs/2405.01470  
- **WildVis paper:** https://arxiv.org/abs/2409.03753  
- **Point of Contact:** [Yuntian Deng](https://yuntiandeng.com/)

## Dataset Description
 
- **Interactive Search Tool:** https://wildvisualizer.com  
- **WildChat paper:** https://arxiv.org/abs/2405.01470  
- **WildVis paper:** https://arxiv.org/abs/2409.03753  
- **Point of Contact:** [Yuntian Deng](https://yuntiandeng.com/)

### Dataset Summary

WildChat-4.8M is a collection of **3,199,860 conversations** between human users and ChatGPT. This version **only contains non-toxic user inputs and ChatGPT responses**, as flagged by the OpenAI Moderations API or Detoxify. It is derived from the [WildChat-4.8M-Full](https://huggingface.co/datasets/allenai/WildChat-4.8M-Full) dataset (4,743,336 conversations after minors removal from the original **4,804,190** conversations) by filtering out 1,543,476 toxic conversations. The dataset includes state, country, hashed IP addresses, request headers, and full conversation transcripts.

The dataset contains a broad spectrum of user-chatbot interactions: ambiguous requests, code-switching, topic shifts, political debates, and more. It also contains **111,836** non-toxic conversations from **reasoning models** `o1-preview` and `o1-mini`.

This version includes only **non-toxic conversations** as flagged by the OpenAI Moderations API or Detoxify. For most use cases that do not require toxic data, this dataset is recommended. If you need access to a version that contains both toxic and non-toxic conversations, please refer to the gated [WildChat-4.8M-Full](https://huggingface.co/datasets/allenai/WildChat-4.8M-Full).

### Updates

**2025-08-11: Content Update**  
- Extended coverage to data up to (but excluding) August 1, 2025.  
- Released the [data processing script](https://github.com/da03/wildchat) used to construct this dataset.  
- Added TruffleHog scanning to remove verified secrets from the conversations.  
- Highlight: **111,836 reasoning model conversations** from `o1-preview` and `o1-mini`.

### Full Version with Toxic Content

For access to the full version of the WildChat dataset which includes toxic conversations, please refer to [WildChat-4.8M-Full](https://huggingface.co/datasets/allenai/WildChat-4.8M-Full). That version is gated and requires manual approval with a detailed justification for why toxic data is needed.

### Statistics

| Model Family   | Count     |
|----------------|-----------|
| gpt-4o         | 1,539,780 |
| gpt-3.5-turbo  |   688,900 |
| gpt-4.1-mini   |   634,037 |
| gpt-4          |   202,915 |
| o1-mini        |    58,529 |
| o1-preview     |    53,307 |
| gpt-4-turbo    |    22,392 |
| **Total**      | 3,199,860 |

### Data Fields

- `conversation_hash` (string): The hash of each conversation's content. This is not a unique key, as different conversations with the same content will share the same hash. For unique identifiers, use `turn_identifier` within each turn.
- `model` (string): The underlying OpenAI model, such as gpt-3.5-turbo or gpt-4.
- `timestamp` (timestamp): The timestamp of the last turn in the conversation in UTC.
- `conversation` (list): A list of user/assistant utterances. Each utterance is a dictionary containing the `role` of the speaker (user or assistant), the `content` of the utterance, the detected `language` of the utterance, whether the content of the utterance is considered `toxic`, and whether PII has been detected and anonymized (`redacted`). For user turns, there's also the hashed IP address `hashed_ip` of the turn, the state `state` and country `country` inferred from the original IP address, and the request headers `header` (which might be useful for linking multiple conversations from the same user when used in conjunction with `hashed_ip`). For assistant turns, there's a field `timestamp` which is the time when the backend server receives the full response from ChatGPT. For both user and assistant turns, there's a unique identifier `turn_identifier`.
- `turn` (int): The number of turns in the conversation. A turn refers to one round of user-assistant interaction.
- `language` (string): The language of the conversation. Note that this is the most frequently detected language in the utterances of the conversation.
- `openai_moderation` (list): A list of OpenAI Moderation results. Each element in the list corresponds to one utterance in the conversation. When the content of an utterance is an empty string, the corresponding moderation reult is set to be an empty dictionary.
- `detoxify_moderation` (list): A list of Detoxify results. Each element in the list corresponds to one utterance in the conversation. When the content of an utterance is an empty string, the corresponding Detoxify reult is set to be an empty dictionary.
- `toxic` (bool): Whether this conversation contains any utterances considered to be toxic by either OpenAI Moderation or Detoxify.
- `redacted` (bool): Whether this conversation contains any utterances in which PII or API secrets are detected and anonymized.
- `state` (string): The state inferred from the most common IP address in the conversation. Its value is sometimes `None` when GeoIP2 does not identify the state of an IP address.
- `country` (string): The country inferred from the most common IP address in the conversation. Its value is sometimes `None` when GeoIP2 does not identify the country of an IP address.
- `hashed_ip` (string): The most common hashed IP address in the conversation.
- `header` (string): The request header containing information about operating system, browser versions, and accepted languages. This field might be useful for linking multiple conversations from the same user when used in conjunction with `hashed_ip`. Note that every turn in a conversation has the same header, as this is the way we linked turns into conversations.

### Languages

Covers dozens of languages (68 detected in earlier releases).

### Personal and Sensitive Information

The dataset has been de-identified with Microsoft Presidio, custom regex rules, and manual adjustments. Verified secrets were removed using TruffleHog scanning.

### Reserved Data for Evaluation

A small subset of conversations from WildChat was reserved for building [WildBench](https://arxiv.org/abs/2406.04770), a benchmark for evaluating large language models on real-world user queries.

### Empty User Inputs

This dataset includes a small subset of conversations where users submitted empty inputs, sometimes leading to hallucinated responses from the assistant. This behavior, first noticed by @yuchenlin, arises from the design of our Hugging Face chatbot used for data collection, which did not restrict the submission of empty inputs. As a result, users could submit without entering any text, causing the assistant to generate responses without any user prompts. This observation motivated our work [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://arxiv.org/abs/2406.08464), which uses empty or template-only prompts to elicit self-generated queries from aligned LLMs for large-scale instruction data synthesis.

### Data Removal Requests

If you believe your own data is included in WildChat and you would like it removed, or if you encounter content that is illegal, you may request deletion.

To do so, please contact me using the information on my homepage: [https://yuntiandeng.com](https://yuntiandeng.com). Please include:
- **Conversation hash(es)** and/or **turn identifier(s)** corresponding to the entries you wish to remove.
- A brief explanation of the reason for removal.
- Any additional information that could help verify authorship or confirm the issue.

### Citation Information

Please consider citing the following papers if you find this dataset useful:

```
@inproceedings{
  zhao2024wildchat,
  title={WildChat: 1M Chat{GPT} Interaction Logs in the Wild},
  author={Wenting Zhao and Xiang Ren and Jack Hessel and Claire Cardie and Yejin Choi and Yuntian Deng},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024},
  url={https://openreview.net/forum?id=Bl8u7ZRlbM}
}
```

```
@inproceedings{deng2024wildvis,
  title     = "{W}ild{V}is: Open Source Visualizer for Million-Scale Chat Logs in the Wild",
  author    = "Deng, Yuntian and Zhao, Wenting and Hessel, Jack and Ren, Xiang and Cardie, Claire and Choi, Yejin",
  booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
  year      = "2024",
  url       = "https://aclanthology.org/2024.emnlp-demo.50/"
}
```