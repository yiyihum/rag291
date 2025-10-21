---
license: cc-by-nc-4.0
task_categories:
- audio-text-to-text
language:
- en
tags:
- multimodal
- speech-language-model
- instruction-tuning
- benchmark
- ASR
- alignment
- reproducible-research
---

# LLaSO: A Foundational Framework for Reproducible Research in Large Language and Speech Model

This repository contains the dataset for the paper [LLaSO: A Foundational Framework for Reproducible Research in Large Language and Speech Model](https://huggingface.co/papers/2508.15418).

Code: https://github.com/EIT-NLP/LLaSO

## Abstract

The development of Large Speech-Language Models (LSLMs) has been slowed by fragmented architectures and a lack of transparency, hindering the systematic comparison and reproducibility of research. Unlike in the vision-language domain, the LSLM field suffers from the common practice of releasing model weights without their corresponding training data and configurations. To address these critical gaps, we introduce LLaSO, the first fully open, end-to-end framework for large-scale speech-language modeling. LLaSO provides the community with three essential resources: (1) LLaSO-Align, a 12M-instance speech-text alignment corpus; (2) LLaSO-Instruct, a 13.5M-instance multi-task instruction-tuning dataset; and (3) LLaSO-Eval, a reproducible benchmark for standardized evaluation. To validate our framework, we build and release LLaSO-Base, a 3.8B-parameter reference model trained exclusively on our public data. It achieves a normalized score of 0.72, establishing a strong, reproducible baseline that surpasses comparable models. Our analysis reveals that while broader training coverage enhances performance, significant generalization gaps persist on unseen tasks, particularly in pure audio scenarios. By releasing the complete stack of data, benchmarks, and models, LLaSO establishes a foundational open standard to unify research efforts and accelerate community-driven progress in LSLMs.

## What is LLaSO?

**LLaSO is the first fully open, end-to-end stack for large-scale speech–language modeling, unifying data, evaluation, and modeling in one framework.**

-   **LLaSO-Align (12.0M):** ASR-based alignment for grounding speech in textual semantic space.
-   **LLaSO-Instruct (13.5M / 20 tasks / 3 modality configs):** Multi-task instruction tuning across linguistic, semantic, and paralinguistic objectives.
-   **LLaSO-Eval (15,044):** Stratified benchmark for instruction-following and cross-modality generalization.
-   **LLaSO-Base (3.8B):** Two-stage trained reference model, adapted from LLaVA-style architectures for robust compositional understanding.

## Key Features

-   **Fully Open, End-to-End Stack:** Unified release of corpus, benchmark, and model-enabling open-source research and fair comparison in speech-language modeling.
-   **25.5M Samples, 20 Tasks, 3 Modality Configurations:** Supports all major text ↔ audio combinations (text + audio, audio + text, pure audio), covering linguistic, semantic, and paralinguistic tasks.
-   **Stratified Evaluation (15,044):** Cohesive design between training and test sets enables systematic assessment of instruction following, cross-modality generalization, abstention rate, and stability.
-   **Robust Reference Model (3.8B):** Two-stage training (ASR alignment → instruction tuning), easily reproducible and extensible for further research.
-   **Empirical Insights:** Broader task and modality coverage consistently leads to stronger overall performance, but unseen modality/task configurations (especially pure audio) remain challenging; interleaving and parallel decoding strategies can bridge some gaps.

## Install
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

#install FlashAttention for acceleration
MAX_JOBS=8 pip install -v flash-attn --no-build-isolation
```
> **Tips:**  
> If you encounter issues with FlashAttention installation (e.g., build errors or the process getting stuck), we recommend manually downloading the appropriate FlashAttention 2 wheel from the [official Dao-AILab releases](https://github.com/Dao-AILab/flash-attention/releases).  
> For example, for `python3.10 + cu12.2 + torch2.1`, download:  
> 
> ```
> https://github.com/Dao-AILab/flash-attention/releases/download/v2.4.3.post1/flash_attn-2.4.3.post1+cu122torch2.1cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
> ```
> and then install it via:  
> 
> ```bash
> pip install /path/to/flash_attn-2.4.3.post1+cu122torch2.1cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
> ```

## Data Preparation

The training and alignment scripts expect a **single JSON file** as input.  
However, for flexibility, we release the instruction data in multiple subdirectories (e.g., `audio_text/`, `pure_audio/`, `text_audio/`).  

-   This split format allows users to **explore or train with individual modality subsets**.  
-   For full training, these subsets need to be **merged into one JSON**.  

We provide [`./llaso/scripts/data_merge.py`](https://github.com/EIT-NLP/LLaSO/blob/main/llaso/scripts/data_merge.py) for this purpose.  
Use it to combine the JSON files under each modality subdirectory into a single training file.  

> **Dataset Availability**  
> - ✅ **[LLaSO-Eval](https://huggingface.co/datasets/YirongSun/LLaSO-Eval)** is already available on Hugging Face.  
> - ✅ **[LLaSO-Instruct](https://huggingface.co/datasets/YirongSun/LLaSO-Instruct)** has been fully uploaded and is available now.  
> - ✅ **[LLaSO-Align](https://huggingface.co/datasets/YirongSun/LLaSO-Align)** has been fully uploaded and is available now.  

## Quick Start (Sample Usage)

### Training
Train LLaSO-Base from scratch with:
```python
# Stage 1: Speech-Text Alignment (ASR)
bash llaso/scripts/align.sh 

# Stage 2: Multi-task Instruction Tuning
bash llaso/scripts/finetune.sh 
```

### Inference
Run model inference on your own data or evaluation set:
```python
python llaso/evaluation/model_eval.py \
  --audio_tower ./whisper-large-v3 \
  --model_path ./LLaSO-Base-3.8B-Instruct \
  --data_path ./LLaSO-Eval/your_eval.json \
  --output_dir ./your_output_dir
```

### Evaluation
LLaSO provides flexible evaluation metrics for all supported tasks.
See the `llaso/evaluation/metrics/` directory for dedicated metric scripts per task type.

## LLaSO Corpus Overview
-   **Composition:** 25.5M samples (12.0M Align + 13.5M Instruct) covering 20 tasks across all major modality configurations (text instr. with audio input, pure audio, audio instr. with text input).
-   **Overall Task Distribution:** 52% linguistic, 8% semantic, 40% paralinguistic.
-   **Real vs. Synthetic:** 71% real-world audio, 29% synthetic speech.
-   **Design Motivation:** 
    -   *Linguistic (ASR)* remains foundational for speech–text alignment and generalization.
    -   *Semantic* tasks are intentionally underweighted, as their challenge lies more in language modeling than in speech understanding.
    -   *Paralinguistic* tasks (speaker, accent, emotion, pronunciation scoring) are prioritized to address their underrepresentation in open datasets.
-   **Flexible Modality Roles:** Both audio and text serve as input/instruction, enabling rich compositional interaction patterns.

---

### LLaSO-Align (12.0M)
-   **Goal:** ASR-based alignment; encoder & LLM frozen, projector trained for speech-to-text semantic grounding.
-   **Domains:** Conversational, narrative, audiobook, accented speech.
-   **Templates:** 18 instruction types for ASR; unified JSON format for integration.

### LLaSO-Instruct (13.5M / 20 tasks)
-   **Purpose:** Multi-task instruction tuning for robust, compositional understanding.
-   **Task Types:** Spans linguistic, semantic, and paralinguistic objectives with a mix of closed- and open-ended formats.
-   **Modality Configurations:**  
    -   Text instruction + Audio input: **X**<sub>query</sub><sup>(t,a)</sup>
    -   Audio instruction + Text input: **X**<sub>query</sub><sup>(a,t)</sup>
    -   Pure audio: **X**<sub>query</sub><sup>(a)</sup>
-   **Label Granularity:** Multi-granularity (e.g., coarse→fine age, accent).

### LLaSO-Eval (15,044)
-   **Benchmarking:** Strictly stratified; consistent with training data.
-   **Coverage:** All tasks and modality combinations.
-   **Metrics:** Supports abstention rate analysis and cross-modality generalization evaluation.

## Citation

If you use LLaSO in your research or applications, please cite our paper:

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