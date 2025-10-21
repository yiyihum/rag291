---
license: mit
task_categories:
- text-generation
- conversational
language:
- en
tags:
- agentgym
- reinforcement-learning
- sft
- trajectory-data
- ai-agents
- multi-agent
size_categories:
- 100K<n<1M
---

# AgentGym SFT Trajectories

A comprehensive dataset of **101,926 training examples** from 5 AgentGym environments, formatted for supervised fine-tuning (SFT) of language models on interactive tasks.

## Dataset Details

- **Total Samples**: 101,926 training examples
- **Environments**: 5 AgentGym environments with balanced representation
- **Format**: ChatML-style messages with environment labels
- **File Size**: 459MB

### Environments Included

1. **AlfWorld** (household tasks)
2. **BabyAI** (grid navigation)
3. **WebShop** (e-commerce)
4. **SciWorld** (science experiments)
5. **TextCraft** (text crafting)

## Dataset Structure

Each sample contains:
```json
{
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "environment": "alfworld"  // environment label
}
```

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("bunnybhaiya/agentgym-sft-trajectories")

# Access samples
for sample in dataset['train']:
    messages = sample['messages']
    environment = sample['environment']
```

## Training Applications

This dataset is designed for:
- **SFT Training**: Supervised fine-tuning on agent trajectories
- **Multi-environment Learning**: Train models across diverse task domains
- **Agent Behavior Modeling**: Learn interactive decision-making patterns
- **GRPO Preparation**: Build foundation for reinforcement learning from human feedback

## License

MIT License - See LICENSE file for details.

## Citation

If you use this dataset, please cite AgentGym and this dataset version.