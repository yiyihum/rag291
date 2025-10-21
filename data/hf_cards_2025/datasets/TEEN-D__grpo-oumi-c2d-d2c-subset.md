---
language:
- en
license:
- cc-by-nc-4.0
library_name: datasets
tags:
- text-generation
- claim-verification
- instruction-tuning
- grpo
- anli
- synthetic-data
size_categories:
- 1K<n<10K
task_categories:
- text-generation
---

# Dataset Card for GRPO Oumi ANLI Subset

## Dataset 

This dataset is a reformatted version of the `oumi-ai/oumi-c2d-d2c-subset` dataset, specifically structured for use with the GRPO trainer. 
You can find more detailed information about the original dataset at the provided link.

Link: https://huggingface.co/datasets/oumi-ai/oumi-c2d-d2c-subset


## Dataset Structure

The dataset consists of a list of dictionaries, where each dictionary represents a single data instance with a `prompt` and a `completion` field.

**Data Fields:**

* `prompt`: A string containing the context documents (split into sentences with `<|sN|>` tags) and the user's request, enclosed in specific tokens (`<|context|>...</end||context>`, `<|request|>...</end||request>`).
* `completion`: A string containing the model's expected response, including the claim(s) (`<|rN|>...</end||r>`), subclaims (`<|subclaims|>...</end||subclaims>`), citation markers (`<|cite|>...</end||cite>`), explanations (`<|explain|>...</end||explain>`), and support status (`<|supported|>` or `<|unsupported|>`).

**Data Instance Example:**

```json
{
  "prompt": "<|context|><|s1|><Salad Days: \"A Decade of Punk in Washington, DC (1980-90)\" is a documentary written and directed by Scott Crawford.><end||s><|s2|><Released on December 19, 2014, the Kickstarter-funded film features early pioneers of the Washington, DC hardcore punk music scene over a decade (1980-1990) including Minor Threat, Fugazi, Bad Brains, Government Issue, Youth Brigade, Teen Idles, Rites of Spring, and others.><end||s><end||context><|request|><Make one or more claims about information in the documents.><end||request><|response|><|r1|><Decade of Punk was Crawford's first film><end||r><end||response>",
  "completion": "<|r1|><Decade of Punk was Crawford's first film><|subclaims|><Scott Crawford directed Decade of Punk.><Decade of Punk was the first film Scott Crawford directed.><end||subclaims><|cite|><|s1|><end||cite><|explain|><While the document mentions Scott Crawford as the writer and director of the documentary, it does not provide information about whether this was his first film.><end||explain><|unsupported|><end||r>"
}
```

## Citation Information:

If you use this GRPO dataset, please cite both this version and the original Oumi dataset:
```
@misc{grpoOumiANLISubset_TeenDifferent_2025,
  author = {Tarun Reddi and Teen Different},
  title = {GRPO Oumi ANLI Subset},
  month = {April},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/TEEN-D/grpo-oumi-anli-subset}
}

@misc{oumiC2DAndD2CSubset,
  author = {Jeremiah Greer},
  title = {Oumi C2D and D2C Subset},
  month = {March},
  year = {2025},
  url = {https://huggingface.co/datasets/oumi-ai/oumi-c2d-d2c-subset}
}

@software{oumi2025,
  author = {Oumi Community},
  title = {Oumi: an Open, End-to-end Platform for Building Large Foundation Models},
  month = {January},
  year = {2025},
  url = {https://github.com/oumi-ai/oumi}
}

```