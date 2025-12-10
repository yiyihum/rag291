---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
base_model:
- allenai/OLMoE-1B-7B-0125-DPO
library_name: transformers
datasets:
- allenai/RLVR-GSM
---

<img alt="OLMo Logo" src="https://huggingface.co/allenai/OLMoE-1B-7B-0125/resolve/main/olmoe-logo.png" width="242px">


# OLMoE-1B-7B-0125-Instruct


## Release Documentation

OLMoE-1B-7B-0125-Instruct January 2025 is post-trained variant of the [OLMoE-1B-7B January 2025](https://huggingface.co/allenai/OLMoE-1B-7B-0125) model, which has undergone supervised finetuning on an OLMo-specific variant of the [Tülu 3 dataset](allenai/tulu-3-sft-olmo-2-mixture) and further DPO training on [this dataset](https://huggingface.co/datasets/allenai/olmo-2-1124-13b-preference-mix), and finally RLVR training using [this data](https://huggingface.co/datasets/allenai/RLVR-GSM).
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.
Check out the [OLMoE paper](https://arxiv.org/abs/2409.02060) or [Tülu 3 paper](https://arxiv.org/abs/2411.15124) for more details!

OLMo is a series of **O**pen **L**anguage **Mo**dels designed to enable the science of language models. 
These models are trained on the Dolma dataset. We are releasing all code, checkpoints, logs (coming soon), and associated training details. 
The core models released in this batch include the following:


| **Stage**           | **OLMoE 1B-7B**                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------|
| **Base Model**       | [allenai/OLMoE-1B-7B-0125](https://huggingface.co/allenai/OLMoE-1B-7B-0125)                                |
| **SFT**              | [allenai/OLMoE-1B-7B-0125-SFT](https://huggingface.co/allenai/OLMoE-1B-7B-0125-SFT)                |
| **DPO**              | [allenai/OLMoE-1B-7B-0125-DPO](https://huggingface.co/allenai/OLMoE-1B-7B-0125-DPO)                |
| **Final Models (RLVR)** | [allenai/OLMoE-1B-7B-0125-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0125-Instruct)                        |
| **Reward Model (RM)**| [allenai/OLMoE-1B-7B-0125-RM](https://huggingface.co/allenai/OLMoE-1B-7B-0125-RM)                                                     |



## Model description

- **Model type:** A model trained on a mix of publicly available, synthetic and human-created datasets.
- **Language(s) (NLP):** Primarily English
- **License:** Apache 2.0
- **Finetuned from model:** allenai/OLMoE-1B-7B-0125-DPO

### Model Sources

- **Project Page:** https://allenai.org/olmo
- **Repositories:** 
    - Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo
    - Evaluation code: https://github.com/allenai/olmes
    - Further fine-tuning code: https://github.com/allenai/open-instruct
- **Paper:** https://arxiv.org/abs/2409.02060
- **Demo:** https://playground.allenai.org/

## Installation

OLMo 2 will be supported in the next version of Transformers, and you need to install it from the main branch using:
```bash
pip install --upgrade git+https://github.com/huggingface/transformers.git
```

## Using the model

### Loading with HuggingFace

To load the model with HuggingFace, use the following snippet:
```
from transformers import AutoModelForCausalLM

olmo_model = AutoModelForCausalLM.from_pretrained("OLMoE-1B-7B-0125-Instruct")
```

### Chat template

The chat template for our models is formatted as:
```
<|endoftext|><|user|>\nHow are you doing?\n<|assistant|>\nI'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
Or with new lines expanded:
```
<|endoftext|><|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
It is embedded within the tokenizer as well, for `tokenizer.apply_chat_template`.

### System prompt

In Ai2 demos, we use this system prompt by default:
```
You are OLMo 2, a helpful and harmless AI Assistant built by the Allen Institute for AI.
```
The model has not been trained with a specific system prompt in mind.

### Bias, Risks, and Limitations

The OLMo-2 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
See the Falcon 180B model card for an example of this.


## Performance

| Benchmark (eval)                | OLMoE-1B-7B-0125-Instruct | OLMoE-1B-7B-0924-Instruct | OLMoE-1B-7B-0125-DPO | OLMoE-1B-7B-0125-SFT | OLMoE-1B-7B-0924-SFT |
|--------------------------------|---------------------------|--------------------------|----------------------|---------------------|---------------------|
| **Avg.**                       | **45.62**                 | 38.44                   | 45.05                | 41.76               | 37.05               |
| **MMLU (CoT)**                 | 55.08                     | 54.57                   | 54.93                | **55.26**           | 54.32               |
| **PopQA**                      | 19.75                     | 20.56                   | 19.65                | 20.12               | **21.01**           |
| **TruthfulQA**                 | **50.56**                 | 49.14                   | 49.99                | 45.48               | 44.66               |
| **BigBenchHard (CoT)**         | **38.61**                 | 36.78                   | 37.37                | 37.31               | 36.55               |
| **DROP**                       | 47.87                     | 34.48                   | 48.38                | **48.57**           | 34.71               |
| **MATH (Flex)**                | **21.41**                 | 8.16                    | 20.36                | 21.38               | 8.15                |
| **GSM8K**                      | **72.40**                 | 47.38                   | 64.59                | 55.72               | 42.46               |
| **HumanEval**                  | 62.30                     | 63.04                   | 61.92                | 62.58               | **63.72**           |
| **HumanEval+**                 | 54.37                     | **58.93**               | 57.61                | 55.67               | 57.40               |
| **IFEval**                     | **66.36**                 | 45.29                   | 65.62                | 56.56               | 41.22               |
| **AlpacaEval**                 | 17.99                     | 7.54                    | **19.50**            | 5.83                | 6.38                |
| **Safety (average)**           | 90.40                     | 51.40                   | 91.40                | **94.50**           | 65.80               |

## License and use

OLMoE is licensed under the Apache 2.0 license.
OLMoE is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).
This model has been fine-tuned using a dataset mix with outputs generated from third party models and are subject to additional terms: [Gemma Terms of Use](https://ai.google.dev/gemma/terms).

## Citation

```bibtex
@misc{muennighoff2024olmoeopenmixtureofexpertslanguage,
      title={OLMoE: Open Mixture-of-Experts Language Models}, 
      author={Niklas Muennighoff and Luca Soldaini and Dirk Groeneveld and Kyle Lo and Jacob Morrison and Sewon Min and Weijia Shi and Pete Walsh and Oyvind Tafjord and Nathan Lambert and Yuling Gu and Shane Arora and Akshita Bhagia and Dustin Schwenk and David Wadden and Alexander Wettig and Binyuan Hui and Tim Dettmers and Douwe Kiela and Ali Farhadi and Noah A. Smith and Pang Wei Koh and Amanpreet Singh and Hannaneh Hajishirzi},
      year={2024},
      eprint={2409.02060},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.02060}, 
}
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

