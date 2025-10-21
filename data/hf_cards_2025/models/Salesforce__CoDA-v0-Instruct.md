---
language:
- en
library_name: transformers
license: cc-by-nc-4.0
pipeline_tag: text-generation
tags:
- text diffusion model
- language model
- code generation
arxiv: 2510.0327
---

# CoDA: Coding LM via Diffusion Adaptation

<p align="center">
  <img alt="coda-logo" src="https://raw.githubusercontent.com/weirayao/CoDA/main/CoDA-logo.png">
</p>

<p align="center">
  <a href="https://github.com/SalesforceAIResearch/CoDA"><strong>Try CoDA</strong></a> ·
  <a href="https://huggingface.co/papers/2510.03270"><strong>Paper</strong></a> ·
  <a href="https://huggingface.co/collections/Salesforce/coda-68d627d87921c0e28a69e340"><strong>Model Collection</strong></a> ·
  <a href="https://github.com/SalesforceAIResearch/CoDA/blob/main/README.md"><strong>GitHub Repository</strong></a>
</p>

<br>

Welcome to CoDA, Salesforce AI Research's diffusion-based language model designed for powerful code generation and bidirectional context understanding, presented in the paper [CoDA: Coding LM via Diffusion Adaptation](https://huggingface.co/papers/2510.03270).

We're releasing CoDA as a lightweight yet capable model:
- `CoDA-1.7B-Instruct` — optimized for code generation tasks with bidirectional diffusion modeling (1.7B parameters)
- `CoDA-1.7B-Base` — diffusion foundation model with bidirectional diffusion architecture, ideal for further fine-tuning and RL training

CoDA leverages discrete diffusion processes to enable understanding of both past and future tokens, making it uniquely suited for code completion and generation tasks where context flows in both directions.

> [!NOTE]
> This model card is dedicated to the `CoDA-1.7B-Instruct` model. Check out our [model collection](https://huggingface.co/collections/Salesforce/coda-68d627d87921c0e28a69e340) for other variants.

# ⭐ Highlights

*   **Bidirectional Context Understanding:** Leverage discrete diffusion processes to understand both past and future tokens, enabling superior code completion.
*   **Confidence-Guided Sampling:** Maintain competitive inference latency through intelligent sampling strategies that balance quality and speed.
*   **Lightweight Architecture:** Achieve strong performance with only 1.7B parameters, making it accessible for researchers with limited computational resources.
*   **Full Training Pipeline:** Complete reproducible training pipeline from pre-training to fine-tuning, enabling customization for specific domains.
*   **Optimized for Code:** Specifically designed and trained for code generation tasks, with strong performance on HumanEval, MBPP, and other coding benchmarks.

---

## 📊 Model Details

-   **Model Size**: 1.7B parameters
-   **Architecture**: Diffusion-based language model
-   **Training**: TPU-based pre-training with GPU fine-tuning
-   **Primary Use**: Code generation and completion tasks

## ✨ Key Features

-   **Bidirectional Context**: Diffusion modeling enables understanding of both past and future tokens
-   **Confidence-Guided Sampling**: Maintains competitive inference latency through intelligent sampling
-   **Lightweight Design**: Achieves strong performance with fewer parameters than comparable models
-   **Open Training Pipeline**: Fully reproducible training from pre-training to fine-tuning

## 📈 Performance

CoDA-1.7B-Instruct demonstrates competitive performance on standard code generation benchmarks:

| Model | HumanEval | HumanEval+ | MBPP | MBPP+ | EvalPlus |
|-------|-----------|------------|------|-------|----------|
| **CoDA-Base** | 29.3 | 23.8 | 35.2 | 46.0 | 34.9 |
| **CoDA-Instruct** | **54.3** | **47.6** | 47.2 | **63.2** | **55.4** |
| Dream-Base | 56.7 | 50.0 | 68.7 | 57.4 | 53.7 |
| Dream-7B-Instruct | 57.9 | 53.7 | 68.3 | 56.1 | 54.9 |
| LLaDA-8B-Instruct | 35.4 | 31.7 | 31.5 | 28.6 | 30.2 |

**🎯 Key Finding**: CoDA-1.7B-Instruct matches or surpasses diffusion models up to 7B parameters while maintaining significantly lower computational requirements. CoDA offers an advantageous balance between inference speed and accuracy compared to larger diffusion models.

## 🎓 Training Methodology

CoDA employs a three-stage training process:

*Three-stage training: (1) Pre-training with bidirectional masking, (2) Post-training with instruction format, (3) Inference with progressive denoising.*

## 🛠️ Usage

### 🚀 Quick Start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Salesforce/CoDA-v0-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate code
prompt = "Write a Python function to calculate fibonacci numbers"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    **inputs,
    max_tokens=256,
    diffusion_steps=128,
    temperature=0.0
)
print(tokenizer.decode(outputs[0]))
```

### 🚀 Deployment

For production deployment, we provide serving with OpenAI-compatible APIs:

```bash
# Clone the repository
git clone https://github.com/SalesforceAIResearch/CoDA
cd CoDA

# Set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r serving/requirements.txt

# Export your Hugging Face token
export HF_TOKEN="hf_..."

# Start the server
bash serving/fast-api/start_server.sh
```

The server will listen on `http://localhost:8000`.

### 💬 Interactive CLI

```bash
python serving/fast-api/chat_cli.py \
  --base-url http://localhost:8000 \
  --model Salesforce/CoDA-v0-Instruct \
  --stream \
  --show-meta
```

### ⚙️ Generation Hyperparameters

Customize generation behavior with environment variables:

```bash
export MAX_TOKENS=512          # Maximum tokens to generate
export TEMPERATURE=0.7         # Sampling temperature
export TOP_P=0.9              # Nucleus sampling threshold
export STEPS=128              # Number of diffusion steps
export ALG="entropy"          # Sampling algorithm
export ALG_TEMP=0.1           # Algorithm temperature
export BLOCK_LENGTH=32        # Block size for processing
```

**Recommended Settings**:
- **Fast inference**: `STEPS=64`, `TEMPERATURE=0.0`
- **Quality generation**: `STEPS=128`, `TEMPERATURE=0.7`, `TOP_P=0.9`
- **High quality**: `STEPS=256`, `TEMPERATURE=0.5`, `TOP_P=0.95`

## 🔧 Training from Scratch

The complete training pipeline is available in our [repository](https://github.com/SalesforceAIResearch/CoDA):

```bash
# Clone the repository
git clone https://github.com/SalesforceAIResearch/CoDA
cd CoDA
```

### 🧠 Pre-training on TPU
```bash
# Configure TPU environment
cd pre-train
cp env.example .env  # Add your TPU metadata
bash setup_tpu.sh

# Launch pre-training
bash recipes/midtrain_v4_512.sh
```

### 🎯 Supervised Fine-tuning
```bash
# Set up fine-tuning environment
cd post-train/LLaMA-Factory
pip install -r requirements.txt

# Configure dataset and run fine-tuning
bash ../../run_sft.sh
```

### 📊 Evaluation
```bash
cd evaluation/lm_eval
bash eval_mbpp_humaneval.sh
```
## 📚 Citation

```bibtex
@misc{coda2025,
  title={CoDA: Coding LM via Diffusion Adaptation},
  author={Chen, Haolin and Wang, Shiyu and Qin, Can and Pang, Bo and Liu, Zuxin and Qiu, Jielin and Zhang, Jianguo and Zhou, Yingbo and Chen, Zeyuan and Xu, Ran and Heinecke, Shelby and Savarese, Silvio and Xiong, Caiming and Wang, Huan and Yao, Weiran},
  year={2025},
  publisher={Salesforce AI Research}
}
```

## 🔗 Resources

- 📄 **Paper**: [huggingface.co/papers/2510.03270](https://huggingface.co/papers/2510.03270)
- 💻 **Code Repository**: [github.com/SalesforceAIResearch/CoDA](https://github.com/SalesforceAIResearch/CoDA)
- 🤗 **Model Hub**: [Salesforce CoDA collection](https://huggingface.co/collections/Salesforce/coda-68d627d87921c0e28a69e340)

## 🙏 Acknowledgements

We thank Lingpeng Kong for insightful discussions and Jialei Chen for technical support with TPU infrastructure.

---

*🏢 Developed by Salesforce AI Research*