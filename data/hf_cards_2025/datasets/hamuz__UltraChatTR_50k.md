---
license: mit
task_categories:
- text-generation
language:
- tr
tags:
- nlp
- dialogue
- turkish
- llm-sft
- llm
- fine-tuning
- chat
- instruction-tuning
pretty_name: UltraChatTR 50K – Türkçe Diyalog Veri Seti
size_categories:
- 10K<n<100K
---

# 💬 UltraChat 50K – Türkçe Diyalog Veri Seti

UltraChat 50K, **orijinal [UltraChat](https://github.com/thunlp/UltraChat)** veri setinden türetilmiş,  
**55.046 Türkçe diyalog örneği** içeren açık kaynak bir veri setidir.  
Veri, büyük dil modellerinin Türkçe konuşma anlayışı ve cevap kalitesini geliştirmek için  
**fine-tuning (SFT)** amacıyla düzenlenmiştir.

---

## 📘 Veri Künyesi

| Özellik | Açıklama |
|----------|-----------|
| **Toplam Satır Sayısı** | 55.046 |
| **Veri Formatı** | JSON Lines, Parquet |
| **Alanlar** | `instruction`, `input`, `output` |
| **Dil** | Türkçe 🇹🇷 |
| **Lisans** | MIT |
| **Kaynak** | [UltraChat](https://github.com/thunlp/UltraChat) , [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) | 
| **Kullanım Alanı** | Supervised Fine-Tuning (SFT), Instruction Tuning |

---

## 📃 Örnek Kayıt

```json
{
  "prompt": "Kanada'daki deniz biyolojisi için en iyi kolejler nelerdir?",
  "messages": [
    {
      "role": "user",
      "content": "Kanada'daki deniz biyolojisi için en iyi kolejler nelerdir?"
    },
    {
      "role": "assistant",
      "content": "İşte Kanada'daki deniz biyolojisi için en iyi kolejler:\n\n1. Dalhousie Üniversitesi\n2. Newfoundland Anıt Üniversitesi\n3. British Columbia Üniversitesi\n4. Victoria Üniversitesi\n5. Manitoba Üniversitesi\n6. Guelph Üniversitesi\n7. Toronto Üniversitesi\n8. Simon Fraser Üniversitesi\n9. Waterloo Üniversitesi\n10. Windsor Üniversitesi."
    }
  ],
  "prompt_id": "f9d9b254a36bc99fd3ca9ca11175cb360fade67422b69e21eaafc0b84037ffb1"
}