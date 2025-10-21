---
pretty_name: Simon-Liu/gemma-270m-medium-qa (Gemma-3-27B-it, ADK Reference)
tags:
- dialog
- instruction-tuning
- sft
- openai-messages
- reference-based
- reference-free
license: cc-by-4.0
task_categories:
- text-generation
language:
- zh
---

本資料集包含由 ** gemini-2.0-flash ** 生成的對話資料，採用 **OpenAI Chat Messages** 格式（`.jsonl`）。資料來源結合：
- **Reference-free**：由 seed 派生的單輪問答。
- **Reference-based**：依據參考文本生成單輪問答。

> 檔案路徑：`data/train.jsonl`（選配：`data/train.parquet`）

## 結構說明
- 每列為一筆樣本：`{"id": "...", "type": "...", "seed": "...", "context": "...", "messages": [{"role":"user","content":"..."}, {"role":"assistant","content":"..."}]}`
- `type` 欄位標示資料來源：`reference_free` 或 `reference_based`。
- `seed` 欄位儲存 Reference-free 的原始 seed 指令，或 Reference-based 的參考文本片段。
- `context` 欄位僅在 `reference_based` 資料中包含完整的參考文本片段。
- 訓練時可直接使用 `messages` 欄位的對話格式進行訓練。

## 來源與限制
- Model: gemini-2.0-flash
- 語言：繁體中文（生成內容），部分參考文本為英文。
- 使用情境：教學示範用；不代表專業意見。
- **重要**：Reference-based 資料的問題和答案均從參考文本中生成，答案不應超出參考文本範圍。

## 授權
- 建議使用 **CC BY 4.0**；若另有需求請調整 `license` 欄位。
