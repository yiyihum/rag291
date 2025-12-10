---
license: apache-2.0
datasets:
- AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations
language:
- en
pipeline_tag: text-generation
tags:
- mixture-of-experts
- moe
- expert-pruning
- gpt-oss
- openai
- reasoning
- all
- specialized
- efficient
- transformer
- causal-lm
- text-generation
- pytorch
- pruned-model
- domain-specific
---

# All GPT-OSS Model (12 Experts)

**Project**: https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/

<div align="center">

### 👥 Follow the Authors

**Aman Priyanshu**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aman-priyanshu/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/AmanPriyanshu6)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://amanpriyanshu.github.io/)

**Supriti Vijay**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/supriti-vijay/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/SupritiVijay)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://supritivijay.github.io/)

</div>

## Introduction

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 12 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for all tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~9.0B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 12 |
| **Layers** | 24 |
| **Top-k Routing** | 4 |
| **Context Length** | 128K tokens |
| **Attention Heads** | 64 (Query), 8 (Key-Value) |
| **Residual Dimension** | 2880 |
| **Attention Pattern** | Alternating dense & sliding window (128 tokens) |
| **Positional Encoding** | RoPE (Rotary Position Embedding) |
| **Normalization** | RMSNorm |
| **Precision** | BF16 |
| **License** | Apache 2.0 |
| **Specialization** | All |

## Pruning Methodology

### What is Expert Pruning?
Mixture-of-Experts models contain multiple specialized sub-networks (experts) per layer. During inference, only a subset of experts are activated for each token. Expert pruning involves:

1. **Analyzing Usage Patterns**: Tracking which experts activate most frequently for specific tasks
2. **Removing Underutilized Experts**: Discarding experts with low activation rates for the target domain
3. **Preserving Router Functionality**: Maintaining the routing mechanism with fewer available experts

### Our Approach
- **Data-Driven Selection**: Used activation patterns from all evaluation tasks
- **Systematic Reduction**: Reduced from 32 to 12 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 37.5% of original expert parameters
- **Reduced Computational Load**: Fewer routing decisions during inference
- **Focused Capabilities**: Retains experts relevant to all tasks

### Use Cases
- **Speculative Decoding**: Draft model for full GPT-OSS-20B
- **Resource-Constrained Deployment**: Edge devices, mobile applications
- **Research**: Study expert specialization in MoE models
- **Fine-tuning**: Smaller base model for domain adaptation

*Note: Performance may vary depending on how well the pruned experts match your specific use case.*

## Motivation & Expert Selection

This general-purpose model maintains broad capabilities across all domains while significantly reducing computational requirements. It preserves the essential routing patterns discovered across our comprehensive analysis of diverse evaluation benchmarks including GPQA, MMLU, SORRY-Bench, and Tulu3 datasets.

The expert selection process utilized our comprehensive analysis of router activation patterns across multiple evaluation benchmarks:

- **GPQA**: Graduate-level questions in physics, chemistry, biology (Diamond & Expert subsets)
- **MMLU/MMLU-Pro**: Comprehensive knowledge across 57+ subjects including science, medicine, law
- **SORRY-Bench**: Safety evaluation across harmful content categories  
- **Tulu3**: Persona-driven instruction following with verifiable constraints
- **Polyglot-or-Not**: Multilingual factual completion tasks

By identifying experts that consistently activated for all tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 12 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 12 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-9.0b-specialized-all-pruned-moe-only-12-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-9.0b-specialized-all-pruned-moe-only-12-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What is artificial intelligence and how does it work?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Ensure inputs are on the same device as model
inputs = {k: v.to(model.device) for k, v in inputs.items()}

outputs = model.generate(
    **inputs, 
    max_new_tokens=512,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id
)

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### Apple Silicon (MPS) Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Check MPS availability and load model
device = "mps" if torch.backends.mps.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-9.0b-specialized-all-pruned-moe-only-12-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-9.0b-specialized-all-pruned-moe-only-12-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What is artificial intelligence and how does it work?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Move inputs to model device
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

# Use torch.no_grad for MPS stability
with torch.no_grad():
    outputs = model.generate(
        **inputs, 
        max_new_tokens=512,
        do_sample=True,
        temperature=0.1,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=True
    )

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### GPU Inference

For CUDA GPU inference, the models work with minimal modifications from the CPU example above. Simply change:
```python
device_map="auto"  # Will automatically use GPU if available
torch_dtype=torch.bfloat16  # or torch.float16
```

## Model Examples

The following examples demonstrate the model's performance on all tasks:

### Example 1
**Question:** What is artificial intelligence and how does it work?

**Response:**
```
<|channel|>analysis<|message|>Need explain AI concept, types, how works.<|end|><|start|>assistant<|channel|>final<|message|>## 1. What is Artificial Intelligence?

Artificial Intelligence (AI) is a set of computational techniques that let machines “think” and “act” in ways that resemble human cognition.  In short, AI is a **software system that can learn, reason, and make decisions** without a human brain.

| **Key Features** | **What Makes It “Artificial”** | **What Makes It “Intelligent”** |
|-------------------|---------------------------|---------------------------|
| **Learning** | Learges from data it has seen | Learges from patterns, not from a pre‑built rule set |
| **Reasoning** | Uses logic, inference, and prediction | Can generate new solutions to problems |
| **Generalization** | Works on a wide range of tasks | Adises to new contexts |
| **Autonomy** | Can act without explicit human control | Makes decisions that are useful or optimal |

AI is not a single technology; it is a **family of methods** that can be combined to build a system that can:

* **Recognize** patterns in images, text, or sound (image, speech, text recognition)
* **Predict** future events from past data (forecasting, recommendation)
* **Generate** new content (writing, music, art)
* **Plan** and **solve** problems (planning, optimization, game‑playing)

---

## 2. How AI Works – The Core Ingredients

### 2.1 Data

AI starts with a **dataset** – a collection of facts, images, or text. The data can be:

* **Structured** (labels, categories) – e.g., a labeled dataset of “cat” vs “dog” images.
* **Unstructured** (raw, noisy) – e.g., millions of tweets with no labels.

### 2.2 Representation

The data is turned into a **machine‑readable format**:

* **Text → Tokens** (words, characters)
* **Images → Pixels + Features** (color, shape, texture)
* **Audio → Frequencies** (pitch, timo)

### 2.3 Training

The system learns by **exposing it to the data** and letting it **try** to answer a question. The learning process is usually:

| **Method** | **What Happens** | **Why It Works** |
|------------|-----------------|-----------------|
| **Revised
```

---

### Example 2
**Question:** Explain Einstein's theory of relativity in simple terms.

**Response:**
```
<|channel|>analysis<|message|>Need simple explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Einstein’s Theory of Relativity – in plain words**

---

### 1. What the idea is

Einstein’s theory says that **the way we measure distances, time, and mass changes when objects move very fast or very far from each other**. In everyday physics we treat objects as if they are “fixed” in space, but when they are moving, especially over huge distances, that’s not true.

---

### 2. The two main ideas

| Concept | What we normally think | What Einstein says |
|--------|------------------------|------------------------|
| **Time** | “Time is the same everywhere.” | Time *depends* on the motion of an object. If something moves, the time it takes to travel changes. |
| **Mass** | “Mass is a fixed property of an object.” | Mass *depends* on the motion of an object. An object can appear heavier or lighter depending on where it is. |

---

### 3. How it works – the “clock” example

1. **Two clocks on a moving spaceship**  
   - Clock A is on the spaceship.  
   - Clock B is on a planet far away.  

2. **If the spaceship is moving toward the planet**  
   - Clock A’s time ticks *slier* than Clock B’s time.  
   - The difference in the time between the two clocks is exactly the *speed* of the spaceship.  

3. **If the spaceship is moving away from the planet**  
   - Clock A’s time ticks *fier* than Clock B’s time.  
   - The difference is again the speed, but now in the opposite direction.  

So the *time difference* between two clocks tells us how fast the spaceship is moving. That’s the “time moves with the object” part.

---

### 4. Mass changes the same way

If we look at a *mass* (like a ball) on the spaceship:

- While the spaceship is moving toward the planet, the ball’s mass appears *smaller* than it would be on the planet.  
- While the spaceship is moving away, the ball’s mass appears *larger*.  

The change in mass is exactly the same as the change in time. That’s the “mass changes with the object” part.

---

### 5. Why it matters

- **Gravity**: The theory explains why a ball feels heavier when it
```

---

### Example 3
**Question:** How does democracy function in modern governments?

**Response:**
```
<|channel|>analysis<|message|>Need explain concept, institutions, checks, participation, representation, accountability, checks of power, etc.<|end|><|start|>assistant<|channel|>final<|message|>### 1.  What is “democracy” in today’s world?

In the 21‑st‑century, democracy is usually understood as a **system of government in which the people have the ultimate authority** over the state’s policies, laws, and leaders.  The core ideas are:

| Feature | How it works in practice |
|--------|------------------------|
| **Representative** | Citizens elect elected officials (parliament, council, etc.) who act on the public’s will. |
| **Participative** | Citizens can influence policy through voting, petitions, public debate, protests, and civic engagement. |
| **Accountable** | Leaders are answerable to the public, through elections, oversight bodies, and the media. |
| **Rule‑of‑law** | Laws are made, interpreted, and enforced by independent institutions (cour courts, judiciary). |
| **Checks of power** | Separation of branches (executive, legislative, judiciary) and checks (epar, oversight, civil‑rights). |

### 2.  How democracy shows itself in modern governments

| Institutional | What does it do? | Typical examples |
|----------------|----------------|----------------|
| **Parleg‑/Council** | Elects leaders, drafts laws, debates policy. | Parliament (UK, Australia), Senate (US), Legislative Assembly (India). |
| **Executive** | Implements policy, runs day‑of‑the‑state. | President/Prime‑Minister, Cabinet. |
| **Judiciary** | Interinterpres law, protects rights. | Courts, Supreme Court, Constitutional Review Board. |
| **Civil‑Rights Bodies** | Protect minority rights, ensure fairness. | Human‑Rights Commission, Ombudsman. |
| **Media & NGOs** | Inform the public, hold leaders in check. | Newspapers, watchdog groups. |
| **E‑polling & Digital Platforms** | Facilitate voting, debate, data‑analysis. | Online voting pilots, social‑media campaigns. |

### 3.  The “checks” that keep democracy alive

1. **Separation of branches** – The executive, legislative, and judiciary are independent.  
2. **Checks & balances** – Overswatch committees, parliamentary oversight, judicial review.  
3. **Transparency** – Open‑data portals, public‑record of‑decations,
```

---

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{priyanshu2025gptoss,
  title={{GPT-OSS MoE Expert Fingerprinting: Analyzing Expert Activation Patterns in Mixture of Experts Models}},
  author={Priyanshu, Aman and Vijay, Supriti},
  year={2025},
  howpublished={\url{https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/}},
  note={Interactive analysis tool for expert activation patterns in MoE architectures}
}
```

## References & Resources

- **Original Model**: [OpenAI GPT-OSS Model Card](https://openai.com/index/introducing-gpt-oss/)
- **Model Hub**: [GPT-OSS-20B on Hugging Face](https://huggingface.co/openai/gpt-oss-20b)
- **Expert Analysis Dataset**: [GPT-OSS-20B MoE Expert Activations](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations)
- **Project Page**: [GPT-OSS MoE Expert Fingerprinting](https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/)
- **GitHub Repository**: [OpenAI GPT-OSS](https://github.com/openai/gpt-oss)
