---
license: apache-2.0
size_categories:
- 10K<n<100K
language:
- zh
- en
tags:
- chat
- dialog
- full-duplex
---
# SemanticVAD 对话状态检测数据集 🌟

## 数据集简介 

本数据集为全双工人机语音交互系统提供语义级语音活动检测（Semantic Voice Activity Detection）任务的训练与测试支持，包含15,000条训练样本和4,400条测试样本，标注质量经过大模型验证优化。

## SemanticVAD 💡

SemanticVAD 通过语义理解实现智能对话状态检测，通常由轻量级语言模型实现。

- 输入：人机交互文本（含历史与实时对话内容） + 当前发言人标识（`'human'`(用户)/`'agent'`(模型)）
- 输出：四类控制标签
  - 🗣️ human 发言时：
    - <完成>: 用户语义完全，模型可以开始回复。
    - <未完>: 用户语义未完，模型继续等待用户输入。
  - 🤖 agent 发言时：
    - <打断>: 用户试图抢夺话题主导权，模型需停止当前回复并聆听用户的新发言。
    - <附和>: 用户赞同模型发言，模型可以继续输出。


## 数据集结构 🗂️
### 训练集（15,000条）

- 数据分布及来源：
  
  | 标签类型 | 中文数据量（来源）                           | 英文数据量（来源）               |
  |----------|------------------------------------------|----------------------------------|
  | <打断>   | 3,000（MagicData-RAMC真实场景 + Ke-SpeechChat 多轮对话） | 1,500（Ke-SpeechChat 单轮合成对话拼接）           |
  | <附和>   | 3,000（MagicData-RAMC真实场景）             | 1,500（CANDOR真实对话）          |
  | <未完>   | 2,000（Ke-SpeechChat 多轮合成对话）                | 1,000（Ke-SpeechChat 单轮合成对话）           |
  | <完成>   | 2,000（Ke-SpeechChat 多轮合成对话）                | 1,000（Ke-SpeechChat 单轮合成对话）           |

- 数据格式为alpaca，样例如:
  ```json
    {
      "instruction": "# Dialog\nHuman[历史]:怎么把人工智能技术用在虚拟现实开发上呢？\nAgent[实时]:将人工智能技术应用到虚拟现实开发中，可以通过智能算法来提升用户体验，比如使用机器学习来创建更真实的虚拟角色\nHuman[实时]:那具体是怎么实现的？比如说，如\n",
      "input": "",
      "output": "<打断>",
      "system": "# Role\n你是人机实时交互的**用户行为分析**模块，你将收到包含部分历史信息的 Human 和 Agent 最新实时对话记录 (Dialog)\n\n# 任务\n当前【Agent正在发言】，在此过程中，你需要基于对话分析 Human 的意图属于 <打断> 还是 <附和>\n\n# 输出\n不要有多余的分析，仅严格输出以下二者之一: <打断> 或 <附和>\n\n# 判断标准\n## <打断> 的情况\nHuman 行为: 试图抢夺话题主导权\n特征包括:\n- 提供新概念/词汇/判断（如命名、定性、对比）\n- 提出问题或异议\n- 引入与当前话题无关的新话题\n\n## <附和> 的情况\nHuman 行为: 赞同 Agent, 期望 Agent 继续说\n特征包括:\n- 使用零内容反馈（嗯/啊/对）\n- 机械重复 Agent 中的原词/同义词\n- 表达简单的确认或同意（如“是的”、“没错”）\n",
      "source": "Ke-多轮",
      "lang": "中文"
    },
  ```

### 测试集（4,400条）
- 来源：Tencent Full-Duplex Spoken Dialogue Systems 测试集
- 数据分布：每类各1100条
- 标注保障：经Qwen2.5-72B-Instruct进行标签校验与修正


## 原始数据来源
本数据集融合以下公开资源，均已进行合规化处理：

1. MagicData-RAMC 数据集
```Bibtex
@article{yang2022open,
  title={Open Source MagicData-RAMC: A Rich Annotated Mandarin Conversational (RAMC) Speech Dataset},
  author={Yang, Zehui and Chen, Yifan and Luo, Lei and Yang, Runyan and Ye, Lingxuan and Cheng, Gaofeng and Xu, Ji and Jin, Yaohui and Zhang, Qingqing and Zhang, Pengyuan and others},
  journal={arXiv preprint arXiv:2203.16844},
  year={2022}
}
```
2. CANDOR 数据集
   
```Bibtex
@article{reece2023candor,
  title={The CANDOR corpus: Insights from a large multimodal dataset of naturalistic conversation},
  author={Reece, Andrew and Cooney, Gus and Bull, Peter and Chung, Christine and Dawson, Bryn and Fitzpatrick, Casey and Glazer, Tamara and Knox, Dean and Liebscher, Alex and Marin, Sebastian},
  journal={Science Advances},
  volume={9},
  number={13},
  pages={eadf3197},
  year={2023},
  publisher={American Association for the Advancement of Science}
}
```
3. Tencent Full-Duplex Spoken Dialogue Systems 测试集
```Bibtex
@misc{zhang2025llmenhanceddialoguemanagementfullduplex,
      title={LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems}, 
      author={Hao Zhang and Weiwei Li and Rilin Chen and Vinay Kothapally and Meng Yu and Dong Yu},
      year={2025},
      eprint={2502.14145},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.14145}, 
}
```
4. Ke-SpeechChat 数据集
```Bibtext
@misc{KE-SemanticVAD,
      title={Advancing Speech Language Models by Scaling Supervised Fine-Tuning with Over 60,000 Hours of Synthetic Speech Dialogue Data}, 
      author={Shuaijiang Zhao and Tingwei Guo and Bajian Xiang and Tongtang Wan and Qiang Niu and Wei Zou and Xiangang Li},
      year={2024},
      eprint={2412.01078},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.01078}, 
}
```


# Citation

Please cite our Hugging-Face when using our code, data or model.
```Bibtext
@misc{KE-SemanticVAD,
      author = {KE-TEAM},
      title = {KE-SemanticVAD},
      year = {2025},
      publisher = {Hugging Face},
      url = {https://huggingface.co/KE-Team/KE-SemanticVAD}
}
```