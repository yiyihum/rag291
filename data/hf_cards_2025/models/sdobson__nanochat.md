---
language:
- en
license: mit
tags:
- text-generation
- transformer
- conversational
datasets:
- HuggingFaceFW/fineweb-edu
- cais/mmlu
- gsm8k
- HuggingFaceTB/smoltalk
model-index:
- name: nanochat
  results:
  - task:
      type: text-generation
    dataset:
      name: MMLU
      type: cais/mmlu
    metrics:
    - type: accuracy
      value: 31.51
  - task:
      type: text-generation
    dataset:
      name: GSM8K
      type: gsm8k
    metrics:
    - type: accuracy
      value: 4.55
  - task:
      type: text-generation
    dataset:
      name: HumanEval
      type: openai_humaneval
    metrics:
    - type: pass@1
      value: 8.54
---

# nanochat

**nanochat** is a 561M parameter transformer language model trained for conversational AI tasks. This model demonstrates that capable chat models
can be trained efficiently on modest hardware budgets (~$100 on 8x H100 GPUs).

Read about the process at https://samdobson.uk/posts/training-a-chatgpt-clone-for-cheap/

Chat with the model at https://huggingface.co/spaces/sdobson/nanochat

## Model Description

- **Developed by:** Andrej Karpathy
- **Trained by:** Sam Dobson
- **Model type:** Transformer-based causal language model
- **Language(s):** English
- **License:** MIT
- **Parameters:** 560,988,160 (~561M)

### Architecture

- **Layers:** 20
- **Hidden size:** 1280 channels
- **Attention heads:** 10
- **Head dimension:** 128
- **Vocabulary size:** 65,536 tokens

## Training Details

### Training Data

nanochat was trained in multiple stages:

1. **Pretraining:** 100B token subset of FineWeb-EDU (11.2B tokens processed)
2. **Midtraining:** SmolTalk conversations, MMLU multiple choice questions, GSM8K math problems
3. **Supervised Fine-tuning (SFT):** Conversational adaptation data

### Training Procedure

#### Tokenization
- Custom Rust-based tokenizer
- Vocabulary: 65,536 tokens
- Compression ratio: 4.8 characters per token

#### Training Infrastructure
- **Hardware:** 8x H100 GPUs (Lambda GPU Cloud)
- **Training time:** ~3 hours for pretraining stage
- **Estimated compute:** ~4e19 FLOPs
- **Total cost:** ~$100

#### Training Stages
The model was trained in three stages:
1. **Pretraining** on web text (FineWeb-EDU)
2. **Midtraining** on domain-specific datasets (reasoning, conversation, maths)
3. **Supervised fine-tuning** for chat optimisation

## Performance

### Benchmark Results

| Benchmark | Score | Description |
|-----------|-------|-------------|
| **MMLU**  | 23.99% | Multitask language understanding |
| **GSM8K** | 4.47% | Grade school math problems |
| **HumanEval** | 6.71% | Python code generation |
| **ARC-Easy** | 24.79% | Science questions (easy) |
| **ARC-Challenge** | 24.32% | Science questions (hard) |
| **ChatCORE** | 1.73% | Conversational reasoning |

## Intended Use

### Direct Use

nanochat is designed for:
- Conversational AI applications
- Research on efficient language model training
- Educational purposes for understanding LLM training pipelines
- Low-resource deployment scenarios

### Downstream Use

The model can be fine-tuned for specific conversational tasks or used as a base model for further domain adaptation.

### Out-of-Scope Use

- Production-grade conversational AI (the model is relatively small and has limited capabilities)
- Tasks requiring specialised knowledge or high accuracy
- Critical applications where errors could cause harm

## Limitations and Bias

- **Small scale:** At 561M parameters, this model has significantly fewer capabilities than larger models (1B+ parameters)
- **Limited training:** Trained on only 11.2B tokens, which is modest by modern standards
- **Performance:** Benchmark scores indicate limited reasoning and mathematical capabilities
- **Bias:** Inherits biases from training data (FineWeb-EDU, SmolTalk, etc.)
- **Language:** English-only

## Inference guide

Simon Willison created a script to allow this to run on CPU on MacOS:

```
  cd /tmp
  git clone https://huggingface.co/sdobson/nanochat
  uv run https://gist.githubusercontent.com/simonw/912623bf00d6c13cc0211508969a100a/raw/80f79c6a6f1e1b5d4485368ef3ddafa5ce853131/generate_cpu.py \
    --model-dir /tmp/nanochat \
    --prompt "Tell me about dogs."
```

Otherwise you can:

1. Download all files
2. Put `tokenizer.pkl` and `token_bytes.pt` in `~/.cache/nanochat/tokenizer`
3. Put `model_000650.pt` and `meta_000650.json` in `~/.cache/nanochat/chatsft_checkpoints/d20`
4. Clone https://github.com/karpathy/nanochat
5. Run `uv sync` followed by `uv run python -m scripts.chat_web`

## Citation

**Repository:** [github.com/karpathy/nanochat](https://github.com/karpathy/nanochat)

```bibtex
@software{nanochat2025,
  author = {Karpathy, Andrej},
  title = {nanochat: A 561M parameter conversational language model},
  year = {2025},
  url = {https://github.com/karpathy/nanochat}
}
```

## Model Card Author

Sam Dobson