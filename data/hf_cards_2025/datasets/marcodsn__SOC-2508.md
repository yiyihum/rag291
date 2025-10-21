---
license: cc-by-4.0
language:
- en
pretty_name: Synthetic Online Conversations
tags:
- synthetic
- conversational
- dialogue
- role-playing
- chat
- multi-turn
---

# Dataset Card for Synthetic Online Conversations

![Generation Pipeline](SPB_SOC_Pipeline.png)

## Dataset Summary

This dataset contains over 1,180 synthetically generated, multi-turn online conversations. Each conversation is a complete dialogue between two fictional personas drawn from the [Synthetic Persona Bank (SPB-2508)](https://huggingface.co/datasets/marcodsn/SPB-2508) dataset.

The dataset was created using a multi-stage programmatic pipeline (inspired by [ConvoGen](https://huggingface.co/papers/2503.17460)) driven by a large language model ([Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)). The generation process was guided by detailed instructions to produce natural, context-aware, and stylistically consistent dialogues with human-like imperfections, realistic conflict, and simulated multimedia elements.

Unlike typical synthetic chats, these conversations explicitly model real-time online behavior: participants may send multiple consecutive messages per turn, include human-like delays between replies, and “attach” simulated multimedia using lightweight XML-like tags (e.g., `<image>`, `<gif>`, `<audio>`, `<video>`, `<delay>`, `<end/>`). This makes the conversations feel more like actual messaging app threads rather than single-turn exchanges with a chatbot.

You can visualize the generated conversations using the [SOC Visualizer](https://huggingface.co/spaces/marcodsn/SOC_Visualizer) HF Space.

## Dataset Structure

The dataset consists of a single JSONL file where each line is a JSON object representing a complete conversation.

### Data Instances

Each line in the dataset is a JSON object representing a single chat. Here is an example of what a chat object looks like:

```json
{
  "chat_id": "4436437d368e4325a7c1c6f7092c2d9e_f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5_1754636647",
  "experience": {
    "persona1": {
      "name": "Elias Vance",
      "username": "quantum_scribe",
      "age": 42,
      "traits": ["analytical", "introspective", "witty", "reserved"],
      "background": "A theoretical physicist who, after a breakthrough, left academia to write science fiction novels from a secluded cabin. He's currently grappling with a severe case of writer's block for his second book.",
      "chatting_style": "Uses precise language and often employs metaphors from physics. Tends to write in well-structured, complete sentences, even in casual chat.",
      "model": "Qwen3-235B-A22B-Instruct-2507",
      "id": "4436437d368e4325a7c1c6f7092c2d9e"
    },
    "persona2": {
      "name": "Luna Reyes",
      "username": "StardustSketcher",
      "age": 28,
      "traits": ["creative", "optimistic", "daydreamer", "empathetic"],
      "background": "A freelance digital artist who illustrates children's books and streams her drawing process online. She finds inspiration in mythology and the night sky.",
      "chatting_style": "Uses a lot of emojis and kaomoji (´｡• ᵕ •｡`). Her messages are often short, enthusiastic, and full of creative typos.",
      "model": "Qwen3-235B-A22B-Instruct-2507",
      "id": "f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5"
    },
    "relationship": "Strangers who met in a 'Vintage Sci-Fi Book Club' Discord server.",
    "situation": "Elias posted a message asking for recommendations to overcome writer's block, and Luna, a fellow member, decided to DM him directly to offer some creative, non-traditional advice.",
    "topic": "I saw your post in the #writing- woes channel and had a few weird ideas that might help! Mind if I share?",
    "id": "c1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6"
  },
  "chat_parts": [
    {
      "sender": "f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5",
      "messages": [
        "Hiii Elias! Saw your post in #writing-woes. I know the feeling (art block is the wooooorst 😭).",
        "Had a few maybe-weird ideas if you're open to them? ✨"
      ]
    },
    {
      "sender": "4436437d368e4325a7c1c6f7092c2d9e",
      "messages": [
        "<delay minutes=\"5\"/>",
        "Hello, Luna. I appreciate the outreach. At this point, I am receptive to any and all suggestions, regardless of their position on the conventionality spectrum."
      ]
    },
    {
      "sender": "f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5",
      "messages": [
        "Awesome! Okay, so forget writing. Just for a day. Go outside tonight and just... look at the stars. No pressure, just observe.",
        "Like you're cataloging them for a galactic library. What do they make you *feel*?",
        "<gif>animated gif of twinkling stars from a 90s anime</gif>"
      ]
    },
    {
      "sender": "4436437d368e4325a7c1c6f7092c2d9e",
      "messages": [
        "An interesting proposition. A purely observational, non-analytical exercise. It has a certain... elegance. I will attempt it.",
        "Thank you. <end/>"
      ]
    }
  ],
  "model": "Qwen3-235B-A22B-Instruct-2507"
}
```

### Data Fields

Each JSON object contains the following fields:

- **chat_id** (string): A unique identifier for the conversation.
- **experience** (object): An object containing the full context for the conversation.
    - **persona1** & **persona2** (object): The complete persona objects from the SPB-2508 dataset for the two participants.
    - **relationship** (string): A brief description of how the two personas know each other.
    - **situation** (string): The specific online context or reason for the conversation starting.
    - **topic** (string): The opening line or subject that kicks off the dialogue.
    - **id** (string): A unique identifier for the experience object itself.
- **chat_parts** (list[object]): A list of objects, where each object represents one turn in the conversation.
    - **sender** (string): The ID of the persona who sent the messages in this turn.
    - **messages** (list[string]): A list of one or more messages sent by the persona in this turn. Can include special XML-like tags.
- **model** (string): The model used to generate the conversation.

### Data Splits

The dataset is provided as a single file, which constitutes the `train` split. Users are encouraged to create their own validation and test splits as needed for their specific use cases.

## Dataset Creation

### Curation Rationale

This dataset was created to address the need for large-scale, high-quality conversational data that goes beyond simple question-answering. The goal was to generate dialogues that exhibit deep persona consistency, natural topic progression, and the messy, imperfect nature of real online chats. By building directly on the structured `SPB-2508` persona bank, we ensure each conversation is grounded in a rich, pre-defined context.

### Source Data

This is a synthetically generated dataset. Its primary source is the `marcodsn/SPB-2508` dataset, which provides the character personas. The conversational scenarios and dialogue were generated through a programmatic, multi-stage pipeline.

### Generation Process

The conversations were generated using a three-stage pipeline:

1.  **Stage 1: Experience Generation**:
    - Two personas were selected from the `SPB-2508` pool, with a weighting system to favor pairing personas of similar age, promoting more plausible interactions.
    - A relationship context (e.g., "old friends from college," "strangers in a gaming lobby") was dynamically constructed from seed components.
    - These elements were fed to the LLM, which generated a unique `situation` (the reason for the chat) and a starting `topic` (the opening line). Few-shot examples were used to encourage novelty.

2.  **Stage 2: Conversational Rollout**:
    - Each generated "experience" served as a prompt for a new conversation.
    - The LLM generated the dialogue turn-by-turn, alternating between the two personas.
    - The prompt for each turn included the full persona details, the initial scenario, and the entire chat history up to that point.
    - The LLM was given a rich set of instructions to encourage realism, including:
        - **Human Imperfection**: Allowing for typos, topic drift, and variable effort in replies.
        - **Realistic Conflict**: Guiding the model to handle disagreements without immediate, clean resolutions.
        - **Special Tags**: Using XML-like tags to simulate online features: `<image>`, `<gif>`, `<audio>`, `<video>` for multimedia; `<delay>` to simulate response times; and `<end/>` to signal a natural conclusion to the chat.

3.  **Stage 3: Post-Processing and Cleaning**:
    - The raw generated chats were collected and merged.
    - A cleaning script removed duplicates, filtered out conversations that were too short (fewer than two turns), and scrubbed artifacts like model-inserted speaker names (e.g., "Elias Vance: Hello").
    - The final, cleaned dataset was shuffled to ensure random distribution.

## Known Limitations

-   **Synthetic Nature**: While designed for realism, the dialogues are synthetic and may not capture the full chaotic unpredictability of genuine human interaction.
-   **Inherited Bias**: Any biases, stereotypes, or patterns present in the source `SPB-2508` dataset will be inherited and potentially amplified in these conversations.
-   **Tag Frequency**: The use of special tags (`<image>`, `<delay>`, etc.) is not uniform across all conversations, as their inclusion was left to the model's discretion during generation.
-   **Conversation Endings**: The `<end/>` tag provides a clear signal but might lead to some conversations concluding more formulaically than they would in the wild.
-   **Instruction Following**: The LLM we used is not perfect and various problems derived from poor instruction following have been found; furthermore, the `<end/>` tag is often used prematurely. We will try to solve these issues in a future release.

## Additional Information

### Code and Seed Data

The generation scripts and seed data can be found on [GitHub](https://github.com/marcodsn/SOC/tree/2508).

### Licensing Information

This dataset is licensed under the CC BY 4.0 License.

The code used to generate the dataset is available under the Apache 2.0 License.

### Citation Information

If you use this dataset in your research, please consider citing it as follows:

```bibtex
@misc{marcodsn_2025_SOC2508,
  title     = {Synthetic Online Conversations},
  author    = {Marco De Santis},
  year      = {2025},
  month     = {August},
  url       = {https://huggingface.co/datasets/marcodsn/SOC-2508},
}
```