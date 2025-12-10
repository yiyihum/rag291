---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 323455006
    num_examples: 41082
  download_size: 152719721
  dataset_size: 323455006
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- tr
tags:
- medical
- math
- general
- if
- reasoning
- sungur
size_categories:
- 10K<n<100K
---

<img src="./Sungur.png"/>

# Sungur-Dataset

## 📖 Overview

**Sungur-Dataset** is a large-scale, instruction–response style dataset designed to improve the **reasoning capabilities of Turkish language models**.
The dataset was created by merging **four publicly available reasoning datasets** into a unified format, resulting in **41,1k samples** covering multiple domains such as **mathematics, medicine, and general reasoning**.

This dataset is ideal for **Supervised Fine-Tuning (SFT)** in Turkish.

---

## 📊 Dataset Composition

Sungur-Dataset integrates the following sources:

* **[ituperceptron/turkish_medical_reasoning]**
* **[ituperceptron/turkish-general-reasoning-28k]**
* **[duxx/reasoning_dataset_turkish]**
* **[SoAp9035/r1-reasoning-tr]**

All datasets were reformatted into a **chat-style structure**:

```json
[
  {"role": "user", "content": "Question/Prompt"},
  {"role": "assistant", "content": "Answer (with reasoning if available)"}
]
```

---

## 🔍 Key Features

* **Size:** 41.1K reasoning samples
* **Languages:** Turkish (native + translated prompts)
* **Domains:** Math, Medical, General reasoning, and more
* **Structure:** Instruction–response pairs with optional `<think>...</think>` reasoning traces
* **Use Cases:**

  * Instruction fine-tuning of LLMs
  * Enhancing reasoning ability in Turkish models

---

## 📦 Example

```json
{
  "messages": [
    {"role": "user", "content": "Bir hasta göğüs ağrısıyla acile başvuruyor. İlk yapılacak tetkik nedir?"},
    {"role": "assistant", "content": "<think>\nÖncelikle kardiyak nedenler ekarte edilmelidir. Bu yüzden en acil test EKG'dir.\n</think>\n\nİlk yapılacak tetkik: EKG."}
  ],
  "source": "ituperceptron/turkish_medical_reasoning"
}
```

---

## 🚀 Usage

```python
from datasets import load_dataset

ds = load_dataset("suayptalha/Sungur-Dataset", split="train")

print(ds[0])
```

---

## 🙏 Acknowledgements

This dataset was made possible by integrating and reformatting several open-source datasets.
Special thanks to the following contributors and projects:

* **[ituperceptron](https://huggingface.co/ituperceptron)** for releasing *Turkish Medical Reasoning* and *Turkish General Reasoning* datasets.
* **[duxx](https://huggingface.co/duxx)** for creating the *Turkish Reasoning Dataset*.
* **[SoAp9035](https://huggingface.co/SoAp9035)** for publishing *R1-Reasoning-TR*.

## 📌 Citation

If you use **Sungur-Dataset**, please cite it as:

```
@misc{sungur_collection_2025,
  title        = {Sungur (Hugging Face Collection)},
  author       = {Şuayp Talha Kocabay},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/collections/suayptalha/sungur-68dcd094da7f8976cdc5898e}},
  note         = {Turkish LLM family and dataset collection}
}
```

---
license: apache-2.0
---