---
license: apache-2.0
tags:
- instruction-tuning
- code-generation
- synthetic-data
- persona
- multi-persona
---

# Dataset Card for "tame-the-weights-personas"

## Dataset Description

This dataset contains instruction-following data designed for fine-tuning language models, specifically focused on generating Python code explanations and snippets while adopting distinct personas.

The data was synthetically generated using a large language model, prompted to adopt one of three personas:

1.  **Professor Snugglesworth:** A friendly, encouraging, and slightly verbose persona, like a kind university professor.
2.  **Captain Codebeard:** A gruff, pirate-themed persona, offering direct and concise explanations with a nautical flair.
3.  **Zen Coder:** A calm, mindful persona, providing clear, step-by-step guidance with a focus on simplicity and clarity.

It includes both the initial seed examples for each persona and a larger set of generated examples following the same instruction format.

The primary goal of this dataset is to enable the fine-tuning of models capable of adapting their conversational style based on the `persona` tag, particularly for coding-related tasks.

## Dataset Structure

### Data Instances

A typical data instance looks like this:

```json
{
  "instruction": "Explain the concept of list comprehensions in Python.",
  "input": "",
  "output": "Ahoy there, matey! List comprehensions be a way t' create lists in Python based on existing lists, faster than yer usual loops. Imagine ye have a list o' numbers, `nums = [1, 2, 3, 4]`, and ye want a new list with each number squared. Instead o' a loop, ye write `squared_nums = [n*n for n in nums]`. Shiver me timbers, it's concise! It follows the pattern `[expression for item in iterable]`. Ye can add conditions too, like `[n*n for n in nums if n % 2 == 0]` t' only square the even numbers. Savvy?",
  "persona": "captain_codebeard"
}
```

### Data Fields

- `instruction` (string): The task or question the model should address.
- `input` (string): Optional additional context for the instruction (often empty in this dataset).
- `output` (string): The desired response, generated according to the persona's style.
- `persona` (string): The name of the persona the `output` adheres to. One of `professor_snugglesworth`, `captain_codebeard`, or `zen_coder`.

### Data Splits

The dataset contains a single split: `train`.

## How to Use

You can load this dataset using the `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("leonvanbokhorst/tame-the-weights-personas")

# Access the training split
train_data = dataset["train"]

# Example: Filter for a specific persona
zen_data = train_data.filter(lambda example: example["persona"] == "zen_coder")

print(train_data[0])
print(f"\nNumber of Zen Coder examples: {len(zen_data)}")
```

## Citation

If you use this dataset in your research or project, please consider citing it.

```bibtex
@misc{tame_the_weights_personas_dataset,
  author = {Master Lonn-san and Little Padawan},
  title = {Tame-the-Weights Personas Dataset},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/datasets/leonvanbokhorst/tame-the-weights-personas}}
}
```

## Dataset Creation

This dataset was created as part of the "Tame the Weights" project, exploring persona adaptation in fine-tuned language models. Initial seed data was manually created, and further examples were generated using the `scripts/generate_persona_data.py` script within the project repository.

## Licensing Information

The dataset is licensed under the Apache License, Version 2.0. See the `LICENSE` file for details (or refer to the standard Apache 2.0 terms).
