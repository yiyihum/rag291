---
tags:
- low-resource-languages
- instruction-tuning
- zarma
- Bambara
- Fulfulde
configs:
- config_name: ZarmaInstruct-50k
  data_files:
  - dje_50k/dje_50k.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Zarma
      type: string
    - name: resp_lrl
      description: Response in Zarma
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Zarma
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
- config_name: BambaraInstruct-50k
  data_files:
  - bm_50k/bm_50k.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Bambara
      type: string
    - name: resp_lrl
      description: Response in Bambara
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Bambara
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
- config_name: Fulfulde-50k
  data_files:
  - ff_50k/ff_50k.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Bambara
      type: string
    - name: resp_lrl
      description: Response in Bambara
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Bambara
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
- config_name: ZarmaFull
  data_files:
  - dje/dje.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Bambara
      type: string
    - name: resp_lrl
      description: Response in Bambara
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Bambara
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
- config_name: BambaraFull
  data_files:
  - bm/bm.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Bambara
      type: string
    - name: resp_lrl
      description: Response in Bambara
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Bambara
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
- config_name: FulfuldeFull
  data_files:
  - ff/ff.jsonl
  dataset_info:
    features:
    - name: instr_fr
      description: Original French instruction
      type: string
    - name: instr_lrl
      description: Translated instruction in Bambara
      type: string
    - name: resp_lrl
      description: Response in Bambara
      type: string
    - name: CoT_lrl
      description: Chain of Thought reasoning in Bambara
      type: string
    - name: topic_fr
      description: Topic name in French
      type: string
    - name: lang
      description: Language code
      type: string
    splits:
    - name: train
license: cc-by-4.0
language:
- bm
- dje
- ff
---


# InstructLR_Generate_Datasets

## Description
This dataset collection, generated using the **InstructLR** framework, provides high-quality instruction-response pairs for low-resource languages (LRLs), specifically Zarma and Bambara. The primary dataset, **ZarmaInstruct-5k**, contains 5,000 instruction-response pairs across 20 domains, designed to support instruction tuning for large language models (LLMs) in Zarma, a West African language. An experimental dataset, **BambaraInstruct-1k**, includes 1,000 pairs in Bambara. The datasets were created with a dual-layer quality pipeline involving automated RAG-based checks and human validation to ensure fluency and accuracy.

## Dataset Details
- **ZarmaInstruct-50k**: 50,000 instruction-response pairs in Zarma, covering domains such as General Knowledge, Mathematics, Biology, and more. Includes chain-of-thought (CoT) explanations for reasoning tasks.
- **BambaraInstruct-50k**: 50,000 instruction-response pairs in Bambara.
- **FulfuldeInstruct-50k**: 50,000 instruction-response pairs in Fulfulde.
- **Source Language**: French (used for seed instructions).
- **Quality Control**: Combines automated Retrieval-Augmented Generation (RAG) checks with human validation by native speakers.
- **Format**: JSONL, with fields: `instr_fr`, `instr_lrl`, `resp_lrl`, `CoT_lrl`, `topic_fr`, and `lang`.

## Usage
Usage

The dataset is intended for instruction tuning of LLMs to enhance their capabilities in Zarma and other low-resource languages. It can be used for tasks such as **question answering**, **reasoning**, and **domain-specific knowledge transfer**.

```
{
  "instr_fr": "Explique la photosynthèse en termes simples",
  "instr_lrl": "Fangaa fotosintez no ga hin ka bay kaani ra",
  "resp_lrl": "Fotosintez no ga hin ka hayyan nda wayno...",
  "CoT_lrl": "N/A",
  "topic_fr": "Biologie",
  "lang": "dje",
}
```
