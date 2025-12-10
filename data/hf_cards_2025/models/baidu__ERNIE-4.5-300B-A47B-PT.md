---
license: apache-2.0
language:
- en
- zh
pipeline_tag: text-generation
tags:
- ERNIE4.5
library_name: transformers
---

<div align="center" style="line-height: 1;">
  <a href="https://ernie.baidu.com/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖_Chat-ERNIE_Bot-blue" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/baidu" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Baidu-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/PaddlePaddle/ERNIE" target="_blank" style="margin: 2px;">
    <img alt="Github" src="https://img.shields.io/badge/GitHub-ERNIE-000?logo=github&color=0000FF" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://ernie.baidu.com/blog/ernie4.5" target="_blank" style="margin: 2px;">
    <img alt="Blog" src="https://img.shields.io/badge/🖖_Blog-ERNIE4.5-A020A0" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://discord.gg/JPmZXDsEEK" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-ERNIE-5865F2?logo=discord&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://x.com/PaddlePaddle" target="_blank" style="margin: 2px;">
    <img alt="X" src="https://img.shields.io/badge/X-PaddlePaddle-6080F0"?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="#license" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-Apache2.0-A5de54" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

# ERNIE-4.5-300B-A47B

> [!NOTE]
> Note: "**-Paddle**" models use [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) weights, while "**-PT**" models use Transformer-style PyTorch weights.


## ERNIE 4.5 Highlights

The advanced capabilities of the ERNIE 4.5 models, particularly the MoE-based A47B and A3B series, are underpinned by several key technical innovations:

1. **Multimodal Heterogeneous MoE Pre-Training:** Our models are jointly trained on both textual and visual modalities to better capture the nuances of multimodal information and improve performance on tasks involving text understanding and generation, image understanding, and cross-modal reasoning. To achieve this without one modality hindering the learning of another, we designed a *heterogeneous MoE structure*, incorporated *modality-isolated routing*, and employed *router orthogonal loss* and *multimodal token-balanced loss*. These architectural choices ensure that both modalities are effectively represented, allowing for mutual reinforcement during training.

2. **Scaling-Efficient Infrastructure:** We propose a novel heterogeneous hybrid parallelism and hierarchical load balancing strategy for efficient training of ERNIE 4.5 models. By using intra-node expert parallelism, memory-efficient pipeline scheduling, FP8 mixed-precision training and finegrained recomputation methods, we achieve remarkable pre-training throughput. For inference, we propose *multi-expert parallel collaboration* method and *convolutional code quantization* algorithm to achieve 4-bit/2-bit lossless quantization. Furthermore, we introduce PD disaggregation with dynamic role switching for effective resource utilization to enhance inference performance for ERNIE 4.5 MoE models. Built on [PaddlePaddle](https://github.com/PaddlePaddle/Paddle), ERNIE 4.5 delivers high-performance inference across a wide range of hardware platforms.

3. **Modality-Specific Post-Training:** To meet the diverse requirements of real-world applications, we fine-tuned variants of the pre-trained model for specific modalities. Our LLMs are optimized for general-purpose language understanding and generation. The VLMs focuses on visuallanguage understanding and supports both thinking and non-thinking modes. Each model employed a combination of *Supervised Fine-tuning (SFT)*, *Direct Preference Optimization (DPO)* or a modified reinforcement learning method named *Unified Preference Optimization (UPO)* for post-training.

## Model Overview

ERNIE-4.5-300B-A47B is a text MoE Post-trained model, with 300B total parameters and 47B activated parameters for each token. The following are the model configuration details:

|Key|Value|
|-|-|
|Modality|Text|
|Training Stage|Pretraining|
|Params(Total / Activated)|300B / 47B|
|Layers|54|
|Heads(Q/KV)|64 / 8|
|Text Experts(Total / Activated)|64 / 8|
|Vision Experts(Total / Activated)|64 / 8|
|Context Length|131072|

## Quickstart

### Using `transformers` library

**Note**: Before using the model, please ensure you have the `transformers` library installed
(upcoming version 4.54.0 or [the latest version](https://github.com/huggingface/transformers?tab=readme-ov-file#installation))

The following contains a code snippet illustrating how to use the model generate content based on given inputs.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "baidu/ERNIE-4.5-300B-A47B-PT"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], add_special_tokens=False, return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=1024
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

# decode the generated ids
generate_text = tokenizer.decode(output_ids, skip_special_tokens=True).strip("\n")
print("generate_text:", generate_text)
```

### Using vLLM

[vllm](https://github.com/vllm-project/vllm/tree/main) github library. Python-only [build](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#set-up-using-python-only-build-without-compilation).

```bash
# 80G * 16 GPU
vllm serve baidu/ERNIE-4.5-300B-A47B-PT --tensor-parallel-size 16
```

```bash
# FP8 online quantification 80G * 8 GPU
vllm serve baidu/ERNIE-4.5-300B-A47B-PT --tensor-parallel-size 8 --quantization fp8
```

## Best Practices

### **Sampling Parameters**

To achieve optimal performance, we suggest using `Temperature=0.8`, `TopP=0.8`.

### Prompts for Web Search

For Web Search, {references}, {date}, and {question} are arguments.

For Chinese question, we use the prompt:

```python
ernie_search_zh_prompt = \
'''下面你会收到当前时间、多个不同来源的参考文章和一段对话。你的任务是阅读多个参考文章，并根据参考文章中的信息回答对话中的问题。
以下是当前时间和参考文章：
---------
#当前时间
{date}

#参考文章
{references}

---------
请注意：
1. 回答必须结合问题需求和当前时间，对参考文章的可用性进行判断，避免在回答中使用错误或过时的信息。
2. 当参考文章中的信息无法准确地回答问题时，你需要在回答中提供获取相应信息的建议，或承认无法提供相应信息。
3. 你需要优先根据百科、官网、权威机构、专业网站等高权威性来源的信息来回答问题。
4. 回复需要综合参考文章中的相关数字、案例、法律条文、公式等信息，使你的答案更专业。
5. 当问题属于创作类任务时，需注意以下维度：
   - 态度鲜明：观点、立场清晰明确，避免模棱两可，语言果断直接
   - 文采飞扬：用词精准生动，善用修辞手法，增强感染力
   - 有理有据：逻辑严密递进，结合权威数据/事实支撑论点
---------
下面请结合以上信息，回答问题，补全对话
{question}'''
```

For English question, we use the prompt:

```python
ernie_search_en_prompt = \
'''
Below you will be given the current time, multiple references from different sources, and a conversation. Your task is to read the references and use the information in them to answer the question in the conversation.
Here are the current time and the references:
---------
#Current Time
{date}

#References
{references}

---------
Please note:
1. Based on the question’s requirements and the current time, assess the usefulness of the references to avoid using inaccurate or outdated information in the answer.  
2. If the references do not provide enough information to accurately answer the question, you should suggest how to obtain the relevant information or acknowledge that you are unable to provide it.  
3. Prioritize using information from highly authoritative sources such as encyclopedias, official websites, authoritative institutions, and professional websites when answering questions.
4. Incorporate relevant numbers, cases, legal provisions, formulas, and other details from the references to make your answer more professional.
5. For creative tasks, keep these dimensions in mind:
   - Clear attitude: Clear views and positions, avoid ambiguity, and use decisive and direct language
   - Brilliant writing: Precise and vivid words, good use of rhetoric, and enhance the appeal
   - Well-reasoned: Rigorous logic and progressive, combined with authoritative data/facts to support the argument

---------
Now, using the information above, answer the question and complete the conversation:  
{question}'''
```

Parameter notes:

* {question} is the user’s question
* {date} is the current time, and the recommended format is “YYYY-MM-DD HH:MM:SS, Day of the Week, Beijing/China.”
* {references} is the references, and the recommended format is:

```text
##参考文章1
标题：周杰伦
文章发布时间：2025-04-20
内容：周杰伦(Jay Chou),1979年1月18日出生于台湾省新北市,祖籍福建省永春县,华语流行乐男歌手、音乐人、演员、导演、编剧,毕业于淡江中学。2000年,发行个人首张音乐专辑《Jay》。...
来源网站网址：baike.baidu.com
来源网站的网站名：百度百科

##参考文章2
...
```

## License

The ERNIE 4.5 models are provided under the Apache License 2.0. This license permits commercial use, subject to its terms and conditions. Copyright (c) 2025 Baidu, Inc. All Rights Reserved.

## Citation

If you find ERNIE 4.5 useful or wish to use it in your projects, please kindly cite our technical report:

```bibtex
@misc{ernie2025technicalreport,
      title={ERNIE 4.5 Technical Report},
      author={Baidu ERNIE Team},
      year={2025},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={}
}
```
