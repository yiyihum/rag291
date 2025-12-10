---
tags:
- function-calling
- chain-of-thought
- reasoning
- tool-use
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
license: apache-2.0
---

## 📌 Overview

- **Total Samples:** 10,000  
- **Primary Focus:**  
  - High-quality **Function Calling** demonstrations  
  - Clear, well-structured **Chain of Thought** reasoning  
- **Selection Process:**  
  - Translated from Chinese to English
  - Removed noisy or incomplete examples  
  - Selected cases with precise function arguments  
  - Each example has been made clearer and more effective
  - Ensured reasoning steps are logically sound and human-readable

---

## 🎯 Use Cases

This dataset is ideal for:
- Fine-tuning LLMs for **tool calling / function calling**
- Training models to provide **explainable reasoning (CoT)**
- Evaluating LLMs' ability to follow structured reasoning before producing function calls
- Benchmarking agent frameworks or automated reasoning pipelines

---

## 📊 Dataset Architecture

The dataset is structured with three core components for each example:

| Field           | Type            | Description                                                                                             |
|-----------------|-----------------|---------------------------------------------------------------------------------------------------------|
| `query`         | `string`        | The natural language prompt from the user, translated into English.                                     |
| `reasoning`     | `string`        | The model's explicit, step-by-step logical process (Chain-of-Thought) for arriving at the correct function call. |
| `function_call` | `list[dict]`    | The final, structured output—a list of one or more function calls in a machine-readable JSON format.    |


## 📜 License

This dataset inherits the license of the original dataset: **Apache-2.0**.

- ✅ **Free for research and commercial use**  
- ✅ **Modification and redistribution allowed**  
- ⚠️ **Attribution required** (see Credits section below)

---

## ✨ Credits

- **Original Dataset:** **AymanTarig**/Function-Calling-with-Chain-of-Thoughts and **twinkle-ai**/tw-function-call-reasoning-10k
- **Curated & Maintained By:** [Arcosoph AI](https://huggingface.co/Arcosoph)

---

## 🤝 Contribution

We welcome contributions!  
If you have additional high-quality function-calling + CoT examples, feel free to **submit a pull request** or **open an issue** to help improve this dataset.

---