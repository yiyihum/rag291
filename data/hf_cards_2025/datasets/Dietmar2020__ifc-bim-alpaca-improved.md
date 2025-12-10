---
language:
- en
license: apache-2.0
tags:
- ifc
- bim
- architecture
- construction
- alpaca
- instruction-tuning
pretty_name: IFC-BIM Improved Alpaca Dataset
size_categories:
- 10K<n<100K
---

# IFC-BIM Improved Alpaca Dataset

A high-quality instruction-following dataset for Industry Foundation Classes (IFC) and Building Information Modeling (BIM).

## Dataset Description

This dataset contains carefully curated and validated instruction-response pairs about IFC concepts, schemas, and BIM practices. It has been cleaned and improved from an original dataset of 545k+ entries.

### Dataset Quality
- **Quality Score**: 4.6/5.0 (improved from 3.0)
- **LLM Validation**: 95.1% accuracy
- **Total Examples**: ~53k high-quality pairs

### Key Improvements
1. **Removed 478,822 duplicate questions** (88.7% reduction)
2. **Fixed all IFC schema errors** (e.g., IfcRelContainsSpatialStructure → IfcRelContainedInSpatialStructure)
3. **Validated with LLM** for answer quality
4. **Consistent formatting** throughout

## Dataset Structure

The dataset follows the Alpaca format with three fields:
- `instruction`: The question or task description
- `input`: Additional context (usually empty for this dataset)
- `output`: The detailed answer about IFC/BIM concepts

### Example

```json
{
  "instruction": "What is IfcWall and how does it relate to IfcBuildingElement?",
  "input": "",
  "output": "IfcWall is a specific type of IfcBuildingElement that represents vertical constructions..."
}
```

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Dietmar2020/ifc-bim-alpaca-improved")

# Access training split
train_data = dataset['train']

# Example usage
for example in train_data.select(range(5)):
    print(f"Instruction: {example['instruction']}")
    print(f"Output: {example['output'][:100]}...")
    print()
```

## Training Example

```python
# For use with Alpaca-style training
from transformers import AutoTokenizer, AutoModelForCausalLM

def format_alpaca(example):
    if example['input']:
        text = f"### Instruction:\n{example['instruction']}\n\n### Input:\n{example['input']}\n\n### Response:\n{example['output']}"
    else:
        text = f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['output']}"
    return {"text": text}

# Format dataset
formatted_dataset = dataset.map(format_alpaca)
```

## Topics Covered

- IFC entity definitions and relationships
- IFC property sets and attributes
- Spatial structure hierarchy
- Building elements (walls, doors, windows, etc.)
- Material definitions and assignments
- Geometric representations
- IFC schema concepts
- BIM workflows and best practices

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{ifc_bim_alpaca_improved_2024,
  title={IFC-BIM Improved Alpaca Dataset},
  author={Your Name},
  year={2024},
  publisher={Hugging Face}
}
```

## License

Apache 2.0 - Feel free to use for research and commercial purposes.

## Acknowledgments

This dataset was created by cleaning and improving a larger corpus of IFC/BIM documentation using advanced deduplication and validation techniques.
