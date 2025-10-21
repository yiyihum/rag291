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
pretty_name: STXBP1 ClinVar Curated Variants
size_categories:
- 10M<n<100M
---

language:
  - en

---

# stxbp1_clinvar_curated

_ Curated STXBP1 and related variant records from ClinVar (24Million), ready for LLM and biomedical NLP applications._ 
>> Updated Jun 10th 2025. - Fields containing {null} or {} were removed.


## Dataset Overview

A curated, LLM-friendly dataset of **STXBP1 and related variant records from ClinVar**, converted from ClinVar VCF and annotated for clinical, research, rare disease, and advanced AI applications.  
This resource is suitable for medical language modeling, rare disease NLP, variant curation, and biomedical Q&A.  

**Formats included:**  
- Structured JSONL (main split)
- Q/A pairs (txt, 7,013,256 examples, 1.66 GB)
- Curated summaries (txt, 24,548,655 examples, 1.51 GB)
- Parquet conversion is recommended for large-scale use

---

## Curation Criteria

Variants were selected from ClinVar using the following inclusion keywords (case-insensitive):

- STXBP1
- MUNC18
- STXBP2
- STXBP3
- STXBP4
- STXBP5
- STXBP6
- syntaxin.binding
- CRISPR Cas9
- CRISPR Cas12
- encephalopathy
- SNARE

Any variant record containing one or more of these keywords (in gene symbols, molecular consequence, disease name, or database annotations) was included. This ensures comprehensive coverage of the STXBP gene family, SNARE-complex biology, CRISPR-mediated editing, and associated neurological disorders (notably epileptic encephalopathies).

---

## Features

- **Natural language clinical summaries for each variant**
- **Structured JSONL** (parquet-compatible) for easy data science/NLP use
- **Ready-to-use Q/A pairs** for instruction and LLM fine-tuning
- Full field coverage: variant position, gene, disease, clinical significance, HGVS description, database cross-links, review status, and more

---

## Dataset Statistics

| Format            | Size (bytes)   | Number of Examples/Lines |
|-------------------|---------------:|-------------------------:|
| QA (.txt)         | 1,664,122,880  | 7,013,256                |
| Curated summaries | 1,511,264,256  | 24,548,655               |
| JSONL             | 1,598,603,264  | 3,506,628                |

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
| significance           | Clinical significance (e.g., Pathogenic, Benign, Uncertain)   |
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

## Data Examples

**JSON record:**
```json
{
  "ID": "3385321",
  "chrom": "1",
  "pos": "66926",
  "ref": "AG",
  "alt": "A",
  "gene": "OR4F5",
  "disease": "Retinitis_pigmentosa",
  "significance": "Uncertain_significance",
  "hgvs": "NC_000001.11:g.66927del",
  "review": "criteria_provided, single_submitter",
  "molecular_consequence": "SO:0001627: intron_variant",
  "variant_type": "Deletion",
  "clndisdb": "Human_Phenotype_Ontology:HP:0000547,MONDO:MONDO:0019200,MeSH:D012174,MedGen:C0035334,OMIM:268000,OMIM:PS268000,Orphanet:791",
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

## Load the full dataset (Parquet, recommended)

```from datasets import load_dataset

# This will automatically use the Parquet shards
ds = load_dataset("YOURPATH/ClinVar-STXBP1-NLP-Dataset")

# Access examples
print(ds["train"][0])
```

## To force JSONL loading (if you prefer the original format):

```from datasets import load_dataset

# Specify data_files to point to JSONL file(s)
ds = load_dataset(
    "YOURPATH/ClinVar-STXBP1-NLP-Dataset",
    data_files="ClinVar-STXBP1-NLP-Dataset.jsonl",
    split="train"
)
print(ds[0])
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