---
license: pddl
task_categories:
- text-classification
- question-answering
- text2text-generation
language:
- en
tags:
- stxbp1
- clinvar
- genomics
- biomedical
- variant
- rare-disease
- neurology
- epilepsy
- nlp
- llm
- question-answering
- text-classification
- bioinformatics
- snare
- gene-editing
- crispr
- cas9
- open-data
- instruction-tuning
pretty_name: STXBP1 ClinVar Pathogenic Variants (Curated)
size_categories:
- 100K<n<1M
---

# stxbp1_clinvar_curated_pathogenic

_Curated set of **307,587 pathogenic and likely pathogenic** STXBP1 and related variants from ClinVar, ready for LLM, variant curation, and biomedical NLP applications._ 
>>> (Updated Jun 10th 2025. - Fields containing {null} or {} were removed.) <<<
>>> 

## Dataset Overview

A **hand-curated, LLM-friendly** dataset of 307,587 STXBP1 and family variants from ClinVar, filtered for clinical significance (`Pathogenic`, `Likely_pathogenic`).  
Ideal for medical language modeling, rare disease NLP, AI-powered variant curation, and biomedical Q&A.

**Formats included:**  
- Structured JSONL (`.jsonl`, main split)
- Q/A pairs (`.txt`, for demo/fine-tuning)
- Parquet conversion recommended for large-scale use

---

## Curation Criteria

Variants included here are:
- Annotated as **Pathogenic** or **Likely_pathogenic** in ClinVar
- Matching gene family:  
  - STXBP1, MUNC18, STXBP2, STXBP3, STXBP4, STXBP5, STXBP6
  - Related SNARE-complex/CRISPR/neurological disorder keywords

---

## Features

- **Natural language clinical summaries for each variant**
- **Structured JSONL** (parquet-compatible) for data science and NLP
- **Q/A pairs** for LLM training and evaluation
- Full coverage: variant, gene, disease, clinical significance, HGVS, database links, review status, and more

---

## Dataset Statistics

| Format    | Size (bytes)     | Number of Examples/Lines |
|-----------|-----------------:|-------------------------:|
| QA (.txt) |     163,561,472  |    615,174               |
| JSONL     |     157,364,224  |    307,587               |

_Main split for Hugging Face: JSONL format (see above for statistics)._

---

## Schema

| Field                  | Description                                                    |
|------------------------|----------------------------------------------------------------|
| ID                     | ClinVar Variation ID                                           |
| chrom                  | Chromosome                                                    |
| pos                    | Genomic position (GRCh38)                                     |
| ref                    | Reference allele                                              |
| alt                    | Alternate allele                                              |
| gene                   | Gene symbol                                                   |
| disease                | Disease/phenotype name                                        |
| significance           | Clinical significance (e.g., Pathogenic, Likely_pathogenic)   |
| hgvs                   | HGVS variant description                                      |
| review                 | ClinVar review status                                         |
| molecular_consequence  | Sequence Ontology + effect                                    |
| variant_type           | SNV, Insertion, Deletion, etc.                                |
| clndisdb               | Disease database links (OMIM, MedGen, etc.)                   |
| clndnincl              | Included variant disease name                                 |
| clndisdbincl           | Included variant disease database links                       |
| onc_fields             | Dict of oncogenicity fields                                   |
| sci_fields             | Dict of somatic clinical impact fields                        |
| incl_fields            | Dict of included fields (INCL)                                |

---

## Data Example

**JSON record:**
```json
{
  "ID": "3385321",
  "chrom": "1",
  "pos": "66926",
  "ref": "AG",
  "alt": "A",
  "gene": "STXBP1",
  "disease": "Developmental and epileptic encephalopathy, 4",
  "significance": "Pathogenic",
  "hgvs": "NC_000001.11:g.66927del",
  "review": "criteria_provided, single_submitter",
  "molecular_consequence": "SO:0001627: intron_variant",
  "variant_type": "Deletion",
  "clndisdb": "Human_Phenotype_Ontology:HP:0000547,MONDO:MONDO:0019200,MeSH:D012174,MedGen:C0035334,OMIM:268000",
  "clndnincl": null,
  "clndisdbincl": null,
  "onc_fields": {},
  "sci_fields": {},
  "incl_fields": {}
}
```


===================================================================================================================
## You can easily load this dataset using the 🤗 Datasets library.

The Hugging Face infrastructure will automatically use the efficient Parquet files by default, but you can also specify the JSONL if you prefer.

### Install dependencies (if needed):

```bash
pip install datasets
```

## Load the full dataset (JSONL, recommended)

```from datasets import load_dataset

ds = load_dataset("SkyWhal3/ClinVar-STXBP1-NLP-Dataset", data_files="ClinVar-STXBP1-NLP-Dataset.jsonl", split="train")
print(ds[0])
```

## Parquet conversion (for large scale)

```import pandas as pd

df = pd.read_json("ClinVar-STXBP1-NLP-Dataset.jsonl", lines=True)
df.to_parquet("ClinVar-STXBP1-NLP-Dataset.parquet")
```

## Other ways to use the data
   Load all Parquet shards with pandas

```import pandas as pd
import glob

# Load all Parquet shards in the train directory
parquet_files = glob.glob("default/train/*.parquet")
df = pd.concat([pd.read_parquet(pq) for pq in parquet_files], ignore_index=True)
print(df.shape)
print(df.head())
```

## Filter for a gene (e.g., STXBP1)

```df = pd.read_parquet("default/train/0000.parquet")
stxbp1_df = df[df["gene"] == "STXBP1"]
print(stxbp1_df.head())
```

## Randomly sample a subset

```sample = df.sample(n=5, random_state=42)
print(sample)
```

## Load with Polars (for high performance)

```import polars as pl

df = pl.read_parquet("default/train/0000.parquet")
print(df.head())
```

## Query with DuckDB (SQL-style)

```import duckdb

con = duckdb.connect()
df = con.execute("SELECT * FROM 'default/train/0000.parquet' WHERE gene='STXBP1' LIMIT 5").df()
print(df)
```

## Streaming mode with 🤗 Datasets

```ds = load_dataset("YOURPATH/ClinVar-STXBP1-NLP-Dataset", split="train", streaming=True)
for record in ds.take(5):
    print(record)
```


Created by Adam Freygang, A.K.A. SkyWhal3


---
**License:**  
This dataset is licensed under the ODC Public Domain Dedication and License (PDDL).  
To the extent possible under law, the author(s) have dedicated this data to the public domain worldwide by waiving all rights to the work under copyright law, including all related and neighboring rights, to the extent allowed by law.  
NO WARRANTY is provided.  
See [ODC-PDDL](https://opendatacommons.org/licenses/pddl/1-0/) for full legal text.