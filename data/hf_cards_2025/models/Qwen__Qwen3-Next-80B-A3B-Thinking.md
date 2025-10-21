---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking/blob/main/LICENSE
pipeline_tag: text-generation
---

# Qwen3-Next-80B-A3B-Thinking
<a href="https://chat.qwen.ai/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/%F0%9F%92%9C%EF%B8%8F%20Qwen%20Chat%20-536af5" style="display: inline-block; vertical-align: middle;"/>
</a>

Over the past few months, we have observed increasingly clear trends toward scaling both total parameters and context lengths in the pursuit of more powerful and agentic artificial intelligence (AI). 
We are excited to share our latest advancements in addressing these demands, centered on improving scaling efficiency through innovative model architecture. 
We call this next-generation foundation models **Qwen3-Next**.

## Highlights

**Qwen3-Next-80B-A3B** is the first installment in the Qwen3-Next series and features the following key enchancements:
- **Hybrid Attention**: Replaces standard attention with the combination of **Gated DeltaNet** and **Gated Attention**, enabling efficient context modeling for ultra-long context length.
- **High-Sparsity Mixture-of-Experts (MoE)**: Achieves an extreme low activation ratio in MoE layers, drastically reducing FLOPs per token while preserving model capacity. 
- **Stability Optimizations**: Includes techniques such as **zero-centered and weight-decayed layernorm**, and other stabilizing enhancements for robust pre-training and post-training.  
- **Multi-Token Prediction (MTP)**: Boosts pretraining model performance and accelerates inference.

We are seeing strong performance in terms of both parameter efficiency and inference speed for Qwen3-Next-80B-A3B:
- Qwen3-Next-80B-A3B-Base outperforms Qwen3-32B-Base on downstream tasks with 10% of the total training cost and with 10 times inference throughput for context over 32K tokens.
- Leveraging [GSPO](https://qwenlm.github.io/blog/gspo/), we have addressed the stability and efficiency challenges posed by the hybrid attention mechanism combined with a high-sparsity MoE architecture in RL training. 
  Qwen3-Next-80B-A3B-Thinking demonstrates outstanding performance on complex reasoning tasks, not only **surpassing Qwen3-30B-A3B-Thinking-2507 and Qwen3-32B-Thinking**, but also **outperforming the proprietary model Gemini-2.5-Flash-Thinking** across multiple benchmarks.

![Qwen3-Next-80B-A3B-Thinking Benchmark Comparison](https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-Next/Qwen3-Next-80B-A3B-Thinking.001.jpeg)

For more details, please refer to our blog post [Qwen3-Next](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list).

## Model Overview

> [!Note]
> **Qwen3-Next-80B-A3B-Thinking** supports only thinking mode. 
> To enforce model thinking, the default chat template automatically includes `<think>`. 
> Therefore, it is normal for the model's output to contain only `</think>` without an explicit opening `<think>` tag.

> [!Note]
> **Qwen3-Next-80B-A3B-Thinking** may generate thinking content longer than its predecessor.
> We strongly recommend its use in highly complex reasoning tasks.


**Qwen3-Next-80B-A3B-Thinking** has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining (15T tokens) & Post-training
- Number of Parameters: 80B in total and 3B activated
- Number of Paramaters (Non-Embedding): 79B
- Hidden Dimension: 2048
- Number of Layers: 48
  - Hybrid Layout: 12 \* (3 \* (Gated DeltaNet -> MoE) -> 1 \* (Gated Attention -> MoE))
- Gated Attention:
  - Number of Attention Heads: 16 for Q and 2 for KV
  - Head Dimension: 256
  - Rotary Position Embedding Dimension: 64
- Gated DeltaNet:
  - Number of Linear Attention Heads: 32 for V and 16 for QK
  - Head Dimension: 128
- Mixture of Experts:
  - Number of Experts: 512
  - Number of Activated Experts: 10
  - Number of Shared Experts: 1
  - Expert Intermediate Dimension: 512
- Context Length: 262,144 natively and extensible up to 1,010,000 tokens

<img src="https://qianwen-res.oss-accelerate.aliyuncs.com/Qwen3-Next/model_architecture.png" height="384px" title="Qwen3-Next Model Architecture" />


## Performance

|  | Qwen3-30B-A3B-Thinking-2507 | Qwen3-32B Thinking | Qwen3-235B-A22B-Thinking-2507 | Gemini-2.5-Flash Thinking | Qwen3-Next-80B-A3B-Thinking |
|--- | --- | --- | --- | --- | --- |
| **Knowledge** | | | | |
| MMLU-Pro | 80.9 | 79.1 | **84.4** | 81.9 | 82.7 |
| MMLU-Redux | 91.4 | 90.9 | **93.8** | 92.1 | 92.5 |
| GPQA | 73.4 | 68.4 | 81.1 | **82.8** | 77.2 |
| SuperGPQA | 56.8 | 54.1 | **64.9** | 57.8 | 60.8 |
| **Reasoning** | | | | |
| AIME25 | 85.0 | 72.9 | **92.3** | 72.0 | 87.8 |
| HMMT25 | 71.4 | 51.5 | **83.9** | 64.2 | 73.9 |
| LiveBench 241125 | 76.8 | 74.9 | **78.4** | 74.3 | 76.6 |
| **Coding** | | | | |
| LiveCodeBench v6 (25.02-25.05) | 66.0 | 60.6 | **74.1** | 61.2 | 68.7 |
| CFEval | 2044 | 1986 | **2134** | 1995 | 2071 |
| OJBench | 25.1 | 24.1 | **32.5** | 23.5 | 29.7 |
| **Alignment** | | | | |
| IFEval | 88.9 | 85.0 | 87.8 | **89.8** | 88.9 |
| Arena-Hard v2* | 56.0 | 48.4 | **79.7** | 56.7 | 62.3 |
| WritingBench | 85.0 | 79.0 | **88.3** | 83.9 | 84.6 |
| **Agent** | | | | |
| BFCL-v3 |  **72.4** | 70.3 | 71.9 | 68.6 | 72.0 |
| TAU1-Retail | 67.8 | 52.8 | 67.8 | 65.2 | **69.6** |
| TAU1-Airline | 48.0 | 29.0 | 46.0 | **54.0** | 49.0 |
| TAU2-Retail | 58.8 | 49.7 | **71.9** | 66.7 | 67.8 |
| TAU2-Airline | 58.0 | 45.5 | 58.0 | 52.0 | **60.5** |
| TAU2-Telecom | 26.3 | 27.2 | **45.6** | 31.6 | 43.9 |
| **Multilingualism** | | | | |
| MultiIF | 76.4 | 73.0 | **80.6** | 74.4 | 77.8 |
| MMLU-ProX | 76.4 | 74.6 | **81.0** | 80.2 | 78.7 |
| INCLUDE | 74.4 | 73.7 | 81.0 | **83.9** | 78.9 |
| PolyMATH | 52.6 | 47.4 | **60.1** | 49.8 | 56.3 |

*: For reproducibility, we report the win rates evaluated by GPT-4.1.

## Quickstart

The code for Qwen3-Next has been merged into the main branch of Hugging Face `transformers`. 

```shell
pip install git+https://github.com/huggingface/transformers.git@main
```

With earlier versions, you will encounter the following error:
```
KeyError: 'qwen3_next'
```

The following contains a code snippet illustrating how to use the model generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-Next-80B-A3B-Thinking"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt},
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768,
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content) # no opening <think> tag
print("content:", content)
```

> [!Note]
> Multi-Token Prediction (MTP) is not generally available in Hugging Face Transformers.

> [!Note]
> The efficiency or throughput improvement depends highly on the implementation.
> It is recommended to adopt a dedicated inference framework, e.g., SGLang and vLLM, for inference tasks.

> [!Tip]
> Depending on the inference settings, you may observe better efficiency with [`flash-linear-attention`](https://github.com/fla-org/flash-linear-attention#installation) and [`causal-conv1d`](https://github.com/Dao-AILab/causal-conv1d).
> See the links for detailed instructions and requirements.

## Deployment

For deployment, you can use the latest `sglang` or `vllm` to create an OpenAI-compatible API endpoint.

### SGLang

[SGLang](https://github.com/sgl-project/sglang) is a fast serving framework for large language models and vision language models.
SGLang could be used to launch a server with OpenAI-compatible API service. 

`sglang>=0.5.2` is required for Qwen3-Next, which can be installed using:
```shell
pip install 'sglang[all]>=0.5.2'
```
See [its documentation](https://docs.sglang.ai/get_started/install.html) for more details.

The following command can be used to create an API endpoint at `http://localhost:30000/v1` with maximum context length 256K tokens using tensor parallel on 4 GPUs.
```shell
python -m sglang.launch_server --model-path Qwen/Qwen3-Next-80B-A3B-Thinking --port 30000 --tp-size 4 --context-length 262144 --reasoning-parser deepseek-r1 --mem-fraction-static 0.8
```

The following command is recommended for MTP with the rest settings the same as above:
```shell
python -m sglang.launch_server --model-path Qwen/Qwen3-Next-80B-A3B-Thinking --port 30000 --tp-size 4 --context-length 262144 --reasoning-parser deepseek-r1 --mem-fraction-static 0.8 --speculative-algo NEXTN --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4
```

> [!Note]
> The default context length is 256K. 
> If you encounter out-of-memory (OOM) issues, you may consider reducing the context length to a smaller value. 
> However, since the model may require longer token sequences for reasoning, we strongly recommend using a context length greater than 131,072.

Please also refer to SGLang's usage guide on [Qwen3-Next](https://docs.sglang.ai/basic_usage/qwen3.html).

### vLLM

[vLLM](https://github.com/vllm-project/vllm) is a high-throughput and memory-efficient inference and serving engine for LLMs.
vLLM could be used to launch a server with OpenAI-compatible API service. 

`vllm>=0.10.2` is required for Qwen3-Next, which can be installed using:
```shell
pip install 'vllm>=0.10.2'
```
See [its documentation](https://docs.vllm.ai/en/stable/getting_started/installation/index.html) for more details.

The following command can be used to create an API endpoint at `http://localhost:8000/v1` with maximum context length 256K tokens using tensor parallel on 4 GPUs.
```shell
vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking --port 8000 --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser deepseek_r1
```

The following command is recommended for MTP with the rest settings the same as above:
```shell
vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking --port 8000 --tensor-parallel-size 4 --max-model-len 262144 --reasoning-parser deepseek_r1 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}'
```

> [!Note]
> The default context length is 256K. 
> If you encounter out-of-memory (OOM) issues, you may consider reducing the context length to a smaller value. 
> However, since the model may require longer token sequences for reasoning, we strongly recommend using a context length greater than 131,072 when possible.

Please also refer to vLLM's usage guide on [Qwen3-Next](https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html).


## Agentic Use

Qwen3 excels in tool calling capabilities. We recommend using [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) to make the best use of agentic ability of Qwen3. Qwen-Agent encapsulates tool-calling templates and tool-calling parsers internally, greatly reducing coding complexity.

To define the available tools, you can use the MCP configuration file, use the integrated tool of Qwen-Agent, or integrate other tools by yourself.
```python
from qwen_agent.agents import Assistant

# Define LLM
# Using Alibaba Cloud Model Studio
llm_cfg = {
    'model': 'Qwen3-Next-80B-A3B-Thinking',
    'model_type': 'qwen_dashscope',
}

# Using OpenAI-compatible API endpoint. It is recommended to disable the reasoning and the tool call parsing
# functionality of the deployment frameworks and let Qwen-Agent automate the related operations. For example, 
# `vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking --served-model-name Qwen3-Next-80B-A3B-Thinking --port 8000 --tensor-parallel-size 4 --max-model-len 262144`.
#
# llm_cfg = {
#     'model': 'Qwen3-Next-80B-A3B-Thinking',
# 
#     # Use a custom endpoint compatible with OpenAI API:
#     'model_server': 'http://localhost:8000/v1',  # api_base without reasoning and tool call parsing
#     'api_key': 'EMPTY',
#     'generate_cfg': {
#         'thought_in_content': True,
#     },
# }

# Define Tools
tools = [
    {'mcpServers': {  # You can specify the MCP configuration file
            'time': {
                'command': 'uvx',
                'args': ['mcp-server-time', '--local-timezone=Asia/Shanghai']
            },
            "fetch": {
                "command": "uvx",
                "args": ["mcp-server-fetch"]
            }
        }
    },
  'code_interpreter',  # Built-in tools
]

# Define Agent
bot = Assistant(llm=llm_cfg, function_list=tools)

# Streaming generation
messages = [{'role': 'user', 'content': 'https://qwenlm.github.io/blog/ Introduce the latest developments of Qwen'}]
for responses in bot.run(messages=messages):
    pass
print(responses)
```


## Processing Ultra-Long Texts

Qwen3-Next natively supports context lengths of up to 262,144 tokens. 
For conversations where the total length (including both input and output) significantly exceeds this limit, we recommend using RoPE scaling techniques to handle long texts effectively. 
We have validated the model's performance on context lengths of up to 1 million tokens using the [YaRN](https://arxiv.org/abs/2309.00071) method.

YaRN is currently supported by several inference frameworks, e.g., `transformers`, `vllm` and `sglang`. 
In general, there are two approaches to enabling YaRN for supported frameworks:

- Modifying the model files:
  In the `config.json` file, add the `rope_scaling` fields:
    ```json
    {
        ...,
        "rope_scaling": {
            "rope_type": "yarn",
            "factor": 4.0,
            "original_max_position_embeddings": 262144
        }
    }
    ```

- Passing command line arguments:

  For `vllm`, you can use
    ```shell
    VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve ... --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":262144}' --max-model-len 1010000  
    ```

  For `sglang`, you can use
    ```shell
    SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 python -m sglang.launch_server ... --json-model-override-args '{"rope_scaling":{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":262144}}' --context-length 1010000
    ```

> [!NOTE]
> All the notable open-source frameworks implement static YaRN, which means the scaling factor remains constant regardless of input length, **potentially impacting performance on shorter texts.**
> We advise adding the `rope_scaling` configuration only when processing long contexts is required. 
> It is also recommended to modify the `factor` as needed. For example, if the typical context length for your application is 524,288 tokens, it would be better to set `factor` as 2.0. 

## Best Practices

To achieve optimal performance, we recommend the following settings:

1. **Sampling Parameters**:
   - We suggest using `Temperature=0.6`, `TopP=0.95`, `TopK=20`, and `MinP=0`.
   - For supported frameworks, you can adjust the `presence_penalty` parameter between 0 and 2 to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance.

2. **Adequate Output Length**: We recommend using an output length of 32,768 tokens for most queries. For benchmarking on highly complex problems, such as those found in math and programming competitions, we suggest setting the max output length to 81,920 tokens. This provides the model with sufficient space to generate detailed and comprehensive responses, thereby enhancing its overall performance.

3. **Standardize Output Format**: We recommend using prompts to standardize model outputs when benchmarking.
   - **Math Problems**: Include "Please reason step by step, and put your final answer within \boxed{}." in the prompt.
   - **Multiple-Choice Questions**: Add the following JSON structure to the prompt to standardize responses: "Please show your choice in the `answer` field with only the choice letter, e.g., `"answer": "C"`."

4. **No Thinking Content in History**: In multi-turn conversations, the historical model output should only include the final output part and does not need to include the thinking content. It is implemented in the provided chat template in Jinja2. However, for frameworks that do not directly use the Jinja2 chat template, it is up to the developers to ensure that the best practice is followed.

### Citation

If you find our work helpful, feel free to give us a cite.

```
@misc{qwen3technicalreport,
      title={Qwen3 Technical Report}, 
      author={Qwen Team},
      year={2025},
      eprint={2505.09388},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.09388}, 
}

@article{qwen2.5-1m,
      title={Qwen2.5-1M Technical Report}, 
      author={An Yang and Bowen Yu and Chengyuan Li and Dayiheng Liu and Fei Huang and Haoyan Huang and Jiandong Jiang and Jianhong Tu and Jianwei Zhang and Jingren Zhou and Junyang Lin and Kai Dang and Kexin Yang and Le Yu and Mei Li and Minmin Sun and Qin Zhu and Rui Men and Tao He and Weijia Xu and Wenbiao Yin and Wenyuan Yu and Xiafei Qiu and Xingzhang Ren and Xinlong Yang and Yong Li and Zhiying Xu and Zipeng Zhang},
      journal={arXiv preprint arXiv:2501.15383},
      year={2025}
}
```