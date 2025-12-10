---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: zai-org/GLM-4.6
license: mit
base_model_relation: quantized
tags:
- imatrix
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of zai-org/GLM-4.6
This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support the ik's latest SOTA quants and optimizations! Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

*NOTE* `ik_llama.cpp` can also run your existing GGUFs from bartowski, unsloth, mradermacher, etc if you want to try it out before downloading my quants.

Some of ik's new quants are supported with [Nexesenex/croco.cpp](https://github.com/Nexesenex/croco.cpp) fork of KoboldCPP with Windows builds for CUDA 12.9. Also check for [Windows builds by Thireus here.](https://github.com/Thireus/ik_llama.cpp/releases) which have been CUDA 12.8.

These quants provide best in class perplexity for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community on [BeaverAI Club Discord](https://huggingface.co/BeaverAI) and on [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) for tips and tricks helping each other run, test, and benchmark all the fun new models!

## Quant Collection
Perplexity computed against *wiki.test.raw*.

![Perplexity Chart](images/perplexity.png "Chart showing Perplexity improving as BPW increases.")

These first two are just test quants for baseline perplexity comparison:
* `BF16` 664.707 GiB (16.003 BPW)
  - Final estimate: PPL = 3.4454 +/- 0.01999
* `Q8_0` 353.259 GiB (8.505 BPW)
  - Final estimate: PPL = 3.4471 +/- 0.02001

## IQ5_K 249.099 GiB (5.997 BPW)
Final estimate: PPL = 3.4428 +/- 0.01993

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\..*\.attn_q.*=q8_0
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=q8_0

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq6_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq5_k

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq6_k
blk\..*\.nextn\.shared_head_head\.weight=iq6_k
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-IQ5_K.gguf \
    IQ5_K \
    192
```

</details>

## IQ4_K 207.708 GiB (5.001 BPW)
Final estimate: PPL = 3.4758 +/- 0.02023

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\..*\.attn_q.*=q8_0
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=q8_0

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq5_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_k

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq5_k
blk\..*\.nextn\.shared_head_head\.weight=iq5_k
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-IQ4_K.gguf \
    IQ4_K \
    192
```

</details>


## IQ4_KS 192.967 GiB (4.646 BPW)
Final estimate: PPL = 3.5309 +/- 0.02057

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_ks

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq5_ks
blk\..*\.nextn\.shared_head_head\.weight=iq5_ks
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-IQ4_KS.gguf \
    IQ4_KS \
    192
```

</details>

## smol-IQ4_KSS 169.895 GiB (4.090 BPW)
Final estimate: PPL = 3.5911 +/- 0.02092

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_kss

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq4_kss
blk\..*\.nextn\.shared_head_head\.weight=iq4_kss
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 1 -m 1 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-smol-IQ4_KSS.gguf \
    IQ4_KSS \
    192
```

</details>

## IQ3_KS 148.390 GiB (3.573 BPW)
Final estimate: PPL = 3.6427 +/- 0.02127

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_ks

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq4_kss
blk\..*\.nextn\.shared_head_head\.weight=iq4_kss
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 1 -m 1 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-IQ3_KS.gguf \
    IQ3_KS \
    192
```

</details>

## IQ2_KL 127.516 GiB (3.070 BPW)
Final estimate: PPL = 4.1456 +/- 0.02521

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq3_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq4_kss
blk\..*\.nextn\.shared_head_head\.weight=iq4_kss
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 1 -m 1 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-IQ2_KL.gguf \
    IQ2_KL \
    192
```

</details>

## smol-IQ2_KS 97.990 GiB (2.359 BPW)
Final estimate: PPL = 5.2760 +/- 0.03410

<details>

<summary>👈 Secret Recipe</summary>

Did *not* use PR624 https://github.com/ikawrakow/ik_llama.cpp/pull/624 (it would probably give slightly perplexity better, but a pain to rebase and confirm at this point, lol)

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq2_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_ks

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq4_kss
blk\..*\.nextn\.shared_head_head\.weight=iq4_kss
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 1 -m 1 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-smol-IQ2_KS.gguf \
    IQ2_KS \
    192
```

</details>

## smol-IQ1_KT 80.906 GiB (1.948 BPW)
Final estimate: PPL = 5.9034 +/- 0.03812

*Good luck everybody!* 😅

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# 93 Repeating Layers [0-92]

# Attention
blk\.(0|1|2)\.attn_q.*=q8_0
blk\.(0|1|2)\.attn_k.*=q8_0
blk\.(0|1|2)\.attn_v.*=q8_0
blk\.(0|1|2)\.attn_output.*=q8_0

blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2]
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92]
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-92]
blk\..*\.ffn_down_exps\.weight=iq1_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq1_kt

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq4_kss
blk\..*\.nextn\.shared_head_head\.weight=iq4_kss
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/data/models/ubergarm/GLM-4.6-GGUF/imatrix-GLM-4.6-BF16.dat \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-160x19B-4.6-BF16-00001-of-00015.gguf \
    /mnt/data/models/ubergarm/GLM-4.6-GGUF/GLM-4.6-smol-IQ1_KT.gguf \
    IQ1_KT \
    192
```

</details>


## Quick Start
If you want to disable thinking, add `/nothink` (correct, no underscore) at the *end* of your prompt.

```bash
# Clone and checkout
$ git clone https://github.com/ikawrakow/ik_llama.cpp
$ cd ik_llama.cpp

# Build for hybrid CPU+CUDA
$ cmake -B build -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON -DGGML_BLAS=OFF -DGGML_SCHED_MAX_COPIES=1
$ cmake --build build --config Release -j $(nproc)

# Run API server
$ ./build/bin/llama-server \
    --model GLM-4.6-IQ4_KSS-00001-of-00004.gguf \
    --alias ubergarm/GLM-4.6-IQ4_KSS \
    --ctx-size 32768 \
    -fa -fmoe \
    -ctk q8_0 -ctv q8_0 \
    -ub 4096 -b 4096 \
    -ngl 99 \
    -ot exps=CPU \
    --parallel 1 \
    --threads 8 \
    --host 127.0.0.1 \
    --port 8080 \
    --no-mmap

# MCP/Tool Use
# --jinja etc...
```

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)
* [Getting Started Guide (already out of date lol)](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [ubergarm-imatrix-calibration-corpus-v02.txt](https://gist.github.com/ubergarm/edfeb3ff9c6ec8b49e88cdf627b0711a?permalink_comment_id=5682584#gistcomment-5682584)
* [bartowski mainline llama.cpp GLM-4.6 fix PR16359](https://github.com/ggml-org/llama.cpp/pull/16359)
* [ik_llama.cpp PR814 Downtown-Case](https://github.com/ikawrakow/ik_llama.cpp/pull/814)
* [Speed benchmarks on local gaming rig](https://huggingface.co/ubergarm/GLM-4.6-GGUF/discussions/5)
* [More good quants by AesSedai/GLM-4.6-GGUF](https://huggingface.co/AesSedai/GLM-4.6-GGUF)
