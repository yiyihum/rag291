---
license: cc-by-nc-4.0
task_categories:
- text-generation
language:
- en
tags:
- Reasoning
- Vision-Language
- Data
- LLama4
size_categories:
- 1M<n<10M
---

# HoneyBee: Data Recipes for Vision-Language Reasoners

This is the official data release for the paper: https://arxiv.org/abs/2510.12225.

Github Repo: https://github.com/facebookresearch/HoneyBee_VLM.

## Abstract

Recent advances in vision-language models (VLMs) have made them highly effective at reasoning tasks. However, the principles underlying the construction of performant VL reasoning training datasets remain poorly understood. In this work, we introduce several data curation approaches and study their impacts on VL reasoning capabilities by carefully controlling training and evaluation setups. We analyze the effects of context (image and question pair) sources, implement targeted data interventions, and explore scaling up images, questions, and chain-of-thought (CoT) solutions. Our findings reveal that (a) context source strategies significantly affect VLM performance, (b) interventions such as auxiliary signals from image captions and the inclusion of text-only reasoning yield substantial gains, and (c) scaling all data dimensions (e.g., unique questions per image and unique CoTs per image-question pair) consistently improves reasoning capability. Motivated by these insights, we introduce HoneyBee, a large-scale, high-quality CoT reasoning dataset with 2.5M examples consisting 350K image-question pairs. VLMs trained with HoneyBee outperform state-of-the-art models across model sizes. For instance, a HoneyBee-trained VLM with 3B parameters outperforms the SOTA model and the base model by 7.8% and 24.8%, respectively, on MathVerse. Furthermore, we propose a test-time scaling strategy that reduces decoding cost by 73% without sacrificing accuracy. Overall, this work presents improved strategies for VL reasoning dataset curation research.

![image](https://cdn-uploads.huggingface.co/production/uploads/61c5c25705aa54027c52f7b3/pz-sjA_aCUBx9i0hryLky.png)

The data is composed of three components:

1. Questions from OpenThought3, and chain-of-thoughts from Llama-4 Scout (`q_source='OpenThoughts3'`). We do not re-distribute questions from OT3.
2. Images and Questions from ViRL, and chain-of-thoughts from Llama-4 Scout (`q_source='ViRL'`). We do not re-distribute images and questions from ViRL.
3. Images from ViRL, and new questions and chain-of-thoughts from Llama-4 Scout (`q_source='Ours'`). We do not re-distribute images from ViRL.

## Pointers

1. Use this link to download the images from the ViRL dataset: https://huggingface.co/datasets/TIGER-Lab/ViRL39K/blob/main/images.zip
2. Use this script to merge our data release with original questions from the OT3 and ViRL dataset: https://huggingface.co/datasets/facebook/HoneyBee/blob/main/full_data.py

## Data Explanation

```
q_source: question source
q_id: unique id that will help in populating the questions from original source
image_path: image path from the ViRL data release
question: original question from OT3, ViRL, or Llama-4 Scout generated question
cot: Llama-4 Scout generated chain-of-thought (CoT). As per our insights in the paper, the cot consists of image caption (within <caption> and </caption> tags) from Llama-4 followed by solution to the question. The final answer is enclosed within \\boxed{}.
```

## Results of Training with HoneyBee

![image](https://cdn-uploads.huggingface.co/production/uploads/61c5c25705aa54027c52f7b3/BsDvu3FHvoIksQWYoZxtQ.png)

## License Information
The Data is released CC-by-NC. The data are outputs of Llama 4, and subject to the Llama 4 license (https://github.com/meta-llama/llama-models/tree/main/models/llama4). If you use of this portion of the data to create, train, fine tune, or otherwise improve an AI model, which is distributed or made available, you shall also include “Llama” at the beginning of any such AI model name. Third party content pulled from other locations are subject to its own licenses and you may have other legal obligations or restrictions that govern your use of that content