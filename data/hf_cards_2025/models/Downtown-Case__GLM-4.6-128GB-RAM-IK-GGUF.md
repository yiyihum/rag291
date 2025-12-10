---
license: mit
language:
- en
- zh
pipeline_tag: text-generation
base_model:
- zai-org/GLM-4.6
base_model_relation: quantized
tags:
- imatrix
- conversational
- ik_llama.cpp
---

# GLM 4.6

Quantized for 128GB RAM + single GPU setups, with `IQ_K` quants for better quality/performance in the size than mainline llama.cpp. **Requires** ik_llama.cpp.

https://github.com/ikawrakow/ik_llama.cpp

I can hit ~6.8 tokens a second textgen on 128GB dual-channel DDR5, single CCD Ryzen 7000 + a single 3090. See ubergarm's model card for more info on running these quants:

https://huggingface.co/ubergarm/GLM-4.6-GGUF

***

## V1 (Obsolete):

123.7GB, for 24GB VRAM + 128GB RAM.

<details>

<summary>Recipe (click)</summary>

```
# Attention (GPU)
blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-6] (GPU)
blk\.[3-6]\.ffn_down_exps\.weight=iq3_kt
blk\.[3-6]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [7-19] (CPU)
blk\.[7-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[7-9]\.ffn_(gate|up)_exps\.weight=iq3_ks
blk\.[1-1][0-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[1-1][0-9]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [81-92] (CPU)
blk\.[8-8][1-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[8-8][1-9]\.ffn_(gate|up)_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_down_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [20-80] (CPU)
blk\..*\.ffn_down_exps\.weight=iq2_kl
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

# NextN MTP Layer [92] (Unused, not loaded from disk)
blk\..*\.nextn\.embed_tokens\.weight=iq5_ks
blk\..*\.nextn\.shared_head_head\.weight=iq5_ks
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
```

- Uses bartowski's imatrix.

- The first 6 layers are `IQ3_KT` (a less lossy and more GPU optimal 3bpw trellis quant), running under the assumption they will be offloaded to GPU.

- Instead of quantizing ffn_down asymmetrically, it's quantized the same as ffn_up/gate, but the beginning/end layers are `IQ3_KS`. Targeting this more finely is a WIP.

</details>

***

## V2 (Obsolete):

117.3GB, for ~11GB-16GB VRAM + 128GB RAM (or longer context).

<details>

<summary>Recipe (click)</summary>

```
# Attention (GPU)
blk\..*\.attn_q.*=iq4_kt
blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq4_kt

# First 3 Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq4_kt
blk\..*\.ffn_(gate|up)\.weight=iq4_kt

# Shared Expert Layers [3-92] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq4_kt
blk\..*\.ffn_(gate|up)_shexp\.weight=iq4_kt

# Routed Experts Layers [3-7] (CPU)
blk\.[3-7]\.ffn_down_exps\.weight=iq3_ks
blk\.[3-7]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [89-92] (CPU)
blk\.[8-8][9-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[8-8][9-9]\.ffn_(gate|up)_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_down_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [9-87] (CPU)
blk\..*\.ffn_down_exps\.weight=iq2_kl
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

# NextN MTP Layer [92] (Unused, not loaded from disk)
blk\..*\.nextn\.embed_tokens\.weight=iq4_k
blk\..*\.nextn\.shared_head_head\.weight=iq4_k
blk\..*\.nextn\.eh_proj\.weight=iq4_k

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
```

Vs V1:

- Dense parts are `IQ4_KT` instead of `IQ5_KS` to save VRAM.

- More layers are `IQ2_KL` instead of `IQ3_KS` to avoid CPU swapping, and layer 92 was also 'trimmed' since it's not used.

</details>

***

## V3:

123.3GB, for 24GB VRAM + 128GB RAM. 0.098 KLD.

<details>

<summary>Recipe (click)</summary>

```
# Attention (GPU)
blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-6] (GPU)
blk\.[3-6]\.ffn_down_exps\.weight=iq3_kt
blk\.[3-6]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [7-8] (CPU)
blk\.[7-8]\.ffn_down_exps\.weight=iq3_ks
blk\.[7-8]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [12] (CPU)
blk\.[12]\.ffn_down_exps\.weight=iq3_ks
blk\.[12]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [22-24] (CPU)
blk\.[2-2][2-4]\.ffn_down_exps\.weight=iq3_ks
blk\.[2-2][2-4]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [34-41] (CPU)
blk\.[3-3][4-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[3-3][4-9]\.ffn_(gate|up)_exps\.weight=iq3_ks
blk\.[4-4][0-1]\.ffn_down_exps\.weight=iq3_ks
blk\.[4-4][0-1]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [52] (CPU)
blk\.[52]\.ffn_down_exps\.weight=iq3_ks
blk\.[52]\.ffn_(gate|up)_exps\.weight=iq3_ks

# Routed Experts Layers [83-92] (CPU)
blk\.[8-8][3-9]\.ffn_down_exps\.weight=iq3_ks
blk\.[8-8][3-9]\.ffn_(gate|up)_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_down_exps\.weight=iq3_ks
blk\.[9-9][0-2]\.ffn_(gate|up)_exps\.weight=iq3_ks

# All Other Routed Experts Layers [3-92] (CPU)
blk\..*\.ffn_down_exps\.weight=iq2_kl
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq5_k
blk\..*\.nextn\.shared_head_head\.weight=iq5_k
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
```

Vs V1:

- Uses ubergarm's ik_llama.cpp imatrix (which should be less lossy without a .gguf -> .dat conversion).

- Unsloth bf16 weights used as a base, including its tokenizer bugfixes.

- Expert quantization follows Unsloth's IQ2_XSS layer scheme, with perplexity 'bumps' boosted. See the quantization dump here: https://huggingface.co/ubergarm/GLM-4.6-GGUF/discussions/2#68dd8ca9cb29272d402f3062

</details>

<details>

<summary>Example Command (click)</summary>

`taskset -c 8-15 nice --20 build/bin/llama-server --cache-type-k q8_0 --cache-type-v q5_1 --batch_size 4096 --ubatch_size 4096 --ctx-size 20480 --host 0.0.0.0 --port 5000 -fa -fmoe -ngl 999 -ngld 999 -ot "blk\.([0-6])\.ffn_.*=CUDA0" -ot exps=CPU --parallel 1 --threads 8 --no-mmap --path examples/server/public_mikupad --sql-save-file /home/alpha/FastStorage/SQL_Save/sqlite-save.sql --model /path/to/GLM-4.6/24GB+128GB_V3/GLM-4.6-IQ2_KL-BIG-00001-of-00003.gguf`

6 MoE layers on GPU, adjust with the '6' in `"blk\.([0-6])\.ffn_.*=CUDA0"`

</details>

<details>

<summary>KLD/Perplexity Test (click)</summary>

`taskset -c 8-15 ./build/bin/llama-perplexity --ctx-size 2048 -fa -fmoe -ngl 999 -ngld 999 -ot "blk\.([0-9])\.ffn_.*=CUDA0" -ot exps=CPU --no-mmap --file /home/alpha/Models/GGUF/ddh0_imat_calibration_data_v2.txt --kl-divergence --kl-divergence-base /home/alpha/Models/GGUF/GLM-4.6-KLD-ref-logits-Q8_0-ddh0-imat-calibration-data-v2.bin --model /home/alpha/Models/GGUF/GLM-4.6/24GB+128GB_V3/GLM-4.6-unsloth.gguf-00001-of-00003.gguf`

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.966302 ±   0.160270
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.10%
Mean ln(PPL(Q)/PPL(base))     :   0.058880 ±   0.003478
Mean PPL(Q)/PPL(base)         :   1.060648 ±   0.003689
Mean PPL(Q)-PPL(base)         :   0.512694 ±   0.031904

====== KL divergence statistics ======
Mean    KLD:   0.097973 ±   0.002198
Maximum KLD:  20.749897
99.9%   KLD:   4.200683
99.0%   KLD:   1.447031
95.0%   KLD:   0.367780
90.0%   KLD:   0.183454
Median  KLD:   0.024584
10.0%   KLD:   0.000105
 5.0%   KLD:   0.000028
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000001
Minimum KLD:  -0.000134

====== Token probability statistics ======
Mean    Δp: -1.461 ± 0.065 %
Maximum Δp: 99.362%
99.9%   Δp: 54.835%
99.0%   Δp: 21.144%
95.0%   Δp:  6.569%
90.0%   Δp:  2.669%
75.0%   Δp:  0.176%
Median  Δp: -0.009%
25.0%   Δp: -0.831%
10.0%   Δp: -6.200%
 5.0%   Δp: -13.478%
 1.0%   Δp: -51.942%
 0.1%   Δp: -90.755%
Minimum Δp: -99.634%
RMS Δp    : 10.455 ± 0.186 %
Same top p: 85.422 ± 0.223 %
```

</details>

***

## V4 (Recommended):

126.8GB, for 24GB VRAM + 128GB RAM. Slower, higher quality than V3, 0.081 KLD.

<details>

<summary>Recipe (click)</summary>

```
# Attention (GPU)
blk\..*\.attn_q.*=iq5_ks
blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq5_ks

# First 3 Dense Layers [0-2] (GPU)
blk\..*\.ffn_down\.weight=iq5_ks
blk\..*\.ffn_(gate|up)\.weight=iq5_ks

# Shared Expert Layers [3-92] (GPU)
blk\..*\.ffn_down_shexp\.weight=iq5_ks
blk\..*\.ffn_(gate|up)_shexp\.weight=iq5_ks

# Routed Experts Layers [3-6] (GPU)
blk\.[3-6]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [7-8] (CPU)
blk\.[7-8]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [12] (CPU)
blk\.[12]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [22-24] (CPU)
blk\.[2-2][2-4]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [34-41] (CPU)
blk\.[3-3][4-9]\.ffn_(gate|up)_exps\.weight=iq3_kt
blk\.[4-4][0-1]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [52] (CPU)
blk\.[52]\.ffn_(gate|up)_exps\.weight=iq3_kt

# Routed Experts Layers [83-92] (CPU)
blk\.[8-8][3-9]\.ffn_(gate|up)_exps\.weight=iq3_kt
blk\.[9-9][0-2]\.ffn_(gate|up)_exps\.weight=iq3_kt

# All Other Routed Experts Layers [3-92] (CPU)
blk\..*\.ffn_down_exps\.weight=iq3_kt
blk\..*\.ffn_(gate|up)_exps\.weight=iq2_kl

# NextN MTP Layer [92]
blk\..*\.nextn\.embed_tokens\.weight=iq3_k
blk\..*\.nextn\.shared_head_head\.weight=iq3_k
blk\..*\.nextn\.eh_proj\.weight=q8_0

# Non-Repeating Layers
token_embd\.weight=iq4_k
output\.weight=iq6_k
```

Vs V3:

- All ffn_down layers are 3 bit. The same 'sensitive' up/gate ffns as V3 are still 3-bit.

- `IQ3_KT` instead of `IQ3_KS`, for smaller size *and* less loss.

- The cost: ~15% slower TG than V3 (on my Ryzen 7800).

</details>

<details>

<summary>Example Command (click)</summary>

`taskset -c 8-15 nice --20 build/bin/llama-server --cache-type-k q8_0 --cache-type-v q5_1 --batch_size 4096 --ubatch_size 4096 --ctx-size 20480 --host 0.0.0.0 --port 5000 -fa -fmoe -ngl 999 -ngld 999 -ot "blk\.([0-6])\.ffn_.*=CUDA0" -ot exps=CPU --parallel 1 --threads 8 --no-mmap --path examples/server/public_mikupad --sql-save-file /home/alpha/FastStorage/SQL_Save/sqlite-save.sql --model /path/to/GLM-4.6/24GB+128GB_V3/GLM-4.6-IQ2_KL-BIG-00001-of-00003.gguf`

3 MoE layers on GPU, adjust with the '6' in `"blk\.([0-6])\.ffn_.*=CUDA0"`

</details>

<details>

<summary>KLD/Perplexity Test (click)</summary>

`taskset -c 8-15 ./build/bin/llama-perplexity --ctx-size 2048 -fa -fmoe -ngl 999 -ngld 999 -ot "blk\.([0-9])\.ffn_.*=CUDA0" -ot exps=CPU --no-mmap --file /home/alpha/Models/GGUF/ddh0_imat_calibration_data_v2.txt --kl-divergence --kl-divergence-base /home/alpha/Models/GGUF/GLM-4.6-KLD-ref-logits-Q8_0-ddh0-imat-calibration-data-v2.bin --model /home/alpha/Models/GGUF/GLM-4.6/24GB+128GB_V4/GLM-4.6-slow.gguf-00001-of-00003.gguf`

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.894389 ±   0.158902
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.45%
Mean ln(PPL(Q)/PPL(base))     :   0.050827 ±   0.003141
Mean PPL(Q)/PPL(base)         :   1.052141 ±   0.003305
Mean PPL(Q)-PPL(base)         :   0.440781 ±   0.028588

====== KL divergence statistics ======
Mean    KLD:   0.080672 ±   0.001829
Maximum KLD:  18.875971
99.9%   KLD:   3.780314
99.0%   KLD:   1.146402
95.0%   KLD:   0.295799
90.0%   KLD:   0.153155
Median  KLD:   0.020809
10.0%   KLD:   0.000088
 5.0%   KLD:   0.000023
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000217

====== Token probability statistics ======
Mean    Δp: -1.231 ± 0.059 %
Maximum Δp: 99.351%
99.9%   Δp: 48.984%
99.0%   Δp: 19.863%
95.0%   Δp:  6.112%
90.0%   Δp:  2.490%
75.0%   Δp:  0.155%
Median  Δp: -0.009%
25.0%   Δp: -0.731%
10.0%   Δp: -5.427%
 5.0%   Δp: -11.712%
 1.0%   Δp: -44.734%
 0.1%   Δp: -88.132%
Minimum Δp: -99.827%
RMS Δp    :  9.421 ± 0.179 %
Same top p: 86.479 ± 0.216 %
```

</details>

***

For reference, Unsloth's (130.8GB) Q2_K_XL has a KL Divergence of ~0.12, and bartowski's 128GB Q2_K_XL is ~0.155, per AesSedai's benchmarks. Ik quants make a *massive* difference in this range.

Ubergarm's IQ2_KL mix has a KLD of .088 at 127.5GB. I'd recommend that as well!

https://huggingface.co/ubergarm/GLM-4.6-GGUF/tree/main/IQ2_KL

<details>

<summary>KLD/Perplexity Test (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.928715 ±   0.159610
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.32%
Mean ln(PPL(Q)/PPL(base))     :   0.054679 ±   0.003272
Mean PPL(Q)/PPL(base)         :   1.056202 ±   0.003455
Mean PPL(Q)-PPL(base)         :   0.475107 ±   0.029935

====== KL divergence statistics ======
Mean    KLD:   0.087773 ±   0.001884
Maximum KLD:  18.312426
99.9%   KLD:   3.710539
99.0%   KLD:   1.265782
95.0%   KLD:   0.326257
90.0%   KLD:   0.169567
Median  KLD:   0.023128
10.0%   KLD:   0.000102
 5.0%   KLD:   0.000025
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000081

====== Token probability statistics ======
Mean    Δp: -1.309 ± 0.061 %
Maximum Δp: 99.302%
99.9%   Δp: 50.628%
99.0%   Δp: 20.658%
95.0%   Δp:  6.840%
90.0%   Δp:  2.672%
75.0%   Δp:  0.157%
Median  Δp: -0.012%
25.0%   Δp: -0.816%
10.0%   Δp: -5.845%
 5.0%   Δp: -12.594%
 1.0%   Δp: -46.154%
 0.1%   Δp: -87.708%
Minimum Δp: -97.729%
RMS Δp    :  9.784 ± 0.178 %
Same top p: 85.906 ± 0.220 %
```

</details>

***

# K/V Cache Quantization

With all the hearsay about the effects of context cache quantization( `--cache-type-k`, `--cache-type-v` ), I tested the V4 GGUF at different levels:

<details>

<summary>F16/F16: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.894389 ±   0.158902
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.45%
Mean ln(PPL(Q)/PPL(base))     :   0.050827 ±   0.003141
Mean PPL(Q)/PPL(base)         :   1.052141 ±   0.003305
Mean PPL(Q)-PPL(base)         :   0.440781 ±   0.028588

====== KL divergence statistics ======
Mean    KLD:   0.080672 ±   0.001829
Maximum KLD:  18.875971
99.9%   KLD:   3.780314
99.0%   KLD:   1.146402
95.0%   KLD:   0.295799
90.0%   KLD:   0.153155
Median  KLD:   0.020809
10.0%   KLD:   0.000088
 5.0%   KLD:   0.000023
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000217

====== Token probability statistics ======
Mean    Δp: -1.231 ± 0.059 %
Maximum Δp: 99.351%
99.9%   Δp: 48.984%
99.0%   Δp: 19.863%
95.0%   Δp:  6.112%
90.0%   Δp:  2.490%
75.0%   Δp:  0.155%
Median  Δp: -0.009%
25.0%   Δp: -0.731%
10.0%   Δp: -5.427%
 5.0%   Δp: -11.712%
 1.0%   Δp: -44.734%
 0.1%   Δp: -88.132%
Minimum Δp: -99.827%
RMS Δp    :  9.421 ± 0.179 %
Same top p: 86.479 ± 0.216 %
```

</details>

<details>

<summary>q8_0/q8_0: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.899594 ±   0.159037
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.45%
Mean ln(PPL(Q)/PPL(base))     :   0.051412 ±   0.003139
Mean PPL(Q)/PPL(base)         :   1.052757 ±   0.003304
Mean PPL(Q)-PPL(base)         :   0.445986 ±   0.028619

====== KL divergence statistics ======
Mean    KLD:   0.081708 ±   0.001927
Maximum KLD:  19.058842
99.9%   KLD:   4.014917
99.0%   KLD:   1.186584
95.0%   KLD:   0.298380
90.0%   KLD:   0.152932
Median  KLD:   0.020809
10.0%   KLD:   0.000092
 5.0%   KLD:   0.000024
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000134

====== Token probability statistics ======
Mean    Δp: -1.232 ± 0.060 %
Maximum Δp: 99.362%
99.9%   Δp: 51.764%
99.0%   Δp: 19.850%
95.0%   Δp:  6.145%
90.0%   Δp:  2.462%
75.0%   Δp:  0.150%
Median  Δp: -0.009%
25.0%   Δp: -0.731%
10.0%   Δp: -5.516%
 5.0%   Δp: -11.651%
 1.0%   Δp: -45.131%
 0.1%   Δp: -87.501%
Minimum Δp: -99.705%
RMS Δp    :  9.487 ± 0.179 %
Same top p: 86.395 ± 0.217 %
```

</details>

<details>

<summary>q8_0/q5_1 (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.911598 ±   0.159248
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.45%
Mean ln(PPL(Q)/PPL(base))     :   0.052760 ±   0.003141
Mean PPL(Q)/PPL(base)         :   1.054177 ±   0.003311
Mean PPL(Q)-PPL(base)         :   0.457990 ±   0.028720

====== KL divergence statistics ======
Mean    KLD:   0.082269 ±   0.001856
Maximum KLD:  18.557695
99.9%   KLD:   3.692760
99.0%   KLD:   1.216560
95.0%   KLD:   0.301221
90.0%   KLD:   0.155614
Median  KLD:   0.021264
10.0%   KLD:   0.000092
 5.0%   KLD:   0.000023
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000231

====== Token probability statistics ======
Mean    Δp: -1.273 ± 0.060 %
Maximum Δp: 99.358%
99.9%   Δp: 51.804%
99.0%   Δp: 20.154%
95.0%   Δp:  6.165%
90.0%   Δp:  2.519%
75.0%   Δp:  0.147%
Median  Δp: -0.010%
25.0%   Δp: -0.759%
10.0%   Δp: -5.560%
 5.0%   Δp: -11.955%
 1.0%   Δp: -45.656%
 0.1%   Δp: -88.357%
Minimum Δp: -99.488%
RMS Δp    :  9.579 ± 0.180 %
Same top p: 86.210 ± 0.218 %
```

</details>

<details>

<summary>q5_1/q5_1: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.909289 ±   0.159159
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.39%
Mean ln(PPL(Q)/PPL(base))     :   0.052501 ±   0.003202
Mean PPL(Q)/PPL(base)         :   1.053904 ±   0.003374
Mean PPL(Q)-PPL(base)         :   0.455681 ±   0.029191

====== KL divergence statistics ======
Mean    KLD:   0.084287 ±   0.001934
Maximum KLD:  18.733398
99.9%   KLD:   3.808352
99.0%   KLD:   1.230128
95.0%   KLD:   0.309447
90.0%   KLD:   0.156537
Median  KLD:   0.021888
10.0%   KLD:   0.000100
 5.0%   KLD:   0.000026
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000123

====== Token probability statistics ======
Mean    Δp: -1.297 ± 0.061 %
Maximum Δp: 99.364%
99.9%   Δp: 54.727%
99.0%   Δp: 19.744%
95.0%   Δp:  6.244%
90.0%   Δp:  2.570%
75.0%   Δp:  0.151%
Median  Δp: -0.010%
25.0%   Δp: -0.793%
10.0%   Δp: -5.597%
 5.0%   Δp: -12.532%
 1.0%   Δp: -45.786%
 0.1%   Δp: -89.441%
Minimum Δp: -98.359%
RMS Δp    :  9.719 ± 0.182 %
Same top p: 86.006 ± 0.219 %
```

</details>

<details>

<summary>q5_1/iq4_nl: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.909554 ±   0.159207
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.37%
Mean ln(PPL(Q)/PPL(base))     :   0.052531 ±   0.003220
Mean PPL(Q)/PPL(base)         :   1.053935 ±   0.003394
Mean PPL(Q)-PPL(base)         :   0.455946 ±   0.029356

====== KL divergence statistics ======
Mean    KLD:   0.085131 ±   0.001969
Maximum KLD:  19.693703
99.9%   KLD:   3.856266
99.0%   KLD:   1.228572
95.0%   KLD:   0.308196
90.0%   KLD:   0.159706
Median  KLD:   0.022195
10.0%   KLD:   0.000098
 5.0%   KLD:   0.000026
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000001
Minimum KLD:  -0.000091

====== Token probability statistics ======
Mean    Δp: -1.275 ± 0.061 %
Maximum Δp: 99.351%
99.9%   Δp: 51.305%
99.0%   Δp: 20.998%
95.0%   Δp:  6.177%
90.0%   Δp:  2.504%
75.0%   Δp:  0.151%
Median  Δp: -0.010%
25.0%   Δp: -0.797%
10.0%   Δp: -5.772%
 5.0%   Δp: -12.275%
 1.0%   Δp: -43.956%
 0.1%   Δp: -91.987%
Minimum Δp: -99.801%
RMS Δp    :  9.705 ± 0.183 %
Same top p: 86.174 ± 0.218 %
```

</details>

<details>

<summary>iq4_nl/iq4_nl: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   9.014357 ±   0.161583
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.15%
Mean ln(PPL(Q)/PPL(base))     :   0.064225 ±   0.003436
Mean PPL(Q)/PPL(base)         :   1.066333 ±   0.003663
Mean PPL(Q)-PPL(base)         :   0.560749 ±   0.032060

====== KL divergence statistics ======
Mean    KLD:   0.092430 ±   0.001945
Maximum KLD:  10.236455
99.9%   KLD:   4.337639
99.0%   KLD:   1.295029
95.0%   KLD:   0.339931
90.0%   KLD:   0.175536
Median  KLD:   0.024666
10.0%   KLD:   0.000114
 5.0%   KLD:   0.000028
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000001
Minimum KLD:  -0.000069

====== Token probability statistics ======
Mean    Δp: -1.457 ± 0.063 %
Maximum Δp: 97.292%
99.9%   Δp: 51.854%
99.0%   Δp: 20.847%
95.0%   Δp:  6.355%
90.0%   Δp:  2.597%
75.0%   Δp:  0.153%
Median  Δp: -0.012%
25.0%   Δp: -0.863%
10.0%   Δp: -6.138%
 5.0%   Δp: -13.415%
 1.0%   Δp: -48.651%
 0.1%   Δp: -91.712%
Minimum Δp: -99.799%
RMS Δp    : 10.102 ± 0.183 %
Same top p: 85.270 ± 0.224 %

```

</details>

<details>

<summary>q4_0/q4_0: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.989389 ±   0.160672
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.20%
Mean ln(PPL(Q)/PPL(base))     :   0.061452 ±   0.003379
Mean PPL(Q)/PPL(base)         :   1.063379 ±   0.003593
Mean PPL(Q)-PPL(base)         :   0.535781 ±   0.031258

====== KL divergence statistics ======
Mean    KLD:   0.095753 ±   0.002066
Maximum KLD:  18.313120
99.9%   KLD:   3.814511
99.0%   KLD:   1.351413
95.0%   KLD:   0.351929
90.0%   KLD:   0.186834
Median  KLD:   0.026491
10.0%   KLD:   0.000125
 5.0%   KLD:   0.000032
 1.0%   KLD:   0.000003
 0.1%   KLD:  -0.000001
Minimum KLD:  -0.000185

====== Token probability statistics ======
Mean    Δp: -1.526 ± 0.064 %
Maximum Δp: 99.418%
99.9%   Δp: 53.180%
99.0%   Δp: 21.094%
95.0%   Δp:  6.615%
90.0%   Δp:  2.596%
75.0%   Δp:  0.153%
Median  Δp: -0.014%
25.0%   Δp: -0.923%
10.0%   Δp: -6.439%
 5.0%   Δp: -14.138%
 1.0%   Δp: -49.446%
 0.1%   Δp: -90.444%
Minimum Δp: -99.226%
RMS Δp    : 10.279 ± 0.181 %
Same top p: 85.030 ± 0.226 %

```
</details>

<details>

<summary>f16/q4_1: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.877527 ±   0.158448
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.47%
Mean ln(PPL(Q)/PPL(base))     :   0.048930 ±   0.003116
Mean PPL(Q)/PPL(base)         :   1.050147 ±   0.003272
Mean PPL(Q)-PPL(base)         :   0.423919 ±   0.028223

====== KL divergence statistics ======
Mean    KLD:   0.081548 ±   0.001653
Maximum KLD:   7.626703
99.9%   KLD:   3.458830
99.0%   KLD:   1.238388
95.0%   KLD:   0.305159
90.0%   KLD:   0.159369
Median  KLD:   0.021200
10.0%   KLD:   0.000096
 5.0%   KLD:   0.000023
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000001
Minimum KLD:  -0.000248

====== Token probability statistics ======
Mean    Δp: -1.236 ± 0.060 %
Maximum Δp: 98.952%
99.9%   Δp: 53.722%
99.0%   Δp: 20.829%
95.0%   Δp:  6.295%
90.0%   Δp:  2.531%
75.0%   Δp:  0.156%
Median  Δp: -0.009%
25.0%   Δp: -0.768%
10.0%   Δp: -5.622%
 5.0%   Δp: -11.933%
 1.0%   Δp: -44.170%
 0.1%   Δp: -87.853%
Minimum Δp: -98.051%
RMS Δp    :  9.506 ± 0.176 %
Same top p: 86.118 ± 0.219 %
```

</details>

<details>

<summary>q4_1/f16: (click)</summary>

```
====== Perplexity statistics ======
Mean PPL(Q)                   :   8.940920 ±   0.159879
Mean PPL(base)                :   8.453608 ±   0.150165
Cor(ln(PPL(Q)), ln(PPL(base))):  98.34%
Mean ln(PPL(Q)/PPL(base))     :   0.056045 ±   0.003249
Mean PPL(Q)/PPL(base)         :   1.057645 ±   0.003436
Mean PPL(Q)-PPL(base)         :   0.487312 ±   0.029850

====== KL divergence statistics ======
Mean    KLD:   0.087104 ±   0.001802
Maximum KLD:   8.198884
99.9%   KLD:   4.082293
99.0%   KLD:   1.282577
95.0%   KLD:   0.319321
90.0%   KLD:   0.168931
Median  KLD:   0.023545
10.0%   KLD:   0.000107
 5.0%   KLD:   0.000027
 1.0%   KLD:   0.000002
 0.1%   KLD:  -0.000002
Minimum KLD:  -0.000195

====== Token probability statistics ======
Mean    Δp: -1.354 ± 0.062 %
Maximum Δp: 93.440%
99.9%   Δp: 50.761%
99.0%   Δp: 20.380%
95.0%   Δp:  6.501%
90.0%   Δp:  2.649%
75.0%   Δp:  0.142%
Median  Δp: -0.011%
25.0%   Δp: -0.853%
10.0%   Δp: -5.913%
 5.0%   Δp: -12.579%
 1.0%   Δp: -45.759%
 0.1%   Δp: -90.052%
Minimum Δp: -99.540%
RMS Δp    :  9.816 ± 0.182 %
Same top p: 85.502 ± 0.223 %
```

</details>

Takeaways:

- q8_0/q8_0 is within the margin of error (+0.001 KLD); seemingly very little loss for the huge vram savings.

- K is more sensitive than V to quantization.

- I don't recommend q4_0/q4_0.

- But some other configurations appears to be reasonably low loss, with q8_0/q5_1 (for instance) within the margin of error, and q5_1/iq4_nl (at +0.0045) being quite reasonable for squeezing in a lot of context. Personaly, I use q8_0/q5_1 now.

- Take this with a grain of salt, as (due to the way the test uses the K/V cache) I haven't confirmed the correlation between KV cache quantization KLD with actual long context inference.

***

## Info

KL divergence/perplexity tests are done with AesSedai's wonderful testing data: https://huggingface.co/AesSedai/GLM-4.6-GGUF/discussions/1#68dcb412ae30ad1405dacd9a

MoE Experts are generally `IQ2_KL`/`IQ3_KS` on CPU, or `IQ3_KT` if destined for the GPU, with dense layers at higher quants levels like `IQ5_KS` for less loss.

My hardware is a undervolted 3090, dual channel DDR5 6000, an AMD 7800 CPU and linux, though dual CDD ryzen (or tweaked systems) should be notably faster due to the single CCD bandwidth limit.

See the example scripts for quantizing, launching the server, and such.

KLD results are not *necessarily* comparible to other repos (as they were run at 2048 context instead of the default 512), but they will be once I rerun them.

More variants are a WIP.

**If you want a different sized quant, ask!**

***

## TODO

- ~~Native (instead of converted) imatrix data.~~

- ~~Add unsloth chat template bug fixes.~~

- ~~KLD benchmarks vs Q8_0.~~

- ~~Check perplexity of expert FFNs in each layer.~~

- ~~Test impact of K/V cache quantization.~~

- Make more optimal mixes using the Thireus's perplexity data, as seen in `Example_Scripts/GLM-4.6-expert-sorted-perplexity.txt`.

- Find 'point of diminishing returns' for dense layer quantization (`Q6_K`?).

- Test KLD impact of different token_embd quantization.

- Rerun KLD to make results more comparable.

***

Derived from ubergarm's GLM-4.5 (Instruct) quantizations: https://huggingface.co/ubergarm/GLM-4.5-GGUF

And GGUF-Tool-Suite: https://github.com/Thireus/GGUF-Tool-Suite

Also see:

https://huggingface.co/ubergarm/GLM-4.6-GGUF

Thanks for these!

