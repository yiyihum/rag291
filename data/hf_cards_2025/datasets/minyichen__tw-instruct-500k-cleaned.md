---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
language:
- zh
- en
tags:
- Taiwan
- ROC
- tw
- zh-tw
- chat
- instruction
pretty_name: Common Task-Oriented Dialogues in Taiwan
size_categories:
- 100K<n<1M
---

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->
此資料集為 [lianghsun/tw-instruct](https://huggingface.co/datasets/lianghsun/tw-instruct) 的修正版，資料筆數為 **499148** 筆。<br>
主要修正以下兩點: <br>
(1) 簡轉繁套件 OpenCC 轉換的一些缺漏及錯誤。
(2) 刪除 模型回答無窮回覆 的資料

**(1) 錯誤包含但不限於**:
1. 自「制」果醬 → 自「製」果醬
2. 「酸奶」 → 「優酪乳」
3. 小「貼士」 → 小「提醒」
4. 「俯臥撐」 → 「伏地挺身」
5. QR「碼」 → QR 「code」
6. 「幹」擾 → 「干」擾
7. 濃「鬱」 → 濃「郁」
8. 適「閤」 → 適「合」
9. 「瞭」解 → 「了」解
10. 「引」數 → 「參」數

以上僅為部分舉例。而在修改過程中，並非只作字詞轉換，會考慮到許多包含 關鍵字 前後語的情況<br>

**舉例說明:**<br>
例如上述範例1：<br>
法「制」作業 並不會 轉換為 法「製」作業。


**此資料集 已知但未處理 的錯誤如以下**:
1. **生抽**、**老抽** 未作轉換
2. **程序**、**程式** 的誤用

**(2) 模型回答無窮回覆**<br>
刪除852筆 無窮回覆資料，刪除資料舉例如下:<br>

```bash
{
  'conversations':
    [
      {
        'from': 'human',
        'value': '請問如何正確填寫綜合所得稅申報表？能否提供相關的稅務規定和最新的稅率資訊？'
      },
      {
        'from': 'gpt',
        'value': '填寫綜合所得稅申報表時，需要準備好相關的收入證明、扣除專案證明等材料，並按照以下步驟進行：\n\n1. **確認身份**：確認自己是否需要申報綜合所得稅。一般來說，如果你的全年綜合所得淨額超過新臺幣 54 萬元，就需要申報。\n\n2. **準備相關檔案**：包括但不限於薪資所得憑證、利息所得憑證、股利所得憑證、租金收入憑證、營利事業所得憑證、執行業務所得憑證、退職所得憑證、執行業務所得憑證、執行業務所得憑證、執行業務所得憑證、執行業務所得憑證、執行業務所得憑證、....'
      }
    ]
}
```

### Dataset structure

新增欄位說明
1. **converted_conversations** : 經二次修改轉換後的對話。
2. **converted_string** : 紀錄轉換的詞語。<br>
    conv_idx = 0 為 input、conv_idx = 1 為 output； old 代表 轉換前的字詞， new 代表轉換後的字詞。


台灣的訓練資料需要大家一同努力，希望大家可以貢獻自己的力量。<br>
<a href="https://discord.gg/fj6WbHMvfs" target="_blank">[👋歡迎加入 Discord 討論，我們正在找人一塊擴充這個對話集🎉]</a>

### Dataset Sources

<!-- Provide the basic links for the dataset. -->
- **Repository:** [minyichen/tw-instruct-500k-cleaned](https://huggingface.co/datasets/minyichen/tw-instruct)

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
如果您有使用本資料集，請務必在模型下載處的公開頁面上標註來源；如有模型有在 Hugging Face 上架，請務必在 metadata 標註使用 `lianghsun/tw-instruct-500k` 及 `minyichen/tw-instruct-500k-cleaned`。

## Original Dataset Card Author

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Original Dataset Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang/?locale=en_US)

## Revised Dataset Card Authors

[Min Yi Chen](https://www.linkedin.com/in/min-yi-chen-68b6ab130/?locale=en_US)

## Revised Dataset Card Contact

[Min Yi Chen](https://www.linkedin.com/in/min-yi-chen-68b6ab130/?locale=en_US)