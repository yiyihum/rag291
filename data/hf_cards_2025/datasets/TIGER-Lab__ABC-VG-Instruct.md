---
language:
- en
license: mit
size_categories:
- 10K<n<100K
task_categories:
- image-text-to-text
pretty_name: ABC-VG-Instruct
tags:
- multimodal
- embeddings
- visual-retrieval
- visual-question-answering
- instruction-tuning
- vision-language
- visual-genome
dataset_info:
  features:
  - name: '0'
    struct:
    - name: height
      dtype: int64
    - name: id
      dtype: int64
    - name: image
      dtype: int64
    - name: instruction
      dtype: string
    - name: phrase
      dtype: string
    - name: width
      dtype: int64
    - name: x
      dtype: int64
    - name: y
      dtype: int64
  - name: '1'
    struct:
    - name: height
      dtype: int64
    - name: id
      dtype: int64
    - name: image
      dtype: int64
    - name: instruction
      dtype: string
    - name: phrase
      dtype: string
    - name: width
      dtype: int64
    - name: x
      dtype: int64
    - name: y
      dtype: int64
  - name: '2'
    struct:
    - name: height
      dtype: int64
    - name: id
      dtype: int64
    - name: image
      dtype: int64
    - name: instruction
      dtype: string
    - name: phrase
      dtype: string
    - name: width
      dtype: int64
    - name: x
      dtype: int64
    - name: y
      dtype: int64
  - name: '3'
    struct:
    - name: height
      dtype: int64
    - name: id
      dtype: int64
    - name: image
      dtype: int64
    - name: instruction
      dtype: string
    - name: phrase
      dtype: string
    - name: width
      dtype: int64
    - name: x
      dtype: int64
    - name: y
      dtype: int64
  splits:
  - name: train
    num_bytes: 6787354
    num_examples: 12500
  download_size: 3386465
  dataset_size: 6787354
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

## VG Instruct

This is the instruction finetuning dataset for *ABC: Achieving better control of multimodal embeddings using VLMs*.
Each element in this dataset contains 4 instruction-captions pairs for images in the visual genome dataset, corresponding to different bounding boxes in the image.
We use this dataset to train an embedding model that can use instruction to embeds specific aspects of a scene.

![My Image](https://huggingface.co/datasets/TIGER-Lab/ABC-VG-Instruct/resolve/main/example.png)

Combined with our pretraining step, this results in a model that can create high quality embeddings from images containing multiple, potentially distracting elements.

## Paper, Website, and Code

For more information, please refer to the [Paper](https://huggingface.co/papers/2503.00329), [Website](https://tiger-ai-lab.github.io/ABC/), and [Code](https://github.com/TIGER-AI-Lab/ABC).

## Sample Usage

### Loading the dataset

You can load the text data and dataset metadata using HF's `load_dataset` utility:

```python
from datasets import load_dataset

dataset = load_dataset("TIGER-Lab/ABC-VG-Instruct")
print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['0', '1', '2', '3'],
#         num_rows: 12500
#     })
# })
print(dataset['train'][0])
# Example (output will vary):
# {
#   '0': {'height': 200, 'id': 2379374, 'image': 123, 'instruction': 'the person on the left', 'phrase': 'man', 'width': 100, 'x': 50, 'y': 100},
#   '1': {'height': 150, 'id': 2379375, 'image': 123, 'instruction': 'the woman in the middle', 'phrase': 'woman', 'width': 75, 'x': 180, 'y': 120},
#   '2': {'height': 180, 'id': 2379376, 'image': 123, 'instruction': 'the building in the background', 'phrase': 'building', 'width': 300, 'x': 0, 'y': 0},
#   '3': {'height': 50, 'id': 2379377, 'image': 123, 'instruction': 'the car on the right', 'phrase': 'car', 'width': 80, 'x': 350, 'y': 200}
# }
```

### Fetching Images

To fetch the images from our datasets, we provide scripts in the `fetch_datasets` directory within the [Github repository](https://github.com/TIGER-AI-Lab/ABC). These scripts will pull the pretraining/finetuning image data off the hub and unpack them in your huggingface datasets cache (under a directory called `tigerlab`).

Run `python ./fetch_datasets/instruct.py` to get the finetuning dataset's images.

### Quick Start with the Associated Model

To quickly get started with making multimodal embeddings using the ABC model, follow these steps from the project's GitHub repository:

1.  **Install Dependencies:**
    ```bash
    git clone https://github.com/TIGER-AI-Lab/ABC
    cd ABC
    pip install -r requirements.txt
    ```
2.  **Start making multimodal embeddings!**
    ```bash
    python -i ./quick_start.py
    ```

## Citation

```bibtex
@misc{schneider2025abcachievingbettercontrol,
      title={ABC: Achieving Better Control of Multimodal Embeddings using VLMs}, 
      author={Benjamin Schneider and Florian Kerschbaum and Wenhu Chen},
      year={2025},
      eprint={2503.00329},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2503.00329}, 
}
```