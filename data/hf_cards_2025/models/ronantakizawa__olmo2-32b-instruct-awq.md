---
language:
- en
license: apache-2.0
base_model: allenai/OLMo-2-0325-32B-Instruct
tags:
- awq
- quantized
- 4-bit
- olmo2
- conversational
- llm-compressor
library_name: transformers
pipeline_tag: text-generation
---

# OLMo-2-0325-32B-Instruct AWQ 4-bit

This is a 4-bit AWQ quantized version of [allenai/OLMo-2-0325-32B-Instruct](https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct) using [LLM Compressor](https://github.com/vllm-project/llm-compressor).

## Key Features

- ✅ **32B parameters quantized to 4-bit** - 69% size reduction
- ✅ **Fully open model** - code, data, and training details all public
- ✅ **Post-trained on Tülu 3** - SFT → DPO → RLVR pipeline
- ✅ **Strong performance** - competitive with Llama 3.1 70B on many tasks
- ✅ **State-of-the-art on specific tasks** - MATH, GSM8K, IFEval

## Model Details

- **Base Model:** allenai/OLMo-2-0325-32B-Instruct (32B parameters)
- **Architecture:** OLMo 2 (fully open language model)
- **Quantization Method:** AWQ (Activation-aware Weight Quantization)
- **Quantization Scheme:** W4A16 (4-bit weights, 16-bit activations)
- **Calibration Dataset:** OpenOrca (128 samples)

## Size Comparison

| Metric | Value |
|--------|-------|
| **Original (BF16)** | ~64.0 GB |
| **Quantized (W4A16)** | ~16.91 GB |
| **Reduction** | ~73.6% |
| **Memory Saved** | ~47.1 GB |

## About OLMo 2

OLMo 2 is a series of fully open language models by the Allen Institute for AI:

- **Training:** Trained on Dolma dataset
- **Post-training:** Supervised finetuning, DPO, and RLVR on Tülu 3
- **Performance:** Competitive with much larger models
- **Openness:** All code, data, and training details released

### Performance Highlights

- **Average Score:** 68.8 across diverse benchmarks
- **GSM8K:** 87.6 (math reasoning)
- **IFEval:** 85.6 (instruction following)
- **MATH:** 49.7 (mathematical problem solving)
- **MMLU:** 77.3 (general knowledge)

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "ronantakizawa/olmo2-32b-instruct-awq-w4a16",
    trust_remote_code=True,
    torch_dtype="auto",
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(
    "ronantakizawa/olmo2-32b-instruct-awq-w4a16",
    trust_remote_code=True
)

# Chat template
messages = [
    {"role": "user", "content": "Explain quantum computing in simple terms."}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Chat Template

The model uses this chat template format:

```
<|user|>
How are you doing?
<|assistant|>
I'm just a computer program, so I don't have feelings, but I'm functioning as expected. How can I assist you today?<|endoftext|>
```

## System Prompt (Optional)

In Ai2 demos, this system prompt is used by default:

```
You are OLMo 2, a helpful and harmless AI Assistant built by the Allen Institute for AI.
```

However, the model has not been trained with a specific system prompt requirement.

## Quantization Details

- **Method:** AWQ (Activation-aware Weight Quantization)
- **Independent Pipeline:** Used with BasicPipeline for layer-by-layer quantization
- **Calibration:** 128 OpenOrca samples
- **Max Sequence Length:** 512 tokens
- **Why AWQ:** Preserves important weights based on activation patterns

## Requirements

- Transformers (install from main branch for OLMo 2 support)
- PyTorch with AWQ/GPTQ support
- 20GB+ GPU VRAM for inference

## Limitations

- Quantization may cause slight quality degradation compared to BF16
- Limited safety training (not production-ready without additional filtering)
- Primarily English language support

## License

Apache 2.0 (same as base model)

## Citation

```bibtex
@article{olmo20242olmo2furious,
      title={2 OLMo 2 Furious},
      author={Team OLMo and Pete Walsh and Luca Soldaini and others},
      year={2024},
      eprint={2501.00656},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.00656},
}
```

```bibtex
@misc{olmo2-32b-awq,
  title={OLMo-2-0325-32B-Instruct AWQ 4-bit},
  author={Quantized by ronantakizawa},
  year={2025},
  url={https://huggingface.co/ronantakizawa/olmo2-32b-instruct-awq-w4a16}
}
```

## Acknowledgements

- Base model by [Allen Institute for AI](https://allenai.org/)
- Quantization using [LLM Compressor](https://github.com/vllm-project/llm-compressor)

---

🤖 Generated with [LLM Compressor](https://github.com/vllm-project/llm-compressor)
