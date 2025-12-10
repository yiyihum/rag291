---
language:
- dv
license: other
tags:
- dhivehi
- instruction-tuning
- question-answering
- low-resource
size_categories:
- n<1K
task_categories:
- text-generation
- question-answering
pretty_name: Dhivehi QA Instruction Dataset
---

# Dhivehi Question–Answer Instruction Dataset

This repository contains a simple JSON dataset of **Dhivehi (ދިވެހި)** question–answer pairs formatted as `instruction`–`input`–`output` triples.  
It is intended for **instruction tuning**, **chatbot prototyping**, and **question-answering** tasks in Dhivehi.

---

## Dataset Overview

- **Language:** Dhivehi (dv)  
- **Script:** Thaana  
- **Format:** JSON list of records  
- **Fields:**  
  - `instruction`: prompt or task directive (e.g., “Answer the question in Dhivehi”)  
  - `input`: the question (Dhivehi)  
  - `output`: the answer (Dhivehi)

Example entry:
```json
{
  "instruction": "Answer the question in Dhivehi",
  "input": "މާލެއަކީ ކޮންތާކުތޯ؟",
  "output": "މާލެއަކީ ދިވެހިރާއްޖޭގެ ވެރިރަށް."
}
