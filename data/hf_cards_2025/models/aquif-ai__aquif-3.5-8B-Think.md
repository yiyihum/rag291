---
pipeline_tag: text-generation
inference: false
license: apache-2.0
library_name: transformers
tags:
- language
- aquif
- text-generation-inference
- math
- coding
- small
- aquif-3.5
language:
- en
- de
- it
- pt
- fr
- hi
- es
- th
- zh
- ja
---

# aquif-3.5

The aquif-3.5 series is the successor to aquif-3, featuring a simplified naming scheme, expanded Mixture of Experts (MoE) options, and across-the-board performance improvements. This release streamlines model selection while delivering enhanced capabilities across reasoning, multilingual support, and general intelligence tasks.

## Model Repository Links

| Model | HuggingFace Repository |
|-------|----------------------|
| aquif-3.5-A0.6B-Preview | [aquiffoo/aquif-3.5-A0.6B-Preview](https://huggingface.co/aquiffoo/aquif-3.5-A0.6B-Preview) |
| aquif-3.5-3B | [aquiffoo/aquif-3.5-3B](https://huggingface.co/aquiffoo/aquif-3.5-3B) |
| aquif-3.5-7B | [aquiffoo/aquif-3.5-7B](https://huggingface.co/aquiffoo/aquif-3.5-7B) |
| aquif-3.5-8B-Think | [aquiffoo/aquif-3.5-8B-Think](https://huggingface.co/aquiffoo/aquif-3.5-8B-Think) |
| aquif-3.5-A4B-Think | [aquiffoo/aquif-3.5-A4B-Think](https://huggingface.co/aquiffoo/aquif-3.5-A4B-Think) |

## Model Overview

| Model | Size (B) | Active Params (B) | Reasoning | MoE | Multilingual | MMLU | Context Window |
|-------|----------|-------------------|-----------|-----|--------------|------|----------------|
| aquif-3.5-A0.6B | 2.61 | 0.6 | ❌ | ✅ | ✅ | 60.5% | 4k |
| aquif-3.5-3B | 2.67 | 2.67 | ❌ | ❌ | ✅ | 70.2% | 32k |
| aquif-3.5-7B | 7.3 | 7.3 | ❌ | ❌ | ✅ | 78.5% | 16k |
| aquif-3.5-8B-Think | 8.2 | 8.2 | ✅ | ❌ | ✅ | 81.1% | 40k |
| aquif-3.5-A4B-Think | 12 | 4 | ✅ | ✅ | ✅ | 86.9% | 128k |

## Model Details

### aquif-3.5-A0.6B (Experimental MoE)

An experimental small-scale Mixture of Experts model designed for multilingual applications with minimal computational overhead. Despite its compact active parameter count, it demonstrates competitive performance against larger dense models.

**Performance Comparison:**

| Metric | aquif-3.5 (2.6B A0.6B) | Qwen3 (0.8B) | LFM2 (0.7B) | aquif-3 (0.4B) |
|--------|------------------------|--------------|-------------|----------------|
| MMLU | 60.5 | 44.9 | 49.9 | 55.6 |
| GPQA | 30.2 | 22.1 | 28.5 | 28.5 |
| GSM8K | 50.7 | 36.5 | 46.4 | 52.1 |
| HumanEval | 45.2 | 36.0 | 40.0 | 37.4 |
| **Average** | **46.7** | **34.9** | **41.2** | **43.4** |

### aquif-3.5-3B (State-of-the-Art Dense)

The new standard for small dense models, offering optimal performance-per-parameter efficiency for general-purpose applications.

**Performance Comparison:**

| Metric | aquif-3.5 (2.7B) | EXAONE 3.5 (2.4B) | Qwen3 (4B) | Gemma 3 (4B) | Phi-4-mini (3.8B) | Apriel-5B-Instruct (4.8B) | aquif-3 (3.2B) |
|--------|------------------|-------------------|------------|--------------|-------------------|---------------------------|----------------|
| MMLU (General Knowledge) | 70.2 | 60.4 | 70.4 | 59.6 | 67.3 | 64.6 | 67.5 |
| GPQA Diamond (Science) | 35.8 | 28.4 | 39.3 | 30.9 | 25.2 | 28.4 | 36.1 |
| LiveCodeBench (Coding) | 23.1 | 12.5 | 21.3 | 11.2 | 10.4 | 11.6 | 15.4 |
| IFEval (Instruction Following) | 78.9 | 73.6 | 71.2 | 80.2 | 68.6 | 80.8 | 78.9 |
| AIME 2025 (Competition Math) | 13.4 | 4.5 | 9.8 | 12.7 | 5.3 | 4.3 | 9.6 |
| **Average** | **44.3** | **35.9** | **42.4** | **38.9** | **35.4** | **37.9** | **41.5** |

### aquif-3.5-7B (Multilingual Long Context)

A Qwen-based architecture optimized for multilingual applications with extended context capabilities, delivering state-of-the-art performance in its size class.

**Performance Comparison:**

| Metric | aquif-3.5 (7.3B) | EXAONE 3.5 (7.8B) | Qwen3 (8.2B) | Gemma 3 (12B) | Llama 3.1 (8B) | Kanana 1.5 (8B) | aquif-3 (3.2B) |
|--------|------------------|-------------------|-------------|---------------|----------------|-----------------|----------------|
| MMLU (General Knowledge) | 78.5 | 72.2 | 82.9 | 74.5 | 69.2 | 68.8 | 67.5 |
| GPQA Diamond (Science) | 42.3 | 39.4 | 39.3 | 40.9 | 32.8 | 37.5 | 36.1 |
| LiveCodeBench (Coding) | 21.3 | 18.0 | 23.9 | 13.7 | 10.8 | 16.5 | 15.4 |
| IFEval (Instruction Following) | 85.6 | 82.6 | 85.4 | 80.2 | 75.0 | 80.1 | 78.9 |
| AIME 2025 (Competition Math) | 23.4 | 18.3 | 20.9 | 18.8 | 2.7 | 13.4 | 9.6 |
| **Average** | **50.2** | **46.1** | **50.4** | **45.6** | **38.1** | **43.3** | **41.5** |

### aquif-3.5-8B-Think & aquif-3.5-A4B-Think (Reasoning Models)

Advanced reasoning-capable models designed for complex problem-solving tasks. The A4B variant leverages MoE architecture for enhanced efficiency while maintaining superior reasoning performance.

**Performance Comparison:**

| Metric | aquif-3.5 (12B A4B) | aquif-3.5 (8B) | Qwen3 Thinking 2507 (31B A3B) | gpt-oss-20b (21B A4B) | Nemotron Nano v2 (9B) | Solar Pro 2 |
|--------|---------------------|-----------------|-------------------------------|----------------------|----------------------|-------------|
| MMLU-Pro | 78.5 | 78.1 | 80.5 | 73.6 | 74.2 | 80.5 |
| GPQA Diamond | 70.8 | 66.8 | 70.7 | 61.7 | 64.0 | 68.7 |
| AIME 2025 | 84.4 | 81.4 | 56.3 | 61.7 | 69.7 | 61.3 |
| LiveCodeBench | 66.1 | 61.5 | 70.7 | 72.1 | 71.1 | 61.6 |
| Humanity's Last Exam | 8.9 | 8.2 | 9.8 | 8.5 | 6.5 | 7.0 |
| TAU-Bench v2 (avg) | 43.7 | 36.8 | 35.7 | 43.2 | 34.9 | 38.7 |
| **Average** | **58.7** | **55.5** | **54.0** | **53.5** | **53.4** | **53.0** |

## Key Improvements Over aquif-3

- **Simplified Naming**: Clear size-based nomenclature for easier model selection
- **Enhanced MoE Support**: Multiple MoE configurations across different model sizes
- **Reasoning Capabilities**: Dedicated thinking models for complex problem-solving
- **Extended Context**: Up to 128k context window for long-form applications
- **Multilingual by Default**: Native multilingual support across all variants
- **Performance Gains**: 5-15% improvement across benchmarks compared to aquif-3

## Usage Recommendations

- **aquif-3.5-A0.6B**: Experimental applications, resource-constrained environments
- **aquif-3.5-3B**: General-purpose applications, balanced performance/efficiency
- **aquif-3.5-7B**: Multilingual applications, long-context tasks
- **aquif-3.5-8B-Think**: Complex reasoning, scientific analysis
- **aquif-3.5-A4B-Think**: Advanced reasoning with efficiency optimization

## Technical Specifications

All models support:
- BF16 and FP16 precision
- Standard transformer architecture optimizations
- Efficient attention mechanisms
- Multi-head attention with optimized KV caching

## Acknowledgements

- **Qwen Team**: Base architecture for 7B, 8B, and 12B-A4B models
- **Meta Llama Team**: Base architecture for 3B and 2.6B-A0.6B models  
- **Hugging Face**: Model hosting infrastructure and training libraries

## License

This project is released under the Apache 2.0 License. See LICENSE file for details.

---

*Made in 🇧🇷*

© 2025 aquif AI. All rights reserved.