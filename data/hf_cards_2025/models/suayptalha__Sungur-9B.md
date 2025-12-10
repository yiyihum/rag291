---
library_name: transformers
license: gemma
language:
- tr
base_model:
- ytu-ce-cosmos/Turkish-Gemma-9b-v0.1
tags:
- gemma2
- instruction
- DPO
- Turkish
- axolotl
- sungur
---

<img src="./Sungur.png"/>

# Sungur-9B

Sungur-9B is a Turkish-specialized large language model derived from ytu-ce-cosmos/Turkish-Gemma-9b-v0.1, which itself is based on Gemma-2-9b. The model was further trained using a 7k-sample Direct Preference Optimization (DPO) dataset created via translation and fine-tuned with 4-bit QLoRA, refining its alignment with human preferences.

Sungur-9B is designed for Turkish text generation tasks, producing coherent and contextually appropriate outputs. Its training process enables it to deliver fluent, context-aware responses.

## Turkish Evaluation Benchmark Results (via `malhajar17/lm-evaluation-harness_turkish`)

| Task / Dataset       | **suayptalha/Sungur-9B** | Qwen/Qwen2.5-7B-Instruct | google/gemma-2-9b-it | ytu-ce-cosmos/Turkish-Gemma-9b-v0.1 | google/gemma-3-12b-it | Qwen/Qwen2.5-14B-it | Qwen/Qwen2.5-32B-Instruct | google/gemma-2-27b-it | google/gemma-3-27b-it | Qwen/Qwen2.5-72B-Instruct | meta-llama/Llama-3-1-70B-Instruct |
| -------------------- | ------------------------ | ------------------------ | -------------------- | ----------------------------------- | --------------------- | ------------------- | ------------------------- | --------------------- | --------------------- | ------------------------- | --------------------------------- |
| **MMLU (tr)**        | **61.19**                | 56.31                    | 61.07                | 63.85                               | 63.92                 | 65.28               | 70.93                     | 66.49                 | 70.20                 | 77.28                     | 74.00                             |
| **Truthful_QA (tr)** | **55.21**                | 55.99                    | 55.77                | 54.21                               | 57.16                 | 59.00               | 57.87                     | 57.45                 | 57.06                 | 59.86                     | 51.41                             |
| **ARC (tr)**         | **55.03**                | 42.06                    | 56.31                | 59.64                               | 60.67                 | 50.00               | 57.00                     | 63.65                 | 66.98                 | 61.52                     | 59.64                             |
| **Hellaswag (tr)**   | **64.36**                | 44.71                    | 56.48                | 64.19                               | 62.00                 | 52.22               | 57.04                     | 63.86                 | 66.58                 | 61.98                     | 64.31                             |
| **Gsm8K (tr)**       | **74.49**                | 64.16                    | 63.10                | 73.42                               | 72.06                 | 76.77               | 77.83                     | 76.54                 | 77.52                 | 83.60                     | 66.13                             |
| **Winogrande (tr)**  | **63.43**                | 59.66                    | 62.09                | 64.53                               | 61.77                 | 58.77               | 61.77                     | 65.40                 | 65.80                 | 61.92                     | 66.90                             |

## Usage

### Pipeline

```py
from transformers import pipeline

pipe = pipeline("text-generation", model="suayptalha/Sungur-9B")

messages = [
    {"role": "user", "content": "Bana kuantum dolanıklığını çok kısaca anlat."},
]
pipe(messages)[0]["generated_text"][-1]["content"]

#Kuantum dolanıklığı, birbirine bağlı iki parçacığın, ne kadar uzakta olsalar bile, birinin durumunun diğerini anında etkilemesi olarak düşünülebilir.

#Örneğin, bir parçacık "yukarı" döndüğünde, dolanık olduğu diğer parçacık kesinlikle "aşağı" dönecektir. Bu değişim anında gerçekleşir, ışık hızını aşarak. Fakat bu durum, uzaktaki parçacığın bir "bilgiyi" aldığını göstermez, çünkü ölçüm sonucu zaten önceden belirlenmiştir.

#Dolanıklık, kuantum dünyasının tuhaf ve ilginç bir özelliğidir ve bilgi teknolojileri (kuantum bilgisayarlar) gibi alanlarda devrim yaratma potansiyeline sahiptir.
```

### AutoModelForCausalLM
```py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "suayptalha/Sungur-9B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "user", "content": "5x + 1 = 16. x'i bul."},
]

inputs = tokenizer.apply_chat_template(
	messages,
	add_generation_prompt=True,
	tokenize=True,
	return_dict=True,
	return_tensors="pt",
).to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=2048,
    do_sample=False,
    eos_token_id=tokenizer.eos_token_id
)

output_ids = outputs[0]
input_length = inputs["input_ids"].shape[1]
generated_tokens = output_ids[input_length:]
answer = tokenizer.decode(generated_tokens, skip_special_tokens=True)
print(answer)

# 5x + 1 = 16 denklemini çözmek için şu adımları izleyelim:

# 1. **Sabit terimi eşitliğin diğer tarafına taşıyalım:**
#    5x = 16 - 1
#    5x = 15

# 2. **x'i yalnız bırakmak için her iki tarafı 5'e bölelim:**
#    x = 15 / 5
#    x = 3

# **Sonuç:** x = 3

# Denklemi kontrol edelim:
# 5 * 3 + 1 = 15 + 1 = 16 (Doğru)
```

## Acknowledgments
- Thanks to [ytu-ce-cosmos](https://huggingface.co/ytu-ce-cosmos) for their amazing Turkish-Gemma-9b-v0.1 model.
- Thanks to [axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) for making the repository I used to make this model.
- Thanks to all Turkish open source AI community.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Citation

```
@misc{sungur_collection_2025,
  title        = {Sungur (Hugging Face Collection)},
  author       = {Şuayp Talha Kocabay},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/collections/suayptalha/sungur-68dcd094da7f8976cdc5898e}},
  note         = {Turkish LLM family and dataset collection}
}
```

## Support

<a href="https://www.buymeacoffee.com/suayptalha" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---
license: gemma2
---