---
license: cc-by-sa-4.0
task_categories:
- text-generation
language:
- zh
size_categories:
- 10K<n<100K
---

<h1 align="center">
  中文 DeepSeek-R1-Distil 数学指令微调数据集
</h1>

<p align="center">
  <a href="https://github.com/Mxoder/Maxs-Awesome-Datasets" target="_blank">💻 Github Repo</a> <br>
</p>

## 基本信息

数据集大小 10K，独立生成指令与回复，并非其他社区数据集的子集。**所有数据经过校验，答案正确性可以得到保证。**

数据集的组成如下：

| 问题类型         | 数据条数 |
|--------------|----------|
| 定积分计算       | 2626     |
| 多项式化简       | 1621     |
| 因式分解         | 2557     |
| 多项式展开       | 2095     |
| 多项式方程       | 1101     |
| **总数**         | **10000** |


## 数据格式

每条数据的格式如下：

```json
{
  "id": <<12位nanoid>>,
  "prompt": <<提示词>>,
  "reasoning": <<模型思考过程>>,
  "response": <<模型最终回复>>
}
```