---
library_name: transformers
pipeline_tag: text-generation
---

---

# wasm-32B-Instruct-V1

**wasm-32B-Instruct-V1** is a state-of-the-art instruction-tuned large language model developed by [wasmdashai](https://huggingface.co/wasmdashai). With 32 billion parameters, this model is designed to deliver high-quality performance across a wide range of natural language processing and code-related tasks,
## 🚀 Introduction

`wasm-32B-Instruct-V1` is built for instruction-following tasks and general-purpose reasoning. It leverages a powerful transformer architecture with optimized performance for large-scale generation tasks including:

* 🧠 Code generation and debugging
* 📚 Long-context understanding
* 🗣️ Multi-turn dialogue and reasoning
* 🔐 Privacy-conscious edge deployments (e.g., via WebAssembly)

This model is fine-tuned on diverse instruction datasets and optimized for both human alignment and computational efficiency.

## 🏗️ Model Details

* **Type**: Causal Language Model (Decoder-only)
* **Parameters**: 32 Billion
* **Training**: Pretraining + Instruction Fine-tuning
* **Architecture**: Transformer with:

  * Rotary Position Embeddings (RoPE)
  * SwiGLU activation
  * RMSNorm
  * Attention with QKV bias
* **Context Length**: Up to **32,768** tokens
* **Extended Context Option**: Via `rope_scaling` (supports up to 128K with YaRN)
* **Format**: Hugging Face Transformers-compatible

## ⚙️ Requirements

To use this model, install the latest version of 🤗 `transformers` (>= 4.37.0 recommended):

```bash
pip install --upgrade transformers
```

## 🧪 Quickstart

Here is a minimal example to load the model and generate a response:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "wasmdashai/wasm-32B-Instruct-V1"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

prompt = "Explain the concept of recursion with Python code."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
```

## 🧩 Processing Long Texts

This model supports **context lengths up to 32,768 tokens**. For even longer inputs, you can enable **YaRN** scaling by modifying the `config.json` as follows:

```json
{
  "rope_scaling": {
    "type": "yarn",
    "factor": 4.0,
    "original_max_position_embeddings": 32768
  }
}
```

This is ideal for handling documents, logs, or multi-step reasoning tasks that exceed standard limits.

## 📦 Deployment Notes

We recommend using `vLLM` for efficient deployment, especially with large input lengths or real-time serving needs. Please note:

* `vLLM` currently supports static YaRN only.
* Avoid applying rope scaling unless necessary for long-context tasks, as it may impact performance on short inputs.

## 📬 Contact

For support, feedback, or collaboration inquiries, please contact:

📧 **[modelasg@gmail.com](mailto:modelasg@gmail.com)**

---

