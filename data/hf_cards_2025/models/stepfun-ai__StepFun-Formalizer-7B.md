---
language:
- en
base_model: deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
tags:
- chat
library_name: transformers
license: apache-2.0
datasets:
- stepfun-ai/StepFun-Formalizer-Training
---

<p align="center">
  <img src="assets/logo.png" width="250px"><br>
</p>

# StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion

<div align="center"> 
  <a href="https://www.arxiv.org/abs/2508.04440"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red"></a> &ensp;
  <a href="https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"><img src="https://img.shields.io/static/v1?label=Model&message=HuggingFace&color=yellow"></a> &ensp;
  <a href="https://github.com/stepfun-ai/StepFun-Formalizer"><img src="https://img.shields.io/static/v1?label=Code&message=Github&color=blue"></a> &ensp;
</div>
<br>

## Introduction

We introduce StepFun-Formalizer, a family of large language models designed to translate natural-language mathematical problems into formal statements in Lean 4. Through the fusion of formal knowledge and informal-to-formal reasoning capability, StepFun-Formalizer achieves strong performance on autoformalization tasks. Evaluated with [BEq](https://github.com/Purewhite2019/rethinking_autoformalization) verification on mainstream benchmarks including [FormalMATH-Lite](https://huggingface.co/datasets/SphereLab/FormalMATH-Lite), [ProverBench](https://huggingface.co/datasets/deepseek-ai/DeepSeek-ProverBench), and [CombiBench](https://huggingface.co/datasets/AI-MO/CombiBench), StepFun-Formalizer matches or exceeds all prior general-purpose and specialized autoformalization models of comparable scale. Please refer to our [paper](https://arxiv.org/abs/2508.04440) and [code](https://github.com/stepfun-ai/StepFun-Formalizer) for more details.

## Models

<div align="center">
  
| Model | Download |
| -------- | -------- |
|    StepFun-Formalizer-7B    |   [🤗HuggingFace](https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B)    |
|    StepFun-Formalizer-32B    |   [🤗HuggingFace](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)    |

</div>

## Usage

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

def get_formal_statement_prompt(informal_problem: str, header: str = "import Mathlib\n") -> str:
    prompt = "Please autoformalize the following problem in Lean 4 with a header. Use the following theorem names: my_favorite_theorem.\n\n"
    prompt += informal_problem
    prompt += f"\n\nYour code should start with:\n```Lean4\n{header}\n```\n"
    return prompt

MODEL_DIR = "stepfun-ai/StepFun-Formalizer-7B"

if __name__ == "__main__":

    system_prompt = "You are an expert in mathematics and Lean 4."
    informal_problem = "The real numbers $x, y, z$ satisfy $0 \\leq x \\leq y \\leq z \\leq 4$. If their squares form an arithmetic progression with common difference 2, determine the minimum possible value of $|x-y|+|y-z|$.\n Prove that the answer is: 4-2\\sqrt{3}"
    header = "import Mathlib\n\nopen Real\n"
    user_prompt = get_formal_statement_prompt(informal_problem, header)

    dialog = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ] 

    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    prompt = tokenizer.apply_chat_template(dialog, tokenize=False, add_generation_prompt=True) + "<think>"
    print(f"prompt: {prompt}")

    model = LLM(
        MODEL_DIR, 
        tensor_parallel_size=4 # 8 for 32B, 4 for 7B
    )

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        max_tokens=16384,
        n=1
    )

    responses = model.generate(prompt, sampling_params)
    print(f"response: {responses[0].outputs[0].text}")
```

## License
Both the code repository and the model weights are released under the Apache License (Version 2.0).

## Citation

```latex
@misc{stepfunformalizer2025,
      title={StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion}, 
      author={Yutong Wu and Di Huang and Ruosi Wan and Yue Peng and Shijie Shang and Chenrui Cao and Lei Qi and Rui Zhang and Zidong Du and Jie Yan and Xing Hu},
      year={2025},
      eprint={2508.04440},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.04440}, 
}
```

