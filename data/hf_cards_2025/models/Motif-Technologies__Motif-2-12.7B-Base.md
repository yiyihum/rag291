---
license: apache-2.0
language:
- en
- ko
tags:
- text-generation-inference
- conversational
- custom_code
- text-generation
- Motif
---

Last update: TBA

# Introduction

We announce **Motif-2-12.7B-Base**, a 12.7 billion parameter language model. Detailed information including technical report will be released later.

# Evaluation

All models listed in the table below are **base models**. *The results of Qwen3 and Gemma 3 are <U>sourced directly from their technical reports.</U>*

|Benchmark|Evaluation setting|Motif-2-12.7B|Qwen3-14B|Qwen3-32B|Qwen3-30B-A3B|Gemma-3-12B|Gemma-3-27B|
|---|---|---|---|---|---|---|---|
|MMLU|5-shot|78.1|81.05|83.61|81.38|74.5|78.6|
|MMLU-Redux|5-shot|78.68|79.88|83.41|81.17|-|-|
|MMLU-Pro|5-shot, CoT|66.38|61.03|65.54|61.49|45.3|52.2|
|SuperGPQA|5-shot, CoT|32.68|34.27|39.78|35.72|-|-|
|BBH|3-shot, CoT|81.34|81.07|87.38|81.54|-|-|
|GPQA|5-shot, CoT|42.18|39.9|49.49|43.94|-|-|
|GPQA-Diamond|5-shot, CoT|42.92|-|-|-|25.4|24.3|
|GSM8K|4-shot, CoT|93.85|92.49|93.4|91.81|-|-|
|GSM8K|8-shot, CoT|94.92|-|-|-|71|82.6|
|MATH|4-shot, CoT|73.62|62.02|61.62|59.04|43.3|50|
|EvalPlus|0-shot|72.22|72.23|72.05|71.45|-|-|
|MBPP|3-shot|81.5|73.4|78.2|74.4|60.4|65.6|
|CRUX-O|1-shot|63.1|68.6|72.5|67.2|-|-|
|HumanEval|0-shot|65.9|-|-|-|45.7|48.8|
|DROP|1-shot|69.9|-|-|-|72.2|77.2|
|HellaSwag|10-shot|84|-|-|-|84.2|85.6|
|BoolQ|0-shot|78.5|-|-|-|78.8|82.4|
|PIQA|0-shot|81.6|-|-|-|81.8|83.3|
|SIQA|0-shot|53.8|-|-|-|53.4|54.9|
|TriviaQA|5-shot|72.2|-|-|-|78.2|85.5|
|Natural Question|5-shot|29.6|-|-|-|31.4|36.1|
|ARC-C|25-shot|69.6|-|-|-|68.9|70.6|
|ARC-E|0-shot|84.1|-|-|-|88.3|89|
|WinoGrande|5-shot|79.6|-|-|-|74.3|78.8|
|BBH|few-shot|81.3|-|-|-|72.6|77.7|

## Averages and improvements of the corresponding benchmark scores:

### v.s. Gemma 3

||Motif-2-12.7B|Gemma-3-12B|Gemma-3-27B|
|---|---|---|---|
|**Average**|71.53|63.87|67.96|
|**Improvement**||+11.99%|+5.26%|

### v.s. Qwen3

||Motif-2-12.7B|Qwen3-14B|Qwen3-32B|Qwen3-30B-A3B|
|---|---|---|---|---|
|**Average**|69.42|67.81|71.54|68.10|
|**Improvement**||+2.37%|-2.96%|+1.94%|