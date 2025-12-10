---
language:
- en
- zh
license: apache-2.0
size_categories:
- 1M<n<10M
task_categories:
- text-generation
tags:
- code
---

<p align="center">
    <img src="https://huggingface.co/inclusionAI/Ling-lite/resolve/main/ant-bailing.png" width="100"/>
<p>

<p align="center">
          🤗 <a href="https://huggingface.co/inclusionAI">Hugging Face</a>
          🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope</a>
          🖥️ <a href="https://github.com/codefuse-ai/Ling-Coder-Lite">GitHub</a>
<p>

# Ling-Coder Dataset
The Ling-Coder Dataset comprises the following components:
- [Ling-Coder-SFT](https://huggingface.co/datasets/inclusionAI/Ling-Coder-SFT): A subset of SFT data used for training Ling-Coder Lite, containing more than 5 million samples.
- [Ling-Coder-DPO](https://huggingface.co/datasets/inclusionAI/Ling-Coder-DPO): A subset of DPO data used for training Ling-Coder Lite, containing 250k samples.
- [Ling-Coder-SyntheticQA](https://huggingface.co/datasets/inclusionAI/Ling-Coder-SyntheticQA): A subset of synthetic data used for annealing training of Ling-Coder Lite, containing more than 24 million samples.

## Ling-Coder-SFT

This is a subset of the SFT data used during the fine-tuning of the [Ling-Coder Lite](https://huggingface.co/inclusionAI/Ling-Coder-lite) model, comprising over 5 million English and Chinese samples. It covers more than 20 programming languages and encompasses various topics, including text-to-code, code completion, code execution reasoning, complex algorithm question-and-answer, and the use of popular Python libraries.


This dataset was synthesized using methods similar to OSS-Instruct and Evol-Instruct. Initially, we utilized LLMs to extract key points and further explanations from each code-related seed. Then, LLMs were employed to expand these key points into seven divergent sets of key point combinations. For each divergent set, we generated 10 unique programming-related questions. Subsequently, LLMs were used to answer each question. Finally, questions and answers were combined and underwent rule-based filtering, detoxification, decontamination, quality checking, and ablation selection to produce this dataset. For more detailed information on the construction process, please refer to our technique report.


## Citation Information
**Please consider citing our technique report [Ling-Coder-TR](https://huggingface.co/papers/2503.17793) if you find this dataset useful:**

```
@misc{codefuse2025samplemattersleveragingmixtureofexperts,
      title={Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM}, 
      author={Codefuse and Ling Team},
      year={2025},
      eprint={2503.17793},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2503.17793}, 
}
```