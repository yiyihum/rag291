---
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
library_name: peft
tags:
- conversion-rate-optimization
- cro
- lora
- sft
- llama3.1
- a-b-testing
- marketing-ai
license: llama3.1
pipeline_tag: text-generation
language:
- en
---

# 🧠 Keak CRO LoRA — Llama 3.1 8B Instruct

A **LoRA-fine-tuned** variant of Meta’s **Llama 3.1 8B Instruct**, optimized for **Conversion Rate Optimization (CRO)** and **A/B testing automation**.  
Developed by **Keak AI**, this model generates high-converting website copy, structured business insights, and persuasive content that aligns with CRO best practices.

---

## 🪶 Overview

**Base Model:** `meta-llama/Meta-Llama-3.1-8B-Instruct`  
**Adapter Type:** LoRA (Low-Rank Adaptation) via [PEFT](https://github.com/huggingface/peft)  
**Trained By:** [Keak AI](https://huggingface.co/Keak-AI)  
**Specialization:** Conversion rate optimization, persuasive copywriting, and structured web analysis

This model enhances Llama 3.1’s reasoning and language generation with CRO-specific knowledge, enabling it to:
- Extract business and visual identity context from webpages  
- Generate optimized A/B testing variants of copy and CTAs  
- Apply CRO principles such as clarity, curiosity, urgency, and benefit framing  

---

## 🧭 Intended Use

The model is designed for:
1. **Webpage Analysis & Context Extraction** – Identify core offering, audience, pain points, and design tone  
2. **Variant Generation** – Produce high-performing alternatives for headlines, CTAs, and product descriptions  

It performs best when used in **two steps**:  
**(1)** Analyze context → **(2)** Generate optimized variant.

---

## 📊 Training Data

Fine-tuned on **Keak AI’s proprietary A/B testing dataset**, containing real conversion experiments and human-evaluated high-performing variants.  
This dataset reflects diverse industries (e-commerce, SaaS, marketing) and is continuously updated for improvement.

---

## 💬 Recommended System Message

```

You are an expert conversion rate optimization specialist with deep expertise in persuasive copywriting, consumer psychology, and A/B testing. Your singular goal is to generate variations that maximize conversion rates.

```

---

## 🧩 Structured Page Context Format

The model expects input in this structured schema:

```

Business: [Organization name and type]
Core Offering: [Primary service/product in 1–2 sentences]
Value Proposition: [Main benefit/outcome for customers]

Target Audience: [Who this is for]
Primary Pain Point: [Problem being solved]

Key Differentiators:

* [Unique selling point 1]
* [Unique selling point 2]
* [Unique selling point 3]

Conversion Goal: [Primary CTA/desired action]

Trust Signals: [Credentials, certifications, guarantees]

Location/Context: [Geographic area served, if relevant]

Visual Identity:

* Primary colors: [List main colors with hex codes if identifiable]
* Accent colors: [List accent colors with hex codes if identifiable]
* Overall tone: [Professional, Playful, Serious, Warm, etc.]
* Style: [Minimalist, Bold, Corporate, Creative, etc.]

```

---

## 🧠 Example 1 – Webpage Analysis

**Prompt:**
```

Analyze the following webpage and extract both business context and visual identity.
URL: [https://example.com](https://example.com)

Dominant colors: #000000, #3e3b41, #0d0e11, #294a85, #181c28
WEBPAGE CONTENT:
TITLE: Example Company
META: Description of the business...
H1: Main headline
H2: Subheadings...
P: Paragraph content...

Output strictly in the structured Page Context format.

```

---

## 🧠 Example 2 – Generate a High-Converting Variant

**Prompt:**
```

Generate a high-converting variation for A/B testing.

# Page Context

Business: Keak, a SaaS company specializing in AI-powered website optimization
Core Offering: AI-driven A/B testing and CRO automation platform
...

# Current Element

Type: headline
Selector: #hero-headline
Current text: "Boost your website's conversion rates with AI-powered testing"

# Optimization Requirements

Length: ±20% of original
Tone: Keep brand voice
CRO Principles: Clarity, Curiosity, Urgency, Benefits

# Output Format

Variation: [new variant]
Justification: [2–3 sentences on why it improves conversions]

````

---

## 🧰 Usage (Transformers + PEFT)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
import torch

# Model identifiers
base = "meta-llama/Meta-Llama-3.1-8B-Instruct"  # Base Llama 3.1 8B model
adapter = "Keak-AI/keak-CRO-llama-3.1-8B-instruct"  # Fine-tuned adapter for conversion rate optimization

# Configure 4-bit quantization (same as training)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,  # Enable 4-bit quantization for memory efficiency
    bnb_4bit_quant_type="nf4",  # Use NormalFloat4 quantization type
    bnb_4bit_compute_dtype=torch.bfloat16,  # Computation dtype for better precision
    bnb_4bit_use_double_quant=True,  # Enable nested quantization for additional memory savings
)

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(base)
tokenizer.pad_token = tokenizer.eos_token  # Set padding token to end-of-sequence token
tokenizer.padding_side = "right"  # Pad sequences on the right side

# Load base model with quantization
model = AutoModelForCausalLM.from_pretrained(
    base,
    quantization_config=bnb_config,  # Apply 4-bit quantization
    device_map="auto",  # Automatically distribute model across available devices
    dtype=torch.bfloat16  # Use bfloat16 for model weights
)

# Load and merge the PEFT adapter on top of base model
model = PeftModel.from_pretrained(model, adapter)

# Generate function
def generate_variant(messages, max_new_tokens=256):
    # Format messages using the model's chat template
    formatted_input = tokenizer.apply_chat_template(
        messages,
        tokenize=False,  # Return string instead of tokens
        add_generation_prompt=True  # Add prompt for model to start generation
    )
    
    # Tokenize the formatted input and move to model's device
    inputs = tokenizer(formatted_input, return_tensors="pt").to(model.device)
    
    # Generate response without computing gradients
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,  # Maximum tokens to generate
            temperature=0.7,  # Sampling temperature (higher = more random)
            do_sample=True,  # Enable sampling instead of greedy decoding
            top_p=0.9,  # Nucleus sampling threshold
            pad_token_id=tokenizer.pad_token_id,  # Padding token ID
            eos_token_id=tokenizer.eos_token_id,  # End-of-sequence token ID
        )
    
    # Decode only the newly generated tokens (skip the input)
    response = tokenizer.decode(
        outputs[0][inputs.input_ids.shape[1]:],  # Slice to get only generated tokens
        skip_special_tokens=True  # Remove special tokens from output
    )
    return response.strip()  # Remove leading/trailing whitespace

# Example usage
messages = [
    {"role": "system", "content": "You are an expert conversion rate optimization specialist..."},
    {"role": "user", "content": "Generate a headline variation for..."}
]

result = generate_variant(messages)
print(result)
````

---

## ⚙️ Training Details

### Base Model

* **Model:** `meta-llama/Meta-Llama-3.1-8B-Instruct`
* **Quantization:** 4-bit (NF4) with bitsandbytes
* **Compute dtype:** bfloat16
* **Double quantization:** Enabled

### LoRA Configuration

```python
LoraConfig(
    r=4,
    lora_alpha=8,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
)
```

### Hyperparameters

| Setting                | Value                                |
| ---------------------- | ------------------------------------ |
| Epochs                 | 3                                    |
| Learning Rate          | 2e-5                                 |
| Batch Size             | 1 (per GPU, eff. 8 with grad accum.) |
| Optimizer              | paged_adamw_8bit                     |
| Scheduler              | cosine, 10 % warmup                  |
| Weight Decay           | 0.01                                 |
| Max Grad Norm          | 0.3                                  |
| Seq Length             | 2048                                 |
| Gradient Checkpointing | ✅ Enabled                            |

---

## 💡 Performance Tips

* Always include the **recommended system message**
* Use the **two-step workflow** (analyze → generate)
* Provide clear **optimization constraints** (tone, length, principles)
* Specify **selectors** when optimizing page elements

---

## ⚠️ Limitations

* Proprietary dataset — limited open benchmarking
* Optimal for English; multilingual support still experimental
* May underperform on niches unseen in training data
* Follows the Llama 3.1 Community License restrictions

---

## 📜 License

Released under the **Llama 3.1 Community License Agreement**.
Use is permitted for **commercial** and **research** applications within the license terms.
See [Meta Llama 3.1 License](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) for details.

---

## 📚 Citation

```bibtex
@misc{keak2025cro,
  title={Keak CRO LoRA — Llama 3.1 8B Instruct Fine-Tuned Adapter},
  author={Keak AI},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/Keak-AI/keak-CRO-llama-3.1-8B-instruct}}
}
```

---

## 📬 Contact

For questions or collaboration inquiries, contact **Keak AI** via [https://huggingface.co/Keak-AI](https://huggingface.co/Keak-AI) or open an issue in the model repository.