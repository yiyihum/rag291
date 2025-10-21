---
dataset_info:
  features:
  - name: problem
    dtype: string
  - name: answer
    dtype: string
  - name: source
    dtype: string
  - name: domain
    sequence: string
  - name: llama8b_solve_rate
    dtype: float64
  splits:
  - name: train
    num_bytes: 76969060
    num_examples: 251122
  download_size: 32238760
  dataset_size: 76969060
task_categories:
- question-answering
- text-generation
language:
- en
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
size_categories:
- 100K<n<1M
tags:
- mathematics
- math
- reinforcement-learning
- RL
- reasoning
- verifiable
- open-ended-questions
- closed-form-answers
license: apache-2.0
---


# Big-Math: A Large-Scale, High-Quality Math Dataset for Reinforcement Learning in Language Models

Big-Math is the largest open-source dataset of high-quality mathematical problems, curated specifically for reinforcement learning (RL) training in language models. With over 250,000 rigorously filtered and verified problems, Big-Math bridges the gap between quality and quantity, establishing a robust foundation for advancing reasoning in LLMs.

<div align="center">
  <a href="https://forms.synthlabs.ai/big-math" style="display: inline-block; background-color: #FFB5D8; color: black; font-weight: 600; border-radius: 9999px; padding: 1.5rem 2rem; text-align: center; font-size: 1.125rem; border: 2px solid black; box-shadow: 4px 4px 0px 0px rgba(0,0,0,1); text-decoration: none; margin-bottom: 1rem; transition: opacity 0.3s;">
    Request Early Access to Private Reasoning Evals ↗
  </a>
</div>

- 📄 [Click here to read the full details of how Big-Math was created in our paper!](https://arxiv.org/abs/2502.17387)
- 💾 [Click here for our github repo](https://github.com/SynthLabsAI/big-math) containing the filters used to create this, and the code for reformulating multiple choice problems into open-ended questions.

---

## 📊 Dataset Details


### Subsets
Big-Math is divided into the following subsets:
|**Subset** |**Number of Problems**|
|---|---|
|Orca-Math|	83,215|
|cn_k12| 63,609|
|olympiads| 33,485|
|MATH| 9,257|
|aops_forum| 5,740|
|GSM8k| 3,254|
|HARP| 2,996|
|Omni-MATH| 2,478|
|amc_aime| 78|
|Big-Math-Reformulated|	47,010|
|**Total**| 251,122|

### Columns
Each problem includes:
- **problem**: The math problem in text form.
- **answer**: A closed-form, verifiable answer.
- **source**: The dataset that the problem was sourced from.
- **domain**: The mathematics domain of the problem (eg. sequences and series).
- **llama8b_solve_rate**: The percent of Llama-3.1-8B rollouts that succeed (out of 64).

---

## 📋 Dataset Description

Big-Math was created to address the limitations of existing math datasets for reinforcement learning, which often force researchers to choose between quality and quantity. Key features of Big-Math include:
- **Uniquely verifiable solutions**: Problems with a single correct, verifiable answer.
- **Open-ended problem formulations**: Problems requiring reasoning instead of guesswork.
- **Closed-form solutions**: Problems with answers expressible in clear, closed-form expressions.

Additionally, we provide a new source of 47,000 problems, **Big-Math-Reformulated**, reformulated open-ended questions from multiple-choice formats.

---

## 🔍 Dataset Creation

Big-Math is curated using rigorous filtering and cleaning processes to ensure the inclusion of high-quality problems suitable for RL training of LLMs.
Below are the key filters and procedures (see the paper for full details):
- Deduplication (exact matching and semantic deduplication)
- Test set decontamination (using MATH-500 and Omni-MATH test sets)
- Remove non-English problems
- Remove problems with hyperlinks
- Remove problems that are unsolvable in 8 rollouts from Llama-3.1-405B or 64 rollouts from Llama-3.1-8B (excluded from this filter are all problems in HARP, Omni-MATH, MATH, and GSM8k)
- Remove multiple choice problems
- Remove yes/no and true/false problems
- Remove multi-part questions
- Remove questions asking for a proof
- Clean miscellaneous unnecessary information (eg. problem scoring)

---

## ⚙️ Big-Math-Reformulated
Big-Math-Reformulated was created by transforming multiple-choice questions into open-ended formats. This was done through a 4-step process:

- Key Information Extraction: Identified core mathematical concepts and rephrasing strategies.
- Reformulation: Rewrite questions into open-ended forms using the key information as a guide.
- Judgment: Ensure the reformulated problems maintained their mathematical integrity and uniqueness.
- Verification: Check that the full process succeeded

<p align="left">
  <img src="big_math_reformulation.png" width="85%">
</p>

## 🧩 Dataset Difficulty

The Llama-3.1-8B solve rate column can be used as a measure for problem difficulty. Below we plot the difficulty by source dataset, and by mathematics domain.

<p align="left">
    <img src="llama8b_solve_rate_distribution.png" width="85%">
</p>

<p align="left">
    <img src="llama8b_solve_rate_by_domain.png" width="85%">
</p>

---

## ⚠️ Unverified Dataset Subset

We have published an additional subset, containing problems that were unsolvable within the allotted rollouts from Llama-3.1-405B or Llama-3.1-8B models. This subset is considered "unverified," as it may contain incorrect, unparseable, or otherwise problematic question-answer-pairs. Researchers interested in more challenging or uncertain problems may find this subset useful.

🔗 [Access the Unverified Subset (SynthLabsAI/Big-Math-RL-UNVERIFIED)](https://huggingface.co/datasets/SynthLabsAI/Big-Math-RL-UNVERIFIED)

---

## Citation
If you use this dataset in your work, please cite us using the below citation:
```bibtex
@misc{albalak2025bigmathlargescalehighqualitymath,
      title={Big-Math: A Large-Scale, High-Quality Math Dataset for Reinforcement Learning in Language Models}, 
      author={Alon Albalak and Duy Phung and Nathan Lile and Rafael Rafailov and Kanishk Gandhi and Louis Castricato and Anikait Singh and Chase Blagden and Violet Xiang and Dakota Mahan and Nick Haber},
      year={2025},
      eprint={2502.17387},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2502.17387}, 
}
```