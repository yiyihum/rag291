---
language:
- en
license: cc-by-4.0
size_categories:
- 1M<n<10M
task_categories:
- image-to-image
pretty_name: GPT-Image-Edit-1.5M
tags:
- image
- image-editing
- instruction-tuning
- instruction-guided
- multimodal
library_name: datasets
---

# **GPT-Image-Edit-1.5M** A *Million-Scale*, *GPT-Generated* Image Dataset

[📃Arxiv](https://arxiv.org/abs/2507.21033) | [🌐 Project Page](https://ucsc-vlaa.github.io/GPT-Image-Edit/) | [💻Github](https://github.com/wyhlovecpp/GPT-Image-Edit/)

**GPT-Image-Edit-1.5M** is a comprehensive image editing dataset that is built upon HQ-Edit, UltraEdit, OmniEdit and Complex-Edit, with all output images regenerated with GPT-Image-1.

# 📣 News
*   **[2025.08.20]** 🚀 We provide a script for multi-process downloading. See [Multi-process Download](#multi-process-download).
*   **[2025.07.27]** 🤗 We release GPT-Image-Edit, a state-of-the-art image editing model with 1.5M high-quality editing samples. All [data](https://huggingface.co/datasets/UCSC-VLAA/GPT-Image-Edit-1.5M), [models](https://huggingface.co/UCSC-VLAA/gpt-image-edit-training), training code and evaluation code are open-sourced. Our code is based on [UniWorld-V1](https://github.com/PKU-YuanGroup/UniWorld-V1), Thanks to the authors of UniWorld-V1. Checking our [report](https://arxiv.org/abs/2507.21033) for more details. Welcome to **watch** 👀 this repository for the latest updates.

## Dataset Statistics Summary

### Full Dataset Overview

| Dataset Source | Total Samples | Instruction Types | Description |
|----------------|---------------|-------------|-------------|
| **HQ-Edit** | 183,182 | Original | Fully-synthetic image editing dataset with high-quality input and output images |
| **UltraEdit** | 100,008 | Original | Comprehensive image editing dataset with 9 editing tasks |
| **OmniEdit** | 1,270,385 | Original/Rewrited/Complex | Large-scale multi-task dataset with original, rewrited and Complex-Edit style instructions |
| **Total** | **1,553,575** | Original/Rewrited/Complex | **Complete unified dataset with output images re-edited with GPT-Image-1** |

### Instruction Complexity Distribution
- **Original Instructions** :
    - 1,140,182 samples
    - Same instructions from the original dataset
    - Basic to moderate complexity
- **Rewrited Instructions**: 
    - 100,000 samples
    - Instructions rewrited based on the input image and new output image
    - Enhanced complexity
- **Complex Instructions**:
    - 313,393 samples
    - Complex-edit style instructions, with $C_3$ level complexity
    - Advanced complexity


### Detailed Breakdown by Source and Task

#### HQ-Edit Dataset (183,182 samples)
| Subfolder | Samples | Input Source | Instruction Source | Output Source |
|------|---------|--------------|-------------------|---------------|
| edit | 89,585 | HQ-Edit's original input images | HQ-Edit's original rewrited instructions | GPT-edited output images |
| generate | 93,597 | Input images generated with original captions | HQ-Edit's original rewrited instructions | GPT-edited output images |

Output images of 89,585 samples in `edit` subfolder are based on the original input images of HQ-Edit but edited with GPT-Image-1. 93,597 samples in `generate` subfolder have the input images re-genererated with GPT-Image-1 and then edited by the same model to produce output images.

#### OmniEdit Dataset (1,270,385 samples)
| Task | Samples| Rewrite Instructions |
|------|---------|---------------------|
|addition|189,336|14,385|
|attribute_modification|204,065|14,509|
|env|137,440|14,509|
|removal|149,763|13,497|
|style|14,405|14,405|
|swap (object + background)|261,983|28,695|
|complex-edit|313,393|–|

Output images from OmniEdit are re-edited with original input images and instructions with GPT-Image-1. Additionally, we sampled 313,393 input images from OmniEdit and generated Complex-Edit style instructions, with $C_3$ level complexity.

#### UltraEdit Dataset (100,008 samples)
| Task | Samples |
|------|---------|
| add | 11,112 |
| change_color | 11,112 |
| change_global | 11,112 |
| change_local | 11,112 |
| others | 11,112 |
| replace | 11,112 |
| transform_global | 11,112 |
| transform_local | 11,112 |
| turn | 11,112 |

100,008 samples from UltraEdit, uniformly sampled from 9 categories, have original input images re-edited by GPT-Image-1 with original instructions.

## Unified Directory Structure

```
gpt-edit/
├── hqedit/
│   ├── edit/
│   │   ├── input/                    # Original input images
│   │   ├── output/                   # GPT-generated edited images
│   │   └── metadata/
│   │       └── hqedit_edit.json      # 89,585 samples
│   └── generate/
│       ├── input/                    # Generated input images
│       ├── output/                   # Generated output images
│       └── metadata/
│           └── hqedit_generate.json  # 93,597 samples
├── omniedit/
│   ├── addition/
│   │   ├── input/                    # Original input images
│   │   ├── output/                   # Original + GPT outputs
│   │   └── metadata/
│   │       └── omniedit_addition.json
│   ├── attribute_modification/
│   ├── background_swap/
│   ├── complex-edit/
│   ├── env/
│   ├── object_swap/
│   ├── removal/
│   ├── style/
│   └── swap/
└── ultraedit/
    ├── add/
    │   ├── input/                    # Original input images
    │   ├── output/                   # GPT-generated outputs
    │   └── metadata/
    │       └── ultraedit_add.json
    ├── change_color/
    ├── change_global/
    ├── change_local/
    ├── others/
    ├── replace/
    ├── transform_global/
    ├── transform_local/
    └── turn/
```

Please note that samples in `gpt-edit/omniedit/swap` are **NOT** a third kind of `swap` operation but haven't yet been classified into `background_swap` or `object_swap`.

## Metadata Format

All metadata files follow a unified JSON structure:

### Common Fields
```python
{
  "id": "string",                    # Unique identifier: <dataset>_<task>_<id>
  "dataset_source": "string",       # "hqedit" | "omniedit" | "ultraedit"
  "task": "string",                 # Task category (e.g., "edit", "addition", "add")
  "input": "string",                # Relative path to input image: "input/<id>.png"
  "output": "string",               # Relative path to output image: "output/<id>.png"
  "instruction": "string",          # Editing instruction text
  "instruction_type": "string",     # "original" | "rewrite" | "complex"
  "input_description": "string"     # Description of the input image
}
```

### Dataset-Specific Fields

#### OmniEdit
```python
{
  "instruction_original": "string"  # Original instruction (for rewrite cases)
}
```

## Usage Guide

### Download
You can download the dataset using `git lfs` from the Hugging Face Hub:
```bash
git lfs install
git clone https://huggingface.co/datasets/UCSC-VLAA/GPT-Image-Edit-1.5M
```

#### Multi-process Download
We provide a script for faster download with multi-processing.

1. Download the script.
    ```bash
    wget https://huggingface.co/datasets/UCSC-VLAA/GPT-Image-Edit-1.5M/blob/main/download.sh
    ```

2. Use the script for multi-process downloading.
    ```bash
    bash download.sh -d <dataset_name> -o <your_directory>/gpt-edit -p <process_number>
    ```

    `<dataset_name>` should be one of `hqedit`/`ultraedit`/`omniedit`.

### Prepare the Data

The annotation JSON files are located in [UCSC-VLAA/gpt-image-edit-training/training_json](https://huggingface.co/UCSC-VLAA/gpt-image-edit-training/tree/main/training_json).

To prepare a `data.txt` file for training (as mentioned in the associated GitHub repository), use the following format:
1. The first column is the root path to the image.
2. The second column is the corresponding annotation JSON file.
3. The third column indicates whether to enable the region-weighting strategy (we use `false` in our training setting).

An example `data.txt` for `gpt-edit` can be found in the [GitHub repository](https://github.com/wyhlovecpp/GPT-Image-Edit#data-preparation), or an example structure is:
```
data/gpt-edit/hqedit/edit,training_json/hqedit_gpt_edit.json,false
data/gpt-edit/hqedit/generate,training_json/hqedit_gpt_generate.json,false
data/gpt-edit/omniedit,training_json/omniedit_gpt.json,false
data/gpt-edit/omniedit,training_json/omniedit_gpt_rewrite.json,false
data/gpt-edit/omniedit/complex-edit,training_json/complexedit_gpt.json,false
data/gpt-edit/ultraedit,training_json/ultraedit_gpt.json,false
```

### Working with Image Paths
Paths in metadata are relative to the task directory

```python
# Input: "input/00070858.png" -> hqedit/edit/input/00070858.png
# Output: "output/00070858.png" -> hqedit/edit/output/00070858.png
```

# 📊 Benchmarks

### GEdit-EN-full
| Model | BG<br>Change | Color<br>Alt. | Mat.<br>Mod. | Motion | Portrait | Style | Add | Remove | Replace | Text | Tone | Avg |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| *Open-Sourced Models* |||||||||||||
| AnyEdit | 4.31 | 4.25 | 2.64 | 0.67 | 1.90 | 1.95 | 3.72 | 3.75 | 3.23 | 0.77 | 4.21 | 2.85 |
| MagicBrush | 6.17 | 5.41 | 4.75 | 1.55 | 2.90 | 4.10 | 5.53 | 4.13 | 5.10 | 1.33 | 5.07 | 4.19 |
| Instruct-Pix2Pix | 3.94 | 5.40 | 3.52 | 1.27 | 2.62 | 4.39 | 3.07 | 1.50 | 3.48 | 1.13 | 5.10 | 3.22 |
| OmniGen | 5.23 | 5.93 | 5.44 | 3.12 | 3.17 | 4.88 | 6.33 | 6.35 | 5.34 | 4.31 | 4.96 | 5.01 |
| Step1X-Edit | 7.03 | 6.26 | 6.46 | 3.66 | 5.23 | 7.24 | 7.17 | 6.42 | 7.39 | 7.40 | 6.62 | 6.44 |
| Bagel | 7.44 | 6.99 | 6.26 | 5.09 | 4.82 | 6.04 | 7.94 | 7.37 | 7.31 | 7.16 | 6.17 | 6.60 |
| Bagel-thinking | 7.22 | 7.24 | 6.69 | 7.12 | 6.03 | 6.17 | 7.93 | 7.44 | 7.45 | 3.61 | 6.36 | 6.66 |
| Ovis-U1 | 7.49 | 6.88 | 6.21 | 4.79 | 5.98 | 6.46 | 7.49 | 7.25 | 7.27 | 4.48 | 6.31 | 6.42 |
| OmniGen2 | - | - | - | - | - | - | - | - | - | - | - | 6.42 |
| Step1X-Edit (v1.1) | 7.45 | 7.38 | 6.95 | 4.73 | 4.70 | 7.11 | 8.20 | 7.59 | 7.80 | 7.91 | 6.85 | 6.97 |
| FluxKontext dev | 7.06 | 7.03 | 5.52 | 5.62 | 4.68 | 5.55 | 6.95 | 6.76 | 6.13 | 6.10 | 7.48 | 6.26 |
| *Proprietary Models* |||||||||||||
| Gemini | 7.11 | 7.14 | 6.47 | 5.67 | 3.99 | 4.95 | 8.12 | 6.89 | 7.41 | 6.85 | 7.01 | 6.51 |
| Doubao | 8.07 | 7.36 | 7.20 | 5.38 | 6.28 | 7.20 | 8.05 | 7.71 | 7.87 | 4.01 | 7.67 | 6.98 |
| GPT-4o | 6.96 | 6.85 | 7.10 | 5.41 | 6.74 | 7.44 | 7.51 | 8.73 | 8.55 | 8.45 | 8.69 | 7.49 |
| **Ours** | **7.80** | **7.54** | **7.12** | **7.75** | **7.09** | **6.74** | **8.04** | **7.95** | **7.17** | **5.45** | **6.95** | **7.24** |

### Complex-Edit
| Method | IF | IP | PQ | Overall |
|:--|:--:|:--:|:--:|:--:|
| AnyEdit | 1.60 | 8.15 | 7.25 | 5.67 |
| UltraEdit | 6.56 | 5.93 | 7.29 | 6.59 |
| OmniGen | 6.25 | 6.42 | 7.54 | 6.74 |
| FluxKontext Dev | 8.56 | 8.39 | 8.51 | 8.49 |
| Imagen3 | 7.56 | 6.55 | 7.67 | 7.26 |
| SeedEdit | 8.49 | 6.91 | 8.74 | 8.04 |
| GPT-4o | 9.29 | 7.51 | 9.47 | 8.76 |
| **Ours** | **8.99** | **8.41** | **8.93** | **8.78** |

### ImgEdit-Full
| Model | Add | Adjust | Extract | Replace | Remove | Background | Style | Hybrid | Action | Overall |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MagicBrush | 2.84 | 1.58 | 1.51 | 1.97 | 1.58 | 1.75 | 2.38 | 1.62 | 1.22 | 1.90 |
| Instruct-Pix2Pix | 2.45 | 1.83 | 1.44 | 2.01 | 1.50 | 1.44 | 3.55 | 1.20 | 1.46 | 1.88 |
| AnyEdit | 3.18 | 2.95 | 1.88 | 2.47 | 2.23 | 2.24 | 2.85 | 1.56 | 2.65 | 2.45 |
| UltraEdit | 3.44 | 2.81 | 2.13 | 2.96 | 1.45 | 2.83 | 3.76 | 1.91 | 2.98 | 2.70 |
| OmniGen | 3.47 | 3.04 | 1.71 | 2.94 | 2.43 | 3.21 | 4.19 | 2.24 | 3.38 | 2.96 |
| Step1X-Edit | 3.88 | 3.14 | 1.76 | 3.40 | 2.41 | 3.16 | 4.63 | 2.64 | 2.52 | 3.06 |
| ICEdit | 3.58 | 3.39 | 1.73 | 3.15 | 2.93 | 3.08 | 3.84 | 2.04 | 3.68 | 3.05 |
| BAGEL | 3.56 | 3.31 | 1.70 | 3.30 | 2.62 | 3.24 | 4.49 | 2.38 | 4.17 | 3.20 |
| UniWorld-V1 | 3.82 | 3.64 | 2.27 | 3.47 | 3.24 | 2.99 | 4.21 | 2.96 | 2.74 | 3.26 |
| OmniGen2 | 3.57 | 3.06 | 1.77 | 3.74 | 3.20 | 3.57 | 4.81 | 2.52 | 4.68 | 3.44 |
| Ovis-U1 | 4.13 | 3.62 | 2.98 | 4.45 | 4.06 | 4.22 | 4.69 | 3.45 | 4.61 | 4.00 |
| FluxKontext dev | 3.76 | 3.45 | 2.15 | 3.98 | 2.94 | 3.78 | 4.38 | 2.96 | 4.26 | 3.52 |
| GPT-4o | 4.61 | 4.33 | 2.90 | 4.35 | 3.66 | 4.57 | 4.93 | 3.96 | 4.89 | 4.20 |
| **Ours** | **4.07** | **3.79** | **2.04** | **4.13** | **3.89** | **3.90** | **4.84** | **3.04** | **4.52** | **3.80** |

# 👍 Acknowledgement and Related Work
*   [UniWorld-V1](https://github.com/PKU-YuanGroup/UniWorld-V1): UniWorld-V1 is a unified framework for understanding, generation, and editing.
*   [ImgEdit](https://github.com/PKU-YuanGroup/ImgEdit): ImgEdit is a large-scale, high-quality image-editing dataset comprising 1.2 million carefully curated edit pairs and a comprehensive benchmark for image editing.
*   [Complex-edit](https://github.com/UCSC-VLAA/Complex-Edit): Complex-edit is benchmark for complex image editing.
*   [Qwen2.5-VL](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct): The new flagship vision-language model of Qwen.
*   [FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev): A state-of-the-art image editing model.
*   [Step1X-Edit](https://github.com/stepfun-ai/Step1X-Edit): A state-of-the-art image editing model and a comprehensive benchmark for image editing.
*   [OmniGen2](https://github.com/VectorSpaceLab/OmniGen2): A state-of-the-art image editing model and a comprehensive benchmark for image editing.

## Citation

If you find our paper useful, please cite us with
```
@misc{wang2025gptimageedit15mmillionscalegptgeneratedimage,
      title={GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset}, 
      author={Yuhan Wang and Siwei Yang and Bingchen Zhao and Letian Zhang and Qing Liu and Yuyin Zhou and Cihang Xie},
      year={2025},
      eprint={2507.21033},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2507.21033}, 
}
```