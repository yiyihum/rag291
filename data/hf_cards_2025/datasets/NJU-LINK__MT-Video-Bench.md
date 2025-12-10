---
license: cc-by-nc-nd-4.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- video
viewer: false
extra_gated_prompt: You need to agree to the following terms to access this dataset
extra_gated_fields:
  Full Name: text
  Country: country
  Institution/Organization: text
  Department: text
  Position:
    type: select
    options:
    - Professor
    - PostDoc
    - PhD Student
    - MS Student
    - Research Scientist
    - Industry Researcher
    - Other
  Institutional Email: text
  Website or Google Scholar (if none, enter N/A): text
  Research Purpose: text
  How did you hear about this dataset?: text
  I agree to use this dataset for non-commercial research purposes only: checkbox
  I will cite the MT-Video-Bench paper in any publications: checkbox
  I will not redistribute the dataset without permission: checkbox
extra_gated_button_content: Submit Application
---

<p align="center">
  <img src="./static/LINK-LOGO.png" width="260" alt="link Logo" style="border-radius: 12px;">
</p>

<h1 align="center">MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues</h1>
<p align="center">
  <a href="https://github.com/NJU-LINK/MT-Video-Bench">
    <img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white&color=gray" alt="GitHub">
  </a>
  <a href="https://mt-video-bench.github.io/">
    <img src="https://img.shields.io/badge/%F0%9F%8C%90%20Homepage-MT--Video--Bench-blue.svg" alt="Homepage">
  </a>
  <a href="https://arxiv.org/abs/2510.10689">
    <img src="https://img.shields.io/badge/Paper-ArXiv-red.svg" alt="Arxiv Paper">
  </a >
  <a href="https://huggingface.co/datasets/NJU-LINK/MT-Video-Bench">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Huggingface-MT--Video--Bench-yellow.svg" alt="Huggingface">
  </a>
</p>

---

## ✨ Introduction

Recent advances in **multimodal large language models (MLLMs)** have brought remarkable progress in video understanding.  
However, existing evaluation benchmarks remain limited to single-turn question answering, overlooking the complexity of multi-turn dialogues in real-world scenarios.

🎬 **MT-Video-Bench** fills this gap.  
It emphasizes cross-scene reasoning, long-range dependencies, and interactive adaptability, thereby aligning closely with real-world application demands.
<p align="center">
  <img src="./static/intro.png" width="88%" alt="Illustration of MT-Video-Bench">
  <br>
  <em>Figure 1. Illustration of multi-turn dialogues under single-scene and cross-scene settings. The evaluated questions corresponding to tasks are marked with underlining, and the scenes involved in the entire multi-turn dialogues are marked with blue dotted boxes.</em>
</p>

---

## 🚀 Overview

**MT-Video-Bench**‘s information:

- 📌 **135 videos** from 5 major categories & 23 subcategories 

- 💬 **987 dialogues** (each with 5–8 turns) and **5,805 QA pairs** for evaluating six core abilities
  - Object Reference
  - Memory Recall
  - Content Summary
  - Answer Refusal
  - Topic Shifting
  - Proactive Interaction

- 🧮 **Long-Video Evaluation:** durations up to 20 minutes 
  
- 🧠 Very challenging, even 🥇 best-performing model achieving only ⚠️ 68.45 % overall accuracy, revealing the considerable difficulty of this dataset.

<p align="center">
  <img src="./static/benchmark_statistics.png" width="88%" alt="Statistics of multi-turn dialogues">
  <br>
  <em>Figure 2. It covers a broad range of topics across five main categories: Movie, TV, Sports, Knowledge, and Life Record, each with multiple sub-topics, ensuring a diverse and balanced data distribution.</em>
</p>

---

## 🧩 Pipeline

A glance at how MT-Video-Bench was built👇

1. 🔎 **Video Collection & Single-Scene Splitting:** Manually collect videos → split into short clips using PySceneDetect → generate captions for each clip → merge related clips based on captions to form coherent single-scene videos.
2. 🧾 **Cross-Scene Video Merging:** Extract key frames → perform object detection → build a dynamic object memory bank → retrieve and merge segments sharing common objects or themes.
3. 📦 **Multi-Turn Dialogue Generation:** Use Gemini 2.5 to automatically generate single-scene and cross-scene multi-turn dialogues → select the most suitable task for each scene → design cross-scene questions with an object-centered approach.
4. 🚦 **Human Quality Control:** Remove cases with information leakage → manually verify QA alignment, factual correctness, and difficulty → ensure high-quality, contextually coherent multi-turn dialogues.


<p align="center">
  <img src="./static/pipeline_page-0001.jpg" width="85%" alt="Data Pipeline">
  <br>
  <em>Figure 3. Data construction and refinement pipeline of MT-Video-Bench.</em>
</p>

---

## 🌟 License

Our dataset is under the CC-BY-NC-SA-4.0 license.

⚠️ If you need to access and use our dataset, you must understand and agree: This dataset is for research purposes only and cannot be used for any commercial or other purposes. The user assumes all effects arising from any other use and dissemination.

We do not own the copyright of any raw video files. Currently, we provide video access to researchers under the condition of acknowledging the above license. For the video data used, we respect and acknowledge any copyrights of the video authors. 

If the original authors of the related works still believe that the videos should be removed, please contact ynpan24@m.fudan.edu.cn or directly raise an issue.

---

## 🔐 Dataset Access

Please contact ynpan24@m.fudan.edu.cn to get full dataset.

---

## 🪶 Citation

If you find **MT-Video-Bench** useful for your research, please cite:

```bibtex

```