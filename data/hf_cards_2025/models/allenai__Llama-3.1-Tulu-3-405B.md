---
license: llama3.1
language:
- en
pipeline_tag: text-generation
datasets:
- allenai/RLVR-MATH
base_model:
- allenai/Llama-3.1-Tulu-3-405B-DPO
library_name: transformers
---

<img src="https://huggingface.co/datasets/allenai/blog-images/resolve/main/tulu3/Tulu3-logo.png" alt="Tulu 3 banner" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# Llama-3.1-Tulu-3-405B

Tülu 3 is a leading instruction following model family, offering a post-training package with fully open-source data, code, and recipes designed to serve as a comprehensive guide for modern techniques.
This is one step of a bigger process to training fully open-source models, like our [OLMo](https://allenai.org/olmo) models.
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.

## Model description

- **Model type:** A model trained on a mix of publicly available, synthetic and human-created datasets.
- **Language(s) (NLP):** Primarily English
- **License:** Llama 3.1 Community License Agreement
- **Finetuned from model:** allenai/Llama-3.1-Tulu-3-405B-DPO

### Model Sources

- **Training Repository:** https://github.com/allenai/open-instruct
- **Eval Repository:** https://github.com/allenai/olmes
- **Paper:** https://arxiv.org/abs/2411.15124
- **Demo:** https://playground.allenai.org/

### Model Family

| **Stage**           | **Llama 3.1 8B**                                                                                          | **Llama 3.1 70B**                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Base Model**       | [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B)                                | [meta-llama/Llama-3.1-70B](https://huggingface.co/meta-llama/Llama-3.1-70B)                              |
| **SFT**              | [allenai/Llama-3.1-Tulu-3-8B-SFT](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT)                | [allenai/Llama-3.1-Tulu-3-70B-SFT](https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-SFT)              |
| **DPO**              | [allenai/Llama-3.1-Tulu-3-8B-DPO](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-DPO)                | [allenai/Llama-3.1-Tulu-3-70B-DPO](https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B-DPO)              |
| **Final Models (RLVR)**     | [allenai/Llama-3.1-Tulu-3-8B](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B)                        | [allenai/Llama-3.1-Tulu-3-70B](https://huggingface.co/allenai/Llama-3.1-Tulu-3-70B)                      |
| **Reward Model (RM)**| [allenai/Llama-3.1-Tulu-3-8B-RM](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM)                                                     | (Same as 8B)                                                     |

| **Stage** | **Llama 3.1 405B** |
|-----------|-------------------|
| **Base Model** | [meta-llama/llama-3.1-405B](https://huggingface.co/meta-llama/llama-3.1-405B) |
| **SFT** | [allenai/llama-3.1-Tulu-3-405B-SFT](https://huggingface.co/allenai/llama-3.1-Tulu-3-405B-SFT) |
| **DPO** | [allenai/llama-3.1-Tulu-3-405B-DPO](https://huggingface.co/allenai/llama-3.1-Tulu-3-405B-DPO) |
| **Final Model (RLVR)** | [allenai/llama-3.1-Tulu-3-405B](https://huggingface.co/allenai/llama-3.1-Tulu-3-405B) |
| **Reward Model (RM)**| (Same as 8B)


## Using the model

### Loading with HuggingFace

To load the model with HuggingFace, use the following snippet:
```
from transformers import AutoModelForCausalLM

tulu_model = AutoModelForCausalLM.from_pretrained("allenai/Llama-3.1-Tulu-3-405B")
```

### VLLM

As a Llama base model, the model can be easily served with:
```
vllm serve allenai/Llama-3.1-Tulu-3-405B
```
Note that given the long chat template of Llama, you may want to use `--max_model_len=8192`.

### Chat template

The chat template for our models is formatted as:
```
<|user|>\nHow are you doing?\n<|assistant|>\nI'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
Or with new lines expanded:
```
<|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
It is embedded within the tokenizer as well, for `tokenizer.apply_chat_template`.

### System prompt

In Ai2 demos, we use this system prompt by default:
```
You are Tulu 3, a helpful and harmless AI Assistant built by the Allen Institute for AI.
```
The model has not been trained with a specific system prompt in mind.

### Bias, Risks, and Limitations

The Tülu3 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
It is also unknown what the size and composition of the corpus was used to train the base Llama 3.1 models, however it is likely to have included a mix of Web data and technical sources like books and code. 
See the Falcon 180B model card for an example of this.


## Performance

*Note, see the updated version of the paper for the latest, fixed evaluations that improve scores for models such as Qwen 2.5 Instruct.*


| Benchmark (eval)                | Tülu 3 SFT 8B | Tülu 3 DPO 8B | Tülu 3 8B | Llama 3.1 8B Instruct | Qwen 2.5 7B Instruct | Magpie 8B | Gemma 2 9B Instruct | Ministral 8B Instruct |
|---------------------------------|----------------|----------------|------------|------------------------|----------------------|-----------|---------------------|-----------------------|
| **Avg.**                        | 60.4           | 64.4           | **64.8**   | 62.2                  | 57.8                | 44.7      | 55.2               | 58.3                 |
| **MMLU (0 shot, CoT)**          | 65.9           | 68.7           | 68.2       | 71.2                  | **76.6**            | 62.0      | 74.6               | 68.5                 |
| **PopQA (15 shot)**             | **29.3**       | 29.3           | 29.1       | 20.2                  | 18.1                | 22.5      | 28.3               | 20.2                 |
| **TruthfulQA (6 shot)**         | 46.8           | 56.1           | 55.0       | 55.1                  | **63.1**            | 57.0      | 61.4               | 55.5                 |
| **BigBenchHard (3 shot, CoT)**  | **67.9**       | 65.8           | 66.0       | 62.8                  | 21.7                | 0.9       | 2.5                | 56.2                 |
| **DROP (3 shot)**               | 61.3           | 62.5           | **62.6**   | 61.5                  | 54.4                | 49.4      | 58.8               | 56.2                 |
| **MATH (4 shot CoT, Flex)**     | 31.5           | 42.0           | **43.7**   | 42.5                  | 14.8                | 5.1       | 29.8               | 40.0                 |
| **GSM8K (8 shot, CoT)**         | 76.2           | 84.3           | **87.6**   | 83.4                  | 83.8                | 61.2      | 79.7               | 80.0                 |
| **HumanEval (pass@10)**         | 86.2           | 83.9           | 83.9       | 86.3                  | **93.1**            | 75.4      | 71.7               | 91.0                 |
| **HumanEval+ (pass@10)**        | 81.4           | 78.6           | 79.2       | 82.9                  | **89.7**            | 69.1      | 67.0               | 88.5                 |
| **IFEval (prompt loose)**       | 72.8           | 81.1           | **82.4**   | 80.6                  | 74.7                | 38.8      | 69.9               | 56.4                 |
| **AlpacaEval 2 (LC % win)**     | 12.4           | 33.5           | 34.5       | 24.2                  | 29.0                | **49.0**  | 43.7               | 31.4                 |
| **Safety (6 task avg.)**        | **93.1**       | 87.2           | 85.5       | 75.2                  | 75.0                | 46.4      | 75.5               | 56.2                 |

| Benchmark (eval)                | Tülu 3 70B SFT | Tülu 3 DPO 70B | Tülu 3 70B | Llama 3.1 70B Instruct | Qwen 2.5 72B Instruct | Hermes 3 Llama 3.1 70B | Nemotron Llama 3.1 70B |
|---------------------------------|-----------------|-----------------|-------------|-------------------------|-----------------------|------------------------|-------------------------|
| **Avg.**                        | 72.6            | 75.9            | **76.0**    | 73.4                   | 71.5                  | 68.3                   | 65.5                   |
| **MMLU (0 shot, CoT)**          | 78.9            | 83.3            | 83.1        | 85.3                   | **85.5**             | 80.4                   | 83.8                   |
| **PopQA (15 shot)**             | **48.6**        | 46.3            | 46.5        | 46.4                   | 30.6                  | 48.1                   | 36.4                   |
| **TruthfulQA (6 shot)**         | 55.7            | 67.9            | 67.6        | 66.8                   | **69.9**             | 66.5                   | 62.6                   |
| **BigBenchHard (3 shot, CoT)**  | **82.7**        | 81.8            | 82.0        | 73.8                   | 67.2                  | 82.1                   | 0.7                    |
| **DROP (3 shot)**               | **77.2**        | 74.1            | 74.3        | 77.0                   | 34.2                  | 73.2                   | 68.8                   |
| **MATH (4 shot CoT, Flex)**     | 53.7            | 62.3            | 63.0        | 56.4                   | **74.3**             | 41.9                   | 55.0                   |
| **GSM8K (8 shot, CoT)**         | 91.1            | 93.5            | 93.5        | **93.7**              | 89.5                  | 90.0                   | 84.7                   |
| **HumanEval (pass@10)**         | 92.9            | 92.4            | 92.4        | 93.6                   | 94.0                  | 89.6                   | **94.1**              |
| **HumanEval+ (pass@10)**        | 87.3            | 88.4            | 88.0        | 89.5                   | **90.8**             | 85.9                   | 85.5                   |
| **IFEval (prompt loose)**       | 82.1            | 82.6            | 83.2        | **88.0**              | 87.6                  | 76.0                   | 79.9                   |
| **AlpacaEval 2 (LC % win)**     | 26.3            | 49.6            | 49.8        | 33.4                   | 47.7                  | 28.4                   | **66.1**              |
| **Safety (6 task avg.)**        | **94.4**        | 89.0            | 88.3        | 76.5                   | 87.0                  | 57.9                   | 69.0                   |

| Benchmark (eval) | Tülu 3 405B SFT | Tülu 3 405B DPO | Tülu 3 405B | Llama 3.1 405B Instruct | Nous Hermes 3 405B | Deepseek V3 | GPT 4o (11-24) |
|-----------------|----------------|----------------|-------------|------------------------|-------------------|-------------|----------------|
| **Avg w/o Safety** | 76.3 | 79.0 | 80.0 | 78.1 | 74.4 | 79.0 | **80.5** |
| **Avg w/ Safety** | 77.5 | 79.6 | 80.7 | 79.0 | 73.5 | 75.9 | **81.6** |
| **MMLU (5 shot, CoT)** | 84.4 | 86.6 | 87.0 | **88.0** | 84.9 | 82.1 | 87.9 |
| **PopQA (3 shot)** | **55.7** | 55.4 | 55.5 | 52.9 | 54.2 | 44.9 | 53.6 |
| **BigBenchHard (0 shot, CoT)** | 88.0 | 88.8 | 88.6 | 87.1 | 87.7 | **89.5** | 83.3 |
| **MATH (4 shot, Flex)** | 63.4 | 59.9 | 67.3 | 66.6 | 58.4 | **72.5** | 68.8 |
| **GSM8K (8 shot, CoT)** | 93.6 | 94.2 | **95.5** | 95.4 | 92.7 | 94.1 | 91.7 |
| **HumanEval (pass@10)** | 95.7 | **97.2** | 95.9 | 95.9 | 92.3 | 94.6 | 97.0 |
| **HumanEval+ (pass@10)** | 93.3 | **93.9** | 92.9 | 90.3 | 86.9 | 91.6 | 92.7 |
| **IFEval (prompt loose)** | 82.4 | 85.0 | 86.0 | **88.4** | 81.9 | 88.0 | 84.8 |
| **AlpacaEval 2 (LC % win)** | 30.4 | 49.8 | 51.4 | 38.5 | 30.2 | 53.5 | **65.0** |
| **Safety (6 task avg.)** | 87.7 | 85.5 | 86.7 | 86.8 | 65.8 | 72.2 | **90.9** |


## Hyperparamters

PPO settings for RLVR:
- **Learning Rate**: 1 × 10⁻⁷
- **Discount Factor (gamma)**: 1.0
- **General Advantage Estimation (lambda)**: 0.95
- **Mini-batches (N_mb)**: 1
- **PPO Update Iterations (K)**: 4
- **PPO's Clipping Coefficient (epsilon)**: 0.2
- **Value Function Coefficient (c1)**: 0.1
- **Gradient Norm Threshold**: 1.0
- **Learning Rate Schedule**: Linear
- **Generation Temperature**: 1.0
- **Batch Size (effective)**: 1,856
- **Max Token Length**: 2,048
- **Max Prompt Token Length**: 2,048
- **Penalty Reward Value for Responses without an EOS Token**: -10.0
- **Response Length**: 2,048
- **Total Episodes**: 300,000
- **KL penalty coefficient (beta)**: 0.05
- **Warm up ratio (omega)**: 0.0

## License and use

All Llama 3.1 Tülu3 models are released under Meta's [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/).
Llama 3.1 is licensed under the Llama 3.1 Community License, Copyright © Meta Platforms, Inc.
Tülu3 is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).

The models have been fine-tuned using a dataset mix with outputs generated from third party models and are subject to additional terms: 
[Gemma Terms of Use](https://ai.google.dev/gemma/terms) and [Qwen License Agreement](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct/blob/main/LICENSE) (models were improved using Qwen 2.5).


## Citation

If Tülu3 or any of the related materials were helpful to your work, please cite:
```
@article{lambert2024tulu3,
  title = {Tülu 3: Pushing Frontiers in Open Language Model Post-Training},
  author = {
    Nathan Lambert and 
    Jacob Morrison and 
    Valentina Pyatkin and 
    Shengyi Huang and 
    Hamish Ivison and 
    Faeze Brahman and 
    Lester James V. Miranda and 
    Alisa Liu and 
    Nouha Dziri and 
    Shane Lyu and 
    Yuling Gu and 
    Saumya Malik and 
    Victoria Graf and 
    Jena D. Hwang and 
    Jiangjiang Yang and
    Ronan Le Bras and
    Oyvind Tafjord and
    Chris Wilhelm and
    Luca Soldaini and 
    Noah A. Smith and 
    Yizhong Wang and 
    Pradeep Dasigi and 
    Hannaneh Hajishirzi
  },
  year = {2024},
  email = {tulu@allenai.org}
}
```