---
license: mit
language: zh
library_name: datasets
tags:
- mining-engineering
- instruction-tuning
- SFT
- chinese
- llm
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: response
    dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 6559967
    num_examples: 5287
  download_size: 3342351
  dataset_size: 6559967
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# 矿建工程领域中文指令与评估数据集

## 数据集概述

**注: 本数据集为不带CoT标注的数据集，如果您要对DeekSeek R1、Qwen3系列等具有内嵌的CoT输出的模型进行微调，为了避免模型发生灾难性遗忘，请移步至本项目的[思维链增强训练集 (CoT-Enhanced SFT Dataset)](https://huggingface.co/datasets/acnul/Mining-Engineering-SFT-CoT) **

本项目是**合肥工业大学**大一学生的大学生创新创业训练计划（大创）项目成果。我们构建了一套专为提升大型语言模型在**中国矿建工程领域**专业知识与实践能力而设计的中文数据集。

这套数据集旨在让模型掌握矿建工程的核心知识，内容覆盖了六大模块：
1.  **法律法规 (law)**
2.  **工程规范 (specifications)**
3.  **专业术语 (concept)**
4.  **安全事故案例 (safety)**
5.  **行业实践经验 (forum)**
6.  **领域综合知识 (synthesis)**

为了支持完整的模型开发、评估和验证周期，我们将数据组织为多个独立的Hugging Face仓库：

*   **本数据集 (原始训练集)**: `acnul/Mining-Engineering-SFT` 包含 **5,287** 条高质量的“指令-回答”对，用于基础的模型微调，侧重于**知识灌输**。
*   [**思维链增强训练集 (CoT-Enhanced SFT Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-SFT-CoT)：**（推荐）** 这是本数据集的升级版。我们设计并应用了**两阶段知识蒸馏策略**，为每一条数据都注入了高质量的思维链（Chain-of-Thought），旨在显著提升模型的**逻辑推理与深度分析能力**。
*   [**评估集 (Evaluation Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-Eval)：包含 **301** 条数据，用于全面评估模型在各个模块上的综合表现。
*   [**探针集 (Probe Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-Probe)：从评估集中精选的 **50** 条代表性样本，用于在调参过程中进行快速、低成本的性能验证。

## 数据集结构

本系列数据集通过三个独立的仓库进行组织，每个仓库有其特定的结构和用途。

### 1. 训练集 - `acnul/Mining-Engineering-SFT` & `acnul/Mining-Engineering-SFT-CoT`

这是用于监督式微调（SFT）的核心数据集。它被合并成一个单一的拆分。
*   **拆分 (Split)**: `train`
*   **特征 (Features)**:
    *   `prompt`: 向模型提出的指令或问题。
    *   `response`: 模型应当生成的理想回答。
    *   `source`: 数据的知识来源类别，为以下六个分类之一：`law`, `specifications`, `concept`, `safety`, `forum`, `synthesis`。

### 2. 评估集与探针集 - `acnul/Mining-Engineering-Eval` & `acnul/Mining-Engineering-Probe`

这两个仓库用于对微调后模型进行能力评估，结构一致，仅数据量不同。
*   **拆分 (Splits)**: 评估集的**拆分**对应了项目的六大知识模块，允许对模型在特定子领域的能力进行独立测试。
    *   `concept`
    *   `forum`
    *   `law`
    *   `safety`
    *   `specifications`
    *   `synthesis`
*   **特征 (Features)**: 为了清晰和一致，所有拆分都统一为5个核心字段。
    *   `prompt`: 评估问题。
    *   `response`: 评估的黄金标准答案 (`golden_answer`)。
    *   `question_type`: 问题的类型分类，用于更细致的评估。
    *   `source`: 数据的知识来源类别（与训练集一致）。
    *   `task_id`: 每个问题的唯一标识符。

## 构建方法

数据集的构建采用了多种数据工程技术，旨在确保数据的质量、广度和深度。
*   **法律法规**：基于公开发布的核心法律文本，通过数据合成技术生成高质量问答对，并设计了对抗性样本，以提升模型的法律遵循和辨伪能力。
*   **工程规范**：从权威的工程标准与规范中系统性地提取关键技术要求和量化指标，并将其转化为结构化的问-答形式，用于训练模型对技术细节和合规性问题的理解。
*   **安全事故案例**：对公开的事故调查报告进行了深度分析，并开创性地设计了从“核心概括”到“原理泛化”的多层次、递进式提问范式，旨在由浅入深地培养模型的事故归因、逻辑推理和举一反三的能力。
*   **行业实践与综合知识**：结合了一线从业者的实践经验和领域内的长尾知识点，通过半自动化流程生成了大量覆盖面广的问答数据，以增强模型解决实际问题的能力和知识广度。

## 如何使用

您可以使用 Hugging Face `datasets` 库轻松加载本系列数据集。

**1. 加载训练集 (SFT)**

```python
from datasets import load_dataset

# 加载SFT数据集，它只有一个 'train' split
sft_dataset = load_dataset("acnul/Mining-Engineering-SFT")

print(sft_dataset)
# DatasetDict({
#     'train': Dataset({
#         features: ['prompt', 'response', 'source'],
#         num_rows: 5287
#     })
# })

# 查看source字段的分布
print(sft_dataset['train'].to_pandas()['source'].value_counts())
```

**2. 加载评估集 (Eval)**

```python
from datasets import load_dataset

# 加载完整的评估集，它包含多个split，分别对应不同模块
eval_dataset = load_dataset("acnul/Mining-Engineering-Eval")

print(eval_dataset)
# DatasetDict({
#     'concept': Dataset({ features: ['prompt', 'response', ...], num_rows: 15 }),
#     'forum': Dataset({ features: ['prompt', 'response', ...], num_rows: 60 }),
#     'law': Dataset({ features: ['prompt', 'response', ...], num_rows: 30 }),
#     'safety': Dataset({ features: ['prompt', 'response', ...], num_rows: 20 }),
#     'specifications': Dataset({ features: ['prompt', 'response', ...], num_rows: 56 }),
#     'synthesis': Dataset({ features: ['prompt', 'response', ...], num_rows: 120 })
# })

# 访问 "法律法规" 模块的评估数据
law_eval_data = eval_dataset['law']
print(law_eval_data[0])
```

## 引用

如果您在研究中使用了本数据集，请考虑引用：

```bibtex
@misc{hfut_mining_engineering_datasets_2025,
  author       = {Hefei University of Technology Undergraduate Innovation Program},
  title        = {A Chinese Instruction and Evaluation Dataset Collection for the Mining Engineering Domain},
  year         = {2025},
  publisher    = {Hugging Face},
  journal      = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/datasets/acnul/Mining-Engineering-SFT}}
}
```