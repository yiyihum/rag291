---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen3-1.7B
pipeline_tag: text-generation
library_name: transformers
---

# Lucy: Edgerunning Agentic Web Search on Mobile with a 1.7B model.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/menloresearch/deep-research) 
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://opensource.org/licenses/Apache-2.0)

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/PA6JCiYLPJX_WFO42ClTd.jpeg" width="300" alt="Lucy-128k">
</div>

**Authors:** [Alan Dao](https://scholar.google.com/citations?user=eGWws2UAAAAJ&hl=en), [Bach Vu Dinh](https://scholar.google.com/citations?user=7Lr6hdoAAAAJ&hl=vi), [Alex Nguyen](https://github.com/nguyenhoangthuan99), [Norapat Buppodom](https://scholar.google.com/citations?user=utfEThsAAAAJ&hl=th&authuser=1)


![image/gif](lucy_demo.gif)


## Overview

Lucy is a compact but capable 1.7B model focused on agentic web search and lightweight browsing. Built on [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B), Lucy inherits deep research capabilities from larger models while being optimized to run efficiently on mobile devices, even with CPU-only configurations.

We achieved this through machine-generated task vectors that optimize thinking processes, smooth reward functions across multiple categories, and pure reinforcement learning without any supervised fine-tuning.

## What Lucy Excels At

- **🔍 Strong Agentic Search**: Powered by MCP-enabled tools (e.g., Serper with Google Search)
- **🌐 Basic Browsing Capabilities**: Through Crawl4AI (MCP server to be released), Serper,...
- **📱 Mobile-Optimized**: Lightweight enough to run on CPU or mobile devices with decent speed
- **🎯 Focused Reasoning**: Machine-generated task vectors optimize thinking processes for search tasks

## Evaluation
Following the same MCP benchmark methodology used for [Jan-Nano](https://huggingface.co/Menlo/Jan-nano) and [Jan-Nano-128k](https://huggingface.co/Menlo/Jan-nano-128k), Lucy demonstrates impressive performance despite being only a 1.7B model, achieving higher accuracy than DeepSeek-v3 on [SimpleQA](https://openai.com/index/introducing-simpleqa/).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/lG2FqLCWXq1N8lh7wlJgW.png)

## 🖥️ How to Run Locally

Lucy can be deployed using various methods including vLLM, llama.cpp, or through local applications like Jan, LMStudio, and other compatible inference engines. The model supports integration with search APIs and web browsing tools through the MCP.

### Deployment

Deploy using VLLM:
```bash
vllm serve Menlo/Lucy-128k \
    --host 0.0.0.0 \
    --port 1234 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes \
    --rope-scaling '{"rope_type":"yarn","factor":3.2,"original_max_position_embeddings":40960}' --max-model-len 131072
```

Or `llama-server` from `llama.cpp`:
```bash
llama-server ... --rope-scaling yarn --rope-scale 3.2 --yarn-orig-ctx 40960
```

### Recommended Sampling Parameters

```yaml
Temperature: 0.7
Top-p: 0.9
Top-k: 20
Min-p: 0.0
```

## 🤝 Community & Support

- **Discussions**: [HuggingFace Community](https://huggingface.co/Menlo/Lucy-128k/discussions)

## 📄 Citation
```bibtex
@misc{dao2025lucyedgerunningagenticweb,
      title={Lucy: edgerunning agentic web search on mobile with machine generated task vectors}, 
      author={Alan Dao and Dinh Bach Vu and Alex Nguyen and Norapat Buppodom},
      year={2025},
      eprint={2508.00360},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.00360}, 
}
```
**Paper **: *Lucy: edgerunning agentic web search on mobile with machine generated task vectors.*