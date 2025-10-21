---
language:
- en
license: apache-2.0
tags:
- quantization
- sinq
- int4
- efficient-inference
- text-generation
- qwen
- llm
- compression
base_model: Qwen/Qwen3-32B
base_model_relation: quantized
---

<p align="center">
  <img src="logo.png" alt="Logo" style="max-width: 80%; height: auto;">
</p>

<p align="center">🐙 <a href="https://github.com/huawei-csl/SINQ">Github</a>&nbsp;&nbsp; | &nbsp;&nbsp;📄 <a href="http://arxiv.org/abs/2509.22944">Paper</a></p>


# SINQ 4-bit Quantized Qwen3-32B model

This repository contains the official **4-bit quantized** version of the [`Qwen3-32B`](https://huggingface.co/Qwen/Qwen3-32B) model using the **SINQ (Sinkhorn-Normalized Quantization)** method.  
SINQ is a novel, fast and high-quality quantization method designed to make any Large Language Models smaller while keeping their accuracy almost intact. 

To support the project please put a star ⭐ in the official [SINQ](https://github.com/huawei-csl/SINQ) github repository. 

## Model Details
- **Model Name:** `Qwen3-32B-4bit-SINQ `
- **Base Model:** [`Qwen/Qwen3-32B`](https://huggingface.co/Qwen/Qwen3-32B)
- **Task:** Text Generation
- **Framework:** PyTorch / Transformers
- **License:** [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
- **Quantized By:** *Huawei - Computing Systems Lab*


## Quantization Details

- **Quantization Method:**  SINQ (Sinkhorn-Normalized Quantization)
- **Precision:** INT4 
- **Group Size:**  64 
- **Framework:**  PyTorch 
- **Quantization Library:**  `sinq` 

---

# 🚀 Usage</span>

## Prerequisite
Before running the quantization script, make sure the **SINQ** library is installed.
Installation instructions and setup details are available in the [SINQ official github repository](https://github.com/huawei-csl/SINQ).

## Usage example
You can load and use the model with our wrapper based on the 🤗 Transformers library:

```python
from transformers import AutoTokenizer
from sinq.patch_model import AutoSINQHFModel

model_name = "huawei-csl/Qwen3-32B-4bit-SINQ"
tokenizer = AutoTokenizer.from_pretrained(model_name)
sinq_model = AutoSINQHFModel.from_quantized_safetensors(
    model_name,
    device="cuda:0",
    compute_dtype=torch.bfloat16
)

prompt = "Explain neural network quantization in one sentence."
inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
with torch.inference_mode():
    out_ids = sinq_model.generate(**inputs, max_new_tokens=32, do_sample=False)
print(tokenizer.decode(out_ids[0], skip_special_tokens=True))

```

<details>
<summary><span style="font-size:1.1em; font-weight:bold;">🧩 Quantization Process</span></summary>

The quantized model was obtained using the **SINQ** quantization library, following the steps below:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from sinq.patch_model import AutoSINQHFModel
from sinq.sinqlinear import BaseQuantizeConfig

# Load base model
base_model_name = "Qwen/Qwen3-32B"
model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype="float16")
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

# Apply 4-bit SINQ quantization
quant_cfg = BaseQuantizeConfig(
    nbits=4,            # quantization bit-width
    group_size=64,     # group size
    tiling_mode="1D",   # tiling strategy
    method="sinq"       # quantization method ("asinq" for the calibrated version)
)

qmodel = AutoSINQHFModel.quantize_model(
    model,
    tokenizer=tokenizer,
    quant_config=quant_cfg,
    compute_dtype=torch.bfloat16,
    device="cuda:0"
)
```

> **Reproducibility Note**: This model was quantized using the SINQ implementation from commit [`14ad847`](https://github.com/huawei-csl/SINQ/commit/14ad847d0ab25f1794b8820506f59b5c9c1fc979) of the [SINQ](https://github.com/huawei-csl/SINQ) repository.  

</details>

</br>

---

# 🧾 How to Cite This Work

If you find **SINQ** useful in your research or applications, please
- Put a star ⭐ in the official [SINQ](https://github.com/huawei-csl/SINQ) github repository.
- Cite our <a href="http://arxiv.org/abs/2509.22944" target="_blank"><strong>paper</strong></a>:

```bibtex
@misc{muller2025sinq,
      title={SINQ: Sinkhorn-Normalized Quantization for Calibration-Free Low-Precision LLM Weights}, 
      author={Lorenz K. Muller and Philippe Bich and Jiawei Zhuang and Ahmet Celik and Luca Benfenati and Lukas Cavigelli},
      year={2025},
      eprint={2509.22944},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={http://arxiv.org/abs/2509.22944}
}
```