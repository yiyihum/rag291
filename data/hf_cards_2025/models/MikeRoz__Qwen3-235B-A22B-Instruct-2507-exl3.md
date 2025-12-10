---
library_name: exllamav3
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507/blob/main/LICENSE
pipeline_tag: text-generation
base_model: Qwen/Qwen3-235B-A22B-Instruct-2507
base_model_relation: quantized
tags:
- exl3
---

Exllamav3 quantization of [Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507)

[2.25 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/2.25bpw_H6) 63.377 GiB    
[2.85 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/2.85bpw_H6) 79.714 GiB    
[3.00 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/3.00bpw_H6) 83.800 GiB    
[3.20 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/3.20bpw_H6) 89.177 GiB   
[3.60 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/3.60bpw_H6) 100.125 GiB    
[4.00 bpw h6](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3/tree/4.00bpw_H6) 111.013 GiB    

* The 2.25 bpw quant will fit in three 24 GB cards with 20k tokens of fp16 context.    
* The 2.85 bpw quant will fit in four 24 GB cards with 40k tokens of fp16 context.
* The 3.60 bpw quant will fit in five 24 GB cards with 57k tokens of fp16 context.
* The 4.00 bpw quant will fit in six 24 GB cards with 81,920 tokens of fp16 context.
* The 3.20 bpw quant would not load at all on four 24 GB cards. I could only get the 3.00 to load with 4096 of q8 cache. These two are probably best left to five-card setups and above (or 96 GB on fewer cards).
* Note that all these numbers are on the current version of exllamav3, which does not support tensor parallelism at this time. If you're reading this from a future where this feature has been implemented, or if you have larger cards, then you can probably do better than what I'm reporting here.
