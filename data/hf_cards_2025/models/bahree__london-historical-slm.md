---
license: mit
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- gpt2
- historical
- london
- slm
- small-language-model
- text-generation
- history
- english
- safetensors
---

# London Historical LLM – Small Language Model (SLM)

A compact GPT-2 Small model (~117M params) **trained from scratch** on historical London texts (1500–1850). Fast to run on CPU, and supports NVIDIA (CUDA) and AMD (ROCm) GPUs.

> **Note**: This model was **trained from scratch** - not fine-tuned from existing models.

> This page includes simple **virtual-env setup**, **install choices for CPU/CUDA/ROCm**, and an **auto-device inference** example so anyone can get going quickly.

---

## 🔎 Model Description

This is a **Small Language Model (SLM)** version of the London Historical LLM, **trained from scratch** using GPT-2 Small architecture on historical London texts with a custom historical tokenizer. The model was built from the ground up, not fine-tuned from existing models.

### Key Features
- ~117M parameters (vs ~354M in the full model)  
- Custom historical tokenizer (≈30k vocab)  
- London-specific context awareness and historical language patterns (e.g., *thou, thee, hath*)  
- Lower memory footprint and faster inference on commodity hardware  
- **Trained from scratch** - not fine-tuned from existing models  

---

## 🧪 Intended Use & Limitations

**Use cases:** historical-style narrative generation, prompt-based exploration of London themes (1500–1850), creative writing aids.  
**Limitations:** may produce anachronisms or historically inaccurate statements; smaller models have less complex reasoning than larger LLMs. Validate outputs before downstream use.

---

## 🐍 Set up a virtual environment (Linux/macOS/Windows)

> Virtual environments isolate project dependencies. Official Python docs: `venv`.

**Check Python & pip**
```bash
# Linux/macOS
python3 --version && python3 -m pip --version
```

```powershell
# Windows (PowerShell)
python --version; python -m pip --version
```

**Create the env**

```bash
# Linux/macOS
python3 -m venv helloLondon
```

```powershell
# Windows (PowerShell)
python -m venv helloLondon
```

```cmd
:: Windows (Command Prompt)
python -m venv helloLondon
```

> **Note**: You can name your virtual environment anything you like, e.g., `.venv`, `my_env`, `london_env`.

**Activate**

```bash
# Linux/macOS
source helloLondon/bin/activate
```

```powershell
# Windows (PowerShell)
.\helloLondon\Scripts\Activate.ps1
```

```cmd
:: Windows (CMD)
.\helloLondon\Scripts\activate.bat
```

> If PowerShell blocks activation (*"running scripts is disabled"*), set the policy then retry activation:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# or just for this session:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## 📦 Install libraries

Upgrade basics, then install Hugging Face libs:

```bash
python -m pip install -U pip setuptools wheel
python -m pip install "transformers" "accelerate" "safetensors"
```

---

## Install **one** PyTorch variant (CPU / NVIDIA / AMD)

Use **one** of the commands below. For the most accurate command per OS/accelerator and version, prefer PyTorch's **Get Started** selector.

### A) CPU-only (Linux/Windows/macOS)

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### B) NVIDIA GPU (CUDA)

Pick the CUDA series that matches your system (examples below):

```bash
# CUDA 12.6
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# CUDA 12.4
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### C) AMD GPU (ROCm, **Linux-only**)

Install the ROCm build matching your ROCm runtime (examples):

```bash
# ROCm 6.3
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.3

# ROCm 6.2 (incl. 6.2.x)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2.4

# ROCm 6.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.1
```

**Quick sanity check**

```bash
python - <<'PY'
import torch
print("torch:", torch.__version__)
print("GPU available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("device:", torch.cuda.get_device_name(0))
PY
```

---

## 🚀 Inference (auto-detect device)

This snippet picks the best device (CUDA/ROCm if available, else CPU) and uses sensible generation defaults for this SLM.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "bahree/london-historical-slm"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

prompt = "In the year 1834, I walked through the streets of London and witnessed"
inputs = tokenizer(prompt, return_tensors="pt").to(device)

outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=50,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.2,
    no_repeat_ngram_size=3,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id,
    early_stopping=True,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## 🧪 **Testing Your Model**

### **Quick Testing (10 Automated Prompts)**
```bash
# Test with 10 automated historical prompts
python 06_inference/test_published_models.py --model_type slm
```

**Expected Output:**
```
🧪 Testing SLM Model: bahree/london-historical-slm
============================================================
📂 Loading model...
✅ Model loaded in 8.91 seconds
📊 Model Info:
   Type: SLM
   Description: Small Language Model (117M parameters)
   Device: cuda
   Vocabulary size: 30,000
   Max length: 512

🎯 Testing generation with 10 prompts...
[10 automated tests with historical text generation]
```

### **Interactive Testing**
```bash
# Interactive mode for custom prompts
python 06_inference/inference_unified.py --published --model_type slm --interactive

# Single prompt test
python 06_inference/inference_unified.py --published --model_type slm --prompt "In the year 1834, I walked through the streets of London and witnessed"
```

**Need more headroom later?** Load with 🤗 Accelerate and `device_map="auto"` to spread layers across available devices/CPU automatically.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
```

---

## 🪟 Windows Terminal one-liners

**PowerShell**

```powershell
python -c "from transformers import AutoTokenizer,AutoModelForCausalLM; m='bahree/london-historical-slm'; t=AutoTokenizer.from_pretrained(m); model=AutoModelForCausalLM.from_pretrained(m); p='In the year 1834, I walked through the streets of London and witnessed'; i=t(p,return_tensors='pt'); print(t.decode(model.generate(i['input_ids'],max_new_tokens=50,do_sample=True)[0],skip_special_tokens=True))"
```

**Command Prompt (CMD)**

```cmd
python -c "from transformers import AutoTokenizer, AutoModelForCausalLM ^&^& import torch ^&^& m='bahree/london-historical-slm' ^&^& t=AutoTokenizer.from_pretrained(m) ^&^& model=AutoModelForCausalLM.from_pretrained(m) ^&^& p='In the year 1834, I walked through the streets of London and witnessed' ^&^& i=t(p, return_tensors='pt') ^&^& print(t.decode(model.generate(i['input_ids'], max_new_tokens=50, do_sample=True)[0], skip_special_tokens=True))"
```

---

## 💡 Basic Usage (Python)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("bahree/london-historical-slm")
model = AutoModelForCausalLM.from_pretrained("bahree/london-historical-slm")

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

prompt = "In the year 1834, I walked through the streets of London and witnessed"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=50,
    do_sample=True,
    temperature=0.8,
    top_p=0.95,
    top_k=40,
    repetition_penalty=1.2,
    no_repeat_ngram_size=3,
    pad_token_id=tokenizer.pad_token_id,
    eos_token_id=tokenizer.eos_token_id,
    early_stopping=True,
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 🧰 Example Prompts

* **Tudor (1558):** "On this day in 1558, Queen Mary has died and …"
* **Stuart (1666):** "The Great Fire of London has consumed much of the city, and …"
* **Georgian/Victorian:** "As I journeyed through the streets of London, I observed …"
* **London specifics:** "Parliament sat in Westminster Hall …", "The Thames flowed dark and mysterious …"

---

## 🛠️ Training Details

* **Architecture:** GPT-2 Small (12 layers, hidden size 768)
* **Params:** ~117M
* **Tokenizer:** custom historical tokenizer (~30k vocab) with London-specific and historical tokens
* **Data:** historical London corpus (1500–1850)
* **Steps/Epochs:** 30,000 steps (extended training for better convergence)
* **Batch/LR:** 32, 3e-4 (optimized for segmented data)
* **Hardware:** 2× GPU training with Distributed Data Parallel
* **Final Training Loss:** 1.395 (43% improvement from 20K steps)
* **Model Flops Utilization:** 3.5% (excellent efficiency)
* **Training Method:** **Trained from scratch** - not fine-tuned
* **Context Length:** 256 tokens (optimized for historical text segments)
* **Status:** ✅ **Successfully published and tested** - ready for production use

---

## 🔤 Historical Tokenizer

* Compact 30k vocab targeting 1500–1850 English
* Tokens for **year/date/name/place/title**, plus **thames**, **westminster**, etc.; includes **thou/thee/hath/doth** style markers

---

## ⚠️ Troubleshooting

* **`ImportError: AutoModelForCausalLM requires the PyTorch library`**
  → Install PyTorch with the correct accelerator variant (see CPU/CUDA/ROCm above or use the official selector).

* **AMD GPU not used**
  → Ensure you installed a ROCm build and you're on Linux (`pip install ... --index-url https://download.pytorch.org/whl/rocmX.Y`). Verify with `torch.cuda.is_available()` and check the device name. ROCm wheels are Linux-only.

* **Running out of VRAM**
  → Try smaller batch/sequence lengths, or load with `device_map="auto"` via 🤗 Accelerate to offload layers to CPU/disk.

---

## 📚 Citation

If you use this model, please cite:

```bibtex
@misc{london-historical-slm,
  title   = {London Historical LLM - Small Language Model: A Compact GPT-2 for Historical Text Generation},
  author  = {Amit Bahree},
  year    = {2025},
  url     = {https://huggingface.co/bahree/london-historical-slm}
}
```

---

## Repository

The complete source code, training scripts, and documentation for this model are available on GitHub:

**🔗 [https://github.com/bahree/helloLondon](https://github.com/bahree/helloLondon)**

This repository includes:
- Complete data collection pipeline for 1500-1850 historical English
- Custom tokenizer optimized for historical text  
- Training infrastructure with GPU optimization
- Evaluation and deployment tools
- Comprehensive documentation and examples

### Quick Start with Repository
```bash
git clone https://github.com/bahree/helloLondon.git
cd helloLondon
python 06_inference/test_published_models.py --model_type slm
```

---

## 🧾 License

MIT (see [LICENSE](https://github.com/bahree/helloLondon/blob/main/LICENSE) in repo).
