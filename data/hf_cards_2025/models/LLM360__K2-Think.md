---
base_model: Qwen/Qwen2.5-32B
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
---

# K2-Think: A Parameter-Efficient Reasoning System

📚 [Paper](https://huggingface.co/papers/2509.07604) - 📝 [Code](https://github.com/MBZUAI-IFM/K2-Think-SFT) - 🏢 [Project Page](https://k2think.ai)

<center><img src="banner.png" alt="k2-think-banner"/></center>

<br>

K2-Think is a 32 billion parameter open-weights general reasoning model with strong performance in competitive mathematical problem solving. 

# Quickstart

### Transformers
You can use `K2-Think` with Transformers. If you use `transformers.pipeline`, it will apply the chat template automatically. If you use `model.generate` directly, you need to apply the chat template mannually.

```python
from transformers import pipeline
import torch

model_id =  "LLM360/K2-Think"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "what is the next prime number after 2600?"},
]

outputs = pipe(
    messages,
    max_new_tokens=32768,
)
print(outputs[0]["generated_text"][-1])
```

---

# Evaluation & Performance
Detailed evaluation results are reported in out [Tech Report](https://k2think-about.pages.dev/assets/tech-report/K2-Think_Tech-Report.pdf)

## Benchmarks (pass\@1, average over 16 runs)

| Domain  | Benchmark        | K2-Think |
| ------- | ---------------- | -----------: |
| Math    | AIME 2024        |        90.83 |
| Math    | AIME 2025        |        81.24 |
| Math    | HMMT 2025        |        73.75 |
| Math    | OMNI-Math-HARD   |        60.73 |
| Code    | LiveCodeBench v5 |        63.97 |
| Science | GPQA-Diamond     |        71.08 |

---

## Inference Speed

We deploy K2-THINK on Cerebras Wafer-Scale Engine (WSE) systems, leveraging the world’s largest processor and speculative decoding to achieve unprecedented inference speeds for our 32B reasoning system.  

| Platform                          | Throughput (tokens/sec) | Example: 32k-token response (time) |
| --------------------------------- | ----------------------: | ---------------------------------: |
| **Cerebras WSE (our deployment)** |             **\~2,000** |                         **\~16 s** |
| Typical Cloud Service setup   |                   \~200 |                            \~160 s |

---

## Safety Evaluation

Aggregated across four safety dimensions (**Safety-4**):

| Aspect                          | Macro-Avg |
| ------------------------------- | --------: |
| High-Risk Content Refusal       |     0.83 |
| Conversational Robustness       |     0.89 |
| Cybersecurity & Data Protection |     0.56 |
| Jailbreak Resistance            |     0.72 |
| **Safety-4 Macro (avg)**        | **0.75** |

---

# Terms of Use

We have employed various techniques to reduce bias, harmful outputs, and other risks in the model. While these efforts help improve safety and reliability, the model, like all Large Language Models, may still generate inaccurate, misleading, biased, or otherwise undesirable content. By downloading, using, or interacting with this model, you acknowledge these limitations and agree to the following:

1. **Prohibited Uses**  
   - You may **not** use this model for any **illegal, unlawful, or harmful activities**, including but not limited to fraud, abuse, harassment, privacy violations, or the creation/dissemination of malicious content.  

2. **User Responsibility**  
   - You are solely responsible for how you use the model and for any outcomes that result from its use.  
   - The authors and institutions involved in releasing this model do **not** accept liability for any consequences arising from its use.  

3. **No Warranty**  
   - The model is provided **“as is” without any warranties or guarantees**.  
---

# Citation

```bibtex
@misc{cheng2025k2thinkparameterefficientreasoning,
      title={K2-Think: A Parameter-Efficient Reasoning System}, 
      author={Zhoujun Cheng and Richard Fan and Shibo Hao and Taylor W. Killian and Haonan Li and Suqi Sun and Hector Ren and Alexander Moreno and Daqian Zhang and Tianjun Zhong and Yuxin Xiong and Yuanzhe Hu and Yutao Xie and Xudong Han and Yuqi Wang and Varad Pimpalkhute and Yonghao Zhuang and Aaryamonvikram Singh and Xuezhi Liang and Anze Xie and Jianshu She and Desai Fan and Chengqian Gao and Liqun Ma and Mikhail Yurochkin and John Maggs and Xuezhe Ma and Guowei He and Zhiting Hu and Zhengzhong Liu and Eric P. Xing},
      year={2025},
      eprint={2509.07604},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2509.07604}, 
}
```