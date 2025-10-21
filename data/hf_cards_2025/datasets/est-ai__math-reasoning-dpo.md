---
license: mit
language:
- en
tags:
- mathematics
- reasoning
- instruction-following
- dpo
- preference-learning
- rlhf
task_categories:
- text-generation
- question-answering
size_categories:
- 1K<n<2K
---

# Mathematical Reasoning DPO Dataset

This dataset contains mathematical reasoning problems with chosen and rejected responses, designed for Direct Preference Optimization (DPO) and preference learning of language models.

## Dataset Structure

The dataset follows the ShareGPT format for DPO training with three main fields:

- `conversations`: List of conversation turns leading up to the response
- `chosen`: Preferred response with detailed reasoning and correct solution
- `rejected`: Less preferred response (may contain errors, incomplete reasoning, or suboptimal solutions)

## Example

```json
{
  "conversations": [
    {
      "from": "human",
      "value": "Find the derivative of y = (1/24)(x² + 8)√(x² - 4) + (x²/16) arcsin(2/x), x > 0"
    }
  ],
  "chosen": {
    "from": "gpt",
    "value": "<think>\n[Detailed step-by-step reasoning]\n</think>\n\n[Clear mathematical solution with proper derivation]\n\n\\boxed{final answer}"
  },
  "rejected": {
    "from": "gpt",
    "value": "[Less detailed or potentially incorrect solution]"
  }
}
```

## Field Mapping

When using with LLaMA Factory, the dataset uses these mappings:
- `conversations` → `messages` field
- `chosen` → `chosen` field  
- `rejected` → `rejected` field
- Role tags: `from` → role, `value` → content
- User role: `human`, Assistant role: `gpt`

## Usage

This dataset is compatible with DPO training frameworks including:
- LLaMA Factory (with `ranking: true` and `formatting: "sharegpt"`)
- TRL (Transformers Reinforcement Learning)
- Other preference learning libraries

## Training Configuration

This dataset was used with:
- Base Model: DeepSeek-R1-Distill-Qwen-7B (after SFT)
- Template: Qwen
- DPO Beta: 0.3
- Loss Function: NCA Pair Loss
- Sequence Length: 20,000 tokens
- Training: 2 epochs with constant learning rate

## Citation

If you use this dataset, please cite the relevant mathematical competition and DPO methodology papers.
