---
language:
- en
pretty_name: HCC ICD-CM Instruction Tuning Dataset
tags:
- medical
- healthcare
- icd-cm
- code-extraction
- instruction-tuning
- nlp
license: apache-2.0
task_categories:
- text-generation
annotations_creators:
- human-annotated
- programmatically-created
---
# HCC ICD-CM Instruction Tuning Dataset

## Dataset Description

The `ICD10CM_HCC` dataset is specifically designed for **instruction tuning of large language models (LLMs)** for the task of **ICD-CM code extraction** including the **MEAT justification** from discharge summary. This dataset aims to provide high-quality, instruction-formatted examples to guide LLMs in accurately identifying and extracting relevant ICD-10-CM (International Classification of Diseases, Tenth Revision, Clinical Modification) codes from clinical notes, discharge summary.

The primary goal of this dataset is to facilitate the development of LLMs that can understand natural language instructions related to medical coding and produce the correct ICD-CM codes, which are crucial for healthcare billing, statistics, and epidemiological studies.

## Dataset Structure

### Data Fields:
The dataset is structured to be compatible with instruction-tuning paradigms, typically containing the following fields for each example:

* `instruction`: (instructions - string) Natural language instructions, for extraction task of icd10cm, and its MEAT justification.
* `input`: (string) The medical text (discharge summaries) from which the ICD-CM codes are to be extracted.
* `output`: (json) The expected output in json.


### Data Splits:
| split         | data  |
|---------------|------:|
| train         | 9960  |

### Total Prompt Length:

mean: 21625.739457831325, std: 8985.9238278459

### Prompt Template:
```Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n### Instruction:{}\n### Input:{}\n### Response:{}```

# How to Use
You can easily load the icd10cm_hcc_fragmented dataset using the Hugging Face datasets library:

```Python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("ParamDev/ICD10CM_HCC", split = "train")

# Example of accessing a data point
print(dataset[0])
```

If you use the hcc_composite_fixed dataset in your research or project, please cite it appropriately.
Code snippet
```Citation
@misc{ICD10CM_HCC, 
  author = {ParamDev},
  title = {HCC ICD-CM Instruction Tuning Dataset},
  year = {2025},
  publisher = {Hugging Face},
  url = {[https://huggingface.co/datasets/ParamDev/ICD10CM_HCC](https://huggingface.co/datasets/ParamDev/ICD10CM_HCC)}
}
```