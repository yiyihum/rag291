---
library_name: transformers
license: other
base_model: meta-llama/Llama-3.2-3B-Instruct
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: helpsteer3_llama32_3b_dpo_nemotron_en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# helpsteer3_llama32_3b_dpo_nemotron_en

This model is a fine-tuned version of [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) on the dpo_helpsteer3_llama32_3b_nemotron_en dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.52.4
- Pytorch 2.6.0
- Datasets 3.6.0
- Tokenizers 0.21.1
