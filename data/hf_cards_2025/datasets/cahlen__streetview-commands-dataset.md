---
language: en
license: apache-2.0
tags:
- text-generation
- instruction-tuning
- street-view
- navigation
- intent-recognition
- json
pretty_name: Street View Natural Language Command Dataset
dataset_info:
  splits:
  - name: train
    num_bytes: null
    num_examples: 10000
  download_size: null
  dataset_size: null
---

![EnfuseBot](https://i.imgur.com/IQD9atN.png)

# Dataset Card for streetview-commands-dataset

## Dataset Description

* **Homepage:** [https://cahlen.github.io](https://cahlen.github.io)
* **Repository:** [cahlen/streetview-commands-dataset](https://huggingface.co/datasets/cahlen/streetview-commands-dataset)
* **Point of Contact:** cahlen@gmail.com

This dataset contains pairs of natural language instructions (simulating commands given to Google Street View) and their corresponding structured JSON outputs representing the intended navigation action. It was generated using the Gemini API (gemini-1.5-flash-latest) based on predefined templates and few-shot examples.

The primary intended use is for **fine-tuning small language models (like TinyLlama)** to act as a translation layer between natural language commands and API calls needed to control an interactive Street View interface (e.g., within a React app using the Google Maps JavaScript API).

## Dataset Structure

The dataset is provided in JSON Lines (JSONL) format. Each line is a JSON object with two keys:

* `instruction`: (string) The natural language command input.
* `output`: (object) A JSON object representing the desired structured output. The object structure is:
    ```json
    {
      "action": "ACTION_TYPE",
      "parameters": { ... }
    }
    ```
    *(Note: Double braces used here for literal display in Markdown)*

### Data Fields

* `instruction`: The raw natural language text command.
* `output.action`: A string indicating the type of action requested (e.g., `set_pov`, `move`, `set_zoom`, `set_pano`, `look_at`).
* `output.parameters`: A dictionary containing parameters specific to the action (e.g., `heading_change`, `pitch_change`, `direction`, `change`, `address`, `latlng`, `pano_id`, `target_description`).

### Data Splits

Currently, the dataset is provided as a single file (`my_streetview_data.jsonl`). For fine-tuning, users should split this into training and validation sets as needed.

## Dataset Creation

* **Curation Rationale:** To create a dataset suitable for fine-tuning an LLM to understand and translate common Street View navigation commands into a structured format usable by APIs. Diversity in commands, phrasing, and target actions was prioritized.
* **Source Data:** The dataset was synthetically generated using the Google Gemini API (gemini-1.5-flash-latest) based on a set of prompt templates covering different action types and variations. Few-shot examples were provided within the prompts.
* **Annotations:** The 'output' JSON structure serves as the annotation for the 'instruction' field. Generation was guided by predefined templates and reviewed statistically, but individual item quality may vary. **Manual review is recommended.**
* **Personal and Sensitive Information:** The dataset was synthetically generated and should not contain real personal or sensitive information. Addresses and place names used are either common landmarks or potentially fabricated examples.

## Considerations for Using the Data

* **Limitations:** The dataset reflects the patterns present in the generation prompts. While diverse, it may not cover every possible phrasing or edge case for Street View commands. The quality is dependent on the generation capabilities of the LLM used. The 'look_at' action mapping is particularly complex and may require significant application-side logic.
* **Bias:** Generation may reflect biases inherent in the underlying LLM (gemini-1.5-flash-latest). Commands might lean towards certain types of phrasing or locations if not carefully balanced during generation/review.
* **Other Known Limitations:** The accuracy of generated `latlng` or `pano_id` values (when explicitly requested in hypothetical instructions) is not guaranteed unless they were part of the few-shot examples or known by the base model. The primary mechanism for location finding relies on the `address` parameter and external Geocoding.

## Additional Information

* **Licensing Information:** apache-2.0
* **Citation:**
    ```bibtex
    @misc{cahlen_streetview_commands_dataset_2025,
      author = {cahlen},
      title = {streetview-commands-dataset: Street View Natural Language Command Dataset},
      year = {2025},
      publisher = {Hugging Face},
      journal = {Hugging Face Hub},
      url = {[https://huggingface.co/datasets/](https://huggingface.co/datasets/)cahlen/streetview-commands-dataset}
    }
    ```
