---
license: mit
library_name: transformers
base_model:
- deepseek-ai/DeepSeek-R1-0528-Qwen3-8B
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

# huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated
This is an uncensored version of [deepseek-ai/DeepSeek-R1-0528-Qwen3-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 

## ollama

You can use [huihui_ai/deepseek-r1-abliterated:8b](https://ollama.com/huihui_ai/deepseek-r1-abliterated:8b) directly, 
Switch the thinking toggle using `/set think` and `/set nothink`

```
ollama run huihui_ai/deepseek-r1-abliterated
```

## Usage
You can use this model in your applications by loading it with Hugging Face's `transformers` library:
You can try using **/no_think** to toggle think mode, but it’s not guaranteed to work every time.


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
NEW_MODEL_ID = "huihui-ai/DeepSeek-R1-0528-Qwen3-8B-abliterated"
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
    quantization_config=quant_config_4,
    torch_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(NEW_MODEL_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
tokenizer.pad_token_id = tokenizer.eos_token_id

messages = []
enable_thinking = True
skip_prompt=True
skip_special_tokens=True

def apply_chat_template(tokenizer, messages, enable_thinking, add_generation_prompt=True):
    input_ids = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
    )
    if not enable_thinking:
        input_ids += "\n<think>\n\n</think>\n"
    return input_ids

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
    formatted_prompt = apply_chat_template(tokenizer, messages, enable_thinking)
    input_ids = tokenizer(
        formatted_prompt,
        return_tensors="pt",
        return_attention_mask=True,
        padding=False
    )
    
    tokens = input_ids['input_ids'].to(model.device)
    attention_mask = input_ids['attention_mask'].to(model.device)

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
            #use_cache=False,
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
        messages = []
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
    response, stop_flag = generate_stream(model, tokenizer, messages, enable_thinking, skip_prompt, skip_special_tokens, 8192)
    print("", flush=True)
    if stop_flag:
        continue
    messages.append({"role": "assistant", "content": response})
```


### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
