---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- en
size_categories:
- 10K<n<100K
---

# Long Health 100k

100k medical/health samples with long context for T5-Gemma 2B inference

## Dataset Details

- **Samples**: 100,032
- **Model**: T5-Gemma 2B (google/t5gemma-2b-2b-prefixlm-it)
- **Format**: JSON with teacher logits for knowledge distillation

## Structure

Each sample contains:
- `encoder_input_ids`: Long context input tokens (~52k tokens avg)
- `decoder_input_ids`: Output sequence tokens (~296 tokens avg)
- `reasoning_mask`: Mask for reasoning tokens
- `teacher_token_ids`: Teacher model's predicted tokens
- `teacher_logits`: Teacher model's logits for distillation
- `teacher_positions`: Position indices for teacher tokens
- `dataset_source`: Source dataset identifier

## Usage

```python
import json
from huggingface_hub import hf_hub_download

# Download the dataset
filepath = hf_hub_download(
    repo_id="agu18dec/longhealth-100k-t5gemma-2b-inference",
    filename="data.json",
    repo_type="dataset"
)

# Load the data
with open(filepath, 'r') as f:
    data = json.load(f)

print(f"Loaded {len(data)} samples")
```

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{longcontext_distillation,
  author = {Your Name},
  title = {Long Health 100k},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/datasets/agu18dec/longhealth-100k-t5gemma-2b-inference}
}
```
