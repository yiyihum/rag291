---
language:
- en
- zh
license: apache-2.0
pretty_name: AL-GR
tags:
- generative-recommendation
- sequential-recommendation
- e-commerce
- llm
- instruction-tuning
- prompting
- generative-retrieval
task_categories:
- text-generation
- text-retrieval
- feature-extraction
- image-feature-extraction
dataset_info:
- config_name: default
  splits:
  - name: s1
  - name: s2
  - name: s3
---

# AL-GR: A Large-scale Generative Recommendation Dataset

<!-- Paper: [FORGE: Forming Semantic Identifiers for Generative Retrieval in Industrial Datasets](https://huggingface.co/papers/2509.20904)\
Code: [https://github.com/selous123/al_sid](https://github.com/selous123/al_sid)\
Project Page: [https://huggingface.co/datasets/AL-GR](https://huggingface.co/datasets/AL-GR) -->

## Dataset Summary

**AL-GR** is a large-scale dataset designed for generative recommendation tasks using Large Language Models (LLMs). The core idea is to transform user historical behavior sequences into natural language prompts, enabling an LLM to learn and predict a user's subsequent actions in an e-commerce scenario.

The dataset contains over **400 million** behavior sequences. Each sample includes three fields: `system`, `user`, and `answer`. The `system` field defines the LLM's role and task, the `user` field provides the sequence of historical user behaviors, and the `answer` field contains the next sequence of actions the model is expected to predict.

This format allows for direct use in instruction fine-tuning to train an LLM for powerful sequential recommendation tasks.

## Supported Tasks and Leaderboards

-   **`generative-recommendation`**: This dataset primarily supports the generative recommendation task, where the model needs to generate multiple subsequent behavior codes at once based on the given history.

## Dataset Structure

### Data Instances

A typical data instance is as follows. Note that the `answer` field contains multiple subsequent behavior codes, concatenated as a single string.

```json
{
  "system": "You are a recommendation system. Based on the user's historical behavior, predict the user's next action in an e-commerce scenario. I will provide a sequence of semantic codes for continuous behaviors, arranged in the order of user clicks.",
  "user": "The current user's historical behavior is as follows: C1220C8322C20452C6084C10195C20067C3256C14673C21112C705",
  "answer": "C9988C7766C5544"
}
```

### Data Fields

-   `system` (string): A system-level instruction for the LLM, describing its role and task.
-   `user` (string): The user's specific request, containing a time-ordered sequence of historical behavior codes.
-   `answer` (string): The user's subsequent sequence of behavior codes that the model needs to predict. It is a single string concatenated from multiple semantic IDs (e.g., `C9988`, `C7766`, `C5544`).

### Data Splits

The dataset comprises over 400 million behavior sequences in total and is divided into three distinct training sets based on time. This chronological split is suitable for training and evaluating time-aware models.

| Split | Description | Number of Samples |
| :---- | :---------- | :---------------- |
| `s1` | Early training data | `[Number of s1 samples]` |
| `s2` | Mid-period training data| `[Number of s2 samples]` |
| `s3` | Recent training data | `[Number of s3 samples]` |

## Dataset Creation

### Source Data

This dataset originates from a large-scale, anonymized, real-world industrial e-commerce dataset, ensuring the authenticity and complexity of the data.

### Data Curation & Annotations

The codes in the behavior sequences (e.g., `C1220`) are not simple item IDs but **semantic IDs**. They are obtained by **discretizing rich multi-modal features** (such as images, text descriptions, etc.). This method ensures that each ID encapsulates deep semantic information about the items, providing a solid foundation for the LLM's comprehension and generation capabilities.

The dataset construction process is as follows:
1.  Extract user behavior sessions from the source data.
2.  Split each session chronologically into a historical part (for the `user` field) and a future part to be predicted (for the `answer` field).
3.  Combine these with a predefined instruction template (the `system` field) to create samples suitable for instruction fine-tuning.
4.  Finally, all data is partitioned chronologically into three splits: `s1`, `s2`, and `s3`.

## Usage

You can easily load this dataset using the `datasets` library from Hugging Face:

```python
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
# For the full AL-GR dataset, use:
# dataset = load_dataset("AL-GR/AL-GR")
# For a tiny demo subset, use:
dataset = load_dataset("AL-GR/AL-GR-Tiny", data_files="train_data/s1_tiny.csv", split="train")

# Inspect a sample
print(dataset[0])
# Output:
# {
#   'system': 'You are a recommendation system...',
#   'user': 'The current user\'s historical behavior is as follows: C1220...',
#   'answer': 'C9988C7766C5544'
# }
```

### Prompting

For inference or training, you would typically combine the `system` and `user` fields to form the model's input. Here is an example following the Llama-2-chat format:

```python
# To load the dataset with `datasets.load_dataset`
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
# For the full AL-GR dataset, use:
# dataset = load_dataset("AL-GR/AL-GR")
# For a tiny demo subset, use:
dataset = load_dataset("AL-GR/AL-GR-Tiny", data_files="train_data/s1_tiny.csv", split="train")

sample = dataset[0] # Access the first sample from the loaded split

# Prompt for inference
prompt = f"<s>[INST] <<SYS>>
{sample['system']}
<</SYS>>

{sample['user']} [/INST]"

# Full sequence for training
full_prompt = f"<s>[INST] <<SYS>>
{sample['system']}
<</SYS>>

{sample['user']} [/INST] {sample['answer']} </s>"

# The `prompt` or `full_prompt` can then be fed into a model for inference or training.
print("Inference Prompt Example:")
print(prompt)
print("
Training Prompt Example:")
print(full_prompt)
```

## Citation

If you use this dataset in your research, please cite:

<!-- ```bibtex
@misc{fu2025forge,
      title={FORGE: Forming Semantic Identifiers for Generative Retrieval in Industrial Datasets}, 
      author={Kairui Fu and Tao Zhang and Shuwen Xiao and Ziyang Wang and Xinming Zhang and Chenchi Zhang and Yuliang Yan and Junjun Zheng and Yu Li and Zhihong Chen and Jian Wu and Xiangheng Kong and Shengyu Zhang and Kun Kuang and Yuning Jiang and Bo Zheng},
      year={2025},
      eprint={2509.20904},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2509.20904}, 
}
``` -->

## License

This dataset is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).