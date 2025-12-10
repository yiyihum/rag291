---
base_model: trituenhantaoio/llm-vn-1-7b
language:
- vi
- en
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- vietnamese
- multilingual
- llm
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
<!-- ### quants:  x-f16 Q4_K_S Q2_K Q8_0 Q6_K Q3_K_M Q3_K_S Q3_K_L Q4_K_M Q5_K_S Q5_K_M IQ4_XS -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
static quants of https://huggingface.co/trituenhantaoio/llm-vn-1-7b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#llm-vn-1-7b-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/llm-vn-1-7b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q2_K.gguf) | Q2_K | 3.1 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q3_K_S.gguf) | Q3_K_S | 3.6 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q3_K_M.gguf) | Q3_K_M | 3.9 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q3_K_L.gguf) | Q3_K_L | 4.2 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.IQ4_XS.gguf) | IQ4_XS | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q4_K_S.gguf) | Q4_K_S | 4.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q4_K_M.gguf) | Q4_K_M | 4.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q5_K_S.gguf) | Q5_K_S | 5.4 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q5_K_M.gguf) | Q5_K_M | 5.5 |  |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q6_K.gguf) | Q6_K | 6.4 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.Q8_0.gguf) | Q8_0 | 8.2 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/llm-vn-1-7b-GGUF/resolve/main/llm-vn-1-7b.f16.gguf) | f16 | 15.3 | 16 bpw, overkill |

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
this work in my free time.

<!-- end -->
