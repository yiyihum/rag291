---
license: apache-2.0
datasets:
- TorpedoSoftware/LuauLeetcode
language:
- en
- fr
- de
- es
- pt
- it
base_model:
- TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.1
tags:
- roblox
- luau
- code
- grpo
- transformers
- trl
- unsloth
---

# Luau Devstral 24B Instruct v0.2

**State-of-the-art Luau code generation through reinforcement learning post-training**

A refined version of [Luau-Devstral-24B-Instruct-v0.1](https://huggingface.co/TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.1), enhanced with Dr. GRPO ([Zichen Liu et al., 2025](https://arxiv.org/abs/2503.20783)) to deliver superior Luau programming capabilities for Roblox development.

## Overview

This model represents a significant advancement in specialized code generation for Luau, building upon continuous pretraining with targeted reinforcement learning to achieve exceptional code quality.

**Key Achievements:**
- State-of-the-art code formatting and linting performance
- Minimal typechecker issues with strict mode compliance
- Concise, direct responses without unnecessary verbosity
- Robust problem-solving capabilities on complex Luau challenges

## Model Information

- **Developer:** Zack Williams ([boatbomber](https://huggingface.co/boatbomber))
- **Sponsor:** [Torpedo Software LLC](https://huggingface.co/TorpedoSoftware)
- **Base Model:** [Luau-Devstral-24B-Instruct-v0.1](https://huggingface.co/TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.1)
- **Training Method:** Dr. GRPO (Group Relative Policy Optimization)

## Performance Benchmarks

Evaluated on the `test` split of [TorpedoSoftware/LuauLeetcode](https://huggingface.co/datasets/TorpedoSoftware/LuauLeetcode) containing 226 challenges, with results averaged across 3 runs per challenge.

### Comparison Models

**Base Models:**
- [Devstral-Small-2507](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [Luau-Devstral-24B-Instruct-v0.1](https://huggingface.co/TorpedoSoftware/Luau-Devstral-24B-Instruct-v0.1)

**Competitive Benchmarks:**
- [Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [gpt-oss-20b (low reasoning)](https://huggingface.co/openai/gpt-oss-20b)
- [GPT-5 nano (minimal reasoning)](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 (minimal reasoning)](https://openai.com/gpt-5/)
- [Claude Sonnet 4](https://www.anthropic.com/claude/sonnet)
- [Claude Opus 4.1](https://www.anthropic.com/claude/opus)

*Note: OpenAI models utilize reasoning tokens as complete disabling of thinking is not available.*

### Benchmark Results

#### Unit Test Pass Rate
*Measures problem-solving accuracy and correctness*

![Unit Tests](assets/bench-unit-tests.png)

**Result:** 4th place overall, demonstrating solid problem-solving capabilities while outperforming OpenAI models.

#### Linter Errors
*Evaluates fundamental code quality*

![Linter Errors](assets/bench-linter-errors.png)

**Result:** State-of-the-art performance with the lowest error rate by a significant margin.

#### Linter Warnings
*Assesses non-critical code quality issues*

![Linter Warnings](assets/bench-linter-warnings.png)

**Result:** State-of-the-art performance in minimizing code warnings.

#### Type Safety
*Strict mode typechecking compliance*

![Typechecker Issues](assets/bench-typechecker-issues.png)

**Result:** 2nd place, closely trailing Claude Opus 4.1. Our model favors explicit type definitions for enhanced code clarity, which creates more opportunities for mistakes compared to Claude's reliance on inferred types.

#### Code Formatting
*Edit distance from Stylua's standard format*

![Formatter Distance](assets/bench-formatter-distance.png)

**Result:** State-of-the-art performance with exceptional adherence to standard formatting conventions.

#### Response Length
*Average response size (excluding reasoning tokens)*

![Response Length](assets/bench-response-length.png)

**Result:** Most concise responses among all models, delivering direct solutions without unnecessary preamble. This efficiency suggests potential for further improvements in problem solving through explicit problem decomposition or reasoning.

## Training Methodology

### Dataset

**Primary Source:** [TorpedoSoftware/LuauLeetcode](https://huggingface.co/datasets/TorpedoSoftware/LuauLeetcode)
- 2.6K leetcode-style Luau programming challenges
- Structured difficulty progression: Easy → Medium → Hard

### Training Process

**Curriculum Learning Approach:**

1. **Easy Difficulty Phase**
   - 6.45M input tokens
   - 25 hours training
   
2. **Medium Difficulty Phase**
   - 17.02M input tokens
   - 58 hours training
   
3. **Hard Difficulty Phase**
   - 6.07M input tokens
   - 20 hours training

**Technical Configuration:**
- LoRA adapter with rank=128
- Full precision training
- Final merge to BF16 model

### Reward Function Design

The model was optimized using four complementary reward signals:

1. **Correctness** - Unit testing via [Jest-Lua](https://github.com/jsdotlua/jest-lua)
2. **Quality** - Code linting with [Selene](https://github.com/Kampfkarren/selene)
3. **Type Safety** - Strict typechecking using [Luau](https://luau.org)
4. **Formatting** - Style conformance via [Stylua](https://github.com/JohnnyMorganz/StyLua)

### Training Progress

#### Easy Difficulty Training
![Easy Overall Reward Curve](assets/easy-overall-reward.png)
![Easy Individual Reward Curves](assets/easy-individual-rewards.png)

#### Medium Difficulty Training
![Medium Overall Reward Curve](assets/medium-overall-reward.png)
![Medium Individual Reward Curves](assets/medium-individual-rewards.png)

#### Hard Difficulty Training
![Hard Overall Reward Curve](assets/hard-overall-reward.png)
![Hard Individual Reward Curves](assets/hard-individual-rewards.png)

## Quantization Support

### Imatrix Calibration

Custom importance matrix computed using 5.73MB of specialized text data:

**Calibration Sources:**
- [technical.txt](https://huggingface.co/datasets/froggeric/imatrix/blob/main/technical.txt)
- [groups_merged.txt](https://huggingface.co/datasets/froggeric/imatrix/blob/main/groups_merged.txt)
- [the-luau-stack](https://huggingface.co/datasets/TorpedoSoftware/the-luau-stack)
- [roblox-info-dump](https://huggingface.co/datasets/TorpedoSoftware/roblox-info-dump)

This calibration ensures optimal performance for Luau/Roblox tasks while maintaining general intelligence. The `imatrix.gguf` file is included in the repository for custom quantization needs.

## Environmental Impact

Carbon emissions estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) ([Lacoste et al., 2019](https://arxiv.org/abs/1910.09700)):

- **Hardware:** A100 80GB SXM
- **Training Duration:** 103 hours
- **Carbon Emissions:** ~12 kg CO2eq
- **Equivalent Impact:** ~31 miles driven by an average internal combustion engine vehicle
