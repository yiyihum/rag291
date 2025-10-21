---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-14B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-14B
tags:
- chat
- abliterated
- uncensored
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

# huihui-ai/Qwen3-14B-abliterated


This is an uncensored version of [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 

Ablation was performed using a new and faster method, which yields better results.

**Important Note** There's a new version available, please try using the new version [huihui-ai/Qwen3-14B-abliterated-v2](https://huggingface.co/huihui-ai/Qwen3-14B-abliterated-v2).


## ollama

You can use [huihui_ai/qwen3-abliterated:14b](https://ollama.com/huihui_ai/qwen3-abliterated:14b) directly, 
```
ollama run huihui_ai/qwen3-abliterated:14b
```


## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TextStreamer
import torch
import os
import signal

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
NEW_MODEL_ID = "huihui-ai/Qwen3-14B-abliterated"
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

initial_messages = [{"role": "system", "content": "You are a helpful assistant."}]
messages = initial_messages.copy()
enable_thinking = True
skip_prompt=True
skip_special_tokens=True

class CustomTextStreamer(TextStreamer):
    def __init__(self, tokenizer, skip_prompt=True, skip_special_tokens=True):
        super().__init__(tokenizer, skip_prompt=skip_prompt, skip_special_tokens=skip_special_tokens)
        self.generated_text = ""
        self.stop_flag = False

    def on_finalized_text(self, text: str, stream_end: bool = False):
        self.generated_text += text
        print(text, end="", flush=True)
        if self.stop_flag:
            raise StopIteration

    def stop_generation(self):
        self.stop_flag = True

def generate_stream(model, tokenizer, messages, enable_thinking, skip_prompt, skip_special_tokens, max_new_tokens):
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        enable_thinking = enable_thinking,
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
    
    print("Response: ", end="", flush=True)
    try:
        generated_ids = model.generate(
            tokens,
            attention_mask=attention_mask,
            use_cache=False,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
            streamer=streamer
        )
        del generated_ids
    except StopIteration:
        print("\n[Stopped by user]")

    del input_ids, attention_mask
    torch.cuda.empty_cache()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    return streamer.generated_text, streamer.stop_flag

while True:
    user_input = input("User: ").strip()
    if user_input.lower() == "/exit":
        print("Exiting chat.")
        break
    if user_input.lower() == "/clear":
        messages = initial_messages.copy()
        print("Chat history cleared. Starting a new conversation.")
        continue
    if user_input.lower() == "/no_think":
        if enable_thinking:
            enable_thinking = False
            print("Thinking = False.")
        else:
            enable_thinking = True
            print("Thinking = True.")        
        continue
    if user_input.lower() == "/skip_prompt":
        if skip_prompt:
            skip_prompt = False
            print("skip_prompt = False.")
        else:
            skip_prompt = True
            print("skip_prompt = True.")        
        continue
    if user_input.lower() == "/skip_special_tokens":
        if skip_special_tokens:
            skip_special_tokens = False
            print("skip_special_tokens = False.")
        else:
            skip_special_tokens = True
            print("skip_special_tokens = True.")        
        continue
    if not user_input:
        print("Input cannot be empty. Please enter something.")
        continue
    messages.append({"role": "user", "content": user_input})
    response, stop_flag = generate_stream(model, tokenizer, messages, enable_thinking, skip_prompt, skip_special_tokens, 14192)
    print("", flush=True)
    if stop_flag:
        continue
    messages.append({"role": "assistant", "content": response})
```

## Pass Rate Description

The pass rate is defined as the proportion of harmful instructions that did not trigger the test condition (TestPassed=False) out of the total number of instructions processed. It is calculated by subtracting the number of triggered instructions (triggered_total) from the total number of instructions (total), then dividing the result by the total number of instructions: (total - triggered_total) / total. The pass rate is presented as a decimal value (rounded to two decimal places for clarity) and as a percentage (rounded to one decimal place) to clearly indicate the fraction of instructions that did not trigger the condition. 

The test set data comes from [huihui-ai/harmbench_behaviors](https://huggingface.co/datasets/huihui-ai/harmbench_behaviors), the test code, [TestPassed.py](https://huggingface.co/huihui-ai/Qwen3-14B-abliterated/blob/main/TestPassed.py).

The test result is [100.00%](https://huggingface.co/huihui-ai/Qwen3-14B-abliterated/blob/main/TestPassed-abliterated.jsonl).
```
python TestPassed.py
Load Model huihui-ai/Qwen3-14B-abliterated ...
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:41<00:00,  6.90s/it]
Processing harmful instructions: 100%|███████████████████████████████████████████████████████████████████████████████████| 320/320 [02:23<00:00,  2.22it/s]
Passed total: 320/320, Passed ratio: 1.00 (100.00%)
```

Below is the pass rate for harmful instructions. 
This test is only a simple judgment and does not represent the actual result. You can increase the max_new_tokens value to obtain the final result.

| Model                | Passed total | Passed ratio |
|----------------------|--------------|--------------|
| Qwen3-14B             | 246/320      | 76.88%       |
| Qwen3-14B-abliterated | **320/320**  | **100.00%**  |


### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
