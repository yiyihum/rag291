---
license: mit
datasets:
- UI-Simulator/UI-Simulator_android_data
language:
- en
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
tags:
- agent
- mobile-agent
- world-model
- GUI-agent
---

# 🌍 UI-Simulator: LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training

[![License](https://img.shields.io/github/license/WadeYin9712/UI-Simulator)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Stars](https://img.shields.io/github/stars/WadeYin9712/UI-Simulator?style=social)]()

🔗 **Paper link**: [Link]() 

🌐 **Website**: https://ui-simulator.notion.site/llms-as-scalable-digital-world-simulator

📚 **Github:** https://github.com/WadeYin9712/UI-Simulator

📧 **Contact:** [da.yin9712@gmail.com](mailto:da.yin9712@gmail.com), [w10y20ming@gmail.com](mailto:w10y20ming@gmail.com)

---

# Model Card for Model ID

This is the agent trained on **retrieval-free** Android UI-Simulator. It is trained to solve AndroidWorld tasks.

## Uses

We provide a script for loading the model and run AndroidWorld evaluation [here](https://github.com/WadeYin9712/UI-Simulator/blob/main/android_world/run.py).