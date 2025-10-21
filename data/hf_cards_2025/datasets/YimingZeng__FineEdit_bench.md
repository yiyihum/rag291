---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
tags:
- text-editing
- instruction-tuning
- llm
- benchmark
- code
- latex
- database
---

# FineEdit Dataset

[Paper](https://huggingface.co/papers/2502.13358) | [GitHub Repository](https://github.com/StuRinDQB/FineEdit)

## Introduction

This repository contains **InstrEditBench**, a high-quality benchmark dataset introduced in the paper [Bridging the Editing Gap in LLMs: FineEdit for Precise and Targeted Text Modifications](https://huggingface.co/papers/2502.13358) accpeted by **EMNLP 2025**

Large Language Models (LLMs) have significantly advanced natural language processing,
demonstrating strong capabilities in tasks such
as text generation, summarization, and reasoning. Recently, their potential for automating
precise text editing tasks across specialized domains, such as programming code, LaTeX, and
structured database languages, has gained attention. However, current state-of-the-art LLMs
still struggle with executing precise, instructiondriven edits, particularly when structural accuracy and strict adherence to domain conventions are required. To address these challenges, we introduce InstrEditBench, an automated benchmark dataset comprising over
30,000 structured editing tasks spanning diverse domains, including Wikipedia articles,
LaTeX documents, source code, and database
languages. Using this benchmark, we develop FineEdit, a specialized editing model
explicitly trained for accurate, context-aware
text modifications. Experimental evaluations
demonstrate that FineEdit outperforms stateof-the-art models, achieving improvements of
approximately 10% over Gemini models on
single-turn edits, up to 30% over Llama-3.2-
3B, and exceeding Mistral-7B-OpenOrca performance by over 40% on direct editing tasks.
FineEdit also effectively generalizes to realistic multi-turn editing scenarios, highlighting
its practical applicability. To facilitate further
research and reproducibility, we release FineEdit at https://github.com/StuRinDQB/
FineEdit and https://huggingface.co/
datasets/YimingZeng/FineEdit_bench
## Dataset Structure

**InstrEditBench** (referred to as **FineEdit** in this dataset repository) is designed for advancing **instruction-based text editing in large language models (LLMs)**. Each entry in the dataset contains:

-   **context**: the original text
-   **edit_request**: the editing instruction
-   **edit_content**: the edited text
-   **diff**: the difference between the original and edited text
-   **g_score**: a quality score assessing the edit

This dataset enables training and evaluation of **precise and targeted text modifications** in LLMs.

## Models
-   [**FineEdit-XL**] (https://huggingface.co/YimingZeng/FineEdit_Model)
-   [**FineEdit-Pro**] (https://huggingface.co/YimingZeng/FineEdit_Model)

## Metrics

Following established approaches (Nakamachi et al., 2020; Shen et al., 2017), we use BLEU
and ROUGE-L metrics to assess the vocabulary
and structural consistency between the edited and
reference texts.

## Citation

Please cite our paper if you use this benchmark:

```bibtex
@misc{zeng2025bridgingeditinggapllms,
      title={Bridging the Editing Gap in LLMs: FineEdit for Precise and Targeted Text Modifications}, 
      author={Yiming Zeng and Wanhao Yu and Zexin Li and Tao Ren and Yu Ma and Jinghan Cao and Xiyan Chen and Tingting Yu},
      year={2025},
      eprint={2502.13358},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.13358}, 
}
```