---
base_model:
- unsloth/gpt-oss-120b-BF16
license: apache-2.0
pipeline_tag: text-generation
library_name: transformers
tags:
- vllm
- unsloth
- abliterated
- uncensored
---

# huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated


This is an uncensored version of [unsloth/gpt-oss-120b-BF16](https://huggingface.co/unsloth/gpt-oss-120b-BF16) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).  

## ollama
Ollama requires the latest version: [v0.11.8](https://github.com/ollama/ollama/releases/tag/v0.11.8)

You can use [huihui_ai/gpt-oss-abliterated:120b](https://ollama.com/huihui_ai/gpt-oss-abliterated:120b) directly, 
```
ollama run huihui_ai/gpt-oss-abliterated:120b
```


## Download and merge 

Use the [llama.cpp](https://github.com/ggml-org/llama.cpp) split program to merge model (llama-gguf-split needs to be compiled.),

If you use llama-cli to run GGUF, it is recommended to use the latest version of llama.cpp.

[Q4_K_M-GGUF](https://huggingface.co/huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/tree/main/Q4_K_M-GGUF)

[Q8_0-GGUF](https://huggingface.co/huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/tree/main/Q8_0-GGUF)

[f16-GGUF](https://huggingface.co/huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/tree/main/f16-GGUF)


```
huggingface-cli download huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated --local-dir ./huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated --token xxx

mkdir huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/Q4_K_M-GGUF

llama-gguf-split --merge huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/Q4_K_M-GGUF/Q4_K_M-GGUF-00001-of-00015.gguf huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated/Q4_K_M.gguf
```

## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
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
NEW_MODEL_ID = "huihui-ai/Huihui-gpt-oss-120b-BF16-abliterated"
print(f"Load Model {NEW_MODEL_ID} ... ")

model = AutoModelForCausalLM.from_pretrained(
    NEW_MODEL_ID, 
    device_map="auto", 
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
)
#print(model)
#print(model.config)

tokenizer = AutoTokenizer.from_pretrained(NEW_MODEL_ID, trust_remote_code=True)

messages = []
skip_prompt=False
skip_special_tokens=False
do_sample = True

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
        
def generate_stream(model, tokenizer, messages, skip_prompt, skip_special_tokens, do_sample, max_new_tokens):
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
    ).to(model.device)

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
              "temperature": 0.7,
              "top_k": 20,
              "top_p": 0.8,
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
            **input_ids,
            streamer=streamer,
            **generate_kwargs
        )
        del generated_ids
    except StopIteration:
        print("\n[Stopped by user]")

    del input_ids
    torch.cuda.empty_cache()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    return streamer.generated_text, streamer.stop_flag, streamer.get_metrics()

while True:
    print(f"skip_prompt: {skip_prompt}")
    print(f"skip_special_tokens: {skip_special_tokens}")
    print(f"do_sample: {do_sample}")
    
    user_input = input("User: ").strip()
    if user_input.lower() == "/exit":
        print("Exiting chat.")
        break
    if user_input.lower() == "/clear":
        messages = []
        print("Chat history cleared. Starting a new conversation.")
        continue
    if user_input.lower() == "/skip_prompt":
        skip_prompt = not skip_prompt
        continue
    if user_input.lower() == "/skip_special_tokens":
        skip_special_tokens = not skip_special_tokens
        continue
    if user_input.lower() == "/do_sample":
        do_sample = not do_sample
        continue
    if not user_input:
        print("Input cannot be empty. Please enter something.")
        continue
    

    messages.append({"role": "user", "content": user_input})
    response, stop_flag, metrics = generate_stream(model, tokenizer, messages, skip_prompt, skip_special_tokens, do_sample, 40960)
    print("\n\nMetrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")

    print("", flush=True)
    if stop_flag:
        continue
    messages.append({"role": "assistant", "content": response})
```

## Usage Warnings


 - **Risk of Sensitive or Controversial Outputs**: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

 - **Not Suitable for All Audiences**: Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

 - **Legal and Ethical Responsibilities**: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

 - **Research and Experimental Use**: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

 - **Monitoring and Review Recommendations**: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

 - **No Default Safety Guarantees**: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.


### Donation
##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin:
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
- Support our work on Ko-fi (https://ko-fi.com/huihuiai)!
