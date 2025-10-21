---
license: cc-by-4.0
language:
- en
- fr
- it
- de
- es
pretty_name: Multilingual Synthetic Online Conversations
tags:
- synthetic
- conversational
- dialogue
- role-playing
- chat
- multi-turn
- multilingual
- translation
dataset_info:
  features:
  - name: chat_id
    dtype: string
  - name: experience
    struct:
    - name: id
      dtype: string
    - name: persona1
      struct:
      - name: age
        dtype: int64
      - name: background
        struct:
        - name: de
          dtype: string
        - name: en
          dtype: string
        - name: es
          dtype: string
        - name: fr
          dtype: string
        - name: it
          dtype: string
      - name: chatting_style
        struct:
        - name: de
          dtype: string
        - name: en
          dtype: string
        - name: es
          dtype: string
        - name: fr
          dtype: string
        - name: it
          dtype: string
      - name: id
        dtype: string
      - name: model
        dtype: string
      - name: name
        dtype: string
      - name: traits
        struct:
        - name: de
          list: string
        - name: en
          list: string
        - name: es
          list: string
        - name: fr
          list: string
        - name: it
          list: string
      - name: username
        dtype: string
    - name: persona2
      struct:
      - name: age
        dtype: int64
      - name: background
        struct:
        - name: de
          dtype: string
        - name: en
          dtype: string
        - name: es
          dtype: string
        - name: fr
          dtype: string
        - name: it
          dtype: string
      - name: chatting_style
        struct:
        - name: de
          dtype: string
        - name: en
          dtype: string
        - name: es
          dtype: string
        - name: fr
          dtype: string
        - name: it
          dtype: string
      - name: id
        dtype: string
      - name: model
        dtype: string
      - name: name
        dtype: string
      - name: traits
        struct:
        - name: de
          list: string
        - name: en
          list: string
        - name: es
          list: string
        - name: fr
          list: string
        - name: it
          list: string
      - name: username
        dtype: string
    - name: relationship
      struct:
      - name: de
        dtype: string
      - name: en
        dtype: string
      - name: es
        dtype: string
      - name: fr
        dtype: string
      - name: it
        dtype: string
    - name: situation
      struct:
      - name: de
        dtype: string
      - name: en
        dtype: string
      - name: es
        dtype: string
      - name: fr
        dtype: string
      - name: it
        dtype: string
    - name: topic
      struct:
      - name: de
        dtype: string
      - name: en
        dtype: string
      - name: es
        dtype: string
      - name: fr
        dtype: string
      - name: it
        dtype: string
  - name: chat_parts
    list:
    - name: messages
      list:
      - name: de
        dtype: string
      - name: en
        dtype: string
      - name: es
        dtype: string
      - name: fr
        dtype: string
      - name: it
        dtype: string
      - name: tag
        dtype: string
    - name: sender
      dtype: string
  - name: model
    dtype: string
  splits:
  - name: train
    num_bytes: 36638233
    num_examples: 1181
  download_size: 22229453
  dataset_size: 36638233
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Dataset Card for Multilingual Synthetic Online Conversations

![Generation Pipeline](SPB_SOC_Pipeline.png)

## Dataset Summary

This dataset contains multilingual translations of the [Synthetic Online Conversations (SOC-2508)](https://huggingface.co/datasets/marcodsn/SOC-2508) dataset. Each conversation from the original dataset has been translated into French, Italian, German, Spanish, providing over 1,180 synthetically generated, multi-turn online conversations in multiple languages.

The translations were generated using [google/gemma-3n-E4B-it](https://huggingface.co/google/gemma-3n-E4B-it) with **vLLM** as the inference backend through HuggingFace Jobs (check [this wonderful blog post](https://danielvanstrien.xyz/posts/2025/hf-jobs/vllm-batch-inference.html)). The translation script is available [on Github](https://github.com/marcodsn/SOC/blob/2508/scripts/translation/translate.uv.py).

Each conversation preserves the complete dialogue between two fictional personas, including their detailed backgrounds, relationship dynamics, and conversation context, but now available in more languages. Special multimedia tags (e.g., `<image>`, `<audio>`) are preserved to maintain the authentic online conversation experience.

> [!Important]
> For details about the original generation process, data fields, and design goals, see the seed dataset page: [Synthetic Online Conversations (SOC-2508)](https://huggingface.co/datasets/marcodsn/SOC-2508).

## Dataset Structure

The dataset consists of a single split where each item is a JSON object representing a complete conversation with multilingual content.

### Data Instances

Each line in the dataset is a JSON object representing a single chat with multilingual fields. Here is an example of what a chat object looks like:

```json
{
  "chat_id": "4436437d368e4325a7c1c6f7092c2d9e_f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5_1754636647",
  "experience": {
    "persona1": {
      "name": "Elias Vance",
      "username": "quantum_scribe",
      "age": 42,
      "traits": {
        "en": ["analytical", "introspective", "witty", "reserved"],
        "fr": ["analytique", "introspectif", "spirituel", "réservé"]
      },
      "background": {
        "en": "A theoretical physicist who, after a breakthrough, left academia to write science fiction novels from a secluded cabin. He's currently grappling with a severe case of writer's block for his second book.",
        "fr": "Un physicien théoricien qui, après une percée, a quitté le monde académique pour écrire des romans de science-fiction depuis une cabane isolée. Il lutte actuellement contre un grave blocage d'écrivain pour son deuxième livre."
      },
      "chatting_style": {
        "en": "Uses precise language and often employs metaphors from physics. Tends to write in well-structured, complete sentences, even in casual chat.",
        "fr": "Utilise un langage précis et emploie souvent des métaphores de la physique. A tendance à écrire en phrases bien structurées et complètes, même dans une discussion décontractée."
      },
      "model": "Qwen3-235B-A22B-Instruct-2507",
      "id": "4436437d368e4325a7c1c6f7092c2d9e"
    },
    "persona2": {
      "name": "Luna Reyes",
      "username": "StardustSketcher",
      "age": 28,
      "traits": {
        "en": ["creative", "optimistic", "daydreamer", "empathetic"],
        "fr": ["créative", "optimiste", "rêveuse", "empathique"]
      },
      "background": {
        "en": "A freelance digital artist who illustrates children's books and streams her drawing process online. She finds inspiration in mythology and the night sky.",
        "fr": "Une artiste numérique freelance qui illustre des livres pour enfants et diffuse son processus de dessin en ligne. Elle trouve son inspiration dans la mythologie et le ciel nocturne."
      },
      "chatting_style": {
        "en": "Uses a lot of emojis and kaomoji (´｡-  ᵕ - ｡`). Her messages are often short, enthusiastic, and full of creative typos.",
        "fr": "Utilise beaucoup d'emojis et de kaomoji (´｡-  ᵕ - ｡`). Ses messages sont souvent courts, enthousiastes et pleins de fautes de frappe créatives."
      },
      "model": "Qwen3-235B-A22B-Instruct-2507",
      "id": "f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5"
    },
    "relationship": {
      "en": "Strangers who met in a 'Vintage Sci-Fi Book Club' Discord server.",
      "fr": "Des inconnus qui se sont rencontrés dans un serveur Discord 'Club de Livres de Science-Fiction Vintage'."
    },
    "situation": {
      "en": "Elias posted a message asking for recommendations to overcome writer's block, and Luna, a fellow member, decided to DM him directly to offer some creative, non-traditional advice.",
      "fr": "Elias a posté un message demandant des recommandations pour surmonter le blocage de l'écrivain, et Luna, un membre du groupe, a décidé de lui envoyer un message privé pour offrir des conseils créatifs et non conventionnels."
    },
    "topic": {
      "en": "I saw your post in the #writing- woes channel and had a few weird ideas that might help! Mind if I share?",
      "fr": "J'ai vu ton post dans le canal #writing-woes et j'ai eu quelques idées bizarres qui pourraient t'aider ! Ça te dérange si je les partage ?"
    },
    "id": "c1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6"
  },
  "chat_parts": [
    {
      "sender": "f8e1b2a3c4d5e6f7g8h9i0j1k2l3m4n5",
      "messages": {
        "en": [
          "Hiii Elias! Saw your post in #writing-woes. I know the feeling (art block is the wooooorst 😭).",
          "Had a few maybe-weird ideas if you're open to them? ✨"
        ],
        "fr": [
          "Salut Elias ! J'ai vu ton post dans #writing-woes. Je connais ce sentiment (le blocage artistique c'est le piiiiire 😭).",
          "J'ai eu quelques idées peut-être bizarres si tu es ouvert à ça ? ✨"
        ]
      }
    },
    {
      "sender": "4436437d368e4325a7c1c6f7092c2d9e",
      "messages": {
        "en": [
          "Hello, Luna. I appreciate the outreach. At this point, I am receptive to any and all suggestions, regardless of their position on the conventionality spectrum."
        ],
        "fr": [
          "Bonjour, Luna. J'apprécie ta démarche. À ce stade, je suis réceptif à toutes les suggestions, peu importe leur position sur le spectre de la conventionnalité."
        ]
      }
    }
  ],
  "model": "Qwen3-235B-A22B-Instruct-2507"
}
```

### Data Fields

Each JSON object contains the same structure as the original SOC-2508 dataset, but with multilingual content:

- **chat_id** (string): A unique identifier for the conversation.
- **experience** (object): An object containing the full multilingual context for the conversation.
    - **persona1** & **persona2** (object): The complete persona objects with multilingual fields:
        - **traits** (object): Character traits in multiple languages
        - **background** (object): Character background in multiple languages  
        - **chatting_style** (object): Communication style descriptions in multiple languages
    - **relationship** (object): Relationship description in multiple languages
    - **situation** (object): Scenario description in multiple languages
    - **topic** (object): Opening line in multiple languages
    - **id** (string): A unique identifier for the experience object itself.
- **chat_parts** (list[object]): A list of conversation turns with multilingual messages.
    - **sender** (string): The ID of the persona who sent the messages in this turn.
    - **messages** (object): Messages organized by language code, preserving special XML-like tags.
- **model** (string): The original model used to generate the English conversation.

### Language Codes

This dataset uses ISO 639-1 language codes:
- **en**: English (original)
- **fr**: Français (French)
- **it**: Italiano (Italian)
- **de**: Deutsch (German)
- **es**: Español (Spanish)

### Data Splits

The dataset is provided as a single `train` split. Users are encouraged to create their own validation and test splits as needed for their specific use cases.

## Dataset Creation

### Curation Rationale

This multilingual version was created to extend the reach and utility of the original SOC-2508 dataset across different language communities. By providing high-quality translations that preserve the nuanced persona-based dialogue structure, this dataset enables research and development of multilingual conversational AI systems that can maintain persona consistency and natural dialogue flow across languages.

### Source Data

This dataset is built upon the synthetically generated [SOC-2508](https://huggingface.co/datasets/marcodsn/SOC-2508) dataset. The original English conversations were translated using automated translation methods while preserving the structure and special formatting elements.

### Translation Process

The translations were generated using the following pipeline:

1. **Model Selection**: **google/gemma-3n-E4B-it** was selected as the translation model for its strong multilingual capabilities / efficency ratio.

2. **Infrastructure**: **vLLM** served as the inference backend, deployed through Hugging Face Jobs for efficient (and super fast!) batch processing.

3. **Field-by-Field Translation**: Each multilingual field (persona traits, backgrounds, chat messages, etc.) was translated individually to prevent formatting errors with the small translation model.

4. **Special Tag Preservation**: XML-like tags (`<audio><audio/>`, `<image><image/>`, `<delay/>`, etc.) were preserved in their original form to maintain the multimedia conversation experience across languages.

5. **Quality Assurance**: Post-processing steps ensured structural integrity and consistent formatting across all language versions.

## Usage

```
from datasets import load_dataset

dataset = load_dataset("marcodsn/SOC-2508-MULTI")

# Access English version
english_background = dataset["experience"]["persona1"]["background"]["en"]

# Access Italian version
italian_background = dataset["experience"]["persona1"]["background"]["it"]

# Access multilingual messages
english_messages = dataset["chat_parts"]["messages"]["en"]
italian_messages = dataset["chat_parts"]["messages"]["it"]
```

## Known Limitations

- **Translation Quality**: While generated using a capable model, automated translations may not capture all linguistic nuances, cultural references, or idiomatic expressions perfectly. Furthermore, in this revision the model did not have full conversation context, so some translated messages may sound off.
- **Inherited Limitations**: All limitations from the original SOC-2508 dataset apply, including synthetic nature and potential biases.
- **Cultural Adaptation**: Translations are linguistic rather than cultural adaptations, so some references may not translate meaningfully across cultural contexts.

## Additional Information

### Original Dataset

This multilingual version is based on the [SOC-2508](https://huggingface.co/datasets/marcodsn/SOC-2508) dataset. Please refer to the original dataset card for detailed information about the generation methodology and underlying persona bank.

### Licensing Information

This dataset is licensed under the CC BY 4.0 License, maintaining consistency with the original dataset.

### Citation Information

If you use this dataset in your research, please consider citing it as follows:

```bibtex
@misc{marcodsn_2025_SOC2508_MULTI,
  title     = {Multilingual Synthetic Online Conversations},
  author    = {Marco De Santis},
  year      = {2025},
  month     = {August},
  url       = {https://huggingface.co/datasets/marcodsn/SOC-2508-MULTI},
}
```