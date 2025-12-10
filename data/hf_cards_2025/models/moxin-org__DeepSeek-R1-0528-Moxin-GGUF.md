---
quantized_by: moxin-org
base_model:
- deepseek-ai/DeepSeek-R1-0528
base_model_relation: quantized
license: mit
tags:
- deepseek_r1
- deepseek
- transformers
- GGUF
pipeline_tag: text-generation
---

## llama.cpp Mixed Precision Quant of DeepSeek-R1-0528

All quants made based on [moxin-org/CC-MoE](https://github.com/moxin-org/CC-MoE).

We hold higher expectations for the reasoning models’ performance; therefore, we have currently opted not to compress them into smaller sizes as we did for the V3 versions.


```
- Q2_K_L : 220.55 GiB (2.82 BPW)
- IQ2_XXS : 186.23 GiB (2.38 BPW)
```

### Download

Download available for huggingface_hub, huggingface-cli, snapshot_download, xet
<details>

<summary>👈 Download Guide</summary>

```bash
# !pip install huggingface_hub hf_transfer
import os
# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "moxin-org/DeepSeek-R1-0528-Moxin-GGUF",
    local_dir = "DeepSeek-R1-0528-Moxin-GGUF",
    allow_patterns = ["*Q2_K_L*"], # IQ2_XXS
)
```

</details>



### Usage

Example of runing gguf with local build of llama.cpp. (llama-cli/llama-server)

<details>

<summary>👈 Build llama.cpp locally</summary>

```
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp

cmake -B build -DGGML_CUDA=ON -DBUILD_SHARED_LIBS=OFF -DLLAMA_CURL=OFF
cmake --build build --config Release -j --clean-first
```
</details>

```
build/bin/llama-cli -m DeepSeek-R1-0528-Moxin-GGUF/R1-Q2_K_L/DeepSeek-R1-0528-Moxin-Q2_K_L-00001-of-00007.gguf \
  -ngl 99 \
  --temp 0.6 \
  --top-p 0.95 \
  --min-p 0.01 \
  --ctx-size 16384 
```


---
### Citation

If this work is helpful, please kindly cite as:

```bibtex
@article{chen2025collaborative,
  title={Collaborative Compression for Large-Scale MoE Deployment on Edge},
  author={Chen, Yixiao and Xie, Yanyue and Yang, Ruining and Jiang, Wei and Wang, Wei and He, Yong and Chen, Yue and Zhao, Pu and Wang, Yanzhi},
  journal={arXiv preprint arXiv:2509.25689},
  year={2025}
}
```

## Acknowledgements

This repository builds upon the outstanding work of the following open-source authors and projects:

- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1).
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp), [unsloth.ai](https://unsloth.ai/), [bartowski](https://github.com/bartowski1182).  
- [ikawrakow/ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp), [ikawrakow](https://github.com/ikawrakow), [ubergarm](https://github.com/ubergarm).
- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

We sincerely thank them for their excellent contributions to the open-source community.