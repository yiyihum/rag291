---
license: apache-2.0
language:
- en
base_model:
- Menlo/Jan-nano
pipeline_tag: text-generation
library_name: transformers
---

# Jan-Nano-128k: Empowering deeper research through extended context understanding.
<sub>*Note: Jan-Nano is a non-thinking model.*</sub>

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/menloresearch/deep-research) 
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://opensource.org/licenses/Apache-2.0)

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/NP7CvcjOtLX8mST0t7eAM.png" width="300" alt="Jan-Nano-128k">
</div>

**Authors:** [Alan Dao](https://scholar.google.com/citations?user=eGWws2UAAAAJ&hl=en), [Bach Vu Dinh](https://scholar.google.com/citations?user=7Lr6hdoAAAAJ&hl=vi)


![image/gif](https://cdn-uploads.huggingface.co/production/uploads/62d7b2339b629105a5d6888a/aLL8fyMLE3ujV75qD4WKI.gif)


## Overview

Jan-Nano-128k represents a significant advancement in compact language models for research applications. Building upon the success of [Jan-Nano](https://huggingface.co/Menlo/Jan-nano), this enhanced version features a **native 128k context window** that enables deeper, more comprehensive research capabilities without the performance degradation typically associated with context extension methods.

**Key Improvements:**
- **🔍 Research Deeper**: Extended context allows for processing entire research papers, lengthy documents, and complex multi-turn conversations
- **⚡ Native 128k Window**: Built from the ground up to handle long contexts efficiently, maintaining performance across the full context range  
- **📈 Enhanced Performance**: Unlike traditional context extension methods, Jan-Nano-128k shows improved performance with longer contexts

This model maintains full compatibility with Model Context Protocol (MCP) servers while dramatically expanding the scope of research tasks it can handle in a single session.

## Evaluation

Jan-Nano-128k has been rigorously evaluated on the SimpleQA benchmark using our MCP-based methodology, demonstrating superior performance compared to its predecessor:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/Bc0ehij86l_NX52OfxeOj.png)

## Why Jan-Nano-128k?

Traditional approaches to extending context length, such as YaRN (Yet another RoPE extensioN), often result in performance degradation as context length increases. Jan-Nano-128k breaks this paradigm:

This fundamental difference makes Jan-Nano-128k ideal for research applications requiring deep document analysis, multi-document synthesis, and complex reasoning over large information sets.

## 🖥️ How to Run Locally

Jan desktop will eventually support this model (WIP). Otherwise you can check the deployment options below that we have tested.

For additional tutorials and community guidance, visit our [Discussion Forums](https://huggingface.co/Menlo/Jan-nano-128k/discussions).

### Deployment

Deploy using VLLM:
```bash
vllm serve Menlo/Jan-nano-128k \
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
**Note:** The chat template is included in the tokenizer. For troubleshooting, download the [Non-think chat template](https://qwen.readthedocs.io/en/latest/_downloads/c101120b5bebcc2f12ec504fc93a965e/qwen3_nonthinking.jinja).

### Recommended Sampling Parameters

```yaml
Temperature: 0.7
Top-p: 0.8
Top-k: 20
Min-p: 0.0
```

## FAQ:
- I have Jinja template issue with LMStudio, how can i fix? [Here](https://huggingface.co/Menlo/Jan-nano-128k-gguf/discussions/1#6862fe2375cb85f79b28d69c)

## 🤝 Community & Support

- **Discussions**: [HuggingFace Community](https://huggingface.co/Menlo/Jan-nano-128k/discussions)
- **Issues**: [GitHub Repository](https://github.com/menloresearch/jan/issues)
- **Documentation**: [Official Docs](https://menloresearch.github.io/deep-research/)

## 📄 Citation

```bibtex
@misc{dao2025jannanotechnicalreport,
      title={Jan-nano Technical Report}, 
      author={Alan Dao and Dinh Bach Vu},
      year={2025},
      eprint={2506.22760},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.22760}, 
}
```

---

*Jan-Nano-128k: Empowering deeper research through extended context understanding.*