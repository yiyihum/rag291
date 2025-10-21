---
language:
- zh
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- transit-planning
- route-planning
- transportation
- shanghai
- agentic-rl
- qwen2.5
- sft
- chinese
- public-transport
pipeline_tag: text-generation
model-index:
- name: Transit-R1-SFT
  results:
  - task:
      type: transit-route-planning
      name: Transit Route Planning
    dataset:
      name: Shanghai Transit Dataset
      type: custom
    metrics:
    - type: format_compliance
      value: 95.3
      name: Format Compliance Rate
    - type: route_quality
      value: 89.7
      name: Route Quality Score
---

# Transit-R1-SFT

## 模型介绍

Transit-R1-SFT 是基于 Qwen2.5-3B-Instruct 微调的智能出行规划模型，专门针对上海市公共交通路径规划场景优化。该模型通过监督微调(SFT)学习了结构化的推理范式，能够为用户提供个性化的出行方案。

这是 Transit-R1 项目的 SFT 版本，旨在为后续的强化学习提供基础。

## 主要特性

- 🚇 **智能路线规划**: 支持地铁、公交、步行等多种交通方式的组合规划
- 🎯 **个性化推荐**: 根据用户偏好（时间优先、成本优先、换乘最少、舒适优先）提供定制化方案
- 🔄 **结构化推理**: 采用 `<think>→<code>→<observation>→<answer>` 的四阶段推理流程
- 🗺️ **上海地区专精**: 针对上海市公共交通系统和地标建筑深度优化
- ⚡ **轻量高效**: 3B参数规模，支持本地部署和实时推理
- 📱 **API集成**: 支持高德地图API调用进行实时路线查询

## 训练数据

- **数据规模**: 5000条高质量出行规划样本
- **覆盖场景**: 医院、学校、商圈、住宅区、文化场所等多样化出行场景
- **用户画像**: 涵盖学生、上班族、老人、游客、商务人士等不同群体
- **地理范围**: 专注上海市主要区域和热门地标
- **数据质量**: 真实API响应，人工校验，确保方案可行性

## 模型架构

- **基础模型**: Qwen2.5-3B-Instruct
- **训练方法**: 监督微调 (SFT)
- **参数量**: 3B
- **上下文长度**: 2048 tokens
- **训练轮数**: 4 epochs
- **学习率**: 1e-5