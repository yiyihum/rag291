---
language:
- en
pretty_name: Topical-Chat ShareGPT
size_categories:
- 10K<n<100K
task_categories:
- text-generation
- text2text-generation
tags:
- conversation
- dialogue
- chat
- trivia
---

# Topical-Chat ShareGPT

This dataset is a modified version of the [Conversational-Reasoning/Topical-Chat](https://huggingface.co/datasets/Conversational-Reasoning/Topical-Chat) dataset, formatted in a ShareGPT-like structure for chatbot training. It comprises conversations between two individuals discussing news or Wikipedia articles, adapted for AI and user interaction. Please refer to the original dataset for comprehensive study details.

## Dataset Description

### Modifications

Key changes from the original dataset include:

*   **AI and User Interaction:** The conversations are restructured to simulate interactions between an AI and a user, instead of human agent_1 and agent_2.
*   **System Prompt:** A randomly selected system prompt is added at the beginning of each conversation, instructing the AI on how to converse with the user.
*   **Emotions in Messages:** The emotions annotated in the original dataset are now incorporated directly into the message content for role-playing purposes.

### Dataset Statistics

The dataset consists of the following number of entries:

*   **Train:** 8&thinsp;628
*   **Validation:** 1&thinsp;078
*   **Test:** 1&thinsp;078
*   **Total:** 10&thinsp;784

### Data Format

Each entry in the dataset is a JSON object with the following structure:

```json
{
  "conversations": [
    {
      "from": "system",
      "value": "You're chatting about fun facts and current affairs with the user. Feel free to add your perspective in any way you'd like."
    },
    {
      "from": "human",
      "value": "hi how are you? do you like rap music?"
    },
    {
      "from": "gpt",
      "value": "I like some stuff.  Mainly some of the older stuff.  I do enjoy Jay-Z"
    },
    {
      "from": "human",
      "value": "*hands at sides* I dont really know his stuff. he is quite popular ive heard."
    },
    {
      "from": "gpt",
      "value": "I know he is in the Songwriter's Hall of Fame, I am not too familiar with his entire body of work, but what I have heard, I like."
    },
    {
      "from": "human",
      "value": "I guess he has rivals in the rap world? Is kanye one of them?"
    },
    {
      "from": "gpt",
      "value": "I think so, but I also think they worked on an album together.  I dont personally care for Kanye."
    },
    ...
    {
      "from": "gpt",
      "value": "*hands at sides* Same to you!  Have a great day!"
    },
    {
      "from": "human",
      "value": "Thanks, you too! Bye"
    },
    {
      "from": "gpt",
      "value": "Bye!"
    }
  ],
  "file": "valid_rare.jsonl"
}
```

*   `conversations`: A list of dictionaries, where each dictionary represents a turn in the conversation.
    *   `from`: Indicates the speaker ("system", "human", or "gpt").
    *   `value`: The content of the message.
*   `file`: The name of the original JSONL file from which the conversation was extracted.

### Intended Use

This dataset is intended for training and evaluating chatbot models, particularly those designed for engaging in topical and knowledge-grounded conversations.

### Limitations

The dataset has the following limitations:

*   **Outdated/Inaccurate Trivia:** Some of the trivia or factual information may be outdated or inaccurate.
*   **Non-Literal Interpretation:** The conversations may contain hyperbole or other figures of speech that should not be taken literally.
*   **Non-Sequiturs:** Sudden topic changes may occur, resulting in non-sequiturs.
*   **Incomplete Conversations:** Some conversations may be incomplete to maintain an even number of turns.

## Citation

If you use this dataset in your work, please cite the original Topical-Chat dataset:

```
@inproceedings{gopalakrishnan2019topical,
  author={Karthik Gopalakrishnan and Behnam Hedayatnia and Qinlang Chen and Anna Gottardi and Sanjeev Kwatra and Anu Venkatesh and Raefer Gabriel and Dilek Hakkani-Tür},
  title={{Topical-Chat: Towards Knowledge-Grounded Open-Domain Conversations}},
  year=2019,
  booktitle={Proc. Interspeech 2019},
  pages={1891--1895},
  doi={10.21437/Interspeech.2019-3079},
  url={http://dx.doi.org/10.21437/Interspeech.2019-3079}
}
```

```
Gopalakrishnan, Karthik, et al. "Topical-Chat: Towards Knowledge-Grounded Open-Domain Conversations.", Proc. INTERSPEECH 2019
```