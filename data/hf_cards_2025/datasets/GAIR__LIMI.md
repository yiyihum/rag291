---
configs:
- config_name: train
  data_files: limi.json
tags:
- datasets
- sft
- chat
- tool-use
license: other
language:
- en
task_categories:
- text-generation
pretty_name: LIMI (Agentic SFT)
---

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="assets/sii.jpg" alt="SII" width="100px">
  <img src="assets/asi.png" alt="ASI" width="100px">
  
</div>

<div align="center>  
<a href="https://github.com/GAIR-NLP/LIMI" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="assets/teaser.jpg" style="display: inline-block; vertical-align: middle;"/>
</a>
</div>

# LIMI: Less is More for Agency

[![arXiv](https://img.shields.io/badge/arXiv-2509.17567-b31b1b.svg)](https://arxiv.org/pdf/2509.17567)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-green)](https://github.com/GAIR-NLP/LIMI)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)](https://huggingface.co/GAIR/LIMI)

---
To learn more about LIMI, feel free to explore our documentation and resources. Our release consists of the following sections:

This dataset release includes the following sections:

- **Data Fields**: Message schema, tool definitions, and tool-call format.
- **Splits**: Available partitions and counts.
- **Examples**: Representative JSON samples.

# News
- **2025.10.08**: 📝 Released training scripts for Qwen3 dense models (4B/8B/32B) - check out our [training scripts](https://github.com/GAIR-NLP/LIMI/tree/main/scripts/train) to reproduce the results!
- **2025.10.08**: 📊 Our LIMI dataset significantly enhances dense models on **AgencyBench**: Qwen3-4B (4.6% → 8.6%), Qwen3-8B (7.3% → 10.6%), Qwen3-32B (8.4% → 20.5%).
- **2025.10.08**: 🎯 Strong generalization on **out-of-domain benchmarks** while maintaining performance: Qwen3-4B (28.3% → 28.9%), Qwen3-8B (31.2% → 32.0%), Qwen3-32B (35.2% → 37.1%).
- **2025.09.23**: 🚀 LIMI paper is now available on arXiv! Check out our [paper](https://arxiv.org/pdf/2509.17567) for detailed methodology and experimental results.
- **2025.09.23**: 🤗 Released LIMI models on Hugging Face! Both [LIMI](https://huggingface.co/GAIR/LIMI) (355B) and [LIMI-Air](https://huggingface.co/GAIR/LIMI-Air) (106B) are now available.
- **2025.09.23**: 📊 Released the LIMI training dataset with 78 carefully curated samples on [Hugging Face](https://huggingface.co/datasets/GAIR/LIMI).

## Dataset Summary

Curated agentic training data with OpenAI‑style multi‑turn dialogs and tool calls. Focuses on functional completeness, correction over rounds, and spec adherence. For more details, please check the [GAIR-NLP/LIMI](https://github.com/GAIR-NLP/LIMI).

## Data Fields

- `messages` (list): chat messages with roles `system` | `user` | `assistant` | `tool`
- `tools` (optional list): OpenAI function‑call schemas
- `assistant.tool_calls` (optional, list): entries like `{ "type": "function", "function": { "name": str, "arguments": object } }`

## Splits

- `train`: 78 samples (current release)

## Examples

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant tasked with discovering mathematical function structures for scientific systems."},
    {"role": "user", "content": "Modify the equation.py function, considering the physical meaning and relationships of the inputs."}
  ],
  "tools": [
    {"type": "function", "function": {"name": "run_tests", "parameters": {"type": "object", "properties": {"path": {"type": "string"}}}}}
  ]
}
```
## License

- Provided for research; verify final license policy before redistribution

## Citation

```bibtex
@misc{xiao2025limiagency,
      title={LIMI: Less is More for Agency}, 
      author={Yang Xiao and Mohan Jiang and Jie Sun and Keyu Li and Jifan Lin and Yumin Zhuang and Ji Zeng and Shijie Xia and Qishuo Hua and Xuefeng Li and Xiaojie Cai and Tongyu Wang and Yue Zhang and Liming Liu and Xia Wu and Jinlong Hou and Yuan Cheng and Wenjie Li and Xiang Wang and Dequan Wang and Pengfei Liu},
      year={2025},
      eprint={2509.17567},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2509.17567}, 
}
```

