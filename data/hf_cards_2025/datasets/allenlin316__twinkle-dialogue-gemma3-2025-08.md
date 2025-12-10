---
pretty_name: Twinkle Dialogue (Gemma-3-12B-it, 2025-08)
tags:
- dialog
- instruction-tuning
- sft
- openai-messages
license: cc-by-4.0
task_categories:
- text-generation
dataset_info:
  features:
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 123456
    num_examples: 1000
  download_size: 123456
  dataset_size: 123456
language:
- zh
---

# Twinkle Dialogue (Gemma-3-12B-it, 2025-08)
<div align="left" style="line-height: 1;">
  <a href="https://discord.gg/Cx737yw4ed" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-Twinkle%20AI-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/twinkle-ai" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Twinkle%20AI-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

本資料集由 **Gemma-3-12B-it（Twinkle AI 社群服務）** 生成之對話資料，採用 **OpenAI Chat Messages** 格式（`.jsonl`），並整合：
- Reference-free（由 seed 派生單輪問答）
- Reference-based（依據參考文本生成單輪問答）

> 檔案路徑：`data/train.jsonl`（選配：`data/train.parquet`）

## 結構說明
- 每列為一筆樣本：`{"id": "...", "type": "...", "messages": [{"role":"system","content":"..."}, ...]}`
- 訓練時可擷取第一個 `user` 與對應 `assistant` 形成 (instruction, response) pair，或直接使用 chat 格式的 trainer。

## 來源與限制
- Model: gemma-3-12b-it（Twinkle AI 社群）
- 語言：繁體中文
- 使用情境：教學示範用；不代表專業意見

## 授權
- 建議使用 **CC BY 4.0**；若另有需求請調整 `license` 欄位。
