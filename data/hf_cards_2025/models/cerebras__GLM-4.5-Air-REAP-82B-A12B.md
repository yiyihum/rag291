---
language:
- en
library_name: transformers
tags:
- glm
- MOE
- pruning
- compression
license: mit
name: cerebras/GLM-4.5-Air-REAP-82B-A12B
description: 'This model was obtained by uniformly pruning 25% of experts in GLM-4.5-Air
  using the REAP method.

  '
readme: 'https://huggingface.co/cerebras/GLM-4.5-Air-REAP-82B-A12B/main/README.md

  '
license_link: https://huggingface.co/zai-org/GLM-4.5-Air/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- zai-org/GLM-4.5-Air
---

<p align="center">
  <em>𓌳 <strong>REAP</strong>𓌳  the Experts: Why Pruning Prevails for One-Shot MoE Compression</em><br>
  <img src="https://i.imgur.com/rmzG3gg.png" alt="REAP" width="75%">
</p>

# GLM-4.5-Air-REAP-82B-A12B

## ✨ Highlights

Introducing **GLM-4.5-Air-REAP-82B-A12B**, a **memory-efficient compressed variant** of GLM-4.5-Air that maintains near-identical performance while being **25% lighter**.

This model was created using **REAP (Router-weighted Expert Activation Pruning)**, a novel expert pruning method that selectively removes redundant experts while preserving the router's independent control over remaining experts. Key features include:

- **Near-Lossless Performance**: Maintains almost identical accuracy on code generation, agentic coding, and function calling tasks compared to the full 106B model
- **25% Memory Reduction**: Compressed from 106B to 82B parameters, significantly lowering deployment costs and memory requirements
- **Preserved Capabilities**: Retains all core functionalities including code generation, agentic workflows, repository-scale understanding, and function calling
- **Drop-in Compatibility**: Works with vanilla vLLM - no source modifications or custom patches required
- **Optimized for Real-World Use**: Particularly effective for resource-constrained environments, local deployments, and academic research
---
## 📋 Model Overview

**GLM-4.5-Air-REAP-82B-A12B** has the following specifications:

- **Base Model**: GLM-4.5-Air
- **Compression Method**: REAP (Router-weighted Expert Activation Pruning)
- **Compression Ratio**: 25% expert pruning
- **Type**: Sparse Mixture-of-Experts (SMoE) Causal Language Model
- **Number of Parameters**: 82B total, 12B activated per token
- **Number of Layers**: 46
- **Number of Attention Heads (GQA)**: 96 for Q and 8 for KV
- **Number of Experts**: 96 (uniformly pruned from 128)
- **Number of Activated Experts**: 8 per token
- **Context Length**: 131,072 tokens
- **License**: MIT

---

## 📊 Evaluations

<table>
  <thead>
    <tr>
      <th align="left">Benchmark</th>
      <th align="center">GLM-4.5-Air</th>
      <th align="center"><a href="https://huggingface.co/cerebras/GLM-4.5-Air-REAP-82B-A12B">GLM-4.5-Air-REAP-82B-A12B</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Compression</strong></td>
      <td align="center">—</td>
      <td align="center">25%</td>
    </tr>
    <tr>
      <td colspan="3" align="center"><strong>Coding</strong></td>
    </tr>
    <tr>
      <td><strong>HumanEval</strong></td>
      <td align="center">92.7</td>
      <td align="center">89.6</td>
    </tr>
    <tr>
      <td><strong>HumanEval+</strong></td>
      <td align="center">86.0</td>
      <td align="center">84.8</td>
    </tr>
    <tr>
      <td><strong>MBPP</strong></td>
      <td align="center">86.2</td>
      <td align="center">84.4</td>
    </tr>
    <tr>
      <td><strong>MBPP+</strong></td>
      <td align="center">69.8</td>
      <td align="center">69.6</td>
    </tr>
    <tr>
      <td colspan="3" align="center"><strong>Reasoning</strong></td>
    </tr>
    <tr>
      <td><strong>LiveCodeBench</strong> (25.01 - 25.05, thinking)</td>
      <td align="center">39.6</td>
      <td align="center">42.9</td>
    </tr>
    <tr>
      <td><strong>GPQA diamond</strong> (thinking)</td>
      <td align="center">65.2</td>
      <td align="center">65.2</td>
    </tr>
    <tr>
      <td><strong>AIME24</strong> (thinking)</td>
      <td align="center">83.3</td>
      <td align="center">80.0</td>
    </tr>
    <tr>
      <td><strong>MATH-500</strong> (thinking)</td>
      <td align="center">94.8</td>
      <td align="center">94.8</td>
    </tr>
    <tr>
      <td colspan="3" align="center"><strong>Tool Calling</strong></td>
    </tr>
    <tr>
      <td><strong>BFCL-v3</strong></td>
      <td align="center">73.4</td>
      <td align="center">71.8</td>
    </tr>
    <tr>
      <td><strong>BFCL-v3</strong> (thinking)</td>
      <td align="center">76.8</td>
      <td align="center">76.3</td>
    </tr>
    <tr>
      <td><strong>𝜏²-bench</strong> (airline)</td>
      <td align="center">63.3</td>
      <td align="center">64.0</td>
    </tr>
    <tr>
      <td><strong>𝜏²-bench</strong> (retail)</td>
      <td align="center">72.8</td>
      <td align="center">75.1</td>
    </tr>
    <tr>
      <td><strong>𝜏²-bench</strong> (telecom)</td>
      <td align="center">28.4</td>
      <td align="center">30.7</td>
    </tr>
    <tr>
      <td><strong>𝜏²-bench</strong> (telecom, thinking)</td>
      <td align="center">27.2</td>
      <td align="center">26.9</td>
    </tr>
  </tbody>
</table>

🟩 *This checkpoint maintains almost identical performance while being 25% lighter.*

For more details on the evaluation setup, refer to the [REAP arXiv preprint](https://arxiv.org/abs/2510.13999).

---

## 🚀 Deployment

You can deploy the model directly using the **latest vLLM** (v0.11.0), no source modifications or custom patches required.

```bash
vllm serve cerebras/GLM-4.5-Air-REAP-82B-A12B \
    --tensor-parallel-size 8 \
    --tool-call-parser glm45 \
    --enable-auto-tool-choice \
    --enable-expert-parallel
```

If you encounter insufficient memory when running this model, you might need to set a lower value for `--max-num-seqs` flag (e.g. set to 64).


## 🧩 Model Creation

This checkpoint was created by applying the **REAP (Router-weighted Expert Activation Pruning)** method uniformly across all Mixture-of-Experts (MoE) blocks of **GLM-4.5-Air**, with a **25% pruning rate**.

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
**[`zai-org/GLM-4.5-Air`](https://huggingface.co/zai-org/GLM-4.5-Air)**
and distributed under the **MIT license**.

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