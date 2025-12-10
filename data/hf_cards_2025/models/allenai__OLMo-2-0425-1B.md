---
license: apache-2.0
language:
- en
library_name: transformers
---

## Model Details

<img alt="OLMo Logo" src="https://huggingface.co/datasets/allenai/blog-images/resolve/main/olmo2/olmo.png" width="242px" style="margin-left:'auto' margin-right:'auto' display:'block'">


# Model Card for OLMo 2 1B

We introduce OLMo 2 1B, the smallest model in the OLMo 2 family.
OLMo 2 was pre-trained on [OLMo-mix-1124](https://huggingface.co/datasets/allenai/olmo-mix-1124)
and uses [Dolmino-mix-1124](https://huggingface.co/datasets/allenai/dolmino-mix-1124) for mid-training.

OLMo 2 is the latest in a series of **O**pen **L**anguage **Mo**dels designed to enable the science of language models.
We have released all code, checkpoints, logs, and associated training details on [GitHub](https://github.com/allenai/OLMo).

| Size | Training Tokens | Layers | Hidden Size | Attention Heads | Context Length |
|------|--------|---------|-------------|-----------------|----------------|
| [OLMo 2-1B](https://huggingface.co/allenai/OLMo-2-0425-1B) | 4 Trillion   | 16     | 2048        | 16              |  4096  |
| [OLMo 2-7B](https://huggingface.co/allenai/OLMo-2-1124-7B) | 4 Trillion   | 32     | 4096        | 32              |  4096  |
| [OLMo 2-13B](https://huggingface.co/allenai/OLMo-2-1124-13B) | 5 Trillion   | 40     | 5120        | 40              |  4096  |
| [OLMo 2-32B](https://huggingface.co/allenai/OLMo-2-0325-32B) | 6 Trillion   | 64     | 5120        | 40              |  4096  |

The core models released in this batch include the following:

| **Stage**             | **OLMo 2 1B**                                                                                           | **OLMo 2 7B**                                                                                           | **OLMo 2 13B**                                                                                          | **OLMo 2 32B**                                                                                           |
|------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Base Model**         | [allenai/OLMo-2-0425-1B](https://huggingface.co/allenai/OLMo-2-0425-1B)                                 | [allenai/OLMo-2-1124-7B](https://huggingface.co/allenai/OLMo-2-1124-7B)                                 | [allenai/OLMo-2-1124-13B](https://huggingface.co/allenai/OLMo-2-1124-13B)                               | [allenai/OLMo-2-0325-32B](https://huggingface.co/allenai/OLMo-2-0325-32B)                                |
| **SFT**                | [allenai/OLMo-2-0425-1B-SFT](https://huggingface.co/allenai/OLMo-2-0425-1B-SFT)                        | [allenai/OLMo-2-1124-7B-SFT](https://huggingface.co/allenai/OLMo-2-1124-7B-SFT)                         | [allenai/OLMo-2-1124-13B-SFT](https://huggingface.co/allenai/OLMo-2-1124-13B-SFT)                       | [allenai/OLMo-2-0325-32B-SFT](https://huggingface.co/allenai/OLMo-2-0325-32B-SFT)                        |
| **DPO**                | [allenai/OLMo-2-0425-1B-DPO](https://huggingface.co/allenai/OLMo-2-0425-1B-DPO)                        | [allenai/OLMo-2-1124-7B-DPO](https://huggingface.co/allenai/OLMo-2-1124-7B-DPO)                         | [allenai/OLMo-2-1124-13B-DPO](https://huggingface.co/allenai/OLMo-2-1124-13B-DPO)                       | [allenai/OLMo-2-0325-32B-DPO](https://huggingface.co/allenai/OLMo-2-0325-32B-DPO)                        |
| **Final Models (RLVR)**| [allenai/OLMo-2-0425-1B-Instruct](https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct)               | [allenai/OLMo-2-1124-7B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct)               | [allenai/OLMo-2-1124-13B-Instruct](https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct)             | [allenai/OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct)              |
| **Reward Model (RM)**  |                                                                                            | [allenai/OLMo-2-1124-7B-RM](https://huggingface.co/allenai/OLMo-2-1124-7B-RM)                                                                                               |(Same as 7B)                                                                        |                                                                                                  |

## Installation

OLMo 2 1B is supported in transformers v4.48 or higher:
```bash
pip install transformers>=4.48
```

If using vLLM, you will need to install from the main branch until v0.7.4 is released. Please

## Inference

You can use OLMo with the standard HuggingFace transformers library:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
olmo = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B")
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-2-0425-1B")
message = ["Language modeling is "]
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
# optional verifying cuda
# inputs = {k: v.to('cuda') for k,v in inputs.items()}
# olmo = olmo.to('cuda')
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])
>> 'Language modeling is  a key component of any text-based application, but its effectiveness...'
```

For faster performance, you can quantize the model using the following method:
```python
AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B",
    torch_dtype=torch.float16,
    load_in_8bit=True)  # Requires bitsandbytes
```
The quantized model is more sensitive to data types and CUDA operations. To avoid potential issues, it's recommended to pass the inputs directly to CUDA using:
```python
inputs.input_ids.to('cuda')
```

We have released checkpoints for these models. For pretraining, the naming convention is `stage1-stepXXX-tokensYYYB`. For checkpoints with ingredients of the soup, the naming convention is `stage2-ingredientN-stepXXX-tokensYYYB`


To load a specific model revision with HuggingFace, simply add the argument `revision`:
```bash
olmo = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0425-1B", revision="stage1-step140000-tokens294B")
```

Or, you can access all the revisions for the models via the following code snippet:
```python
from huggingface_hub import list_repo_refs
out = list_repo_refs("allenai/OLMo-2-0425-1B")
branches = [b.name for b in out.branches]
```

### Fine-tuning
Model fine-tuning can be done from the final checkpoint (the `main` revision of this model) or many intermediate checkpoints. Two recipes for tuning are available.
1. Fine-tune with the OLMo repository:
```bash
torchrun --nproc_per_node=8 scripts/train.py {path_to_train_config} \
    --data.paths=[{path_to_data}/input_ids.npy] \
    --data.label_mask_paths=[{path_to_data}/label_mask.npy] \
    --load_path={path_to_checkpoint} \
    --reset_trainer_state
```
For more documentation, see the [GitHub README](https://github.com/allenai/OLMo/).

2. Further fine-tuning support is being developing in AI2's Open Instruct repository. Details are [here](https://github.com/allenai/open-instruct).



### Model Description

- **Developed by:** Allen Institute for AI (Ai2)
- **Model type:** a Transformer style autoregressive language model.
- **Language(s) (NLP):** English
- **License:** The code and model are released under Apache 2.0.
- **Contact:** Technical inquiries: `olmo@allenai.org`. Press: `press@allenai.org`
- **Date cutoff:** Dec. 2023.


### Model Sources

- **Project Page:** https://allenai.org/olmo
- **Repositories:**
    - Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo
    - Evaluation code: https://github.com/allenai/OLMo-Eval
    - Further fine-tuning code: https://github.com/allenai/open-instruct
- **Paper:** https://arxiv.org/abs/2501.00656

## Evaluation
Core model results for OLMo 2 1B are found below.

| Instruct Model         | Avg  | FLOP×10²³ | AE2  | BBH  | DROP | GSM8K | IFE  | MATH | MMLU | Safety | PQA  | TQA  |
|------------------------|------|-----------|------|------|------|-------|------|------|------|--------|------|------|
| **Closed API models**  |      |           |      |      |      |       |      |      |      |        |      |      |
| GPT-3.5 Turbo 0125     | 60.5 | n/a       | 38.7 | 66.6 | 70.2 | 74.3  | 66.9 | 41.2 | 70.2 | 69.1   | 45.0 | 62.9 |
| GPT 4o Mini 0724       | 65.7 | n/a       | 49.7 | 65.9 | 36.3 | 83.0  | 83.5 | 67.9 | 82.2 | 84.9   | 39.0 | 64.8 |
| **Open weights models 1-1.7B Parameters** |      |           |      |      |      |       |      |      |      |        |      |      |
| SmolLM2 1.7B           | 34.2 | 1.1      | 5.8  | 39.8 | 30.9 | 45.3  | 51.6 | 20.3 | 34.3 | 52.4   | 16.4 | 45.3 |
| Gemma 3 1B             | 38.3 | 1.2      | 20.4 | 39.4 | 25.1 | 35.0  | 60.6 | 40.3 | 38.9 | 70.2   | 9.6  | 43.8 |
| Llama 3.1 1B           | 39.3 | 6.7      | 10.1 | 40.2 | 32.2 | 45.4  | 54.0 | 21.6 | 46.7 | 87.2   | 13.8 | 41.5 |
| Qwen 2.5 1.5B          | 41.7 | 1.7      | 7.4  | 45.8 | 13.4 | 66.2  | 44.2 | 40.6 | 59.7 | 77.6   | 15.5 | 46.5 |
| **Fully-open models**  |      |           |      |      |      |       |      |      |      |        |      |      |
| OLMo 1B 0724           | 24.4 |   0.22    | 2.4  | 29.9 | 27.9 | 10.8  | 25.3 | 2.2  | 36.6 | 52.0   | 12.1 | 44.3 |
| **OLMo 2 1B**              | 42.7 | 0.35      | 9.1  | 35.0 | 34.6 | 68.3  | 70.1 | 20.7 | 40.0 | 87.6   | 12.9 | 48.7 |


## Model Details

### Training
|  | **OLMo 2 1B** | **OLMo 2 7B** | **OLMo 2 13B** | **OLMo 2 32B** |
|-------------------|------------|------------|------------|------------|
| Pretraining Stage 1 | 4 trillion tokens<br>(1 epoch) | 4 trillion tokens<br>(1 epoch) | 5 trillion tokens<br>(1.2 epochs) | 6 trillion tokens<br>(1.5 epochs) |
| Pretraining Stage 2 | 50B tokens | 50B tokens (3 runs)<br>*merged* | 100B tokens (3 runs)<br>300B tokens (1 run)<br>*merged* | 100B tokens (3 runs)<br>300B tokens (1 run)<br>*merged* |
| Post-training | SFT+DPO+GRPO<br>([preference mix](https://huggingface.co/datasets/allenai/olmo-2-0425-1b-preference-mix)) | SFT + DPO + PPO<br>([preference mix](https://huggingface.co/datasets/allenai/olmo-2-1124-7b-preference-mix)) | SFT + DPO + PPO<br>([preference mix](https://huggingface.co/datasets/allenai/olmo-2-1124-13b-preference-mix)) | SFT + DPO + GRPO<br>([preference mix](https://huggingface.co/datasets/allenai/olmo-2-32b-pref-mix-v1)) |

#### Stage 1: Initial Pretraining
- Dataset: [OLMo-mix-1124](https://huggingface.co/datasets/allenai/olmo-mix-1124) (3.9T tokens)
- Coverage: 95%+ of total pretraining budget
- 1B Model: ~1 epoch

#### Stage 2: Mid-training
- Dataset: Dolmino-Mix-1124
- One training mix:
  - 50B tokens
- Mix composition: 50% high-quality web data + academic/Q&A/instruction/math content 

#### Model Merging
- 1B Model: only 1 version is trained on a 50B mix (ingredient 3), we did not merge. Ingredients 1 and 2 are just exploratory runs.


## Bias, Risks, and Limitations
Like any base or fine-tuned language model, AI can  be prompted by users to generate harmful and sensitive content. Such content may also be produced unintentionally, especially in cases involving bias, so we recommend that users consider the risks when applying this technology. Additionally, many statements from OLMo or any LLM are often inaccurate, so facts should be verified.


## Citation
```
@misc{olmo20242olmo2furious,
      title={{2 OLMo 2 Furious}},
      author={Team OLMo and Pete Walsh and Luca Soldaini and Dirk Groeneveld and Kyle Lo and Shane Arora and Akshita Bhagia and Yuling Gu and Shengyi Huang and Matt Jordan and Nathan Lambert and Dustin Schwenk and Oyvind Tafjord and Taira Anderson and David Atkinson and Faeze Brahman and Christopher Clark and Pradeep Dasigi and Nouha Dziri and Michal Guerquin and Hamish Ivison and Pang Wei Koh and Jiacheng Liu and Saumya Malik and William Merrill and Lester James V. Miranda and Jacob Morrison and Tyler Murray and Crystal Nam and Valentina Pyatkin and Aman Rangapur and Michael Schmitz and Sam Skjonsberg and David Wadden and Christopher Wilhelm and Michael Wilson and Luke Zettlemoyer and Ali Farhadi and Noah A. Smith and Hannaneh Hajishirzi},
      year={2024},
      eprint={2501.00656},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00656},
}
```

## Model Card Contact
For errors in this model card, contact `olmo@allenai.org`.