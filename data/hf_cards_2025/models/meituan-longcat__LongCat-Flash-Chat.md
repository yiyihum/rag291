---
license: mit
library_name: LongCat-Flash-Chat
pipeline_tag: text-generation
tags:
- transformers
---

# LongCat-Flash-Chat

<div align="center">
  <img src="https://raw.githubusercontent.com/meituan-longcat/LongCat-Flash-Chat/main/figures/longcat_logo.svg" 
       width="300" 
       alt="LongCat Logo"/>
</div>

<hr>

<div align="center" style="line-height: 1;">

  <a href="https://longcat.ai/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-LongCat--Flash--Chat-ADFF2F?color=29E154&logoColor=white"  fill-opacity="1" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/meituan-longcat" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-LongCat-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/meituan-longcat/LongCat-Flash-Chat/blob/main/figures/wechat_official_accounts.png" target="_blank" style="margin: 2px;">
    <img alt="Wechat" src="https://img.shields.io/badge/WeChat-LongCat-brightgreen?logo=wechat&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://x.com/Meituan_LongCat" target="_blank" style="margin: 2px;">
    <img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-LongCat-white?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/meituan-longcat/LongCat-Flash-Chat/blob/main/LICENSE" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>


## Model Introduction
We introduce LongCat-Flash, a powerful and efficient language model with 560 billion total parameters, featuring an innovative Mixture-of-Experts (MoE) architecture. The model incorporates a dynamic computation mechanism that activates 18.6B∼31.3B parameters (averaging∼27B) based on contextual demands, optimizing both computational efficiency and performance. To achieve advanced training and inference efficiency, we employ a shortcut-connected architecture that expands computation-communication overlap window, achieving over 100 tokens per second (TPS) for inference cost-effectively. Our comprehensive training and scaling strategies ensure stable, efficient training, while tailored data strategies enhance model performance. 

Now we release LongCat-Flash-Chat, a non-thinking foundation model that delivers highly competitive performance among leading models, with exceptional strengths in agentic tasks.


### Key Features

#### 🌟 Scalable Architectural Design for Computational Efficiency

LongCat-Flash is designed and optimized under two key principles: efficient computation utilization, as well as  efficient training and inference. Specifically, (1) As not all tokens are equal, we introduce the zero-computation experts mechanism in MoE blocks to allocate a dynamic computation budget to important tokens based on their significance, i.e., activating 18.6 to 31.3 billion parameters (out of 560 billion total) based on contextual demands. To ensure consistent computation load, we employ expert bias adjusted by a PID-controller, maintaining an average of∼27 billion activated parameters per token. (2) As communication overhead becomes a bottleneck during MoE model scaling, we incorporate the Shortcut-connected MoE (ScMoE) design to expand the computation-communication overlap window. Combined with customized infrastructure optimizations, this design enables training at a massive scale of over tens of thousands accelerators and inference with high throughput and low latency.


#### 🌟 Effective Model Scaling Strategy

Effectively and efficiently scaling model size remains a key challenge in strategy design. To this end, we develop a comprehensive stability-and-scaling framework for robustly training large-scale models: (1) We successfully apply a hyperparameter transfer strategy to such a large model, predicting optimal hyperparameter configurations by leveraging results from smaller proxy models with theoretical guarantees. (2) We initialize the model using a model-growth mechanism based on a refined half-scale checkpoint, achieving improved performance compared to conventional initialization methods. (3) A multi-pronged stability suite incorporates principled router-gradient balancing, a hidden z-loss to suppress massive activations, and fine-tuned optimizer configurations. (4) To enhance the reliability of large-scale cluster training, we introduce deterministic computation. This guarantees the exact reproducibility of experiments and enables the detection of SDC (Silent Data Corruption) during the training process. These interventions ensure that LongCat-Flash ’s training remains stable, with no irrecoverable loss spikes.

#### 🌟 Multi-Stage Training Pipeline for Agentic Capability
Through a meticulously designed pipeline, LongCat-Flash is endowed with advanced agentic behaviors. Initial efforts focus on constructing a more suitable base model for agentic post-training, where we design a two-stage pretraining data fusion strategy to concentrate reasoning-intensive domain data. During mid-training, we enhance reasoning and coding capabilities while extending the context length to 128k to meet agentic post-training requirements. Building on this advanced base model, we proceed with a multi-stage post-training. Recognizing the scarcity of high-quality, high-difficulty training problems for agentic tasks, we design a multi-agent synthesis framework that defines task difficulty across three axes, i.e., information processing, tool-set complexity, and user interaction—using specialized controllers to generate complex tasks requiring iterative reasoning and environmental interaction.

For more detail, please refer to the comprehensive [***LongCat-Flash Technical Report***](https://github.com/meituan-longcat/LongCat-Flash-Chat/blob/main/tech_report.pdf).

## Evaluation Results
| **Benchmark** | **DeepSeek V3.1** | **Qwen3 MoE-2507** | **Kimi-K2** | **GPT-4.1** | **Claude4 Sonnet** | **Gemini2.5 Flash** | **LongCat-Flash** |
|---------------|-------------------|--------------------|-------------|-------------|--------------------|---------------------|-------------|
| **Architecture** | MoE | MoE | MoE | - | - | - | MoE |
| **# Total Params** | 671B | 235B | 1043B | - | - | - | 560B |
| **# Activated Params** | 37B | 22B | 32B | - | - | - | 27B |
| **General Domains** | | | | | | | |
| MMLU<sub>(acc)</sub> | 90.96 | 90.23 | 89.86 | 89.64 | 91.75 | 86.33 | 89.71 |
| MMLU-Pro<sub>(acc)</sub> | 84.45 | 84.83 | 82.06 | 81.72 | 83.74 | 81.95 | 82.68 |
| ArenaHard-V2<sub>(acc)</sub> | 84.10 | 88.20 | 85.70 | 61.50 | 62.10 | 77.00 | 86.50 |
| CEval<sub>(acc)</sub> | 89.21 | 92.70 | 91.26 | 79.53 | 86.63 | 78.78 | 90.44 |
| CMMLU<sub>(acc)</sub> | 88.04 | 88.14 | 89.66 | 77.65 | 86.51 | 78.30 | 84.34 |
| **Instruction Following** | | | | | | | |
| IFEval<sub>(acc)</sub> | 86.69 | 88.54 | 88.91 | 85.58 | 88.35 | 83.92 | 89.65 |
| COLLIE<sub>(acc)</sub> | 43.80 | 49.71 | 56.34 | 50.00 | 51.22 | 48.60 | 57.10 |
| Meeseeks-zh<sub>(acc)</sub> | 33.83 | 35.32 | 42.79 | 41.54 | 35.07 | 34.84 | 43.03 |
| **Mathematical Reasoning** | | | | | | | |
| MATH500<sub>(acc)</sub> | 96.08 | 98.80 | 97.60 | 90.60 | 93.80 | 98.40 | 96.40 |
| AIME24<sub>(avg@10)</sub> | 66.30* | 81.67 | 69.60* | 47.00 | 47.00 | 79.67 | 70.42 |
| AIME25<sub>(avg@10)</sub> | 49.27 | 68.33 | 50.66 | 32.00 | 37.00 | 67.33 | 61.25 |
| BeyondAIME<sub>(avg@10)</sub> | 36.50 | 57.60 | 36.60 | 22.10 | 20.50 | 44.20 | 43.00 |
| **General Reasoning** | | | | | | | |
| GPQA-diamond<sub>(acc)</sub> | 74.90* | 77.43 | 75.76 | 67.68 | 70.71 | 80.30 | 73.23 |
| DROP<sub>(f1)</sub> | 84.19 | 78.57 | 89.04 | 66.94 | 73.06 | 45.03 | 79.06 |
| ZebraLogic<sub>(acc)</sub> | 85.30 | 94.22 | 89.11 | 56.30* | 75.85 | 51.78 | 89.30 |
| GraphWalks-128k<sub>(precision)</sub> | 73.54 | 80.72 | 47.50 | 85.02 | 80.57 | 64.83 | 51.05 |
| **Coding** | | | | | | | |
| LiveCodeBench<sub>(pass@1)</sub> | 56.40* | 46.48 | 46.70 | 39.21 | 45.59 | 39.65 | 48.02 |
| Humaneval+<sub>(pass@1)</sub> | 92.68 | 94.51 | 85.98 | 93.29 | 94.51 | 87.80 | 88.41 |
| MBPP+<sub>(pass@1)</sub> | 79.89 | 79.89 | 81.75 | 79.37 | 80.16 | 76.19 | 79.63 |
| SWE-Bench-Verified<sub>(acc)</sub> | 66.00* | 42.00 | 64.60 | 48.60 | 68.00* | 40.60 | 60.40 |
| TerminalBench<sub>(acc)</sub> | 31.30* | 17.28 | 25.93 | 28.40 | 40.74 | 12.35 | 39.51 |
| **Agentic Tool Use** | | | | | | | |
| τ²-Bench (telecom)<sub>(avg@4)</sub> | 38.50 | 22.50 | 67.50 | 35.20 | 46.20 | 16.50 | 73.68 |
| τ²-Bench (airline)<sub>(avg@4)</sub> | 46.00 | 36.00 | 54.20 | 56.00 | 60.00 | 41.50 | 58.00 |
| τ²-Bench (retail)<sub>(avg@4)</sub> | 64.90 | 70.50 | 70.80 | 74.10 | 80.00 | 64.80 | 71.27 |
| AceBench<sub>(acc)</sub> | 69.70 | 71.10 | 82.20 | 80.10* | 76.20* | 74.50* | 76.10 |
| VitaBench<sub>(avg@4)</sub> | 20.30 | 8.50 | 18.20 | 19.00 | 23.00 | 8.00 | 24.30 |
| **Safety** | | | | | | | |
| Harmful | 82.79 | 80.82 | 53.91 | 56.19 | 66.56 | - | 83.98 |
| Criminal | 87.83 | 89.13 | 77.19 | 81.58 | 87.58 | - | 91.24 |
| Misinformation | 83.17 | 77.76 | 42.68 | 45.49 | 54.91 | - | 81.72 |
| Privacy | 98.80 | 98.80 | 96.39 | 98.80 | 100.00 | - | 93.98 |

Note:
* Values marked with `*` are sourced from other public reports. 
* DeepSeek-V3.1, Qwen3-235B-A22B, Gemini2.5-Flash, and Claude4-Sonnet are evaluated under their non-thinking mode.

## Quick Start

### Chat Template
The details of our chat template are provided in the `tokenizer_config.json` file. Below are some examples.

#### First-Turn

With the following prefix, LongCat-Flash can generate responses corresponding to user queries:

```
[Round 0] USER:{query} ASSISTANT:
```

When a system prompt is specified, the prefix will take the following format:

```
SYSTEM:{system_prompt} [Round 0] USER:{query} ASSISTANT:
```

#### Multi-Turn

In multi-turn scenarios, the prefix is constructed by concatenating the context with the latest user query:
```
SYSTEM:{system_prompt} [Round 0] USER:{query} ASSISTANT:{response}</longcat_s>... [Round N-1] USER:{query} ASSISTANT:{response}</longcat_s> [Round N] USER:{query} ASSISTANT:
```

Here, N denotes the N-th round of user queries, with indexing starting from zero.

#### ToolCall

LongCat-Flash supports tool calling in the following format:
```
{tool_description}

## Messages
SYSTEM:{system_prompt} [Round 0] USER:{query} ASSISTANT:
```



The tool_description is:
```markdown
## Tools
You have access to the following tools: 

### Tool namespace: function

#### Tool name: {func.name}

Description: {func.description}

InputSchema: 
{json.dumps(func.parameters, indent=2)}

**Note**: For each function call, return a json object with function name and arguments within <longcat_tool_call></longcat_tool_call> XML tags as follows:
<longcat_tool_call>
{"name": <function-name>, "arguments": <args-dict>}
</longcat_tool_call>
When multiple functions need to be called simultaneously, each function call should be wrapped in its own <longcat_tool_call> tag and placed consecutively. For example:
<longcat_tool_call>
{"name": <function-name>, "arguments": <args-dict>}
</longcat_tool_call><longcat_tool_call>
{"name": <function-name>, "arguments": <args-dict>}
</longcat_tool_call>
```


## Deployment
We have implemented basic adaptations in both SGLang and vLLM to support the deployment of LongCat-Flash. For comprehensive guidance, please refer to the [Deployment Guide](https://github.com/meituan-longcat/LongCat-Flash-Chat/blob/main/docs/deployment_guide.md) in the LongCat-Flash-Chat repository.

## Chat Website
You can chat with LongCat-Flash on our official website: [https://longcat.ai](https://longcat.ai).

## License Agreement

This repository, including both the model weights and the source code, is released under the **MIT License**. 

Any contributions to this repository are licensed under the MIT License, unless otherwise stated. This license does not grant any rights to use Meituan trademarks or patents. 

For details, see the [LICENSE](./LICENSE) file. 

## Usage Considerations 
This model has not been specifically designed or comprehensively evaluated for every possible downstream application. 

Developers should take into account the known limitations of large language models, including performance variations across different languages, and carefully assess accuracy, safety, and fairness before deploying the model in sensitive or high-risk scenarios. 
It is the responsibility of developers and downstream users to understand and comply with all applicable laws and regulations relevant to their use case, including but not limited to data protection, privacy, and content safety requirements. 

Nothing in this Model Card should be interpreted as altering or restricting the terms of the MIT License under which the model is released. 


## Citation

We kindly encourage citation of our work if you find it useful.

```
@misc{meituan2025longcatflashtechnicalreport, 
    title={LongCat-Flash Technical Report}, 
    author={Meituan LongCat Team}, 
    year={2025}, 
    eprint={2509.01322}, 
    archivePrefix={arXiv}, 
    primaryClass={cs.CL}, 
    url={https://arxiv.org/abs/2509.01322}, 
}
```


## Contact
Please contact us at <a href="mailto:longcat-team@meituan.com">longcat-team@meituan.com</a> or open an issue if you have any questions.

