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

