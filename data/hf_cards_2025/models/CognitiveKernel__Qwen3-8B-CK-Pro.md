---
license: other
license_name: cognitive-kernel-pro
license_link: https://huggingface.co/CognitiveKernel/Qwen3-8B-CK-Pro/blob/main/LICENSE
base_model:
- Qwen/Qwen3-8B
pipeline_tag: text-generation
library_name: transformers
---


This model was the CK-Pro-8B model mentioned in the paper [Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training](https://huggingface.co/papers/2508.00414).

This model is finetuned using self-collected trajectories from the queries as presented in Table 2 of the paper. 

Qwen-3-8B-CK-Pro achieves a Pass@1/3 score of  32.7%/38.2% on the full dev set of GAIA, and 40.3%/49.3% on the text-only subset of GAIA.