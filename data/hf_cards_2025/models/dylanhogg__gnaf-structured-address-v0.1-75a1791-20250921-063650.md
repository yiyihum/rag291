---
library_name: peft
license: other
base_model: meta-llama/Llama-3.2-1B-Instruct
tags:
- base_model:adapter:meta-llama/Llama-3.2-1B-Instruct
- llama-factory
- lora
- transformers
pipeline_tag: text-generation
model-index:
- name: llama3_lora
  results: []
---

# llama3_lora

This model is a fine-tuned version of [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) on the gnaf-2022-structured-training-100000-v0-instruct-train dataset.

## Model description

Extracts structured address information from text. Structured output is json with [G-NAF](https://docs.geoscape.com.au/projects/gnaf_desc/en/stable/overview.html) (Geocoded National Address File) fields.

Example:

Input text: `Lvl 15/333 George St Sydney NSW 2000`

Response: `{"level_type": "level", "level_number": "15", "street_name": "george", "street_type_code": "street", "locality_name": "sydney", "state_abbreviation": "nsw", "postcode": "2000"}`

Note that this model is a work in progresss as of Oct 2025.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- PEFT 0.17.1
- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0