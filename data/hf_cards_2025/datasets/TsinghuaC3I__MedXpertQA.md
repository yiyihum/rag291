---
language:
- en
license: mit
size_categories:
- 1K<n<10K
task_categories:
- table-question-answering
- question-answering
- text-generation
tags:
- medical
- question-answering
- multimodal
- reasoning
- expert-level
configs:
- config_name: MM
  data_files:
  - split: dev
    path: MM/dev.jsonl
  - split: test
    path: MM/test.jsonl
- config_name: Text
  data_files:
  - split: dev
    path: Text/dev.jsonl
  - split: test
    path: Text/test.jsonl
---

# Dataset Card for MedXpertQA

<!-- Provide a quick summary of the dataset. -->

**MedXpertQA** is a highly challenging and comprehensive benchmark designed to evaluate expert-level medical knowledge and advanced reasoning capabilities. It features both text-based and multimodal question-answering tasks, with the multimodal subset leveraging structured clinical information alongside images.

## Dataset Description

**MedXpertQA** comprises 4,460 questions spanning diverse medical specialties, tasks, body systems, and image types. It includes two subsets:

- **MedXpertQA Text:** Focuses on text-based medical question answering.
- **MedXpertQA MM:** Presents multimodal questions incorporating diverse images and rich clinical information (patient records, examination results) structured in a tabular format.

Key features:

- **Challenging Questions:** Collected from expert-level sources and rigorously filtered, augmented, and reviewed.
- **High Clinical Relevance:** Includes specialty board questions for enhanced comprehensiveness. The MM subset introduces a novel level of complexity in multimodal medical benchmarking.
- **Reasoning-Oriented Subset:** Enables assessment of model reasoning abilities beyond simpler question-answering tasks.

For more details, please refer to our [preprint](https://arxiv.org/abs/2501.18362), [GitHub repository](https://github.com/TsinghuaC3I/MedXpertQA), and [project page](https://medxpertqa.github.io).

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

The following is an example from **MedXpertQA MM**:

- `id`: Question ID (e.g., "MM-26").
- `question`: Question text with formatted answer choices.
- `options`: Answer choices (5 for MM, 10 for Text).
- `label`: Correct answer choice (single letter).
- `images`: List of image filenames (MM subset only). Images are provided in `images.zip`.
- `medical_task`: Main medical task (Diagnosis, Treatment, or Basic Medicine).
- `body_system`: Relevant body system.
- `question_type`: Question type (Reasoning or Understanding).

```json
{
    "id": "MM-26",
    "question": "A 70-year-old female patient seeks medical attention with complaints of dizziness and widespread rash that developed over the past week, following a viral respiratory infection. Physical examination reveals a generalized, macular, purplish rash that does not blanch with pressure. What is the most probable diagnosis?
Answer Choices: (A) Erythema infectiosum (B) Cutaneous larva migrans (C) Cold agglutinin disease (D) Cutis marmorata (E) Erythema ab igne",
    "options": {
        "A": "Erythema infectiosum",
        "B": "Cutaneous larva migrans",
        "C": "Cold agglutinin disease",
        "D": "Cutis marmorata",
        "E": "Erythema ab igne"
    },
    "label": "C",
    "images": ["MM-26-a.jpeg"],
    "medical_task": "Diagnosis",
    "body_system": "Lymphatic",
    "question_type": "Reasoning"
}
```

## Dataset Splits

Each subset (Text and MM) contains `dev.jsonl` (development set) and `test.jsonl` (test set).

## Citation

If you find our work helpful, please use the following citation.

```
@article{zuo2025medxpertqa,
  title={MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding},
  author={Zuo, Yuxin and Qu, Shang and Li, Yifei and Chen, Zhangren and Zhu, Xuekai and Hua, Ermo and Zhang, Kaiyan and Ding, Ning and Zhou, Bowen},
  journal={arXiv preprint arXiv:2501.18362},
  year={2025}
}
```