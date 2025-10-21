---
license: mit
language:
- tr
tags:
- turkish
- wikipedia
- chat
- instruction-tuning
- kamu-kurumlari
- tarih
- fine-tuning
- llm
pretty_name: Türkçe Kamu Kurumları ve Tarih Sohbet Veri Seti
size_categories:
- 1K<n<10K
---

# Türkçe Kamu Kurumları ve Tarih Sohbet Veri Seti

Bu veri seti, Türkiye'deki kamu kurumları, bakanlıklar, devlet organları, resmi semboller ve tarihi figürler hakkında yapılandırılmış Türkçe sohbet verileri içermektedir. Veriler, güvenilir ve tarafsız bir kaynak olan Türkçe Vikipedi'den otomatik olarak çıkarılmış ve büyük dil modellerini (LLM) ince ayar (fine-tuning) için uygun bir formata dönüştürülmüştür.

Her bir örnek, bir "sistem" talimatı, bir "kullanıcı" sorgusu ve bir "yardımcı" (assistant) cevabı içeren bir sohbet formatındadır. Bu yapı, özellikle talimat takibi ve diyalog yeteneklerini geliştirmek amacıyla tasarlanmıştır.

Format: Chat

Veri Tarihi: 2025

## Veri Seti Yapısı

Veri setindeki her bir örnek, aşağıdaki alanları içeren bir JSON nesnesidir:

- `id`: Örneğin benzersiz kimliği.
- `messages`: Sohbeti temsil eden bir sözlük listesi.
    - `role`: Mesajın yazarının rolü (`"system"`, `"user"`, veya `"assistant"`).
    - `content`: Mesajın metinsel içeriği.
- `metadata`: Örnek hakkında ek bilgiler içeren bir sözlük.
    - `source_url`: İçeriğin alındığı orijinal Vikipedi sayfası.
    - `source_type`: Veri kaynağının türü (örn: `"Wikipedia"`).
    - `language`: Metnin dili (örn: `"tr"`).
    - `categories`: İlgili Vikipedi kategorileri.
    - `page_type`: Sayfanın türü.
    - `extracted_at`: Verinin çıkarıldığı tarih ve saat.
    - `query`: Veriyi oluşturmak için kullanılan arama sorgusu.
    - `token_length_*`: Talimat, çıktı ve toplam token uzunlukları.

### Örnek

```json
{
  "id": "mustafa-kemal-ataturk-005",
  "messages": [
    {
      "role": "system",
      "content": "Sen, Türkiye ve bazı diğer ülkelerdeki kamu kurumları, bakanlıklar, devlet organları, resmi semboller, tarihçeler ve görevler hakkında detaylı ve akademik bilgiler veren bir uzmansın. Verdiğin bilgiler tarafsız, doğru ve güvenilir kaynaklara dayalı olmalı. Yanıtlarını açık, kısa paragraflar veya madde listeleri hâlinde ver, tarihleri, kanunları, sembollerin anlamlarını ve önemli değişiklikleri vurgula. Kullanıcıya kurumların görevleri, kuruluş tarihçesi, yetki alanları ve sembollerini kapsamlı biçimde açıkla."
    },
    {
      "role": "user",
      "content": "Mustafa Kemal Atatürk"
    },
    {
      "role": "assistant",
      "content": "Türkiye Cumhuriyeti Devlet Demiryolları, Türk Hava Yolları, Maden Tetkik ve Arama Genel Müdürlüğü, Hıfzıssıhha Enstitüsü, Türkkuşu, Sümerbank, Etibank, Türk Tarih Kurumu, Türk Dil Kurumu, Diyanet İşleri Başkanlığı ve daha birçok kamu kurumu Atatürk tarafından veya Atatürk'ün desteğiyle kuruldu. Yerli tarım, tekstil, makine, uçak ve otomobil endüstrilerinin gelişimini destekledi. Tüm bunlara karşın Atatürk'ün hedefleri ile ülkenin sosyopolitik yapısı arasındaki uçurum kapanmadı."
    }
  ],
  "metadata": {
    "source_url": "https://tr.wikipedia.org/wiki/Mustafa_Kemal_Atat%C3%BCrk",
    "source_type": "Wikipedia",
    "language": "tr",
    "categories": ["Kategoriler", "Mustafa Kemal Atatürk", "..."],
    "page_type": "Mustafa_Kemal_Atat",
    "extracted_at": "2025-09-27 14:27:24",
    "query": "Mustafa Kemal Atatürk",
    "token_length_instruction": 4,
    "token_length_output": 84,
    "token_length_total": 88
  }
}