---
license: llama3.1
base_model: meta-llama/Llama-3.3-70B-Instruct
tags:
- quantized
- fp8
- compressed-tensors
- llama
- instruct
- 70b
library_name: transformers
pipeline_tag: text-generation
---

# Llama-3.3-70B-Instruct-FP8

This is a quantized version of Meta's Llama 3.3 70B Instruct model using FP8 quantization with compressed-tensors.

## Model Details

- **Base Model**: [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)
- **Quantization**: FP8 (8-bit float) using compressed-tensors
- **Model Size**: ~70.5B parameters
- **Quantized Size**: ~72.7GB (significantly reduced from original)
- **Architecture**: LlamaForCausalLM
- **Context Length**: 131,072 tokens
- **Quantization Method**: compressed-tensors v0.12.2

## Quantization Details

This model uses FP8 quantization with the following configuration:
- **Format**: float-quantized
- **Bits**: 8-bit float
- **Strategy**: tensor-level quantization
- **Observer**: minmax
- **Symmetric**: true
- **Target Layers**: Linear layers (excluding lm_head)

## Usage

### Using Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_name = "your-username/Llama-3.3-70B-Instruct-FP8"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Example usage
prompt = "Explain quantum computing in simple terms:"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Using with Compressed-Tensors

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from compressed_tensors import load_model

# Load the quantized model
model_name = "your-username/Llama-3.3-70B-Instruct-FP8"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = load_model(model_name, device_map="auto")
```

## Performance

- **Memory Usage**: Significantly reduced compared to the original model
- **Speed**: Faster inference due to reduced precision
- **Quality**: Minimal quality degradation with FP8 quantization

## Requirements

- `transformers >= 4.55.4`
- `compressed-tensors >= 0.12.2`
- `torch`
- `accelerate`

## Model Card

This model is a quantized version of Meta's Llama 3.3 70B Instruct model. The original model is designed for instruction-following tasks and general language understanding. The FP8 quantization reduces memory requirements while maintaining high performance.

### Training Data

This model inherits the training data from the base Llama 3.3 70B Instruct model.

### Intended Use

This model is intended for:
- Text generation
- Instruction following
- Code generation
- General language understanding tasks

### Limitations

- Quantization may introduce minor quality degradation
- Requires compatible hardware for optimal performance
- Large model size still requires significant computational resources

## Citation

```bibtex
@misc{llama33instruct,
  title={Llama 3.3 70B Instruct},
  author={Meta AI},
  year={2024},
  url={https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct}
}
```

## License

This model is released under the Llama 3.1 Community License. Please review the license terms before use.