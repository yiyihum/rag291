---
language:
- en
license: mit
task_categories:
- text-generation
library_name: streaming
tags:
- pretraining
- language-modeling
- encoder-decoder
---

# Ettin Decay Phase Data

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2507.11412)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-12%20Models-blue)](https://huggingface.co/jhu-clsp)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black)](https://github.com/jhu-clsp/ettin-encoder-vs-decoder)

> **Phase 3 of 3**: Premium data sources for final training phase (100B tokens) following the ProLong recipe.

This dataset contains the decay phase data used to train all [Ettin encoder and decoder models](https://huggingface.co/jhu-clsp). This final phase uses **premium data sources** with emphasis on **long-form content** and **educational materials**. The data is provided in **MDS format** ready for use with [Composer](https://github.com/mosaicml/composer) and the [ModernBERT training repository](https://github.com/answerdotai/ModernBERT).

## Abstract

The large language model (LLM) community focuses almost exclusively on decoder-only language models, since they are easier to use for text generation. However, a large subset of the community still uses encoder-only models for tasks such as classification or retrieval. Previous work has attempted to compare these architectures, but is forced to make comparisons with models that have different numbers of parameters, training techniques, and datasets. We introduce the SOTA open-data Ettin suite of models: paired encoder-only and decoder-only models ranging from 17 million parameters to 1 billion, trained on up to 2 trillion tokens. Using the same recipe for both encoder-only and decoder-only models produces SOTA recipes in both categories for their respective sizes, beating ModernBERT as an encoder and Llama 3.2 and SmolLM2 as decoders. Like previous work, we find that encoder-only models excel at classification and retrieval tasks while decoders excel at generative tasks. However, we show that adapting a decoder model to encoder tasks (and vice versa) through continued training is subpar compared to using only the reverse objective (i.e. a 400M encoder outperforms a 1B decoder on MNLI, and vice versa for generative tasks). We open-source all artifacts of this study including training data, training order segmented by checkpoint, and 200+ checkpoints to allow future work to analyze or extend all aspects of training.

## 📊 Data Composition

| Data Source | Tokens (B) | Percentage | Description |
|:------------|:-----------|:-----------|:------------|
| DCLM (Dolmino) | 26.0 | 31.9% | Highest-quality web crawl data |
| Code Repos | 20.2 | 24.7% | Premium code repositories |
| Books | 10.5 | 12.9% | Literature and reference books |
| Math (Dolmino) | 5.0 | 6.1% | Mathematical content (premium) |
| StackExchange (Dolmino) | 4.0 | 4.9% | High-quality Q&A content |
| Tulu Flan | 4.1 | 5.0% | Instruction-following data |
| Arxiv | 3.0 | 3.7% | Academic preprints |
| Wikipedia | 3.0 | 3.7% | Encyclopedia articles |
| Textbooks | 0.5 | 0.6% | Educational textbooks |
| **Total** | **81.6** | **100.0%** | Premium quality mixture |

## 🎯 Key Features of Decay Phase

### Training Characteristics  
- **Aggressive LR Decay**: Learning rate decays to 0.02 of peak
- **Long Context**: Maintains 8K token sequences from mid-training
- **Lower Masking**: 5% masking ratio (vs 30% earlier) for encoders
- **Quality Over Quantity**: Focus on premium sources rather than scale

## 🚀 Usage

Please see the ModernBERT repo: https://github.com/AnswerDotAI/ModernBERT

### Direct Access

```python
from streaming import StreamingDataset

# Load the streaming dataset
dataset = StreamingDataset(
    remote='https://huggingface.co/datasets/jhu-clsp/ettin-decay-data',
    local='/tmp/ettin-decay-data',
    shuffle=True
)

# Access premium quality samples
for sample in dataset:
    text = sample['text']  # High-quality, long-form content
    # Process your data...
```

## 📁 Structure

Each folder contains premium quality data sources in MDS format:
- `arxiv/` - Academic papers from ArXiv
- `books/` - Literature and reference books (expanded)
- `books_2/` - Additional book collections  
- `code_repos/` - Premium code repositories
- `dclm_dolmino/` - Highest-quality filtered web data
- `math_dolmino/` - Premium mathematical content
- `stackexchange_dolmino/` - Top-quality Q&A content
- `stackexchange_dolmino_dup/` - Additional curated Q&A
- `stackexchange_dolmino_dup_2/` - Extra Q&A collections
- `textbooks/` - Educational textbook content
- `textbooks_2/` - Additional textbook collections
- `tulu_flan/` - Instruction-following examples
- `wikipedia/` - Wikipedia articles

## 💡 Usage in Cross-Objective Training

This decay phase data is also used for **cross-objective training** experiments:
- **Decoder → Encoder**: Training decoders with MLM on this premium data
- **Encoder → Decoder**: Training encoders with CLM on this premium data
- **Extended Training**: 50B additional tokens for cross-objective experiments

## 🔗 Related Resources

- **Models**: [Ettin Model Suite](https://huggingface.co/jhu-clsp) (17M-1B parameters)
- **Phase 1**: [Pre-training Data](https://huggingface.co/datasets/jhu-clsp/ettin-pretraining-data) (1.7T tokens)  
- **Phase 2**: [Mid-training Data](https://huggingface.co/datasets/jhu-clsp/ettin-extension-data) (250B tokens)
- **Training Order**: [Batch-level Data Order](https://huggingface.co/datasets/jhu-clsp/ettin-data-order)
- **Paper**: [Arxiv link](https://arxiv.org/abs/2507.11412)
- **Code**: [GitHub Repository](https://github.com/jhu-clsp/ettin-encoder-vs-decoder)

## Citation

```bibtex
@misc{weller2025seqvsseqopen,
      title={Seq vs Seq: An Open Suite of Paired Encoders and Decoders}, 
      author={Orion Weller and Kathryn Ricci and Marc Marone and Antoine Chaffin and Dawn Lawrie and Benjamin Van Durme},
      year={2025},
      eprint={2507.11412},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.11412}, 
}
```