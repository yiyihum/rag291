---
license: mit
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- math
- reasoning
- rlhf
- verl
- ppo
- comparison
- gsm8k
size_categories:
- n<1K
---

# GSM8K: BASE vs VERL-trained Model Comparison Dataset

## Overview

This dataset provides a comprehensive comparison between a base language model and its VERL (Reinforcement Learning from Human Feedback) fine-tuned version on mathematical reasoning tasks from GSM8K.

## Dataset Summary

- **Total Samples**: 50 GSM8K test problems
- **BASE Model**: Qwen/Qwen2.5-0.5B-Instruct (22.0% accuracy)  
- **VERL Model**: karthik/verl-qwen2.5-0.5b-gsm8k-ppo-step360 (28.0% accuracy)
- **Improvement**: +6.0 percentage points (+27% relative improvement)

## Performance Analysis

| Metric | Count | Percentage |
|--------|--------|------------|
| VERL Improved | 9 problems | 18% |
| VERL Degraded | 6 problems | 12% |
| Both Correct | 5 problems | 10% |
| Both Incorrect | 30 problems | 60% |
| **Net Improvement** | **+3 problems** | **+6%** |

## Dataset Structure

Each row contains:

### Input
- `problem_id`: Unique identifier (0-49)
- `question`: Original GSM8K math word problem
- `ground_truth_text`: Full solution from GSM8K
- `ground_truth_answer`: Correct numerical answer

### BASE Model Output
- `base_model_name`: "Qwen/Qwen2.5-0.5B-Instruct"
- `base_response`: Step-by-step solution attempt
- `base_predicted_answer`: Predicted numerical answer
- `base_correct`: Boolean correctness

### VERL Model Output  
- `verl_model_name`: "karthik/verl-qwen2.5-0.5b-gsm8k-ppo-step360"
- `verl_response`: Step-by-step solution attempt
- `verl_predicted_answer`: Predicted numerical answer
- `verl_correct`: Boolean correctness

### Comparison Metrics
- `improvement`: VERL correct AND BASE incorrect
- `degradation`: BASE correct AND VERL incorrect  
- `both_correct`: Both models correct
- `both_incorrect`: Both models incorrect

## Example Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("karthik/gsm8k-base-vs-verl-comparison")

# Example: Find problems where VERL improved
improvements = dataset['train'].filter(lambda x: x['improvement'])
print(f"VERL improved on {len(improvements)} problems")

# Example: Compare responses for a specific problem
problem = dataset['train'][0]
print(f"Question: {problem['question']}")
print(f"BASE: {problem['base_response'][:100]}...")
print(f"VERL: {problem['verl_response'][:100]}...")
print(f"Correct answer: {problem['ground_truth_answer']}")
```

## Key Findings

1. **Significant Improvement**: VERL training improved mathematical reasoning by 27% relative to the base model
2. **Better Problem Solving**: VERL model showed more structured, step-by-step reasoning
3. **Reduced Errors**: Fewer arithmetic and logical errors in VERL responses
4. **Consistent Format**: VERL responses more consistently followed the expected solution format

## Training Details

The VERL model was trained using:
- **Method**: PPO (Proximal Policy Optimization) 
- **Training Steps**: 360 steps
- **Dataset**: GSM8K training set (7,473 problems)
- **Validation Accuracy**: 26.0% during training
- **Test Accuracy**: 28.0% on this evaluation set

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{gsm8k_base_verl_comparison,
  title={GSM8K: BASE vs VERL-trained Model Comparison Dataset},
  author={Karthik},
  year={2025},
  url={https://huggingface.co/datasets/karthik/gsm8k-base-vs-verl-comparison}
}
```

## License

MIT License - Free for research and commercial use.
