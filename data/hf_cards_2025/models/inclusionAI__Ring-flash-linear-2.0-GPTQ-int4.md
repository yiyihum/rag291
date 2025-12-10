---
license: mit
language:
- en
base_model:
- inclusionAI/Ring-mini-linear-2.0
pipeline_tag: text-generation
---
# Quantized Ring-Linear-2.0

## Introduction

To enable deployment of [Ring-Linear-2.0](https://github.com/inclusionAI/Ring-V2/blob/main/hybrid_linear/README.md
) on memory-constrained devices, we release quantized weights using the GPTQ INT4 format. Additionally, we evaluate the online FP8 quantization performance of `Ring-Linear-2.0` models, which closely approaches that of BF16 precision.



## Model Downloads


|       **Model**        | **Maximum Supported Length** |                                                                             **Download**                                                                             |
|:----------------------:| :----------------: |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Ring-flash-linear-2.0-GPTQ-int4  |        128k         |  [🤗 HuggingFace](https://huggingface.co/inclusionAI/Ring-flash-linear-2.0-GPTQ-int4) <br>[🤖 ModelScope](https://www.modelscope.cn/models/inclusionAI/Ring-flash-linear-2.0-GPTQ-int4)  |
| Ring-mini-linear-2.0-GPTQ-int4   |        512k         |  [🤗 HuggingFace](https://huggingface.co/inclusionAI/Ring-mini-linear-2.0-GPTQ-int4) <br>[🤖 ModelScope](https://www.modelscope.cn/models/inclusionAI/Ring-mini-linear-2.0-GPTQ-int4)  |


## Quickstart


### 🚀 vLLM

#### Environment Preparation

Since the Pull Request (PR) has not been submitted to the vLLM community at this stage, please prepare the environment by following the steps below.

First, create a Conda environment with Python 3.10 and CUDA 12.8:
```shell
conda create -n vllm python=3.10
conda activate vllm
```

Next, install our vLLM wheel package:
```shell
pip install https://media.githubusercontent.com/media/zheyishine/vllm_whl/refs/heads/main/vllm-0.8.5.post2.dev28%2Bgd327eed71.cu128-cp310-cp310-linux_x86_64.whl --force-reinstall
```

Finally, install compatible versions of transformers after vLLM is installed:
```shell
pip install transformers==4.51.1 
```

#### Offline Inference

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained("inclusionAI/Ring-flash-linear-2.0-GPTQ-int4")
    
    sampling_params = SamplingParams(temperature=0.6, top_p=1.0, max_tokens=16384)

    # use `max_num_seqs=1` without concurrency
    llm = LLM(model="inclusionAI/Ring-flash-linear-2.0-GPTQ-int4", dtype='auto', enable_prefix_caching=False, max_num_seqs=128)
    
    
    prompt = "Give me a short introduction to large language models."
    messages = [
        {"role": "user", "content": prompt}
    ]
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    outputs = llm.generate([text], sampling_params)
    for output in outputs:
        print(output.outputs[0].text)
```

#### Online Inference
```shell
vllm serve inclusionAI/Ring-flash-linear-2.0-GPTQ-int4 \
              --tensor-parallel-size 2 \
              --pipeline-parallel-size 1 \
              --gpu-memory-utilization 0.90 \
              --max-num-seqs 128 \
              --no-enable-prefix-caching
              --api-key your-api-key
```



## Evaluation


We evaluate the INT4 and FP8 quantized models using several datasets. The FP8 quantization is applied via the quantization="fp8" argument in SGLang or vLLM.



### Ring-mini-linear-2.0
|  **Dataset** | **BF16** | **FP8** | **GPTQ-Int4** |
| :----------------: |:--------:|:-------:|:-------------:|   
|       AIME25       |  73.65   |  72.40  |     66.56     |
|       AIME24       |  79.95   |  79.53  |     74.95     |
|       LiveCodeBench|  59.53   |  58.42  |     56.29     |
|       GPQA         |  65.69   |  66.79  |     62.53     |

### Ring-flash-linear-2.0
|  **Dataset** | **BF16** | **FP8** |  **GPTQ-Int4** |
| :----------------: |:--------:|:-------:|   :-----------------------:|
|       AIME25       |  85.10  |  84.22  | 82.88 |
|       LiveCodeBench|  69.82  |  69.44  | 66.14 |
|       GPQA         |  72.85  |  72.95  | 71.72 |




## License

This code repository is licensed under [the MIT License](https://github.com/inclusionAI/Ring-V2/blob/master/LICENSE).

## Citation

If you find our work helpful, feel free to give us a cite.