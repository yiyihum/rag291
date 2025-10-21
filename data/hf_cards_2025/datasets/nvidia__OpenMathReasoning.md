---
language:
- en
license: cc-by-4.0
size_categories:
- 1M<n<10M
task_categories:
- question-answering
- text-generation
pretty_name: OpenMathReasoning
tags:
- math
- nvidia
configs:
- config_name: default
  data_files:
  - split: cot
    path: data/cot-*
  - split: tir
    path: data/tir-*
  - split: genselect
    path: data/genselect-*
  - split: additional_problems
    path: data/additional_problems-*
dataset_info:
  features:
  - name: expected_answer
    dtype: string
  - name: problem_type
    dtype: string
  - name: problem_source
    dtype: string
  - name: generation_model
    dtype: string
  - name: pass_rate_72b_tir
    dtype: string
  - name: problem
    dtype: string
  - name: generated_solution
    dtype: string
  - name: inference_mode
    dtype: string
  - name: used_in_kaggle
    dtype: bool
  splits:
  - name: cot
    num_bytes: 71639174648
    num_examples: 3201061
  - name: tir
    num_bytes: 35746562996
    num_examples: 1718466
  - name: genselect
    num_bytes: 6981124435
    num_examples: 565620
  - name: additional_problems
    num_bytes: 66328865
    num_examples: 193170
  download_size: 49585391985
  dataset_size: 114433190944
---


# OpenMathReasoning

 
OpenMathReasoning is a large-scale math reasoning dataset for training large language models (LLMs). 
This dataset contains 

* 306K unique mathematical problems sourced from [AoPS forums](https://artofproblemsolving.com/community) with: 
    * 3.2M long chain-of-thought (CoT) solutions
    * 1.7M long tool-integrated reasoning (TIR) solutions
    * 566K samples that select the most promising solution out of many candidates (GenSelect)
* Additional 193K problems sourced from AoPS forums (problems only, no solutions)

We used [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) to preprocess problems, and 
[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) and [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B) to generate solutions. 

This dataset was a foundation of our winning submission to the 
[AIMO-2 Kaggle competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-2/leaderboard).

See our [paper](https://arxiv.org/abs/2504.16891) to learn more details!

**_NOTE:_** We initially reported 540K unique problems in our dataset, but this figure represented the question count at the pipeline's beginning. But the actual CoT and TIR solutions in the released dataset correspond to 306K problems. Since our OpenMath-Nemotron models were trained on this reduced subset, all published results remain reproducible with the current release—only our initial problem count was overstated.

Two factors explain this discrepancy in question numbers. 
- Our filtering process removed many questions due to format restrictions (yes/no questions, multiple choice questions, etc.), benchmark decontamination, and the inability of existing LLMs to generate valid solutions for certain problems. 
- A pipeline bug caused us to lose 137K proof-based questions. When we recovered and included this additional data in training, the SFT performance regressed. We are currently testing different approaches for incorporating these recovered questions and will release their solutions only if we identify clear performance improvements.


 
**_NOTE:_** An early version of this data was released separately in [Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset).

## Dataset fields

OpenMathReasoning dataset contains the following fields:

- **problem**: Problem statement extracted from [AoPS forums](https://artofproblemsolving.com/community) and refined with [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct)
- **generated_solution**: Synthetically generated solution using either [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) or [QwQ-32B](https://huggingface.co/Qwen/QwQ-32B)
- **generation_model**: DeepSeek-R1 or QwQ-32B
- **problem_type**: Can be one of "has_answer_extracted", "no_answer_extracted" and "converted_proof" dependening on whether we were able to extract the answer or if this is a proof question converted to answer question.
- **expected_answer**: Extracted answer if "problem_type" is "has_answer_extracted". Otherwise this is the majority-voting answer across all generated solutions for this problem.
- **problem_source**: States the corresponding AoPS forum (e.g. "aops_c6_high_school_olympiads") or "MATH_training_set" as we also include a small set of generations from [MATH](https://github.com/hendrycks/math).
- **inference_mode**: "cot", "tir" or "genselect"
- **pass_rate_72b_tir**: Pass rate out of 32 generations for [Qwen2.5-Math-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Math-72B-Instruct) run in TIR mode. This attribute is only available when "problem_type" is "has_answer_extracted" and is set to "n/a" for other cases. 
- **used_in_kaggle**: Whether the instance was used in training the winning model for [AIMO-2 Kaggle competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-2/leaderboard) or not. We had used 2.2M CoT and 15K TIR solutions for training the [OpenMath-Nemotron-14B-Kaggle](https://huggingface.co/nvidia/OpenMath-Nemotron-14B-Kaggle) model. Note that for training the OpenMath-Nemotron models, we used all the CoT, TIR, and GenSelect data, except for the TIR subset used in Kaggle.  

## OpenMath-Nemotron models

To demonstrate the quality of this dataset, we release a series of OpenMath-Nemotron models trained on this data.

* [OpenMath-Nemotron-1.5B](https://huggingface.co/nvidia/OpenMath-Nemotron-1.5B)
* [OpenMath-Nemotron-7B](https://huggingface.co/nvidia/OpenMath-Nemotron-7B)
* [OpenMath-Nemotron-14B](https://huggingface.co/nvidia/OpenMath-Nemotron-14B)
* [OpenMath-Nemotron-14B-Kaggle](https://huggingface.co/nvidia/OpenMath-Nemotron-14B-Kaggle) (this is the model used in [AIMO-2 Kaggle competition](https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-2/leaderboard))
* [OpenMath-Nemotron-32B](https://huggingface.co/nvidia/OpenMath-Nemotron-32B)

![Evaluation Results](./results.png)

The models achieve state-of-the-art results on popular mathematical benchmarks. We present metrics as pass@1 (maj@64) where pass@1
is an average accuracy across 64 generations and maj@64 is the result of majority voting. 
Please see our [paper](https://arxiv.org/abs/2504.16891) for more details on the evaluation setup.

| Model                         | AIME24 |  AIME25     |  HMMT-24-25     | HLE-Math    |
|-------------------------------|-----------------|-------|-------|-------------|
| DeepSeek-R1-Distill-Qwen-1.5B | 26.8 (60.0)     | 21.4 (36.7) | 14.2 (26.5) | 2.9 (5.0)   |
| [OpenMath-Nemotron-1.5B](https://huggingface.co/nvidia/OpenMath-Nemotron-1.5B) CoT   | 61.6 (80.0)     | 49.5 (66.7) | 39.9 (53.6) | 5.4 (5.4)   |
| [OpenMath-Nemotron-1.5B](https://huggingface.co/nvidia/OpenMath-Nemotron-1.5B) TIR   | 52.0 (83.3)     | 39.7 (70.0) | 37.2 (60.7) | 2.5 (6.2)   |
| + Self GenSelect              | 83.3            | 70.0  | 62.2  | 7.9         |
| + 32B GenSelect               | 83.3            | 70.0  | 62.8  | 8.3         |
| DeepSeek-R1-Distill-Qwen-7B  | 54.4 (80.0)     | 38.6 (53.3) | 30.6 (42.9) | 3.3 (5.2)   |
| [OpenMath-Nemotron-7B](https://huggingface.co/nvidia/OpenMath-Nemotron-7B) CoT    | 74.8 (80.0)     | 61.2 (76.7) | 49.7 (57.7) | 6.6 (6.6)   |
| [OpenMath-Nemotron-7B](https://huggingface.co/nvidia/OpenMath-Nemotron-7B) TIR    | 72.9 (83.3)     | 57.5 (76.7) | 54.6 (66.3) | 7.8 (10.8)  |
| + Self GenSelect              | 86.7            | 76.7  | 68.4  | 11.5        |
| + 32B GenSelect               | 86.7            | 76.7  | 69.9  | 11.9        |
| DeepSeek-R1-Distill-Qwen-14B | 65.8 (80.0)     | 48.4 (60.0) | 40.1 (52.0) | 4.2 (4.8)   |
| [OpenMath-Nemotron-14B-MIX (kaggle)](https://huggingface.co/nvidia/OpenMath-Nemotron-14B-Kaggle) | 73.7 (86.7) | 57.9 (73.3) | 50.5 (64.8) | 5.7 (6.5)   |
| [OpenMath-Nemotron-14B](https://huggingface.co/nvidia/OpenMath-Nemotron-14B) CoT   | 76.3 (83.3)     | 63.0 (76.7) | 52.1 (60.7) | 7.5 (7.6)   |
| [OpenMath-Nemotron-14B](https://huggingface.co/nvidia/OpenMath-Nemotron-14B) TIR   | 76.3 (86.7)     | 61.3 (76.7) | 58.6 (70.9) | 9.5 (11.5)  |
| + Self GenSelect              | 86.7            | 76.7  | 72.4  | 14.1        |
| + 32B GenSelect               | 90.0            | 76.7  | 71.9  | 13.7        |
| QwQ-32B                       | 78.1 (86.7)     | 66.5 (76.7) | 55.9 (63.3) | 9.0 (9.5)   |
| DeepSeek-R1-Distill-Qwen-32B | 66.9 (83.3)     | 51.8 (73.3) | 39.9 (51.0) | 4.8 (6.0)   |
| [OpenMath-Nemotron-32B](https://huggingface.co/nvidia/OpenMath-Nemotron-32B) CoT   | 76.5 (86.7)     | 62.5 (73.3) | 53.0 (59.2) | 8.3 (8.3)   |
| [OpenMath-Nemotron-32B](https://huggingface.co/nvidia/OpenMath-Nemotron-32B) TIR   | 78.4 (93.3)     | 64.2 (76.7) | 59.7 (70.9) | 9.2 (12.5)  |
| + Self GenSelect              | 93.3            | 80.0  | 73.5  | 15.7        |
| DeepSeek-R1                   | 79.1 (86.7)     | 64.3 (73.3) | 53.0 (59.2) | 10.5 (11.4) |

## Reproducing our results

The pipeline we used to produce the data and models is fully open-sourced!

- [Code](https://github.com/NVIDIA/NeMo-Skills)
- [Models](https://huggingface.co/collections/nvidia/openmathreasoning-68072c0154a5099573d2e730)
- [Dataset](https://huggingface.co/datasets/nvidia/OpenMathReasoning)
- [Paper](https://arxiv.org/abs/2504.16891)

We provide [all instructions](https://nvidia.github.io/NeMo-Skills/openmathreasoning1/)
to fully reproduce our results, including data generation.

## Citation

If you find our work useful, please consider citing us!

```bibtex
@article{moshkov2025aimo2,
  title   = {AIMO-2 Winning Solution: Building State-of-the-Art Mathematical Reasoning Models with OpenMathReasoning dataset},
  author  = {Ivan Moshkov and Darragh Hanley and Ivan Sorokin and Shubham Toshniwal and Christof Henkel and Benedikt Schifferer and Wei Du and Igor Gitman},
  year    = {2025},
  journal = {arXiv preprint arXiv:2504.16891}
}
```


## Dataset Owner(s):
NVIDIA Corporation

## Release Date:
04/23/2025

## Data Version
1.0 (04/23/2025)

## License/Terms of Use:
cc-by-4.0

## Intended Usage:
This dataset is intended to be used by the community to continue to improve models. The data may be freely used to train and evaluate.


## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.   

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

