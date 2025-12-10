---
license: mit
task_categories:
- fill-mask
tags:
- pretraining
- encoder
- multilingual
---

# mmBERT Training Data (Ready-to-Use)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2509.06888)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-2%20Models-blue)](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black)](https://github.com/jhu-clsp/mmBERT)

> **Complete Training Dataset**: Pre-randomized and ready-to-use multilingual training data (3T tokens) for encoder model pre-training.

This dataset is part of the complete, pre-shuffled training data used to train the [mmBERT encoder models](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4). Unlike the individual phase datasets, this version is ready for immediate use but **the mixture cannot be modified easily**. The data is provided in **decompressed MDS format** ready for use with [ModernBERT's Composer](https://github.com/mosaicml/composer) and the [ModernBERT training repository](https://github.com/answerdotai/ModernBERT).

## Licensing & Attribution

This dataset aggregates multiple open-source datasets under permissive licenses. See individual source datasets for specific attribution requirements.

## Related Resources

- **Models**: [mmBERT Model Suite](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
- **Individual Phases**: [Pre-training](https://huggingface.co/datasets/jhu-clsp/mmbert-pretrain-p1-fineweb2-langs) | [Mid-training](https://huggingface.co/datasets/jhu-clsp/mmbert-midtraining) | [Decay](https://huggingface.co/datasets/jhu-clsp/mmbert-decay)
- **Checkpoints**: [Training Checkpoints](https://huggingface.co/datasets/jhu-clsp/mmbert-checkpoints)
- **Paper**: [Arxiv link](https://arxiv.org/abs/2509.06888)
- **Code**: [GitHub Repository](https://github.com/jhu-clsp/mmBERT)

## Citation

```bibtex
@misc{marone2025mmbertmodernmultilingualencoder,
      title={mmBERT: A Modern Multilingual Encoder with Annealed Language Learning}, 
      author={Marc Marone and Orion Weller and William Fleshman and Eugene Yang and Dawn Lawrie and Benjamin Van Durme},
      year={2025},
      eprint={2509.06888},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.06888}, 
}
```