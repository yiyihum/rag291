---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- en
---

## GeoRAG-QA: A Benchmark Test Set for Geoscience Information Retrieval

### 1. Dataset Description

We introduce **GeoRAG-QA**, a curated test set designed for evaluating retrieval-augmented generation (RAG) systems and information retrieval approaches in the geoscience domain.

GeoRAG-QA was constructed using the Test Set Generation module from [RAGAS (Es et al., 2023)](https://arxiv.org/pdf/2309.15217). The dataset consists of automatically generated QA items based on open-access geoscience publications (see [GeoGPT Training Data from Open Access Papers](https://github.com/GeoGPT-Research-Project/GeoGPT/blob/main/GeoGPT%20Training%20Data%20from%20Open%20Access%20Papers.md) for reference), licensed under CC BY or CC BY-NC. During the generation process, some QA items were incomplete or invalid. After manual review, these flawed entries were removed, yielding a final set of **938** high-quality QA items. The dataset is organized into four categories:

- 250 single-document fact-based QA pairs
- 250 single-document inference QA pairs
- 188 multi-document QA pairs
- 250 conditional QA pairs

In cases where the generated reference answer was incorrectly labeled as “The answer to the given question is not present in the context”, we re-generated the reference answers using GPT-4o to improve accuracy, consistency, and evaluation reliability.

For more details regarding dataset construction and methodology, please refer to the [technical report](https://github.com/GeoGPT-Research-Project/GeoGPT-RAG/blob/master/GeoGPT_RAG_Technical_Report.pdf).

### 2. How to download

#### Using 🤗`datasets`

```python
import datasets

data=datasets.load_dataset('GeoGPT-Research-Project/GeoRAG-QA')
```

### 3. License and Intended Uses

**License**：GeoRAG-QA is released under the Creative Commons Attribution-NonCommercial (CC BY-NC) license.

**Copyright**: Copyright (c) 2025 Zhejiang Lab. All rights reserved.

**Intended Use**：The dataset is intended for non-commercial research and educational purposes, particularly for:

- Evaluating retrieval and RAG pipelines in geoscience,
- Supporting the development of domain-specific benchmarks,
- Advancing methods for QA and information access in scientific domains.

It must not be used for commercial purposes, activities that violate laws or regulations, or in any manner inconsistent with the license terms.

## 4. Contact
For questions, feedback, or contributions, please open an issue in this repository or contact us at 📧 [support.geogpt@zhejianglab.org](support.geogpt@zhejianglab.org).