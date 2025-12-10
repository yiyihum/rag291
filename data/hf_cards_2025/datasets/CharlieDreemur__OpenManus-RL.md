---
language:
- en
tags:
- sft
- instruction-tuning
- conversational-ai
license: apache-2.0
task_categories:
- text-generation
pretty_name: OpenManusRL
dataset_info:
  features:
  - name: id
    dtype: string
  - name: conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 277895199
    num_examples: 48927
  download_size: 73312767
  dataset_size: 277895199
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Dataset Card for OpenManusRL

## Dataset Description

### Overview

<p align="center">
  💻 <a href="https://github.com/OpenManus/OpenManus-RL" target="_blank">[Github Repo]</a>
</p>

**OpenManusRL** combines agent trajectories from [AgentInstruct](https://huggingface.co/datasets/THUDM/AgentInstruct), [Agent-FLAN](https://huggingface.co/datasets/internlm/Agent-FLAN) and [AgentTraj-L(AgentGym)](https://huggingface.co/datasets/AgentGym/AgentTraj-L) with features:

- 🔍 **ReAct Framework** - <a href="https://react-lm.github.io/" target="_blank">Reasoning-Acting integration</a>
- 🧠 **Structured Training** - Separate format/reasoning learning
- 🚫 **Anti-Hallucination** - Negative samples + environment grounding
- 🌐 **6 Domains** - OS, DB, Web, KG, Household, E-commerce

### Dataset Overview

| Source | Trajectories | Avg Turns | Key Features |
|--------|--------------|-----------|--------------|
| [Agent-FLAN](https://huggingface.co/datasets/internlm/Agent-FLAN) | 34442 | 3-35 | Error recovery patterns, CoT reasoning|
  [AgentTraj-L](https://huggingface.co/datasets/AgentGym/AgentTraj-L) | 14485 | 3-35 | interactive environments and tasks
| **Combined** | 48927 | 4-20 | Enhanced generalization, uniform format with broader task coverage |

### Supported Tasks
- **text-generation**: ReAct-style instruction following
- **conversational-ai**: Tool-augmented dialogues

### Languages
English

## Dataset Structure

### Data Instances

**ReAct Pattern Example**:
```json
{
  "id": "os_0",
  "conversations": [
    {"role": "user", "content": "Count files in /etc"},
    {"role": "assistant", "content": "Think: Need reliable counting method\nAct: bash\n```bash\nls -1 /etc | wc -l\n```"},
    {"role": "user", "content": "OS Output: 220"},
    {"role": "assistant", "content": "Think: Verified through execution\nAct: answer(220)"}
  ]
}
```

## Licensing
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- **Sources:**
  - [AgentInstruct](https://huggingface.co/datasets/THUDM/AgentInstruct) (CC-BY-NC-4.0)
  - [Agent-FLAN](https://huggingface.co/datasets/internlm/Agent-FLAN) (Apache 2.0)

## Citation
```bibtex
@misc{zeng2023agenttuning,
  title={AgentTuning: Enabling Generalized Agent Abilities for LLMs},
  author={Aohan Zeng and Mingdao Liu and Rui Lu and Bowen Wang and Xiao Liu and Yuxiao Dong and Jie Tang},
  year={2023},
  eprint={2310.12823},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}

@article{chen2024agent,
  title={Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models},
  author={Chen, Zehui and Liu, Kuikun and Wang, Qiuchen and Zhang, Wenwei and Liu, Jiangning and Lin, Dahua and Chen, Kai and Zhao, Feng},
  journal={arXiv preprint arXiv:2403.12881},
  year={2024}
}

@misc{xi2024agentgym,
      title={AgentGym: Evolving Large Language Model-based Agents across Diverse Environments}, 
      author={Zhiheng Xi and Yiwen Ding and Wenxiang Chen and Boyang Hong and Honglin Guo and Junzhe Wang and Dingwen Yang and Chenyang Liao and Xin Guo and Wei He and Songyang Gao and Lu Chen and Rui Zheng and Yicheng Zou and Tao Gui and Qi Zhang and Xipeng Qiu and Xuanjing Huang and Zuxuan Wu and Yu-Gang Jiang},
      year={2024},
      eprint={2406.04151},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

## Contact
[OpenManus Team](https://github.com/OpenManus/OpenManus-RL)