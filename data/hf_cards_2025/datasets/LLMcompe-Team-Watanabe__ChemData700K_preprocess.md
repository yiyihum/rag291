---
annotations_creators:
- found
language_creators:
- found
language:
- en
license:
- mit
multilinguality:
- monolingual
pretty_name: ChemData700K Preprocessed
homepage: https://huggingface.co/datasets/AI4Chem/ChemData700K
tags:
- chemistry
- instruction-tuning
task_categories:
- text-generation
task_ids:
- chemical-property-prediction
---

# ChemData700K Preprocessed Dataset

This dataset is a preprocessed version of the [AI4Chem/ChemData700K](https://huggingface.co/datasets/AI4Chem/ChemData700K) dataset.

## Preprocessing Steps

1. **Filtering**: The dataset was filtered to include only samples that are not part of a conversation and have no top-level instruction. Specifically, only rows where `history` is empty (`[]`) and `instruction` is null/empty were kept.
2. **Formatting**: The `output` column was prefixed with `#### `.
3. **Column Renaming**: The `input` and `output` columns were renamed to `question` and `answer` respectively for standardization.
4. **Column Pruning**: All other columns (`history`, `instruction`, `id`) were removed.

## Data Structure

- `question`: The original `input` data.
- `answer`: The original `output` data, prefixed with `#### `.

## Data Splits

The `train` split was filtered, resulting in the following size:

- **Train**: 373928 (from an original size of ~700,000)

## How to Use

```python
from datasets import load_dataset

ds = load_dataset("daichira/ChemData700K_preprocess", split="train")
print(ds[0])
```

## Original Dataset

For more information, please refer to the original dataset card at [AI4Chem/ChemData700K](https://huggingface.co/datasets/AI4Chem/ChemData700K).
