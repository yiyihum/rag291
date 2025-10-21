---
language:
- en
license: apache-2.0
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- feature-extraction
pretty_name: Extract-0 Document Information Extraction Dataset
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: reference_text
    dtype: string
  splits:
  - name: train
    num_bytes: 422354810
    num_examples: 280128
  download_size: 422354810
  dataset_size: 422354810
configs:
- config_name: default
  data_files:
  - split: train
    path: train.csv
tags:
- document-extraction
- information-extraction
- structured-generation
- synthetic
- json-extraction
---

# Extract-0 Document Information Extraction Dataset

![Extract-0](extract-zero.png)

This dataset contains 280,128 synthetic training examples for document information extraction, used to train Extract-0, a specialized 7B parameter language model that outperforms GPT-4 and other larger models on extraction tasks.

## Dataset Description

The Extract-0 dataset represents a comprehensive collection of document extraction examples generated from diverse sources including arXiv papers, PubMed Central articles, Wikipedia content, and FDA regulatory documents. Each example pairs a document chunk with a schema-based extraction task and its corresponding structured output.

### Dataset Statistics
- **Total extraction examples**: 280,128
- **Source documents**: 34,761 text chunks
- **Document sources**: arXiv, PubMed Central, Wikipedia, FDA databases
- **Average tokens per example**: 532-1900 tokens
- **Schema types**: Varied (objects, arrays, strings, dates, numbers)

## Files

- `train.csv`: Training examples with input schemas, expected outputs, and reference text IDs
- `documents.csv`: Source document chunks used for generating extraction examples

## Dataset Structure

### train.csv
Each row contains:
- `input`: JSON schema defining the extraction requirements
- `output`: Expected extraction result in JSON format
- `reference_text`: ID linking to the source document chunk

### documents.csv
Each row contains:
- `chunk_id`: Unique identifier for the document chunk
- `text`: Raw text content (up to 2000 characters per chunk)

## Model Performance

Extract-0, trained with part of this dataset, achieves:
- **Mean reward**: 0.573 (vs GPT-4: 0.457)
- **JSON validity**: 89.0%

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("HenriqueGodoy/extract-0")

train_data = dataset["train"]
```

## Example

```python
{
  "input": "{\"title\": {\"type\": \"string\", \"extraction_instruction\": \"Extract the full paper title exactly as it appears.\"}}",
  "output": "{\"title\": \"Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models\"}",
  "reference_text": "5_0"
}
```

## Methodology

The dataset was created using a memory-preserving synthetic data generation pipeline that:

1. **Document Processing**: Documents are chunked into 2000-character segments with 200-character overlap
2. **Sequential Extraction**: Chunks processed sequentially to maintain context consistency
3. **Augmentation**: Multi-field combinations generated with controlled token counts
4. **Validation**: All examples validated for JSON compliance and schema adherence

The generation process employs a mathematical formulation where for document chunks {c₁, c₂, ..., cₙ}, the extraction function E operates sequentially: E(cᵢ) = f(cᵢ, Mᵢ₋₁), maintaining accumulated memory M across chunks.

## Training Configuration

Models trained on this dataset used:
- **Base model**: DeepSeek-R1-Distill-Qwen-7B
- **Fine-tuning**: LoRA (rank=16, α=32) modifying 0.53% of parameters
- **Learning rate**: 1e-4 (SFT), 5e-5 (GRPO)
- **Batch size**: 16 (SFT), 64 effective (GRPO)
- **Max sequence length**: 2048 tokens

## Citation

If you use this dataset, please cite:

```bibtex
@misc{godoy2025extract0specializedlanguagemodel,
      title={Extract-0: A Specialized Language Model for Document Information Extraction}, 
      author={Henrique Godoy},
      year={2025},
      eprint={2509.22906},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.22906}, 
}
```

## License

Apache-2.0

## Contact

For questions or issues with the dataset, please open an issue in this repository.
