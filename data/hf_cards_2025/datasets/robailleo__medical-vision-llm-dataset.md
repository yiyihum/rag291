---
license: apache-2.0
task_categories:
- visual-question-answering
- image-to-text
- visual-instruction-following
task_ids:
- medical-image-analysis
- radiology-report-generation
- medical-vision-language
language:
- en
tags:
- medical
- healthcare
- radiology
- vision-language
- multimodal
- instruction-tuning
size_categories:
- 10K<n<100K
---

# Combined Medical Vision-Language Dataset

## Dataset Description

Comprehensive medical vision-language dataset with 4793 samples for vision-based LLM training.

## Dataset Statistics

- **Total Samples**: 4793
- **Training Samples**: 3834
- **Validation Samples**: 959

### Modality Distribution

- X-ray: 2325 samples
- CT: 1351 samples
- Unknown: 812 samples
- MRI: 231 samples
- Ultrasound: 70 samples
- Microscopy: 2 samples
- Endoscopy: 2 samples

### Body Part Distribution

- Unknown: 2856 samples
- Chest: 718 samples
- Abdomen: 468 samples
- Head: 408 samples
- Extremities: 125 samples
- Spine: 119 samples
- Pelvis: 99 samples

### Source Distribution

- ROCO: 3000 samples
- VQA-RAD: 1793 samples

## Sources

1. **ROCO (Radiology Objects in Context)**: Medical images with detailed captions
2. **VQA-RAD**: Visual question answering for radiology with expert annotations
3. **PubMedVision-enhanced**: Large-scale medical VQA dataset with aligned image-text pairs

## Dataset Format

Each sample contains:
- `image`: Medical image (PIL.Image)
- `conversations`: Multi-turn conversation in role-content format
- `image_description`: Textual description of the image
- `question`: Medical question about the image
- `answer`: Expert answer/description
- `dataset_source`: Source dataset
- `modality`: Imaging modality (X-ray, CT, MRI, etc.)
- `body_part`: Anatomical region
- `instruction`: Task instruction for training

## Intended Use

- Fine-tuning vision-language models for medical applications
- Training medical AI assistants for image analysis
- Research in medical multimodal AI
- Educational purposes in medical imaging

## Vision-Based LLM Training

This dataset is optimized for training vision-language models on:
- Medical image description and explanation
- Visual question answering in healthcare
- Diagnostic reasoning from images
- Multimodal medical conversation

## Ethical Considerations

- For research and educational purposes only
- Not for clinical decision making
- Comply with medical ethics and privacy guidelines
- Ensure proper model validation before deployment

## Citation

Please cite the original datasets:
- ROCO: https://huggingface.co/datasets/eltorio/ROCOv2-radiology
- VQA-RAD: https://huggingface.co/datasets/flaviagiammarino/vqa-rad
- PubMedVision: https://huggingface.co/datasets/FreedomIntelligence/PubMedVision

## License

Apache 2.0