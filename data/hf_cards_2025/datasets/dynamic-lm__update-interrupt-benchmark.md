---
license: apache-2.0
task_categories:
- text-generation
- question-answering
tags:
- large-language-model
- llm
- reasoning
- math
- code-generation
- robustness
- interrupt
dataset_info:
- config_name: Math
  features:
  - name: id
    dtype: int32
  - name: source
    dtype: string
  - name: original_problem
    dtype: string
  - name: original_answer
    dtype: string
  - name: revised_problem
    dtype: string
  - name: update
    dtype: string
  splits:
  - name: test
    num_bytes: 849823
    num_examples: 1060
    dataset_name: update-interrupt-benchmark
- config_name: Coding
  features:
  - name: id
    dtype: int32
  - name: platform
    dtype: string
  - name: contest_id
    dtype: string
  - name: difficulty
    dtype: string
  - name: question_title
    dtype: string
  - name: original_starter_code
    dtype: string
  - name: original_problem
    dtype: string
  - name: revised_starter_code
    dtype: string
  - name: revised_problem
    dtype: string
  - name: update
    dtype: string
  splits:
  - name: test
    num_bytes: 816276
    num_examples: 341
    dataset_name: update-interrupt-benchmark
configs:
- config_name: Math
  data_files:
  - split: test
    path: data_math.parquet
- config_name: Coding
  data_files:
  - split: test
    path: data_code.parquet
---

# Update-Driven Math & Code Interrupt Datasets

<img src="logo.png" alt="Interrupt-LRM logo" width="250">

- Paper: [Are Large Reasoning Models Interruptible?](https://arxiv.org/abs/2510.11713)

- Authors: Tsung-Han Wu*, Mihran Miroyan*, David Chan, Trevor Darrell, Narges Norouzi, Joseph Gonzalez

- Project page: [https://dynamic-lm.github.io/](https://dynamic-lm.github.io/)

- Github: [https://github.com/dynamic-lm/interrupt-lrm](https://github.com/dynamic-lm/interrupt-lrm)

This dataset page contains the update-driven interrupt subsets for math (GSM8K, MATH500, AIME) and coding (LiveCodeBench) problems. For both splits, we revise the source problems and create corresponding update instructions using GPT-5, followed by manual human validation. Additional details on the data generation pipeline (e.g., prompts) are provided in the appendix of the [paper](https://arxiv.org/abs/2510.11713).

## Math Subset

### Source Overview

We sample 500 problems from GSM8K and the full MATH 500 and AIME 2024 / 2025 sets. Each original problem is augmented with the revised problem and a corresponding update instruction.

### Dataset Fields

| Field name       | Type   | Description |
|------------------|--------|-------------|
| `id` | `int` | Unique problem identifier |
| `source` | `str` | Dataset source (`gsm8k`, `math500`, `aime2024`, `aime2025`) |
| `original_problem` | `str` | Original problem text from the source dataset |
| `original_answer` | `str` | Original answer from the source dataset |
| `revised_problem` | `str` | Revised version of the original problem |
| `update` | `str` | Update instruction from the revised to the original version |

**Loading**
```python
update_interrupt_math = load_dataset("dynamic-lm/update-interrupt-benchmark", "Math", split="test")
```

## Coding Subset

### Source Overview

We pull the 6th version of LiveCodeBench and filter for problems dated between 2024-10-01 and 2025-05-01. We revise the original problem text and, where needed, the starter code, and then generate an update instruction.

### Dataset Fields

| Field name       | Type   | Description |
|------------------|--------|-------------|
| `id` | `int` | Unique problem identifier |
| `platform` | `str` | Coding platform (`atcoder`, `leetcode`) |
| `contest_id` | `str` | Contest ID |
| `difficulty` | `str` | Problem difficulty (`easy`, `medium`, `hard`) |
| `question_title` | `str` | Question title from the source dataset |
| `original_starter_code` | `str` | Original starter code from the source dataset |
| `original_problem` | `str` | Original problem text from the source dataset |
| `revised_starter_code` | `str` | Revised version of the starter code (original starter code if not updated) |
| `revised_problem` | `str` | Revised version of the original problem |
| `update` | `str` | Update instruction from the revised to the original version |

Public and private test cases are not included in the dataset; we use the test cases from the official LiveCodeBench HuggingFace page ([`livecodebench/code_generation_lite`](https://huggingface.co/datasets/livecodebench/code_generation_lite)).

**Loading**
```python
update_interrupt_coding = load_dataset("dynamic-lm/update-interrupt-benchmark", "Coding", split="test")
```

### Citation

```
@misc{wu2025largereasoningmodelsinterruptible,
      title={Are Large Reasoning Models Interruptible?}, 
      author={Tsung-Han Wu and Mihran Miroyan and David M. Chan and Trevor Darrell and Narges Norouzi and Joseph E. Gonzalez},
      year={2025},
      eprint={2510.11713},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.11713}, 
}
```