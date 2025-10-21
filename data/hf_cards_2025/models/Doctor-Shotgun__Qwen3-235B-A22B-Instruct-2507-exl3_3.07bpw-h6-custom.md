---
library_name: exllamav3
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-235B-A22B-Instruct-2507
---

# Qwen3-235B-A22B-Instruct-2507-exl3_3.07bpw-h6-custom

Exllamav3 quantization of [Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507).

This quantization uses manual recompilation to customize the bitrate of individual tensors in the mix, in a way inspired by [ubergarm](https://huggingface.co/ubergarm)'s work on large MoE models using GGUF. It relies on the finding that retaining higher precision in the attention and shared expert (this model does not have a shared expert) allows for reasonable quality to be maintained despite very aggressive quantization of the routed experts.

Specifically, we use 5bit for the attention tensors and 3bit for the routed experts to create an optimized mix intended to fit within 96gb of VRAM on a single headless RTX PRO 6000 with `PYTORCH_CUDA_ALLOC_CONF=backend:cudaMallocAsync`.

Quantized tensors are sourced from:
- [MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3](https://huggingface.co/MikeRoz/Qwen3-235B-A22B-Instruct-2507-exl3)
- [bullerwins/Qwen3-235B-A22B-Instruct-2507-exl3-5.0bpw](https://huggingface.co/bullerwins/Qwen3-235B-A22B-Instruct-2507-exl3-5.0bpw)

## Evaluation

Wikitext perplexity as evaluated by exllamav3's `eval/ppl.py`:

"Plain" exl3_3.0bpw-h6
```
 -- Bitrate: 3.02 bpw / 6.00 bpw (head)
 -- Evaluated: 100 rows of 2048 tokens
 -- Perplexity: 4.026279
```

exl3_3.07bpw-h6-custom
```
 -- Bitrate: 3.07 bpw / 6.00 bpw (head)
 -- Evaluated: 100 rows of 2048 tokens
 -- Perplexity: 3.935338
```

Additional metrics via `eval/model_diff.py` courtesy of [turboderp](https://huggingface.co/turboderp):

"Plain" exl3_3.0bpw-h6 vs original bf16 weights
```
 -- original perplexity:  1.76745635
 -- original label in top-K:
      K = 1: 0.8681
      K = 2: 0.9237
      K = 3: 0.9411
      K = 4: 0.9502
      K = 5: 0.9564
 -- 3.0bpw-h6 perplexity:  2.14967564
 -- 3.0bpw-h6 label in top-K:
      K = 1: 0.8142
      K = 2: 0.8949
      K = 3: 0.9231
      K = 4: 0.9368
      K = 5: 0.9464
 -- Top-K agreement, 3.0bpw-h6 vs original:
      K = 1: 0.8820
      K = 2: 0.5225
      K = 3: 0.2585
      K = 4: 0.1132
      K = 5: 0.0491
 -- KL divergence (3.0bpw-h6, original):  0.23334818
```

exl3_3.07bpw-h6-custom vs original bf16 weights
```
 -- original perplexity:  1.76745635
 -- original label in top-K:
      K = 1: 0.8681
      K = 2: 0.9237
      K = 3: 0.9411
      K = 4: 0.9502
      K = 5: 0.9564
 -- 3.07bpw-h6-custom perplexity:  2.03357968
 -- 3.07bpw-h6-custom label in top-K:
      K = 1: 0.8305
      K = 2: 0.9021
      K = 3: 0.9286
      K = 4: 0.9416
      K = 5: 0.9504
 -- Top-K agreement, 3.07bpw-h6-custom vs original:
      K = 1: 0.8981
      K = 2: 0.5702
      K = 3: 0.3027
      K = 4: 0.1461
      K = 5: 0.0691
 -- KL divergence (3.07bpw-h6-custom, original):  0.17770892
```