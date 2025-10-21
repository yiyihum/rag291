---
license: odc-by
dataset_info:
  features:
  - name: chat
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 9962835254
    num_examples: 2606173
  download_size: 3633676909
  dataset_size: 9962835254
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ka
- en
---

## Dataset Details

- **Developed by:** Tbilisi AI Lab

## Citation
```bibtex
@misc{tbilisi2025konasftmix2.6M,
  title        = {kona-sft-mix-2.6M: A Dataset by Tbilisi AI Lab},
  author       = {Tbilisi AI Lab Team},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/tbilisi-ai-lab/kona-sft-mix-2.6M}},
  note         = {Accessed: 2025-10-18}
}
```

## License/Terms of Use:
odc-by