---
tags:
- math
- reasoning
- instruction-tuning
- alignment
- non-dual
language:
- en
license: cc-by-4.0
---

# nondual_openmath_final

A **non-dual reformulation** of the [unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini) dataset.  
All assistant solutions have been rewritten into **impersonal, non-dual language** using OpenAI models, and finalized so that the dataset no longer contains duplicate `*_nondual` fields.

## Dataset Summary

- **Source:** [unsloth/OpenMathReasoning-mini](https://huggingface.co/datasets/unsloth/OpenMathReasoning-mini)  
- **Format:** JSONL, each line is a dictionary with the following fields:

| Field                | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `problem`            | Math problem statement (rewritten into non-dual phrasing).                  |
| `generated_solution` | Assistant-generated solution, rewritten into non-dual phrasing.             |
| `expected_answer`    | Final answer, rewritten if needed into non-dual form.                       |
| `problem_type`       | Metadata about how the problem/answer was extracted.                        |
| `problem_source`     | Dataset or corpus of origin (e.g., AoPS, MATH).                             |
| `generation_model`   | Model that produced the original solution.                                  |
| `pass_rate_72b_tir`  | Evaluation metric (pass rate) for problem difficulty.                       |
| `inference_mode`     | Inference style (e.g., `cot` = chain-of-thought).                           |

All `*_nondual` fields from the intermediate dataset have been **promoted** to their base names (`problem`, `generated_solution`, `expected_answer`), and the originals with dual phrasing have been removed.

## Example

```json
{
  "expected_answer": "14",
  "problem_type": "has_answer_extracted",
  "problem_source": "aops_c4_high_school_math",
  "generation_model": "DeepSeek-R1",
  "pass_rate_72b_tir": "0.96875",
  "problem": "Given √(x^2+165) - √(x^2-52) = 7 and x is positive, all possible values of x are to be found.",
  "generated_solution": "To solve the equation √(x^2+165) - √(x^2-52) = 7 for positive x, the steps are as follows: ...",
  "inference_mode": "cot"
}
