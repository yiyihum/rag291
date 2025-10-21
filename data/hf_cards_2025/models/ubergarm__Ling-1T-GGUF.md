---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: inclusionAI/Ling-1T
license: mit
base_model_relation: quantized
tags:
- imatrix
- bailing_moe
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of inclusionAI/Ling-1T
This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support the ik's latest SOTA quants and optimizations! Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

*NOTE* `ik_llama.cpp` can also run your existing GGUFs from bartowski, unsloth, mradermacher, etc if you want to try it out before downloading my quants.

Some of ik's new quants are supported with [Nexesenex/croco.cpp](https://github.com/Nexesenex/croco.cpp) fork of KoboldCPP with Windows builds for CUDA 12.9. Also check for [Windows builds by Thireus here.](https://github.com/Thireus/ik_llama.cpp/releases) which have been CUDA 12.8.

These quants provide best in class perplexity for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community on [BeaverAI Club Discord](https://huggingface.co/BeaverAI) and on [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) for tips and tricks helping each other run, test, and benchmark all the fun new models!

Finally, I appreciate all the support from [aifoundry.org](https://aifoundry.org) and team as well as huggingface for hosting all these big quants!

## Quant Collection
Perplexity computed against *wiki.test.raw*.

![Perplexity Chart](images/perplexity.png "Chart showing Perplexity improving as BPW increases.")

This one is just a test quant for baseline perplexity comparison:
* `Q8_0` 989.678 GiB (8.504 BPW)
  - Final estimate: PPL = 1.9859 +/- 0.00907

## IQ5_K 689.866 GiB (5.928 BPW)
Final estimate: PPL = 1.9897 +/- 0.00910

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\..*\.attn_qkv.*=q8_0
blk\..*\.attn_output.*=q8_0

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq6_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq5_k

# Non-Repeating Layers
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-IQ5_K.gguf \
    IQ5_K \
    192
```

</details>

## smol-IQ4_KSS 471.923 GiB (4.055 BPW)
Final estimate: PPL = 2.0176 +/- 0.00927

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\..*\.attn_qkv.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_kss

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-smol-IQ4_KSS.gguf \
    IQ4_KSS \
    192
```

</details>

## smol-IQ3_KS 378.853 GiB (3.255 BPW)
Final estimate: PPL = 2.0770 +/- 0.00968

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\..*\.attn_qkv.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq3_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_ks

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-smol-IQ3_KS.gguf \
    IQ3_KS \
    192
```

</details>

## IQ2_K 330.923 GiB (2.843 BPW)
Final estimate: PPL = PPL = 2.2169 +/- 0.01055

This will use full q8_0 for VRAM layers and likely suit 384 RAM/VRAM.

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\..*\.attn_qkv.*=q8_0
blk\..*\.attn_output.*=q8_0

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq3_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_k

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-IQ2_K.gguf \
    IQ2_K \
    192
```

</details>

## smol-IQ2_KS 264.984 GiB (2.277 BPW)
Final estimate: PPL = 2.4429 +/- 0.01191

Should hopefully fit in 250 GiB RAM + 15 GiB VRAM + kv-cache/context...🤞

Leaving the `attn.*`/first 4 dense layers/shexp at full q8_0 would take about 20.1 GiB VRAM which is how the `iqN_k` quants are done.

<details>

<summary>👈 Secret Recipe</summary>

```bash
custom="
# 80 Repeating Layers [0-79]

# Attention
blk\.(0|1|2|3)\.attn_qkv.*=q8_0
blk\.(0|1|2|3)\.attn_output.*=q8_0
blk\..*\.attn_qkv.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq2_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_ks

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-smol-IQ2_KS.gguf \
    IQ2_KS \
    192
```

</details>

## smol-IQ2_XXS 249.92 GiB (2.15 BPW)
Final estimate: PPL = 2.5870 +/- 0.01279

This is a rare mainline compatible quant I released for folks to test this PR: https://github.com/ggml-org/llama.cpp/pull/16063

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\.(0|1|2|3)\.attn_qkv.*=q8_0
blk\.(0|1|2|3)\.attn_output.*=q8_0
blk\..*\.attn_qkv.*=q6_K
blk\..*\.attn_output.*=q6_K

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=q5_K
blk\..*\.ffn_(gate|up)\.weight=q4_K

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=q5_K
blk\..*\.ffn_(gate|up)_shexp\.weight=q4_K

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq2_xxs
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_xxs

# Non-Repeating Layers
token_embd\.weight=q4_K
output\.weight=q6_K
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-smol-IQ2_XXS.gguf \
    IQ2_XXS \
    192
```

</details>

## smol-IQ1_KT 215.423 GiB (1.851 BPW)
Final estimate: PPL = 2.8581 +/- 0.01471

One of the smallest yet functional quants available, but keep in mind KT types can be slower on CPU inferencing due to likely being computed bottlenecked calculating trellis during TG. Still worth a try if this is all your rig can fit!

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 80 Repeating Layers [0-79]

# Attention
blk\..*\.attn_qkv.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# First 4 Dense Layers [0-3]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-79]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-79]
blk\..*\.ffn_down_exps\.weight=iq1_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq1_kt

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N ${SOCKET} -m ${SOCKET} \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/Ling-1T-GGUF/imatrix-Ling-1T-Q8_0.dat \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-BF16-00001-of-00046.gguf \
    /mnt/data/models/ubergarm/Ling-1T-GGUF/Ling-1T-smol-IQ1_KT.gguf \
    IQ1_KT \
    192
```

</details>


## Quick Start
```bash
# Clone and checkout
$ git clone https://github.com/ikawrakow/ik_llama.cpp
$ cd ik_llama.cpp

# Build for hybrid CPU+CUDA
$ cmake -B build -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON
$ cmake --build build --config Release -j $(nproc)

# CPU-Only Inference
# `-ger` is still fresh:
# https://github.com/ikawrakow/ik_llama.cpp/pull/836
# Omit numactl and `--numa ...` if you have only a single NUMA node
# set batches/threads/kv cache as desired
# NOTE: multiple slots e.g. `--parallel 2` may case error after canceling generation then starting a new one at the moment
SOCKET=0
numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-server \
    --model "$model"\
    --alias ubergarm/Ling-1T-GGUF \
    --ctx-size 65536 \
    -fa -fmoe -ger \
    -ctk q8_0 -ctv q8_0 \
    -ub 4096 -b 4096 \
    --parallel 1 \
    --threads 128 \
    --threads-batch 192 \
    --numa numactl \
    --host 127.0.0.1 \
    --port 8080 \
    --no-mmap \
    --no-display-prompt

# Hybrid GPU+CPU Inference
# WARNING: Haven't tested this personally yet...
# `-ger` on CUDA may not be merged yet:
# https://github.com/ikawrakow/ik_llama.cpp/pull/838
# Omit numactl and `--numa ...` if you have only a single NUMA node
# set batches/threads/kv cache as desired
# NOTE: multiple slots e.g. `--parallel 2` may case error after canceling generation then starting a new one at the moment
SOCKET=0
numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-server \
    --model "$model"\
    --alias ubergarm/Ling-1T-GGUF \
    --ctx-size 65536 \
    -fa -fmoe -ger \
    -ctk q8_0 -ctv q8_0 \
    -ub 4096 -b 4096 \
    -ngl 99 \
    -ot "blk\.(4|5|6)\.ffn_.*=CUDA0" \
    -ot "blk\.(7|8|9)\.ffn_.*=CUDA1" \
    -ot exps=CPU \
    --parallel 1 \
    --threads 128 \
    --threads-batch 192 \
    --numa numactl \
    --host 127.0.0.1 \
    --port 8080 \
    --no-mmap \
    --no-display-prompt

# optional use this once after downloading to confirm good files
    --validate-quants
```

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)
* [Getting Started Guide (already out of date lol)](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [ubergarm-imatrix-calibration-corpus-v02.txt](https://gist.github.com/ubergarm/edfeb3ff9c6ec8b49e88cdf627b0711a?permalink_comment_id=5682584#gistcomment-5682584)
* [ik_llama.cpp PR833](https://github.com/ikawrakow/ik_llama.cpp/pull/833)
* [mainline llama.cpp PR16063](https://github.com/ggml-org/llama.cpp/pull/16063)
