---
license: mit
datasets:
- Aquiles-ai/Medical-Reasoning
language:
- en
base_model:
- huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated
pipeline_tag: text-generation
library_name: transformers
tags:
- medical
- reasoning
- healthcare
- fine-tuned
- clinical
- deepseek-r1
- experimental
- merge
- qwen
- asclepio
---

# Asclepio-8B 🩺

![image](asclepio8b.png)

**Asclepio-8B** is a fine-tuned version of [huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated](https://huggingface.co/huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated) specialized in **medical reasoning and clinical decision-making**. Trained with high-quality data featuring step-by-step reasoning in `<think>` blocks, this model is designed to experiment with adapting large language models to healthcare-related tasks.

> ⚠️ **Important Note**: This model uses an "abliterated" (uncensored) version as its base because medical data can contain graphic descriptions of wounds, invasive procedures, and sensitive clinical cases that require processing without unnecessary restrictions.

## 🎯 Model Description

Asclepio-8B combines DeepSeek-R1's reasoning capabilities with specialized medical knowledge, supporting:
- **Step-by-step clinical reasoning** with `<think>` blocks
- **Differential diagnosis** based on symptoms and findings
- **Complex medical case analysis**
- **Structured responses** with detailed explanations
- **Evidence-based clinical decision-making**

## 🔧 Training Details

- **Base model:** `huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated`
- **Method:** LoRA (r=16, alpha=32)
- **Dropout:** 0.05
- **Target modules:** `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`
- **Dataset:** [Aquiles-ai/Medical-Reasoning](https://huggingface.co/datasets/Aquiles-ai/Medical-Reasoning)
  - 1,319,264 total examples
  - Conversational format (Hermes-style)
  - Includes chain-of-thought reasoning
- **Configuration:**
  - Total steps: 575
  - Learning rate: 2e-4 (cosine scheduler)
  - Max sequence length: 2048 tokens
  - Eval steps: 115
  - Optimized batch size with gradient accumulation
- **Hardware:**  NVIDIA L4 24GB VRAM
- **Training time:** ~6.7 hours

## 📊 Performance Metrics

| Metric | Final Value |
|--------|-------------|
| **Train Loss** | 0.8372 |
| **Eval Loss** | 0.9115 |
| **Train Accuracy** | 76.93% |
| **Eval Accuracy** | 76.36% |
| **Entropy (Train)** | 0.905 |
| **Entropy (Eval)** | 0.909 |

### Training Progression

| Step | Train Loss | Train Accuracy | Eval Loss | Eval Accuracy |
|------|-----------|----------------|-----------|---------------|
| 100  | 1.7316    | 61.34%         | -         | -             |
| 200  | 0.9218    | 74.98%         | 0.9593    | 75.38%        |
| 400  | 0.8919    | 75.33%         | 0.9331    | 75.90%        |
| 575  | 0.8372    | 76.93%         | 0.9115    | 76.36%        |

The model shows **stable convergence** with consistent improvement in accuracy and loss reduction, indicating effective learning without significant overfitting.

## 💻 Usage

### Installation

```bash
pip install transformers torch accelerate
```

### Basic Inference

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Aquiles-ai/Asclepio-8B"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cuda",
    dtype=torch.float16,
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

# Prompt
messages = [
    {"role": "user", "content": """You are a medical AI assistant with advanced reasoning capabilities. Provide detailed, step-by-step analysis for medical questions.

A 30-year-old man has 6/5 vision each eye, unaided. His cycloplegic retinoscopy is + 0.0D sph. at 1 metre distance. His complaints are blurring of newsprint at 30 cm, that clears up in about two minutes. The most probable diagnosis is –
A. Hypermetropia
B. Presbyopia
C. Accommodative inertia
D. Cycloplegia
"""},
]

# Tokenizer and model inference
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to('cuda')

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=8092,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

# Decode and print the output
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### Streaming Inference

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

model_id = "Aquiles-ai/Asclepio-8B"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cuda",
    dtype=torch.float16,
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

messages = [
    {"role": "user", "content": """You are a medical AI assistant with advanced reasoning capabilities. Provide detailed, step-by-step analysis for medical questions.

A 30-year-old man has 6/5 vision each eye, unaided. His cycloplegic retinoscopy is + 0.0D sph. at 1 metre distance. His complaints are blurring of newsprint at 30 cm, that clears up in about two minutes. The most probable diagnosis is –
A. Hypermetropia
B. Presbyopia
C. Accommodative inertia
D. Cycloplegia
"""},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to('cuda')

# Create the streamer
streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

# Build kwargs for generate
generate_kwargs = dict(
    **inputs,
    max_new_tokens=8092,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    streamer=streamer,
)

def _generate_thread(model, kwargs):
    with torch.no_grad():
        model.generate(**kwargs)

thread = Thread(target=_generate_thread, args=(model, generate_kwargs))
thread.start()

for chunk in streamer:
    print(chunk, end="", flush=True)
```

### Production Deployment with vLLM

**Start server:**

```bash
vllm serve Aquiles-ai/Asclepio-8B \
  --host 0.0.0.0 \
  --port 8000 \
  --api-key dummyapikey \
  --max-model-len=16384 \
  --async-scheduling \
  --gpu-memory-utilization=0.90
```

**Request to the server from the OpenAI client:**

```python
from openai import OpenAI

client = OpenAI(api_key="dummyapikey", base_url="http://127.0.0.1:8000/v1")

stream = client.chat.completions.create(
    model="Aquiles-ai/Asclepio-8B",
    messages=[{
        "role": "user",
        "content": """You are a medical AI assistant with advanced reasoning capabilities. Provide detailed, step-by-step analysis for medical questions.

A 30-year-old man has 6/5 vision each eye, unaided. His cycloplegic retinoscopy is + 0.0D sph. at 1 metre distance. His complaints are blurring of newsprint at 30 cm, that clears up in about two minutes. The most probable diagnosis is –
A. Hypermetropia
B. Presbyopia
C. Accommodative inertia
D. Cycloplegia
"""
    }],
    max_tokens=8092,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

**vLLM Benefits:** 20-30x faster inference, OpenAI-compatible API, continuous batching, async scheduling.

## 🚀 Capabilities & Limitations

### ✅ Supported Capabilities

- **Structured clinical reasoning** with `<think>` blocks
- **Differential diagnosis** based on clinical presentations
- **Medical case analysis** with multiple symptoms and findings
- **Detailed pathophysiological explanations**
- **Multiple-choice medical questions** with justification
- **Complementary test evaluation**

### ⚠️ Important Limitations

- **NOT a certified medical device** - Do not use for actual diagnosis
- **Requires professional validation** - All responses must be reviewed by qualified medical personnel
- **Limited to English text** - Primarily trained on English medical literature
- **Does not replace clinical judgment** - It's a support tool, not a substitute
- **May generate errors** - Like all LLMs, it can produce incorrect information
- **No access to real patient data** - Has no context of specific medical records

### 🎯 Best Use Cases

- **Medical education** and student training
- **Academic research** in clinical reasoning
- **Study assistant** for medical exam preparation
- **Prototyping** clinical decision support systems
- **Generating synthetic clinical cases** for training

## 📚 Dataset Information

The model was trained with [Aquiles-ai/Medical-Reasoning](https://huggingface.co/datasets/Aquiles-ai/Medical-Reasoning), which combines:

1. **medical-o1-reasoning-SFT** - Medical reasoning verified with GPT-4o
2. **ReasonMed** - 370K examples with knowledge-graph guided reasoning
3. **MedMCQA** - Medical multiple-choice questions

**Dataset features:**
- Hermes-style conversational format
- `<thinking>` blocks for explicit reasoning
- Evidence-based responses with medical explanations
- Coverage of multiple medical specialties

## 🔗 Related Products

### **Aquiles-RAG** - High-Performance RAG System

If you're building medical information systems, consider **Aquiles-RAG** to add semantic search capabilities:

- **Repository:** https://github.com/Aquiles-ai/Aquiles-RAG
- **PyPI:** `pip install aquiles-rag`
- **Features:**
  - Vector search (Redis HNSW, Qdrant, PostgreSQL pgvector)
  - FastAPI REST API
  - Embedding-agnostic architecture
  - Sync & async Python clients
  - Interactive setup wizard
  - Optional re-ranking

**Perfect for:** Medical literature search systems, clinical knowledge bases, medical documentation assistants.

## 📄 Citation

```bibtex
@misc{asclepio-8b-2025,
  author = {Aquiles-ai},
  title = {Asclepio-8B: Medical Reasoning with DeepSeek-R1 and Qwen Architecture},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/Aquiles-ai/Asclepio-8B}
}
```

## 🙏 Acknowledgments

- **HuiHui-AI** for the base model [DeepSeek-R1-0528-Qwen3-8B-abliterated](https://huggingface.co/huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated)
- **DeepSeek** for the R1 architecture with reasoning capabilities
- **Qwen Team** for the architectural foundation
- Dataset contributors: **FreedomIntelligence**, **Lingshu Medical**, **OpenLifeScience**

## ⚠️ Medical Disclaimer

**IMPORTANT: This model is for research and educational purposes only.**

- ❌ DO NOT use for actual medical diagnosis
- ❌ DO NOT replace consultation with healthcare professionals
- ❌ NO regulatory approval (FDA, EMA, etc.)
- ✅ Requires supervision and validation by qualified medical personnel
- ✅ Intended for research, education, and prototype development

Use of this model in real clinical contexts requires:
1. Rigorous clinical validation
2. Appropriate regulatory approval
3. Continuous supervision by medical professionals
4. Compliance with local health and privacy regulations (HIPAA, GDPR, etc.)

## 📜 License

MIT License - Same as the base model.

**Contact:** https://aquiles.vercel.app/  
**Version:** 1.0  
**Last Updated:** October 2025