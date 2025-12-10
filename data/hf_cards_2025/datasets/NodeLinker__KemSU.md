---
language:
- ru
multilinguality:
- monolingual
license: apache-2.0
tags:
- synthetic
- kemerovo-state-university
- kemsu
- instruction-tuning
- fine-tuning
annotations_creators:
- machine-generated
language_creators:
- found
pretty_name: Kemerovo State University Instructional QA Dataset
size_categories:
- 1K<n<10K
source_datasets:
- custom
task_categories:
- question-answering
task_ids:
- closed-domain-qa
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
  - split: validation
    path: validation.jsonl
  - split: test
    path: test.jsonl
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
    train:
      name: train
      num_bytes: 838488
      num_examples: 1324
    validation:
      name: validation
      num_bytes: 165399
      num_examples: 212
    test:
      name: test
      num_bytes: 161969
      num_examples: 219
  download_size: 1165856
  dataset_size: 1165856
---
# 🎓 Kemerovo State University Instructional QA Dataset (NodeLinker/KemSU)

<div align="center">
  <a href="https://kemsu.ru" target="_blank">
    <img src="https://huggingface.co/datasets/NodeLinker/KemSU/resolve/main/logo.jpg" alt="Логотип КемГУ - Перейти на сайт" width="400"/> 
  </a>
</div>
<div align="center" style="margin-top: 10px;">
  <a href="https://huggingface.co/datasets/NodeLinker/KemSU/blob/main/README.ru.md" target="_blank" style="margin: 2px;">
    <img alt="Читать на русском" src="https://img.shields.io/badge/Read%20in-Russian%20%F0%9F%87%B7%F0%9F%87%BA-blue" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0" target="_blank" style="margin: 2px;">
    <img alt="License: Apache 2.0" src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<br>

## 📝 Dataset Overview & Splits

This dataset provides instructional question-answer (Q&A) pairs meticulously crafted for **Kemerovo State University (КемГУ, KemSU)**, Russia. Its primary purpose is to facilitate the fine-tuning of Large Language Models (LLMs), enabling them to function as knowledgeable and accurate assistants on a wide array of topics concerning KemSU.

The dataset is organized into three distinct splits, each in **JSON Lines (`.jsonl`)** format:

*   🚂 **`train` (1324 examples):** The primary set for supervised fine-tuning (model weight updates).
*   ✅ **`validation` (212 examples):** Used during training to monitor performance, aid hyperparameter selection, and implement early stopping. Model weights are **not** updated using this data.
*   🧪 **`test` (219 examples):** A hold-out set for final, unbiased evaluation of the fine-tuned model on completely unseen data. This split must **not** be used during training or model selection.

---

## 📂 Data Sources

The Q&A triples are based on information from:

1.  **[Official Kemerovo State University Website](https://kemsu.ru):** Publicly available content from the main site and its associated subdomains.
2.  **[KemSU Live Telegram Channel](https://t.me/kemsu_live):** News, updates, and announcements from the university's public Telegram channel.
3.  **Curated Summaries:** Internal, structured summaries compiled by NodeLinker, detailing significant KemSU events and achievements, used as supplementary source material.

---

## 🧱 Dataset Structure & Fields

Each line in the `.jsonl` files is a JSON object representing a single instructional Q&A triple.

**Example Instance:**
```json
{
  "instruction": "Answer the question about Kemerovo State University.",
  "input": "When was the All-Russian Scientific and Practical Conference 'Regional Development: Economy and Society' held in 2018?",
  "output": "The All-Russian Scientific and Practical Conference 'Regional Development: Economy and Society' was held on March 21-22, 2018."
}
```

**Field Descriptions:**

*   `instruction` (string): Task instruction for the model (e.g., "Answer the question about KemSU.").
*   `input` (string): User's query or specific input. Can be empty if the instruction is self-sufficient.
*   `output` (string): Target answer, strictly based on source information.

---

## 🛠️ Data Creation Process

This dataset was predominantly generated using the **Gemini 2.5 Pro** LLM, guided by NodeLinker. The methodology included:

1.  **Source Material Preparation:** Text from designated sources was extracted and processed.
2.  **Iterative Generation:** Data for each split (`train`, `validation`, `test`) was generated in sub-phases targeting varied answer lengths. For `validation` and `test` splits, the LLM was conceptually cued about previously generated data to encourage distinct Q&A pairs.
3.  **Core LLM Instructions:**
    *   Strictly ground answers (`output`) in the provided source text.
    *   Maintain neutrality, avoiding bias or propaganda.
    *   Ensure accuracy, clarity, and natural language.
    *   Handle URLs by describing their purpose or omitting them, not including raw links.
4.  **Human Oversight:** Minimal spot-checking was performed by the dataset creator. Quality heavily relies on Gemini 2.5 Pro's instruction adherence.

**A Note on Quality and Distinction:**
LLM-generated data may contain occasional inaccuracies. The distinction between splits relies on LLM's interpretation of uniqueness prompts and was not exhaustively manually verified.

---

## 🎯 Intended Use & Applications

This dataset is primarily intended for:
*   Supervised fine-tuning (SFT) of LLMs.
*   Developing specialized Q&A systems about Kemerovo State University.
*   Benchmarking models on domain-specific instructional tasks.

---

## 🚀 Loading the Data

The recommended way to load this dataset is with the Hugging Face `datasets` library:

```python
from datasets import load_dataset

# Load all splits
dataset = load_dataset("NodeLinker/KemSU") 

train_data = dataset["train"]
validation_data = dataset["validation"]
test_data = dataset["test"]
```

---

## ⚠️ Limitations

*   **LLM Generation Artifacts:** Potential for occasional LLM errors (hallucinations, misinterpretations).
*   **Split Uniqueness:** Differentiation between splits is not a strict guarantee of non-overlapping semantic content.
*   **Coverage Scope:** Limited by information in the source materials about Kemerovo State University.
*   **Information Timeliness:** Reflects sources as of early-to-mid 2025.
*   **Source Material Reliability:** Dependent on the accuracy of original sources.

---

## ✍️ Citation Information

If you use this dataset in your research, please cite it as follows:

```bibtex
@misc{kemsu_instructional_qa_nodellinker_2025,
  author = {NodeLinker (Primarily Generated via Gemini 2.5 Pro with minimal supervision)},
  title = {Kemerovo State University Instructional QA Dataset},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/datasets/NodeLinker/KemSU}},
  note = {Instructional Q&A dataset (instruction, input, output format) for Kemerovo State University (KemSU), generated primarily by LLM (Gemini 2.5 Pro) based on kemsu.ru and t.me/kemsu_live. Contains train, validation, and test splits. Subject to potential LLM generation limitations.}
}
```