---
license: apache-2.0
base_model:
- huihui-ai/Qwen3-4B-abliterated
- mlabonne/Qwen3-4B-abliterated
- Goekdeniz-Guelmez/Josiefied-Qwen3-4B-abliterated-v1
- fedric95/Qwen3-4B-unc
library_name: transformers
license_link: https://huggingface.co/Qwen/Qwen3-4B/blob/main/LICENSE
pipeline_tag: text-generation
tags:
- moe
extra_gated_prompt: '**Usage Warnings**


  “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering
  has been significantly reduced, potentially generating sensitive, controversial,
  or inappropriate content. Users should exercise caution and rigorously review generated
  outputs.

  “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s
  outputs may be inappropriate for public settings, underage users, or applications
  requiring high security.

  “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies
  with local laws and ethical standards. Generated content may carry legal or ethical
  risks, and users are solely responsible for any consequences.

  “**Research and Experimental Use**“: It is recommended to use this model for research,
  testing, or controlled environments, avoiding direct use in production or public-facing
  commercial applications.

  “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor
  model outputs in real-time and conduct manual reviews when necessary to prevent
  the dissemination of inappropriate content.

  “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone
  rigorous safety optimization. huihui.ai bears no responsibility for any consequences
  arising from its use.'
---
# huihui-ai/Huihui-MoE-12B-A4B-abliterated

## Model Overview
Huihui-MoE-12B-A4B-abliterated is a **Mixture of Experts (MoE)** language model developed by **huihui.ai**, built upon the **[huihui-ai/Qwen3-4B-abliterated](https://huggingface.co/huihui-ai/Qwen3-4B-abliterated)** base model. It enhances the standard Transformer architecture by replacing MLP layers with MoE layers, each containing 4 experts, to achieve high performance with efficient inference. The model is designed for natural language processing tasks, including text generation, question answering, and conversational applications.

This model combines four ablated models, and perhaps it can achieve the performance of all the ablated models?

This is just a test. The exploration of merging different manifestations of models of the same type is another possibility.

 - **Architecture**: Qwen3MoeForCausalLM model with 4 experts per layer (num_experts=4), activating 1 expert per token (num_experts_per_tok=1).
 - **Total Parameters**: ~12 billion (12B)
 - **Activated Parameters**: ~4 billion (4B) during inference, comparable to Qwen3-4B-abliterated
 - **Developer**: huihui.ai
 - **Release Date**: June 2025
 - **License**: Inherits the license of the Qwen3 base model (apache-2.0)

## Expert Models:
  
### Expert 1:
[mlabonne/Qwen3-4B-abliterated](https://huggingface.co/mlabonne/Qwen3-4B-abliterated)

### Expert 2:
[Goekdeniz-Guelmez/Josiefied-Qwen3-4B-abliterated-v1](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen3-4B-abliterated-v1)

### Expert 3:
[huihui-ai/Qwen3-4B-abliterated](https://huggingface.co/huihui-ai/Qwen3-4B-abliterated)

### Expert 4:
[fedric95/Qwen3-4B-unc](https://huggingface.co/fedric95/Qwen3-4B-unc)

### Instruction Following:
[huihui-ai/Qwen3-4B-abliterated](https://huggingface.co/huihui-ai/Qwen3-4B-abliterated)

## Training

 - **Base Model**: Qwen3-4B-abliterated
 - **Conversion**: The model copies embeddings, self-attention, and normalization weights from Qwen3-4B-abliterated, replacing MLP layers with MoE layers (4 experts). Gating weights are randomly initialized.
 - **Fine-Tuning**: Not fine-tuned; users are recommended to fine-tune for specific tasks to optimize expert routing.

## ollama

You can use [huihui_ai/huihui-moe-abliterated:12b](https://ollama.com/huihui_ai/huihui-moe-abliterated:12b) directly, 
Switch the thinking toggle using /set think and /set nothink
```
ollama run huihui_ai/huihui-moe-abliterated:12b
```

## Usage

```
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TextStreamer
import torch
import os
import signal
import random
import numpy as np
import time
from collections import Counter

cpu_count = os.cpu_count()
print(f"Number of CPU cores in the system: {cpu_count}")
half_cpu_count = cpu_count // 2
os.environ["MKL_NUM_THREADS"] = str(half_cpu_count)
os.environ["OMP_NUM_THREADS"] = str(half_cpu_count)
torch.set_num_threads(half_cpu_count)

print(f"PyTorch threads: {torch.get_num_threads()}")
print(f"MKL threads: {os.getenv('MKL_NUM_THREADS')}")
print(f"OMP threads: {os.getenv('OMP_NUM_THREADS')}")

# Load the model and tokenizer
NEW_MODEL_ID = "huihui-ai/Huihui-MoE-12B-A4B-abliterated"
print(f"Load Model {NEW_MODEL_ID} ... ")
quant_config_4 = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
    llm_int8_enable_fp32_cpu_offload=True,
)

model = AutoModelForCausalLM.from_pretrained(
    NEW_MODEL_ID,
    device_map="auto",
    trust_remote_code=True,
    #quantization_config=quant_config_4,
    torch_dtype=torch.bfloat16
)
tokenizer = AutoTokenizer.from_pretrained(NEW_MODEL_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.pad_token_id = tokenizer.eos_token_id

tokenizer = AutoTokenizer.from_pretrained(NEW_MODEL_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.pad_token_id = tokenizer.eos_token_id

messages = []
nothink = False
same_seed = False
skip_prompt=True
skip_special_tokens=True
do_sample = True

def set_random_seed(seed=None):
    """Set random seed for reproducibility. If seed is None, use int(time.time())."""
    if seed is None:
        seed = int(time.time())  # Convert float to int
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # If using CUDA
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    return seed  # Return seed for logging if needed

class CustomTextStreamer(TextStreamer):
    def __init__(self, tokenizer, skip_prompt=True, skip_special_tokens=True):
        super().__init__(tokenizer, skip_prompt=skip_prompt, skip_special_tokens=skip_special_tokens)
        self.generated_text = ""
        self.stop_flag = False
        self.init_time = time.time()  # Record initialization time
        self.end_time = None  # To store end time
        self.first_token_time = None  # To store first token generation time
        self.token_count = 0  # To track total tokens

    def on_finalized_text(self, text: str, stream_end: bool = False):
        if self.first_token_time is None and text.strip():  # Set first token time on first non-empty text
            self.first_token_time = time.time()
        self.generated_text += text
        # Count tokens in the generated text
        tokens = self.tokenizer.encode(text, add_special_tokens=False)
        self.token_count += len(tokens)
        print(text, end="", flush=True)
        if stream_end:
            self.end_time = time.time()  # Record end time when streaming ends
        if self.stop_flag:
            raise StopIteration

    def stop_generation(self):
        self.stop_flag = True
        self.end_time = time.time()  # Record end time when generation is stopped

    def get_metrics(self):
        """Returns initialization time, first token time, first token latency, end time, total time, total tokens, and tokens per second."""
        if self.end_time is None:
            self.end_time = time.time()  # Set end time if not already set
        total_time = self.end_time - self.init_time  # Total time from init to end
        tokens_per_second = self.token_count / total_time if total_time > 0 else 0
        first_token_latency = (self.first_token_time - self.init_time) if self.first_token_time is not None else None
        metrics = {
            "init_time": self.init_time,
            "first_token_time": self.first_token_time,
            "first_token_latency": first_token_latency,
            "end_time": self.end_time,
            "total_time": total_time,  # Total time in seconds
            "total_tokens": self.token_count,
            "tokens_per_second": tokens_per_second
        }
        return metrics
        
def generate_stream(model, tokenizer, messages, nothink, skip_prompt, skip_special_tokens, do_sample, max_new_tokens):
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        enable_thinking = not nothink,
        add_generation_prompt=True,
        return_tensors="pt"
    )
    attention_mask = torch.ones_like(input_ids, dtype=torch.long)
    tokens = input_ids.to(model.device) 
    attention_mask = attention_mask.to(model.device)

    streamer = CustomTextStreamer(tokenizer, skip_prompt=skip_prompt, skip_special_tokens=skip_special_tokens)

    def signal_handler(sig, frame):
        streamer.stop_generation()
        print("\n[Generation stopped by user with Ctrl+C]")

    signal.signal(signal.SIGINT, signal_handler)

    generate_kwargs = {}
    if do_sample:
        generate_kwargs = {
              "do_sample": do_sample,
              "max_length": max_new_tokens,
              "temperature": 0.6,
              "top_k": 20,
              "top_p": 0.95,
              "repetition_penalty": 1.2,
              "no_repeat_ngram_size": 2
        }
    else:
        generate_kwargs = {
              "do_sample": do_sample,
              "max_length": max_new_tokens,
              "repetition_penalty": 1.2,
              "no_repeat_ngram_size": 2
        }
  
          
    print("Response: ", end="", flush=True)
    try:
        generated_ids = model.generate(
            tokens,
            attention_mask=attention_mask,
            #use_cache=False,
            pad_token_id=tokenizer.pad_token_id,
            streamer=streamer,
            **generate_kwargs
        )
        del generated_ids
    except StopIteration:
        print("\n[Stopped by user]")

    del input_ids, attention_mask
    torch.cuda.empty_cache()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    return streamer.generated_text, streamer.stop_flag, streamer.get_metrics()

init_seed = set_random_seed()

# List to store activated expert indices
activated_experts = []

# Define hook function to capture gate_probs output
def hook_fn(module, input, output):
    # output is gate_probs, shape: [batch_size, sequence_length, num_experts]
    gate_probs = output
    # Compute top-1 expert indices (since only one expert is activated)
    _, topk_indices = gate_probs.topk(1, dim=-1)  # Take top-1
    # Flatten and store activated expert indices
    activated_experts.extend(topk_indices.squeeze(-1).view(-1).cpu().tolist())

hooks = []
for layer in model.model.layers:
    hooks.append(layer.mlp.gate.register_forward_hook(hook_fn))
  
while True:
    if same_seed:
        set_random_seed(init_seed)
    else:
        init_seed = set_random_seed()
        
    print(f"\nnothink: {nothink}")
    print(f"skip_prompt: {skip_prompt}")
    print(f"skip_special_tokens: {skip_special_tokens}")
    print(f"do_sample: {do_sample}")
    print(f"same_seed: {same_seed}, {init_seed}\n")
    
    user_input = input("User: ").strip()
    if user_input.lower() == "/exit":
        print("Exiting chat.")
        break
    if user_input.lower() == "/clear":
        messages = []
        print("Chat history cleared. Starting a new conversation.")
        continue
    if user_input.lower() == "/nothink":
        nothink = not nothink
        continue
    if user_input.lower() == "/skip_prompt":
        skip_prompt = not skip_prompt
        continue
    if user_input.lower() == "/skip_special_tokens":
        skip_special_tokens = not skip_special_tokens
        continue
    if user_input.lower().startswith("/same_seed"):
        parts = user_input.split()
        if len(parts) == 1:  # /same_seed (no number)
            same_seed = not same_seed  # Toggle switch
        elif len(parts) == 2:  # /same_seed <number>
            try:
                init_seed = int(parts[1])  # Extract and convert number to int
                same_seed = True
            except ValueError:
                print("Error: Please provide a valid integer after /same_seed")       
        continue
    if user_input.lower() == "/do_sample":
        do_sample = not do_sample
        continue
    if not user_input:
        print("Input cannot be empty. Please enter something.")
        continue
    

    messages.append({"role": "user", "content": user_input})
    activated_experts = []
    response, stop_flag, metrics = generate_stream(model, tokenizer, messages, nothink, skip_prompt, skip_special_tokens, do_sample, 40960)
    print("\n\nMetrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

    # Count the frequency of each activated expert
    expert_counts = Counter(activated_experts)

    # Print activation statistics
    print("\nActivated Expert Statistics:")
    for expert_idx, count in sorted(expert_counts.items()):
        print(f"Expert {expert_idx}: {count} times")
        
    print("", flush=True)
    if stop_flag:
        continue
    messages.append({"role": "assistant", "content": response})

# Remove all hooks after inference
for h in hooks: h.remove()

```

## Applications

 - **Text Generation: Articles**, dialogues, and creative writing.
 - **Question Answering**: Information retrieval and query resolution.
 - **Conversational AI**: Multi-turn dialogues for chatbots.
 - **Research**: Exploration of MoE architectures and efficient model scaling.

## Limitations

 - **Fine-Tuning Required**: Randomly initialized gating weights may lead to suboptimal expert utilization without fine-tuning.
 - **Compatibility**: Developed with transformers 4.52.4; ensure matching versions to avoid loading issues.
 - **Inference Speed**: While efficient for an MoE model, performance depends on hardware (GPU recommended).

## Ethical Considerations

 - **Bias**: Inherits potential biases from the Qwen3-4B-abliterated base model; users should evaluate outputs for fairness.
 - **Usage**: Intended for research and responsible applications; avoid generating harmful or misleading content.

## Contact

 - **Developer**: huihui.ai
 - **Repository**: huihui-ai/Huihui-MoE-12B-A4B-abliterated (available locally or on Hugging Face)
 - **Issues**: Report bugs or request features via the repository or please send an email to support@huihui.ai

