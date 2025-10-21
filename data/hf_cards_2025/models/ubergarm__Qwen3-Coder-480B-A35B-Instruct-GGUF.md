---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: Qwen/Qwen3-Coder-480B-A35B-Instruct
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct/blob/main/LICENSE
base_model_relation: quantized
tags:
- imatrix
- qwen3_moe
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of Qwen/Qwen3-Coder-480B-A35B-Instruct
This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support the ik's latest SOTA quants and optimizations! Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

*NOTE* `ik_llama.cpp` can also run your existing GGUFs from bartowski, unsloth, mradermacher, etc if you want to try it out before downloading my quants.

Some of ik's new quants are supported with [Nexesenex/croco.cpp](https://github.com/Nexesenex/croco.cpp) fork of KoboldCPP. Precompiled binaries compatible with windows available on CUDA 12.9.

These quants provide best in class perplexity for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community on [BeaverAI Club Discord](https://huggingface.co/BeaverAI) and on [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) for tips and tricks helping each other run, test, and benchmark all the fun new models!

## Quant Collection
Perplexity computed against *wiki.test.raw*. This first one is just test quants for baseline perplexity comparison:

* `Q8_0` 475.297 GiB (8.503 BPW)
  - Final estimate: PPL = 5.0975 +/- 0.03261

![Perplexity Chart](images/perplexity.png "Chart showing Perplexity improving as BPW increases.")

## `IQ5_K` 329.804 GiB (5.900 BPW)
Final estimate: PPL = 5.1073 +/- 0.03268

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
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

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ5_K.gguf \
    IQ5_K \
    192
```

</details>

## `IQ4_K` 273.041 GiB (4.885 BPW)
Final estimate: PPL = 5.1257 +/- 0.03285

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq5_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_k

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ4_K.gguf \
    IQ4_K \
    192
```

</details>

## `IQ4_KSS` 233.676 GiB (4.180 BPW)
Final estimate: PPL = 5.1579 +/- 0.03304

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
blk\.(0|1|2)\.ffn_down_exps\.weight=iq5_ks
blk\.(0|1|2)\.ffn_(gate|up)_exps\.weight=iq4_ks
blk\..*\.ffn_down_exps\.weight=iq4_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_kss

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ4_KSS.gguf \
    IQ4_KSS \
    192
```

</details>


## `IQ3_K` 216.047 GiB (3.865 BPW)
Final estimate: PPL = 5.1808 +/- 0.03319

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq4_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_k

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ3_K.gguf \
    IQ3_K \
    192
```

</details>

## `IQ2_KL` 169.597 GiB (3.034 BPW)
Final estimate: PPL = 5.4113 +/- 0.03516

<details>

<summary>👈 Secret Recipe</summary>

Originally this had issues with NaNs but got it working this this PR: https://github.com/ikawrakow/ik_llama.cpp/pull/735

```bash
#!/usr/bin/env bash

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq3_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ2_KL.gguf \
    IQ2_KL \
    192
```

</details>

## `IQ2_K` 144.640 GiB (2.588 BPW)
Final estimate: PPL = 5.6578 +/- 0.03697

This is a `lite-IQ2_K` given it uses iq2_kl for ffn_down_exps instead of usual IQ3_K. This size and PPL is almost identical to an IQ2_KS.

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_k.*=q8_0
blk\..*\.attn_v.*=q8_0
blk\..*\.attn_output.*=iq6_k

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq2_kl
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_k

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ2_K.gguf \
    IQ2_K \
    192
```

</details>

## `IQ2_KS` 144.126 GiB (2.578 BPW)
Final estimate: PPL = 5.6658 +/- 0.03716

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Repeating Layers [0-61]

custom="
# Attention
blk\..*\.attn_q.*=iq4_ks
blk\..*\.attn_k.*=iq5_ks
blk\..*\.attn_v.*=iq5_ks
blk\..*\.attn_output.*=iq4_ks

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq3_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_ks

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
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ2_KS.gguf \
    IQ2_KS \
    192
```

</details>

## `IQ1_KT` 108.702 GiB (1.945 BPW)
Final estimate: PPL = 6.3370 +/- 0.04289

This is mostly for full GPU offload as the KT quants tend to be CPU-bound for TG while calculating Trellis. However, PP is very good.

<details>

<summary>👈 Secret Recipe</summary>

```bash
blk\..*\.attn_q.*=iq4_kt
blk\..*\.attn_k.*=iq4_kt
blk\..*\.attn_v.*=iq4_kt
blk\..*\.attn_output.*=iq4_kt

# Routed Experts
blk\..*\.ffn_down_exps\.weight=iq2_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq1_kt

# Non-Repeating Layers
token_embd\.weight=iq4_kt
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 0 -m 0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/imatrix-Qwen3-Coder-480B-A35B-Instruct-Q8_0.dat \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-BF16-00001-of-00021.gguf \
    /mnt/raid/models/ubergarm/Qwen3-Coder-480B-A35B-Instruct-GGUF/Qwen3-Coder-480B-A35B-Instruct-IQ1_KT.gguf \
    IQ1_KT \
    192
```

</details>



## Quick Start
This example is for a single CUDA GPU hybrid infrencing with CPU/RAM. Check ik_llama.cpp discussions or my other quants for more examples for multi-GPU etc.

```bash
./build/bin/llama-server \
  --model /models/IQ2_KS/Qwen3-Coder-480B-A35B-Instruct-IQ2_KS.gguf \
  --alias ubergarm/Qwen3-Coder-480B-A35B-Instruct \
  -fa -fmoe \
  -ctk q8_0 -ctv q8_0 \
  -c 32768 \
  -ngl 99 \
  -ot "blk\.[0-9]\.ffn.*=CUDA0" \
  -ot "blk.*\.ffn.*=CPU \
  --threads 16 \
  -ub 4096 -b 4096 \
  --host 127.0.0.1 \
  --port 8080
```

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)
* [Getting Started Guide (already out of date lol)](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
