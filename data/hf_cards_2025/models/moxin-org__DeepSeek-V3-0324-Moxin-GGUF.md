---
quantized_by: moxin-org
base_model:
- deepseek-ai/DeepSeek-V3-0324
base_model_relation: quantized
license: mit
tags:
- deepseek_v3
- deepseek
- transformers
- GGUF
pipeline_tag: text-generation
---

## llama.cpp Mixed Precision Quant of DeepSeek-V3-0324

All quants made based on [moxin-org/CC-MoE](https://github.com/moxin-org/CC-MoE).

`IQ1_M` is based on recipes defined via the `--tensor-type` option.

`IQ1_S` is a more dynamic version intended for extreme compression.
```
- IQ1_S : 137.66 GiB (1.76 BPW)
- IQ1_M : 151.25 GiB (1.94 BPW)
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
    repo_id = "moxin-org/DeepSeek-V3-0324-Moxin-GGUF",
    local_dir = "DeepSeek-V3-0324-Moxin-GGUF",
    allow_patterns = ["*IQ1_M*"], # IQ1_S, Mini
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
build/bin/llama-cli -m DeepSeek-V3-0324-Moxin-GGUF/V3-IQ1_M/DeepSeek-V3-0324-Moxin-IQ1_M-00001-of-00006.gguf \
  -ngl 99 \
  --temp 0.3 \
  --min-p 0.01 \
  --ctx-size 8192 \ # 4096, 16384
```


### Smallest Compression (CC-MoE) 

For our smallest compressed version `105.58 GiB (1.79 BPW)`. Please refer to 
[tflsxyy/DeepSeek-V3-0324-E192](https://huggingface.co/tflsxyy/DeepSeek-V3-0324-MoE-Pruner-E192-bf16) 
and [V3-Mini-Exp](https://huggingface.co/moxin-org/DeepSeek-V3-0324-Moxin-GGUF/tree/main/V3-Mini-Exp)
for more details.

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

- [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3).
- [tflsxyy](https://github.com/tflsxyy).
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp), [unsloth.ai](https://unsloth.ai/), [bartowski](https://github.com/bartowski1182).  
- [ikawrakow/ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp), [ikawrakow](https://github.com/ikawrakow), [ubergarm](https://github.com/ubergarm).
- [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

We sincerely thank them for their excellent contributions to the open-source community.