---
pipeline_tag: text-generation
inference: false
license: mit
library_name: transformers
tags:
- llm
- aquif
- text-generation-inference
- foundational
- moe
- aquif-AlphaMoE
- aquif-3.5
language:
- en
---

# aquif-AlphaMoE

**aquif-AlphaMoE** is the first foundational model designed entirely by **aquif AI**, marking a shift from third-party based architectures (used in aquif-3 and aquif-3.5) toward an in-house architecture family. Released on **October 1, 2025**, AlphaMoE debuts the `AquifAlphaMoEForCausalLM` design, a scalable Mixture of Experts (MoE) framework that balances efficiency, reasoning, and multilingual capability.

This release represents aquif AI’s **first step into independent foundational model architecture design**, with a focus on modular expert scaling, long-context performance, and efficient parameter utilization.

## Model Repository Links

| Model | HuggingFace Repository |
|-------|------------------------|
| aquif-AlphaMoE-7.5B-A3B | [aquif-ai/aquif-AlphaMoE-7.5B-A3B](https://huggingface.co/aquif-ai/aquif-AlphaMoE-7.5B-A3B) |

## Model Overview

| Model | Total Params (B) | Active Params (B) | Experts (Total / Active) | Context | Attention | Vocab Size | MMLU | GPQA-D | LiveCodeBench | Math-500 | Average |
|-------|------------------|-------------------|--------------------------|---------|-----------|------------|------|--------|---------------|----------|---------|
| aquif-AlphaMoE-7.5B-A3B | 7.47 | 2.92 | 64 / 4 | 164k | GQA (16 heads) | 128k | 86.7 | 60.1 | 35.9 | 87.3 | 67.5 |

## Performance Comparison

| Metric        | AlphaMoE (7.5B A3B) | aquif-3-moe (17B A2.8B) | Ling-mini-2.0 (16B A1.4B) | Qwen3-Instruct-2507 (4B) | aquif-3.5 (7.3B) | Granite-4.0-HS (32B A9B) | Gemma-3 (12.2B) |
|---------------|---------------------|--------------------------|---------------------------|--------------------------|------------------|--------------------------|----------------|
| MMLU          | 84.3                | 83.2                     | 80.9                      | 81.6                     | 78.5             | 78.5                     | 78.5           |
| GPQA-Diamond  | 57.5                | 56.7                     | 54.3                      | 49.6                     | 42.3             | 41.6                     | 34.9           |
| LiveCodeBench | 35.9                | 28.6                     | 34.8                      | 31.9                     | 21.3             | 25.1                     | 13.7           |
| Math-500      | 87.3                | 91.4                     | 89.4                      | 84.4                     | 90.2             | 85.4                     | 82.4           |
| **Average**   | **66.3**            | **65.0**                 | **64.9**                  | **61.9**                 | **58.1**         | **57.7**                 | **52.4**       |

## Key Features

- **First Foundational Architecture**: Designed from scratch by aquif AI, unlike aquif-3 and 3.5 which relied on third-party bases.  
- **Scalable MoE Design**: 64 total experts with 4 active per token, enabling dynamic compute allocation.  
- **High Efficiency**: 7.47B total parameters but only 2.92B active, delivering strong performance-to-compute ratios.  
- **Extended Context**: 164k token context window for long-form reasoning and document handling.  
- **Strong Benchmarks**: Surpasses previous aquif generations and peer models in general knowledge, science, and code tasks.  
- **Multilingual Support**: Optimized for 10+ major languages, ensuring broad usability.  

## Technical Specifications

- **Architecture Name**: `AquifAlphaMoEForCausalLM`  
- **Total Parameters**: 7.47B  
- **Active Parameters**: 2.92B  
- **Total Experts**: 64  
- **Active Experts**: 4  
- **Context Window**: 164k tokens  
- **Attention Mechanism**: GQA with 16 heads  
- **Vocabulary Size**: 128k  
- **Supported Precisions**: FP16, BF16  

## License

This project is released under the MIT (prev. Apache 2.0) license. See LICENSE file for details.

---

*Made in 🇧🇷*

© 2025 aquif AI. All rights reserved.
