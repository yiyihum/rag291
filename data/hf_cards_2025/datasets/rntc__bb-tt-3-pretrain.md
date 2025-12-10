---
license: mit
language:
- fr
size_categories:
- 1M<n<10M
task_categories:
- text-classification
- text-regression
tags:
- medical
- french
- biomedical
- clinical
- annotations
- pretraining
pretty_name: Biomed-FR-v3 High-Quality Pretraining Dataset
---

# Biomed-FR-v3 High-Quality Pretraining Dataset

This dataset contains French biomedical text annotated with **20 different classification and regression tasks** using the `rntc/biomed-fr-v2-classifier` model.

## Dataset Summary

- **Total samples**: 2,782,686
- **Total columns**: 41
- **Annotation tasks**: 25
- **Language**: French
- **Domain**: Biomedical/Clinical
- **Filter criteria**: Filtered for pretraining_suitable >= 0.0 (94.6% of data)

## Key Features

- ✅ **Complete annotation coverage**: All 20 tasks from biomed-fr-v2-classifier
- ✅ **Includes `rewriting_needed`**: Critical regression task for content quality
- ✅ **Quality metrics**: Educational scores, terminology precision, content richness
- ✅ **Clinical focus**: Medical subfield classification, clinical case detection
- ✅ **Proper column order**: Original educational_score preserved (1-5 scale)

## Annotation Tasks

### Regression Tasks (15)
- `rewriting_needed`: Content rewriting necessity score
- `contains_bias`: Bias detection score
- `writing_quality`: Text quality assessment
- `terminology_precision`: Medical terminology accuracy
- `content_richness`: Information density score
- Plus others: age_group, assertion_type, certainty_level, etc.

### Classification Tasks (5)
- `medical_subfield`: 45 medical specialties
- `content_type`: 9 content categories
- `writing_style`: 5 writing styles
- `text_type`: meaningful vs incomplete
- `interactive_elements`: 4 interaction types

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("rntc/bb-tt-3-pretrain")

# Access key annotations
texts = dataset["train"]["text"]
rewriting_scores = dataset["train"]["rewriting_needed"]
educational_scores = dataset["train"]["educational_score"]  # Original 1-5 scale
medical_fields = dataset["train"]["medical_subfield"]
```

## Data Quality

- All samples processed with consistent batch processing
- Original educational_score preserved (0.58-5.10 scale)
- Regression outputs clearly separated (e.g., educational_score_predicted)
- Dimension mismatches handled for classification tasks
- Complete 20-task coverage including previously missing regression tasks

## Model Information

Annotations generated using:
- **Model**: `rntc/biomed-fr-v2-classifier`
- **Base model**: `almanach/camembertv2-base`
- **Tasks**: 20 multi-task classification and regression heads
- **Key fix**: Restored original educational_score column

## Citation

```bibtex
@dataset{biomed_fr_v3_annotated,
  title={Biomed-FR-v3 High-Quality Pretraining Dataset},
  author={RNTC Research Team},
  year={2024},
  url={https://huggingface.co/datasets/rntc/bb-tt-3-pretrain},
  note={French biomedical corpus with complete 20-task annotations}
}
```

## License

MIT License - see LICENSE file for details.

## Related Datasets

- **Full dataset**: `rntc/bb-tt-3`

- **High quality subset**: `rntc/bb-tt-3-s3`, `rntc/bb-tt-3-s4`
