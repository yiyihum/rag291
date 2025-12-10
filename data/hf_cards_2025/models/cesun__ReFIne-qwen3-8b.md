---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
---

# ReFIne: A Framework for Trustworthy Large Reasoning Models with Reliability, Faithfulness, and Interpretability

This repository contains the `ReFIne-qwen3-8b` model, which is part of the work presented in the paper [ReFIne: A Framework for Trustworthy Large Reasoning Models with Reliability, Faithfulness, and Interpretability](https://huggingface.co/papers/2510.09062).

ReFIne is a new training framework designed to enhance Large Reasoning Models (LRMs) by promoting interpretability, faithfulness, and reliability in their reasoning processes. It integrates supervised fine-tuning with GRPO to encourage models to:
*   **Improve Interpretability**: By producing structured, tag-based traces with high-level planning that are easier for humans to follow.
*   **Enhance Faithfulness**: By explicitly disclosing the decisive information guiding each solution, with consistent cross-section references.
*   **Promote Reliability**: By providing self-assessments of both the derivation's soundness and the confidence of the final answer.

This framework has been applied to Qwen3 models at multiple scales and evaluated across mathematical benchmarks, demonstrating significant improvements in these trustworthiness dimensions.

<p align="center">
  <img src="https://github.com/Trustworthy-ML-Lab/Training_Trustworthy_LRM_with_Refine/raw/main/fig/overview.png" width="80%" alt="Overview of the ReFIne framework" />
  <br>
  <em>Overview of ReFIne framework, which enhances LRMs in terms of reliability, faithfulness, and interpretability.</em>
</p>

## Code and More Information

For detailed installation instructions, training procedures, evaluation scripts, and more information, please refer to the official GitHub repository:
[https://github.com/Trustworthy-ML-Lab/Training_Trustworthy_LRM_with_Refine](https://github.com/Trustworthy-ML-Lab/Training_Trustworthy_LRM_with_Refine)

## Citation

If you find this work useful for your research, please cite the paper:

```bibtex
@article{ReFIne,
   title={ReFIne: A Framework for Trustworthy Large Reasoning Models with Reliability, Faithfulness, and Interpretability},
   author={Sun, Chung-En and Yan, Ge and Kulkarni, Akshay and Weng, Tsui-Wei},
   journal={arXiv},
   year={2025}
}
```