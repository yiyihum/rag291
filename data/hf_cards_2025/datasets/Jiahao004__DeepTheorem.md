---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: source
    dtype: string
  - name: ori_question
    dtype: string
  - name: ori_solution
    dtype: string
  - name: domain
    sequence: string
  - name: difficulty
    dtype: float64
  - name: rationale
    dtype: string
  - name: informal_theorem
    dtype: string
  - name: informal_theorem_qa
    dtype: string
  - name: proof
    dtype: string
  - name: truth_value
    dtype: bool
  - name: pos
    struct:
    - name: question
      dtype: string
    - name: response
      dtype: string
    - name: truth_value
      dtype: bool
  - name: neg
    struct:
    - name: question
      dtype: string
    - name: response
      dtype: string
    - name: truth_value
      dtype: bool
  splits:
  - name: train
    num_bytes: 1146705612
    num_examples: 120754
  download_size: 554423240
  dataset_size: 1146705612
task_categories:
- text-generation
- reasoning
tags:
- reinforcement-learning
---

# DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning 🚀

Welcome to the GitHub repository for **DeepTheorem** 🎉, a comprehensive framework for enhancing large language model (LLM) mathematical reasoning through informal, natural language-based theorem proving. This project introduces a novel approach to automated theorem proving (ATP) by leveraging the informal reasoning strengths of LLMs, moving beyond traditional formal proof systems 🌟.

More info can be found in the paper [DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning](https://huggingface.co/papers/2505.23754)

## Overview 📖

<p align="center">
<img src="frontpage.png" width="800" />
</p>

Theorem proving is a critical benchmark for evaluating complex reasoning in LLMs 🧠. However, formal proof systems often misalign with the informal, natural language knowledge LLMs acquire during pre-training. DeepTheorem addresses this gap by introducing:

1. **A Large-Scale Theorem Proving Dataset** 📊: 
   - Contains **high-quality, IMO-level informal theorems and proofs** across diverse mathematical domains 📚.
   - Rigorously annotated for correctness, difficulty, and topic categories ✅.
   - Includes systematically constructed **verifiable theorem variants** for robust evaluation 🔍.
    
2. **RL-Zero** 🤖: 
   - A novel **reinforcement learning strategy** tailored for informal theorem proving ⚙️.
   - Utilizes verified theorem variants to incentivize robust mathematical inference 💡.

Deeptheorem demonstrates its superior performance over both opensource and commercial models (i.e Gemini and o1)

## Performance 🚀
Deeptheorem achieves the #Rank 5 position along all the commerical models and open source models.

| **Model**             | **FIMO** |         | **HMMT** |         | **Putnam** |         | **Avg.(\#Rank)** |         |
| :--------------------- | :------: | :-----: | :------: | :-----: | :--------: | :-----: | :------: | :-----: |
|                        | *out.*   | *proc.* | *out.*   | *proc.* | *out.*     | *proc.* | *out.*   | *proc.* |
| Gemini2\.5-Pro         | 57\.14   | 54\.06  | 57\.63   | 49\.82  | 64\.58     | 58\.75  | 59\.78(\#2)   | 54\.21(\#3)  |
| o1-mini                | 60\.32   | 55\.23  | 35\.59   | 30\.90  | 61\.46     | 52\.88  | 52\.46(\#4)   | 46\.34(\#4)  |
| o1                     | 66\.67   | 61\.00  | 47\.46   | 47\.30  | 62\.50     | 57\.55  | 58\.88(\#3)   | 55\.28(\#2)  |
| o3-mini                | 80\.95   | 77\.61  | 45\.76   | 43\.47  | 78\.12     | 75\.12  | 68\.28(\#1)   | 65\.40(\#1)  |
| *[DeepTheorem-RL-7B](https://huggingface.co/Jiahao004/DeepTheorem-qwen-7b-rl)     | 55\.56   | 39\.07  | 28\.81   | 20\.85  | 57\.29     | 42\.20  | 47\.22(\#5)   | 34\.04(\#5)  |
| *[DeepTheorem-RL-3B](https://huggingface.co/Jiahao004/DeepTheorem-qwen-3b-rl)     | 38\.10   | 23\.39  | 25\.42   | 13\.56  | 52\.08     | 33\.84  | 38\.53        | 23.60        | 
| *[DeepTheorem-RL-1.5B](https://huggingface.co/Jiahao004/DeepTheorem-qwen-1.5b-rl)   | 31\.75   | 15\.23  | 23\.73   | 10\.15  | 52\.08     | 22\.79  | 35\.85        | 16.06        | 

**Testing:** The testing set is available at [Jiahao004/HMMT_FIMO_Putnam](https://huggingface.co/datasets/Jiahao004/HMMT_FIMO_Putnam). Welcome to try and test your own models with our dataset!

## DeepTheorem Dataset 📊

The DeepTheorem dataset comprises **121K IMO-level informal theorems and proofs** spanning diverse mathematical domains 🌐. Each theorem-proof pair is rigorously annotated for:
- **o3-mini Proofs** 🖋️: Ensuring mathematical accuracy through proofs generated or verified by the o3-mini model ✅.
- **Truth Value** 🔍: The truth value of the theorem extracted from the o3-mini proofs, indicating whether the theorem is true or false ✔️.
- **Difficulty** 🎚️: Categorized by complexity to suit various LLM capabilities 🧩.
- **Topic Categories** 🗂️: Covering algebra, geometry, number theory, and more 📘.
- **Variants** 🔄: Positive or negative variants of the theorem that share the same or inverse truth value of the original theorem 🔀.