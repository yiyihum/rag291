---
license: apache-2.0
language:
- en
tags:
- moe
- olmo
- flexolmo
co2_eq_emissions: 1
library_name: transformers
---

<img alt="FlexOlmo Logo." src="FlexOlmo_Logo.png" width="500px" style="display: block; margin-left: auto; margin-right: auto; margin-top: 50px"> FlexOlmo is a new kind of LM that unlocks a new paradigm of data collaboration. With FlexOlmo, data owners can contribute to the development of open language models without giving up control of their data. There is no need to share raw data directly, and data contributors can decide when their data is active in the model, deactivate it at any time, and receive attributions whenever it's used for inference.


# Model Summary
> FlexOlmo-7x7B-1T (without router training) is a Mixture-of-Experts with 33B total parameters, combining independently trained experts on public-mix, news, math, code, academic texts, creative writing, and Reddit data. The public-mix expert is trained on 1T tokens of public data while the other experts are branched from the public-mix expert and trained on 50B tokens of their respective data.

This information and more can also be found:
- **Paper**: https://allenai.org/papers/flexolmo
- **Code**: https://github.com/allenai/FlexOlmo
- **Blog**: https://allenai.org/blog/flexolmo
- **Data and corresponding models**:
| Corpus            | Public | Math | News           | Academic          | Code           | Creative Writing | Reddit         |
|------------------|----------------|----------------|----------------|----------------|----------------|------------------|----------------|
| Model            |  [Flex-public-7B-1T](https://huggingface.co/allenai/Flex-public-7B-1T) |  [Flex-math-2x7B-1T](https://huggingface.co/allenai/Flex-math-2x7B-1T) | [Flex-news-2x7B-1T](https://huggingface.co/allenai/Flex-news-2x7B-1T) | [Flex-pes2o-2x7B-1T](https://huggingface.co/allenai/Flex-pes2o-2x7B-1T) | [Flex-code-2x7B-1T](https://huggingface.co/allenai/Flex-code-2x7B-1T) |  [Flex-creative-2x7B-1T](https://huggingface.co/allenai/Flex-creative-2x7B-1T) | [Flex-reddit-2x7B-1T](https://huggingface.co/allenai/Flex-reddit-2x7B-1T) |


# Use

Install `transformers` with version `4.57.0` or newer and run:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

MODEL_NAME = "allenai/Flex-reddit-2x7B-1T"
TOKENIZER_NAME = "allenai/dolma2-tokenizer"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)
inputs = tokenizer("Bitcoin is", return_tensors="pt")
inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
out = model.generate(**inputs, max_length=64)
print(tokenizer.decode(out[0]))
```

# Evaluation Snapshot
| **Model** | **MC9** | **Gen5** | **MMLU** | **MMLU Pro** | **AGIEval** | **BBH** | **Math2** | **NewsG** | **PoemG** | **SciRIFF5** | **Code4** | **Avg.** |
|----------|--------|----------|----------|--------------|-------------|---------|-----------|-----------|-----------|--------------|-----------|----------|
| Prev. Public model | 68.7 | 58.8 | 55.9 | 26.2 | 39.9 | 35.7 | 8.2 | 76.0 | 47.8 | 48.1 | 1.1 | 42.4 |
| **Individual** |
| Math | 62.5 | 44.3 | 50.6 | 24.1 | 42.0 | 45.6 | **53.1** | 42.6 | 28.0 | 50.7 | 15.8 | 41.8 |
| Code| 40.5 | 39.4 | 29.5 | 14.5 | 27.4 | 38.1 | 6.0 | 45.1 | 28.2 | 48.0 | 21.0 | 30.7 |
| News | 46.5 | 48.6 | 36.4 | 15.2 | 25.7 | 30.9 | 2.5 | 77.7 | 26.9 | 47.0 | 0.0 | 32.5 |
| Creative Writing | 42.7 | 43.9 | 31.5 | 11.6 | 23.3 | 27.6 | 1.7 | 56.9 | **67.5** | 42.4 | 0.0 | 31.7 |
| Academic | 41.0 | 45.2 | 33.8 | 14.8 | 24.1 | 32.4 | 6.5 | 51.8 | 23.0 | 52.0 | 0.0 | 29.5 |
| Reddit | 64.7 | 36.5 | 56.1 | 25.5 | 35.5 | 19.7 | 2.5 | 54.1 | 8.6 | 32.7 | 1.7 | 30.7 |
| **Combined** |
| BTM (top-2) | 68.7 | 57.7 | 59.4 | 28.3 | 43.2 | 44.3 | 23.1 | 73.6 | 54.4 | 46.3 | **24.0** | 47.6 |
| 🔥 **FlexOlmo-7x7B-1T** | **70.4** | **60.1** | **60.2** | **30.5** | 44.8 | 46.8 | 47.9 | **78.3** | 66.2 | 53.8 | 14.6 | 52.0 |
| **FlexOlmo-7x7B-1T-RT** | 70.3 | 60.0 | **60.2** | 30.3 | **45.2** | **47.2** | 47.7 | 77.2 | **67.6** | **53.9** | 13.3 | **52.2** |

* The evaluation of the individual model refers to the dense model, not the 2x7B MoE model.


# Citation
```bibtex
@misc{flexolmo,
      title={FlexOlmo: Open Language Models for Flexible Data Use}, 
      author={Weijia Shi and Akshita Bhagia and Kevin Farhat and Niklas Muennighoff and Jacob Morrison and Evan Pete Walsh and Dustin Schwenk and Shayne Longpre and Jake Poznanski and Allyson Ettinger and Daogao Liu and Margaret Li and Mike Lewis and Wen-tau Yih and Dirk Groeneveld and Luca Soldaini and Kyle Lo and Noah A. Smith and Luke Zettlemoyer and Pang Wei Koh and Hannaneh Hajishirzi and Ali Farhadi and Sewon Min},
      year={2025},
      eprint={2507.00000},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://allenai.org/papers/flexolmo}, 
}
```
