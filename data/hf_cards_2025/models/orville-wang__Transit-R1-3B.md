---
language:
- zh
license: apache-2.0
base_model: Qwen/Qwen2.5-3B-Instruct
tags:
- transit
- route-planning
- transportation
- shanghai
- qwen2
- rlhf
pipeline_tag: text-generation
---

# Transit-R1-3B

## 模型介绍

Transit-R1-3B 是一个专门针对城市出行规划场景优化的语言模型，具备公共交通路径规划的能力（Agentic RL）.

## 主要特性

- 🚇 **智能路线规划**: 支持地铁、公交等多种公共交通方式的组合规划
- 🎯 **个性化推荐**: 根据用户偏好（时间最短、费用最低、换乘最少等）提供定制化方案
- 🔄 **多步推理**: 采用思考-规划-观察-回答的结构化推理流程
- 🗺️ **上海地区专精**: 针对上海市公共交通系统深度优化
- ⚡ **轻量高效**: 3B参数规模，支持本地部署
