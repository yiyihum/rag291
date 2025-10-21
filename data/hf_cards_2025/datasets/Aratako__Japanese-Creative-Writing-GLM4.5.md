---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 201818274.0
    num_examples: 8203
  download_size: 111399653
  dataset_size: 201818274.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- text-generation
language:
- ja
size_categories:
- 1K<n<10K
---

# Japanese-Creative-Writing-GLM4.5

## 概要

日本語の小説執筆タスクのデータセットである[Aratako/Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k)から一部の指示を抽出し、[zai-org/GLM-4.5](https://huggingface.co/zai-org/GLM-4.5)で応答を再生成した約8000件のデータセットです。

データセット中の一部データはNSFW表現を含みます。

## データの詳細

各データは以下のキーを含みます。

- `messages`: OpenAI messages形式の対話データ
- `instruction`: 指示プロンプト
- `output`: アシスタント応答

system promptは事前に用意した複数種類からランダムに選択されたものが設定されています。

## ライセンス

MITライセンスの元配布します。