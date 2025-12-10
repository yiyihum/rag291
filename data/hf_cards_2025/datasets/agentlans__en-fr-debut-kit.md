---
language:
- en
- fr
configs:
- config_name: fineweb_10000
  data_files:
  - path:
    - fineweb_10000.jsonl.zst
    split: train
  default: true
- config_name: fineweb_50000
  data_files:
  - path:
    - fineweb_50000.jsonl.zst
    split: train
- config_name: alpaca
  data_files:
  - path:
    - alpaca_50000.jsonl.zst
    split: train
- config_name: orca_rlhf
  data_files:
  - path:
    - orca_rlhf_10000.jsonl.zst
    split: train
pretty_name: Début Kit
tags:
- chatbot
- bilingual
- english-french
- pretraining
- sft
- dpo
license: apache-2.0
task_categories:
- text-generation
---
# Début Kit

<details>
  <summary>English</summary>
A dataset for training English-French bilingual chatbots

## Overview

**Début Kit** is a comprehensive dataset designed to facilitate the development of English-French bilingual chatbots. It covers three crucial stages of model development:

1. Pretraining
2. Supervised Fine-Tuning (SFT)
3. Direct Preference Optimization (DPO)

Each stage features a balanced mix of English and French content, ensuring robust bilingual capabilities.

## Dataset Details

| **Stage** | **Files** | **Sources** | **Processing** |
|-----------|-----------|-------------|----------------|
| **Pretraining** | `fineweb_10000.jsonl`, `fineweb_50000.jsonl` | [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb), [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) (`fra_Latn` subset) | Semantic agglomerative clustering using [agentlans/multilingual-e5-small-aligned-v2](https://huggingface.co/agentlans/multilingual-e5-small-aligned-v2) embeddings |
| **SFT** | `alpaca_50000.jsonl` | [jpacifico/French-Alpaca-dataset-Instruct-110K](https://huggingface.co/datasets/jpacifico/French-Alpaca-dataset-Instruct-110K), [yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned) | Clustered into 50,000 rows using the same method as pretraining |
| **DPO** | `orca_rlhf_10000.jsonl` | [jpacifico/french-orca-dpo-pairs-revised](https://huggingface.co/datasets/jpacifico/french-orca-dpo-pairs-revised), [Intel/orca_dpo_pairs](https://huggingface.co/datasets/Intel/orca_dpo_pairs) | Clustered into 10,000 rows using [EuroBERT/EuroBERT-210m](https://huggingface.co/EuroBERT/EuroBERT-210m) |

## Licensing and Acknowledgements

- **Licensing:** Début Kit is released under the **Apache 2.0 Licence**.
- **Acknowledgements:** This dataset incorporates data from Hugging Face datasets, Jonathan Pacifico's contributions, and Intel Corporation.

## Intended Use

Début Kit is specifically designed for:
- Training bilingual chatbots
- Developing conversational AI models
- Supporting English-French language capabilities
</details>

<details>
  <summary>French</summary>
Jeu de données pour l'entraînement de chatbots bilingues anglais-français

## Présentation

**Début Kit** est un jeu de données complet conçu pour faciliter le développement de chatbots bilingues en anglais et en français. Il couvre trois étapes clés dans le développement d'un modèle :

1. Pré-entraînement
2. Réglage fin supervisé (SFT)
3. Optimisation directe des préférences (DPO)

Chaque étape comprend un mélange équilibré de contenu en anglais et en français, garantissant ainsi des capacités bilingues solides.

## Détails du jeu de données

| **Étape**                 | **Fichiers**                  | **Sources**                                                                                                 | **Traitement**                                                                                                     |
|---------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Pré-entraînement**       | `fineweb_10000.jsonl`, `fineweb_50000.jsonl` | [HuggingFaceFW/fineweb](https://huggingface.co/datasets/HuggingFaceFW/fineweb), [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) (sous-ensemble `fra_Latn`) | Regroupement sémantique agglomératif utilisant les intégrations [agentlans/multilingual-e5-small-aligned-v2](https://huggingface.co/agentlans/multilingual-e5-small-aligned-v2) |
| **SFT**                    | `alpaca_50000.jsonl`          | [jpacifico/French-Alpaca-dataset-Instruct-110K](https://huggingface.co/datasets/jpacifico/French-Alpaca-dataset-Instruct-110K), [yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned) | Regroupé en 50 000 lignes selon la même méthode que le pré-entraînement                                             |
| **DPO**                    | `orca_rlhf_10000.jsonl`       | [jpacifico/french-orca-dpo-pairs-revised](https://huggingface.co/datasets/jpacifico/french-orca-dpo-pairs-revised), [Intel/orca_dpo_pairs](https://huggingface.co/datasets/Intel/orca_dpo_pairs) | Regroupé en 10 000 lignes à l'aide de [EuroBERT/EuroBERT-210m](https://huggingface.co/EuroBERT/EuroBERT-210m) |

## Licences et remerciements

- **Licences :** Début Kit est publié sous la **licence Apache 2.0**.
- **Remerciements :** Cet ensemble de données intègre des données provenant des jeux de données Hugging Face, avec des contributions de Jonathan Pacifico et d'Intel Corporation.

## Utilisation prévue

Début Kit est spécialement conçu pour :

- L'entraînement de chatbots bilingues
- Le développement de modèles d'IA conversationnelle
- Le support des fonctionnalités linguistiques en anglais et en français
</details>