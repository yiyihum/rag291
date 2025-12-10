---
library_name: transformers
tags: []
---

# 🐦 Curió 1.1B

## 📖 Overview

Curió 1.1B is a Portuguese-adapted language model created via continued pretraining of TinyLlama 1.1B (1T), originally trained on 1 trillion English tokens, on 150B Portuguese tokens from the ClassiCC-PT corpus.

This model was designed to explore the impact of language-specific corpora on adapting an English-trained base model to Portuguese, yielding performance improvements on Portuguese benchmarks without large-scale retraining from scratch.


## 🏗 Training Setup

- Base model: TinyLlama 1.1B (LLaMA-2 architecture)

- Parameters: 1.1B

- Continued pretraining tokens: 150B (ClassiCC-PT)

- Sequence length: 4096 tokens (with packing)

- Hardware: TPU v2-128 (thanks to Google TRC program)

- Frameworks: T5X


## 📊 Evaluation

Evaluated on the Poeta benchmark — 14 diverse Portuguese tasks (RTE, STS, MCQ exams, sentiment analysis, QA, etc.) — using the Normalized Preferred Metric (NPM).


| Model             | Training Regimen                             | Poeta v2 NPM |
| ----------------- | -------------------------------------------- | ------------ |
| TinyLlama 1T (EN) | –                                            | 17.4         |
| TinyLlama 2T (EN) | +1T EN continued pretraining                 | 20.9         |
| training with mC4-PT            | +150B PT (mC4-PT) continued pretraining           | \~20         |
| training with ClueWeb-22-PT     | +150B PT (Clueweb-22-PT) continued pretraining           | \~27         |
| **Curió 1.1B**    | +150B PT (ClassiCC-PT) continued pretraining | **27.1**     |




## 📥 Usage

Please note that **Curio 1.1B has not trained to be used as a chat model**

```
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "ClassiCC-Corpus/Curio-1.1B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

## 📜 Citation

If you use Curió 1.1B, please cite:
```
Coming soon
```


## Acknowledgements

We thank the google TRC program, which generously granted us the necessary resources for the development of this research.


