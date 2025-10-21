---
language:
- en
pretty_name: CoIN-ASD Benchmark
tags:
- multimodal-continual-instruction-tuning
- continual-learing
- instruction-tuning
license: mit
---

# CoIN-ASD Benchmark

CoIN-ASD is a benchmark dataset designed for multimodal continual instruction tuning (MCIT), based on the [CoIN](https://github.com/zackschen/CoIN) dataset. This dataset aims to evaluate the performance of MCIT models in mitigating *essential forgetting*.
📝 [Paper](https://arxiv.org/abs/2505.02486)
🐙 [GitHub](https://github.com/jinpeng0528/SEFE)

## Dataset Structure

The dataset is organized in the following structure:

```
├── ScienceQA/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── TextVQA/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── ImageNet/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── GQA/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── VizWiz/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── Grounding/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
├── VQAv2/
│   ├── train_ori.json
│   ├── train_x{10,20,40,60,80}.json
│   └── test.json
└── OCRVQA/
    ├── train_ori.json
    ├── train_x{10,20,40,60,80}.json
    └── test.json
```

## Important Notes

1. **Image Data**: This repository only contains the annotations. To obtain the images, please refer to the [CoIN repository](https://github.com/zackschen/CoIN).

2. **Training Data Versions**: For each task, we provide multiple versions of training data with different values of hyperparameter X (10, 20, 40, 60, 80). For example, `train_x20.json` contain the ASD-processed annotations with X set to 20. Additionally, `train_ori.json` contains the original annotations without ASD processing.

3. **Usage**: To use this dataset, you need to:
   - Download the original images of CoIN
   - Download the annotations from this repository
   - Organize them according to the directory structure described in [our GitHub repository](https://github.com/jinpeng0528/SEFE/tree/main#data-organization-and-structure)

## Citation

```
@inproceedings{chen2025sefe,
  title={SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning},
  author={Chen, Jinpeng and Cong, Runmin and Zhao, Yuzhi and Yang, Hongzheng and Hu, Guangneng and Ip, Horace Ho Shing and Kwong, Sam},
  booktitle={ICML},
  year={2025}
}
```