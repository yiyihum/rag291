---
pretty_name: diffractgpt_jarvis_dft (XRD Spectra → Structure)
license: mit
tags:
- materials-science
- text-to-structure
- text2text-generation
- instruction-tuning
task_categories:
- text2text-generation
dataset_info:
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: null
    num_examples: null
  - name: test
    num_bytes: null
    num_examples: null
language:
- en
---

# diffractgpt_jarvis_dft (XRD Spectra → Structure)

**Goal.** Map a textual description of a material (composition + XRD peaks, etc.) to a compact crystal structure description (lattice lengths, angles, fractional coordinates, atom types).

## Data Fields
- `id` *(str)*: source identifier (e.g., POSCAR/JVASP id).
- `instruction` *(str)*: the generic instruction.
- `input` *(str)*: material description (composition, XRD, etc.).
- `output` *(str)*: target structure text (lattice lengths/angles + fractional coords).

## Splits
- `train.json`
- `test.json`

## Quickstart

```python
from datasets import load_dataset

ds = load_dataset("knc6/diffractgpt_jarvis_dft", data_files={
    "train": "train.json",
    "test": "test.json"
})
print(ds)
print(ds["train"][0])

