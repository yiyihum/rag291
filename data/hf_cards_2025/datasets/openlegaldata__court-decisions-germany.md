---
dataset_info:
- config_name: dump-20221018
  features:
  - name: id
    dtype: int64
  - name: slug
    dtype: string
  - name: court
    struct:
    - name: city
      dtype: int64
    - name: id
      dtype: int64
    - name: jurisdiction
      dtype: string
    - name: level_of_appeal
      dtype: string
    - name: name
      dtype: string
    - name: slug
      dtype: string
    - name: state
      dtype: int64
  - name: file_number
    dtype: string
  - name: date
    dtype: string
  - name: created_date
    dtype: string
  - name: updated_date
    dtype: string
  - name: type
    dtype: string
  - name: ecli
    dtype: string
  - name: content
    dtype: string
  - name: markdown_content
    dtype: string
  - name: reference_markers
    dtype: string
  splits:
  - name: train
    num_bytes: 12675871374
    num_examples: 251038
  download_size: 5606739471
  dataset_size: 12675871374
- config_name: dump-20221018-10k
  features:
  - name: id
    dtype: int64
  - name: slug
    dtype: string
  - name: court
    struct:
    - name: city
      dtype: int64
    - name: id
      dtype: int64
    - name: jurisdiction
      dtype: string
    - name: level_of_appeal
      dtype: string
    - name: name
      dtype: string
    - name: slug
      dtype: string
    - name: state
      dtype: int64
  - name: file_number
    dtype: string
  - name: date
    dtype: string
  - name: created_date
    dtype: string
  - name: updated_date
    dtype: string
  - name: type
    dtype: string
  - name: ecli
    dtype: string
  - name: content
    dtype: string
  - name: markdown_content
    dtype: string
  - name: reference_markers
    dtype: string
  splits:
  - name: train
    num_bytes: 657010368
    num_examples: 10000
  download_size: 300018672
  dataset_size: 657010368
- config_name: dump-20221018-1k
  features:
  - name: id
    dtype: int64
  - name: slug
    dtype: string
  - name: court
    struct:
    - name: city
      dtype: int64
    - name: id
      dtype: int64
    - name: jurisdiction
      dtype: string
    - name: level_of_appeal
      dtype: string
    - name: name
      dtype: string
    - name: slug
      dtype: string
    - name: state
      dtype: int64
  - name: file_number
    dtype: string
  - name: date
    dtype: string
  - name: created_date
    dtype: string
  - name: updated_date
    dtype: string
  - name: type
    dtype: string
  - name: ecli
    dtype: string
  - name: content
    dtype: string
  - name: markdown_content
    dtype: string
  - name: reference_markers
    dtype: string
  splits:
  - name: train
    num_bytes: 68786169
    num_examples: 1000
  download_size: 31220475
  dataset_size: 68786169
configs:
- config_name: dump-20221018
  data_files:
  - split: train
    path: dump-20221018/train-*
- config_name: dump-20221018-10k
  data_files:
  - split: train
    path: dump-20221018-10k/train-*
- config_name: dump-20221018-1k
  data_files:
  - split: train
    path: dump-20221018-1k/train-*
task_categories:
- text-generation
- fill-mask
language:
- de
tags:
- legal
size_categories:
- 100K<n<1M
---

# Open Legal Data: Court Decisions Germany

This dataset is a preprocessed version of an [Open Legal Data](https://de.openlegaldata.io) data dump, spefically it contains German court decisions.
The dataset was automatically generated and uploaded to the HF hub using [oldp-toolkit](https://github.com/openlegaldata/oldp-toolkit).

## Data format

Each dataset sample has the following format:

```json
{
    "id": 325566,
    "slug": "lg-koln-2029-11-13-84-o-24918",
    "court": {
        "city": 446,
        "id": 812,
        "jurisdiction": "Ordentliche Gerichtsbarkeit",
        "level_of_appeal": "Landgericht",
        "name": "Landgericht K\u00f6ln",
        "slug": "lg-koln",
        "state": 12
    },
    "file_number": "84 O 249\/18",
    "date": "2029-11-13",
    "created_date": "2020-02-06T11:01:05Z",
    "updated_date": "2020-12-10T13:50:38Z",
    "type": "Urteil",
    "ecli": "ECLI:DE:LGK:2029:1113.84O249.18.00",
    "content": "<h2>Tenor<\/h2>\n\n<ul class=\"ol\"><li><p>I. Die Beklagte wird verurteilt, der Kl\u00e4gerin ...",
    "markdown_content": "## Tenor\n\n- I. Die Beklagte wird verurteilt, der Kl\u00e4gerin ..."
}
```

The `content` fields holds the original HTML content of the court decision. The `markdown_content` is the HTML content converted to the Markdown format.

## Discord

> [!NOTE]  
> We're back! This project is getting a fresh update - join us on [Discord](https://discord.gg/WCy3aq25ZF) to help revive it.

## Citation

If you use this data, please cite our [research paper](https://arxiv.org/abs/2005.13342):

```bibtex
@inproceedings{10.1145/3383583.3398616,
author = {Ostendorff, Malte and Blume, Till and Ostendorff, Saskia},
title = {Towards an Open Platform for Legal Information},
year = {2020},
isbn = {9781450375856},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3383583.3398616},
doi = {10.1145/3383583.3398616},
booktitle = {Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020},
pages = {385–388},
numpages = {4},
keywords = {open data, open source, legal information system, legal data},
location = {Virtual Event, China},
series = {JCDL '20}
}
```

## License

In Germany, acts, statutory instruments, official decrees and official notices, as well as decisions (including court decisions) and official head notes of decisions do not enjoy copyright protection (UrhG § 5).

The collection and metadata has the Open Database License (ODbL) v1.0.