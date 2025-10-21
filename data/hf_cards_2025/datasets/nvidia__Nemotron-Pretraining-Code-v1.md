---
license: other
task_categories:
- text-generation
extra_gated_prompt: 'By clicking “Agree” I confirm I have read and agree to NVIDIA
  Data Agreement for Model Training and agree that I intend to use this data for model
  training purposes only. (https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md) '
extra_gated_fields:
  Company: text
  Institutional Email: text
  I agree to use this dataset for model training purposes ONLY: checkbox
configs:
- config_name: Synthetic-Code
  data_files:
  - path: Synthetic-Code/*.parquet
    split: train
- config_name: Nemotron-Code-Metadata
  data_files:
  - path: Nemotron-Code-Metadata/*.parquet
    split: train
track_downloads: true
---
# Nemotron-Pre-Training-Dataset-v1 Release

## Data Overview

This pretraining dataset, for generative AI model training, preserves high-value math and code while enriching it with diverse multilingual Q&A, fueling the next generation of intelligent, globally-capable models.


This dataset supports [NVIDIA Nemotron Nano 2](https://huggingface.co/collections/nvidia/nvidia-nemotron-689f6d6e6ead8e77dd641615),  a family of large language models (LLMs) that consists of the [NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2), [NVIDIA-Nemotron-Nano-9B-v2-Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2), and [NVIDIA-Nemotron-Nano-12B-v2-Base](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base) models. They are successors of [Nemotron-H-8B-Base-8K](https://huggingface.co/nvidia/Nemotron-H-8B-Base-8K) and [Nemotron-H-8B-Reasoning-128K](https://huggingface.co/nvidia/Nemotron-H-8B-Reasoning-128K), created with commercial use in mind.
The NVIDIA-Nemotron-Nano-9B-v2 model is aligned for human chat preferences and tasks. All of the NVIDIA Nemotron Nano 2 models support a context length of 128K tokens.

Our dataset comes in 4 main categories:
- [nvidia/Nemotron-Pretraining-Dataset-sample](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample)
  - This dataset includes a small sampled version for inspection and quick experimentation, with 10 representative subsets drawn from different components of the full SFT and pretraining corpora. These include diverse QA data (original and translated), high-quality and synthetic high-quality Common Crawl extractions, math-focused subsets, code metadata, and SFT-style data across code, math, and general domains, as well as synthetic code.
- [nvidia/Nemotron-CC-Math-v1](https://huggingface.co/datasets/nvidia/Nemotron-CC-Math-v1)
  - 133B-token high-quality math pretraining dataset from Common Crawl built with a novel Lynx + LLM pipeline that preserves equations and code, standardizes to LaTeX, and removes noise, beating all previous math pretraining datasets on math and improves on code, and reasoning benchmarks. We also regenerated the Nemotron-MIND dataset using Nemotron-cc-math-4plus, our high-quality subset which yielded consistent gains over previous nemotron-MIND.
- [nvidia/Nemotron-CC-v2](https://huggingface.co/datasets/nvidia/Nemotron-CC-v2)
  - Updated English web crawl dataset based on Nemotron-CC with eight additional Common Crawl snapshots (2024–2025), synthetic rephrasing using Qwen3-30B-A3B, filtered for English and globally deduplicated. Includes synthetic data generated with five different prompts. The synthetic Diverse QA data has also been translated into 15 languages.
- [nvidia/Nemotron-Pretraining-Code-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Code-v1)
  - Large-scale curated source code dataset from GitHub, processed through multi-stage filtering including license-based removal (BigCode-inspired, with a stricter license set), exact and fuzzy deduplication, and heuristic quality filters from OpenCoder. All files are annotated with metadata to guide filtering and improve dataset quality. Additionally, we generate large-scale code question–answer data in 11 programming languages by prompting LLMs on curated code snippets, solving the generated problems, and filtering results for correctness, producing diverse natural language–code pairs for pretraining.
- [nvidia/Nemotron-Pretraining-SFT-v1](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-SFT-v1)
  - Diverse synthetically generated and curated SFT-style dataset spanning STEM, multilingual, academic, and reasoning domains. STEM data was expanded from high-quality math and science seeds using multi-iteration generation with Qwen3 and DeepSeek models, producing varied, harder, and multiple-choice questions with solutions. Academic QA pairs were synthesized from complex undergraduate- and graduate-level texts. Additional SFT-style data covers code, math, MMLU-style general QA, and fundamental reasoning tasks, with billions of tokens generated using DeepSeek-V3 and Qwen3 for logical, analytical, and reading comprehension questions.

## Data distribution

The total data category distribution are as follows:

| Dataset Category | Tokens Count (B) |
|------------------|------------------|
| English Common Crawl | 3359.8 |
| English Synthetic CC | 1257.3 |
| Diverse QA | 692.9 |
| Translated Diverse QA | 558.2 |
| Math | 206.2 |
| Math SFT | 190.6 |
| Synthetic Code | 174.9 |
| MMLU SFT | 81.6 |
| Code SFT | 58.5 |
| General SFT | 5.7 |
| **TOTAL** | **6585.8** |

Additionally, we release metadata to reproduce a 747.4B token curated code dataset.

## Filtering the data

Users can download subsets of the data based on the metadata schema described above. Example script for downloading code and math as follows:
```
from datasets import load_dataset
ds = load_dataset("nvidia/Nemotron-CC-Math-v1", "4plus", streaming=True)
```

Models that were used in the creation of this dataset per category are as follows:

**nvidia/Nemotron-Pretraining-Code-v1**

| Model | Token Count (B) |
|-------|-----------------|
| [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) | 174.9 |

## License/Terms of Use
[NVIDIA Open Data License Agreement](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Dataset-sample/raw/main/LICENSE.md)

NVIDIA respects the rights of all content creators and our NVIDIA Data Agreement for Model Training is written to be fully compliant with the letter and the spirit of copyright law. Copyright law protects particular expressions, but not facts, ideas, data, or information. Anyone is free to learn facts, ideas, data, or information from another source and use it to make their own expressions. Fair use also protects the ability to use a work for a transformative purpose, such as model training. The Agreement is designed to limit use to those uses protected as fair uses, such as model training.

The NVIDIA Data Access Agreement for Model Training enables training of any AI model, including models released under proprietary or open source licenses.

This dataset contains synthetic data created using the following models:

DeepSeek-R1, DeepSeek-R1-0528, DeepSeek-R1-Distill-Qwen-32B, DeepSeek-V3, DeepSeek-V3-0324, Mistral-Nemo-12B-Instruct, Mixtral 8x22B, Mixtral-8x22B-v0.1, Nemotron-4-340B-Instruct, Qwen2.5-32B-Instruct, Qwen2.5-72B-Instruct, Qwen-2.5-7B-Math-Instruct, Qwen2.5-0.5B-instruct, Qwen2.5-32B-Instruct, Qwen2.5-72B-Instruct, Qwen2.5-Coder-32B-Instruct, Qwen2.5-Math-72B, Qwen3-235B-A22B, Qwen3-30B-A3B

If this dataset is used to create, train, fine-tune, or otherwise improve an AI model, which is distributed or made available, such AI model may be subject to redistribution and use requirements in the [Qwen License Agreement](https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE) and the [DeepSeek License Agreement](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL).


**Data Developer:** NVIDIA

### Use Case: <br>
Developers training foundation LLM models. <br>

### Release Date:  <br>
8/18/2025 <br>

## Data Version
1.0 (8/18/2025)

## Intended use

The Nemotron Pre-Training Dataset is intended to be used by the community to continue to improve open models. The data may be freely used to train and evaluate with user agreement to open data license.


## Ethical Considerations:

NVIDIA maintains policies and procedures to ensure compliance with laws governing confidential information, PII, and copyright materials. If, when reviewing or using this dataset, you identify issues such as those listed above, please contact nemotron-data@nvidia.com

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Data Opt-Out:
NVIDIA has undertaken legal review to ensure there is no confidential, PII or copyright materials.  If, when reviewing or using this dataset, you identify issues with the data itself, such as those listed above, please contact nemotron-data@nvidia.com.


## Citation & Acknowledgment

If you use our dataset in your research, please cite our [NVIDIA Nemotron Nano 2 paper](https://arxiv.org/abs/2508.14444):

```bibtex
@misc{nvidia2025nvidianemotronnano2,
      title={NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model}, 
      author={NVIDIA and : and Aarti Basant and Abhijit Khairnar and Abhijit Paithankar and Abhinav Khattar and Adithya Renduchintala and Aditya Malte and Akhiad Bercovich and Akshay Hazare and Alejandra Rico and Aleksander Ficek and Alex Kondratenko and Alex Shaposhnikov and Alexander Bukharin and Ali Taghibakhshi and Amelia Barton and Ameya Sunil Mahabaleshwarkar and Amy Shen and Andrew Tao and Ann Guan and Anna Shors and Anubhav Mandarwal and Arham Mehta and Arun Venkatesan and Ashton Sharabiani and Ashwath Aithal and Ashwin Poojary and Ayush Dattagupta and Balaram Buddharaju and Banghua Zhu and Barnaby Simkin and Bilal Kartal and Bita Darvish Rouhani and Bobby Chen and Boris Ginsburg and Brandon Norick and Brian Yu and Bryan Catanzaro and Charles Wang and Charlie Truong and Chetan Mungekar and Chintan Patel and Chris Alexiuk and Christian Munley and Christopher Parisien and Dan Su and Daniel Afrimi and Daniel Korzekwa and Daniel Rohrer and Daria Gitman and David Mosallanezhad and Deepak Narayanan and Dima Rekesh and Dina Yared and Dmytro Pykhtar and Dong Ahn and Duncan Riach and Eileen Long and Elliott Ning and Eric Chung and Erick Galinkin and Evelina Bakhturina and Gargi Prasad and Gerald Shen and Haifeng Qian and Haim Elisha and Harsh Sharma and Hayley Ross and Helen Ngo and Herman Sahota and Hexin Wang and Hoo Chang Shin and Hua Huang and Iain Cunningham and Igor Gitman and Ivan Moshkov and Jaehun Jung and Jan Kautz and Jane Polak Scowcroft and Jared Casper and Jian Zhang and Jiaqi Zeng and Jimmy Zhang and Jinze Xue and Jocelyn Huang and Joey Conway and John Kamalu and Jonathan Cohen and Joseph Jennings and Julien Veron Vialard and Junkeun Yi and Jupinder Parmar and Kari Briski and Katherine Cheung and Katherine Luna and Keith Wyss and Keshav Santhanam and Kezhi Kong and Krzysztof Pawelec and Kumar Anik and Kunlun Li and Kushan Ahmadian and Lawrence McAfee and Laya Sleiman and Leon Derczynski and Luis Vega and Maer Rodrigues de Melo and Makesh Narsimhan Sreedhar and Marcin Chochowski and Mark Cai and Markus Kliegl and Marta Stepniewska-Dziubinska and Matvei Novikov and Mehrzad Samadi and Meredith Price and Meriem Boubdir and Michael Boone and Michael Evans and Michal Bien and Michal Zawalski and Miguel Martinez and Mike Chrzanowski and Mohammad Shoeybi and Mostofa Patwary and Namit Dhameja and Nave Assaf and Negar Habibi and Nidhi Bhatia and Nikki Pope and Nima Tajbakhsh and Nirmal Kumar Juluru and Oleg Rybakov and Oleksii Hrinchuk and Oleksii Kuchaiev and Oluwatobi Olabiyi and Pablo Ribalta and Padmavathy Subramanian and Parth Chadha and Pavlo Molchanov and Peter Dykas and Peter Jin and Piotr Bialecki and Piotr Januszewski and Pradeep Thalasta and Prashant Gaikwad and Prasoon Varshney and Pritam Gundecha and Przemek Tredak and Rabeeh Karimi Mahabadi and Rajen Patel and Ran El-Yaniv and Ranjit Rajan and Ria Cheruvu and Rima Shahbazyan and Ritika Borkar and Ritu Gala and Roger Waleffe and Ruoxi Zhang and Russell J. Hewett and Ryan Prenger and Sahil Jain and Samuel Kriman and Sanjeev Satheesh and Saori Kaji and Sarah Yurick and Saurav Muralidharan and Sean Narenthiran and Seonmyeong Bak and Sepehr Sameni and Seungju Han and Shanmugam Ramasamy and Shaona Ghosh and Sharath Turuvekere Sreenivas and Shelby Thomas and Shizhe Diao and Shreya Gopal and Shrimai Prabhumoye and Shubham Toshniwal and Shuoyang Ding and Siddharth Singh and Siddhartha Jain and Somshubra Majumdar and Soumye Singhal and Stefania Alborghetti and Syeda Nahida Akter and Terry Kong and Tim Moon and Tomasz Hliwiak and Tomer Asida and Tony Wang and Tugrul Konuk and Twinkle Vashishth and Tyler Poon and Udi Karpas and Vahid Noroozi and Venkat Srinivasan and Vijay Korthikanti and Vikram Fugro and Vineeth Kalluru and Vitaly Kurin and Vitaly Lavrukhin and Wasi Uddin Ahmad and Wei Du and Wonmin Byeon and Ximing Lu and Xin Dong and Yashaswi Karnati and Yejin Choi and Yian Zhang and Ying Lin and Yonggan Fu and Yoshi Suhara and Zhen Dong and Zhiyu Li and Zhongbo Zhu and Zijia Chen},
      year={2025},
      eprint={2508.14444},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.14444}, 
}
```