---
pretty_name: Bitcoin SLLM Instruction Dataset
tags:
- bitcoin
- finance
- instruction-tuning
- sft
license: other
language:
- en
task_categories:
- time-series-forecasting
- text-classification
- tabular-regression
size_categories:
- 1K<n<10K
---

# Bitcoin SLLM Instruction Dataset

Daily BTC context transformed into instruction-tuning triples for small LMs.

## Schema

- **id**: unique example id  
- **task**: `direction_cls` | `return_reg` | `maxdd_cls`  
- **split**: `train` | `validation` | `test` (time-based)  
- **instruction**: natural-language task definition  
- **input**: compact JSON string with features (technicals, macro, on-chain, text snippets)  
- **output**: compact JSON string with target(s)  
- **meta**: `{ "date": "YYYY-MM-DD" }`

## Targets

- **direction_cls**: UP (>+2%), FLAT (−2%..+2%), DOWN (<−2%) at t+10; includes `r10`.  
- **return_reg**: 10-day log return `r10_log`.  
- **maxdd_cls**: next-10-day max drawdown bucket (`low`/`med`/`high`) with raw `maxdd`.

## Load

```python
from datasets import load_dataset
ds = load_dataset("tahamajs/bitcoin-sllm-instruct")
print(ds)             # DatasetDict with train/validation/test
print(ds["train"][0]) # one example
````

## Notes

* Text is truncated to short snippets to keep token usage low.
* Normalize numeric features at train time using **train** split stats only.
* Review licensing of underlying sources; this repo may be private.
  