---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: idx
    dtype: int64
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: chosen_eval
    struct:
    - name: length_avg
      dtype: float64
    - name: llm_rw_avg
      dtype: float64
    - name: llm_rw_std
      dtype: float64
    - name: reward
      dtype: float64
    - name: reward_std
      dtype: float64
    - name: rs
      struct:
      - name: '0'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
      - name: '1'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
      - name: '2'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
    - name: task_metric_avg
      dtype: float64
    - name: task_metric_std
      dtype: float64
    - name: token_cost_avg
      dtype: float64
    - name: token_cost_std
      dtype: float64
  - name: rejected_eval
    struct:
    - name: length_avg
      dtype: float64
    - name: llm_rw_avg
      dtype: float64
    - name: llm_rw_std
      dtype: float64
    - name: reward
      dtype: float64
    - name: reward_std
      dtype: float64
    - name: rs
      struct:
      - name: '0'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
      - name: '1'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
      - name: '2'
        struct:
        - name: accuracy
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: average_score
          dtype: float64
        - name: forward_chat
          list:
          - name: content
            dtype: string
          - name: role
            dtype: string
        - name: information_gain
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
        - name: interactivity
          struct:
          - name: score
            dtype: float64
          - name: thought
            dtype: string
    - name: task_metric_avg
      dtype: float64
    - name: task_metric_std
      dtype: float64
    - name: token_cost_avg
      dtype: float64
    - name: token_cost_std
      dtype: float64
  - name: metadata
    struct:
    - name: assistant
      dtype: string
    - name: user
      dtype: string
  - name: prompt_item
    dtype: string
  splits:
  - name: train
    num_bytes: 33351808
    num_examples: 3990
  - name: test
    num_bytes: 14292090
    num_examples: 1711
  download_size: 11418818
  dataset_size: 47643898
tags:
- rlhf
- multiturn
- collabllm
---
