---
task_categories:
- text-generation
language:
- en
- zh
tags:
- reasoning
size_categories:
- 1M<n<10M
---

## 📘 Dataset Summary

AM-Thinking-v1 and Qwen3-235B-A22B are two reasoning datasets distilled from state-of-the-art teacher models. Each dataset contains high-quality, automatically verified responses generated from a shared set of **1.89 million queries** spanning a wide range of reasoning domains.

The datasets share the same format and verification pipeline, allowing for direct comparison and seamless integration into downstream tasks. They are intended to support the development of open-source language models with strong reasoning abilities. Benchmark results show their effectiveness on AIME2024, AIME2025, MATH500, and LiveCodeBench.

For the AM-Qwen3-Distilled dataset, see: https://huggingface.co/datasets/a-m-team/AM-Qwen3-Distilled for more details.


## 📊 Benchmark Performance

![alt text](benchmarks.png)

| Benchmark         | [AM-Thinking-v1 Distilled](https://huggingface.co/datasets/a-m-team/AM-Thinking-v1-Distilled) | [Qwen3-235B-A22B Distilled](https://huggingface.co/datasets/a-m-team/AM-Qwen3-Distilled) | DeepSeek-R1 Distilled|[Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | [AM-Thinking-v1](https://huggingface.co/a-m-team/AM-Thinking-v1) | [Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
|-------------------|--------------------------|---------------------------|---------------------------|--------------------------|--------------------------|---------------------------|---------------------------|
| AIME2024          | **84.3**                 | 79.4                      | 70.9 | 81.4|     85.3          |       85.7      | 79.8 |
| AIME2025          | **72.2**                 | 62.2                      |52.8 |  72.9|      74.4        | 81.5                    | 70.0|
| MATH500           | **98.4**                 | 93.9                      |95.8 |         -       |-|           -           |-|
| LiveCodeBench     | **65.9**                 | 59.6                      | 57.0| 65.7|      70.3    | 70.7                     | 64.3|


These results reflect models trained separately using each dataset, demonstrating the impact of teacher model quality on downstream reasoning capabilities.


## 📂 Dataset Structure

### Data Fields

Each sample is a dictionary with the following fields:

- `system`: The system prompt used during distillation, typically guiding structured reasoning via `<think>` and `<answer>` tags.
Note: Some instance's 'system' fields in our dataset are empty. 'system' field is not used in training. Feel free to use them.

- `conversations`: A list of dialogue turns structured as:
  - `from`: Either `'human'` or `'assistant'`.
  - `value`: Full message content.
  - `info`: Metadata dictionary containing:
    - `source`: Dataset origin (e.g., `OpenHermes-2.5`).
    - `category`: Task domain (e.g., `math`, `code`, `other`).
    - `ground_truth`: Ground truth reference (if applicable).
    - `test_case`: Associated test case ID (optional).
    - `instruction_constrain`: Instruction constraint metadata (optional).
    - `think_content`: Assistant’s reasoning trace.
    - `answer_content`: Final answer segment.
    - `verify_score`: Verification confidence score (float ≥ 0.9).
    - `model_name`: Name of the teacher model (`am_thinking_v1` or `qwen3_235b_a22b`).
    - `ppl`: Perplexity of the assistant’s output.


## 📈 Dataset Statistics

- Shared query base: **1.89 million** unique prompts
- Each dataset contains responses distilled from one of the following models:
  - **AM-Thinking-v1**
  - **Qwen3-235B-A22B**
- Task Category Breakdown:
  - General Chat: ~41.8%
  - Mathematical Reasoning: ~29.5%
  - Code Generation: ~17.1%
  - Others (Science, Instruction Following, Dialogue): ~11.6%
The general chat includes both multi-turn conversations and other types of data.

![alt text](AM-distilled.png)

## ✅ Verification and Quality Control

All outputs underwent **automated verification**, with methods tailored to task categories:

- **Math**: Math-Verify (binary pass/fail)
- **Code**: Test-case based validation in sandbox environments
- **Science**: Answer similarity via LLM scoring
- **Instruction Follow**: Verified by `IFEval` validator
- **General Chat**: Evaluated using a reward model (e.g., Decision-Tree-Reward-Llama-3.1-8B)

Each dataset individually applies:

- Perplexity filtering using a strong 32B LLM
- N-gram repetition filtering
- Structural formatting checks (e.g., presence of `<think>` and `<answer>`)


## ⚠️ Limitations

Developers should strictly limit the use of this project’s open-sourced code, data, models, and related artifacts to **research purposes only**. **Commercial use and any applications that could potentially cause harm are strictly prohibited**.

The content in this dataset does not reflect the views, beliefs, or endorsements of any individual or institution. The authors disclaim any responsibility for consequences arising from the use, misuse, or interpretation of the dataset and associated materials.


## 📜 Citation

If you use either dataset, please cite:
```
@misc{tian2025correctanswersequaldistillation,
      title={Not All Correct Answers Are Equal: Why Your Distillation Source Matters}, 
      author={Xiaoyu Tian and Yunjie Ji and Haotian Wang and Shuaiting Chen and Sitong Zhao and Yiping Peng and Han Zhao and Xiangang Li},
      year={2025},
      eprint={2505.14464},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.14464}, 
}
```