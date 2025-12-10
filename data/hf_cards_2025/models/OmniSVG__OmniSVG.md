---
license: apache-2.0
datasets:
- OmniSVG/MMSVG-Icon
- OmniSVG/MMSVG-Illustration
language:
- en
- zh
base_model:
- Qwen/Qwen2.5-VL-3B-Instruct
pipeline_tag: text-generation
tags:
- SVG
- Image-to-SVG
- Text-to-SVG
---
<!-- <div align= "center">
    <h1> Official repo for OmniSVG</h1>

</div> -->

<h3 align="center"><strong>OmniSVG: A Unified Scalable Vector Graphics Generation Model</strong></h3>


<div align="center">
<a href='https://arxiv.org/abs/2504.06263'><img src='https://img.shields.io/badge/arXiv-2504.06263-b31b1b.svg'></a> &nbsp;&nbsp;&nbsp;&nbsp;
 <a href='https://omnisvg.github.io/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://huggingface.co/OmniSVG/OmniSVG"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Weights-HF-orange"></a> &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://huggingface.co/OmniSVG"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Dataset%20-HF-orange"></a>
</div>

<p align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/67f4fc326576467f43cc20bf/xcG4VDF8tpjmBhH_PeMwl.gif" alt="Demo GIF" width="720px" />
</p>



## 1. Introduction

**OmniSVG** is the first family of end-to-end multimodal SVG generators that leverage pre-trained Vision-Language Models (VLMs), capable of generating complex and detailed SVGs, from simple icons to intricate anime characters. We also introduce MMSVG-2M, a multimodal dataset with two million richly annotated SVG assets, along with a standardized evaluation protocol for conditional SVG generation tasks. 


## 2. Models Downloading
| Model                       | Download link                   | Size       | Update date |                                                                                     
|-----------------------------|-------------------------------|------------|------|
| OmniSVG-3B| 🤗 [Huggingface](https://huggingface.co/OmniSVG/OmniSVG)    | 8.49 GB | 2025-07-21  | 



##  3. Dependencies and Installation
The dependencies configured according to the following instructions provide an environment equipped for inference

### 3.1 Clone the Repository
```bash
git clone https://github.com/OmniSVG/OmniSVG.git
cd OmniSVG
```

### 3.2 Create Conda Environment
Create and activate a new conda environment with Python 3.10:
```bash
conda create -n omnisvg python=3.10
conda activate omnisvg
```

### 3.3 Install Dependencies

#### System Dependencies
Before installing Python packages, you need to install Cairo library which is required by `CairoSVG` in our dependencies:

**macOS:**
```bash
brew install cairo
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install libcairo2 libcairo2-dev
```

> **Note:** Installing Cairo system library beforehand helps prevent potential build errors when installing `CairoSVG` via pip.

#### Python Dependencies
We have tested our environment with CUDA 12.1. You can install CUDA 12.1 by following the [CUDA Toolkit installation guide](https://developer.nvidia.com/cuda-12-1-0-download-archive).

Install PyTorch with CUDA 12.1 support:
```bash
pip install torch==2.3.0+cu121 torchvision==0.18.0+cu121 --index-url https://download.pytorch.org/whl/cu121
```

Install remaining dependencies:
```bash
pip install -r requirements.txt
```

## 4. Inference Script

|                                                  | GPU Memory Usage | Time per 256/512/1024/2048/4096 tokens |
| ------------------------------------------------ | ---------------- | ----------------- |
| OmniSVG-3B     | 17G              | 4.08/8.68/18.07/37.51/82.70 seconds       |

<font color="red">**Note: The inference time shown here is measured per OmniSVG SVG tokens, while the inference time reported in our paper is measured per XML code tokens for fair comparison with baseline methods.**</font> 

### Quick Start

1. **Download Model Weights**
   
   Download the model weights from [Hugging Face](https://huggingface.co/OmniSVG) and place them in the `./pretrained_models/OmniSVG-3B` directory.

2. **Run Inference**
   
   Execute the following command to run inference on your images:
   ```bash
   python inference.py --input_dir ./examples --output_dir ./output --task_type image-to-svg/text-to-svg --weight_path ./pretrained_models/OmniSVG-3B
   ```

### Interactive Demo

We provide an interactive generation interface using Gradio:

- **Local Deployment**
  ```bash
  python app.py
  ```

- **Online Demo**
  
  Try our live demo on [Hugging Face Spaces](https://huggingface.co/spaces/OmniSVG/OmniSVG)


## 5. License
OmniSVG is licensed under the [**Apache License 2.0**](https://www.apache.org/licenses/LICENSE-2.0), while MMSVG dataset is under [**Creative Commons Attribution Non Commercial Share Alike 4.0 License**](https://spdx.org/licenses/CC-BY-NC-SA-4.0). You can find the license files in the respective github and HuggingFace repositories.


<!-- ##  🧩 Dataset - MMSVG-2M -->

## Citation

```bibtex
@article{yang2025omnisvg,
  title={OmniSVG: A Unified Scalable Vector Graphics Generation Model}, 
  author={Yiying Yang and Wei Cheng and Sijin Chen and Xianfang Zeng and Jiaxu Zhang and Liao Wang and Gang Yu and Xinjun Ma and Yu-Gang Jiang},
  journal={arXiv preprint arxiv:2504.06263},
  year={2025}
}
```

## Acknowledgments
We thank the following excellent open-source works:

**IconShop**: is the first advanced work that leverages LLMs to generate monochrome, icon-level SVGs. We referred to its parametric implementation.

Here is the list of highly related concurrent works:

**LLM4SVG**: treats SVG coordinates as number strings and predicts decimal part for higher spatial accuracy.

**StarVector**: equips LLM with an image encoder for Image-to-SVG generation.