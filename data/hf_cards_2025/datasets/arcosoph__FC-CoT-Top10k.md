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
  - Removed noisy or incomplete examples  
  - Selected cases with precise function arguments  
  - Ensured reasoning steps are logically sound and human-readable  

---

## 🎯 Use Cases

This dataset is ideal for:
- Fine-tuning LLMs for **tool calling / function calling**
- Training models to provide **explainable reasoning (CoT)**
- Evaluating LLMs' ability to follow structured reasoning before producing function calls
- Benchmarking agent frameworks or automated reasoning pipelines
- **Version:** [New version available](https://huggingface.co/datasets/arcosoph/Arcosoph-FC-Reasoning-en-10k) (Translated)


## 📂 Dataset Structure

Each sample contains:
- **Instruction / User Prompt**
- **Model’s Chain of Thought**
- **Function Call Output** (JSON arguments or schema)

Example:

```jsonc
{
  "instruction": "Get the current weather for New York City.",
  "chain_of_thought": "First, I need to call the weather API with the correct location parameters...",
  "function_call": {
    "name": "get_weather",
    "arguments": {
      "location": "New York City",
      "unit": "metric"
    }
  }
}
```

## 📜 License

This dataset inherits the license of the original dataset: **Apache-2.0**.

- ✅ **Free for research and commercial use**  
- ✅ **Modification and redistribution allowed**  
- ⚠️ **Attribution required** (see Credits section below)

---

## ✨ Credits

- **Original Dataset:** [AymanTarig/Function-Calling-with-Chain-of-Thoughts](https://huggingface.co/datasets/AymanTarig/Function-Calling-with-Chain-of-Thoughts)  
- **Curated & Maintained By:** [Arcosoph AI](https://huggingface.co/Arcosoph)

---

⚡ **Note:** A new version of this dataset is available with clearer, more actionable examples. (Translated)
- Check it here: [New Version](https://huggingface.co/datasets/arcosoph/Arcosoph-FC-Reasoning-en-10k)




## 🤝 Contribution

We welcome contributions!  
If you have additional high-quality function-calling + CoT examples, feel free to **submit a pull request** or **open an issue** to help improve this dataset.

---