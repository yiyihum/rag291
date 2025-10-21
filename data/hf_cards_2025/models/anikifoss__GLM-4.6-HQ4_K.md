---
quantized_by: anikifoss
pipeline_tag: text-generation
base_model: zai-org/GLM-4.6
license: mit
base_model_relation: quantized
tags:
- conversational
---

# Model Card

High quality quantization of **GLM-4.6** without using imatrix.

# Run

## ik_llama.cpp

See [this detailed guide](https://github.com/ikawrakow/ik_llama.cpp/discussions/258) on how to setup ik_llama and how to make custom quants.

```
./build/bin/llama-server \
    --alias anikifoss/GLM-4.6-HQ4_K \
    --model /mnt/data/Models/anikifoss/GLM-4.6-HQ4_K/GLM-4.6-HQ4_K-00001-of-00005.gguf \
    --no-mmap -rtr \
    --temp 0.5 --top-k 0 --top-p 1.0 --min-p 0.1 \
    --ctx-size 58000 \
    -ctk q8_0 -ctv q8_0 \
    -fa \
    -fmoe \
    --n-gpu-layers 99 \
    --override-tensor exps=CPU \
    --parallel 1 \
    --threads 32 \
    --threads-batch 64 \
    --host 127.0.0.1 \
    --port 8090
```

## llama.cpp

```
./build/bin/llama-server \
    --alias anikifoss/GLM-4.6-HQ4_K \
    --model /mnt/data/Models/anikifoss/GLM-4.6-HQ4_K/GLM-4.6-HQ4_K-00001-of-00005.gguf \
    --temp 0.5 --top-k 0 --top-p 1.0 --min-p 0.1 \
    --ctx-size 56000 \
    -ctk q8_0 -ctv q8_0 \
    -fa on \
    --override-tensor exps=CPU \
    -ngl 99 \
    --jinja \
    --parallel 1 \
    --threads 32 \
    --threads-batch 64 \
    --host 127.0.0.1 \
    --port 8090
```

## Quantization Recipe
Quantized with [ik_llama](https://github.com/ikawrakow/ik_llama.cpp), but should work with any GGUF compatible inference framework.

```bash
#!/usr/bin/env bash

custom="
blk\.92\.nextn\.eh_proj\.weight=q8_0
blk\.92\.nextn\.enorm\.weight=f32
blk\.92\.nextn\.hnorm\.weight=f32
blk\.92\.nextn\.shared_head_norm\.weight=f32

blk\.[0-2]\.ffn_down\.weight=q8_0
blk\.[0-2]\.ffn_gate\.weight=q8_0
blk\.[0-2]\.ffn_up\.weight=q8_0

blk\.[0-9]\.attn_k\.bias=f32
blk\.[0-9]\.attn_k\.weight=q8_0
blk\.[0-9]\.attn_k_norm\.weight=f32
blk\.[0-9]\.attn_norm\.weight=f32
blk\.[0-9]\.attn_output\.weight=q8_0
blk\.[0-9]\.attn_q\.bias=f32
blk\.[0-9]\.attn_q\.weight=q8_0
blk\.[0-9]\.attn_q_norm\.weight=f32
blk\.[0-9]\.attn_v\.bias=f32
blk\.[0-9]\.attn_v\.weight=q8_0
blk\.[0-9]\.post_attention_norm\.weight=f32
blk\.[1-8][0-9]\.attn_k\.bias=f32
blk\.[1-8][0-9]\.attn_k\.weight=q8_0
blk\.[1-8][0-9]\.attn_k_norm\.weight=f32
blk\.[1-8][0-9]\.attn_norm\.weight=f32
blk\.[1-8][0-9]\.attn_output\.weight=q8_0
blk\.[1-8][0-9]\.attn_q\.bias=f32
blk\.[1-8][0-9]\.attn_q\.weight=q8_0
blk\.[1-8][0-9]\.attn_q_norm\.weight=f32
blk\.[1-8][0-9]\.attn_v\.bias=f32
blk\.[1-8][0-9]\.attn_v\.weight=q8_0
blk\.[1-8][0-9]\.post_attention_norm\.weight=f32
blk\.9[0-2]\.attn_k\.bias=f32
blk\.9[0-2]\.attn_k\.weight=q8_0
blk\.9[0-2]\.attn_k_norm\.weight=f32
blk\.9[0-2]\.attn_norm\.weight=f32
blk\.9[0-2]\.attn_output\.weight=q8_0
blk\.9[0-2]\.attn_q\.bias=f32
blk\.9[0-2]\.attn_q\.weight=q8_0
blk\.9[0-2]\.attn_q_norm\.weight=f32
blk\.9[0-2]\.attn_v\.bias=f32
blk\.9[0-2]\.attn_v\.weight=q8_0
blk\.9[0-2]\.post_attention_norm\.weight=f32

blk\.[3-9]\.exp_probs_b\.bias=f32
blk\.[3-9]\.ffn_down_exps\.weight=q6_K
blk\.[3-9]\.ffn_down_shexp\.weight=bf16
blk\.[3-9]\.ffn_gate_exps\.weight=q4_K
blk\.[3-9]\.ffn_gate_inp\.weight=f32
blk\.[3-9]\.ffn_gate_shexp\.weight=bf16
blk\.[3-9]\.ffn_up_exps\.weight=q4_K
blk\.[3-9]\.ffn_up_shexp\.weight=bf16
blk\.[1-8][0-9]\.exp_probs_b\.bias=f32
blk\.[1-8][0-9]\.ffn_down_exps\.weight=q6_K
blk\.[1-8][0-9]\.ffn_down_shexp\.weight=bf16
blk\.[1-8][0-9]\.ffn_gate_exps\.weight=q4_K
blk\.[1-8][0-9]\.ffn_gate_inp\.weight=f32
blk\.[1-8][0-9]\.ffn_gate_shexp\.weight=bf16
blk\.[1-8][0-9]\.ffn_up_exps\.weight=q4_K
blk\.[1-8][0-9]\.ffn_up_shexp\.weight=bf16
blk\.9[0-2]\.exp_probs_b\.bias=f32
blk\.9[0-2]\.ffn_down_exps\.weight=q6_K
blk\.9[0-2]\.ffn_down_shexp\.weight=bf16
blk\.9[0-2]\.ffn_gate_exps\.weight=q4_K
blk\.9[0-2]\.ffn_gate_inp\.weight=f32
blk\.9[0-2]\.ffn_gate_shexp\.weight=bf16
blk\.9[0-2]\.ffn_up_exps\.weight=q4_K
blk\.9[0-2]\.ffn_up_shexp\.weight=bf16

output\.weight=q8_0
output_norm\.weight=f32
token_embd\.weight=q8_0
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

echo "Running with: -custom-q $custom"

TARGET_MODEL="GLM-4.6-HQ4_K"
mkdir -p ~/Env/models/anikifoss/$TARGET_MODEL
./build/bin/llama-quantize \
    --custom-q "$custom" \
    /mnt/data/Models/zai-org/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    ~/Env/models/anikifoss/$TARGET_MODEL/$TARGET_MODEL.gguf \
    Q4_K \
    32
```
