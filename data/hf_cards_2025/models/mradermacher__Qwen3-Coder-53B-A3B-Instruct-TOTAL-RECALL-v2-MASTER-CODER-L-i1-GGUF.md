---
base_model: DavidAU/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L
language:
- en
- fr
- zh
- de
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- programming
- code generation
- code
- codeqwen
- programming
- code generation
- code
- codeqwen
- moe
- coding
- coder
- qwen2
- chat
- qwen
- qwen-coder
- chat
- qwen
- qwen-coder
- moe
- Qwen3-Coder-30B-A3B-Instruct
- Qwen3-30B-A3B
- mixture of experts
- 128 experts
- 10 active experts
- 256k context
- qwen3
- finetune
- brainstorm 40x
- brainstorm
- optional thinking
- qwen3_moe
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags: nicoboss -->
<!-- ### quants: Q2_K IQ3_M Q4_K_S IQ3_XXS Q3_K_M small-IQ4_NL Q4_K_M IQ2_M Q6_K IQ4_XS Q2_K_S IQ1_M Q3_K_S IQ2_XXS Q3_K_L IQ2_XS Q5_K_S IQ2_S IQ1_S Q5_K_M Q4_0 IQ3_XS Q4_1 IQ3_S -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
weighted/imatrix quants of https://huggingface.co/DavidAU/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.imatrix.gguf) | imatrix | 0.3 | imatrix file (for creating your own qwuants) |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ1_S.gguf) | i1-IQ1_S | 11.1 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ1_M.gguf) | i1-IQ1_M | 12.2 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 14.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ2_XS.gguf) | i1-IQ2_XS | 15.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ2_S.gguf) | i1-IQ2_S | 16.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ2_M.gguf) | i1-IQ2_M | 17.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q2_K_S.gguf) | i1-Q2_K_S | 18.2 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q2_K.gguf) | i1-Q2_K | 19.5 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 20.6 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ3_XS.gguf) | i1-IQ3_XS | 21.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q3_K_S.gguf) | i1-Q3_K_S | 23.1 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ3_S.gguf) | i1-IQ3_S | 23.1 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ3_M.gguf) | i1-IQ3_M | 23.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q3_K_M.gguf) | i1-Q3_K_M | 25.5 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q3_K_L.gguf) | i1-Q3_K_L | 27.6 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-IQ4_XS.gguf) | i1-IQ4_XS | 28.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q4_0.gguf) | i1-Q4_0 | 30.2 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q4_K_S.gguf) | i1-Q4_K_S | 30.3 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q4_K_M.gguf) | i1-Q4_K_M | 32.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q4_1.gguf) | i1-Q4_1 | 33.3 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q5_K_S.gguf) | i1-Q5_K_S | 36.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q5_K_M.gguf) | i1-Q5_K_M | 37.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF/resolve/main/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L.i1-Q6_K.gguf) | i1-Q6_K | 43.6 | practically like static Q6_K |

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)

And here are Artefact2's thoughts on the matter:
https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9

## FAQ / Model Request

See https://huggingface.co/mradermacher/model_requests for some answers to
questions you might have and/or if you want some other model quantized.

## Thanks

I thank my company, [nethype GmbH](https://www.nethype.de/), for letting
me use its servers and providing upgrades to my workstation to enable
this work in my free time. Additional thanks to [@nicoboss](https://huggingface.co/nicoboss) for giving me access to his private supercomputer, enabling me to provide many more imatrix quants, at much higher quality, than I would otherwise be able to.

<!-- end -->
