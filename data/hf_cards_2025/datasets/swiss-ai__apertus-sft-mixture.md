---
task_categories:
- text-generation
language:
- en
- fr
- de
- it
- rm
tags:
- SFT
size_categories:
- 1M<n<10M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: conversation_id
    dtype: string
  - name: created_timestamp
    dtype: string
  - name: dataset_source
    dtype: string
  - name: original_metadata
    struct:
    - name: original_id
      dtype: int64
  - name: messages
    list:
    - name: content
      struct:
      - name: blocks
        list:
        - name: calls
          list:
          - name: arguments
            dtype: string
          - name: name
            dtype: string
        - name: outputs
          list:
          - name: name
            dtype: string
          - name: output
            dtype: string
        - name: text
          dtype: string
        - name: type
          dtype: string
      - name: formatted_tools
        dtype: string
      - name: has_thinking
        dtype: bool
      - name: parts
        list:
        - name: text
          dtype: string
        - name: type
          dtype: string
      - name: text
        dtype: string
      - name: tools
        dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 10993678588
    num_examples: 3942208
  download_size: 5061636770
  dataset_size: 10993678588
license: odc-by
---

# Apertus Supervised Finetuning Data

Our supervised finetuning data contains a carefully curated blend of instruction-following datasets, 
developed through eight iterations of empirical evaluation. This final mixture comprises approximately 
3.8 million examples from diverse sources, balancing generalinstruction-following, mathematical reasoning, 
code generation, and multilingual capabilities. 

More details about data provenance, preparation, and statistics can be found in our [tech report](https://github.com/swiss-ai/apertus-tech-report).

Sampling, filtering and data-preparation scripts can be found in [our dedicated GitHub repository](https://github.com/swiss-ai/posttrain-data).

Feel free to [reach out](mailto:sven.najem-meyer@epfl.ch) for any questions or suggestions 😊