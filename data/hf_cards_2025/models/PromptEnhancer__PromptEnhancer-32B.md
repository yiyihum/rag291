---
license: other
license_name: apache-2.0
license_link: https://huggingface.co/PromptEnhancer/PromptEnhancer-32B/blob/main/License.txt
language:
- zh
- en
tags:
- text-to-image
- prompt-enhancement
- prompt-rewriting
- chain-of-thought
pipeline_tag: text-generation
library_name: transformers
base_model: Qwen/Qwen2.5-VL-32B-Instruct
---

# PromptEnhancerV2 (32B)

PromptEnhancerV2 is a multimodal language model fine-tuned for text-to-image prompt enhancement and rewriting. It restructures user input prompts while preserving the original intent, producing clearer, layered, and logically consistent prompts suitable for downstream image generation tasks.

## Model Details

### Model Description

PromptEnhancerV2 is a specialized text-to-image prompt rewriting model that employs chain-of-thought reasoning to enhance user prompts. 

- **Model type:** Vision-Language Model for Prompt Enhancement
- **Language(s) (NLP):** Chinese (zh), English (en)
- **License:** Apache-2.0
- **Finetuned from model:** Qwen/Qwen2.5-VL-32B-Instruct

### Model Sources

- **Repository:** https://github.com/ximinng/PromptEnhancer
- **Paper:** https://arxiv.org/abs/2509.04545
- **Homepage:** https://hunyuan-promptenhancer.github.io/

## How to Get Started with the Model

- **1. Clone the repository:**:

```bash
git clone https://github.com/ximinng/PromptEnhancer.git
cd PromptEnhancer
pip install -r requirements.txt
```

- **2. Model Download:**

```bash
huggingface-cli download PromptEnhancer/PromptEnhancer-32B --local-dir ./models/promptenhancer-32b
```

- **3. Use the model:**

```python
from inference.prompt_enhancer_v2 import PromptEnhancerV2

# Initialize the model
models_root_path = "./models/promptenhancer-32b"
enhancer = PromptEnhancerV2(models_root_path=models_root_path, device_map="auto")

# Enhance a prompt (Chinese or English)
user_prompt = "韩系插画风女生头像，粉紫色短发+透明感腮红，侧光渲染。"
enhanced_prompt = enhancer.predict(
    prompt_cot=user_prompt,
    device="cuda"
)

print("Enhanced:", enhanced_prompt)
```

## Evaluation

The model is evaluated on the [T2I-Keypoints-Eval dataset](https://huggingface.co/datasets/PromptEnhancer/T2I-Keypoints-Eval), which contains diverse text-to-image prompts across various categories and languages.

## Citation

If you find this model useful, please consider citing:

**BibTeX:**
```bibtex
@article{promptenhancer,
  title={PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting},
  author={Wang, Linqing and Xing, Ximing and Cheng, Yiji and Zhao, Zhiyuan and Donghao, Li and Tiankai, Hang and Zhenxi, Li and Tao, Jiale and Wang, QiXun and Li, Ruihuang and Chen, Comi and Li, Xin and Wu, Mingrui and Deng, Xinchi and Gu, Shuyang and Wang, Chunyu and Lu, Qinglin},
  journal={arXiv preprint arXiv:2509.04545},
  year={2025}
}
```
