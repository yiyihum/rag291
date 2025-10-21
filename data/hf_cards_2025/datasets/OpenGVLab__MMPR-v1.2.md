---
language:
- en
license: mit
size_categories:
- 1M<n<10M
task_categories:
- image-text-to-text
tags:
- multimodal
- reasoning
- preference-data
- vision-language
- rlhf
- agents
pretty_name: MMPR-v1.2
dataset_info:
  features:
  - name: image
    dtype: string
  - name: question
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
configs:
- config_name: default
  data_files:
  - split: train
    path: annotations.zip
---

# MMPR-v1.2

[\[📂 GitHub\]](https://github.com/OpenGVLab/InternVL) | [\[🌐 Project Page\]](https://chat.intern-ai.org.cn/) | [\[📜 Paper (InternVL3.5)\]](https://huggingface.co/papers/2508.18265) | [\[📜 Paper (MMPR/MPO)\]](https://arxiv.org/abs/2411.10442) | [\[🆕 Blog (MPO)\]](https://internvl.github.io/blog/2024-11-14-InternVL-2.0-MPO/) | [\[📖 Documents\]](https://internvl.readthedocs.io/en/latest/internvl2.0/preference_optimization.html)

***This is a newer version of [MMPR](https://huggingface.co/datasets/OpenGVLab/MMPR) and [MMPR-v1.1](https://huggingface.co/datasets/OpenGVLab/MMPR-v1.1), which includes additional data sources to enhance the data diversity and greatly improves the overall performance of [InternVL3.5](https://huggingface.co/papers/2508.18265) across all scales. The prompts used to build this dataset is released in [MMPR-v1.2-prompts](https://huggingface.co/datasets/OpenGVLab/MMPR-v1.2-prompts).***

To unzip the archive of images, please first run `cat images.zip_* > images.zip` and then run `unzip images.zip`.

![image/png](ablation-mpo.png)

## Introduction
MMPR is a large-scale and high-quality multimodal reasoning preference dataset. This dataset includes about 3 million samples. It is notably used as training data for advanced multimodal large language models like **InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency** ([https://huggingface.co/papers/2508.18265](https://huggingface.co/papers/2508.18265)).

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/619507e7b74b6c591f794340/mmXL47UPDFwYOWdn9Z6j5.jpeg)
![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/619507e7b74b6c591f794340/6fnvI_wCd9JXAs6vYthaG.jpeg)

We finetune InternVL2-8B with [MPO](https://internvl.github.io/blog/2024-11-14-InternVL-2.0-MPO/#Mix-Preference-Optimization) using this dataset.
The resulting model, [InternVL2-8B-MPO](https://huggingface.co/OpenGVLab/InternVL2-8B-MPO), achieves superior performance across 8 benchmarks, particularly excelling in multimodal reasoning tasks.
**On the MathVista benchmark, our model achieves an accuracy of 67.0%**, outperforming InternVL2-8B by 8.7 points and achieving performance comparable to the \\(10\times\\) larger InternVL2-76B.
**On the MathVision benchmark, our model achieves an accuracy of 25.7%**, establishing a new state-of-the-art performance among open-source models.
These results demonstrate the effectiveness of our preference optimization approach in enhancing multimodal reasoning capabilities.
Additionally, on the POPE benchmark, our model exhibits a 1.2-point improvement over InterVL2-8B, demonstrating the effectiveness of the perception data contained in our MMPR dataset to mitigate hallucinations.
Furthermore, our model also shows superior performance compared to the InternVL2-8B on complex VQA benchmarks, indicating that the general abilities of our model are also improved, benefiting from enhanced reasoning abilities and mitigated hallucinations.
Please refer to our [paper](https://internvl.github.io/blog/2024-11-14-InternVL-2.0-MPO/) for more details.
| Model Name | M3CoT | MathVista | MathVision MINI | MMVet (GPT4-Turbo) | LLaVA-Bench | POPE | CRPE | MMHalBench |
| :---------------------- | :---: | :-------: | :-------------: | :----------------: | :---------: | :---: | :---: | :--------: |
| Gemini-1.5-Pro | - | 63.9 | 19.2 | - | - | - | - | - |
| GPT-4o | 64.3 | 63.8 | 30.4 | 69.1 | 97.6 | 86.9 | 76.6 | 4.0 |
| GPT-4o-Mini | 61.9 | 52.4 | 27.3 | 66.9 | 95.4 | 85.1 | 73.1 | 3.6 |
| LLaVA-1.5-13B | 39.5 | 27.6 | 11.1 | 36.3 | 70.7 | 85.9 | 55.6 | 2.4 |
| Qwen2-VL-7B | 57.8 | 58.2 | 21.1 | 60.6 | 67.7 | 88.1 | 74.4 | 3.4 |
| MiniCPM-V-2-6-8B | 56.0 | 60.6 | 23.4 | 57.4 | 83.4 | 87.3 | 75.2 | 3.6 |
| LLaVA-OneVision-7B | 52.3 | 63.2 | 18.4 | 51.4 | 79.9 | 88.4 | 73.7 | 3.1 |
| InternVL2-26B | 58.2 | 59.4 | 23.4 | 62.1 | 92.3 | 88.0 | 75.6 | 3.7 |
| InternVL2-40B | 63.6 | 63.7 | 21.4 | 65.5 | 100.5 | 88.4 | 77.3 | 3.9 |
| InternVL2-76B | 65.4 | 67.5 | 23.7 | 65.7 | 99.3 | 89.0 | 77.8 | 3.8 |
| InternVL2-Pro | 65.6 | 66.3 | 18.8 | 69.4 | 99.5 | 88.2 | 77.6 | 3.7 |
| InternVL2-8B | 59.3 | 58.3 | 20.4 | 54.2 | 73.2 | 86.9 | 75.0 | 3.3 |
| InternVL2-8B-MPO (ours) | 79.2 | 67.0 | 25.7 | 56.2 | 76.7 | 88.1 | 75.4 | 3.5 |

Additionally, we finetune InternVL2.5 series with MPO using this dataset. The resulting models outperform their counterparts without MPO by an average of 2 points across all scales on the OpenCompass leaderboard.

| Model | Avg. | MMBench v1.1 | MMStar | MMMU | MathVista | HallusionBench | AI2D | OCRBench | MMVet |
| :------------------ | :--- | :----------- | :----- | :--- | :-------- | :------------- | :--- | :------- | :---- |
| InternVL2-5-1B | 54.9 | 66.5 | 51.3 | 41.2 | 47.1 | 39.4 | 69.0 | 77.4 | 47.2 |
| InternVL2-5-1B-MPO | 56.4 | 67.2 | 49.7 | 40.8 | 53.0 | 40.0 | 69.4 | 83.6 | 47.2 |
| InternVL2-5-2B | 59.9 | 70.9 | 54.3 | 43.2 | 51.1 | 42.3 | 74.9 | 80.2 | 62.6 |
| InternVL2-5-2B-MPO | 62.0 | 71.6 | 55.0 | 45.0 | 56.4 | 43.0 | 75.3 | 84.2 | 65.4 |
| InternVL2-5-4B | 65.1 | 78.2 | 58.7 | 51.8 | 60.8 | 46.6 | 81.4 | 82.0 | 61.5 |
| InternVL2-5-4B-MPO | 67.6 | 78.6 | 60.2 | 51.6 | 65.3 | 47.8 | 82.0 | 88.0 | 67.1 |
| InternVL2-5-8B | 68.9 | 82.5 | 63.2 | 56.2 | 64.5 | 49.0 | 84.6 | 82.1 | 62.8 |
| InternVL2-5-8B-MPO | 70.4 | 82.4 | 65.7 | 54.9 | 68.9 | 51.4 | 84.5 | 88.3 | 66.9 |
| InternVL2-5-26B | 71.6 | 84.6 | 66.5 | 60.7 | 68.0 | 55.8 | 86.2 | 85.4 | 65.4 |
| InternVL2-5-26B-MPO | 72.7 | 84.2 | 67.2 | 57.7 | 72.8 | 55.3 | 86.2 | 91.2 | 67.1 |
| InternVL2-5-38B | 73.5 | 85.4 | 68.5 | 64.6 | 72.4 | 57.9 | 87.6 | 84.1 | 67.2 |
| InternVL2-5-38B-MPO | 75.5 | 85.6 | 69.8 | 64.1 | 73.8 | 61.5 | 88.1 | 88.5 | 72.5 |
| InternVL2-5-78B | 75.2 | 87.5 | 69.5 | 70.0 | 70.6 | 57.4 | 89.1 | 85.3 | 71.8 |
| InternVL2-5-78B-MPO | 76.6 | 87.3 | 73.1 | 68.3 | 73.8 | 58.7 | 89.3 | 91.2 | 71.4 |

## Usage
Please refer to [our document](https://internvl.readthedocs.io/en/latest/internvl2.0/preference_optimization.html) for detailed usage and advanced features. This dataset is designed for training multimodal large language models through preference optimization techniques.

### Sample Usage: Multimodal Chat with InternVL 2.5

The following Python code snippet, adapted from the [InternVL GitHub repository](https://github.com/OpenGVLab/InternVL), demonstrates how to perform a single-image, single-round conversation with an InternVL 2.5 model (e.g., `OpenGVLab/InternVL2_5-8B`), which can be fine-tuned using data like MMPR-v1.2.

```python
import numpy as np
import torch
import torchvision.transforms as T
from PIL import Image
from torchvision.transforms.functional import InterpolationMode
from transformers import AutoModel, AutoTokenizer
import os # Added for creating dummy image if needed

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)

def build_transform(input_size):
    MEAN, STD = IMAGENET_MEAN, IMAGENET_STD
    transform = T.Compose([
        T.Lambda(lambda img: img.convert('RGB') if img.mode != 'RGB' else img),
        T.Resize((input_size, input_size), interpolation=InterpolationMode.BICUBIC),
        T.ToTensor(),
        T.Normalize(mean=MEAN, std=STD)
    ])
    return transform

def find_closest_aspect_ratio(aspect_ratio, target_ratios, width, height, image_size):
    best_ratio_diff = float('inf')
    best_ratio = (1, 1)
    area = width * height
    for ratio in target_ratios:
        target_aspect_ratio = ratio[0] / ratio[1]
        ratio_diff = abs(aspect_ratio - target_aspect_ratio)
        if ratio_diff < best_ratio_diff:
            best_ratio_diff = ratio_diff
            best_ratio = ratio
        elif ratio_diff == best_ratio_diff:
            if area > 0.5 * image_size * image_size * ratio[0] * ratio[1]:
                best_ratio = ratio
    return best_ratio

def dynamic_preprocess(image, min_num=1, max_num=12, image_size=448, use_thumbnail=False):
    orig_width, orig_height = image.size
    aspect_ratio = orig_width / orig_height

    # calculate the existing image aspect ratio
    target_ratios = set(
        (i, j) for n in range(min_num, max_num + 1) for i in range(1, n + 1) for j in range(1, n + 1) if
        i * j <= max_num and i * j >= min_num)
    target_ratios = sorted(target_ratios, key=lambda x: x[0] * x[1])

    # find the closest aspect ratio to the target
    target_aspect_ratio = find_closest_aspect_ratio(
        aspect_ratio, target_ratios, orig_width, orig_height, image_size)

    # calculate the target width and height
    target_width = image_size * target_aspect_ratio[0]
    target_height = image_size * target_aspect_ratio[1]
    blocks = target_aspect_ratio[0] * target_aspect_ratio[1]

    # resize the image
    resized_img = image.resize((target_width, target_height))
    processed_images = []
    for i in range(blocks):
        box = (
            (i % (target_width // image_size)) * image_size,
            (i // (target_width // image_size)) * image_size,
            ((i % (target_width // image_size)) + 1) * image_size,
            ((i // (target_width // image_size)) + 1) * image_size
        )
        # split the image
        split_img = resized_img.crop(box)
        processed_images.append(split_img)
    assert len(processed_images) == blocks
    if use_thumbnail and len(processed_images) != 1:
        thumbnail_img = image.resize((image_size, image_size))
        processed_images.append(thumbnail_img)
    return processed_images

def load_image(image_file, input_size=448, max_num=12):
    image = Image.open(image_file).convert('RGB')
    transform = build_transform(input_size=input_size)
    images = dynamic_preprocess(image, image_size=input_size, use_thumbnail=True, max_num=max_num)
    pixel_values = [transform(image) for image in images]
    pixel_values = torch.stack(pixel_values)
    return pixel_values

# If you have an 80G A100 GPU, you can put the entire model on a single GPU.
# Otherwise, you need to load a model using multiple GPUs, please refer to the `Multiple GPUs` section in InternVL docs.
path = 'OpenGVLab/InternVL2_5-8B' # Example model trained with MMPR-v1.2
model = AutoModel.from_pretrained(
    path,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True).eval().cuda()
tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False)

# Prepare an example image for demonstration
dummy_image_path = 'dummy_image.jpg'
if not os.path.exists(dummy_image_path):
    dummy_image = Image.new('RGB', (512, 512), color = 'red')
    dummy_image.save(dummy_image_path)
image_to_load = dummy_image_path

pixel_values = load_image(image_to_load, max_num=12).to(torch.bfloat16).cuda()
generation_config = dict(max_new_tokens=1024, do_sample=False)

# single-image single-round conversation
question = '<image>
Please describe the image shortly.'
response = model.chat(tokenizer, pixel_values, question, generation_config)
print(f'User: {question}
Assistant: {response}')

# For multi-image, video conversations, and batch inference,
# please refer to the comprehensive examples in the [InternVL GitHub repository](https://github.com/OpenGVLab/InternVL)
# under the "Quick Start with HuggingFace" section.
```

## Data fields
| Key | Description |
| :--------- | :----------------------------------- |
| `image` | Image path. |
| `question` | Input query. |
| `chosen` | Chosen response for the question. |
| `rejected` | Rejected response for the question. |

## Citation
If you find this project useful in your research, please consider citing:

```BibTeX
@article{wang2024mpo,
  title={Enhancing the Reasoning Ability of Multimodal Large Language Models via Mixed Preference Optimization},
  author={Wang, Weiyun and Chen, Zhe and Wang, Wenhai and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Zhu, Jinguo and Zhu, Xizhou and Lu, Lewei and Qiao, Yu and Dai, Jifeng},
  journal={arXiv preprint arXiv:2411.10442},
  year={2024}
}
```

## License

This project is released under the [MIT license](LICENSE). Parts of this project contain code and models from other sources, which are subject to their respective licenses.
