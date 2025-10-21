---
language:
- zh
license: apache-2.0
pretty_name: Marx Works SFT Instruction Prompts Dataset / 马克思著作SFT指令提示数据集
size_categories:
- 1K<n<70K
tags:
- text-generation
- instruction-tuning
- sft
- marxism
- philosophy
- political-economy
task_categories:
- text-generation
task_ids:
- language-modeling
---

# Marx Works SFT Instruction Prompts Dataset / 马克思著作SFT指令提示数据集

[English](#english) | [中文](#chinese)

<a id="english"></a>
## English

### Dataset Description

This dataset contains SFT (Supervised Fine-Tuning) instruction prompts generated from the works of Karl Marx. The dataset is specifically designed for training large language models, aiming to capture Marx's dialectical materialist analytical method and writing style.

### Dataset Features


- **Diverse Prompt Types**: Includes various styles of prompts such as basic analysis, thematic exploration, deep analysis, rhetorical style, concept explanation, and dialectical analysis
- **Original Content Source**: Generated based on Marx's original texts, preserving the original thoughts and analytical methods
- **Chinese Language Corpus**: Designed specifically for Chinese language model training

### Dataset Structure

Each sample contains the following fields:

- `title`: The title of the original Marx work
- `content`: The original text content (may be truncated)
- `prompt`: The generated SFT instruction prompt
- `url`: The source URL of the original text

### Generation Method

The prompts were generated through the following steps:

1. Extraction of text content from Marx's works
2. Generation of various types of prompts using the DeepSeek API:
   - BASE: Basic Marx-style prompts
   - TOPIC: Topic-related prompts
   - DEEPN: Deep analysis prompts
   - STYLE: Rhetorical style prompts
   - CONCEPT: Concept explanation prompts
   - DIALECTIC: Dialectical analysis prompts
3. Application of strict historical constraints to ensure prompts conform to the 19th-century historical background
4. Cleaning and formatting of the final prompts

### Use Cases

This dataset is suitable for:

- Training language models that can mimic Marx's analytical methods
- Fine-tuning specialized models in the fields of history and political economy
- Research on dialectical materialist thought and writing style
- Teaching and research on 19th-century socioeconomic analysis methods

### Citation

If you use this dataset in your research or applications, please cite:

```
@dataset{marx_sft_prompts,
  author    = {ChizhongWang},
  title     = {Marx SFT Prompts Dataset},
  year      = {2025},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/ChizhongWang/secondKarlMarx-sft}
}
```

### License

Apache License 2.0

---

<a id="chinese"></a>
## 中文

### 数据集描述

这个数据集包含基于马克思著作生成的SFT（Supervised Fine-Tuning）指令提示。数据集专为训练大型语言模型而设计，旨在捕捉马克思的辩证唯物主义分析方法和写作风格。

### 数据集特点


- **多样化的提示类型**：包含多种风格的提示，如基础分析、主题探讨、深层次分析、修辞风格、概念阐释和辩证分析
- **原始内容来源**：基于马克思原著文本生成，保留了原始思想和分析方法
- **中文语料**：专为中文语言模型训练设计

### 数据集结构

每个样本包含以下字段：

- `title`: 原始马克思著作的标题
- `content`: 原始文本内容（可能被截断）
- `prompt`: 生成的SFT指令提示
- `url`: 原始文本的来源URL

### 生成方法

提示通过以下步骤生成：

1. 从马克思著作中提取文本内容
2. 使用DeepSeek API生成多种类型的提示：
   - BASE: 基本马克思风格提示
   - TOPIC: 主题相关提示
   - DEEPN: 深层次分析提示
   - STYLE: 修辞风格提示
   - CONCEPT: 概念阐释提示
   - DIALECTIC: 辩证分析提示
3. 应用严格的历史限制，确保提示符合19世纪的历史背景
4. 清理和格式化最终提示

### 使用场景

此数据集适用于：

- 训练能够模仿马克思分析方法的语言模型
- 历史和政治经济学领域的专业模型微调
- 辩证唯物主义思想和写作风格的研究
- 19世纪社会经济分析方法的教学和研究

### 引用

如果您在研究或应用中使用了这个数据集，请引用：

```
@dataset{marx_sft_prompts,
  author    = {ChizhongWang},
  title     = {Marx SFT Prompts Dataset},
  year      = {2025},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/ChizhongWang/secondKarlMarx-sft}
}
```

### 许可证

Apache License 2.0
