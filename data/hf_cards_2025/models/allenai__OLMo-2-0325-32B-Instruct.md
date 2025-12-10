---
license: apache-2.0
language:
- en
datasets:
- allenai/RLVR-GSM-MATH-IF-Mixed-Constraints
base_model:
- allenai/OLMo-2-0325-32B-DPO
pipeline_tag: text-generation
library_name: transformers
---

<img alt="OLMo Logo" src="https://huggingface.co/datasets/allenai/blog-images/resolve/main/olmo2/olmo.png" width="242px">

OLMo 2 32B Instruct March 2025 is post-trained variant of the [OLMo-2 32B March 2025](https://huggingface.co/allenai/OLMo-2-0325-32B/) model, which has undergone supervised finetuning on an OLMo-specific variant of the [Tülu 3 dataset](https://huggingface.co/datasets/allenai/tulu-3-sft-olmo-2-mixture), further DPO training on [this dataset](https://huggingface.co/datasets/allenai/olmo-2-0325-32b-preference-mix), and final RLVR training on [this dataset](https://huggingface.co/datasets/allenai/RLVR-GSM-MATH-IF-Mixed-Constraints).
Tülu 3 is designed for state-of-the-art performance on a diversity of tasks in addition to chat, such as MATH, GSM8K, and IFEval.
Check out the [OLMo 2 paper](https://arxiv.org/abs/2501.00656) or [Tülu 3 paper](https://arxiv.org/abs/2411.15124) for more details!

OLMo is a series of **O**pen **L**anguage **Mo**dels designed to enable the science of language models. 
These models are trained on the Dolma dataset. We are releasing all code, checkpoints, logs, and associated training details. 


## Model description

- **Model type:** A model trained on a mix of publicly available, synthetic and human-created datasets.
- **Language(s) (NLP):** Primarily English
- **License:** Apache 2.0
- **Finetuned from model:** allenai/OLMo-2-0325-32B-DPO

### Model Sources

- **Project Page:** https://allenai.org/olmo
- **Repositories:** 
    - Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo-core
    - Evaluation code: https://github.com/allenai/olmes
    - Further fine-tuning code: https://github.com/allenai/open-instruct
- **Paper:** https://arxiv.org/abs/2501.00656
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

olmo_model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0325-32B-Instruct")
```

### Chat template

*NOTE: This is different than previous OLMo 2 and Tülu 3 models due to a minor change in configuration. It does NOT have the bos token before the rest. Our other models have <|endoftext|> at the beginning of the chat template.*

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
You are OLMo 2, a helpful and harmless AI Assistant built by the Allen Institute for AI.
```
The model has not been trained with a specific system prompt in mind.

### Intermediate Checkpoints

To facilitate research on RL finetuning, we have released our intermediate checkpoints during the model's RLVR training.
The model weights are saved every 20 training steps, and can be accessible in the revisions of the HuggingFace repository.
For example, you can load with:
```
olmo_model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-2-0325-32B-Instruct", revision="step_200")
```

### Bias, Risks, and Limitations

The OLMo-2 models have limited safety training, but are not deployed automatically with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
See the Falcon 180B model card for an example of this.


## Performance

| Model | Average | AlpacaEval 2 LC | BBH | DROP | GSM8k | IFEval | MATH | MMLU | Safety | PopQA | TruthQA |
|-------|---------|------|-----|------|-------|--------|------|------|--------|-------|---------|
| **Closed API models** |  |  |  |  |  |  |  |  |  |  |  |
| GPT-3.5 Turbo 0125 | 59.6 | 38.7 | 66.6 | 70.2 | 74.3 | 66.9 | 41.2 | 70.2 | 69.1 | 45.0 | 62.9 |
| GPT 4o Mini 2024-07-18 | 65.7 | 49.7 | 65.9 | 36.3 | 83.0 | 83.5 | 67.9 | 82.2 | 84.9 | 39.0 | 64.8 |
| **Open weights models** |  |  |  |  |  |  |  |  |  |  |  |
| Mistral-Nemo-Instruct-2407 | 50.9 | 45.8 | 54.6 | 23.6 | 81.4 | 64.5 | 31.9 | 70.0 | 52.7 | 26.9 | 57.7 |
| Ministral-8B-Instruct | 52.1 | 31.4 | 56.2 | 56.2 | 80.0 | 56.4 | 40.0 | 68.5 | 56.2 | 20.2 | 55.5 |
| Gemma-2-27b-it | 61.3 | 49.0 | 72.7 | 67.5 | 80.7 | 63.2 | 35.1 | 70.7 | 75.9 | 33.9 | 64.6 |
| Qwen2.5-32B | 66.5 | 39.1 | 82.3 | 48.3 | 87.5 | 82.4 | 77.9 | 84.7 | 82.4 | 26.1 | 70.6 |
| Mistral-Small-24B | 67.6 | 43.2 | 80.1 | 78.5 | 87.2 | 77.3 | 65.9 | 83.7 | 66.5 | 24.4 | 68.1 |
| Llama-3.1-70B | 70.0 | 32.9 | 83.0 | 77.0 | 94.5 | 88.0 | 56.2 | 85.2 | 76.4 | 46.5 | 66.8 |
| Llama-3.3-70B | 73.0 | 36.5 | 85.8 | 78.0 | 93.6 | 90.8 | 71.8 | 85.9 | 70.4 | 48.2 | 66.1 |
| Gemma-3-27b-it | - | 63.4 | 83.7 | 69.2 | 91.1 | - | - | 81.8 | - | 30.9 | - |
| **Fully open models** |  |  |  |  |  |  |  |  |  |  |  |
| OLMo-2-7B-1124-Instruct | 55.7 | 31.0 | 48.5 | 58.9 | 85.2 | 75.6 | 31.3 | 63.9 | 81.2 | 24.6 | 56.3 |
| OLMo-2-13B-1124-Instruct | 61.4 | 37.5 | 58.4 | 72.1 | 87.4 | 80.4 | 39.7 | 68.6 | 77.5 | 28.8 | 63.9 |
| **OLMo-2-32B-0325-SFT** | 61.7 | 16.9 | 69.7 | 77.2 | 78.4 | 72.4 | 35.9 | 76.1 | 93.8 | 35.4 | 61.3 |
| **OLMo-2-32B-0325-DPO** | 68.8 | 44.1 | 70.2 | 77.5 | 85.7 | 83.8 | 46.8 | 78.0 | 91.9 | 36.4 | 73.5 |
| **OLMo-2-32B-0325-Instruct** | 68.8 | 42.8 | 70.6 | 78.0 | 87.6 | 85.6 | 49.7 | 77.3 | 85.9 | 37.5 | 73.2 |




## Learning curves

Below is the training curves for `allenai/OLMo-2-0325-32B-Instruct`. The model was trained using 5 8xH100 nodes.

![](olmo-32b-instruct-learning-curve.png)

![](olmo-32b-instruct-learning-curve-time.png)

Below are the core eval scores over steps for `allenai/OLMo-2-0325-32B-Instruct` (note we took step `320` as the final checkpoint, corresponding to episode `573,440`):

![](olmo-32b-instruct-eval-curve.png)

Below are the other eval scores over steps for `allenai/OLMo-2-0325-32B-Instruct`:

![](olmo-32b-instruct-full-eval-curve.png)


## Reproduction command

The command below is copied directly from the tracked training job:

```bash
# clone and check out commit
git clone https://github.com/allenai/open-instruct.git
# this should be the correct commit, the main thing is to have the vllm monkey patch for
# 32b olmo https://github.com/allenai/open-instruct/blob/894ffa236319bc6c26c346240a7e4ee04ba0bd31/open_instruct/vllm_utils2.py#L37-L59
git checkout a51dc98525eec01de6e8a24c071f42dce407d738
uv sync
uv sync --extra compile

# note that you may need 5 8xH100 nodes for the training.
# so please setup ray properly, e.g., https://github.com/allenai/open-instruct/blob/main/docs/tulu3.md#llama-31-tulu-3-70b-reproduction
python open_instruct/grpo_vllm_thread_ray_gtrl.py \
    --exp_name 0310_olmo2_32b_grpo_12818 \
    --beta 0.01 \
    --local_mini_batch_size 32 \
    --number_samples_per_prompt 16 \
    --output_dir output \
    --local_rollout_batch_size 4 \
    --kl_estimator kl3 \
    --learning_rate 5e-7 \
    --dataset_mixer_list allenai/RLVR-GSM-MATH-IF-Mixed-Constraints 1.0 \
    --dataset_mixer_list_splits train \
    --dataset_mixer_eval_list allenai/RLVR-GSM-MATH-IF-Mixed-Constraints 16 \
    --dataset_mixer_eval_list_splits train \
    --max_token_length 2048 \
    --max_prompt_token_length 2048 \
    --response_length 2048 \
    --model_name_or_path allenai/OLMo-2-0325-32B-DPO \
    --non_stop_penalty \
    --stop_token eos \
    --temperature 1.0 \
    --ground_truths_key ground_truth \
    --chat_template_name tulu \
    --sft_messages_key messages \
    --eval_max_length 4096 \
    --total_episodes 10000000 \
    --penalty_reward_value 0.0 \
    --deepspeed_stage 3 \
    --no_gather_whole_model \
    --per_device_train_batch_size 2 \
    --local_rollout_forward_batch_size 2 \
    --actor_num_gpus_per_node 8 8 8 4 \
    --num_epochs 1 \
    --vllm_tensor_parallel_size 1 \
    --vllm_num_engines 12 \
    --lr_scheduler_type constant \
    --apply_verifiable_reward true \
    --seed 1 \
    --num_evals 30 \
    --save_freq 20 \
    --reward_model_multiplier 0.0 \
    --no_try_launch_beaker_eval_jobs \
    --try_launch_beaker_eval_jobs_on_weka \
    --gradient_checkpointing \
    --with_tracking
```


## License and use

OLMo 2 is licensed under the Apache 2.0 license.
OLMo 2 is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).
This model has been fine-tuned using a dataset mix with outputs generated from third party models and are subject to additional terms: [Gemma Terms of Use](https://ai.google.dev/gemma/terms).

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