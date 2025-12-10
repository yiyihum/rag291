---
base_model: []
library_name: transformers
tags:
- mergekit
- merge
- unaligned
- not-for-all-audiences
---
# Sapphira-L3.3-70b-0.2

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66ca56e62400073af3ad2972/mgdoIkYo2Z8SkkOJKxw4T.png)

Storytelling and RP model similar to [BruhzWater/Sapphira-L3.3-70b-0.1](https://huggingface.co/BruhzWater/Sapphira-L3.3-70b-0.1), but a little spicier. 

I prefer the prose of this one over the original. It has a bit more of [BruhzWater/Serpents-Tongue-L3.3-70b-0.3](https://huggingface.co/BruhzWater/Serpents-Tongue-L3.3-70b-0.3), which consists of:

* [TheDrummer/Anubis-70B-v1.1](https://huggingface.co/TheDrummer/Anubis-70B-v1.1)
* [TheDrummer/Fallen-Llama-3.3-70B-v1](https://huggingface.co/TheDrummer/Fallen-Llama-3.3-70B-v1)
* [Sao10K/L3.1-70B-Hanami-x1](https://huggingface.co/Sao10K/L3.1-70B-Hanami-x1)
* [Sao10K/70B-L3.3-mhnnn-x1](https://huggingface.co/Sao10K/70B-L3.3-mhnnn-x1)
* [Ppoyaa/MythoNemo-L3.1-70B-v1.0](https://huggingface.co/Ppoyaa/MythoNemo-L3.1-70B-v1.0)
* [BruhzWater/Eden-L3.3-70b-0.3](https://huggingface.co/BruhzWater/Eden-L3.3-70b-0.3)


Static quants: https://huggingface.co/mradermacher/Sapphira-L3.3-70b-0.2-GGUF

iMatrix quants: https://huggingface.co/mradermacher/Sapphira-L3.3-70b-0.2-i1-GGUF

Chat Template:
-
Llama3

Instruction Template:
-
Deep Cogito

Llama3

Sampler Settings
-

Starter:
```
Temp: 1
Min_P: 0.02
Top_P: 1
```

Experimental 1:
```
Temp: .95 - 1.1
Min_P: .015 - .03
Top_P: .97 - 1
XTC_Threshold: .11
XTC_Probability: .15
```

Experimental 2:
```
Temp: .95 - 1.1
Min_P: .015 - .03
Top_P: 1
Typical_P: .99
XTC_Threshold: .11
XTC_Probability: .15
```

## Merge Method

This model was merged using the [Multi-SLERP](https://goddard.blog/posts/multislerp-wow-what-a-cool-idea) merge method using [deepcogito/cogito-v2-preview-llama-70B](https://huggingface.co/deepcogito/cogito-v2-preview-llama-70B).
### Models Merged

The following models were included in the merge:
* [BruhzWater/Serpents-Tongue-L3.3-70b-0.3](https://huggingface.co/BruhzWater/Serpents-Tongue-L3.3-70b-0.3)
* [BruhzWater/Apocrypha-L3.3-70b-0.3](https://huggingface.co/BruhzWater/Apocrypha-L3.3-70b-0.3)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: /workspace/cache/models--BruhzWater--Apocrypha-L3.3-70b-0.3/snapshots/3facb4c0a7b953ff34a5caa90976830bf82a84c2
    parameters:
      weight: [0.5]
  - model: /workspace/cache/models--BruhzWater--Serpents-Tongue-L3.3-70b-0.3/snapshots/d007a7bcc7047d712abb2dfb6ad940fe03cd2047
    parameters:
      weight: [0.7]
base_model: /workspace/cache/models--deepcogito--cogito-v2-preview-llama-70B/snapshots/1e1d12e8eaebd6084a8dcf45ecdeaa2f4b8879ce
merge_method: multislerp
tokenizer:
  source: base
chat_template: llama3
parameters:
  normalize_weights: false
  eps: 1e-8
pad_to_multiple_of: 8
int8_mask: true
dtype: bfloat16
```
