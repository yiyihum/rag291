---
license: mit
language:
- en
tags:
- conversational-ai
- text-generation
- mental-health
- empathetic-dialogue
- instruction-tuning
task_categories:
- text-generation
size_categories:
- n<1K
---

# Mind Corpus

## Dataset Description

This dataset contains 124 handcrafted, multi-turn conversations designed to simulate supportive interactions in mental health contexts. The dataset is bifurcated into two distinct settings:

1.  **Clinical Setting (In-Office):** Dialogues between a patient and a psychologist during a therapy session. These conversations explore ongoing personal issues in a structured, reflective environment.
2.  **Crisis Hotline Setting:** Dialogues between a caller in acute distress and a crisis hotline dispatcher. These conversations are immediate, emotionally charged, and focused on de-escalation and providing temporary comfort.

The primary goal of this dataset is to provide high-quality training data for developing empathetic, context-aware AI assistants. The dialogues are intentionally crafted to be deeply personal, creative, and non-cliché, moving beyond textbook examples to reflect the messy, nuanced reality of human struggle. The focus is on modeling active listening, emotional validation, and non-clinical support, rather than providing diagnosis or medical advice.

### Key Features:
- **Dual Settings:** Provides examples of both immediate crisis intervention and longer-term therapeutic conversation.
- **Emotional Depth:** Scenarios cover a range of deeply personal issues like grief, failure, identity loss, caregiver burnout, and existential dread.
- **Realistic Flow:** Conversations are 4-12 turns long, allowing for the development of a coherent narrative and emotional arc.
- **Non-Clinical Focus:** The "responder" (psychologist/dispatcher) minimizes clinical jargon, focusing on empathetic reflection and grounding techniques.

## Supported Tasks

The primary task for this dataset is `text-generation` within a conversational context. The goal is to train a model that, given a conversation history ending with a "human" turn, can generate an appropriate, empathetic "gpt" response.

- **`conversational-ai`**: The dataset is ideal for instruction-tuning or fine-tuning language models for empathetic dialogue systems.
- **`text-generation`**: Models can be trained to generate the next turn in the conversation.


## Languages

The data is in English (`en-US`).

## Dataset Structure

### Data Instances

The dataset is composed of a single JSON file where each row contains one complete conversation. Each conversation is a list of turns.

An example of a single data point:

```json
{
    "conversations": [
      {
        "from": "human",
        "value": "I'm sitting in my car in the driveway. I can't go back in the house. My mom... she has Alzheimer's. A few minutes ago she looked right through me and accused me of stealing from her. She asked me who I was. I've been her only caregiver for five years. My entire life is that house. And she looked at me like I was a monster."
      },
      {
        "from": "gpt",
        "value": "That is a devastating experience. To have your reality, your entire purpose for the last five years, not just forgotten but twisted into something ugly... that's an unimaginable kind of pain. It's a profound loss, happening right there in front of you. I am so sorry you had to hear those words. It's good you're taking a moment for yourself in the car."
      },
      {
        "from": "human",
        "value": "I haven't had a 'moment' in five years. I feed her, I bathe her, I read to her. My friends stopped calling because I always have to cancel. And tonight I realized... she's already gone, and the person I became for her doesn't exist either. I'm just... nothing. A ghost in my own life."
      },
      {
        "from": "gpt",
        "value": "You're grieving two losses at once: the mother you knew, and the self you had to set aside to care for her. When she didn't recognize you, it felt like it invalidated every single sacrifice. You are not nothing. You are a person who has loved someone so completely that you put your entire world on hold. That is something immense, and right now, the weight of that is crushing you."
      }
    ]
}
```

### Data Fields

- `conversations`: A list of dictionaries, where each dictionary represents a single turn in the dialogue.
  - `from`: (string) Indicates the speaker. Has one of two values:
    - `"human"`: Represents the patient or crisis caller seeking help.
    - `"gpt"`: Represents the psychologist or crisis dispatcher providing support.
  - `value`: (string) The text of the utterance from the speaker.

### Data Splits

The dataset consists of a single `train` split containing all 124 conversations. Users are encouraged to create their own `validation` and `test` splits as needed for their specific use case.

## Dataset Creation

### Curation Rationale

This dataset was created to address a gap in publicly available data for training truly empathetic conversational AI. Many existing datasets either lack emotional depth, are overly clinical, or consist of short, decontextualized turns. This dataset was built on the principle that to teach empathy, a model needs to be exposed to rich, personal narratives and high-quality examples of emotional validation and active listening. The goal is to train models capable of providing temporary comfort and a feeling of being "heard" during moments of distress.

### Source Data

**This is a synthetic dataset.** All conversations were generated by a large language model (Google’s Gemini) guided by specific, detailed prompts designed to elicit unique and emotionally resonant scenarios. **No data was collected from real individuals, patients, or crisis callers.** This approach was chosen to ensure privacy, safety, and the ability to craft diverse scenarios without exploiting real human suffering.

### Personal and Sensitive Information

As the data is entirely synthetic, it contains no real personal or sensitive information. Any names, locations, or specific life details are fictional and generated for narrative purposes.

## Considerations for Using the Data

### Social Impact

The intended use of this dataset is to advance research and development in the field of mental health technology, with the goal of creating tools that can offer accessible, first-line emotional support. Such tools could help destigmatize mental health struggles and provide a resource for individuals who are not yet ready or able to seek professional help.

However, the misuse of this dataset or models trained on it presents significant risks. A poorly implemented chatbot could provide harmful, inappropriate, or dangerously simplistic responses to a person in a vulnerable state.

**CRITICAL DISCLAIMER: Models trained on this dataset are not a substitute for professional medical advice, diagnosis, or treatment. They are not therapists, doctors, or crisis workers. Any application built using this data must include clear, prominent disclaimers advising users to seek help from qualified human professionals in a crisis.**

### Discussion of Biases

The dataset was generated by a large language model and reflects the biases inherent in its training data. The scenarios and communication styles are primarily reflective of a Western, English-speaking cultural context. The dataset does not and cannot represent the full spectrum of human experience, cultural norms around mental health, or the myriad ways individuals express distress. Models trained on this data may perform poorly or inappropriately when interacting with users from different cultural or demographic backgrounds.

### Other Known Limitations

- **Small Scale:** With 124 conversations, the dataset is relatively small. Models may overfit to the specific scenarios and conversational styles present.
- **Idealized Responses:** The "gpt" responses are consistently high-quality, articulate, and empathetic. This represents an idealized standard that may not be achievable in all real-world applications and does not reflect the variability of human support.
- **Lack of Messiness:** Real human conversations are often less linear and coherent than the dialogues presented here. This dataset simplifies turn-taking and conversational flow for clarity.

## Additional Information

### Dataset Curators

This dataset was generated by Google’s Gemini, based on a series of creative and therapeutic prompts provided by an Locutusque.

### Licensing Information

The Mind Corpus dataset is licensed under the MIT License.

### Citation

If you use this dataset in your research, please consider citing it as follows:

```bibtex
@misc{mind_corpus_2025,
  author       = {Locutusque},
  title        = {Mind Corpus Dataset},
  year         = {2025},
  publisher    = {Hugging Face},
  journal      = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/datasets/Locutusque/Mind-Corpus}}
}
```