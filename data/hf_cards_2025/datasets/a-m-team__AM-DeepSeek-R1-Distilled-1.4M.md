---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- zh
- en
tags:
- code
- math
- reasoning
- thinking
- deepseek-r1
- distill
size_categories:
- 1M<n<10M
configs:
- config_name: am_0.5M
  data_files: am_0.5M.jsonl.zst
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: info
      struct:
      - name: answer_content
        dtype: string
      - name: reference_answer
        dtype: string
      - name: source
        dtype: string
      - name: test_case
        struct:
        - name: test_code
          dtype: string
        - name: test_entry_point
          dtype: string
      - name: think_content
        dtype: string
    - name: role
      dtype: string
- config_name: am_0.9M
  data_files: am_0.9M.jsonl.zst
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: info
      struct:
      - name: answer_content
        dtype: string
      - name: reference_answer
        dtype: string
      - name: source
        dtype: string
      - name: test_case
        struct:
        - name: test_code
          dtype: string
        - name: test_entry_point
          dtype: string
      - name: think_content
        dtype: string
    - name: role
      dtype: string
- config_name: am_0.9M_sample_1k
  data_files: am_0.9M_sample_1k.jsonl
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: info
      struct:
      - name: answer_content
        dtype: string
      - name: reference_answer
        dtype: string
      - name: source
        dtype: string
      - name: test_case
        struct:
        - name: test_code
          dtype: string
        - name: test_entry_point
          dtype: string
      - name: think_content
        dtype: string
    - name: role
      dtype: string
---

**For more open-source datasets, models, and methodologies, please visit our [GitHub repository](https://github.com/a-m-team/a-m-models).**

[AM-DeepSeek-R1-Distilled-1.4M](https://huggingface.co/datasets/a-m-team/AM-DeepSeek-R1-Distilled-1.4M) is a large-scale general reasoning task dataset composed of 
high-quality and challenging reasoning problems. These problems are collected from numerous 
open-source datasets, semantically deduplicated, and cleaned to eliminate test set contamination. 
All responses in the dataset are distilled from the reasoning model (mostly DeepSeek-R1) and have undergone 
rigorous verification: mathematical problems are validated through answer checking, code 
problems via test cases, and other tasks through reward model evaluation. Specifically, 
responses in am_0.5M.jsonl are distilled by other open-source datasets, 
while those in am_0.9M.jsonl are distilled from the DeepSeek-R1-671B by the [AM team](https://huggingface.co/a-m-team).

We have validated the dataset through model training, confirming its effectiveness and demonstrating performance comparable to 
the distilled models from the DeepSeek team, and the details can be found in our technique reports 
[1.4 Million Open-Source Distilled Reasoning Dataset to Empower Large Language Model Traning](https://github.com/a-m-team/a-m-models/blob/main/docs/AM-DeepSeek-R1-Distilled-Dataset.pdf)

We are releasing these 1.4 million problems and responses to the research community, 
aiming to foster advancements in powerful reasoning-oriented Large Language Models (LLMs).
We sincerely thank the open-source community. Without their support, we would never have come this far.

## Model Training Performance based on this dataset

![alt text](AM-DeepSeek-R1-Distilled.jpeg)


## Scale & Composition

- AM-DeepSeek-R1-Distilled-1.4M: An Open-source Chinese & English dataset with reasoning traces (1.4 million entries).
- 0.5 million entries of data are entirely from open-source datasets, and 0.9 million entries of data are distilled from DeepSeek-R1-671B by AM team, which can be seen in the "am-0309" of the Response sources.
- Data processing:
  - Instruction part: we used the large language model to score all the instructions in terms of difficulty and category. Then we filtered the data according to the difficulty and category labels and conducted strict semantic deduplication to ensure the high-quality and diversity of the instructions.
  - Response part: we verified part of the data with reference answers using both rules and the large language model respectively. For code data with test cases, we used a sandbox for verification. Additionally, we used a reward model to score all the generated results and performed rejection sampling based on the rules and the reward model. 

## Unified Format

#### Dedicated fields
- **`messages`**: Array with user - assistant interaction objects, Each having `role`、`content` and `info` fields.
  - **`role`**: Indicates whether it's user or assistant, defining the sender of the message.
  - **`content`**: Follows `<think> reasoning process </think> <answer> solution </answer>` format in assistant message.
  - **`info`**: Contains metadata.
    - **`source`**: Instrction or response source.
    - **`reference_answer`**: Ground-truth answers only for some math, science, and other problems.
    - **`test_case`**: Test cases only for some code-related problems.
    - **`think_content`**: Reasoning steps in assistant message.
    - **`answer_content`**: Final solution in assistant message.

#### sample
```bash
{
"messages":[{
      "role": "user",
      "content": "Find the integral of \\(e^{-x} + e^{-2x} dx\\).",
      "info":{
        "source":"natural_reasoning",
        "reference_answer": "-e^{-x} - \\frac{1}{2}e^{-2x} + C",
        "test_case": null
      }
    },
    {
      "role": "assistant",
      "content": "<think>Okay, let's see. The user wants to find the integral of e^{-x} + e^{-2x} dx. Hmm, integrals of exponential functions. I remember that the integral of e^{kx} dx is (1/k)e^{kx} + C, right? But here the exponents are negative. Let me think.\n\nFirst, maybe I can split the integral into two parts because it's the sum of two functions. So, ∫(e^{-x} + e^{-2x}) dx = ∫e^{-x} dx + ∫e^{-2x} dx. That makes sense because integration is linear. Now, handle each integral separately.\n\nFor the first integral, ∫e^{-x} dx. If I use the formula, normally ∫e^{kx} dx = (1/k)e^{kx} + C. Here, k is -1. So substituting, that would be (1/(-1))e^{-x} + C, which simplifies to -e^{-x} + C. Wait, but since we're doing an indefinite integral here, each term will have its own constant, but since they're both combined, we'll have one constant at the end.\n\nNow the second integral: ∫e^{-2x} dx. Again, using the same formula, where k is -2. So that becomes (1/(-2))e^{-2x} + C, which is (-1/2)e^{-2x} + C.\n\nPutting both results together: the first integral is -e^{-x} and the second is (-1/2)e^{-2x}, so adding them and combining the constants gives the final answer. Let me check the signs again. The first term's coefficient is -1, and the second is -1/2. So combining those, it should be -e^{-x} - (1/2)e^{-2x} + C. Yeah, that looks right.\n\nLet me verify by differentiating the result. If I take the derivative of -e^{-x}, that's (-1)(-e^{-x}) = e^{-x}. For the second term, derivative of -1/2 e^{-2x} is (-1/2)(-2)e^{-2x} = e^{-2x}. So adding those derivatives gives e^{-x} + e^{-2x}, which matches the original integrand. Great, so the integration is correct. The constants of integration from both terms just combine into a single constant C at the end.\n</think>\n<answer>\nThe integral of \\(e^{-x} + e^{-2x}\\) with respect to \\(x\\) is:\n\n\\[\n\\int \\left(e^{-x} + e^{-2x}\\right) dx = -e^{-x} - \\frac{1}{2}e^{-2x} + C\n\\]\n\nwhere \\(C\\) is the constant of integration.\n</answer>",
      "info": {
        "source": "am-0309",
        "think_content": "Okay, let's see. The user wants to find the integral of e^{-x} + e^{-2x} dx. Hmm, integrals of exponential functions. I remember that the integral of e^{kx} dx is (1/k)e^{kx} + C, right? But here the exponents are negative. Let me think.\n\nFirst, maybe I can split the integral into two parts because it's the sum of two functions. So, ∫(e^{-x} + e^{-2x}) dx = ∫e^{-x} dx + ∫e^{-2x} dx. That makes sense because integration is linear. Now, handle each integral separately.\n\nFor the first integral, ∫e^{-x} dx. If I use the formula, normally ∫e^{kx} dx = (1/k)e^{kx} + C. Here, k is -1. So substituting, that would be (1/(-1))e^{-x} + C, which simplifies to -e^{-x} + C. Wait, but since we're doing an indefinite integral here, each term will have its own constant, but since they're both combined, we'll have one constant at the end.\n\nNow the second integral: ∫e^{-2x} dx. Again, using the same formula, where k is -2. So that becomes (1/(-2))e^{-2x} + C, which is (-1/2)e^{-2x} + C.\n\nPutting both results together: the first integral is -e^{-x} and the second is (-1/2)e^{-2x}, so adding them and combining the constants gives the final answer. Let me check the signs again. The first term's coefficient is -1, and the second is -1/2. So combining those, it should be -e^{-x} - (1/2)e^{-2x} + C. Yeah, that looks right.\n\nLet me verify by differentiating the result. If I take the derivative of -e^{-x}, that's (-1)(-e^{-x}) = e^{-x}. For the second term, derivative of -1/2 e^{-2x} is (-1/2)(-2)e^{-2x} = e^{-2x}. So adding those derivatives gives e^{-x} + e^{-2x}, which matches the original integrand. Great, so the integration is correct. The constants of integration from both terms just combine into a single constant C at the end.\n",
        "answer_content": "\nThe integral of \\(e^{-x} + e^{-2x}\\) with respect to \\(x\\) is:\n\n\\[\n\\int \\left(e^{-x} + e^{-2x}\\right) dx = -e^{-x} - \\frac{1}{2}e^{-2x} + C\n\\]\n\nwhere \\(C\\) is the constant of integration.\n"
      }
    }]
}
```

## Usage

The dataset is split into two compressed files based on response sources:

- **`am_0.9M.jsonl.zst`**: Responses from the `am-0309` source.
- **`am_0.5M.jsonl.zst`**: Responses from other sources.
- Additionally, a subset of 1,000 random samples (`am_0.9M_1k.jsonl`) from `am-0309` is provided for quick experimentation.

Files are compressed using [zstd](https://github.com/facebook/zstd) for faster download and reduced storage requirements.

**Decompression Instructions**:
```bash
apt install zstd
zstd -d am_0.9M.jsonl.zst -o am_0.9M.jsonl
```

**How to use with `load_dataset`**

```python
from datasets import load_dataset, Features, Value
features = Features({
    "messages": [
        {
            "role": Value("string"),
            "content": Value("string"),
            "info": {
                "source": Value("string"),
                "reference_answer": Value("string"),
                "test_case": Value("string"),
                "think_content": Value("string"),
                "answer_content": Value("string")
            }
        }
    ]
})
# Take downloading "am_0.9M_sample_1k.jsonl" as an example.
data = load_dataset('a-m-team/AM-DeepSeek-R1-Distilled-1.4M', 'am_0.9M_sample_1k', features=features)
```


## Sources
- Open-source data: Instructions and reasoning traces from existing datasets.
- AM distilled data: High-quality instructions from the Open-source dataset, augmented with reasoning traces and solutions generated by DeepSeek-R1.
#### Instruction sources
| Source | Nums |
| --- | --- |
| natural_reasoning | 319085 |
| InfinityInstruct | 306675 |
| KodCode | 210838 |
| Dolphin - R1 | 63921 |
| openR1Math_extended | 63290 |
| NuminaMath_1.5 | 62446 |
| openR1Math_default | 62239 |
| codeio | 55176 |
| GeneralThought - Feb25 | 50600 |
| openThoughts | 34620 |
| OpenCoder | 22249 |
| data_ablation_full59K | 14155 |
| MetaMathQA | 14083 |
| ... | ... |


#### Response sources
| Source | Nums |
| --- | --- |
| am-0309 | 900000 |
| KodCode | 210838 |
| openR1Math_extended | 63290 |
| Dolphin - R1 | 62750 |
| openR1Math_default | 60839 |
| GeneralThought - Feb25 | 50600 |
| openThoughts | 31431 |
| data_ablation_full59K | 14155 |
| Bespoke17k | 5747 |
| ... | ... |


## Limitation and Usage Limits

We require developers only use the open-sourced code, data, model and any other artifacts 
generated via this project for research purposes. Commercial use and other potential harmful use cases are not allowed.

Since this dataset was generated by LLM and was not strictly verified,
it still has shortcomings regarding factuality and other aspects. When using this dataset, careful inspection is needed.

This dataset does not represent anyone's ground, interest or thought, and is not related to 
any kind of claim of any groups. The developers of this project do not assume any responsibility to potential harm inflicted by using this dataset and project.

Due to the nested relationships among the sources of some data, there may be issues regarding the inaccuracy of the sources. 


## Citation
If you use this data, please cite with the following BibTex entry:
```
@misc{zhao202514millionopensourcedistilled,
      title={1.4 Million Open-Source Distilled Reasoning Dataset to Empower Large Language Model Training}, 
      author={Han Zhao and Haotian Wang and Yiping Peng and Sitong Zhao and Xiaoyu Tian and Shuaiting Chen and Yunjie Ji and Xiangang Li},
      year={2025},
      eprint={2503.19633},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.19633}, 
}
```
