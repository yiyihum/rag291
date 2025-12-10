---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: deepseek-ai/DeepSeek-V3.1
license: mit
base_model_relation: quantized
tags:
- mla
- imatrix
- deepseek_v3
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of deepseek-ai/DeepSeek-V3.1
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

This first is just a "pure" test quant for baseline perplexity comparison:
* `Q8_0` 664.295 GiB (8.504 BPW)
  - Final estimate: PPL = 3.3473 +/- 0.01935

## IQ5_K 465.075 GiB (5.944 BPW)
Final estimate: PPL = 3.3550 +/- 0.01942

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
# attn_kv_b is only used for PP so keep it q8_0 for best speed and accuracy
blk\..*\.attn_kv_b\.weight=q8_0

# ideally k_b and v_b are smaller than q8_0 as they are is used for TG with -mla 3
# https://github.com/ikawrakow/ik_llama.cpp/issues/651
# blk.*.attn_k_b.weight is not divisible by 256 so only supports iq4_nl or legacy qN_0
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=q8_0

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

## Shared Expert (1-60) (GPU)
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

## Routed Experts (1-60) (CPU)
blk\..*\.ffn_down_exps\.weight=iq6_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq5_k

## Token embedding and output tensors (GPU)
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

numactl -N 1 -m 1 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x21B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ5_K.gguf \
    IQ5_K \
    192
```

</details>

## IQ4_K 384.765 GiB (4.925 BPW)
Final estimate: PPL = 3.3715 +/- 0.01956

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=q8_0

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq5_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_k

## Token embedding and output tensors (GPU)
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ4_K.gguf \
    IQ4_K \
    192
```

</details>

## IQ4_KS 363.151 GiB (4.649 BPW)
Final estimate: PPL = 3.3806 +/- 0.01966

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_ks

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ4_KS.gguf \
    IQ4_KS \
    192
```

</details>

## IQ4_KSS 325.088 GiB (4.162 BPW)
Final estimate: PPL = 3.3887 +/- 0.01968

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq4_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_kss

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=1

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ4_KSS.gguf \
    IQ4_KSS \
    192
```

</details>

## smol-IQ4_KSS 318.745 GiB (4.080 BPW)
Final estimate: PPL = 3.3898 +/- 0.01964

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_kss

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=1

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-smol-IQ4_KSS.gguf \
    IQ4_KSS \
    192
```

</details>

## IQ3_K 293.177 GiB (3.753 BPW)
Final estimate: PPL = 3.4260 +/- 0.01995

<details>

<summary>👈 Secret Recipe</summary>

*NOTE*: Made with https://github.com/ikawrakow/ik_llama.cpp/pull/624

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=q8_0

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_k

## Token embedding and output tensors (GPU)
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ3_K.gguf \
    IQ3_K \
    192
```

</details>

## IQ3_KS 277.397 GiB (3.551 BPW)
Final estimate: PPL = 3.4534 +/- 0.02019

<details>

<summary>👈 Secret Recipe</summary>

*NOTE*: Made with https://github.com/ikawrakow/ik_llama.cpp/pull/624

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq4_kss
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_ks

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ3_KS.gguf \
    IQ3_KS \
    192
```

</details>


## IQ2_KL 231.206 GiB (2.960 BPW)
Final estimate: PPL = 3.6312 +/- 0.02161

<details>

<summary>👈 Secret Recipe</summary>

*NOTE*: Made with https://github.com/ikawrakow/ik_llama.cpp/pull/624

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq3_ks
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ2_KL-PR624.gguf \
    IQ2_KL \
    192
```

</details>

## IQ2_KT 204.592 GiB (2.619 BPW)
Final estimate: PPL = 3.8109 +/- 0.02294

Remember, the KT quants are better suited for full GPU offload as calculating trellis on CPU bottlenecks token generation.

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=q8_0

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=q8_0
blk\..*\.ffn_(gate|up)\.weight=q8_0

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=q8_0
blk\..*\.ffn_(gate|up)_shexp\.weight=q8_0

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq3_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kt

## Token embedding and output tensors (GPU)
token_embd\.weight=iq6_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ2_KT.gguf \
    IQ2_KT \
    192
```

</details>



## IQ2_KS 193.144 GiB (2.472 BPW)
Final estimate: PPL = 3.9583 +/- 0.02433

<details>

*NOTE*: Made with https://github.com/ikawrakow/ik_llama.cpp/pull/624

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=q8_0
blk\..*\.attn_output\.weight=iq6_k

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq2_kl
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_ks

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ2_KS.gguf \
    IQ2_KS \
    192
```

</details>

## IQ1_KT 154.968 GiB (1.984 BPW)
Final estimate: PPL = 4.3987 +/- 0.02786

Remember, the KT quants are better suited for full GPU offload e.g. 2x RTX 6000 Pro Blackwells in this case.

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
blk\..*\.attn_k_b\.weight=q8_0
blk\..*\.attn_v_b\.weight=q8_0

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=q8_0
blk\..*\.attn_q_a\.weight=q8_0
blk\..*\.attn_q_b\.weight=iq5_ks
blk\..*\.attn_output\.weight=iq5_ks

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

## Shared Expert [3-60] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

## Routed Experts [3-60] (CPU)
blk\..*\.ffn_down_exps\.weight=iq2_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq1_kt

## Token embedding and output tensors (GPU)
token_embd\.weight=iq4_k
output\.weight=iq6_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

SOCKET=0

numactl -N "$SOCKET" -m "$SOCKET" \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ1_KT.gguf \
    IQ1_KT \
    192
```

</details>

## IQ1_S 133.610 GiB (1.710 BPW)
Final estimate: PPL = 5.3113 +/- 0.03507

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
## Attention [0-60] (GPU)
# https://github.com/ikawrakow/ik_llama.cpp/issues/651
blk\..*\.attn_k_b\.weight=q6_0
blk\..*\.attn_v_b\.weight=iq6_k

# Balance of attn tensors
blk\..*\.attn_kv_a_mqa\.weight=iq5_ks
blk\..*\.attn_q_a\.weight=iq5_ks
blk\..*\.attn_q_b\.weight=iq5_ks
blk\..*\.attn_output\.weight=iq4_ks

## First Three Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq4_ks

## Shared Expert (1-60) (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq4_ks

## Routed Experts (1-60) (CPU)
blk\..*\.ffn_down_exps\.weight=iq1_m
blk\..*\.ffn_(gate|up)_exps\.weight=iq1_s

## Token embedding and output tensors (GPU)
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
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/imatrix-DeepSeek-V3.1-Q8_0.dat \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-256x20B-safetensors-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3.1-GGUF/DeepSeek-V3.1-IQ1_S.gguf \
    IQ1_S \
    192
```

</details>

## Quick Start
```bash
# Clone and checkout
$ git clone https://github.com/ikawrakow/ik_llama.cpp
$ cd ik_llama.cpp

# Build for hybrid CPU+CUDA
$ cmake -B build -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON -DGGML_BLAS=OFF -DGGML_SCHED_MAX_COPIES=1
$ cmake --build build --config Release -j $(nproc)

# Run API server Hybrid CPU+GPU
# model is the first file of the GGUF splits
$ ./build/bin/llama-server \
    --model "$model"\
    --alias ubergarm/DeepSeek-V3.1-GGUF \
    --ctx-size 32768 \
    -ctk q8_0 \
    -fa -fmoe \
    -mla 3 -amb 512 \
    -ngl 99 \
    -ot exps=CPU \
    --parallel 1 \
    --threads 8 \
    --host 127.0.0.1 \
    --port 8080 \
    --no-display-prompt \
    --chat-template deepseek3

# Run API Server CPU-Only
$ numactl -N 0 -m 0 \
./build/bin/llama-server \
    --model "$model"\
    --alias ubergarm/DeepSeek-V3.1-GGUF \
    --ctx-size 131072 \
    -ub 4096 -b 4096 \
    -ctk q8_0 \
    -fa -fmoe \
    -mla 3 \
    --parallel 1 \
    --threads 128 \
    --threads-batch 192 \
    --numa numactl \
    --host 127.0.0.1 \
    --port 8080 \
    --no-display-prompt \
    --chat-template deepseek3 \
    --no-mmap
```

Multi-GPU is well supported with custom `-ot ...=CUDA1` offload regex arguments etc.

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp)
* [Getting Started Guide (already out of date lol)](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [Quant Cookers Guide](https://github.com/ikawrakow/ik_llama.cpp/discussions/434)
* [Compiling triton-cpu](https://github.com/triton-lang/triton-cpu/issues/237#issuecomment-2878180022)
* [fp8 to bf16 safetensors casting without GPU](https://github.com/ggml-org/llama.cpp/issues/14762#issuecomment-3098571703)
* [avx512 avx_vnni Zen5 experimental optimizations](https://github.com/ikawrakow/ik_llama.cpp/pull/710)
* [ubergarm-imatrix-calibration-corpus-v02.txt](https://gist.github.com/ubergarm/edfeb3ff9c6ec8b49e88cdf627b0711a?permalink_comment_id=5682584#gistcomment-5682584)
