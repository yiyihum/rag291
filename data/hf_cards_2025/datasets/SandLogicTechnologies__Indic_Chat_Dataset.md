---
task_categories:
- text-generation
- translation
language:
- hi
- kn
- te
- ta
- mr
- ml
- gu
- bn
- or
- pa
- as
- si
- ur
tags:
- multilingual
- indic-languages
- mixture-of-experts
- instruction-tuning
- conversational
- translation
pretty_name: IndicMoE Multilingual Dataset
size_categories:
- 100M<n<1B
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: bengali
    num_bytes: 1196018916
    num_examples: 1816124
  - name: gujrathi
    num_bytes: 3039247538
    num_examples: 2943139
  - name: hindi
    num_bytes: 4986383413
    num_examples: 4632910
  - name: kannada
    num_bytes: 3891546404
    num_examples: 3542319
  - name: malayalam
    num_bytes: 3450221419
    num_examples: 2812335
  - name: marathi
    num_bytes: 3460895138
    num_examples: 3790978
  - name: odia
    num_bytes: 282620427
    num_examples: 437511
  - name: punjabi
    num_bytes: 641417623
    num_examples: 1209859
  - name: sinhala
    num_bytes: 109512191
    num_examples: 64181
  - name: tamil
    num_bytes: 4039782997
    num_examples: 3864105
  - name: telugu
    num_bytes: 4008954500
    num_examples: 3717946
  - name: urdu
    num_bytes: 64010825
    num_examples: 58034
  - name: assamese
    num_bytes: 117897307
    num_examples: 184621
  download_size: 10101776703
  dataset_size: 29288508698
configs:
- config_name: default
  data_files:
  - split: bengali
    path: data/bengali-*
  - split: gujrathi
    path: data/gujrathi-*
  - split: hindi
    path: data/hindi-*
  - split: kannada
    path: data/kannada-*
  - split: malayalam
    path: data/malayalam-*
  - split: marathi
    path: data/marathi-*
  - split: odia
    path: data/odia-*
  - split: punjabi
    path: data/punjabi-*
  - split: sinhala
    path: data/sinhala-*
  - split: tamil
    path: data/tamil-*
  - split: telugu
    path: data/telugu-*
  - split: urdu
    path: data/urdu-*
  - split: assamese
    path: data/assamese-*
---

# Large Scale Multilingual Indic Dataset for Finetuning

<!-- Provide a quick summary of the dataset. -->

The Multilingual Indic Dataset is a large-scale corpus spanning 13 Indian languages, curated specifically for finetuning large language models (LLMs) on Indic languages.
In total, over 561 million samples were aggregated from 53 open-source datasets available on Hugging Face, covering domains such as general text, translation corpora, instruction-based data, conversational resources, and mixed-domain datasets.

Through a rigorous filtering and curation pipeline, this collection was distilled into a final high-quality dataset of ~29 million samples across 13 Indic languages.
As one of the largest curated Indic multilingual datasets available, it is designed to significantly enhance the performance of LLMs in natural language understanding (NLU) and natural language generation (NLG) tasks, supporting applications such as instruction tuning, dialogue modeling, translation, and multilingual finetuning.

## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->



- **Curated by:** SandLogic Technologies Pvt. Ltd.[Website](https://www.sandlogic.com/).
- **Language(s):** 13 Indic languages (Hindi, Kannada, Telugu, Tamil, Marathi, Malayalam, Gujarati, Bengali, Odia, Punjabi, Assamese, Sinhala, Urdu).
- **Size of Original Collection:** ~561M samples from 53 Hugging Face datasets
- **Final Curated Dataset Size:** ~29M high-quality samples after filtering and curation.
- **License:** Open Source



## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->
You can load and use the dataset in Python as follows:  

```python
from datasets import load_dataset

# Load the dataset (example: Hindi split)
dataset = load_dataset("SandLogicTechnologies/Indic_Chat_Dataset", split="hindi")

# Inspect one example
print(dataset[0])
```



## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
The dataset has been standardized into the UltraChat-200k Instruction Schema, a JSON-based format designed for instruction tuning and dialogue modeling.
Each record is structured as a multi-turn conversation with the following fields:

from: Specifies the role of the speaker ("user" or "assistant")

value: Contains the actual utterance (instruction, question, response, etc.)

```sh
[
  {
    "from": "user",
    "value": "Translate the following sentence into Hindi: 'How are you?'"
  },
  {
    "from": "assistant",
    "value": "आप कैसे हैं?"
  }
]
```


## Dataset Creation

The **Multilingual Indic Dataset** was curated to address the scarcity of large, high-quality resources for **finetuning large language models (LLMs) on Indian languages**.  

We aggregated **53 open-source datasets from Hugging Face**, covering multiple domains such as:  
- General text corpora  
- Translation datasets  
- Instruction-based datasets  
- Conversational/dialogue resources  
- Code-related corpora  

### A multi-stage **processing pipeline** was applied:

1. **Manual Filtering** – Removed irrelevant, noisy, or malformed subsets.  
2. **Deduplication** – Eliminated exact and near-duplicate entries.  
3. **Language Identification** – Ensured only rows in target Indic languages were retained.  
4. **Minimum Length Filtering** – Discarded trivial or incomplete rows.  
5. **Format Normalization** – Standardized punctuation, whitespace, Unicode, and removed extraneous symbols.  
6. **Schema Conversion** – Converted instruction and dialogue corpora into the **UltraChat-200k Instruction Schema**.  

### Final Collected Dataset (~561M Samples) 
After aggregation from **53 Hugging Face datasets**, the collected dataset distribution across 13 Indic languages is illustrated below:  

**Collected Dataset Pie Chart**
<p align="left">
  <img src="https://raw.githubusercontent.com/sandlogic/SandLogic-Lexicons/main/Images/collected_data_v2.png" width="40%"/>
</p>


## Final Curated Dataset (~29M Samples)  
After rigorous filtering and cleaning, the final curated dataset distribution across languages was:  

| **Language** | **Total High-Quality Rows** |  
|--------------|------------------------------|  
| Hindi        | 4.63M |  
| Kannada      | 3.54M |  
| Telugu       | 3.72M |  
| Tamil        | 3.86M |  
| Marathi      | 3.79M |  
| Malayalam    | 2.81M |  
| Gujarati     | 2.94M |  
| Bengali      | 1.82M |  
| Odia         | 438K  |  
| Punjabi      | 1.21M |  
| Assamese     | 185K  |  
| Sinhala      | 64K   |  
| Urdu         | 58K   |  

### Language Distribution in Curated Training Dataset  

**Curated Dataset Pie Chart**
<p align="left">
  <img src="https://raw.githubusercontent.com/sandlogic/SandLogic-Lexicons/main/Images/Training_data_v2.png" width="40%"/>
</p>

## Acknowledgements  

This dataset was curated from **53 source datasets**.  
We thank the authors and organizations who created these resources.  
The complete list of citations is available [here](https://github.com/sandlogic/SandLogic-Lexicons/blob/main/Images/dataset_citation.md).


