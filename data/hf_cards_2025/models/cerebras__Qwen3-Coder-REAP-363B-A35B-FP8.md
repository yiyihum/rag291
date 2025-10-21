---
language:
- en
library_name: transformers
tags:
- qwen-coder
- MOE
- pruning
- compression
license: apache-2.0
name: cerebras/Qwen3-Coder-REAP-363B-A35B-FP8
description: 'This model was obtained by uniformly pruning 25% of experts in Qwen3-Coder-480B-A35B-Instruct-FP8
  using the REAP method.

  '
readme: 'https://huggingface.co/cerebras/Qwen3-Coder-REAP-363B-A35B-FP8/main/README.md

  '
license_link: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8
---

<p align="center">
  <em>𓌳 <strong>REAP</strong>𓌳  the Experts: Why Pruning Prevails for One-Shot MoE Compression</em><br>
  <img src="https://i.imgur.com/rmzG3gg.png" alt="REAP" width="75%">
</p>

# Qwen3-Coder-REAP-363B-A35B-FP8

## ✨ Highlights

Introducing **Qwen3-Coder-REAP-363B-A35B-FP8**, a **memory-efficient compressed variant** of Qwen3-Coder-480B-A35B-Instruct-FP8 that maintains near-identical performance while being **25% lighter**.

This model was created using **REAP (Router-weighted Expert Activation Pruning)**, a novel expert pruning method that selectively removes redundant experts while preserving the router's independent control over remaining experts. Key features include:

- **Near-Lossless Performance**: Maintains almost identical accuracy on code generation, agentic coding, and function calling tasks compared to the full 480B model
- **25% Memory Reduction**: Compressed from 480B to 363B parameters, significantly lowering deployment costs and memory requirements
- **Preserved Capabilities**: Retains all core functionalities including code generation, agentic workflows, repository-scale understanding, and function calling
- **Drop-in Compatibility**: Works with vanilla vLLM - no source modifications or custom patches required
- **Optimized for Real-World Use**: Particularly effective for resource-constrained environments, local deployments, and academic research
---
## 📋 Model Overview

**Qwen3-Coder-REAP-363B-A35B-FP8** has the following specifications:

- **Base Model**: Qwen3-Coder-480B-A35B-Instruct
- **Compression Method**: REAP (Router-weighted Expert Activation Pruning)
- **Compression Ratio**: 25% expert pruning
- **Type**: Sparse Mixture-of-Experts (SMoE) Causal Language Model
- **Number of Parameters**: 363B total, 35B activated per token
- **Number of Layers**: 62
- **Number of Attention Heads (GQA)**: 96 for Q and 8 for KV
- **Number of Experts**: 120 (uniformly pruned from 160)
- **Number of Activated Experts**: 8 per token
- **Context Length**: 262,144 tokens natively (extendable to 1M with YaRN)
- **Quantization**: FP8
- **License**: Apache 2.0

---

## 📊 Evaluations

| **Benchmark** | Qwen3-Coder-480B-A35B-Instruct-FP8 | [Qwen3-Coder-REAP-363B-A35B-FP8](https://huggingface.co/cerebras/Qwen3-Coder-REAP-363B-A35B-FP8) | [Qwen3-Coder-REAP-246B-A35B-FP8](https://huggingface.co/cerebras/Qwen3-Coder-REAP-246B-A35B-FP8) |
| :------------- | :-------------------------------: | :------------------------: | :------------: |
| **Compression** | — | 25% | 50% |
| **HumanEval** | 95.1 | 95.7 | 93.9 |
| **HumanEval+** | 89.0 | 89.0 | 87.2 |
| **MBPP** | 92.3 | 91.7 | 91.0 |
| **MBPP+** | 79.1 | 77.2 | 77.2 |
| **LiveCodeBench** (25.01 - 25.05) | 43.1 | 41.6 | 41.5 |
| **SWE-Bench-Verified** (w/ mini-swe-agent) | 54.0 | 54.0 | 52.2 |
| **BFCL-v3 (Non-Live)** | 86.6 | 87.8 | 84.9 |
| **BFCL-v3 (Live)** | 82.5 | 82.3 | 80.1 |
| **BFCL-v3 (Multi-Turn)** | 38.0 | 39.2 | 37.1 |
| **BFCL-v3 (Overall)** | 69.0 | 69.8 | 67.4 |
| **𝜏²-bench (Airline)** | 46.0 | 48.7 | 44.7 |
| **𝜏²-bench (Retail)** | 64.3 | 66.1 | 63.2 |
| **𝜏²-bench (Telecom)** | 50.0 | 52.9 | 47.1 |
| **TerminalBench 0.1.1** (Terminus agent) | 30.5 | 30.5 | 30.0 |

🟩 *This checkpoint maintains almost identical performance while being 25% lighter.*

For more details on the evaluation setup, refer to the [REAP arXiv preprint](https://arxiv.org/abs/2510.13999).

---

## 🚀 Deployment

You can deploy the model directly using the **latest vLLM** (v0.11.0), no source modifications or custom patches required.

```bash
vllm serve cerebras/Qwen3-Coder-REAP-363B-A35B-FP8 \
    --tensor-parallel-size 8 \
    --tool-call-parser qwen3_coder \
    --enable-auto-tool-choice \
    --enable-expert-parallel
```

If you encounter insufficient memory when running this model, you might need to set a lower value for `--max-num-seqs` flag (e.g. set to 64).


## 🧩 Model Creation

This checkpoint was created by applying the **REAP (Router-weighted Expert Activation Pruning)** method uniformly across all Mixture-of-Experts (MoE) blocks of **Qwen3-Coder-480B-A35B-Instruct**, with a **25% pruning rate**.

### How REAP Works

REAP selects experts to prune based on a novel **saliency criterion** that considers both:
- **Router gate values**: How frequently and strongly the router activates each expert
- **Expert activation norms**: The magnitude of each expert's output contributions

This dual consideration ensures that experts contributing minimally to the layer's output are pruned, while preserving those that play critical roles in the model's computations.

### Key Advantages

- **One-Shot Compression**: No fine-tuning required after pruning - the model is immediately ready for deployment
- **Preserved Router Control**: Unlike expert merging methods, REAP maintains the router's independent, input-dependent control over remaining experts, avoiding "functional subspace collapse"
- **Generative Task Superiority**: REAP significantly outperforms expert merging approaches on generative benchmarks (code generation, creative writing, mathematical reasoning) while maintaining competitive performance on discriminative tasks

### Calibration

The model was calibrated using a diverse mixture of domain-specific datasets including:
- Code generation samples ([evol-codealpaca](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1))
- Function calling examples ([xlam-function-calling](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k))
- Agentic multi-turn trajectories ([SWE-smith-trajectories](https://huggingface.co/datasets/SWE-bench/SWE-smith-trajectories))

📚 For more details, refer to the following resources:

- [🧾 arXiv Preprint](https://arxiv.org/abs/2510.13999)
- [🧾 REAP Blog](https://www.cerebras.ai/blog/reap)
- [💻 REAP Codebase (GitHub)](https://github.com/CerebrasResearch/reap)

---

## ⚖️ License

This model is derived from
**[`Qwen/Qwen3-Coder-480B-A35B-Instruct`](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)**
and distributed under the **Apache 2.0 License**.

🔗 [View License File →](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct/blob/main/LICENSE)

---

## 🧾 Citation

If you use this checkpoint, please cite the REAP paper:

```bibtex
@article{lasby-reap,
  title={REAP the Experts: Why Pruning Prevails for One-Shot MoE compression},
  author={Lasby, Mike and Lazarevich, Ivan and Sinnadurai, Nish and Lie, Sean and Ioannou, Yani and Thangarasa, Vithursan},
  journal={arXiv preprint arXiv:2510.13999},
  year={2025}
}
```