---
license: mit
task_categories:
- text-generation
- question-answering
language:
- tr
tags:
- turkish
- conversation
- synthetic-data
- deepseek
- instruction-tuning
- chat
- dialogue
- qa
size_categories:
- n<1K
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: category
    dtype: string
  config_name: default
  splits:
  - name: train
    num_bytes: 6793
    num_examples: 10
  download_size: 6793
  dataset_size: 6793
pretty_name: Turkish Synthetic Conversation Dataset
---

# Turkish Synthetic Conversation Dataset

## Dataset Açıklaması

Bu dataset, DeepSeek-V3 API kullanılarak üretilmiş yüksek kaliteli Türkçe sentetik konuşma ve soru-cevap verilerini içermektedir. Günlük hayat, iş hayatı, aile, alışveriş, restoran, teknoloji, sağlık, eğitim, yemek ve seyahat kategorilerinde çeşitli input-output çiftleri bulunmaktadır.

## Dataset İstatistikleri

- **Toplam Örnekler**: 10
- **Ortalama Input Uzunluğu**: 48.2 karakter
- **Ortalama Output Uzunluğu**: 81.6 karakter
- **Dil**: %100 Türkçe

### Kategori Dağılımı
- **iş-hayatı**: 2 örnekler
- **aile-hayatı**: 2 örnekler
- **yemek-restoran**: 2 örnekler
- **alışveriş**: 2 örnekler
- **günlük-hayat**: 2 örnekler

## Veri Yapısı

```json
{
  "input": "Bugün hava nasıl?",
  "output": "Hava bugün oldukça güzel, güneşli ve sıcak. Dışarı çıkmak için ideal bir gün.",
  "category": "günlük-hayat"
}
```

## Kullanım

```python
from datasets import load_dataset

dataset = load_dataset("Vyvo/Open-Conversation-TR")
print(dataset['train'][0])
```

## Citation

Bu dataset'i kullanırsanız, lütfen aşağıdaki gibi atıf yapın:

```bibtex
@dataset{vyvo_turkish_conversation_2024,
  title={Turkish Synthetic Conversation Dataset},
  author={Vyvo Labs},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Vyvo/Open-Conversation-TR}
}
```

## Lisans

MIT License

## İletişim

- GitHub: [Vyvo-Labs](https://github.com/Vyvo-Labs)
- Repository: [VyvoLLM](https://github.com/Vyvo-Labs/VyvoLLM)
