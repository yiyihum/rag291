---
license: apache-2.0
pretty_name: MiniCodeTasks DeepSeek Train
language:
- en
task_categories:
- text-generation
- code-generation
tags:
- code-generation
- instruction-tuning
- deepseek
- fine-tuning
- slm
- open-source
- ai-dataset
- python
size_categories:
- 1K<n<10K
---

 
 
# MiniCodeTasks_DeepSeekTrain

A lightweight, instruction-based dataset curated by **Muhammad Yasir** for fine-tuning code generation models like `DeepSeek-Coder 1.3B`.

This dataset is tailored for **Small Language Models (SLMs)** and code assistant use-cases, making it ideal for training custom developer tools, coding bots, and programming-focused chat agents.

---

## 🧠 Dataset Overview

- **Title:** MiniCodeTasks_DeepSeekTrain
- **Type:** Instruction-Response (Code Generation)
- **Size:** 1,000+ handcrafted samples (v1.0)
- **Format:** JSON (with `instruction` and `response` fields)
- **Language:** English
- **Target Model:** DeepSeek-Coder 1.3B (also compatible with Mistral, LLaMA, CodeGen)

---

## 📁 Data Structure

Each entry in the dataset follows this format:

```json
{
  "instruction": "Write a Python function to reverse a string.",
  "response": "def reverse_string(s):\n    return s[::-1]"
}
````

---

## 💼 Use Cases

This dataset is suitable for:

* Code generation fine-tuning
* Building coding copilots
* Automating developer documentation
* Training local programming assistants
* Education bots / tutoring models

---

## 🏷️ Metadata

* **License:** Apache-2.0
* **Language:** English
* **Tags:** code-generation, deepseek, small-language-models, instruction-tuning, fine-tuning, open-source, ai-datasets
* **Pretty Name:** MiniCodeTasks DeepSeek Train
* **Size Categories:** 1K–10K
* **Task Categories:** text-generation, code-generation

---

## 🧪 Recommended Models

* [DeepSeek-Coder 1.3B](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base)
* [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)
* [Phi-3 Mini](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
* [CodeLlama](https://huggingface.co/codellama)

---

## 📜 License

This dataset is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
You are free to use, distribute, and adapt it for both non-commercial and commercial purposes with proper attribution.

---

## 📌 Author

**👨‍💻 Muhammad Yasir**
AI & Machine Learning Engineer | Developer | Security Researcher

* 🌐 [Portfolio Website](https://devsecure.netlify.app)
* 💻 [GitHub](https://github.com/devxyasir)
* 🐦 [Twitter / X](https://twitter.com/devxyasir)
* 🧠 [Hugging Face](https://huggingface.co/devxyasir)
* 📧 Email: [jamyasir0534@gmail.com](mailto:jamyasir0534@gmail.com)

---

If you find this dataset useful, drop a ⭐ on my GitHub or share your results with me — I’d love to see what you build!
Let’s shape the future of open-source AI, one smart model at a time 🚀
 
 
