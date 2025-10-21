---
language:
- en
license: mit
task_categories:
- text-generation
- question-answering
- text2text-generation
tags:
- structural-tension
- creative-process
- fritz-methodology
- personal-development
- coaching
- instruction-tuning
- conversational
pretty_name: Structural Weaver
size_categories:
- n<1K
---

# Structural Weaver Dataset

## Overview
Training dataset for fine-tuning language models on **structural tension methodology** and the **creative process** as developed by Robert Fritz.

## Dataset Details
- **Size**: 45 high-quality conversational examples
- **Format**: ChatML (system/user/assistant conversations)
- **Domain**: Creative process, structural tension, goal achievement
- **Language**: English
- **License**: MIT

## Content Areas
1. **Structural Tension**: Understanding the dynamic between current reality and desired outcomes
2. **Creative Process**: Three-phase approach (germination, assimilation, completion)
3. **Fritz Methodology**: Principles from "Learning as Art" and structural work
4. **Goal Setting**: Strategic approaches to achieving creative and personal goals

## Usage
Perfect for fine-tuning models to provide guidance on:
- Creative process navigation
- Structural tension understanding
- Personal development coaching
- Artistic and professional goal achievement

## Training Characteristics
- Conversational format suitable for instruction tuning
- Balanced system prompts and detailed responses
- Professional tone with practical guidance
- Minimal repetition, high information density

## Data Format
Each example follows the ChatML format:
```json
{
  "messages": [
    {"role": "system", "content": "System prompt"},
    {"role": "user", "content": "User question"},
    {"role": "assistant", "content": "Assistant response"}
  ]
}
```

## Source
Derived from comprehensive study of Fritz's structural tension methodology and creative process frameworks.

## Citation
```bibtex
@dataset{structural_weaver_2025,
  title={Structural Weaver: Training Dataset for Creative Process and Structural Tension},
  author={jgwill},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/jgwill/structural-weaver}
}
```

## Related Work
- Robert Fritz - "The Path of Least Resistance"
- Robert Fritz - "Creating"
- Structural Tension Methodology
- Creative Process Theory
