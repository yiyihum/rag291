---
base_model: meta-llama/Llama-3.2-1B
datasets:
- yahma/alpaca-cleaned
language: en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- tptt
- peft
- trust_remote_code
---

# Titanesque-Llama-3.2-1B

<p align="center">
    <a href="https://arxiv.org/abs/2506.17671">
        <img alt="arXiv" src="https://img.shields.io/badge/arXiv-tptt-blueviolet.svg">
    </a>
    <a href="https://pypi.org/project/tptt/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/tptt?color=orange">
    </a>
    <a href="https://github.com/fabienfrfr/tptt/">
        <img alt="Release" src="https://img.shields.io/github/v/release/fabienfrfr/tptt?color=brightgreen">
    </a>
    <a href="https://fabienfrfr.github.io/tptt/">
        <img alt="Documentation" src="https://img.shields.io/badge/docs-online-blue">
    </a>
    <a href="https://huggingface.co/ffurfaro">
        <img alt="HuggingFace" src="https://img.shields.io/badge/hf-ffurfaro-yellow">
    </a>
</p>

Titanesque version of `meta-llama/Llama-3.2-1B` with parallel linearized attention (TPTT 😊) and PEFT.

The architecture was presented in the paper [TPTT: Transforming Pretrained Transformers into Titans](https://huggingface.co/papers/2506.17671).

## Abstract
Transformer-based large language models (LLMs) have achieved strong performance across many natural language processing tasks. Nonetheless, their quadratic computational and memory requirements, particularly in self-attention layers, pose challenges for efficient inference on long contexts and for deployment in resource-limited environments. We present TPTT (Transforming Pretrained Transformers into Titans), a framework designed to augment pretrained Transformers with linearized attention (LiZA) and internal memory gating via Memory as Gate (MaG), applied without full retraining. TPTT supports parameter-efficient fine-tuning (LoRA) and integrates with standard toolkits such as Hugging Face Transformers. We evaluated TPTT on several pretrained models, including Llama-1B, OlMoE-1B-7B, Qwen2.5-1.5B, Gemma3-270m, OpenELM-1.3B, and Mistral-7B, in order to assess applicability across architectures of different scales. Experiments on models with approximately 1 billion parameters, evaluated primarily on the MMLU benchmark, suggest potential improvements in both efficiency and accuracy compared to baseline models. For example, Titans-Llama-1B exhibited up to a 20% relative increase in Exact Match scores in one-shot evaluation. An additional finding is that it is possible to convert a quadratic-attention model into a purely linear-attention model using the DeltaProduct mechanism. All training runs were carried out with modest computational resources. These preliminary findings indicate that TPTT may help adapt pretrained LLMs for long-context tasks with limited overhead. Further studies on larger models and a broader set of benchmarks will be necessary to evaluate the generality and robustness of the framework. Code is available at this https URL . Python package at this https URL .

## Model list

Classic model parameter with LiZA injection :

| Subfolder                      | Max Self Attn Length | Mag Weight | Cross Gate | Max Chunk Size | Bidirectional | LoRA | Description                                           |
|-------------------------------|----------------------|------------|------------|----------------|---------------|------|-------------------------------------------------------|
| delta_rule  | 8192 (default)       | 0.5        | False      | 64             | False         | Yes  | Parallel linearized attention with delta_rule operator|
| delta_rule_gelu | 8192 (default) | 0.5        | False      | 64             | False         | Yes  | Non-linear operator with gelu activation              |
| delta_product    | 8192 (default) | 0.5        | False      | 64             | False         | Yes  | Second order operator with derivative trick              |
| delta_product_r  | 8192 (default) | 0.5        | False      | 64             | False         | Yes  | Second order operator with rotative trick             |
| delta_product_c  | 8192 (default) | 0.5        | False      | 64             | False         | Yes  | Second order operator with combined trick             |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
"ffurfaro/Titanesque-Llama-3.2-1B",
subfolder="tptt_subfolder", # see in repo tree
trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("ffurfaro/meta-llama/Llama-3.2-1B")

prompt = "Your prompt here"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs, skip_special_tokens=True))

```


## Citation & Contact

If you use TPTT in your academic work, please cite [Furfaro](https://huggingface.co/ffurfaro). For questions or support, please open an issue on the [GitHub repository](https://github.com/fabienfrfr/tptt) or contact the maintainer.

---