---
pretty_name: DBpediaOntoTrain
license: cc-by-4.0
language:
- en
tags:
- ontology
- owl
- turtle
- llm
- pretraining
- dbpedia
size_categories:
- 1B<n<10B
dataset_info:
  features:
  - name: file_name
    type: string
  - name: text
    type: string
  - name: PD
    type: float
  - name: NTR
    type: float
  - name: SC
    type: float
  - name: PD_norm
    type: float
  - name: NTR_norm
    type: float
  - name: SC_norm
    type: float
  - name: QS
    type: float
  - name: token_count
    type: int
  - name: token_count_acum
    type: int
  - name: percent_token_acum
    type: float
---


# 🧠 DBpediaOntoTrain: A Quality-Segmented Ontology Dataset for LLM Pretraining

## 📘 Overview

**DBpediaOntoTrain** is a dataset of **1,766 OWL ontologies in Turtle format**, extracted from [DBpedia Archivo](https://archivo.dbpedia.org/) and prepared for **continual pretraining of Large Language Models (LLMs)** in ontology generation and completion tasks.

Each ontology is analyzed using a set of **semantic quality metrics**, tokenized using the **LLaMA 3.2 tokenizer**, and sorted by **Quality Score (QS)**. The dataset includes **cumulative token counts and percentages**, allowing precise and reproducible slicing for quality-aware training.

---

## 📦 Dataset Contents

- `data.json`: A JSON file where each entry contains:
  - `File Name`: name of the ontology file (`.ttl`)
  - `Text`: raw ontology content in Turtle syntax
  - `PD`: Property Density by Class
  - `NTR`: Non-Taxonomic Relations per Class
  - `SC`: Subclasses per Class
  - `PD_norm`, `NTR_norm`, `SC_norm`: min-max normalized versions of the above metrics
  - `QS`: Quality Score (`PD_norm + NTR_norm + SC_norm`)
  - `Token Count`: number of tokens computed using the **LLaMA 3.2 tokenizer**
  - `Token Count Accumulation`: cumulative token count (sorted by descending QS)
  - `Percentage of Token Count Accumulation`: running percentage of total tokens across all ontologies

The dataset is sorted in descending order by Quality Score (`QS`), enabling easy extraction of quality-based subsets (e.g., Q1, Q1,2, etc.).

---

## 📊 Quality Metrics

Each ontology is scored with:

| Metric | Description |
|--------|-------------|
| **PD** | Property Density — properties per class |
| **NTR** | Non-Taxonomic Relations — domain-specific relations per class |
| **SC** | Subclass Count — hierarchical depth |
| **QS** | Sum of normalized PD, NTR, SC |

These metrics reflect **semantic modeling richness** rather than raw size.

---

## 🧪 Intended Use

- Continual pretraining of LLMs on semantic data
- Research in ontology learning, alignment, enrichment
- Studying the effect of data quality on model generalization and reasoning

This dataset supports the research study:

> **Enhancing LLM Ontology Generation: The Role of Quality Semantic Data**  
> Miquel Canal-Esteve, Yoan Gutiérrez, José Abreu-Salas (submitted to *ICT Express*, 2025)

---

## 🛠️ Tokenization

- Tokenized using **LLaMA 3.2-1B tokenizer**
- Total tokens: **1.25 billion**
- Cumulative token fields allow extracting top-N% token subsets based on QS
- Token overlap and LLM input chunking are described in the accompanying paper

---

## 💡 Reproducibility

The repository includes:
- Metric calculation scripts using [`rdflib`](https://github.com/RDFLib/rdflib)
- Tokenization scripts with Hugging Face libraries
- Pretraining configs and logs

Repository:  
👉 [https://github.com/miquelcanalesteve/LLM4Onto/](https://github.com/miquelcanalesteve/LLM4Onto/)

---

## 📄 Citation

```bibtex
@misc{canal2025dbpediaontotrain,
  author    = {Miquel Canal-Esteve and Yoan Gutiérrez and José Abreu-Salas},
  title     = {DBpediaOntoTrain: A Quality-Segmented Ontology Dataset for LLM Pretraining},
  year      = {2025},
  url       = {https://github.com/miquelcanalesteve/LLM4Onto/}
}
