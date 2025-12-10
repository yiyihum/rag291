---
datasets:
- dokiik/MIXTURE
tags:
- instruction-tuning
- data-quality
- mixup
license: mit
language:
- en
task_categories:
- text-generation
pretty_name: MIXTURE
size_categories:
- 100K<n<1M
---

# MIXTURE

**MIXTURE** is a dataset designed for instruction distillation, which aims to transform sparse, incomplete, and low-quality inputs into a single information-dense output.


## Overview

This dataset provides two main components for different stages of model training:

- **data_sft/** — Used for *cold start* supervised fine-tuning (SFT).  


- **data_grpo/** — Used for *GRPO* (Group Relative Policy Optimization) training.  


For more details about data construction, structure, and usage examples, please refer to the [official repository](https://github.com/yuu250/LM-mixup/tree/main).
