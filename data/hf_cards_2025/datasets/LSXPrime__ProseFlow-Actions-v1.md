---
license: mit
tags:
- text-generation
- instruction-tuning
- writing-assistant
- code-assistant
- nlp
---

# ProseFlow-Actions-v1 Dataset

## Dataset Description

**ProseFlow-Actions-v1** is a high-quality, diverse dataset of structured instructions designed for fine-tuning language models to act as versatile text-processing assistants. This dataset is the backbone of the local AI engine for the [ProseFlow desktop application](https://github.com/LSXPrime/ProseFlow), a universal, hotkey-driven AI utility.

The dataset is composed of **1,805 examples** (1742 training, 63 testing) across **88 unique "Actions"**. Each example is a self-contained instruction set that includes:
-   **`ActionName`**: A human-readable name for the task (e.g., "Improve Writing," "Refactor Code").
-   **`SystemPrompt`**: A detailed, structured prompt that defines the AI's role, operating principles, constraints (like "output only the rewritten text"), and examples of perfect operation.
-   **`Input`**: The user-provided text to be processed.
-   **`Output`**: The ideal, ground-truth response that perfectly adheres to the `SystemPrompt`.

This structure makes it ideal for supervised fine-tuning of instruction-following models.

### Why This Dataset?

Most instruction datasets focus on general chat or broad reasoning. **ProseFlow-Actions-v1** is specifically curated for a "tool-based" workflow, where an LLM is expected to perform a discrete, well-defined text transformation with high fidelity and strict adherence to formatting constraints.

It covers a wide spectrum of real-world use cases, making it a valuable resource for training models that can:
-   **Enhance Writing:** From simple proofreading to complex tonal shifts (formal, casual, empathetic).
-   **Manipulate Text:** Summarize, expand, convert to bullet points, and change narrative perspective.
-   **Assist with Code:** Explain, refactor, debug, and add comments to code snippets in various languages.
-   **Perform Business Tasks:** Draft professional emails, summarize meeting notes, and create SWOT analyses.
-   **Engage in Creative Work:** Continue stories, brainstorm ideas, generate haikus, and write movie loglines.
-   **Apply Logical Reasoning:** Solve word problems, identify logical fallacies, and follow complex conditional instructions.

## Dataset Structure

The dataset is provided in JSON format and is split into `train` and `test` files.

### Data Fields

Each object in the JSON files has the following structure:

```json
{
  "ActionName": "string",
  "SystemPrompt": "string",
  "Input": "string",
  "Output": "string"
}
```
*   **`ActionName`**: The name of the task.
*   **`SystemPrompt`**: The detailed instruction set for the language model. This should be used as the system prompt or the first part of the instruction.
*   **`Input`**: The user's text.
*   **`Output`**: The target completion for the model to generate.

## Dataset Statistics

### `dataset_train.json`
*   **Total Examples:** 1,742
*   **Unique Actions:** 88

**Top 10 Most Frequent Actions (Training Set):**
1.  `Improve Writing`: 189
2.  `Format Address Block`: 124
3.  `Make Casual`: 77
4.  `Extract Names and Companies`: 77
5.  `Refactor Code`: 65
6.  `Proofread`: 64
7.  `Add Comments`: 55
8.  `To Paragraph`: 49
9.  `Extract Action Items`: 47
10. `Make Formal`: 46

### `dataset_test.json`
*   **Total Examples:** 63
*   **Unique Actions:** 63

The test set is designed to provide broad coverage, with one representative example for each of the 63 most important and distinct actions. This ensures a comprehensive evaluation of a model's versatility.

## Use Cases and Models

This dataset was used to fine-tune the official models for the [ProseFlow](http://lsxprime.github.io/proseflow-web) application:
*   [**ProseFlow-v1-1.5B-Instruct**](https://huggingface.co/LSXPrime/ProseFlow-v1-1.5B-Instruct) (based on Qwen2.5-Coder-1.5B-Instruct)
*   [**ProseFlow-v1-360M-Instruct**](https://huggingface.co/LSXPrime/ProseFlow-v1-360M-Instruct) (based on SmolLM-360M-Instruct)

It is suitable for fine-tuning a wide range of instruction-based models, particularly those intended for tool-like text processing rather than open-ended chat. The detailed system prompts, which include roles, principles, and examples, provide rich context for the model to learn complex behaviors and constraints.

## Licensing

The dataset is released under the **MIT License**, making it freely available for both academic and commercial use.
