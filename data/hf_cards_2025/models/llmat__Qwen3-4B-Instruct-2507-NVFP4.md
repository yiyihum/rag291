---
language: en
license: apache-2.0
pipeline_tag: text-generation
tags:
- quantization
- nvfp4
- qwen
base_model: Qwen/Qwen3-4B-Instruct-2507
model_name: Qwen3-4B-Instruct-2507-NVFP4
---

# Qwen3-4B-Instruct-2507-NVFP4

NVFP4-quantized version of `Qwen/Qwen3-4B-Instruct-2507` produced with [llmcompressor](https://github.com/neuralmagic/llm-compressor).

## Notes
- Quantization scheme: NVFP4 (linear layers, `lm_head` excluded)
- Calibration samples: 512
- Max sequence length during calibration: 2048

## Deployment

### Use with vLLM

This model can be deployed efficiently using the [vLLM](https://docs.vllm.ai/en/latest/) backend, as shown in the example below.

```python
from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_id = "llmat/Qwen3-4B-Instruct-2507-NVFP4"
number_gpus = 1

sampling_params = SamplingParams(temperature=0.6, top_p=0.9, max_tokens=256)

tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

prompts = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

llm = LLM(model=model_id, tensor_parallel_size=number_gpus)

outputs = llm.generate(prompts, sampling_params)

generated_text = outputs[0].outputs[0].text
print(generated_text)
```

vLLM also supports OpenAI-compatible serving. See the [documentation](https://docs.vllm.ai/en/latest/) for more details.