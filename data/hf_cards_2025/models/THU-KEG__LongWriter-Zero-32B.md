---
license: apache-2.0
datasets:
- THU-KEG/LongWriter-Zero-RLData
base_model:
- Qwen/Qwen2.5-32B
tags:
- reinforcement-learning
- writing
- Long Context
language:
- en
- zh
pipeline_tag: text-generation
library_name: transformers
---

# LongWriter-Zero ✍️ — Mastering Ultra-Long Text Generation via Reinforcement Learning

<p align="center">
  🤗 <a href="https://huggingface.co/datasets/THU-KEG/LongWriter-Zero-RLData" target="_blank">HF Dataset</a> • 📃 <a href="https://arxiv.org/abs/2506.18841" target="_blank">Paper</a>
</p>

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63369da91ba5d5ece24118a4/TLTwlGYvPZ1-99MgiveAA.png)

## 🔍 Table of Contents
- [🚀 LongWriter-Zero](#longwriter_zero)
- [📊 Benchmarks & Evaluation](#evaluation)
- [⚡ Quick Start](#quick_start)
- [📝 Citation](#citation)

<a name="longwriter_zero"></a>
## 🚀 LongWriter-Zero

**LongWriter-Zero** is a *purely reinforcement learning (RL)-based* large language model capable of generating coherent passages exceeding **10,000 tokens**.

Built upon **Qwen 2.5-32B-Base**, the training process includes:

- **30 billion-token continual pretraining** on long-form books and technical reports to enhance fundamental writing capabilities;
- Application of **Group Relative Policy Optimization (GRPO)** with a composite reward function:
  - *Length Reward Model (RM)* enforces the desired output length,
  - *Writing RM* scores fluency, coherence, and helpfulness,
  - *Format RM* ensures strict adherence to the `<think>…</think><answer>…</answer>` structure, and also detects repeated content to avoid redundancy;
- A dedicated prompting strategy that encourages models to *explicitly reflect* before answering, thereby improving structural planning and fine-grained length control.

The resulting model, **LongWriter-Zero-32B**, matches or surpasses the performance of 100B-scale models in ultra-long-form generation.

<a name="evaluation"></a>
## 📊 Benchmarks & Evaluation

LongWriter-Zero’s effectiveness is demonstrated on two fronts: **WritingBench**  and **Arena-Write** for automatic scoring and a **human-in-the-loop win-rate study** for pairwise quality comparison.

---

### 📝 WritingBench & Arena-Write Results


 ![image/png](https://cdn-uploads.huggingface.co/production/uploads/63369da91ba5d5ece24118a4/XF1LI5Kjuytmfrfg6ot2p.png)

>  WritingBench (scale 1–10)  & Arena-write (Elo) performance of different LLMs .  


---

### 🏆 Win-Rate Results

 ![image/png](https://cdn-uploads.huggingface.co/production/uploads/63369da91ba5d5ece24118a4/_uWmcqnMFWGLN_iQb1bdx.png)

> Donut charts showing win/tie/loss proportions against six baselines (left) and aggregated human evaluation (right).  

**Summary:** LongWriter-Zero achieves the highest automatic WritingBench score among open models and secures dominant win-rates in pairwise GPT-4.1 evaluations, confirming its superior quality in ultra-long-form generation while maintaining efficiency.


<a name="quick_start"></a>
## ⚡ Quick Start&nbsp;(HF generate)

```python
import re
model_name = "THU-KEG/LongWriter-Zero-32B"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Write a 500-word story."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=2048,
    temperature=0.6,
    do_sample=True,
    stop_strings=["<|user|>", "<|endoftext|>", "</answer>"],
    tokenizer=tokenizer
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
```
*Note: We use a slightly different tokenizer and chat template compared to the original Qwen2.5-32B-Instruct model.*

## ⚡ Quick Start&nbsp;(SGlang)

The snippet below shows how to format prompts with LongWriter-Zero’s `<think> … </think><answer> … </answer>` protocol and call the model through an SGlang-powered endpoint supporting streaming responses.

```python
import json, requests, re

def format_prompt_with_template(prompt):

    base_format_zn = r"用户与助手之间的对话。用户提供一个写作/通用任务，助手完成它。助手首先在脑海中深入思考写作/回答过程，然后向用户提供最终的书面作品。助手应进行全面而深入的规划，确保写作/通用任务的每个方面都详细且结构合理。如果写作要求存在任何不确定性或歧义，助手应反思，向自己提出澄清性问题，并探索多种写作方式，以确保最终作品达到最高质量标准。由于写作是一个既富有创造性又需要结构性的任务，助手应从多个角度进行分析，考虑连贯性、清晰度、风格、语气、受众和目的，等等因素。此外，助手还应对作品进行审查和优化，以增强其表达效果。写作思考过程和最终的书面作品分别用 <think> </think> 和 <answer> </answer> 标签包裹，如下所示：<think>详细的写作规划和结构设计，可能包括头脑风暴、大纲制定、风格选择、受众适配、反思以及质量检查等等。</think> <answer>经过充分优化和润色的最终书面作品。</answer> <|用户|>: {question} <|助手|>:"
    base_format_en = r"A conversation between the user and the assistant. The user provides a writing/general task, and the assistant completes it. The assistant first deeply thinks through the writing/answering process in their mind before providing the final written work to the user. The assistant should engage in comprehensive and in-depth planning to ensure that every aspect of the writing/general task is detailed and well-structured. If there is any uncertainty or ambiguity in the writing request, the assistant should reflect, ask themselves clarifying questions, and explore multiple writing approaches to ensure the final output meets the highest quality standards. Since writing is both a creative and structured task, the assistant should analyze it from multiple perspectives, considering coherence, clarity, style, tone, audience, purpose, etc.. Additionally, the assistant should review and refine the work to enhance its expressiveness. The writing thought process and the final written work should be enclosed within <think> </think> and <answer> </answer> tags, respectively, as shown below: <think>A comprehensive strategy for writing that encompasses detailed planning and structural design—including brainstorming, outlining, style selection, audience adaptation, self-reflection, quality assurance, etc..</think> <answer>The final written work after thorough optimization and refinement.</answer>  <|user|>: {question} <|assistant|>:"
    base_format = base_format_zn if re.search(r'[\u4e00-\u9fff]', prompt) else base_format_en
    formatted_prompt = base_format.format(question=prompt)
    return formatted_prompt



prompt = "XXXX"          # ← replace with your writing task
data = {
    "model": "LongWriter-Zero-32B",
    "prompt": format_prompt_with_template(prompt),
    "temperature": 0.6,
    "top_p": 0.95,
    "max_tokens": 15500,
    "stop": ["<|user|>", "<|endoftext|>", "</answer>"],
    "stream": True,
}

# SGlang Gateway (example)
response = requests.post(
    "http://XXXX:9999/v1/completions",  # ← replace with your IP
    json=data,
    headers={"Content-Type": "application/json"},
    timeout=1200,
    stream=True,
)

for chunk in response.iter_lines():
    if chunk and chunk.startswith(b"data:"):
        if chunk == b"data: [DONE]":
            break
        payload = json.loads(chunk[5:])
        print(payload["choices"][0]["text"], end="", flush=True)
```
<a name="citation"></a>
## 📝 Citation

```bibtex
@misc{wu2025longwriterzeromasteringultralongtext,
      title={LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning}, 
      author={Yuhao Wu and Yushi Bai and Zhiqiang Hu and Roy Ka-Wei Lee and Juanzi Li},
      year={2025},
      eprint={2506.18841},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.18841}, 
}