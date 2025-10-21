---
base_model: qwen/qwen3-30b-a3b-instruct-2507
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_moe
license: apache-2.0
language:
- en
library_name: transformers
---

### Model Card for Daemontatox/Zirel-2

---

**Model Name:** Daemontatox/Zirel-2

**Author:** Daemontatox (Ammar)

**Base Model:** [Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)

#### Model Details

`Zirel-2` is the latest iteration in the Zirel series of models, developed by Daemontatox. It is a fine-tuned version of the powerful `Qwen3-30B-A3B-Instruct-2507` model, which is a Mixture-of-Experts (MoE) architecture from Alibaba's Qwen team .

The primary goals of this fine-tuning are:
1.  **Maximize Knowledge & Capability:** To enhance the model's general knowledge and reasoning abilities, making it a highly capable personal assistant.
2.  **Optimize for Efficiency:** To leverage the inherent efficiency of the MoE architecture, ensuring high performance while keeping GPU memory usage and computational costs to a minimum.

The base model, `Qwen3-30B-A3B-Instruct-2507`, has a total of 30.5 billion parameters but only activates approximately 3.3 billion parameters during each inference step [[12], [14]]. This design allows it to deliver performance comparable to much larger, dense models while being significantly more resource-efficient .

#### Intended Use

`Zirel-2` is designed to be a smart, versatile, and efficient personal assistant. It excels at tasks such as:
*   Answering complex questions with detailed reasoning.
*   Generating high-quality text, code, and creative content.
*   Performing logical and mathematical reasoning.
*   Following intricate, multi-step instructions.

Its efficiency makes it particularly suitable for deployment on consumer-grade hardware or in environments where computational resources are constrained.

#### Architecture

*   **Type:** Mixture-of-Experts (MoE) Language Model.
*   **Total Parameters:** ~30.5B.
*   **Active Parameters per Inference:** ~3.3B .
*   **Experts:** The base model utilizes 128 experts, with 8 being activated for any given token .
*   **Context Length:** Supports a very long context window of up to 262,144 tokens .

---

### Example Inference Code

You can run inference with `Zirel-2` using the Hugging Face `transformers` library. For optimal performance with MoE models, it's recommended to use a library like `vLLM` or `TensorRT-LLM`, but a basic example with `transformers` is provided below.

**Prerequisites:**
```bash
pip install transformers accelerate torch
```

**Basic Inference with `transformers`:**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Load the model and tokenizer
model_name = "Daemontatox/Zirel-2"

# It's highly recommended to use 4-bit or 8-bit quantization to fit the model in memory
# Here we use 4-bit quantization with bitsandbytes
from transformers import BitsAndBytesConfig

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
    torch_dtype=torch.float16,
)

# Create a text generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_p=0.9,
)

# Define your prompt. Qwen models typically use this chat template.
messages = [
    {"role": "system", "content": "You are a helpful and knowledgeable AI assistant named Zirel-2."},
    {"role": "user", "content": "Explain the concept of Mixture of Experts (MoE) in simple terms and why it's efficient."}
]

# Apply the chat template
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Generate a response
outputs = pipe(prompt)
response = outputs[0]["generated_text"][len(prompt):]
print(response)
```

**For Better Performance (Recommended):**

For serious use, consider using `vLLM`, which has excellent support for MoE models and provides much higher throughput and lower latency.

```python
# Example using vLLM (you need to install vLLM first: pip install vllm)
from vllm import LLM, SamplingParams

# Initialize the LLM engine
llm = LLM(model="Daemontatox/Zirel-2", tensor_parallel_size=1) # Adjust tensor_parallel_size for your GPU setup

# Create a sampling params object
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=512
)

# Prepare your prompt using the chat template
tokenizer = AutoTokenizer.from_pretrained("Daemontatox/Zirel-2")
messages = [
    {"role": "system", "content": "You are a helpful and knowledgeable AI assistant named Zirel-2."},
    {"role": "user", "content": "Explain the concept of Mixture of Experts (MoE) in simple terms and why it's efficient."}
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Generate text
outputs = llm.generate([prompt], sampling_params)
print(outputs[0].outputs[0].text)
```