---
license: cc-by-4.0
pretty_name: OpenCodeInstruct
dataset_info:
- config_name: train
  features:
  - name: id
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: domain
    dtype: string
  - name: generation_algorithm
    dtype: string
  - name: llm_judgement
    dtype: string
  - name: unit_tests
    dtype: string
  - name: tests_execution_status
    dtype: string
  - name: average_test_score
    dtype: string
  splits:
  - name: train
    num_bytes: 19066895906
    num_examples: 5000000
  download_size: 6861113102
  dataset_size: 19066895906
configs:
- config_name: train
  data_files:
  - split: train
    path: data/train-*
language:
- en
task_categories:
- text-generation
tags:
- code
- synthetic
size_categories:
- 1M<n<5M
---
# OpenCodeInstruct: A Large-scale Instruction Tuning Dataset for Code LLMs


## Dataset Description

We introduce OpenCodeInstruct, the largest open-access instruction tuning dataset, comprising 5 million diverse samples. OpenCodeInstruct is designed for supervised fine-tuning (SFT).

- [Technical Report](https://arxiv.org/abs/2504.04030) - Discover the methodology and technical details behind OpenCodeInstruct.
- [Github Repo](https://github.com/NVIDIA/NeMo-Skills) - Access the complete pipeline used to perform SFT.

This dataset is ready for commercial/non-commercial use.


## Dataset Owner(s)
NVIDIA Corporation


## Dataset Creation Date
January 2025 - March 2025


## License/Terms of Use

GOVERNING TERMS: This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0) available at https://creativecommons.org/licenses/by/4.0/legalcode.

**Data Developer:** NVIDIA

### Use Case: <br>
Developers training LLMs to specialize LLMs in code generation. <br>

### Release Date:  <br>
04/28/2025 <br>


## Intended Usage

The OpenCodeInstruct Dataset is intended to be used by the community to continue to improve open models. The data may be freely used to train models. **However, for 
each dataset a user elects to use, the user is responsible for checking if the dataset license is fit for the intended purpose**.


## Dataset Characterization

** Data Collection Method<br>
* [Hybrid: Automated, Synthetic] <br>

** Labeling Method<be>
* [Hybrid: Automated, Synthetic] <br>


## Dataset Format
|Field|Type|Description|
|:---|:---|:---|
|id|string|A unique id for each question|
|input|string|The input coding question.|
|output|string|LLM's response.|
|domain|string|Either "generic" or "algorithmic".|
|generation_algorithm|string|Either "self-instruct" or "evol-instruct".|
|llm_judgement|string|string representation of a JSON dictionary containing the LLM's evaluation of the response based on several criteria.|
|unit_tests|string|string representation of a list of assertion statements.|
|tests_execution_status|string|string representation of a list of strings indicating "pass" or "fail".|
|average_test_score|float|Fraction of test cases passed.|

## How to Use It

You can load the dataset with the following two lines of code.

```python
from datasets import load_dataset
opencodeinstruct = load_dataset("nvidia/OpenCodeInstruct", split="train")
```


## Dataset Quantification

- Record Count - 5 million coding question-answer pairs.
- Download Size - 6.4 GB


## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).


## Citation

If you find the data useful, please cite:
```
@article{ahmad2025opencodeinstruct,
      title={OpenCodeInstruct: A Large-scale Instruction Tuning Dataset for Code LLMs}, 
      author={Wasi Uddin Ahmad and Aleksander Ficek and Mehrzad Samadi and Jocelyn Huang and Vahid Noroozi and Somshubra Majumdar and Boris Ginsburg},
      year={2025},
      eprint={2504.04030},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.04030}, 
}
```
