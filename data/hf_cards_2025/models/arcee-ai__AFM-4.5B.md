---
license: apache-2.0
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
library_name: transformers
extra_gated_prompt: Company name is optional, please put NA if you would prefer not
  to share it.
base_model:
- arcee-ai/AFM-4.5B-Base
---

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/Lj9YVLIKKdImV_jID0A1g.png" width="25%" alt="Arcee AFM 4.5B">
  </picture>
</div>


# AFM-4.5B

AFM-4.5B is a 4.5 billion parameter instruction-tuned model developed by Arcee.ai, designed for enterprise-grade performance across diverse deployment environments from cloud to edge. The base model was trained on a dataset of 8 trillion tokens, comprising 6.5 trillion tokens of general pretraining data followed by 1.5 trillion tokens of midtraining data with enhanced focus on mathematical reasoning and code generation. Following pretraining, the model underwent supervised fine-tuning on high-quality instruction datasets. The instruction-tuned model was further refined through reinforcement learning on verifiable rewards as well as for human preference. We use a modified version of [TorchTitan](https://arxiv.org/abs/2410.06511) for pretraining, [Axolotl](https://axolotl.ai) for supervised fine-tuning, and a modified version of [Verifiers](https://github.com/willccbb/verifiers) for reinforcement learning.

The development of AFM-4.5B prioritized data quality as a fundamental requirement for achieving robust model performance. We collaborated with DatologyAI, a company specializing in large-scale data curation. DatologyAI's curation pipeline integrates a suite of proprietary algorithms—model-based quality filtering, embedding-based curation, target distribution-matching, source mixing, and synthetic data. Their expertise enabled the creation of a curated dataset tailored to support strong real-world performance.

The model architecture follows a standard transformer decoder-only design based on Vaswani et al., incorporating several key modifications for enhanced performance and efficiency. Notable architectural features include grouped query attention for improved inference efficiency and ReLU^2 activation functions instead of SwiGLU to enable sparsification while maintaining or exceeding performance benchmarks.

The model available in this repo is the instruct model following supervised fine-tuning and reinforcement learning.

View our documentation here for more details: https://docs.arcee.ai/arcee-foundation-models/introduction-to-arcee-foundation-models

***

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

## Model Details

* **Model Architecture:** ArceeForCausalLM
* **Parameters:** 4.5B
* **Training Tokens:** 8T
* **License:** [Apache 2.0](https://huggingface.co/arcee-ai/AFM-4.5B#license)
* **Recommended settings:**
    * temperature: 0.5
    * top_k: 50
    * top_p: 0.95
    * repeat_penalty: 1.1

***

## Benchmarks

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/BdsWFc4pxiHlK2E0j9AfG.png)
*Qwen3 and SmolLM's reasoning approach causes their scores to vary wildly from suite to suite - but these are all scores on our internal harness with the same hyperparameters. Be sure to reference their reported scores. SmolLM just released its [bench](https://github.com/huggingface/smollm).

## How to use with `transformers`

You can use the model directly with the `transformers` library.

We recommend a lower temperature, around 0.5, for optimal performance.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "arcee-ai/AFM-4.5B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Who are you?"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.5,
    top_k=50,
    top_p=0.95
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## How to use with `vllm`

Ensure you are on version `0.10.1` or newer

```
pip install vllm>=0.10.1
```

You can then serve the model natively

```
vllm serve arcee-ai/AFM-4.5B
```

## How to use with Together API

You can access this model directly via the [Together Playground](https://api.together.xyz/playground/arcee-ai/AFM-4.5B). 

### Python (Official Together SDK)

```python
from together import Together

client = Together()
response = client.chat.completions.create(
    model="arcee-ai/AFM-4.5B",
    messages=[
        {
            "role": "user",
            "content": "What are some fun things to do in New York?"
        }
    ]
)
print(response.choices[0].message.content)
```

### cURL

```bash
curl -X POST "https://api.together.xyz/v1/chat/completions" \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "arcee-ai/AFM-4.5B",
    "messages": [
      {
        "role": "user",
        "content": "What are some fun things to do in New York?"
      }
    ]
  }'
```


## Quantization support

Support for llama.cpp and Intel OpenVINO is available:

https://huggingface.co/arcee-ai/AFM-4.5B-GGUF

https://huggingface.co/arcee-ai/AFM-4.5B-ov

## License

AFM-4.5B is released under the Apache-2.0 license.