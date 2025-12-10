---
dataset: stage1-doctor-patient-chat
language:
- en
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: description
    dtype: string
  - name: utterances
    sequence: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 751307
    num_examples: 482
  - name: validation
    num_bytes: 105366
    num_examples: 60
  - name: test
    num_bytes: 93422
    num_examples: 61
  download_size: 508533
  dataset_size: 950095
tags:
- medical
- instruction-tuning
- LoRA
- tone-fine-tuning
- patient-doctor
---

# 🦷 Stage 1 - AI Doctor Tone Dataset (Dental)

This dataset contains instruction–response formatted examples derived from **realistic patient-doctor conversations**, focused on general medical behavior and tone. It is designed as **Stage 1** in a two-stage fine-tuning pipeline for building a domain-specific, polite, and structured AI dental assistant.

---

## ✨ Intended Use

- Fine-tuning large language models (LLMs) to simulate human-like, empathetic, and structured medical responses.
- Teaching models how to:
  - Speak politely and professionally
  - Structure answers clearly
  - Reassure patients using natural language

---

## 📁 Dataset Structure

| Split        | Examples |
|--------------|----------|
| `train`      | ~480     |
| `validation` | ~60      |
| `test`       | ~60      |

Each sample contains:

```json
{
  "prompt": "### Instruction:\n<patient message>\n\n### Response:",
  "response": "<doctor reply>"
}
```

---

## 📊 Source Dataset

This dataset is derived from [`antareepdey/Patient_doctor_chat`](https://huggingface.co/datasets/antareepdey/Patient_doctor_chat), formatted for instruction fine-tuning. The data was filtered to ensure clean question–answer pairs with doctor-style tone.

---

## 💡 How to Use

Load directly with 🤗 Datasets:

```python
from datasets import load_dataset

dataset = load_dataset("your-username/stage1-dental-tone")
```

---

## ⚠️ Limitations

- Generated responses are not medical advice.
- Should not be used in clinical settings without verification.

---

## 📜 License

MIT License – for research, experimentation, and educational use.

