---
language:
- zh
license: apache-2.0
task_categories:
- text-generation
pretty_name: WuDaoCorpora2.0-RefinedEdition60GTXT
size_categories:
- 10M<n<100M
---

# WuDaoCorpora2.0 Refined Edition (60G TXT)

一个经过深度清洗的高质量中文悟道语料子集，包含约 12M 条长文本。

## 数据来源

本数据集基于**悟道(WuDao) 2.0**开放语料（`WuDaoCorporaText-2.0-open.rar`）清洗得到。

原始文件获取自：[中国科技情报网(Scidb)](https://www.scidb.cn/en/detail?dataSetId=c6a3fe684227415a9db8e21bac4a15ab)

## 数据清洗流程
数据处理所需工具见[github仓库](https://github.com/xizhang123/LLM_from_tokenizer_to_sft)
1.  **文本提取与合并**：从原始压缩包加压得到的json文件中提取纯文本，合并。
2.  **哈希去重**：以行为单位，移除完全相同的语料。
3.  **质量标注与分类**：
    - 人工标注数千条数据（高/中/低质量）。
    - 使用标注数据训练文本分类模型（该模型在[News2016zh](https://opendatalab.com/OpenDataLab/News2016zh)语料上进行了预训练）。
4.  **词表生成与广告清洗**：
    - 使用高质量数据生成词表（基于长片段崩解与最大概率路径分词算法，生僻字支持字节拆分，大模型可用）。
    - **关键步骤**：分析词表中相邻的长片段，定位并彻底清洗相似广告内容（哈希去重无法处理此类变异广告）。
    
正常词汇：

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/er1KkljCAom88S00WYTIh.png)
长词聚集（聚集的原因是词表未排序，广告中的长片段一起进入词表，又因为重复度高，在最大概率路径分词时很难被崩解成小片段，从词频也可以确定是相似广告导致的）：

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/akk9Z7-Q820pEvbl94Raj.png)

广告黑名单节选（根据聚集特性从词表中获取）：

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/LReNNRR9wjw4E0C_-tQ8o.png)

最终词表节选，目标65536，实际65544：

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/3uKdM3dSBWf4PSULJZbmZ.png)

5.  **统计过滤**：
    - 根据文本长度分布去除前后5%
    - 根据标点符号占比分布去除前后5%
    - 根据ASCII字符占比去除前10%

清洗后语料长度统计：

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/UpIocU6LdKFEhDXC89npg.png)
标点符号占比统计（1000个统计区间）

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/WgPBHljhcXq9IS4gIZxMK.png)
ascii占比统计（1000个统计区间）

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cd05ffe709c1aeb655f239/rFkqVCifJ2AwxGVhcOaJA.png)

## 数据概览

- **内容**： 通用中文文本
- **语言**： 中文 (zh)
- **格式**： 纯文本 (.txt)
- **规模**： 约 60 GB
- **条数**： 约 12M 条
- **许可证**： Apache License 2.0
