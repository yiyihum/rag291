---
license: apache-2.0
language:
- zh
- en
pipeline_tag: text-generation
library_name: transformers
---
<div align="center">
<img src="https://github.com/OpenBMB/MiniCPM/blob/main/assets/minicpm_logo.png?raw=true" width="500em" ></img> 
</div>

<p align="center">
<a href="https://github.com/OpenBMB/MiniCPM/" target="_blank">GitHub Repo</a> |
<a href="https://arxiv.org/abs/2506.07900" target="_blank">Technical Report</a> |
<a href="https://mp.weixin.qq.com/s/KIhH2nCURBXuFXAtYRpuXg?poc_token=HBIsUWijxino8oJ5s6HcjcfXFRi0Xj2LJlxPYD9c">Join Us</a>
</p>
<p align="center">
👋 Contact us in <a href="https://discord.gg/3cGQn9b3YM" target="_blank">Discord</a> and <a href="https://github.com/OpenBMB/MiniCPM/blob/main/assets/wechat.jpg" target="_blank">WeChat</a>
</p>

## What's New
- [2025.09.05] **MiniCPM4.1** series are released! This series is a hybrid reasoning model, which can be used in
both deep reasoning mode and non-reasoning mode. 🔥🔥🔥
- [2025.06.06] **MiniCPM4** series are released! This model achieves ultimate efficiency improvements while maintaining optimal performance at the same scale! It can achieve over 5x generation acceleration on typical end-side chips! You can find technical report [here](https://github.com/OpenBMB/MiniCPM/tree/main/report/MiniCPM_4_Technical_Report.pdf).🔥🔥🔥

## MiniCPM4 and MiniCPM4.1 Series
MiniCPM4 and MiniCPM4.1 series are highly efficient large language models (LLMs) designed explicitly for end-side devices, which achieves this efficiency through systematic innovation in four key dimensions: model architecture, training data, training algorithms, and inference systems.
- [MiniCPM4.1-8B](https://huggingface.co/openbmb/MiniCPM4.1-8B): The latest version of MiniCPM4, with 8B parameters, support fusion thinking. 
- [MiniCPM4.1-8B-GPTQ](https://huggingface.co/openbmb/MiniCPM4.1-8B-GPTQ): MiniCPM4.1-8B in GPTQ format.
- [MiniCPM4.1-8B-AutoAWQ](https://huggingface.co/openbmb/MiniCPM4.1-8B-AutoAWQ): MiniCPM4.1-8B in AutoAWQ format.
- [MiniCPM-4.1-8B-Marlin](https://huggingface.co/openbmb/MiniCPM-4.1-8B-Marlin): MiniCPM4.1-8B in Marlin format.
- [MiniCPM4.1-8B-GGUF](https://huggingface.co/openbmb/MiniCPM4.1-8B-GGUF): MiniCPM4.1-8B in GGUF format. (**<-- you are here**)
- [MiniCPM4.1-8B-MLX](https://huggingface.co/openbmb/MiniCPM4.1-8B-MLX): MiniCPM4.1-8B in MLX format.
- [MiniCPM4.1-8B-Eagle3](https://huggingface.co/openbmb/MiniCPM4.1-8B-Eagle3): Eagle3 model for MiniCPM4.1-8B.
- **MiniCPM4 Series**
    <details>
    <summary>Click to expand all MiniCPM4 series models</summary>

    - [**MiniCPM4-8B**](https://huggingface.co/openbmb/MiniCPM4-8B): The flagship model with 8B parameters, trained on 8T tokens
    - [**MiniCPM4-0.5B**](https://huggingface.co/openbmb/MiniCPM4-0.5B): Lightweight version with 0.5B parameters, trained on 1T tokens
    - [**MiniCPM4-8B-Eagle-FRSpec**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-FRSpec): Eagle head for FRSpec, accelerating speculative inference
    - [**MiniCPM4-8B-Eagle-FRSpec-QAT-cpmcu**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-FRSpec-QAT-cpmcu): Eagle head with QAT for FRSpec, integrating speculation and quantization for ultra acceleration
    - [**MiniCPM4-8B-Eagle-vLLM**](https://huggingface.co/openbmb/MiniCPM4-8B-Eagle-vLLM): Eagle head in vLLM format for speculative inference
    - [**MiniCPM4-8B-marlin-Eagle-vLLM**](https://huggingface.co/openbmb/MiniCPM4-8B-marlin-Eagle-vLLM): Quantized Eagle head for vLLM format
    - [**BitCPM4-0.5B**](https://huggingface.co/openbmb/BitCPM4-0.5B): Extreme ternary quantization of MiniCPM4-0.5B, achieving 90% bit width reduction
    - [**BitCPM4-1B**](https://huggingface.co/openbmb/BitCPM4-1B): Extreme ternary quantization of MiniCPM3-1B, achieving 90% bit width reduction
    - [**MiniCPM4-Survey**](https://huggingface.co/openbmb/MiniCPM4-Survey): Generates trustworthy, long-form survey papers from user queries
    - [**MiniCPM4-MCP**](https://huggingface.co/openbmb/MiniCPM4-MCP): Integrates MCP tools to autonomously satisfy user requirements
    </details>

## Introduction
MiniCPM4 and MiniCPM4.1 are extremely efficient edge-side large model that has undergone efficient optimization across four dimensions: model architecture, learning algorithms, training data, and inference systems, achieving ultimate efficiency improvements.

- 🏗️ **Efficient Model Architecture:**
  - InfLLM v2 -- Trainable Sparse Attention Mechanism: Adopts a trainable sparse attention mechanism architecture where each token only needs to compute relevance with less than 5% of tokens in 128K long text processing, significantly reducing computational overhead for long texts

- 🧠 **Efficient Learning Algorithms:**
  - Model Wind Tunnel 2.0 -- Efficient Predictable Scaling: Introduces scaling prediction methods for performance of downstream tasks, enabling more precise model training configuration search
  - BitCPM -- Ultimate Ternary Quantization: Compresses model parameter bit-width to 3 values, achieving 90% extreme model bit-width reduction
  - Efficient Training Engineering Optimization: Adopts FP8 low-precision computing technology combined with Multi-token Prediction training strategy

- 📚 **High-Quality Training Data:**
  - UltraClean -- High-quality Pre-training Data Filtering and Generation: Builds iterative data cleaning strategies based on efficient data verification, open-sourcing high-quality Chinese and English pre-training dataset [UltraFinweb](https://huggingface.co/datasets/openbmb/Ultra-FineWeb)
  - UltraChat v2 -- High-quality Supervised Fine-tuning Data Generation: Constructs large-scale high-quality supervised fine-tuning datasets covering multiple dimensions including knowledge-intensive data, reasoning-intensive data, instruction-following data, long text understanding data, and tool calling data

- ⚡ **Efficient Inference System:**
  - CPM.cu -- Lightweight and Efficient CUDA Inference Framework: Integrates sparse attention, model quantization, and speculative sampling to achieve efficient prefilling and decoding
  - ArkInfer -- Cross-platform Deployment System: Supports efficient deployment across multiple backend environments, providing flexible cross-platform adaptation capabilities

## Usage
### Inference with [llama.cpp](https://github.com/ggml-org/llama.cpp.git)
```bash
# case 1: main-cli
./build/bin/llama-cli -m MiniCPM4.1-8B-Q4_K_M.gguf -p "北京有什么好玩的地方？" -n 1500

# case 2: server
## launch server
./build/bin/llama-server -m MiniCPM4.1-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8080 -c 4096 -fa on &

## send request
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "北京有什么好玩的地方？"}],
    "max_tokens": 1500
  }'
```
