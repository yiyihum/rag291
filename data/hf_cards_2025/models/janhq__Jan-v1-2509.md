---
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen3-4B-Thinking-2507
pipeline_tag: text-generation
library_name: transformers
---
# Jan-v1: Advanced Agentic Language Model

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/menloresearch/deep-research) 
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://opensource.org/licenses/Apache-2.0)
[![Jan App](https://img.shields.io/badge/Powered%20by-Jan%20App-purple?style=flat&logo=android)](https://jan.ai/) 

<!-- Optional: If you have a GIF for Jan-v1, include it here like Lucy's. -->
<!-- ![image/gif](jan_v1_demo.gif) -->

## Overview

### Update: **Jan-v1-2509**

We have released a small weight update, **jan-v1-2509**, which refines the original v1.

* No architectural changes.
* Slightly **lower performance on SimpleQA** compared to jan-v1.
* **Slightly mproved results on other chat benchmarks** and overall more **reliable**

**Jan-v1** is the first release in the **Jan Family**, designed for agentic reasoning and problem-solving within the [Jan App](https://jan.ai/). Based on our [**Lucy**](https://huggingface.co/Menlo/Lucy) model, Jan-v1 achieves improved performance through model scaling.

Jan-v1 uses the [Qwen3-4B-thinking](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) model to provide enhanced reasoning capabilities and tool utilization. This architecture delivers better performance on complex agentic tasks.

## Performance

### Question Answering (SimpleQA) 
For question-answering, Jan-v1 shows a significant performance gain from model scaling, achieving 91.1% accuracy.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/655e3b59d5c0d3db5359ca3c/B5OlbTP3L6Sn6iT9fA2zg.png)

*The 91.1% SimpleQA accuracy represents a significant milestone in factual question answering for models of this scale, demonstrating the effectiveness of our scaling and fine-tuning approach.*

### Chat Benchmarks

These benchmarks evaluate the model's conversational and instructional capabilities.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/655e3b59d5c0d3db5359ca3c/9EjBc6MEjpcItul6sDYkh.png)

## Quick Start

### Integration with Jan App

Jan-v1 is optimized for direct integration with the [Jan App](https://jan.ai/). Simply select the model from the Jan App interface for immediate access to its full capabilities.

### Local Deployment

**Using vLLM:**
```bash
vllm serve janhq/Jan-v1-2509 \
    --host 0.0.0.0 \
    --port 1234 \
    --enable-auto-tool-choice \
    --tool-call-parser hermes
    
```

**Using llama.cpp:**
```bash
llama-server --model Jan-v1-2509-Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 1234 \
    --jinja \
    --no-context-shift
```

### Recommended Parameters

```yaml
temperature: 0.6
top_p: 0.95
top_k: 20
min_p: 0.0
max_tokens: 2048
```


## 🤝 Community & Support

- **Discussions**: [HuggingFace Community](https://huggingface.co/janhq/Jan-v1-2509/discussions) 
- **Jan App**: Learn more about the Jan App at [jan.ai](https://jan.ai/)

## (*) Note
By default we have system prompt in chat template, this is to make sure the model having the same performance with the benchmark result. You can also use the vanilla chat template without system prompt in the file [chat_template_raw.jinja](https://huggingface.co/janhq/Jan-v1-4B/blob/main/chat_template_raw.jinja).

## 📄 Citation
```bibtex
Updated Soon
```
---