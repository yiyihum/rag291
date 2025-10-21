---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-32B-Instruct/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-32B
tags:
- chat
library_name: transformers
---

# Flux-Japanese-Qwen2.5-32B-Instruct-V1.0
[**English**] [[Japanese](./README-ja.md)]

Flux-Japanese-Qwen2.5-32B-Instruct-V1.0 is a 32 billion parameter open-weights models with strong performance in Japanese knowledge, reasoning and language. It is trained based on the Qwen2.5-32B-Instruct and under the Apache 2.0 opensource licence

# 🏆 Open-Japanese-LLM-Leaderboard Rank-1
On the [Open LLM Japanese LLM Leaderboard](https://huggingface.co/spaces/deep-analysis-research/open-japanese-llm-leaderboard), Qwen2.5-32B-Instruct scores 0.6553, compared to the former top-ranked D2IL-Japanese-Qwen2.5-32B-Instruct-v0.1 at 0.7100, and Flux-Japanese-Qwen2.5-32B-V1.0 at 0.7417. Compared with the original Qwen2.5-32B-Instruct, Flux-Japanese-Qwen2.5-32B-v1.0 demonstrates significant gains across most tasks, with especially strong improvements in FA (Fundamental Analysis, 基礎分析), SUM (Summarization, 要約), and CG (Code Generation, コード生成).
| Tasks                              | Qwen2.5-32B-Instruct | D2IL-Japanese-Qwen2.5-32B-Instruct-v0.1 | Flux-Japanese-Qwen2.5-32B-Instruct-V1.0 |
|------------------------------------|----------------------|-----------------------------------------|------------------------------------------|
| NLI - 自然言語推論                  | 0.8106               | 0.8793                                  | 0.8846 (+0.0740)                         |
| QA - 質問応答                       | 0.541                | 0.5897                                  | 0.5965 (+0.0555)                         |
| RC - 読解力                         | 0.9047               | 0.9005                                  | 0.9261 (+0.0214)                         |
| MC - 多肢選択式質問応答              | 0.8966               | 0.9139                                  | 0.9128 (+0.0162)                         |
| EL - エンティティリンキン            | 0.5894               | 0.6782                                  | 0.6975 (+0.1081)                         |
| FA - 基礎分析                       | 0.2737               | 0.4321                                  | 0.5185 (+0.2448)                         |
| MR - 数学的推論                     | 0.944                | 0.938                                   | 0.9420 (-0.0020)                         |
| MT - 機械翻訳                       | 0.8479               | 0.7954                                  | 0.8389 (-0.0090)                         |
| HE - 試験問題                       | 0.7757               | 0.7902                                  | 0.7987 (+0.0230)                         |
| CG - コード生成                     | 0.5281               | 0.6084                                  | 0.7610 (+0.2329)                         |
| SUM - 要約                          | 0.097                | 0.2843                                  | 0.2827 (+0.1857)                         |
| **Average**                         | **0.6553**           | **0.71**                                | **0.7417 (+0.0864)**                     |


# 🚀 Consistent General Performance
While Flux-Japanese-Qwen2.5-32B-Instruct-V1.0 has been specifically tuned for Japanese, its performance on general capabilities and English tasks remains within 1% of Qwen2.5-32B-Instruct, indicating negligible impact. The evaluation is based on [simple-evals](https://github.com/deep-analysis-research/simple-evals).

| Tasks               | Dataset        | Qwen2.5-32B-Instruct | Flux-Japanese-Qwen2.5-32B-Instruct-V1.0 |
|---------------------|----------------|----------------------|------------------------------------------|
| General Tasks       | MMLU-redux     | 80.37                | 80.03 (-0.34)                            |
|                     | GPQGA-Diamond  | 46.11                | 47.32 (+1.21)                            |
|                     | MMLU           | 82.84                | 83.39 (+0.55)                            |
| Math Tasks          | MATH-500       | 78.14                | 78.50 (+0.36)                            |
|                     | AIME24         | 17.06                | 17.92 (+0.86)                            |
|                     | AIME25         | 16.25                | 14.58 (-1.67)                            |
|                     | MT-AIME24      | 12.73                | 12.97 (+0.24)                            |
| Multilingual Tasks  | Multi-IF       | 71.85                | 63.45 (-8.40)                            |
|                     | INCLUDE        | 65.16                | 64.64 (-0.52)                            |
|                     | MMMLU          | 73.43                | 74.08 (+0.65)                            |
| Coding Tasks        | HumanEval      | 87.93                | 86.51 (-1.42)                            |
| Alignment Tasks     | IFEval         | 78.37                | 77.46 (-0.91)                            |
| **Average**             |                | **59.17**                | **58.40 (-0.77)**                            |


# ⚙️ Technical Development

<center><img src="tech-dev.png" alt="technical-development"/></center>

- **Phase 1: Interpretability Analysis & Pinpoint Tuning** — For Japanese Knowledge, Reasoning, and Language, leverage mechanistic interpretability techniques to identify independent pathways/circuits, and apply targeted pinpoint tuning to only 5% of the parameters. This produces three expert models specialized respectively in Japanese knowledge, reasoning, and language.
- **Phase 2: Pinpoint Merging** — Perform pinpoint parameter merging on the three expert models to obtain a unified model that reaches expert-level performance across Japanese knowledge, reasoning, and language [[Code of Pinpoint Merging](https://github.com/deep-analysis-research/SLTA)].

# 🚩 Quickstart
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "Deep-Analysis-Research/Flux-Japanese-Qwen2.5-32B-V1.0",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Deep-Analysis-Research/Flux-Japanese-Qwen2.5-32B-V1.0")

prompt = "大規模言語モデルについて簡単に紹介してください。"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```
# 💡 Terms of Use
We have employed various techniques to reduce bias, harmful outputs, and other risks in the model. While these efforts help improve safety and reliability, the model, like all Large Language Models, may still generate inaccurate, misleading, biased, or otherwise undesirable content. By downloading, using, or interacting with this model, you acknowledge these limitations and agree to the following:
1. Prohibited Uses
   - You may NOT use this model for any illegal, unlawful, or harmful activities, including but not limited to fraud, abuse, harassment, privacy violations, or the creation/dissemination of malicious content.
2. User Responsibility
   - You are solely responsible for how you use the model and for any outcomes that result from its use.
   - The authors and institutions involved in releasing this model do NOT accept liability for any consequences arising from its use.
3. No Warranty
   - The model is provided “as is” without any warranties or guarantees.