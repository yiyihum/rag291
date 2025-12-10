---
language:
- en
license: cc-by-4.0
size_categories:
- 1M<n<10M
task_categories:
- text-generation
- text2text-generation
pretty_name: Alizee OpenCodeReasoning Phase 3 Conformant - 1.2M Examples
dataset_info:
  features:
  - name: id
    dtype: string
  - name: prompt
    dtype: string
  - name: rationale
    dtype: string
  - name: reference_code
    dtype: string
  - name: tests
    sequence: string
  - name: source
    dtype: string
  - name: meta
    struct:
    - name: difficulty
      dtype: string
    - name: tags
      sequence: string
    - name: license
      dtype: string
configs:
- config_name: sft
  data_files: sft_rationale_lite.jsonl
- config_name: grpo
  data_files: grpo_episodes.jsonl
tags:
- code
- reasoning
- chain-of-thought
- python
- competitive-programming
- code-generation
- instruction-tuning
---

# 🚀 Alizee OpenCodeReasoning Phase 3 Conformant Dataset - 1.2M Examples

## 📊 Dataset Summary

This is a **fully conformant** version of the Phase 3 dataset, processed to strictly follow the specification with clean separation between data and formatting tags. Contains **1.2 million high-quality Python code examples** with synthetic prompts and concise reasoning chains.

### Key Improvements
- ✅ **100% Conformant** to Phase 3 specification
- ✅ **Synthetic prompts** generated from code analysis (no more "-")
- ✅ **Clean data** without formatting tags in fields
- ✅ **Deduplicated** using AST-based hashing
- ✅ **Validated** Python code (100% AST-valid)
- ✅ **Proper separation** between SFT and GRPO formats

## 📁 Dataset Structure

### Files
- `sft_rationale_lite.jsonl` (1.2M records) - For supervised fine-tuning
- `grpo_episodes.jsonl` (1.2M records) - For GRPO/reinforcement learning

### Data Fields

#### SFT Format (Conformant)
```json
{
  "id": "converted::source::hash",
  "prompt": "Clear problem description",
  "rationale": "- Step 1\n- Step 2\n- Step 3",
  "reference_code": "def solution():\n    ...",
  "tests": ["assert solution(x) == y"],
  "source": "OpenCodeReasoning-2-source",
  "meta": {
    "difficulty": "easy|medium|hard",
    "tags": ["algorithm", "data_structure"],
    "license": "cc-by-4.0"
  }
}
```

#### GRPO Format (Conformant)
```json
{
  "id": "converted::source::hash",
  "reference_code": "def solution():\n    ...",
  "tests": ["assert solution(x) == y"],
  "meta": {
    "timeout_sec": 1.0,
    "max_new_tokens": 200
  }
}
```

**Note**: GRPO format does NOT contain a prompt field (generated at runtime).

## 🛠️ Processing Pipeline

### Conformance Fixes Applied
1. **Removed all formatting tags** from data fields
2. **Generated synthetic prompts** using code analysis
3. **Created concise rationales** (3-4 bullet points, ≤40 tokens)
4. **Separated schemas** properly (SFT vs GRPO)
5. **Deduplicated** by AST hash (removed 154k duplicates)
6. **Validated** all Python code with AST parser

### Statistics
```json
{
  "total_processed": 1,369,614,
  "valid_records": 1,215,268,
  "duplicates_removed": 154,344,
  "invalid_code": 2,
  "sft_with_rationale": 1,215,268 (100%)
}
```

## 💻 Usage

### Loading with Datasets Library
```python
from datasets import load_dataset

# Load SFT dataset (with prompts and rationales)
sft_dataset = load_dataset("DUKEAI/Alizee-Phase3-Conformant-1.2M", "sft")

# Load GRPO dataset (for RL, no prompts)
grpo_dataset = load_dataset("DUKEAI/Alizee-Phase3-Conformant-1.2M", "grpo")
```

### Proper Collation for Training

#### SFT Collation
```python
def collate_sft(record):
    # Tags added ONLY during collation, not in data
    if record['rationale']:
        input_text = (f"<|prompt|>{record['prompt']}<|endprompt|>"
                     f"<|rationale|>{record['rationale']}<|endrationale|>"
                     f"<|code|>")
    else:
        input_text = f"<|prompt|>{record['prompt']}<|endprompt|><|code|>"

    target = f"{record['reference_code']}<|endcode|>"
    return input_text, target
```

#### GRPO Generation
```python
def prepare_grpo_prompt():
    # Fixed prompt for GRPO
    return "<|prompt|>-<|endprompt|><|code|>\n"
    # Model generates until <|endcode|>
```

## 🎯 Key Differences from Original

| Aspect | Original (Non-Conformant) | This Version (Conformant) |
|--------|---------------------------|---------------------------|
| **Tags in data** | ❌ Yes (mixed with content) | ✅ No (added at collation) |
| **SFT prompts** | ❌ Empty ("-") | ✅ Synthetic descriptions |
| **Rationales** | ❌ Missing | ✅ Concise bullets |
| **GRPO prompt field** | ❌ Stored | ✅ Not stored |
| **Schema separation** | ❌ Mixed | ✅ Clean separation |
| **Deduplication** | ❌ No | ✅ Yes (AST-based) |
| **Code validation** | ❌ Mixed | ✅ 100% AST-valid |

## 📈 Training Recommendations

### Tokenizer Setup
```python
special_tokens = [
    "<|prompt|>", "<|endprompt|>",
    "<|rationale|>", "<|endrationale|>",
    "<|code|>", "<|endcode|>"
]
tokenizer.add_tokens(special_tokens)
model.resize_token_embeddings(len(tokenizer))
```

### Training Configuration
- **Batch size**: 8-16 (depending on sequence length)
- **Learning rate**: 5e-5 for SFT, 1e-6 for GRPO
- **Max length**: 1024 tokens
- **Gradient accumulation**: 4-8 steps

## ✅ Validation Results

- **Format**: 100% JSON Lines valid
- **Schemas**: 100% conformant
- **Python code**: 100% AST-valid
- **No formatting tags** in data fields
- **Clean separation** between SFT and GRPO

## 📜 License

This dataset is released under **CC-BY-4.0** license, following the original OpenCodeReasoning-2 license.

## 🙏 Acknowledgments

- **NVIDIA** for the original OpenCodeReasoning-2 dataset
- **DUKEAI** team for the processing pipeline and conformance fixes

## 📖 Citation

```bibtex
@dataset{dukeai_phase3_conformant_2024,
  title={Alizee-Phase3-Conformant - 1.2M Examples},
  author={DUKEAI Team},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/DUKEAI/Alizee-Phase3-Conformant-1.2M}
}
```

---
**Dataset prepared by DUKEAI** | [Organization Page](https://huggingface.co/DUKEAI)