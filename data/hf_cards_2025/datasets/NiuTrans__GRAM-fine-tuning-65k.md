---
license: apache-2.0
language:
- en
tags:
- rlhf
- reward
- preference
---

This is the dataset for Fine-tuning [GRAM](https://github.com/wangclnlp/GRAM).

## Format

Each item of the dataset includes following keys:

- `instruction`: any prompt with corresponding two responses in following template:
  ```text
  Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user's instructions and answers the user's question better.
  Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision. Do not allow the length of the responses to influence your evaluation. Do not favor certain names of the assistants. Be as objective as possible.
  Please directly output your final verdict by strictly following this format: "A" if assistant A is better, "B" if assistant B is better.

  [User Question]
  {your prompt here}

  [The Start of Assistant A's Answer]
  {answer of assistant A}
  [The End of Assistant A's Answer]

  [The Start of Assistant B's Answer]
  {answer of assistant B}
  [The End of Assistant B's Answer]

  #Preferred:
  ```
- `input`: leave it empty.
- `output`: the correct option, "A" or "B".

An example in json format:

```json
[
  {
    "instruction": "Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. ... [User Question]... [The Start of Assistant A's Answer] ... [The Start of Assistant B's Answer] ...",
    "input": "",
    "output": "B"
  },
  ...
]
```

## Source

The dataset is filtered from [Skywork/Skywork-Reward-Preference-80K-v0.2](https://huggingface.co/datasets/Skywork/Skywork-Reward-Preference-80K-v0.2) by removing data that is too long and those including garbled characters.

## Citation
```bash
@misc{wang2025gram,
      title={GRAM: A Generative Foundation Reward Model for Reward Generalization}, 
      author={Chenglong Wang and Yang Gan and Yifu Huo and Yongyu Mu and Qiaozhi He and Murun Yang and Bei Li and Tong Xiao and Chunliang Zhang and Tongran Liu and Jingbo Zhu},
      year={2025},
      eprint={2506.14175},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.14175}, 
}
```