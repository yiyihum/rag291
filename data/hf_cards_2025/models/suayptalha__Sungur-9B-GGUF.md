---
license: gemma
language:
- tr
base_model:
- suayptalha/Sungur-9B
pipeline_tag: text-generation
tags:
- sungur
- Turkish
- DPO
- gguf
- axolotl
- gemma2
---


<img src="./Sungur.png"/>

# Sungur-9B

This is the quantized version of [suayptalha/Sungur-9B](https://huggingface.co/suayptalha/Sungur-9B).

Sungur-9B is a Turkish-specialized large language model derived from ytu-ce-cosmos/Turkish-Gemma-9b-v0.1, which itself is based on Gemma-2-9b. The model was further trained using a 7k-sample Direct Preference Optimization (DPO) dataset created via translation and fine-tuned with 4-bit QLoRA, refining its alignment with human preferences.

Sungur-9B is designed for Turkish text generation tasks, producing coherent and contextually appropriate outputs. Its training process enables it to deliver fluent, context-aware responses.

## Turkish Evaluation Benchmark Results (via `malhajar17/lm-evaluation-harness_turkish`)

| Task / Dataset       | **suayptalha/Sungur-9B** | Qwen/Qwen2.5-7B-Instruct | google/gemma-2-9b-it | ytu-ce-cosmos/Turkish-Gemma-9b-v0.1 | google/gemma-3-12b-it | Qwen/Qwen2.5-14B-it | Qwen/Qwen2.5-32B-Instruct | google/gemma-2-27b-it | google/gemma-3-27b-it | Qwen/Qwen2.5-72B-Instruct | meta-llama/Llama-3-1-70B-Instruct |
| -------------------- | ------------------------ | ------------------------ | -------------------- | ----------------------------------- | --------------------- | ------------------- | ------------------------- | --------------------- | --------------------- | ------------------------- | --------------------------------- |
| **MMLU (tr)**        | **61.19**                | 56.31                    | 61.07                | 63.85                               | 63.92                 | 65.28               | 70.93                     | 66.49                 | 70.20                 | 77.28                     | 74.00                             |
| **Truthful_QA (tr)** | **55.21**                | 55.99                    | 55.77                | 54.21                               | 57.16                 | 59.00               | 57.87                     | 57.45                 | 57.06                 | 59.86                     | 51.41                             |
| **ARC (tr)**         | **55.03**                | 42.06                    | 56.31                | 59.64                               | 60.67                 | 50.00               | 57.00                     | 63.65                 | 66.98                 | 61.52                     | 59.64                             |
| **Hellaswag (tr)**   | **64.36**                | 44.71                    | 56.48                | 64.19                               | 62.00                 | 52.22               | 57.04                     | 63.86                 | 66.58                 | 61.98                     | 64.31                             |
| **Gsm8K (tr)**       | **74.49**                | 64.16                    | 63.10                | 73.42                               | 72.06                 | 76.77               | 77.83                     | 76.54                 | 77.52                 | 83.60                     | 66.13                             |
| **Winogrande (tr)**  | **63.43**                | 59.66                    | 62.09                | 64.53                               | 61.77                 | 58.77               | 61.77                     | 65.40                 | 65.80                 | 61.92                     | 66.90                             |

## Acknowledgments
- Thanks to [ytu-ce-cosmos](https://huggingface.co/ytu-ce-cosmos) for their amazing Turkish-Gemma-9b-v0.1 model.
- Thanks to [axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) for making the repository I used to make this model.
- Thanks to all Turkish open source AI community.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Citation

```
@misc{sungur_collection_2025,
  title        = {Sungur (Hugging Face Collection)},
  author       = {Şuayp Talha Kocabay},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/collections/suayptalha/sungur-68dcd094da7f8976cdc5898e}},
  note         = {Turkish LLM family and dataset collection}
}
```

## Support

<a href="https://www.buymeacoffee.com/suayptalha" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---
license: gemma2
---