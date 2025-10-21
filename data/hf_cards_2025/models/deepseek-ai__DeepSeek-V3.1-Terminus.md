---
license: mit
library_name: transformers
base_model:
- deepseek-ai/DeepSeek-V3.1-Base
---
# DeepSeek-V3.1-Terminus

<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <img src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/logo.svg?raw=true" width="60%" alt="DeepSeek-V3" />
</div>
<hr>
<div align="center" style="line-height: 1;">
  <a href="https://www.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Homepage" src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/badge.svg?raw=true" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://chat.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-DeepSeek%20V3-536af5?color=536af5&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/deepseek-ai" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-DeepSeek%20AI-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://discord.gg/Tc7c45Zzu5" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-DeepSeek%20AI-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/qr.jpeg?raw=true" target="_blank" style="margin: 2px;">
    <img alt="Wechat" src="https://img.shields.io/badge/WeChat-DeepSeek%20AI-brightgreen?logo=wechat&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://twitter.com/deepseek_ai" target="_blank" style="margin: 2px;">
    <img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-deepseek_ai-white?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="LICENSE" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

## Introduction

This update maintains the model's original capabilities while addressing issues reported by users, including:

- Language consistency: Reducing instances of mixed Chinese-English text and occasional abnormal characters;
- Agent capabilities: Further optimizing the performance of the Code Agent and Search Agent.

| Benchmark | DeepSeek-V3.1 | DeepSeek-V3.1-Terminus |
| :--- | :---: | :---: |
| **Reasoning Mode w/o Tool Use** | | |
| MMLU-Pro | 84.8 | 85.0 |
| GPQA-Diamond | 80.1 | 80.7 |
| Humanity's Last Exam | 15.9 | 21.7 |
| LiveCodeBench | 74.8 | 74.9 |
| Codeforces | 2091 | 2046 |
| Aider-Polyglot | 76.3 | 76.1 |
| **Agentic Tool Use** | | |
| BrowseComp | 30.0 | 38.5 |
| BrowseComp-zh | 49.2 | 45.0 |
| SimpleQA | 93.4 | 96.8 |
| SWE Verified | 66.0 | 68.4 |
| SWE-bench Multilingual | 54.5 | 57.8 |
| Terminal-bench | 31.3 | 36.7 |

**The template and tool-set of search agent have been updated, which is shown in `assets/search_tool_trajectory.html`.**

## How to Run Locally

The model structure of DeepSeek-V3.1-Terminus is the same as DeepSeek-V3. Please visit [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) repo for more information about running this model locally.

For the model's chat template other than search agent, please refer to the [DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) repo.

**Here we also provide an updated inference demo code in the `inference` folder to help the community get started with running our model and understand the details of model architecture.**

**NOTE: In the current model checkpoint, the parameters of `self_attn.o_proj` do not conform to the UE8M0 FP8 scale data format. This is a known issue and will be corrected in future model releases.**

## License

This repository and the model weights are licensed under the [MIT License](LICENSE).

## Citation

```
@misc{deepseekai2024deepseekv3technicalreport,
      title={DeepSeek-V3 Technical Report}, 
      author={DeepSeek-AI},
      year={2024},
      eprint={2412.19437},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.19437}, 
}
```

## Contact

If you have any questions, please raise an issue or contact us at [service@deepseek.com](service@deepseek.com).
