---
license: cc-by-4.0
task_categories:
- text-generation
language:
- en
tags:
- code
- math
- chat
- instruction-following
- synthetic
- nvidia
- nemotron
- splits
- tagged
- untagged
source_datasets:
- nvidia/Llama-Nemotron-Post-Training-Dataset
arxiv: 2505.00949
---

# Nemotron Post-Training Samples with Train/Val/Test Splits

This dataset contains structured train/validation/test splits from the [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset), with both tagged and untagged versions for different training scenarios.

## Attribution

This work is derived from the **Llama-Nemotron-Post-Training-Dataset-v1.1** by NVIDIA Corporation, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Original Dataset**: [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset)
**Original Authors**: NVIDIA Corporation
**Original License**: CC BY 4.0

## Dataset Details

- **Source**: nvidia/Llama-Nemotron-Post-Training-Dataset (SFT config)
- **Sampling Method**: Reservoir sampling for truly random selection
- **Total Samples**: 18000
- **License**: CC BY 4.0 (same as original)

## Splits

- **train**: 10500 samples
- **validation**: 2250 samples
- **test**: 2250 samples
- **untagged_test**: 1500 samples
- **untagged_validation**: 1500 samples

## Usage

Load individual splits:
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits", split="train")
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits", split="validation") 
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits", split="test")
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits", split="untagged_test")
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits", split="untagged_validation")

Load all splits:
- dataset = load_dataset("brandolorian/nemotron-post-training-samples-splits")

## Sample Structure

Each sample contains the original fields from the source dataset plus:
- `domain`: Indicates which domain the sample belongs to (chat/math/code)

Tagged splits have domain tags (#chat, #math, #code) appended to user messages.
Untagged splits preserve the original conversation format.

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), the same license as the original dataset. You are free to:

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit to both the original NVIDIA dataset and this derived work, provide a link to the license, and indicate if changes were made.

## Citations

**Original Dataset Paper**:
@article{nvidia2025nemotron,
  title={Llama-3.1-Nemotron-Ultra-253B: Unleashing the Power of Neural Scaling},
  author={NVIDIA},
  journal={arXiv preprint arXiv:2505.00949},
  year={2025},
  url={https://arxiv.org/abs/2505.00949}
}

**Original Dataset**:
@misc{nvidia-nemotron-dataset,
  title={Llama-Nemotron-Post-Training-Dataset},
  author={NVIDIA Corporation},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset},
  license={CC BY 4.0}
}

**This Derived Dataset**:
@misc{brandolorian-nemotron-post-training-samples-splits,
  title={Nemotron Post-Training Samples with Splits},
  author={Derived from nvidia/Llama-Nemotron-Post-Training-Dataset},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/brandolorian/nemotron-post-training-samples-splits},
  license={CC BY 4.0}
}
