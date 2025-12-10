---
license: apache-2.0
language:
- en
tags:
- moe
- olmo
- olmoe
co2_eq_emissions: 1
datasets:
- allenai/OLMoE-mix-0924
- allenai/dolmino-mix-1124
library_name: transformers
---

<img alt="OLMoE Logo." src="olmoe-logo.png" width="250px">


# Model Summary

> OLMoE-1B-7B is a Mixture-of-Experts LLM with 1B active and 7B total parameters released in January 2025 (0125) that is 100% open-source. It is an improved version of OLMoE-09-24, see the [paper appendix](https://arxiv.org/abs/2409.02060) for details.

This information and more can also be found on the [**OLMoE GitHub repository**](https://github.com/allenai/OLMoE).

- **Paper**: [arxiv.org/abs/2409.02060](https://arxiv.org/abs/2409.02060)
- **Pretraining** [Checkpoints](https://hf.co/allenai/OLMoE-1B-7B-0125), [Code](https://github.com/allenai/OLMo/tree/Muennighoff/MoE), [Data](https://huggingface.co/datasets/allenai/OLMoE-mix-0924) and [Logs](https://wandb.ai/ai2-llm/olmoe/reports/OLMoE-1B-7B-0924--Vmlldzo4OTcyMjU3).
- **SFT (Supervised Fine-Tuning)** [Checkpoints](https://huggingface.co/allenai/OLMoE-1B-7B-0125-SFT), [Code](https://github.com/allenai/open-instruct/tree/olmoe-sft), [Data](https://hf.co/datasets/allenai/tulu-v3.1-mix-preview-4096-OLMoE) and [Logs](https://github.com/allenai/OLMoE/blob/main/logs/olmoe-sft-logs.txt).
- **DPO/KTO (Direct Preference Optimization/Kahneman-Tversky Optimization)**, [Checkpoints](https://huggingface.co/allenai/OLMoE-1B-7B-0125-Instruct), [Preference Data](https://hf.co/datasets/allenai/ultrafeedback_binarized_cleaned), [DPO code](https://github.com/allenai/open-instruct/tree/olmoe-sft), [KTO code](https://github.com/Muennighoff/kto/blob/master/kto.py) and [Logs](https://github.com/allenai/OLMoE/blob/main/logs/olmoe-dpo-logs.txt).

# Use

Install `transformers` (version `4.45.0` or greater) & `torch` and run:

```python
from transformers import OlmoeForCausalLM, AutoTokenizer
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load different ckpts via passing e.g. `revision=step10000-tokens41B`
model = OlmoeForCausalLM.from_pretrained("allenai/OLMoE-1B-7B-0125").to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMoE-1B-7B-0125")
inputs = tokenizer("Bitcoin is", return_tensors="pt")
inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
out = model.generate(**inputs, max_length=64)
print(tokenizer.decode(out[0]))
# > # Bitcoin is a digital currency that is created and held electronically. No one controls it. Bitcoins aren’t printed, like dollars or euros – they’re produced by people and businesses running computers all around the world, using software that solves mathematical
```

You can list all revisions/branches by installing `huggingface-hub` & running:
```python
from huggingface_hub import list_repo_refs
out = list_repo_refs("allenai/OLMoE-1B-7B-0125")
branches = [b.name for b in out.branches]
```

Important branches:
- `step1200000-tokens5033B`: Pretraining checkpoint used for annealing. There are a few more checkpoints after this one but we did not use them.
- `main`: Checkpoint annealed from `step1200000-tokens5033B` for an additional 100B tokens (23,842 steps). We use this checkpoint for our adaptation (https://huggingface.co/allenai/OLMoE-1B-7B-0125-SFT & https://huggingface.co/allenai/OLMoE-1B-7B-0125-Instruct).
- `fp32`: FP32 version of `main`. The model weights were stored in FP32 during training but we did not observe any performance drop from casting them to BF16 after training so we upload all weights in BF16. If you want the original FP32 checkpoint for `main` you can use this one. You will find that it yields slightly different results but should perform around the same on benchmarks.

# Evaluation Snapshot

| Model                       | Active Params | Open Data | MMLU | HellaSwag | ARC-Chall. | ARC-Easy | PIQA | WinoGrande |
|-----------------------------|---------------|-----------|------|-----------|------------|----------|------|------------|
| **LMs with ~1B active parameters** |               |           |      |           |            |          |      |            |
| **OLMoE-1B-7B-0125**              | **1.3B**      | **✅**    | **56.3** | **81.7** | **67.5**   | **84.4** | 78.7 | **70.6**  |
| OLMoE-1B-7B-0924            | 1.3B          | ✅        | 54.1 | 80.0      | 62.1       | 84.2     | **79.8** | 70.2  |
| DCLM-1B                     | 1.4B          | ✅        | 48.5 | 75.1      | 57.6       | 79.5     | 76.6 | 68.1       |
| TinyLlama-1B                | 1.1B          | ✅        | 33.6 | 60.8      | 38.1       | 69.5     | 71.7 | 60.1       |
| OLMo-1B (0724)              | 1.3B          | ✅        | 32.1 | 67.5      | 36.4       | 53.5     | 74.0 | 62.9       |
| Pythia-1B                   | 1.1B          | ✅        | 31.1 | 48.0      | 31.4       | 63.4     | 68.9 | 52.7       |
| **LMs with ~2-3B active parameters** |               |           |      |           |            |          |      |            |
| Qwen1.5-3B-14B              | 2.7B          | ❌        | **62.4** | 80.0      | **77.4**   | **91.6** | **81.0** | 72.3 |
| Gemma2-3B                   | 2.6B          | ❌        | 53.3 | 74.6      | 67.5       | 84.3     | 78.5 | 71.8       |
| JetMoE-2B-9B                | 2.2B          | ❌        | 49.1 | **81.7**  | 61.4       | 81.9     | 80.3 | 70.7       |
| DeepSeek-3B-16B             | 2.9B          | ❌        | 45.5 | 80.4      | 53.4       | 82.7     | 80.1 | **73.2**   |
| StableLM-2B                 | 1.6B          | ❌        | 40.4 | 70.3      | 50.6       | 75.3     | 75.6 | 65.8       |
| OpenMoE-3B-9B               | 2.9B          | ✅        | 27.4 | 44.4      | 29.3       | 50.6     | 63.3 | 51.9       |
| **LMs with ~7-9B active parameters** |               |           |      |           |            |          |      |            |
| Gemma2-9B                   | 9.2B          | ❌        | **70.6** | **87.3**  | **89.5**   | **95.5** | **86.1** | **78.8** |
| Llama3.1-8B                 | 8.0B          | ❌        | 66.9 | 81.6      | 79.5       | 91.7     | 81.1 | 76.6       |
| DCLM-7B                     | 6.9B          | ✅        | 64.4 | 82.3      | 79.8       | 92.3     | 80.1 | 77.3       |
| Mistral-7B                  | 7.3B          | ❌        | 64.0 | 83.0      | 78.6       | 90.8     | 82.8 | 77.9       |
| OLMo-7B (0724)              | 6.9B          | ✅        | 54.9 | 80.5      | 68.0       | 85.7     | 79.3 | 73.2       |
| Llama2-7B                   | 6.7B          | ❌        | 46.2 | 78.9      | 54.2       | 84.0     | 77.5 | 71.7       |

# Citation

```bibtex
@misc{muennighoff2024olmoeopenmixtureofexpertslanguage,
      title={OLMoE: Open Mixture-of-Experts Language Models}, 
      author={Niklas Muennighoff and Luca Soldaini and Dirk Groeneveld and Kyle Lo and Jacob Morrison and Sewon Min and Weijia Shi and Pete Walsh and Oyvind Tafjord and Nathan Lambert and Yuling Gu and Shane Arora and Akshita Bhagia and Dustin Schwenk and David Wadden and Alexander Wettig and Binyuan Hui and Tim Dettmers and Douwe Kiela and Ali Farhadi and Noah A. Smith and Pang Wei Koh and Amanpreet Singh and Hannaneh Hajishirzi},
      year={2024},
      eprint={2409.02060},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.02060}, 
}
```