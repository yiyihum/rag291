---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: model_a
    dtype: string
  - name: model_b
    dtype: string
  - name: winner
    dtype: string
  - name: judge
    dtype: string
  - name: conversation_a
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: speaker
      dtype: string
  - name: conversation_b
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
    - name: speaker
      dtype: string
  - name: turn
    dtype: int64
  - name: annoy
    dtype: bool
  - name: language
    dtype: string
  - name: tstamp
    dtype: float64
  - name: openai_moderation
    struct:
    - name: categories
      struct:
      - name: harassment
        dtype: bool
      - name: harassment/threatening
        dtype: bool
      - name: hate
        dtype: bool
      - name: hate/threatening
        dtype: bool
      - name: illicit
        dtype: bool
      - name: illicit/violent
        dtype: bool
      - name: self-harm
        dtype: bool
      - name: self-harm/instructions
        dtype: bool
      - name: self-harm/intent
        dtype: bool
      - name: sexual
        dtype: bool
      - name: sexual/minors
        dtype: bool
      - name: violence
        dtype: bool
      - name: violence/graphic
        dtype: bool
    - name: category_applied_input_types
      struct:
      - name: harassment
        list: string
      - name: harassment/threatening
        list: string
      - name: hate
        list: string
      - name: hate/threatening
        list: string
      - name: illicit
        list: string
      - name: illicit/violent
        list: string
      - name: self-harm
        list: string
      - name: self-harm/instructions
        list: string
      - name: self-harm/intent
        list: string
      - name: sexual
        list: string
      - name: sexual/minors
        list: string
      - name: violence
        list: string
      - name: violence/graphic
        list: string
    - name: category_scores
      struct:
      - name: harassment
        dtype: float64
      - name: harassment/threatening
        dtype: float64
      - name: hate
        dtype: float64
      - name: hate/threatening
        dtype: float64
      - name: illicit
        dtype: float64
      - name: illicit/violent
        dtype: float64
      - name: self-harm
        dtype: float64
      - name: self-harm/instructions
        dtype: float64
      - name: self-harm/intent
        dtype: float64
      - name: sexual
        dtype: float64
      - name: sexual/minors
        dtype: float64
      - name: violence
        dtype: float64
      - name: violence/graphic
        dtype: float64
  - name: flagged
    dtype: bool
license: cc
task_categories:
- question-answering
- text-generation
size_categories:
- n<1K
language:
- ja
configs:
- config_name: default
  data_files: conversations.jsonl
  default: true
---

## LLM-jp Chatbot Arena Conversations Dataset

This dataset contains approximately 1,000 conversations with pairwise human preferences, most of which are in Japanese.
The data was collected during the trial phase of the LLM-jp Chatbot Arena (January–February 2025), where users compared responses from two different models in a head-to-head format.
Each sample includes a question ID, the names of the two models, their conversation transcripts, the user's vote, an anonymized user ID, a detected language tag, OpenAI moderation API output, and a timestamp.

To ensure a safe public release, we made our best effort to remove all conversations containing personally identifiable information (PII).
User consent was obtained via the "Terms of Use" on the data collection site.
We also provide the output of the OpenAI moderation API to help identify potentially inappropriate content.
However, we have retained conversations flagged as unsafe to support research on safety concerns in real-world LLM use and the effectiveness of moderation systems.

## Basic Statistics

| Metric       |     |
|:-------------|:----|
| # of Samples | 990 |
| # of Models  | 10  |
| # of Judges  | 200 |

## Disclaimers

- **This dataset includes conversations that may contain sensitive, offensive, or potentially upsetting content.** It is provided to support research on language model behavior, safety, and robustness. When using this dataset for training or evaluation, we strongly encourage the application of appropriate safety measures and content filtering.
- Statements and opinions expressed in the dataset do not represent the views of the researchers or affiliated institutions involved in its creation.

## License

User prompts are licensed under CC BY 4.0, while model outputs are subject to their respective licenses.

## Citation

```
@misc{llm-jp-chatbot-arena-conversations-dataset,
  author = {LLM-jp},
  title = {LLM-jp Chatbot Arena Conversations Dataset},
  year = {2025},
  url = {https://huggingface.co/datasets/llm-jp/llm-jp-chatbot-arena-conversations},
}
```
