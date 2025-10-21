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
- **input**: compact JSON string with features (technicals, macro, on-chain, text snippets, **30-day price history**)  
- **output**: compact JSON string with target(s)  
- **meta**: `{ "date": "YYYY-MM-DD" }`

## Key input features

Technicals:
- `asof_close`  
- `price_30d_ago` – close 30 days before as-of  
- `trail30_close_rel` – last 30 closes, scaled by as-of close (p/last − 1)  
- `trail30_logret` – last 29 daily log returns  
- `ret_1d`, `ret_7d`, `ret_30d`, `ma_5`, `ma_20`, `ma5_gt_ma20`, `rsi_14`, `vol_20_annualized`

Macro:
- `gold`, `oil`

On-chain:
- `hash_rate`, `difficulty`, `n_transactions`, `n_unique_addresses`, `fng`, `cbbi`,
  `market_cap`, `total_supply`, `est_tx_volume_usd`

Texts (truncated for token efficiency):
- `news_snippets`, `tweet_snippets`, `context_article`

## Targets

- **direction_cls**: UP (>+2%), FLAT (−2%..+2%), DOWN (<−2%) at t+10 (also returns `r10`).  
- **return_reg**: 10-day log return (`r10_log`).  
- **maxdd_cls**: next-10-day max drawdown bucket (`low`/`med`/`high`) with raw `maxdd`.

## Load

```python
from datasets import load_dataset
ds = load_dataset("tahamajs/bitcoin-sllm-instruct_v2")
print(ds)             # DatasetDict with train/validation/test
print(ds["train"][0]) # one example
````

## Notes

* Normalize numeric features at train time using **train** split stats only.
* Ensure you have rights to re-distribute underlying sources.
  