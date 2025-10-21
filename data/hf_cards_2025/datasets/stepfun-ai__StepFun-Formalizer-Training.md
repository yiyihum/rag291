---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- Autoformalization
- Lean4
size_categories:
- 100K<n<1M
---

<p align="center">
  <img src="assets/logo.png" width="250px"><br>
</p>

# StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion

<div align="center"> 
  <a href="https://www.arxiv.org/abs/2508.04440"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red"></a> &ensp;
  <a href="https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"><img src="https://img.shields.io/static/v1?label=Model&message=HuggingFace&color=yellow"></a> &ensp;
  <a href="https://github.com/stepfun-ai/StepFun-Formalizer"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=blue"></a> &ensp;
</div>
<br>

## Introduction

This repository includes the Stage-1 SFT and RL training data of [StepFun-Formalizer](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B):

- `NuminaMath-Formal-SFT-183K`: Informal-formal problem pairs translated from [NuminaMath-1.5](https://huggingface.co/datasets/AI-MO/NuminaMath-1.5) by [Kimina-Autoformalizer-7B](https://huggingface.co/AI-MO/Kimina-Autoformalizer-7B), used to supplement the model’s domain knowledge in formal language.

- ` StepFun-Formalizer-RL-6K`: We collected informal math problems paired with human-annotated (or model-generated and manually reviewed) formal statements as RL data, including [MiniF2F](https://arxiv.org/abs/2109.00110), [ProofNet](https://arxiv.org/abs/2302.12433), [PutnamBench](https://arxiv.org/abs/2407.11214), [Compfiles](https://github.com/dwrensha/compfiles) and [FormalMATH](https://arxiv.org/abs/2505.02735) (w/o Lite).

The formal statements pass the syntax check of Lean4 v4.15.0. All training data have undergone 13-gram decontamination against benchmarks.

Due to copyright restrictions, the Stage-2 SFT (Reasoning) data cannot be released.

Please refer to our [paper](https://arxiv.org/abs/2508.04440) for more details.


## License

The datasets are released under the Apache License (Version 2.0).

## Citation

```latex
@misc{stepfunformalizer2025,
      title={StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion}, 
      author={Yutong Wu and Di Huang and Ruosi Wan and Yue Peng and Shijie Shang and Chenrui Cao and Lei Qi and Rui Zhang and Zidong Du and Jie Yan and Xing Hu},
      year={2025},
      eprint={2508.04440},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.04440}, 
}
```
