---
license: apache-2.0
task_categories:
- text-generation
language:
- zh
- en
---


<p align="center">
    <img src="https://huggingface.co/inclusionAI/Ring-lite-distill-preview/resolve/main/ant-bailing.png" width="100"/>
<p>

<p align="center">
          🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope</a>
          🤗 <a href="https://huggingface.co/inclusionAI">HuggingFace</a>
          🖥️ <a href="https://github.com/inclusionAI/Ring">GitHub</a>
<p>


## Ring-lite-sft-data

This is a the SFT data used during the fine-tuning of the [Ring-lite](https://huggingface.co/inclusionAI/Ring-lite) model. The query pool was sourced from open-source repositories and further enriched through synthetic generation using large language models (LLMs). To ensure the production of high-fidelity responses with Long-CoT, we implemented an iterative refinement pipeline that synergistically combines automated model generation, expert manual annotation, and rejection sampling mechanisms. After that, rigorous data-cleansing protocols were applied, including detection and removal of repetitive patterns, mixed-language artifacts, and other noise sources, to yield a robust and high-quality dataset.
The final data is predominantly dominated by three major domains: Mathematics (64.5\%), Code (25.5\%), and Science (9.2\%). The remaining portion of the dataset includes contributions from other categories, such as medicine and history domains. 


More details are reported in our [technical report](https://arxiv.org/abs/2506.14731).

**Note**: Only a partial subset of the complete dataset is publicly released due to third-party data licensing restrictions and procurement agreements. The published portion has been carefully selected to comply with all copyright requirements while maintaining research utility.


## Citation
```
@misc{ringteam2025ringlitescalablereasoningc3postabilized,
      title={Ring-lite: Scalable Reasoning via C3PO-Stabilized Reinforcement Learning for LLMs}, 
      author={Ling Team},
      year={2025},
      eprint={2506.14731},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.14731}, 
}
```