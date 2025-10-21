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
name: cerebras/Qwen3-Coder-REAP-25B-A3B
description: 'This model was obtained by uniformly pruning 20% of experts in Qwen3-Coder-30B-A3B-Instruct
  using the REAP method.

  '
readme: 'https://huggingface.co/cerebras/Qwen3-Coder-REAP-25B-A3B/main/README.md

  '
license_link: https://huggingface.co/cerebras/Qwen3-Coder-REAP-25B-A3B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-Coder-30B-A3B-Instruct
---

<p align="center">
  <em>𓌳 <strong>REAP</strong>𓌳  the Experts: Why Pruning Prevails for One-Shot MoE Compression</em><br>
  <img src="https://i.imgur.com/rmzG3gg.png" alt="REAP" width="75%">
</p>

# Qwen3-Coder-REAP-25B-A3B

## ✨ Highlights

Introducing **Qwen3-Coder-REAP-25B-A3B**, a **memory-efficient compressed variant** of Qwen3-Coder-30B-A3B-Instruct that maintains near-identical performance while being **20% lighter**.

This model was created using **REAP (Router-weighted Expert Activation Pruning)**, a novel expert pruning method that selectively removes redundant experts while preserving the router's independent control over remaining experts. Key features include:

- **Near-Lossless Performance**: Maintains almost identical accuracy on code generation, agentic coding, and function calling tasks compared to the full 480B model
- **20% Memory Reduction**: Compressed from 30B to 25B parameters, significantly lowering deployment costs and memory requirements
- **Preserved Capabilities**: Retains all core functionalities including code generation, agentic workflows, repository-scale understanding, and function calling
- **Drop-in Compatibility**: Works with vanilla vLLM - no source modifications or custom patches required
- **Optimized for Real-World Use**: Particularly effective for resource-constrained environments, local deployments, and academic research
---
## 📋 Model Overview

**Qwen3-Coder-REAP-25B-A3B** has the following specifications:

- **Base Model**: Qwen3-Coder-30B-A3B-Instruct
- **Compression Method**: REAP (Router-weighted Expert Activation Pruning)
- **Compression Ratio**: 20% expert pruning
- **Type**: Sparse Mixture-of-Experts (SMoE) Causal Language Model
- **Number of Parameters**: 25B total, 3B activated per token
- **Number of Layers**: 48
- **Number of Attention Heads (GQA)**: 32 for Q and 4 for KV
- **Number of Experts**: 103 (uniformly pruned from 128)
- **Number of Activated Experts**: 8 per token
- **Context Length**: 262,144 tokens natively (extendable to 1M with YaRN)
- **License**: Apache 2.0

---

## 📊 Evaluations

| **Benchmark** | Qwen3-Coder-30B-A3B-Instruct | [Qwen3-Coder-REAP-25B-A3B](https://huggingface.co/cerebras/Qwen3-Coder-REAP-25B-A3B) |
| :------------- | :-------------------------------: | :------------------------: |
| **Compression** | — | 20% |
| **HumanEval** | 92.1 | 94.5 |
| **HumanEval+** | 87.8 | 89.0 |
| **MBPP** | 87.6 | 87.3 |
| **MBPP+** | 73.5 | 72.8 |
| **LiveCodeBench** (25.01 - 25.05) | 35.2 | 35.2 |
| **BFCL-v3 (Non-Live)** | 83.9 | 82.2 |
| **BFCL-v3 (Live)** | 76.2 | 74.0 |
| **BFCL-v3 (Multi-Turn)** | 29.6 | 30.5 |
| **BFCL-v3 (Overall)** | 63.2 | 62.2 |
| **𝜏²-bench (Airline)** | 39.3 | 40.7 |
| **𝜏²-bench (Retail)** | 62.6 | 62.0 |
| **𝜏²-bench (Telecom)** | 33.6 | 32.2 |


🟩 *This checkpoint maintains almost identical performance while being 20% lighter.*

For more details on the evaluation setup, refer to the [REAP arXiv preprint](https://arxiv.org/abs/2510.13999).

---

## 🚀 Deployment

You can deploy the model directly using the **latest vLLM** (v0.11.0), no source modifications or custom patches required.

```bash
vllm serve cerebras/Qwen3-Coder-REAP-25B-A3B \
    --tensor-parallel-size 8 \
    --tool-call-parser qwen3_coder \
    --enable-auto-tool-choice \
    --enable-expert-parallel
```

If you encounter insufficient memory when running this model, you might need to set a lower value for `--max-num-seqs` flag (e.g. set to 64).


## 🧩 Model Creation

This checkpoint was created by applying the **REAP (Router-weighted Expert Activation Pruning)** method uniformly across all Mixture-of-Experts (MoE) blocks of **Qwen3-Coder-30B-A3B-Instruct**, with a **20% pruning rate**.

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
- Function calling examples ([xlam-function-calling](Salesforce/xlam-function-calling-60k))
- Agentic multi-turn trajectories ([SWE-smith-trajectories](https://huggingface.co/datasets/SWE-bench/SWE-smith-trajectories))

📚 For more details, refer to the following resources:

- [🧾 arXiv Preprint](https://arxiv.org/abs/2510.13999)
- [🧾 REAP Blog](https://www.cerebras.ai/blog/reap-one-shot-pruning-for-trillion-parameter-mixture-of-experts-models)
- [💻 REAP Codebase (GitHub)](https://github.com/CerebrasResearch/reap)

---

## ⚖️ License

This model is derived from
**[`Qwen3-Coder-30B-A3B-Instruct`](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)**
and distributed under the **Apache 2.0 License**.

🔗 [View License File →](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/main/LICENSE)

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