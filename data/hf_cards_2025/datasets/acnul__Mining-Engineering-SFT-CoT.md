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
- chain-of-thought
- cot
- knowledge-distillation
- reasoning
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
    num_bytes: 33689277
    num_examples: 5287
  download_size: 18252121
  dataset_size: 33689277
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# 矿建工程领域中文指令与评估数据集（带CoT标注）

## 数据集概述

本项目是**合肥工业大学**大一学生的大学生创新创业训练计划（大创）项目成果。我们构建了一套专为提升大型语言模型在**中国矿建工程领域**专业知识与实践能力而设计的中文数据集。

这套数据集旨在让模型掌握矿建工程的核心知识，内容覆盖了六大模块：
1.  **法律法规 (law)**
2.  **工程规范 (specifications)**
3.  **专业术语 (concept)**
4.  **安全事故案例 (safety)**
5.  **行业实践经验 (forum)**
6.  **领域综合知识 (synthesis)**

为了支持完整的模型开发、评估和验证周期，我们将数据组织为多个独立的Hugging Face仓库：

*   [**原始训练集 (Original SFT Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-SFT)：包含 **5,287** 条高质量的“指令-回答”对，用于基础的模型微调。
*   [**思维链增强训练集 (CoT-Enhanced SFT Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-SFT-CoT)：**（推荐使用）**这是原始训练集的升级版。我们设计并采用了**两阶段知识蒸馏策略**，为每一条数据都注入了高质量的思维链（Chain-of-Thought），旨在显著提升模型的逻辑推理、深度分析和复杂问题解决能力。
*   [**评估集 (Evaluation Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-Eval)：包含 **301** 条数据，用于全面评估模型在各个模块上的综合表现。
*   [**探针集 (Probe Dataset)**](https://huggingface.co/datasets/acnul/Mining-Engineering-Probe)：从评估集中精选的 **50** 条代表性样本，用于在调参过程中进行快速、低成本的性能验证。

---

## CoT增强版：区别与构建方法 (Difference & Construction Method)

### 与原始数据集的区别

| 特性 | 原始 SFT 数据集 (`acnul/Mining-Engineering-SFT`) | CoT增强 SFT 数据集 (`acnul/Mining-Engineering-SFT-CoT`) |
| :--- | :--- | :--- |
| **核心目标** | 知识灌输 (Knowledge Injection) | **推理能力注入 (Reasoning Injection)** + 知识灌输 |
| **`response` 格式** | 直接的、最终的答案。 | **`<think>`标签包裹的思考过程** + 融合了事实与逻辑的最终答案。 |
| **预期效果** | 提升模型在领域的**知识储备**和回答准确性。 | 在此基础上，显著增强模型的**逻辑推理、问题拆解和系统性分析能力**。 |

### 构建方法：两阶段思维链蒸馏与事实对齐

我们设计并实施了一套 **两阶段知识蒸馏与事实对齐（Two-Stage CoT Distillation and Fact-Alignment）**的自动化数据生产流水线，以确保CoT的质量和最终答案的事实准确性：

1.  **第一阶段：自然思维链生成**
    *   我们使用一个以推理能力著称的模型（`DeepSeek R1`）作为“教师模型”。
    *   通过“零指导”的提示工程，我们激发教师模型针对每一个原始问题，**自然地涌现**出其内在的、不受干扰的思考过程（CoT）和初步答案。

2.  **第二阶段：事实对齐与风格融合**
    *   我们将第一阶段生成的“CoT草稿”和我们人工校验过的“事实标准答案”同时提供给一个强大的通用模型（`DeepSeek V3`）。
    *   通过精心设计的“融合Prompt”，我们指导该模型扮演“内容编辑”的角色：**以我们的标准答案为事实的唯一基准，同时尽可能地保留教师模型优秀的逻辑框架和专业风格**，最终合成一份既逻辑严密又事实准确的完美回答。

通过这一策略，我们成功地将教师模型的**隐性推理能力**显性化，并将其高质量地“蒸馏”到了我们的数据集中。

---

## 数据集结构

*   **特征 (Features)**:
    *   `prompt`: 向模型提出的指令或问题。
    *   `response`: 理想的回答。在CoT增强版中，此字段内容以`<think>...</think>`开头的思考过程开始。
    *   `source`: 数据的知识来源类别，为以下六个分类之一：`law`, `specifications`, `concept`, `safety`, `forum`, `synthesis`。

## 如何使用

您可以使用 Hugging Face `datasets` 库轻松加载本系列数据集。

**1. 加载CoT增强训练集 (推荐)**

```python
from datasets import load_dataset

# 加载CoT增强的SFT数据集
cot_sft_dataset = load_dataset("acnul/Mining-Engineering-SFT-CoT")

print(cot_sft_dataset)
# DatasetDict({
#     'train': Dataset({
#         features: ['prompt', 'response', 'source'],
#         num_rows: 5287
#     })
# })

# 查看一条包含CoT的样本
print(cot_sft_dataset['train'][0]['response'])
```

**2. 加载原始训练集 (用于对比实验)**

```python
from datasets import load_dataset

# 加载原始SFT数据集
original_sft_dataset = load_dataset("acnul/Mining-Engineering-SFT")
print(original_sft_dataset)
```

**3. 加载评估集 (Eval)**

```python
from datasets import load_dataset

# 加载完整的评估集
eval_dataset = load_dataset("acnul/Mining-Engineering-Eval")
print(eval_dataset)
```

## 引用

如果您在研究中使用了本数据集，请考虑引用：

```bibtex
@misc{hfut_mining_engineering_datasets_2025,
  author       = {Hefei University of Technology Undergraduate Innovation Program},
  title        = {A Chinese Instruction and Evaluation Dataset Collection with Chain-of-Thought for the Mining Engineering Domain},
  year         = {2025},
  publisher    = {Hugging Face},
  journal      = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/datasets/acnul/Mining-Engineering-SFT-CoT}}
}
```