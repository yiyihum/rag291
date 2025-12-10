---
license: apache-2.0
language:
- en
tags:
- rlhf
- reward
- preference
---

This is the dataset for Per-Training [GRAM](https://github.com/wangclnlp/GRAM).

## Format

Each item of the dataset includes following keys:

- `instruction`: any prompt in following template:
  ```text
  [User Question]
  {your prompt here}
  ```
- `input`: the input for above prompt, can be empty if there is not.
- `output`: two responses in following template:
  ```text
  [The Start of Assistant A's Answer]
  {answer of assistant A}
  [The End of Assistant A's Answer]

  [The Start of Assistant B's Answer]
  {answer of assistant B}
  [The End of Assistant B's Answer]
  ```

An example in json format:

```json
[
  {
    "instruction": "[User Question]\nCan dogs get covid?\n\n",
    "input": "",
    "output": "[The Start of Assistant A's Answer]\nYes, indeed. ... [The End of Assistant A's Answer]\n\n[The Start of Assistant B's Answer]\nMany of the symptoms are similar, including fever, coughing, loss of smell, etc. ...\n[The End of Assistant B's Answer]"
  },
  ...
]
```

## Source

The dataset is filtered from [llm-blender/Unified-Feedback](https://huggingface.co/datasets/llm-blender/Unified-Feedback) by removing data that is too long and those including garbled characters.

## Citation
```
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