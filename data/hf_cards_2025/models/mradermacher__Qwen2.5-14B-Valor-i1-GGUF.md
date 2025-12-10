---
base_model: TECHNOPRAVIN01/Qwen2.5-14B-Valor
language: en
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- qwen
- lora
- question-generation
- text-generation
- valor
- assumption-challenging
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags: nicoboss -->
<!-- ### quants:  Q2_K IQ3_M Q4_K_S IQ3_XXS Q3_K_M small-IQ4_NL Q4_K_M IQ2_M Q6_K IQ4_XS Q2_K_S IQ1_M Q3_K_S IQ2_XXS Q3_K_L IQ2_XS Q5_K_S IQ2_S IQ1_S Q5_K_M Q4_0 IQ3_XS Q4_1 IQ3_S -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
weighted/imatrix quants of https://huggingface.co/TECHNOPRAVIN01/Qwen2.5-14B-Valor

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Qwen2.5-14B-Valor-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own qwuants) |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ1_S.gguf) | i1-IQ1_S | 3.7 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ1_M.gguf) | i1-IQ1_M | 4.0 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ2_XS.gguf) | i1-IQ2_XS | 4.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ2_S.gguf) | i1-IQ2_S | 5.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ2_M.gguf) | i1-IQ2_M | 5.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q2_K_S.gguf) | i1-Q2_K_S | 5.5 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q2_K.gguf) | i1-Q2_K | 5.9 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 6.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ3_XS.gguf) | i1-IQ3_XS | 6.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q3_K_S.gguf) | i1-Q3_K_S | 6.8 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ3_S.gguf) | i1-IQ3_S | 6.8 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ3_M.gguf) | i1-IQ3_M | 7.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q3_K_M.gguf) | i1-Q3_K_M | 7.4 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q3_K_L.gguf) | i1-Q3_K_L | 8.0 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ4_XS.gguf) | i1-IQ4_XS | 8.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q4_0.gguf) | i1-Q4_0 | 8.6 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-IQ4_NL.gguf) | i1-IQ4_NL | 8.6 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q4_K_S.gguf) | i1-Q4_K_S | 8.7 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q4_K_M.gguf) | i1-Q4_K_M | 9.1 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q4_1.gguf) | i1-Q4_1 | 9.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q5_K_S.gguf) | i1-Q5_K_S | 10.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q5_K_M.gguf) | i1-Q5_K_M | 10.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwen2.5-14B-Valor-i1-GGUF/resolve/main/Qwen2.5-14B-Valor.i1-Q6_K.gguf) | i1-Q6_K | 12.2 | practically like static Q6_K |

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
