---
license: cc-by-nc-sa-4.0
language:
- en
tags:
- chat
- conversational-ai
- dialogue
- emotions
task_categories:
- text2text-generation
- text-generation
---

# DailyDialog in ShareGPT-like Format

## Dataset Summary

This dataset is a reformatted version of the [DailyDialog](https://huggingface.co/datasets/li2017dailydialog/daily_dialog) dataset, structured to resemble ShareGPT conversations. 
Each row represents a single conversation, with added features and adjustments to better support conversational AI training.

The dataset includes:
- A random system prompt to initiate natural interactions.
- Emotion annotations for user or AI messages.
- Corrected message spacing using [agentlans/flan-t5-small-detokenizer](https://huggingface.co/agentlans/flan-t5-small-detokenizer).
- Conversations truncated so that the AI reply is always last.

The dataset retains the original split sizes:
- **Train**: 11,118 conversations
- **Validation**: 1,000 conversations
- **Test**: 1,000 conversations

## Dataset Format

Each row in the dataset contains a conversation represented as a list of message objects. Each message object includes:
- `from`: The sender of the message (`system`, `human`, or `gpt`).
- `value`: The content of the message.

### Example Row

```json
{
  "conversations": [
    {
      "from": "system",
      "value": "This is a discussion on normal, everyday things. Take on the role of the person the user is speaking with, and feel free to invent details to keep it real. Just keep it casual."
    },
    {
      "from": "human",
      "value": "Have you heard Jenny divorced her French husband?"
    },
    {
      "from": "gpt",
      "value": "*Body freezes, head jerks back* Oh, really? No wonder that she looks quite depressed recently."
    },
    {
      "from": "human",
      "value": "Yes. They used to be joined at the hip."
    },
    {
      "from": "gpt",
      "value": "I heard they were just married for half a year."
    },
    {
      "from": "human",
      "value": "That’s true. She said they often argued over nickel-and-dime things."
    },
    {
      "from": "gpt",
      "value": "Yeah. Mixed marriage is tempting but full of culture shock."
    },
    {
      "from": "human",
      "value": "You said it. You know, they fell in love at the first sight and quickly jumped into marriage."
    },
    {
      "from": "gpt",
      "value": "Maybe they were just attracted to each other but too different to be married."
    }
  ]
}
```

## Limitations

While this dataset offers enhanced formatting and additional features, it has several limitations:
1. **Original Errors**: The source dataset contains spelling, grammar, and formatting errors.
2. **Emotion Granularity**: Emotion annotations do not distinguish between intensity levels.
3. **Awkward Reactions**: Some body language reactions may feel unnatural in context.
4. **System Prompt Specificity**: The system prompt is generic, requiring models trained on this data to generate plausible scenarios independently.

## Intended Uses

This dataset is designed for training and fine-tuning conversational AI models capable of multi-turn dialogue with emotional context. It can be used for tasks such as:
- Dialogue modeling
- Conversational emotion recognition
- Chatbot development

## Citation

If you use this dataset, please cite the original [DailyDialog paper](https://arxiv.org/abs/1709.09087):

```
@InProceedings{li2017dailydialog,
    author = {Li, Yanran and Su, Hui and Shen, Xiaoyu and Li, Wenjie and Cao, Ziqiang and Niu, Shuzi},
    title = {DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset},
    booktitle = {Proceedings of The 8th International Joint Conference on Natural Language Processing (IJCNLP 2017)},
    year = {2017}
}
```