---
license: apache-2.0
tags:
- Reformed
- Christian
- Bible
- Theology
- Jesus
- Seminary
pipeline_tag: text-generation
---

# Reformed Christian Bible Expert

A specialized language model fine-tuned for Reformed theology and biblical studies. Based on `mistralai/Mistral-Nemo-Instruct-2407` for superior theological reasoning with a **128k token context window**.

## Features

- 🕊️ Answers theological questions from a Reformed/Calvinist perspective
- ✝️ Explains biblical passages with historical-grammatical hermeneutics
- 🎓 Assists with seminary studies and sermon preparation
- 💬 Can roleplay as a pastor for counseling scenarios
- 📜 Inherits 128k context window from base model

## Usage

**Chat Template:** Mistral V3 Tekken
**Recommended Settings:**
```python
{
  "temperature": 0,
  "top_k": 1,
  "top_p": 0,
  "min_p": 0,
  "repetition_penalty": 1.18
}
```

**Example Prompt:**
```
[INST] Explain the doctrine of justification by faith alone from Romans 3:28 [/INST]
```

## Quantized Formats

- **EXL2 Collection**:
  [Reformed-Christian-Bible-Expert EXL2 Models](https://huggingface.co/collections/sleepdeprived3/reformed-christian-bible-expert-exl2-67ace8acd900c8cadd4c2a4e)

- **GGUF Collection**:
  [Reformed-Christian-Bible-Expert GGUF Models](https://huggingface.co/collections/sleepdeprived3/reformed-christian-bible-expert-gguf-67ace8b70d16eec807037c6e)

## Training Details

- **Base Model**: `mistralai/Mistral-Nemo-Instruct-2407` (128k context)
- **Fine-Tuning**: QLoRA on curated Reformed theological texts
- **License**: Apache 2.0

## Ethical Considerations

This model is designed to:
- Affirm the authority of Scripture (2 Tim 3:16)
- Uphold the Westminster Standards
- Avoid speculative theology

*Soli Deo Gloria*