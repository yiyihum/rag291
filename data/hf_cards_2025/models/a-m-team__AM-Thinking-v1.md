---
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
---
# AM‑Thinking‑v1: Advancing the Frontier of Reasoning at 32B Scale
* 2025-05-10 · a-m‑team

<p align="center">
🤗 <a href="https://huggingface.co/a-m-team">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2505.08311"> Paper</a>  &nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://a-m-team.github.io/am-thinking-v1/">Blog</a> &nbsp&nbsp 
</p>

## 🚀 Introduction

We release **AM-Thinking‑v1**, a 32B dense language model focused on enhancing reasoning capabilities. 
Built on Qwen 2.5‑32B‑Base, AM-Thinking‑v1 shows strong performance on reasoning benchmarks, comparable to much larger MoE models like **DeepSeek‑R1**, **Qwen3‑235B‑A22B**, **Seed1.5-Thinking**, and larger dense model like **Nemotron-Ultra-253B-v1**.

<div style="text-align: center;">
    <img src="assets/benchmark.png" alt="benchmark" style="width: 90%;">
</div>


## 🧩 Why Another 32B Reasoning Model Matters?

Large Mixture‑of‑Experts (MoE) models such as **DeepSeek‑R1** or **Qwen3‑235B‑A22B** dominate leaderboards—but they also demand clusters of high‑end GPUs. Many teams just need *the best dense model that fits on a single card*.
**AM‑Thinking‑v1** fills that gap **while remaining fully based on open-source components**:

* **Outperforms DeepSeek‑R1** on AIME’24/’25 & LiveCodeBench and **approaches Qwen3‑235B‑A22B** despite being 1/7‑th the parameter count.
* **Built on the publicly available Qwen 2.5‑32B‑Base**, as well as the RL training queries.
* Shows that with a **well‑designed post‑training pipeline** ( SFT + dual‑stage RL ) you can squeeze flagship‑level reasoning out of a 32 B dense model.
* **Deploys on one A100‑80 GB** with deterministic latency—no MoE routing overhead.

<div style="text-align: center;">
  <img src="assets/param-aime2024.jpeg" alt="AIME 2024" style="width: 90%; margin-bottom: 20px;">
  <img src="assets/param-lcb.jpeg" alt="LiveCodeBench" style="width: 90%;">
  <div style="margin-top: 10px;">
    <em>AM-Thinking-v1 achieves strong reasoning performance with significantly fewer parameters.</em>
  </div>
</div>



## 🛠️ Use Cases

### 1) Code Generation
<pre style="font-family: 'Times New Roman', serif; font-size: 12px; border: 1px solid black; padding: 10px; font-style: italic;">
PROMPT :
write a python script for a bouncing red ball within a triangle, make sure to handle collision detection properly. make the triangle slowly rotate. implement it in python. make sure ball stays within the triangle
</pre>
<div style="text-align: center;">
    <img src="assets/ball.gif" alt="Bouncing Red Ball" width="50%">
</div>


### 2) Logic


<div style="text-align: center;">
    <img src="assets/diamond.png" alt="diamond" width="90%">
</div>


### 3) Writing
<div style="text-align: center;">
    <img src="assets/writing.png" alt="sushi" width="90%">
</div>



## ⚡ Quick start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "a-m-team/AM-Thinking-v1"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

prompt = "How can I find inner peace?"
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
    max_new_tokens=49152
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

response = tokenizer.decode(output_ids, skip_special_tokens=True)
think_content = response.split("<think>")[1].split("</think>")[0]
answer_content = response.split("<answer>")[1].split("</answer>")[0]

print (f"user prompt: {prompt}")
print (f"model thinking: {think_content}")
print (f"model answer: {answer_content}")
```
> Note: We have included the system prompt in the tokenizer configuration, as it was used during both the SFT and RL stages. To ensure consistent output quality, we recommend including the same system prompt during actual usage; otherwise, the model's responses may be significantly affected.

### Quantized versions for compact devices
A series of quantized versions for [AM-Thinking-v1](https://huggingface.co/a-m-team/AM-Thinking-v1-gguf) model.
For use with [llama.cpp](https://github.com/ggml-org/llama.cpp) and [Ollama](https://github.com/ollama/ollama)
is available at [AM-Thinking-v1-gguf](https://huggingface.co/a-m-team/AM-Thinking-v1-gguf).


## 🔧 Post-training pipeline

To achieve its strong reasoning ability, AM‑Thinking‑v1 goes through a carefully designed post-training pipeline. 
Below we describe the key stages involved in turning a base model into a high-performing reasoner:


**Step 1 – Cold‑start SFT.**
We begin with the open-sourced **Qwen 2.5‑32B‑Base** and run a broad supervised fine‑tune on a blended training dataset of math, code and open‑domain chat. This endows the model with a "think‑then‑answer" behavioural pattern and equips it with an initial capacity for reasoning.

**Step 2 – Pass‑rate‑aware data curation.**
Before any RL, the SFT model is evaluated on every math‑ and code‑oriented training query. For each item we log a pass rate; only those with **0 < pass‑rate < 1** are kept. In effect we discard problems the model already masters and those it utterly fails, concentrating learning on genuinely informative cases.

**Step 3 – Reinforcement learning .**
We adopt a two‑stage GRPO scheme: Stage 1 trains only on math and code queries. Once it converges, stage 2 starts by removing every query the model answered 100% correctly in Stage 1 and adjusting key hyper‑parameters such as maximum generation length and learning rate.


## ⚠️ Limitations

While AM‑Thinking‑v1 excels at pure language reasoning and open‑domain chat, it has not yet been trained for structured function‑calling or tool‑use workflows, which restricts its usefulness in agent‑style applications that must act on external systems.
Improving the model's ability to follow complex instructions is also an important direction for our future work.
In addition, our safety alignment is still at an early stage, so more rigorous red‑teaming are required to reduce potential harms.

## 📚 Citation
The a-m-team is an internal team at Beike (Ke.com), dedicated to exploring AGI technology.
If you find our work helpful, feel free to give us a cite.

```
@misc{ji2025amthinkingv1advancingfrontierreasoning,
      title={AM-Thinking-v1: Advancing the Frontier of Reasoning at 32B Scale}, 
      author={Yunjie Ji and Xiaoyu Tian and Sitong Zhao and Haotian Wang and Shuaiting Chen and Yiping Peng and Han Zhao and Xiangang Li},
      year={2025},
      eprint={2505.08311},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.08311}, 
}
```