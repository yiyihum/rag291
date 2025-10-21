---
license: cc-by-sa-4.0
task_categories:
- text-generation
- fill-mask
task_ids:
- language-modeling
- masked-language-modeling
configs:
- config_name: default
  data_files:
  - split: train
    path: 20250320/*parquet/*parquet
- config_name: ar
  data_files:
  - split: train
    path: 20250320/arw*parquet/*parquet
- config_name: br
  data_files:
  - split: train
    path: 20250320/brw*parquet/*parquet
- config_name: ca
  data_files:
  - split: train
    path: 20250320/caw*parquet/*parquet
- config_name: co
  data_files:
  - split: train
    path: 20250320/cow*parquet/*parquet
- config_name: de
  data_files:
  - split: train
    path: 20250320/dew*parquet/*parquet
- config_name: en
  data_files:
  - split: train
    path: 20250320/enw*parquet/*parquet
- config_name: es
  data_files:
  - split: train
    path: 20250320/esw*parquet/*parquet
- config_name: eu
  data_files:
  - split: train
    path: 20250320/euw*parquet/*parquet
- config_name: fr
  data_files:
  - split: train
    path: 20250320/frw*parquet/*parquet
- config_name: frp
  data_files:
  - split: train
    path: 20250320/frpw*parquet/*parquet
- config_name: it
  data_files:
  - split: train
    path: 20250320/itw*parquet/*parquet
- config_name: nl
  data_files:
  - split: train
    path: 20250320/nlw*parquet/*parquet
- config_name: oc
  data_files:
  - split: train
    path: 20250320/ocw*parquet/*parquet
- config_name: pcd
  data_files:
  - split: train
    path: 20250320/pcdw*parquet/*parquet
- config_name: pt
  data_files:
  - split: train
    path: 20250320/ptw*parquet/*parquet
language:
- en
- fr
- de
- es
- it
- nl
- pt
- ca
- ar
- eu
- br
- oc
- co
- pcd
- frp
---

# Dataset Card

This dataset is a curated collection of Wikimedia pages in markdown format,
compiled from various Wikimedia projects across multiple languages.

**Covered Wikimedia Projects:**
* wikipedia
* wikibooks
* wikinews
* wikiquote
* wikisource
* wikiversity
* wikivoyage
* wiktionary

**Supported Languages:**
* ar (Arabic)
* br (Breton)
* ca (Catalan)
* co (Corsican)
* de (German)
* en (English)
* es (Spanish)
* eu (Basque)
* fr (French)
* frp (Arpitan)
* it (Italian)
* nl (Dutch)
* oc (Occitan)
* pcd (Picard)
* pt (Portuguese)

## Data Source

The content was extracted from the  [Wikimedia dumps](https://dumps.wikimedia.org/other/enterprise_html/runs),
specifically from the dump dated March 20, 2025 (20250320).

The extraction process follows the same methodology as the one used in the [OpenLLM-France/wikipedia](https://huggingface.co/datasets/OpenLLM-France/wikipedia).

## Dataset Size

The tables below provide a detailed overview of the dataset size, organized by language:

| language | # pages | # words | # characters |
|----------|----------|-----------|-----------|
| en (English) | 16.46 M | 6.93 B | 39.97 B |
| fr (French) | 9.66 M | 3.07 B | 18.00 B |
| de (German) | 4.56 M | 2.21 B | 14.83 B |
| es (Spanish) | 3.06 M | 1.56 B | 9.07 B |
| it (Italian) | 2.75 M | 1.48 B | 8.86 B |
| nl (Dutch) | 3.16 M | 734.36 M | 4.40 B |
| pt (Portuguese) | 1.76 M | 710.99 M | 4.06 B |
| ca (Catalan) | 1.44 M | 564.51 M | 3.33 B |
| ar (Arabic) | 1.46 M | 562.65 M | 3.22 B |
| eu (Basque) | 511.70 K | 124.81 M | 882.24 M |
| br (Breton) | 148.47 K | 37.92 M | 206.85 M |
| oc (Occitan) | 160.15 K | 35.94 M | 202.87 M |
| co (Corsican) | 17.85 K | 2.64 M | 15.59 M |
| pcd (Picard) | 6.04 K | 1.59 M | 8.92 M |
| frp (Arpitan) | 5.79 K | 873.34 K | 4.97 M |
| **TOTAL** | 45.16 M | 18.03 B | 107.07 B |


The tables below provide a detailed overview of the dataset size, organized by language and Wikimedia project:

| language | domain | # pages | # words | # characters |
|----------|--------|----------|-----------|-----------|
| ar | wikipedia | 1.29 M | 448.80 M | 2.60 B |
| ar | wikibooks | 1.14 K | 1.12 M | 6.48 M |
| ar | wikinews | 9.55 K | 3.51 M | 21.15 M |
| ar | wikiquote | 4.05 K | 1.44 M | 8.49 M |
| ar | wikisource | 79.05 K | 105.56 M | 569.20 M |
| ar | wikiversity | 943 | 459.03 K | 2.74 M |
| ar | wiktionary | 71.95 K | 1.76 M | 11.96 M |
| br | wikipedia | 87.91 K | 19.30 M | 108.62 M |
| br | wikiquote | 171 | 194.98 K | 1.06 M |
| br | wikisource | 8.28 K | 14.27 M | 73.10 M |
| br | wiktionary | 52.12 K | 4.16 M | 24.06 M |
| ca | wikipedia | 808.82 K | 519.77 M | 3.04 B |
| ca | wikibooks | 2.91 K | 1.94 M | 11.81 M |
| ca | wikinews | 4.88 K | 2.65 M | 10.47 M |
| ca | wikiquote | 4.12 K | 1.62 M | 9.55 M |
| ca | wikisource | 4.65 K | 7.99 M | 43.16 M |
| ca | wiktionary | 619.56 K | 30.53 M | 211.58 M |
| co | wikipedia | 8.32 K | 2.40 M | 14.02 M |
| co | wiktionary | 9.54 K | 243.04 K | 1.57 M |
| de | wikipedia | 3.04 M | 1.78 B | 11.79 B |
| de | wikibooks | 10.75 K | 12.13 M | 82.44 M |
| de | wikinews | 14.32 K | 4.23 M | 31.46 M |
| de | wikiquote | 8.00 K | 2.29 M | 14.61 M |
| de | wikisource | 264.20 K | 279.29 M | 1.82 B |
| de | wikiversity | 47.34 K | 4.18 M | 34.88 M |
| de | wikivoyage | 20.71 K | 21.79 M | 154.83 M |
| de | wiktionary | 1.15 M | 113.33 M | 906.85 M |
| en | wikipedia | 7.14 M | 5.11 B | 29.00 B |
| en | wikibooks | 86.51 K | 111.09 M | 661.77 M |
| en | wikinews | 22.41 K | 9.83 M | 58.96 M |
| en | wikiquote | 58.10 K | 90.33 M | 522.59 M |
| en | wikisource | 617.50 K | 1.05 B | 6.02 B |
| en | wikiversity | 47.58 K | 35.78 M | 225.45 M |
| en | wikivoyage | 34.05 K | 50.32 M | 306.01 M |
| en | wiktionary | 8.46 M | 472.32 M | 3.18 B |
| es | wikipedia | 2.03 M | 1.38 B | 7.97 B |
| es | wikibooks | 8.81 K | 8.74 M | 53.48 M |
| es | wikinews | 12.32 K | 4.47 M | 26.57 M |
| es | wikiquote | 8.67 K | 5.01 M | 29.62 M |
| es | wikisource | 51.76 K | 93.02 M | 541.36 M |
| es | wikiversity | 3.14 K | 3.61 M | 23.07 M |
| es | wikivoyage | 3.40 K | 8.74 M | 52.47 M |
| es | wiktionary | 939.35 K | 56.36 M | 374.12 M |
| eu | wikipedia | 452.95 K | 117.47 M | 826.58 M |
| eu | wikibooks | 2.20 K | 564.08 K | 4.23 M |
| eu | wikiquote | 370 | 90.20 K | 654.51 K |
| eu | wikisource | 1.24 K | 3.61 M | 26.83 M |
| eu | wiktionary | 54.94 K | 3.08 M | 23.94 M |
| frp | wikipedia | 5.79 K | 873.34 K | 4.97 M |
| fr | wikipedia | 2.77 M | 1.89 B | 10.90 B |
| fr | wikibooks | 23.74 K | 26.79 M | 161.96 M |
| fr | wikinews | 24.26 K | 12.03 M | 63.53 M |
| fr | wikiquote | 9.80 K | 4.09 M | 24.63 M |
| fr | wikisource | 316.03 K | 844.05 M | 4.95 B |
| fr | wikiversity | 17.69 K | 10.26 M | 70.43 M |
| fr | wikivoyage | 9.45 K | 11.04 M | 67.16 M |
| fr | wiktionary | 6.48 M | 267.14 M | 1.76 B |
| it | wikipedia | 1.97 M | 1.19 B | 6.96 B |
| it | wikibooks | 18.24 K | 40.78 M | 301.79 M |
| it | wikinews | 12.23 K | 4.36 M | 25.64 M |
| it | wikiquote | 53.55 K | 38.63 M | 234.14 M |
| it | wikisource | 101.73 K | 157.49 M | 1.00 B |
| it | wikiversity | 5.44 K | 6.43 M | 42.38 M |
| it | wikivoyage | 12.83 K | 18.00 M | 115.42 M |
| it | wiktionary | 575.73 K | 25.09 M | 180.32 M |
| nl | wikipedia | 2.20 M | 650.71 M | 3.83 B |
| nl | wikibooks | 10.39 K | 5.95 M | 37.40 M |
| nl | wikinews | 4.82 K | 1.94 M | 12.38 M |
| nl | wikiquote | 1.26 K | 567.74 K | 3.50 M |
| nl | wikisource | 14.20 K | 13.69 M | 84.50 M |
| nl | wikivoyage | 4.22 K | 2.12 M | 13.47 M |
| nl | wiktionary | 922.49 K | 59.39 M | 421.34 M |
| oc | wikipedia | 87.87 K | 30.29 M | 165.44 M |
| oc | wikibooks | 67 | 22.36 K | 127.57 K |
| oc | wiktionary | 72.21 K | 5.63 M | 37.30 M |
| pcd | wikipedia | 6.04 K | 1.59 M | 8.92 M |
| pt | wikipedia | 1.17 M | 617.13 M | 3.52 B |
| pt | wikibooks | 11.74 K | 7.87 M | 49.26 M |
| pt | wikinews | 34.54 K | 16.16 M | 91.11 M |
| pt | wikiquote | 11.36 K | 3.13 M | 18.63 M |
| pt | wikisource | 31.04 K | 26.91 M | 158.31 M |
| pt | wikiversity | 4.43 K | 3.27 M | 20.79 M |
| pt | wikivoyage | 4.04 K | 3.93 M | 23.77 M |
| pt | wiktionary | 496.48 K | 32.59 M | 184.28 M |

## Example use (python)

Load the full dataset:

```python
import datasets

ds = datasets.load_dataset("OpenLLM-France/wikimedia",
    streaming=True,
    split="train"
)
```

Load the dataset for a given language (French in this example):
```python
ds = datasets.load_dataset("OpenLLM-France/wikimedia", "fr",
    streaming=True,
    split="train"
)
```
