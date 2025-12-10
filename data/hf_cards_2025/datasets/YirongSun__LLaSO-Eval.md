---
license: cc-by-nc-4.0
task_categories:
- audio-text-to-text
language:
- en
tags:
- speech
- multimodal
- instruction-tuning
- large-language-model
- speech-language-model
- speech-to-text
- text-to-speech
- reproducible-research
---

# LLaSO-Instruct: A Multi-task Instruction-Tuning Dataset for Large Language and Speech Models

This repository contains **LLaSO-Instruct**, a 13.5M-instance multi-task instruction-tuning dataset, which is an essential part of the LLaSO framework.

The LLaSO framework and the LLaSO-Instruct dataset were presented in the paper:
**[LLaSO: A Foundational Framework for Reproducible Research in Large Language and Speech Model](https://huggingface.co/papers/2508.15418)**

The complete code, models, and datasets are available on the project's GitHub repository:
**[https://github.com/EIT-NLP/LLaSO](https://github.com/EIT-NLP/LLaSO)**

## Introduction to LLaSO-Instruct

LLaSO-Instruct is a 13.5M-instance multi-task instruction-tuning dataset designed for robust, compositional understanding in Large Speech-Language Models (LSLMs). It is one of three essential resources provided by the LLaSO framework to address fragmented architectures and a lack of transparency in LSLM research.

The LLaSO framework aims to be the first fully open, end-to-end stack for large-scale speech–language modeling, unifying data, evaluation, and modeling. It comprises:
-   **LLaSO-Align (12.0M):** An ASR-based speech-text alignment corpus.
-   **LLaSO-Instruct (13.5M):** This multi-task instruction-tuning dataset across linguistic, semantic, and paralinguistic objectives.
-   **LLaSO-Eval (15,044):** A stratified benchmark for instruction-following and cross-modality generalization.
-   **LLaSO-Base (3.8B):** A reference model trained exclusively on LLaSO's public data.

## ✨ Key Features of LLaSO-Instruct (13.5M / 20 tasks)

LLaSO-Instruct is built for robust, compositional understanding in LSLMs. Its key characteristics include:

*   **Purpose:** Multi-task instruction tuning across a wide array of speech and language objectives.
*   **Task Types:** Spans 20 diverse linguistic, semantic, and paralinguistic tasks, incorporating both closed-ended and open-ended response formats.
*   **Modality Configurations:** Supports rich compositional interaction patterns across various input modalities:
    *   Text instruction with Audio input: **X**<sub>query</sub><sup>(t,a)</sup>
    *   Audio instruction with Text input: **X**<sub>query</sub><sup>(a,t)</sup>
    *   Pure audio instruction/input: **X**<sub>query</sub><sup>(a)</sup>
*   **Label Granularity:** Features multi-granularity labels, for example, ranging from coarse to fine descriptions of age or accent.

### LLaSO Corpus Overview (Context)

LLaSO-Instruct is part of the larger LLaSO Corpus:

*   **Composition:** A total of 25.5M samples (12.0M Align + 13.5M Instruct) covering 20 tasks across all major modality configurations (text instr. with audio input, pure audio, audio instr. with text input).
*   **Overall Task Distribution:** 52% linguistic, 8% semantic, 40% paralinguistic.
*   **Real vs. Synthetic:** Consists of 71% real-world audio and 29% synthetic speech.
*   **Design Motivation:**
    *   *Linguistic (ASR)* remains foundational for speech–text alignment and generalization.
    *   *Semantic* tasks are intentionally underweighted, as their challenge lies more in language modeling than in speech understanding.
    *   *Paralinguistic* tasks (speaker, accent, emotion, pronunciation scoring) are prioritized to address their underrepresentation in open datasets.
*   **Flexible Modality Roles:** Both audio and text serve as input/instruction, enabling rich compositional interaction patterns.

<p align="center">
  <img src="https://github.com/EIT-NLP/LLaSO/blob/main/figures/data_pipeline_trim.png?raw=true" width="980" alt="LLaSO data construction pipeline">
</p>
<p align="center"><i>
LLaSO data construction pipeline, from text QA and multi-source speech to two-stage training datasets.
</i></p>

## 📂 Data Preparation

The training and alignment scripts in the LLaSO framework expect a **single JSON file** as input for the instruction data. For flexibility, LLaSO-Instruct data is released in multiple subdirectories (e.g., `audio_text/`, `pure_audio/`, `text_audio/`). This split format allows users to explore or train with individual modality subsets. For full training, these subsets need to be merged into one JSON.

A script [`./llaso/scripts/data_merge.py`](https://github.com/EIT-NLP/LLaSO/blob/main/llaso/scripts/data_merge.py) is provided in the LLaSO GitHub repository for this purpose. Use it to combine the JSON files under each modality subdirectory into a single training file.

## 🚀 Sample Usage for Training

To train a model using the LLaSO-Instruct dataset, you first need to clone the LLaSO framework and install its dependencies, then prepare the data. The general training pipeline involves two stages: Speech-Text Alignment and Multi-task Instruction Tuning.

### 1. Installation

First, clone the repository and set up the environment:

```bash
git clone https://github.com/EIT-NLP/LLaSO.git
cd LLaSO
conda create -n llaso python=3.10 -y
conda activate llaso
pip install --upgrade pip  # enable PEP 660 support
pip install -e .  # See pyproject.toml for dependencies
pip install librosa==0.10.2.post1

# Install additional packages for training
pip install -e ".[train]"

# Optional: Install FlashAttention for acceleration (refer to GitHub for troubleshooting)
# MAX_JOBS=8 pip install -v flash-attn --no-build-isolation
```

### 2. Data Merging (if necessary)

If you have multiple JSON files from different modalities, merge them into a single file for full training:

```bash
# Example: Merge data from two modality subdirectories
python llaso/scripts/data_merge.py --input_dirs path/to/LLaSO-Instruct/audio_text path/to/LLaSO-Instruct/pure_audio --output_file merged_instruct_data.json
```
Refer to the [Data Preparation section on GitHub](https://github.com/EIT-NLP/LLaSO#data-preparation) for more details.

### 3. Training Stages

Once the environment is set up and data is prepared, you can train a model from scratch using the LLaSO-Instruct data for the second stage:

```bash
# Stage 1: Speech-Text Alignment (ASR) - typically uses LLaSO-Align data
bash llaso/scripts/align.sh 

# Stage 2: Multi-task Instruction Tuning - uses LLaSO-Instruct data
bash llaso/scripts/finetune.sh 
```
For detailed configurations, required model weights, and script parameters, please refer to the official [LLaSO GitHub repository](https://github.com/EIT-NLP/LLaSO).

<p align="center">
  <img src="https://github.com/EIT-NLP/LLaSO/blob/main/figures/cases1_trim.png?raw=true" width="900"> 
  <img src="https://github.com/EIT-NLP/LLaSO/blob/main/figures/cases2_trim.png?raw=true" width="900">
</p>
<p align="center"><i>
Cases for input modality configurations and task prototypes illustrate LLaSO's compositional flexibility. Pure audio (top), text instruction with audio input (middle), and audio instruction with text input (bottom). Each figure presents distinct tasks under its respective format.
</i></p>

## 📑 How to Cite

If you use LLaSO or LLaSO-Instruct in your research or applications, please cite the paper:

```bibtex
@misc{sun2025llaso,
      title={LLaSO: A Foundational Framework for Reproducible Research in Large Language and Speech Model}, 
      author={Yirong Sun and Yizhong Geng and Peidong Wei and Yanjun Chen and Jinghan Yang and Rongfei Chen and Wei Zhang and Xiaoyu Shen},
      year={2025},
      eprint={2508.15418},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.15418}, 
}
```