---
library_name: transformers
license: apache-2.0
license-link: https://huggingface.co/radicalnumerics/RND1-Base-0910/blob/main/LICENSE
pipeline_tag: text-generation
---


<center>
<div style="text-align: center;">
  <img 
    src="https://huggingface.co/radicalnumerics/RND1-Base-0910/raw/main/rn-logo-animated.svg" 
    alt="Radical Numerics"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
</center>

<br>

# RND1-Base-0910

RND1 is an experimental diffusion language model with 30B parameters and 3B active parameters per token (sparse Mixture-of-Experts). This model was converted from a pretrained autoregressive base to enable diffusion-based text generation.

## Model Overview

**RND1-Base-0910** has the following features:
- Type: Diffusion Language Model
- Number of Parameters: 30.5B total, 3.3B activated per token
- Architecture: Sparse Mixture-of-Experts
- Training: Converted from pretrained autoregressive base (Qwen3-30BA3B)

For more details, see:

- Code: https://github.com/RadicalNumerics/RND1
- Report: https://www.radicalnumerics.ai/assets/rnd1_report.pdf
- Blog: https://www.radicalnumerics.ai/blog/rnd1

**Note:** RND1-Base-0910 has not been post-trained. Expect occasional repetition with greedy samplers.


## Installation

```bash
pip install torch transformers accelerate numpy rich
```

For faster inference with optimized MoE kernels:
```bash
pip install flashinfer-python
pip install sglang[all]
```

**Warning:** selecting a non-Huggingface backend is highly encouraged. When using `flashinfer-python`, JIT compilation may take a while.

## Quick Start

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

# Load model
model = AutoModelForMaskedLM.from_pretrained(
    "radicalnumerics/RND1-Base-0910",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("radicalnumerics/RND1-Base-0910")

# Generate - Task mode (for instructions and questions)
prompt = "Write a Python function that finds the longest common subsequence."
inputs = tokenizer(f"Question: {prompt}", return_tensors="pt").to(model.device)
output = model.generate(
    inputs=inputs.input_ids,
    max_new_tokens=256,
    num_diffusion_steps=256,
)
text = tokenizer.decode(output[0], skip_special_tokens=True)
print(text)
```

## Generation Parameters

Key parameters for text generation:

- `max_new_tokens`: Number of tokens to generate (default: 256)
- `num_diffusion_steps`: Diffusion denoising steps (default: 256)
- `temperature`: Sampling temperature, 0.0 for greedy (default: 0.0)
- `top_k`: Top-k filtering for sampling
- `top_p`: Nucleus filtering for sampling

## Generation Modes

**Task Mode** (default): For instructions, questions, or requests. Add "Question:" prefix to your prompt.

**Completion Mode**: For text continuation. Use prompt directly without prefix.

```python
# Completion mode example
prompt = "The key to understanding quantum computing lies in"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
output = model.generate(
    inputs=inputs.input_ids,
    max_new_tokens=256,
    num_diffusion_steps=256,
)
```

## Command-Line Interface

```bash
# Task mode
python demo_rnd_generation.py --prompt "Explain neural networks in simple terms"

# Completion mode
python demo_rnd_generation.py --mode completion --prompt "The future of AI"

# With sampling parameters
python demo_rnd_generation.py --top_k 50 --temperature 0.7 --prompt "Your prompt"
```

## Technical Details

RND1 uses a diffusion process for text generation, iteratively denoising random tokens over multiple steps. This approach differs from traditional autoregressive generation and enables parallel token generation within each diffusion step.

The model architecture is based on a sparse Mixture-of-Experts design, activating only a subset of parameters for each token to balance computational efficiency with model capacity.

## Citation

If you use RND1 in your research, please cite:

```
@misc{rnd1-report,
      title={Training Diffusion Language Models at Scale using Autoregressive Models}, 
      author={Radical Numerics},
      year={2025},
}
```
