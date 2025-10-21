---
base_model:
- huihui-ai/Llama-3.3-70B-Instruct-abliterated
library_name: transformers
tags:
- mergekit
- merge
---
# Book_stock

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317d4867690c5b55e61ce3d/kZ-AKfpy8Vr6_iL3TwhSA.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6317d4867690c5b55e61ce3d/SpwLQucyItz8HnrZdwXt5.png)

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Model Stock](https://arxiv.org/abs/2403.19522) merge method using [huihui-ai/Llama-3.3-70B-Instruct-abliterated](https://huggingface.co/huihui-ai/Llama-3.3-70B-Instruct-abliterated) as a base.

### Models Merged

The following models were included in the merge:
* D:\mergekit\LORAs\applied\Book_RPv05
* D:\mergekit\LORAs\applied\Book_RPv15
* D:\mergekit\LORAs\applied\Book_RPvfinal
* D:\mergekit\LORAs\applied\Book_RPv1

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: "D:\\mergekit\\LORAs\\applied\\Book_RPv05"
  - model: "D:\\mergekit\\LORAs\\applied\\Book_RPv1"
  - model: "D:\\mergekit\\LORAs\\applied\\Book_RPv15"
  - model: "D:\\mergekit\\LORAs\\applied\\Book_RPvfinal"
  - model: huihui-ai/Llama-3.3-70B-Instruct-abliterated
base_model: huihui-ai/Llama-3.3-70B-Instruct-abliterated
merge_method: model_stock
dtype: float32
out_dtype: bfloat16
chat_template: llama3
tokenizer:
 source: union
```
