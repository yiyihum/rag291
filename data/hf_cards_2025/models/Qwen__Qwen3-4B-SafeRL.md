---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-4B-SafeRL/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-4B
---

# Qwen3-4B-SafeRL

## Model Overview

**Qwen3-4B-SafeRL** is a safety-aligned version of the [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) model. It has been trained using Reinforcement Learning (RL) with a reward signal from **Qwen3Guard-Gen** to enhance its robustness against harmful or adversarial prompts. This process aims to ensure strong safety guarantees without leading to overly simplistic or evasive refusal behaviors, thereby maintaining a positive user experience.

For more details on the safety alignment process, please refer to the [Qwen3Guard Technical Report](https://github.com/QwenLM/Qwen3Guard/blob/main/Qwen3Guard_Technical_Report.pdf).

### Reinforcement Learning with Hybrid Reward

To prevent the model from defaulting to refusal across all prompts in an attempt to remain safe, we introduce a hybrid reward function that jointly optimizes three key objectives:

- **Safety Maximization:** Penalizes the generation of unsafe content, as detected by [Qwen3Guard-Gen-4B](https://huggingface.co/Qwen/Qwen3Guard-Gen-4B).
- **Helpfulness Maximization:** Rewards responses that are genuinely helpful, as evaluated by the [WorldPM-Helpsteer2](https://huggingface.co/Qwen/WorldPM-72B-HelpSteer2) model.
- **Refusal Minimization:** Applies a moderate penalty for unnecessary refusals, also identified by [Qwen3Guard-Gen-4B](https://huggingface.co/Qwen/Qwen3Guard-Gen-4B).

### Performance


| Mode        | Model                   | Safety Rate (Qwen3-235B) | Safety Rate (WildGuard) | Refusal (WildGuard) | ArenaHard-v2 (Winrate vs GPT-4.1) | AIME25 (Pass@1) | LCB-v6 (Pass@1) | GPQA (Pass@1) |
|-------------|-------------------------|--------------------------|--------------------------|---------------------|-----------------------------------|-----------------|-----------------|---------------|
| **Non-Think** | Qwen3-4B                | 47.5                     | 64.7                     | 12.9                | 9.5                               | **19.1**            | 26.4            | **41.7**          |
|             | Qwen3-4B-SafeRL       | **86.5**                     | **98.1**                     | **5.3**             | **10.7**                          | 18.2            | **27.7**        | 40.8          |
| **Think**     | Qwen3-4B                | 43.8                     | 59.0                     | 6.5                 | 13.7                              | **65.6**            | **48.4**        | **55.9**      |
|             | Qwen3-4B-SafeRL       | **83.4**                     | **97.4**                     | **6.2**             | **16.6**                          | 63.5            | 47.5            | 51.2          |


## Quickstart

Qwen3-4B-SafeRL is used in the same way as Qwen3-4B, preserving the ability of hybrid thinking modes. The code of Qwen3 has been in the latest Hugging Face `transformers` and we advise you to use the latest version of `transformers`.

With `transformers<4.51.0`, you will encounter the following error:
```
KeyError: 'qwen3'
```

The following contains a code snippet illustrating how to use the model generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-4B-SafeRL"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
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

print("thinking content:", thinking_content)
print("content:", content)
```

For deployment, you can use `sglang>=0.4.6.post1` or `vllm>=0.8.5` or to create an OpenAI-compatible API endpoint:
- SGLang:
    ```shell
    python -m sglang.launch_server --model-path Qwen/Qwen3-4B-SafeRL --reasoning-parser qwen3
    ```
- vLLM:
    ```shell
    vllm serve Qwen/Qwen3-4B-SafeRL --enable-reasoning --reasoning-parser deepseek_r1
    ```

For local use, applications such as Ollama, LMStudio, MLX-LM, llama.cpp, and KTransformers have also supported Qwen3.

For more usages, please refer to the modelcard of [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B).

## Citation

If you find our work helpful, feel free to give us a cite.

```
@misc{qwen3guard,
      title={Qwen3Guard Technical Report}, 
      author={Qwen Team},
      year={2025},
      url={http://arxiv.org/abs/2510.14276},
}
```