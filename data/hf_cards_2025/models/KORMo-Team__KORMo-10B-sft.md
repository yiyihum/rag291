---
library_name: transformers
license: apache-2.0
---
<!-- <p align="center">
  <img src="https://github.com/MLP-Lab/KORMo-tutorial/blob/main/tutorial/attachment/kormo_logo.png?raw=true" style="width: 100%; max-width: 1100px;">
</p> -->

<p align="center">
  <img src="https://github.com/MLP-Lab/KORMo-tutorial/blob/main/tutorial/attachment/kormo_logo.svg?raw=true" style="width: 40%; max-width: 1100px;">
</p>




## 🚀 Update News
- **2025-10-13**: Official release of KORMo-10B-sft.
---
## 💡 About KORMo
**KORMo-10B** is a **10.8B parameter fully open LLM** capable of handling both **Korean and English**.  
The model, training code, and training data are all **fully open**, allowing anyone to reproduce and extend them.

- **Model Size**: 10.8B parameters  
- **Languages**: Korean / English  
- **Training Data**: Synthetic data + public datasets (approximately 3T tokens)
- **License**: Apache 2.0

```md
KORMo는 비영어권 최초의 Fully Open Source LLM으로, 공익적 활용을 목표로 탄생했습니다.
우리는 누구나 세계 수준의 언어모델을 직접 만들고 발전시킬 수 있는 환경을 만들고자 합니다.
KORMo의 주요 특징은 다음과 같습니다:

1. From scratch 학습으로 설계된 10B급 한–영 추론 언어모델입니다.
2. 학습 데이터, 코드, 모델 체크포인트와 튜토리얼을 100% 공개하여, 누구나 SOTA에 근접한 모델을 직접 재현하고 확장할 수 있습니다.
3. 총 3.7T 토큰 규모의 학습 데이터를 공개합니다. 특히 지금까지 한 번도 공개된 적 없는 초고품질 전주기 한국어 데이터(사전학습, 사후학습, 일반형, 추론형, 강화학습 등)를 제공합니다.
4. 이 모든 작업은 KAIST 문화기술대학원 MLP연구실의 학부·석사생 8명이 협력하여 진행했으며, 45장에 달하는 논문으로 정리했습니다.

지금까지 한국어 모델을 써보면, 벤치마크 점수는 좋은데 실사용에서는 어딘가 이상하거나,
튜닝만 하면 모델이 망가지는 경험을 하셨을 겁니다. 답답하셨죠?

KORMo는 그런 문제를 정면으로 해결합니다.
모든 중간 모델과 사후학습 데이터를 함께 공개하기 때문에, 사용자는 베이스 모델 위에 자신만의 데이터를 얹어 원하는 방향으로 강화학습·튜닝을 진행할 수 있습니다.
👉 "좋은 한국어 모델을 갖고 싶다면, 이제 직접 만들어보세요. 코랩 무료 GPU로도 튜닝됩니다! 🤗"
```

---

## 🔗 Links

- 📖 **Technical Report**: [👉 Paper](https://huggingface.co/papers/2510.09426) , [👉 한국어 요약ppt](https://github.com/MLP-Lab/KORMo-tutorial/blob/main/20251009_MLP_KORMo(Korean).pdf)
- 🤗 **Hugging Face**: [👉 Model Download](https://huggingface.co/KORMo-Team)  
- 💻 **GitHub Repository**: [👉 Training and Inference Code](https://github.com/MLP-Lab/KORMo-tutorial)
- 🔉 **Tutorial**: [👉 Instruction Tuning over google colab](https://colab.research.google.com/github/MLP-Lab/KORMo-tutorial/blob/main/tutorial/02.sft_qlora.ipynb) [👉 Youtube Tutorial](https://www.youtube.com/@MLPLab)

---


## 📈 Benchmark Performance

### 📊 Quantitative Evaluation

| Benchmark | **KORMo-10B** | smolLM3-3B | olmo2-7B | olmo2-13B | kanana1.5-8B | qwen3-8B | llama3.1-8B | gemma3-4B | gemma3-12B |
|:-----------|---------------:|-----------:|---------:|---------:|------------:|--------:|-----------:|---------:|----------:|
| **🇺🇸 English Benchmarks** |||||||||||
| arc_challenge | 58.96 | 55.55 | 59.13 | 61.01 | 56.48 | 63.82 | 54.61 | 53.58 | 63.82 |
| arc_easy | 85.48 | 83.21 | 85.06 | 86.57 | 82.74 | 87.50 | 84.01 | 82.83 | 87.37 |
| boolq | 83.46 | 82.17 | 84.50 | 86.48 | 84.53 | 87.71 | 81.87 | 80.70 | 86.61 |
| copa | 93.00 | 91.00 | 92.00 | 93.00 | 88.00 | 92.00 | 93.00 | 89.00 | 95.00 |
| gpqa_main | 30.13 | 26.79 | 26.34 | 29.24 | 29.24 | 30.13 | 23.44 | 30.13 | 35.71 |
| hellaswag | 60.25 | 56.78 | 61.52 | 65.02 | 59.93 | 59.54 | 60.96 | 57.56 | 63.67 |
| mmlu | 67.96 | 61.37 | 62.81 | 66.85 | 63.73 | 76.95 | 65.03 | 59.60 | 73.58 |
| mmlu_global | 63.44 | 57.52 | 59.88 | 63.99 | 60.21 | 75.05 | 61.30 | 57.23 | 70.23 |
| mmlu_pro | 40.18 | 34.94 | 27.29 | 32.50 | 34.93 | 56.58 | 36.23 | 27.79 | 37.07 |
| mmlu_redux | 69.00 | 62.95 | 63.53 | 68.37 | 65.88 | 78.19 | 65.86 | 60.86 | 75.25 |
| openbookqa | 39.00 | 36.40 | 39.00 | 39.60 | 36.80 | 39.20 | 39.00 | 37.00 | 40.20 |
| piqa | 81.12 | 78.45 | 80.79 | 82.64 | 80.30 | 79.05 | 80.90 | 79.49 | 82.59 |
| social_iqa | 52.81 | 50.72 | 55.89 | 57.57 | 57.01 | 56.96 | 53.12 | 51.84 | 56.45 |
| **English Avg.** | **63.45** | 59.83 | 61.36 | 64.06 | 61.52 | 67.90 | 61.49 | 59.05 | 66.73 |
| **🇰🇷 Korean Benchmarks** |||||||||||
| click | 55.29 | 46.97 | 37.79 | 41.80 | 62.76 | 60.70 | 49.22 | 49.62 | 62.21 |
| csatqa | 38.00 | 26.67 | 19.33 | 24.67 | 44.67 | 52.00 | 28.67 | 28.67 | 31.33 |
| haerae | 68.29 | 55.82 | 31.62 | 37.58 | 80.75 | 67.19 | 53.25 | 60.68 | 74.34 |
| k2_eval | 84.89 | 75.23 | 49.54 | 63.43 | 84.72 | 84.72 | 76.62 | 76.39 | 85.42 |
| kobest | 75.05 | 69.13 | 57.27 | 59.02 | 81.93 | 80.05 | 70.55 | 69.33 | 77.70 |
| kobalt | 22.86 | 15.86 | 11.43 | 13.14 | 26.29 | 26.57 | 17.43 | 15.57 | 23.86 |
| kmmlu | 46.48 | 38.52 | 33.05 | 31.24 | 48.86 | 56.93 | 40.75 | 39.84 | 51.60 |
| mmlu_global (ko) | 55.16 | 44.15 | 34.00 | 36.95 | 52.65 | 61.95 | 46.34 | 46.33 | 59.68 |
| kr_clinical_qa | 77.32 | 53.97 | 48.33 | 46.22 | 65.84 | 80.00 | 63.54 | 60.00 | 77.22 |
| **Korean Avg.** | **58.15** | 47.37 | 35.82 | 39.34 | 60.94 | 63.35 | 49.60 | 49.60 | 60.37 |


### 📝 Qualitative Evaluation (LLM-as-a-Judge)

| Benchmark | KORMo-10B | smolLM3-3B | olmo2-7B | olmo2-13B | kanana1.5-8B | qwen3-8B | llama3.1-8B | exaone3.5-8B | gemma3-12B |
|:----------|---------:|----------:|---------:|---------:|------------:|--------:|------------:|-------------:|-----------:|
| MT-Bench (EN) | 8.32 | 7.15 | 7.32 | 7.64 | 8.45 | 8.70 | 6.32 | 8.15 | 8.70 |
| KO-MT-Bench (KO) | 8.54 | - | - | - | 8.02 | 8.16 | 4.27 | 8.13 | 8.51 |
| LogicKor (KO) | 8.96 | - | - | - | 8.94 | 8.63 | 6.45 | 9.20 | 8.46 |
| **Average** | **8.61** | - | - | - | **8.47** | **8.50** | **5.68** | **8.49** | **8.56** |

---

## 📦 Installation

```bash
git clone https://github.com/MLP-Lab/KORMo-tutorial.git
cd KORMo-tutorial
bash setup/create_uv_venv.sh
source .venv_kormo/bin/activate
```

---
## 🚀 Inference Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "KORMo-Team/KORMo-10B-sft"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

messages = [
    {"role": "user", "content": "What happens inside a black hole?"}
]

chat_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)

inputs = tokenizer(chat_prompt, return_tensors="pt").to(model.device)

with torch.inference_mode():
    output_ids = model.generate(
        **inputs,
        max_new_tokens=1024,
    )

response = tokenizer.decode(output_ids[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
print("Assistant:", response)
```

## 🧠 Enabling Thinking Mode

If you want to enable the **thinking** mode, simply set `enable_thinking=True`:

```python
chat_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True
)
```
---

## Limitation
The model has not yet been safety-tuned or preference-aligned, which may lead to suboptimal performance or undesired repetitions in complex reasoning tasks.

## Contact
- KyungTae Lim, Professor at KAIST. `ktlim@kaist.ac.kr`


## Acknowledgments 
- This work was supported by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government(MSIT) (RS-2025-02653113, High-Performance Research AI Computing Infrastructure Support at the 2 PFLOPS Scale)

## Citation

```text
@misc{KORMo,
  author = {Minjun Kim, Hyeonseok Lim, Hangyeol Yoo, Inho Won, Seungwoo Song, Minkyung Cho, Junghun Yuk, Changsu Choi, Dongjae Shin, Huije Lee, Hoyun Song, Alice Oh, and KyungTae Lim},
  title = {KORMo: Korean Open Reasoning Model for Everyone},
  year = {2025},
  publisher = {GitHub},
  journal = {Technical Report},
  paperLink = {\url{https://arxiv.org/abs/2510.09426}},
 },
}
```
