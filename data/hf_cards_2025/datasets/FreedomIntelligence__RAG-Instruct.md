---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- en
tags:
- RAG
configs:
- config_name: default
  data_files:
  - split: train
    path: rag_instruct.json
---
## Introduction
RAG-Instruct is a RAG dataset designed to comprehensively enhance LLM RAG capabilities, synthesized using GPT-4o. This dataset is based on the Wikipedia corpus and This dataset is based on the Wikipedia corpus and offers the advantages of query-document scenario diversity and task diversity.

The RAG-Instruct dataset can significantly enhance the RAG ability of LLMs and make remarkable improvements in RAG performance across various tasks.

| Model                          | WQA (acc) | PQA (acc) | TQA (acc) | OBQA (EM) | Pub (EM) | ARC (EM) | 2WIKI (acc) | HotP (acc) | MSQ (acc) | CFQA (EM) | PubMed (EM) |
|--------------------------------|-----------|-----------|-----------|-----------|----------|----------|-------------|------------|-----------|-----------|-------------|
| Llama3.2-3B                    | 58.7 | 61.8 | 69.7 |  77.0 | 55.0 | 66.8 | 55.6 | 40.2 | 13.2 | 46.8 | 70.3 |
| Llama3.1-8B                    | 59.5                      | 60.8                | 73.4               |  82.0                           | 56.7                    | 77.1                    | 65.6                 | 45.6           | 18.7            | 56.5                     | 73.9                    |
| Llama3.2-3B + RAG-Instruct     | 65.3                      | 64.0                | 77.0               |  81.2                           | 66.4                    | 73.0                    | 72.9                 | 52.7           | 25.0            | 50.3                     | 72.6                    |
| Llama3.1-8B + RAG-Instruct     | 69.7                      | 68.4                | 79.3               |  84.8                           | 77.2                    | 79.9                    | 79.3                 | 56.4           | 30.3            | 57.8                     | 77.0                    |

For details, see our [paper](https://arxiv.org/abs/2501.00353) and [GitHub repository](https://github.com/FreedomIntelligence/RAG-Instruct).




## Citation

If you find our data useful, please consider citing our work!
```
@misc{liu2024raginstructboostingllmsdiverse,
      title={RAG-Instruct: Boosting LLMs with Diverse Retrieval-Augmented Instructions}, 
      author={Wanlong Liu and Junying Chen and Ke Ji and Li Zhou and Wenyu Chen and Benyou Wang},
      year={2024},
      eprint={2501.00353},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00353}, 
}
```