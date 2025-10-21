---
base_model:
- darkc0de/XortronCriminalComputingConfig
- Entropicengine/DarkTriad-24b
- Entropicengine/Trifecta-Max-24b
library_name: transformers
tags:
- mergekit
- merge
---
# Pinecone-Sage-24b

![image/png](https://huggingface.co/Entropicengine/Pinecone-sage-24b/resolve/main/pinecone-sage.png)

# 🌲Pinecone Series
The Pinecone Series is a collection of thoughtfully crafted model merges, combining the strengths of the best models among my personal favourites. 
Each version is curated to excel in roleplay, general knowledge, intelligence, and rich creative writing, 
while preserving the unique capabilities of its underlying models.


| Version            | Params | Strengths                                              |
| ------------------ | ------ | ------------------------------------------------------ |
| Pinecone-Rune  | 12B    | Fast, lightweight, surprisingly capable for its size   |
| **Pinecone-Sage**  | 24B    | Balanced speed and performance, rich prose and RP                    |
| Pinecone-Titan | 70B    | Rich prose, better long context capabilities, top-tier roleplay & knowledge |

# Recommended ST preset for RP : 

- [Sphiratrioth](https://huggingface.co/sphiratrioth666/SillyTavern-Presets-Sphiratrioth)

# ☕ Support My Work  
If you like my work, consider [buying me a coffee](https://ko-fi.com/entropicengine) to support future merges, GPU time, and experiments.


This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [darkc0de/XortronCriminalComputingConfig](https://huggingface.co/darkc0de/XortronCriminalComputingConfig) as a base.

### Models Merged

The following models were included in the merge:
* [Entropicengine/DarkTriad-24b](https://huggingface.co/Entropicengine/DarkTriad-24b)
* [Entropicengine/Trifecta-Max-24b](https://huggingface.co/Entropicengine/Trifecta-Max-24b)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: darkc0de/XortronCriminalComputingConfig
chat_template: auto
merge_method: dare_ties
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 40]
        model: Entropicengine/DarkTriad-24b
        parameters:
          density: 0.5
          weight: 0.3
      - layer_range: [0, 40]
        model: darkc0de/XortronCriminalComputingConfig
        parameters:
          density: 0.8
          weight: 0.8
      - layer_range: [0, 40]
        model: Entropicengine/Trifecta-Max-24b
        parameters:
          density: 0.5
          weight: 0.1
out_dtype: bfloat16
tokenizer: {}
```
