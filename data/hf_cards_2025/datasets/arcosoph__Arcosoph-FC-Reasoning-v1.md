---
license: apache-2.0
language:
- en
tags:
- phi-3
- function-calling
- tool-use
- reasoning
- agent-training
- instruction-tuning
- chain-of-thought
- sft
- trl
- unsloth
- chat-template
- persona
- conversational
- transformers
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/68c1b200edea09411075a29f/YXlRQYL3ICKhEchaZoPJV.png)

# Arcosoph-FC-Reasoning-v1

## Dataset Description

This repository contains the **Arcosoph-FC-Reasoning-v1**, a meticulously crafted dataset designed for supervised fine-tuning (SFT) of language models, especially `microsoft/Phi-3-mini-4k-instruct`. The dataset is provided in a ready-to-use **JSON Lines (`.jsonl`)** format, where each line represents a single training example.

The primary goal of this dataset is to teach a model not just to respond to queries, but to **reason, plan, and execute actions** through tool calls, all while maintaining a unique persona named **Arcosoph**. This dataset is the culmination of extensive research, experimentation, and iterative improvement.

**Created by:** [Abid](https://huggingface.co/arcosoph)

---

## Dataset Format and Structure

This dataset is pre-formatted for direct use with Hugging Face's `trl` library, particularly the `SFTTrainer`, and similar fine-tuning scripts. Each line in the `.jsonl` file is a JSON object with a single key: `"text"`.

The value associated with the `"text"` key is a string formatted according to the **official chat template of `microsoft/Phi-3-mini-4k-instruct`**.

### Structure of the `"text"` Field

```python
<s><|user|>
{SYSTEM_PROMPT}\n\n{USER_PROMPT}<|end|>
<|assistant|>
{ASSISTANT_RESPONSE}<|end|>
```

#### The `assistant` Response Structure

The core innovation of this dataset lies within the `{ASSISTANT_RESPONSE}`. It is structured to teach the model a "chain of thought" or reasoning process before acting. This structure is consistent across all examples.

```yaml
Reflection:
{The model's internal monologue or step-by-step thought process. It explains the 'why' and 'how' of its plan.}

Execution:
{The final, actionable output. This is either a tool call or a direct response to the user.}
```

**Types of `Execution`:**

*   **Tool Call:** `tool_call("tool_name", parameter="value")`
*   **Direct Response:** `respond("A direct, natural language answer to the user.")`

---

## Dataset Composition

This version of the dataset is a carefully balanced mix of two high-quality sources, ensuring the model learns both complex reasoning and its core identity. The total size is approximately **13,000 examples**.

1.  **Function Calling & Reasoning (~7,000 - 11,000 samples):**
    *   **Source:** A curated selection from a publicly available, high-quality function-calling dataset. The data has been transformed to fit the `Reflection/Execution` format.
    *   **Purpose:** To teach the model how to understand complex user requests, formulate a step-by-step reasoning process (Reflection), and generate structured tool calls (Execution). This forms the core of the agent's "brain."

2.  **Persona & Identity (~1,700 samples):**
    *   **Source:** A custom-built dataset containing question-answer pairs that define the Arcosoph persona.
    *   **Purpose:** To instill the model with a unique and consistent identity. The model learns that its name is Arcosoph and it was created by Abid.

---

## Intended Use

This dataset is intended for direct use in supervised fine-tuning (SFT) scripts that accept a pre-formatted text column. It is highly recommended for use with `microsoft/Phi-3-mini-4k-instruct` and frameworks like **Unsloth** for efficient training on consumer-grade hardware (like Google Colab).

### Example with `SFTTrainer`:

```python
from datasets import load_dataset
from trl import SFTTrainer

# ... (model and tokenizer loading code) ...

# Load the dataset
dataset = load_dataset("Arcosoph-FC-Reasoning-v1", split="train") 

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text", # This is the key to use
    max_seq_length=4096,
    # ... other SFTTrainer arguments
)

trainer.train()
```

## 📚 Sources / Attribution

Some examples in **Arcosoph-FC-Reasoning-v1** were inspired by the following public datasets:

- **[Microsoft/Orca-Math-Word-Problems-200k](https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k)**  
- **[AymanTarig/Function-Calling-with-Chain-of-Thoughts](https://huggingface.co/datasets/AymanTarig/Function-Calling-with-Chain-of-Thoughts)**  

⚠️ Note: While some examples were sourced from the above datasets, the **structure, formatting, and reasoning steps have been fully reworked, curated, and standardized by the Arcosoph Community** for consistency and quality.

This is the first version of the Arcosoph dataset. Future versions may include a wider variety of tools and more complex reasoning chains.