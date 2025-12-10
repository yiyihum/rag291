---
license: cdla-permissive-2.0
task_categories:
- text-generation
language:
- en
tags:
- clinical
- medical
size_categories:
- 1M<n<10M
---

# MediFlow

A large-scale synthetic instruction dataset of 2.5M rows (~700k unique instructions) for clinical natural language processing covering 14 task types and 98 fine-grained input clinical documents.

## t-SNE 2D Plot of MediFlow Embeddings by Task Types
<img src="tsne_mediflow_v0_3_4_5_task.png" alt="TSNE plot of data by task type" style="display: block; margin-left: auto; margin-right: auto; width: 75%; max-width: 100%"/>

## Dataset Splits

- `mediflow`: 2.5M instruction data for SFT alignment.
- `mediflow_dpo`: ~135k top-quality instructions with GPT-4o generated `rejected_output` for DPO alignment.

## Main Columns

- `instruction`: instructions for the task at hand.
- `input`: input example on which to apply the task.
- `output`: output example of what we expect from applying the instructions on the input.
- `task_type`: one of the 14 task types related to natural language processing.
- `input_data`: type of input data.
- `output_format`: format of the output (`plain_text` or `json`).
- `difficulty_level`: one of the six difficulty levels with emphasis on top-3 hardest levels.
- `rejected_output`: wrong output to reject with DPO (only `mediflow_dpo`, else '').
- `error_type`: error type introduced in `output` to get `rejected_output` (only `mediflow_dpo`, else '').

There are also LLM-as-a-Judge scores: `quality`, `alignment`, `coherence`, `realism`, and `difficulty`.

# Paper

  [A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment](https://arxiv.org/abs/2505.10717)

# License

This dataset is licensed under CDLA 2.0.

# Citation

    @article{corbeil2025modular,
      title={A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment},
      author={Corbeil, Jean-Philippe and Dada, Amin and Attendu, Jean-Michel and Abacha, Asma Ben and Sordoni, Alessandro and Caccia, Lucas and Beaulieu, Fran{\c{c}}ois and Lin, Thomas and Kleesiek, Jens and Vozila, Paul},
      journal={arXiv preprint arXiv:2505.10717},
      year={2025}
    }