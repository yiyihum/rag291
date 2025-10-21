---
base_model: google/gemma-3-270m-it
tags:
- text-generation
- social-media-hashtags
- gemma
- Web4
- MLM
- Linkspreed
- Hashtags
license: apache-2.0
---
# 🤖 Web4/LS-W4-270M-Micro-Hashtags Model Card

## 💻 Model Details

- **Model Name:** Web4/LS-W4-270M-Micro-Hashtags  
- **Model Type:** Micro Language Model (MLM)  
- **Model Size:** 270 Million parameters (270M)  
- **Developer:** Web4  
- **Intended Use:** On-device, offline, and browser-based hashtag generation from user text input  
- **License:** MIT  

## 📄 Model Description

The **LS-W4-270M-Micro-Hashtags** is a compact, high-efficiency 270M parameter Micro Language Model (MLM) developed by **Web4**.  
It is designed specifically for environments with limited computational resources, such as mobile devices, desktop apps, and browsers — with **no server required**.

Its primary function is to generate relevant, trending, and semantically meaningful hashtags from input text in real time.  
It runs **fully offline**, supports **WebAssembly/WebGPU**, and enables **privacy-preserving, decentralized AI applications**.

---

## 📊 Training Data and Procedure

- **Training Dataset Size:** Over **1 million** diverse datasets  
- **Data Sources:** Social media posts, online articles, and real-world text snippets tagged with hashtags  
- **Objective:** Masked Language Modeling (MLM) + fine-tuning for hashtag prediction  
- **Performance Optimizations:** Designed for fast inference, low latency, and minimal memory footprint  

---

## ⚙️ Technical Specifications

| Specification          | Value                                              |
|------------------------|----------------------------------------------------|
| Parameters             | 270M                                               |
| Model Format           | ONNX, Web4 Custom Binary, WebAssembly              |
| Operating Environment  | On-device (mobile/desktop), Browser (WASM/WebGPU) |
| Server Requirement     | None (fully offline)                              |
| Inference Speed        | Real-time on consumer hardware                    |
| Primary Function       | Hashtag generation from freeform text             |
