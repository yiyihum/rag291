---
license: cc-by-4.0
task_categories:
- feature-extraction
language:
- en
tags:
- instruction
- function-calling
- tool-use
- reasoning
- chain-of-thought
- agent
- chat
- dialogue
- tool-call
- structured-output
- llm-training
- fine-tuning
- cot-dataset
- instruction-tuning
- openai-compatible
- agent-training
- high-quality
- curated-dataset
- json-schema
- multi-turn
- top 10
- Thought
---

# Arcosoph Codex Weaver Function Calling Reasoning Dataset (V1)

## Dataset Description

Welcome to the **Arcosoph-Codex-Weaver-FC-Reasoning** dataset! This is a comprehensive, multi-source, and meticulously curated dataset designed for instruction-tuning language models to function as intelligent, offline AI agents.

This dataset is provided in a universal, easy-to-parse **JSON Lines (`.jsonl`)** format, making it an ideal "source of truth" for creating fine-tuning data for various models like Phi-3, Llama, Mistral, and more.

**Created by:** [Muhammad Abid](https://huggingface.co/arcosoph-creator)

---

## Dataset Philosophy and Structure

The core philosophy is to create a model that doesn't just execute tasks but also demonstrates a clear, logical thought process beforehand. This is inspired by state-of-the-art agent frameworks like **ReAct (Reasoning and Acting)**.

Each line in the `.jsonl` file is a JSON object representing a single, complete training example.
---
### The Universal Raw Format:

```jsonc
{
  "id": "a unique identifier, e.g., '0', '1', '2'...",
  "system_prompt": "The core instructions for the Arcosoph persona and task.",
  "query": "The user's question or instruction.",
  "response": "The desired assistant's full response, containing both thought and execution."
}
```
---
#### Structure of the `response` Field

The `"response"` field is a multi-line string containing two key components, inspired by professional agent architectures:

1.  **`Thought:`**: The model's internal monologue. It breaks down the user's query, formulates a logical plan, and decides on the best course of action. This teaches the model **to reason**.

2.  **`Execution:`**: The final, actionable output. This can be one of two types:
    *   **`tool_call(...)`**: A structured function call that an agent system can parse and execute.
    *   **`respond(...)`**: A direct, natural language answer for the user when no tool is needed.

---

## Dataset Composition

This dataset is a rich and diverse tapestry woven from multiple high-quality sources to provide a well-rounded education for an AI agent. The total size is approximately **[20,000]** examples.

The sources include selections from:

*   **Function Calling:** Multi-step reasoning with external API or code execution simulations*

*   **Reasoning Tasks:** Logical, step-by-step problem solving

*   **Persona Dialogue:** Human-like conversation with distinctive personality and empathy

*   **Mathematics & Coding:** Problems with worked-out solutions and explanations

**Purpose:** To provide a rich, ready-to-use resource for fine-tuning models to behave intelligently, naturally, and reliably in complex instruction-following scenarios.

---

## Intended Use & Conversion

This dataset is a **universal raw dataset**. It is not tied to any specific model's chat template.

To use this for fine-tuning, you will need a simple conversion script to transform it into the target model's specific format.

### Example Conversion to Phi-3 Format:

A single entry from this dataset can be converted into the following format for fine-tuning models like `microsoft/Phi-3-mini-4k-instruct`:

```python
<s><|user|>
{system_prompt}\n\n{query}<|end|>
<|assistant|>
{response}<|end|>
```

This two-step process (universal raw data -> model-specific data) is a professional workflow that ensures maximum reusability and modularity.

This is the first version of this dataset. We hope it serves as a valuable resource for the community in building the next generation of powerful and intelligent AI agents.
