---
language:
- multilingual
license: mit
task_categories:
- fill-mask
- feature-extraction
tags:
- pretraining
- language-modeling
- encoder
- multilingual
- feature-extraction
---

# mmBERT Pre-training Data P1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2509.06888)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-2%20Models-blue)](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black)](https://github.com/jhu-clsp/mmBERT)

> **Phase 1 of 3**: Diverse multilingual pre-training data mixture (trained for 2.3T tokens) used to train the mmBERT model suite.

NOTE: **this is only P1 of the pre-training data due to HF limits, you need to download and combine all three into one folder**

This dataset contains the pre-training phase data used to train all [mmBERT encoder models](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4). The data is provided in **MDS format** ready for use with [Composer](https://github.com/mosaicml/composer) and the [ModernBERT training repository](https://github.com/answerdotai/ModernBERT).

## 📊 Data Composition

| Data Source | Tokens (B) | Percentage | Description |
|:------------|:-----------|:-----------|:------------|
| FineWeb2 | 1,196.6 | 60.2% | High-quality multilingual web crawl data |
| DCLM | 600.0 | 30.2% | High-quality English web crawl data |
| Starcoder | 100.6 | 5.1% | Code repositories and files |
| Arxiv | 27.8 | 1.4% | Academic preprints |
| StackExchange | 18.6 | 0.9% | Q&A forums |
| Tulu Flan | 15.3 | 0.8% | Instruction-following data |
| Dolmino Math | 11.2 | 0.6% | Mathematical content |
| PeS2o | 8.4 | 0.4% | Scientific papers |
| Wikipedia (MegaWika) | 4.7 | 0.2% | Encyclopedia articles |
| Books | 4.3 | 0.2% | Literature and reference books |
| StackExchange (Dolmino) | 1.4 | 0.1% | Curated Q&A content |
| **Total** | **1,989.0** | **100.0%** | Diverse mixture for foundation training |

## 🌍 Language Coverage

This phase covers **60 languages** plus code, with an inverse temperature sampling schedule starting at τ=0.7. Languages include:
- **High-resource**: English (34.5%), Russian (5.8%), German (4.4%), Spanish (4.5%), French (4.0%), Chinese (5.2%)
- **Mid-resource**: Italian, Portuguese, Japanese, Dutch, Polish, and 45 others
- **Scripts**: Latin, Cyrillic, Arabic, Chinese, Japanese, Thai, and many more

## 🚀 Usage

For pre-training, see the ModernBERT repo: https://github.com/AnswerDotAI/ModernBERT

### Direct Access
Use the script at [this link](https://github.com/JHU-CLSP/mmBERT/blob/main/data/online_streaming.py) to load any section of the dataset on the fly. This will fail if you try to access too many samples though, due to HF rate-limiting. To download the full dataset, use HF Hub's [Snapshot Download](https://huggingface.co/docs/huggingface_hub/v1.0.0.rc6/en/package_reference/file_download#huggingface_hub.snapshot_download).


## 🔗 Related Resources

- **Models**: [mmBERT Model Suite](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
- **Phase 2**: [Mid-training Data](https://huggingface.co/datasets/jhu-clsp/mmbert-midtraining) (600B tokens)
- **Phase 3**: [Decay Phase Data](https://huggingface.co/datasets/jhu-clsp/mmbert-decay) (100B tokens)
- **Checkpoints**: [Training Checkpoints](https://huggingface.co/datasets/jhu-clsp/mmbert-checkpoints)
- **Paper**: [Arxiv link](https://arxiv.org/abs/2509.06888)
- **Hugging Face Paper**: [mmBERT: A Modern Multilingual Encoder with Annealed Language Learning](https://huggingface.co/papers/2509.06888)
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