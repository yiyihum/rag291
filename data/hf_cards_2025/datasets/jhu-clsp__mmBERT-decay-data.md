---
license: mit
task_categories:
- fill-mask
tags:
- pretraining
- encoder
- multilingual
---

# MMBERT Decay Phase Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2509.06888)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-2%20Models-blue)](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black)](https://github.com/jhu-clsp/mmBERT)

> **Phase 3 of 3**: Annealed language learning decay phase (100B tokens) with massive multilingual expansion to 1833 languages.

## 📊 Data Composition
NOTE: there are multiple decay data mixtures: this mixture described below is the Decay-Cont mixture. However, the data in this repository is the Decay-Eng. If you are interested in the others, please let me know so I can prioritize it.

| Data Source | Tokens (B) | Percentage | Description |
|:------------|:-----------|:-----------|:------------|
| FineWeb2 | 78.5 | 76.0% | High-quality multilingual web crawl data |
| Wikipedia (MegaWika) | 9.5 | 9.2% | Encyclopedia articles (1833 languages) |
| Arxiv | 3.3 | 3.2% | Academic preprints |
| Textbooks (ProLong) | 3.1 | 3.0% | Educational content |
| Code (ProLong) | 2.8 | 2.7% | Code repositories and files |
| Books | 2.2 | 2.1% | Literature and reference books |
| DCLM (Dolmino) | 2.0 | 2.0% | High-quality English web data |
| Tulu Flan | 1.0 | 1.0% | Instruction-following data |
| Starcoder | 0.5 | 0.5% | Code repositories |
| Dolmino Math | 0.5 | 0.5% | Mathematical content |
| **Total** | **103.3** | **100.0%** | Optimized for rapid language acquisition |

## 🌍 Massive Language Coverage

This phase dramatically expands language coverage to **1833 languages**, implementing the novel **Cascading Annealed Language Learning (ALL)** approach:

- **Temperature Schedule**: τ=0.3 (most uniform sampling)
- **Low-resource Focus**: Includes 1723 new languages with minimal data
- **Rapid Learning**: Demonstrates 68% performance improvement on Tigray and 26% on Faroese
- **Script Diversity**: Covers virtually all writing systems in FineWeb2

### Key Innovation: Annealed Language Learning

Rather than training on all languages simultaneously, MMBERT uses a cascading approach:
1. **Phase 1**: 60 high-resource languages (τ=0.7)
2. **Phase 2**: 110 languages including mid-resource (τ=0.5) 
3. **Phase 3**: 1833 languages with focus on low-resource (τ=0.3)

This enables rapid learning of new languages while maintaining performance on high-resource ones.

## ⚙️ Key Features

- **Ultra-low Masking**: 5% mask rate for optimal learning efficiency
- **Model Merging**: Three decay variants (English-focused, 110-lang, 1833-lang) merged using TIES. This is the English focused version.
- **Quality Focus**: Emphasizes highest-quality data sources

## 🚀 Usage

For decay phase training, see the ModernBERT repo: https://github.com/AnswerDotAI/ModernBERT

### Direct Access
Use the script at [this link](https://github.com/JHU-CLSP/mmBERT/blob/main/data/online_streaming.py) to load any section of the dataset on the fly. This will fail if you try to access too many samples though, due to HF rate-limiting. To download the full dataset, use HF Hub's [Snapshot Download](https://huggingface.co/docs/huggingface_hub/v1.0.0.rc6/en/package_reference/file_download#huggingface_hub.snapshot_download).

## 🎯 Performance Impact

The decay phase demonstrates remarkable efficiency in low-resource language learning:
- **Tigray (TiQuAD)**: 68% improvement (12.1 F1 points) from including the language
- **Faroese (FoQA)**: 26% improvement (15.4 F1 points) 
- **SOTA Performance**: Can even outperforms GPT-4o, Gemini 2.5 Pro
- **Rapid Acquisition**: Significant gains with only 100B tokens of exposure

## 🔗 Related Resources

- **Models**: [mmBERT Model Suite](https://huggingface.co/collections/jhu-clsp/mmbert-a-modern-multilingual-encoder-68b725831d7c6e3acc435ed4)
- **Phase 1**: [Pre-training Data](https://huggingface.co/datasets/jhu-clsp/mmbert-pretrain-p1-fineweb2-langs) (2.3T tokens)
- **Phase 2**: [Mid-training Data](https://huggingface.co/datasets/jhu-clsp/mmbert-midtraining) (600B tokens)
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