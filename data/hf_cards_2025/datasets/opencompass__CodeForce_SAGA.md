---
language:
- en
license: apache-2.0
task_categories:
- text-generation
pretty_name: CodeForce-SAGA
tags:
- instruction-tuning
- codeforce
- code-generation
library_name: datasets
---

# CodeForce-SAGA: A Self-Correction-Augmented Code Generation Dataset

**CodeForce-SAGA** is a large-scale, high-quality training dataset designed to enhance the code generation and problem-solving capabilities of Large Language Models (LLMs). All problems and solutions are sourced from the competitive programming platform [Codeforces](https://codeforces.com/).

This dataset is built upon the **SAGA (Strategic Adversarial & Constraint-differential Generative workflow)** framework, a novel human-LLM collaborative methodology introduced in the paper "[Rethinking Verification for LLM Code Generation: From Generation to Testing](https://arxiv.org/abs/2507.06920)". The SAGA process ensures that every solution in this dataset has been rigorously verified against a comprehensive and challenging suite of test cases, making it a reliable resource for training robust code models.


## Dataset Highlights

*   **Rigorously Verified Solutions**: Unlike standard datasets, every solution in CodeForce-SAGA has survived a demanding "generate-and-test" loop. Solutions are validated against a rich set of test cases designed to uncover subtle bugs, edge cases, and diverse error patterns.
*   **High-Quality Problem-Solution Pairs**: The dataset contains thousands of programming problems paired with verified, functional Python solutions, making it ideal for supervised fine-tuning and instruction tuning of LLMs.
*   **Grounded in Research**: The dataset's creation is based on the SAGA framework, which addresses critical flaws in existing code evaluation benchmarks, such as test case homogenization and LLM-centric bias.
*   **Rich Metadata**: Each sample includes the problem description, source, and resource limits, providing valuable context for training.

## How to Use

The dataset can be easily loaded using the `datasets` library.

```python
from datasets import load_dataset

# Load the training split
# Replace 'YourUsername/CodeForce_SAGA' with the actual repository path
dataset = load_dataset("opencompass/CodeForce_SAGA", split='train')

# Print the first example
print(dataset)
```
**Example Record:**
```json
{
  "question_id": "1989_A",
  "problem": "You are given two points P=(a,b) and Q=(c,d) on a 2D plane...",
  "source": "Codeforces",
  "limit": "{\"time\": \"1 s\", \"memory\": \"256 MB\"}",
  "test_case": "{
  \"test_cases\": [
    {
      \"input\": \"1 2\
3 4\",
      \"output\": \"Yes\"
    },
    {
      \"input\": \"5 5\
5 6\",
      \"output\": \"Yes\"
    }
  ]
}"
}
```

## Dataset Structure

#### Data Fields

Based on the processing script, the dataset contains the following fields:

*   `question_id` (string): The unique identifier for the problem, typically in the format of `contestId_problemIndex` (e.g., `1989_A`).
*   `problem` (string): The full problem description in text or Markdown format.
*   `source` (string): The platform from which the problem was sourced (e.g., "Codeforces").
*   `limit` (string): A JSON string containing the specified time and memory limits for the problem (e.g., `{"time": "2 s", "memory": "256 MB"}`).
*   `test_case` (string): A JSON string containing the input-output test cases associated with the problem.

#### Data Splits

*   **train**: The main split containing all the problem-solution pairs for training purposes.

## Dataset Creation Methodology

The creation of CodeForce-SAGA is underpinned by the **SAGA framework**, a systematic process designed to produce highly reliable training data.

1.  **Motivation**: Standard code generation benchmarks often use a limited number of test cases. This can lead to models that appear correct but fail on more diverse or adversarial inputs. SAGA was created to address this gap by generating more comprehensive and discriminative test suites.
2.  **Human-LLM Collaboration**: SAGA is a collaborative framework that leverages insights from both correct human solutions (`GroundTruth`) and incorrect human submissions (`Human Bugs`).
3.  **Dual-Pronged Analysis**: An LLM performs two types of analysis:
    *   **Multidimensional Analysis**: Extracts complex constraints, edge cases, and defensive logic from correct human solutions.
    *   **Differential Analysis**: Compares failed submissions with their corrected versions to identify common error patterns and pitfalls.
4.  **Rigorous Verification**: The insights from this analysis are used to generate a challenging suite of test cases. A powerful "teacher" LLM is then tasked with generating a solution to the problem. This solution is only accepted into the final dataset if it passes every single test case in the SAGA-generated suite, undergoing a "self-correction" loop if it initially fails.

This robust verification process ensures that the solutions in CodeForce-SAGA are not just syntactically correct, but functionally robust.

## Citation

If you use this dataset in your research, please cite the original paper:

```bibtex
@misc{ma2025rethinkingverificationllmcode,
      title={Rethinking Verification for LLM Code Generation: From Generation to Testing}, 
      author={Zihan Ma and Taolin Zhang and Maosong Cao and Junnan Liu and Wenwei Zhang and Minnan Luo and Songyang Zhang and Kai Chen},
      year={2025},
      eprint={2507.06920},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.06920}, 
}
```