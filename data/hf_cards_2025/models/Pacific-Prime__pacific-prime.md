---
language: en
license: cc-by-nc-4.0
tags:
- text-generation
- integrator-neuron
- custom-architecture
pipeline_tag: text-generation
---

# INL Architecture - Integrator Neuron Layer

**Production-ready neural architecture** using **Integrator Neuron dynamics** - replaces traditional FFN layers with iterative dynamics. **Universal architecture** that works for any type of model: LLMs, vision transformers, multimodal, diffusion, RL policies, etc.

### Architecture Features

- **Universal** - Build LLMs, vision models, audio, multimodal, diffusion, RL agents with same architecture
- **HuggingFace ready** - Drop-in replacement for FFN in any transformer
- **KV caching** - Full support for efficient autoregressive generation
- **Adaptive compute** - Auto-stops when converged (30-50% faster)
- **Parameter efficient** - Shared controllers = 96% fewer params than FFN
- **Bio-inspired** - Based on integrator neurons from neuroscience
- **Configurable** - Tune iterations, controllers, equilibrium for your task

### This Checkpoint

**Example implementation**: 1.1B parameter **language model** with INL architecture.
- 25 layers × 5 iterations/layer = rich iterative computation
- But the **architecture scales** from 100M to 100B+ params
- And works for **any domain** (language, vision, audio, etc.)

## What is INL?

**Traditional transformers** use static feedforward layers:
```python
x_out = x + FFN(x)  # One-shot computation
```

**INL-LLM** uses iterative integrator dynamics to find equilibrium:
```python
# Each of the 25 layers performs 5 iterations (configurable)
# Total: 25 layers × 5 iterations = 125 computation steps
for iteration in range(num_iterations_per_layer):  # = 5
    error = x - mu  # Distance from learned equilibrium
    v_next = alpha * v + (1 - alpha) * v_target - beta * error
    x_next = x + dt * gate * v_next
```

**Result**: The model "thinks" iteratively like biological integrator neurons, achieving better parameter efficiency through shared dynamics and adaptive early stopping.

## Model Details

| Parameter | Value |
|-----------|-------|
| Parameters | 1.1B |
| d_model | 1728 |
| Layers | 25 |
| Attention heads | 32 |
| Iterations/layer | 5 (configurable: more = better quality but slower) |
| Context length | 2048 |
| Vocabulary | 50,261 |

### Key Optimizations

- **Shared controllers**: One controller shared across all 25 layers (96% fewer parameters)
- **Low-rank embeddings**: 87% fewer embedding parameters
- **Adaptive stopping**: Stops when converged (30-50% faster inference)
- **Sparse excitation**: 90% sparsity for efficiency

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Pacific-Prime/pacific-prime",
    trust_remote_code=True,
    torch_dtype="bfloat16"
)
tokenizer = AutoTokenizer.from_pretrained("Pacific-Prime/pacific-prime")

# Generate with KV caching (default, much faster!)
prompt = "The future of AI is"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    temperature=0.8,
    use_cache=True  # Enable KV cache (default)
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Chat Format

```python
messages = [
    {"role": "user", "content": "What is machine learning?"}
]

chat_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(chat_text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
```

Special tokens: `<USER>`, `<ASSISTANT>`, `<SYSTEM>`, `<ERROR>`

## vLLM Serving

```bash
python -m vllm.entrypoints.openai.api_server \
    --model Pacific-Prime/pacific-prime \
    --trust-remote-code \
    --dtype bfloat16
```

## Why Integrator Neurons?

**Main benefit**: Achieve similar quality with fewer parameters through parameter sharing and iterative refinement.

- **Parameter efficiency**: One shared controller for all 25 layers (instead of 25 separate FFNs)
- **Adaptive computation**: Stops iterating early when converged (faster inference)
- **Iterative refinement**: Each layer "thinks" multiple times instead of one-shot computation
- **Interpretable**: Can visualize how the model converges to solutions
- **Bio-inspired**: Mimics integrator neurons found in neuroscience

## Learn More

For detailed technical documentation about the INL architecture:
- **GitHub Repository**: [ARKITEKTURE_TRANSFORMER_ADL](https://github.com/pacific-prime777/ARKITEKTURE_TRANSFORMER_ADL)
- **Architecture Docs**: See the repo for implementation details, training code, and benchmarks

## Optimizations

### KV Caching

Full KV caching support for fast autoregressive generation.

```python
# Automatic caching with .generate()
outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    use_cache=True  # Enable KV caching (default)
)

# Manual caching for custom generation loops
past_key_values = None
for _ in range(max_tokens):
    outputs = model(input_ids, past_key_values=past_key_values, use_cache=True)
    past_key_values = outputs.past_key_values
    # ... get next token ...
```

**Benefits**:
- **1.1-1.3× faster** generation for long sequences (100+ tokens)
- Compatible with HuggingFace `.generate()` and vLLM
- Beam search supported via `_reorder_cache()`
- Minimal memory overhead (<1%)

**How it works**: Unlike standard transformers that cache K, V for attention, INL-LLM only needs to cache attention states. Integrator dynamics (x, v) are computed fresh for each token since they operate within each layer, not across tokens.

**Performance Note**: The speedup is more modest than standard transformers (which get 10-20× gains) because **INL architecture is dominated by integrator iterations, not attention**. Most compute (70-90%) goes to iterative dynamics (3-10 iterations per layer × 12-25 layers), while attention is only ~10-30% of FLOPs. The cache optimizes that 10-30%, giving ~1.1-1.3× overall speedup. This is an architectural tradeoff - you get richer dynamics at the cost of less cache benefit.

## Technical Requirements

- Requires `trust_remote_code=True` (custom INL architecture)
- Python 3.8+, PyTorch 2.0+, transformers 4.35+

## Citation

```bibtex
@misc{inl-llm-2024,
  author = {Boris Peyriguère},
  title = {INL-LLM: Integrator Neural Language Model},
  year = {2024},
  url = {https://huggingface.co/Pacific-Prime/pacific-prime}
}
```

**License**: CC BY-NC 4.0 (Non-Commercial - Contact author for commercial use)
