---
license: mit
task_categories:
- fill-mask
tags:
- pretraining
- encoder
- multilingual
---

# mmBERT Mid-training Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2509.06888)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-2%20Models-blue)](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black)](https://github.com/jhu-clsp/mmBERT)

> **Phase 2 of 3**: High-quality mid-training data mixture (600B tokens) with context extension to 8192 tokens.

This dataset contains the mid-training phase data used to train all [mmBERT encoder models](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4). This phase focuses on higher quality data sources and extends the context length from 1024 to 8192 tokens. The data is provided in **MDS format** ready for use with [Composer](https://github.com/mosaicml/composer) and the [ModernBERT training repository](https://github.com/answerdotai/ModernBERT).

## 📊 Data Composition

| Data Source | Tokens (B) | Percentage | Description |
|:------------|:-----------|:-----------|:------------|
| FineWeb2 | 506.7 | 84.3% | High-quality multilingual web crawl data |
| DCLM (Dolmino) | 40.0 | 6.7% | Filtered high-quality English web data |
| Starcoder | 17.2 | 2.9% | Code repositories and files |
| Arxiv | 5.4 | 0.9% | Academic preprints |
| Dolmino Math | 4.3 | 0.7% | Mathematical content |
| Books | 3.9 | 0.7% | Literature and reference books |
| PeS2o | 3.2 | 0.5% | Scientific papers |
| Tulu Flan | 3.1 | 0.5% | Instruction-following data |
| StackExchange | 3.0 | 0.5% | Q&A forums |
| StackExchange (Dolmino) | 2.8 | 0.5% | Curated Q&A content |
| Wikipedia (MegaWika) | 1.2 | 0.2% | Encyclopedia articles |
| **Total** | **600.8** | **100.0%** | High-quality data for context extension |

## 🌍 Language Coverage

This phase covers **110 languages** plus code, with inverse temperature sampling at τ=0.5. Expands from the initial 60 languages to include:
- **Additional mid-resource languages**: Uzbek, Bosnian, Catalan, Albanian, and 46 others
- **Enhanced quality**: Uses filtered FineWeb2-HQ and higher quality DCLM
- **Longer contexts**: Optimized for 8192 token sequences

## ⚙️ Key Features

- **Context Extension**: RoPE base frequency adjusted to 160k for 8192 token support
- **Quality Upgrade**: Switches to filtered, higher-quality versions of datasets
- **Reduced Masking**: Mask rate lowered to 15% (from 30% in pre-training)
- **Language Expansion**: Adds 50 new languages while maintaining data quality

## 🚀 Usage

For mid-training, see the ModernBERT repo: https://github.com/AnswerDotAI/ModernBERT

### Direct Access
Use the script at [this link](https://github.com/JHU-CLSP/mmBERT/blob/main/data/online_streaming.py) to load any section of the dataset on the fly. This will fail if you try to access too many samples though, due to HF rate-limiting. To download the full dataset, use HF Hub's [Snapshot Download](https://huggingface.co/docs/huggingface_hub/v1.0.0.rc6/en/package_reference/file_download#huggingface_hub.snapshot_download).


## 🔗 Related Resources

- **Models**: [mmBERT Model Suite](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
- **Phase 1**: [Pre-training Data](https://huggingface.co/datasets/jhu-clsp/mmbert-pretrain-p1-fineweb2-langs) (2.3T tokens)
- **Phase 3**: [Decay Phase Data](https://huggingface.co/datasets/jhu-clsp/mmbert-decay) (100B tokens)
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