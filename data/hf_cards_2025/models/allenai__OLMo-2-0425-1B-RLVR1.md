---
license: apache-2.0
language:
- en
datasets:
- allenai/RLVR-GSM-MATH-IF-Mixed-Constraints
base_model:
- allenai/OLMo-2-0425-1B-DPO
pipeline_tag: text-generation
library_name: transformers
---

<img alt="OLMo Logo" src="https://huggingface.co/datasets/allenai/blog-images/resolve/main/olmo2/olmo.png" width="242px">

OLMo 2 1B RLVR 1 April 2025 is post-trained variant of the [allenai/OLMo-2-0425-1B-DPO](https://huggingface.co/allenai/OLMo-2-0425-1B-DPO) model, which has undergone supervised finetuning on an OLMo-specific variant of the [Tülu 3 dataset](https://huggingface.co/datasets/allenai/tulu-3-sft-olmo-2-mixture-0225), further DPO training on [this dataset](https://huggingface.co/datasets/allenai/olmo-2-0425-1b-preference-mix), and final RLVR training on [this dataset](https://huggingface.co/datasets/allenai/RLVR-GSM-MATH-IF-Mixed-Constraints).
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.
Check out the [OLMo 2 paper](https://arxiv.org/abs/2501.00656) or [Tülu 3 paper](https://arxiv.org/abs/2411.15124) for more details!

OLMo is a series of **O**pen **L**anguage **Mo**dels designed to enable the science of language models. 
These models are trained on the Dolma dataset. We are releasing all code, checkpoints, logs, and associated training details. 


## Model description

- **Model type:** A model trained on a mix of publicly available, synthetic and human-created datasets.
- **Language(s) (NLP):** Primarily English
- **License:** Apache 2.0
- **Finetuned from model:** allenai/OLMo-2-0425-1B-DPO

### Model Sources

- **Project Page:** https://allenai.org/olmo
- **Repositories:** 
    - Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo-core
    - Evaluation code: https://github.com/allenai/olmes
    - Further fine-tuning code: https://github.com/allenai/open-instruct
- **Paper:** https://arxiv.org/abs/2501.00656
- **Demo:** https://playground.allenai.org/

## Installation

OLMo 2 1B is supported in transformers v4.48 or higher:
```bash
pip install transformers>=4.48
```

If using vLLM, you will need to install from the main branch until v0.7.4 is released. Please

## Using the model

### Loading with HuggingFace

To load the model with HuggingFace, use the following snippet:
```
from transformers import AutoModelForCausalLM

olmo_model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B-RLVR1")
```

### Chat template

*NOTE: This is different than previous OLMo 2 and Tülu 3 models due to a minor change in configuration. It does NOT have the bos token before the rest. Our other models have <|endoftext|> at the beginning of the chat template.*

The chat template for our models is formatted as:
```
<|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
Or with new lines expanded:
```
<|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```
It is embedded within the tokenizer as well, for `tokenizer.apply_chat_template`.

### Intermediate Checkpoints

To facilitate research on RL finetuning, we have released our intermediate checkpoints during the model's RLVR training.
The model weights are saved every 20 training steps, and can be accessible in the revisions of the HuggingFace repository.
For example, you can load with:
```
olmo_model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B-RLVR1", revision="step_200")
```

### Bias, Risks, and Limitations

The OLMo-2 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so).


## Performance

| Model | Average | AlpacaEval 2 LC | BBH | DROP | GSM8K | IFEval | MATH | MMLU | Safety | PopQA | TruthQA |
|-------|---------|-----------------|-----|------|-------|--------|------|------|--------|-------|---------|
| **OLMo 1B 0724** | 24.4 | 2.4 | 29.9 | 27.9 | 10.8 | 25.3 | 2.2 | 36.6 | 52.0 | 12.1 | 44.3 |
| **SmolLM2 1.7B** | 34.2 | 5.8 | 39.8 | 30.9 | 45.3 | 51.6 | 20.3 | 34.3 | 52.4 | 16.4 | 45.3 |
| **Gemma 3 1B** | 38.3 | 20.4 | 39.4 | 25.1 | 35.0 | 60.6 | 40.3 | 38.9 | 70.2 | 9.6 | 43.8 |
| **Llama 3.1 1B** | 39.3 | 10.1 | 40.2 | 32.2 | 45.4 | 54.0 | 21.6 | 46.7 | 87.2 | 13.8 | 41.5 |
| **Qwen 2.5 1.5B** | 41.7 | 7.4 | 45.8 | 13.4 | 66.2 | 44.2 | 40.6 | 59.7 | 77.6 | 15.5 | 46.5 |
| **---** |  |  |  |  |  |  |  |  |  |  |  |
| **OLMo 2 1B SFT** | 36.9 | 2.4 | 32.8 | 33.8 | 52.1 | 50.5 | 13.2 | 36.4 | 93.2 | 12.7 | 42.1 |
| **OLMo 2 1B DPO** | 40.6 | 9.5 | 33.0 | 34.5 | 59.0 | 67.1 | 14.1 | 39.9 | 89.9 | 12.3 | 46.4 |
| **OLMo 2 1B** | 42.7 | 9.1 | 35.0 | 34.6 | 68.3 | 70.1 | 20.7 | 40.0 | 87.6 | 12.9 | 48.7 |


## License and use

OLMo 2 is licensed under the Apache 2.0 license.
OLMo 2 is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).

## Citation

```bibtex
@article{olmo20242olmo2furious,
      title={2 OLMo 2 Furious}, 
      author={Team OLMo and Pete Walsh and Luca Soldaini and Dirk Groeneveld and Kyle Lo and Shane Arora and Akshita Bhagia and Yuling Gu and Shengyi Huang and Matt Jordan and Nathan Lambert and Dustin Schwenk and Oyvind Tafjord and Taira Anderson and David Atkinson and Faeze Brahman and Christopher Clark and Pradeep Dasigi and Nouha Dziri and Michal Guerquin and Hamish Ivison and Pang Wei Koh and Jiacheng Liu and Saumya Malik and William Merrill and Lester James V. Miranda and Jacob Morrison and Tyler Murray and Crystal Nam and Valentina Pyatkin and Aman Rangapur and Michael Schmitz and Sam Skjonsberg and David Wadden and Christopher Wilhelm and Michael Wilson and Luke Zettlemoyer and Ali Farhadi and Noah A. Smith and Hannaneh Hajishirzi},
      year={2024},
      eprint={2501.00656},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00656}, 
}
```