---
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- en
base_model:
- miromind-ai/MiroThinker-14B-SFT-v0.2
tags:
- agent
- open-source
- miromind
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/68525b342230a897a65cc1c0/87mYQ_a-4jpnMkVR4hrgm.png" width="55%" alt="MiroThinker" />
</div>
<!-- <hr> -->
<div align="center">

[![Demo](https://img.shields.io/badge/Demo-FFB300?style=for-the-badge&logo=airplayvideo&logoColor=white)](https://dr.miromind.ai/)
[![Models](https://img.shields.io/badge/Models-5EDDD2?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/collections/miromind-ai/mirothinker-v02-68af084a18035f57b17cd902)
[![Data](https://img.shields.io/badge/Data-0040A1?style=for-the-badge&logo=huggingface&logoColor=ffffff&labelColor)](https://huggingface.co/datasets/miromind-ai/MiroVerse-v0.1)
[![Blog](https://img.shields.io/badge/Blog-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://miromind.ai/blog/miromind-research-agent)

[![Github](https://img.shields.io/badge/GitHub-24292F?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MiroMindAI/MiroThinker)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/GPqEnkzQZd)
[![WeChat](https://img.shields.io/badge/WeChat-07C160?style=for-the-badge&logo=wechat&logoColor=white)](https://huggingface.co/datasets/miromind-ai/MiroFlow-Benchmarks/resolve/main/assets/wechat.png)
[![RedNote](https://img.shields.io/badge/RedNote-FF2442?style=for-the-badge&logo=revoltdotchat&logoColor=white)](https://www.xiaohongshu.com/user/profile/5e353bd80000000001000239)
[![Website](https://img.shields.io/badge/Website-4285F4?style=for-the-badge&logo=monster&logoColor=white)](https://miromind.ai/)

</div>

## Introduction

MiroThinker is an open-source agentic model series. Designed as a research agent for complex, long-horizon problem solving, it integrates strong capabilities in task decomposition, multi-hop reasoning, retrieval-augmented generation, code execution, web browsing, and document/file processing, enabling a wide range of real-world applications.

In MiroThinker-v0.2, we introduced three key improvements:

- **Richer training data** from both English and Chinese sources, yielding significant gains in benchmark performance and generalization.
- **Unified DPO training** with a single preference dataset across all models.
- **Extended context length** from 40k to 64k for more challenging multi-turn tool-use tasks.

Compared to v0.1, MiroThinker-v0.2 delivers consistent gains across benchmarks. For example, scores improved from **57.3 → 64.1** on **GAIA-Text-103** and from **17.0 → 29.4** on **BrowseComp-ZH**, reflecting substantial advancements in the model’s general research agent capabilities.

<div>
  <img src="https://huggingface.co/datasets/miromind-ai/MiroFlow-Benchmarks/resolve/main/assets/MiroThinker_v0.2_Performance_2.png" width="100%" alt="MiroThinker" />
</div>

## Online Demo

Welcome to try out our online demo [here](https://dr.miromind.ai/).

## Performance 

> [!IMPORTANT]
> <div>
> To prevent data leakage during searches, we block Hugging Face domains to ensure the model doesn't access answers through shortcuts.
> </div>

### Comparison with SOTA Research Agents

<div>
  <img src="https://huggingface.co/datasets/miromind-ai/MiroFlow-Benchmarks/resolve/main/assets/MiroThinker_v0.2_Performance_0.png" width="100%" alt="MiroThinker" />
</div>

### GAIA Benchmark

<div>
  <img src="https://huggingface.co/datasets/miromind-ai/MiroFlow-Benchmarks/resolve/main/assets/MiroThinker_v0.2_Performance_1.png" width="100%" alt="MiroThinker" />
</div>

## Quick Start

MiroThinker-v0.2 is trained on our large-scale, high-quality trajectory and preference datasets MiroVerse-v0.2, utilizing the efficient training framework [MiroTrain](https://github.com/MiroMindAI/MiroTrain), and enhanced with tool-use capabilities through our agentic framework [MiroFlow](https://github.com/MiroMindAI/MiroFlow). 

To promote reproducibility and benefit the community, we decided to open-source the entire suite mentioned above. For more technical details, evaluation results, and usage tutorials, please visit our [GitHub repository](https://github.com/MiroMindAI/MiroThinker).

## License

MiroThinker-v0.2 is licensed under Apache 2.0.

## Contact Us

MiroThinker is developed by the MiroMind Foundation Model Team.
If you would like to leave us a message, feel free to get in touch. 
In addition to [GitHub](https://github.com/MiroMindAI/), 
[Discord](https://discord.com/invite/GPqEnkzQZd), 
[WeChat](https://huggingface.co/datasets/miromind-ai/MiroFlow-Benchmarks/resolve/main/assets/wechat.png), 
and [RedNote](https://www.xiaohongshu.com/user/profile/5e353bd80000000001000239), 
you can also reach us via email at service@miromind.ai.