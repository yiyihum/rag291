---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
size_categories:
- 1K<n<10K
pretty_name: SCAR-filtered Tulu v2 Subset
tags:
- data-selection
- instruction-tuning
- LLM
- alignment
- style-consistency
dataset_type: curated
---

# 📘 SCAR-Filtered Instruction-Tuning Subset (10k from Tulu-v2)

This dataset contains 10,000 high-quality instruction–response pairs **filtered from the [allenai/tulu-v2-sft-mixture](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture)** dataset using the **SCAR** data selection method.

SCAR (*Style Consistency-Aware Response Ranking*) is a novel data selection framework accepted to **ACL 2025 (main conference)**. It ranks and filters instruction–response pairs based on **style consistency**, resulting in a more reliable and efficient subset for fine-tuning large language models (LLMs).

📄 **Paper**: [SCAR: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models](https://arxiv.org/abs/2406.10882)  
📍 **Conference**: ACL 2025 main  
🔧 **Selector Package**: [`scar-tool`](https://pypi.org/project/scar-tool/)  
📦 **Model Used**: [`lizhuang144/scar-gte-base`](https://huggingface.co/lizhuang144/scar-gte-base)


## 📊 Dataset Details

- **Source**: [allenai/tulu-v2-sft-mixture](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture)
- **Filtering Method**: [SCAR ranker](https://github.com/zhuang-li/SCAR) (`rank_and_filter` function with `topk=10000`)
- **Size**: 10,000 instruction–response pairs
- **Language**: English
- **Format**: JSONL, each entry contains:
  - `instruction`: the input prompt
  - `response`: the response to the instruction


## ✅ Use Cases

This dataset is ideal for:

- Fine-tuning base LLMs (e.g., Mistral, LLaMA, Phi-2) with a smaller but high-quality instruction set
- Research in data quality, instruction selection, and stylistic alignment
- A cleaner alternative to noisy subsets of Tulu v2


## 🧠 Method Summary

SCAR ranks instruction–response pairs based on a core criterion:

### 🧾 Style Consistency  
Measures whether a response follows the expected style given the instruction.  
This purely stylistic signal is learned via contrastive training without relying on task-specific labels or reward models.

Despite its simplicity, SCAR consistently outperforms random sampling and size-matched subsets across multiple LLM evaluation settings.  
For full benchmarks and details, see the [paper](https://arxiv.org/abs/2406.10882).


## 📈 Results

The SCAR-filtered 10k subset achieves higher performance than the original 320k training data on certain LLMs (e.g., Olmo), demonstrating better alignment with LLM-as-judge preferences on [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval).

| Model | Full Data (320k) | SCAR 10k | SCAR 5k | SCAR 2.5k |
|-------|------------------|----------|---------|-----------|
| Olmo  | 3.86 (L.C. WinRate) | **5.37** | 5.64 | 4.08 |

See the [arXiv paper](https://arxiv.org/abs/2406.10882) for full benchmark results and evaluation setup.


## 🔄 Citation

If you use this dataset, please cite:

```bibtex
@inproceedings{li-etal-2025-scar,
    title = "{SCAR}: Data Selection via Style Consistency-Aware Response Ranking for Efficient Instruction-Tuning of Large Language Models",
    author = "Li, Zhuang  and
      Hua, Yuncheng  and
      Vu, Thuy-Trang  and
      Zhan, Haolan  and
      Qu, Lizhen  and
      Haffari, Gholamreza",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.625/",
    pages = "12756--12790",
    ISBN = "979-8-89176-251-0"
}
```
