---
pretty_name: merged-tool-use
tags:
- tool-calling
- function-calling
- chat
- jsonl
- parquet
- openai-format
size_categories:
- 100K<n<1M
task_categories:
- text-generation
language:
- en
---

# merged-tool-use

High-quality, multi-source dataset normalized to a single, OpenAI-style tool-calling schema. Built by unifying multiple public datasets into one consolidated corpus ready for training and evaluation.

- Total examples: 220,247
- Formats: Parquet and JSONL
- Schema: `messages: list[message]` where each `message` has `role`, optional `content`, and optional `tool_calls`/`function` fields.

## Contents

This dataset merges and normalizes the following sources:

- [minpeter/toolace-parsed](https://huggingface.co/datasets/minpeter/toolace-parsed)
- [microsoft/Taskbench](https://huggingface.co/datasets/microsoft/Taskbench) (config: `huggingface`)
- [hypervariance/function-calling-sharegpt](https://huggingface.co/datasets/hypervariance/function-calling-sharegpt)
- [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1)
- [glaiveai/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2)

Each source is normalized into the same conversation format and concatenated, then deterministically shuffled.

## Schema

Top-level record:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {
          "type": "function",
          "function": {
            "name": "function_name",
            "arguments": "{\"arg\": \"value\"}"
          }
        }
      ]
    },
    {"role": "function", "name": "function_name", "content": "... tool output ..."},
    {"role": "assistant", "content": "final answer ..."}
  ]
}
```

- `tool_calls[].function.arguments` is a JSON-serialized string per the OpenAI format.
- `function` messages contain `name` and textual `content` (tool result).

## Quickstart

Load locally using either Parquet or JSONL.

```python
from datasets import Dataset, load_dataset

# Parquet (fastest)
ds = Dataset.from_parquet("toolcall_unified.parquet")

# JSONL (equivalent)
ds_jsonl = load_dataset("json", data_files="toolcall_unified.jsonl", split="train")

print(ds)
print(ds[0]["messages"][0])  # first system message
```

Example to iterate tool-calls:

```python
def extract_calls(example):
    calls = []
    for msg in example["messages"]:
        if msg.get("tool_calls"):
            for c in msg["tool_calls"]:
                if c.get("type") == "function":
                    calls.append(c["function"]["name"])
    return {"function_names": calls}

calls = ds.map(extract_calls)
```

## Design Notes

- Normalizes varied upstream formats (inline `<functioncall>` tags, JSON-encoded fields, multi-line transcripts) into a single consistent schema.
- Preserves assistant tool-call intent and tool execution results when available.
- Avoids lossy transformations; arguments are retained as provided by sources and serialized into the canonical field.

## Provenance & Licensing

This dataset aggregates multiple public datasets. Licensing and usage terms are governed by the respective upstream datasets. Please consult the source cards linked above before using this dataset in commercial or research contexts. If re-publishing, attribute the original datasets accordingly.


## Reproducibility

Built with the included `unify_toolcall_datasets.py` script using a deterministic shuffle. To regenerate locally:

```bash
python unify_toolcall_datasets.py --out_dir ./unified --seed 42
```

## Acknowledgements

Huge thanks to the creators of the upstream datasets and the Hugging Face community.


