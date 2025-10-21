---
license: apache-2.0
datasets:
- vngrs-ai/vngrs-web-corpus
language:
- tr
base_model:
- vngrs-ai/Kumru-2B
pipeline_tag: text-generation
---
# Kumru-2B Details

## Model Information
<img src="https://cdn-uploads.huggingface.co/production/uploads/6147363543eb04c443cd4e39/1X8noMmS6Mlvj4BalQkuZ.png" alt="preview" width="600"/>

Kumru-2B is the lightweight, open-source version of Kumru LLM, developed for Turkish from scratch by VNGRS.

- It is pre-trained on a cleaned, deduplicated corpora of 500 GB for 300B tokens, and supervised fine-tuned on 1M examples.
- It comes with a modern tokenizer developed for Turkish, supporting code, math and chat template.
- Kumru has a native context length of 8,192 tokens by default.
- This is the **instruct fine-tuned** version.
- Pre-trained Base version is [here](https://huggingface.co/vngrs-ai/Kumru-2B-Base)

Try the demo of 7B version [here](https://kumru.ai/).

## Use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "vngrs-ai/Kumru-2B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

def generate_response(query):
    messages = [
        {'role': 'system', 'content': 'Adın Kumru. VNGRS tarafından Türkçe için sıfırdan eğitilmiş bir dil modelisin.'},
        {'role': 'user', 'content': query}
    ]
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors='pt', add_generation_prompt=True).to(model.device)
    model_outputs = model.generate(model_inputs, max_new_tokens=512, do_sample=True, top_p=0.9, temperature=0.7, repetition_penalty=1.1)
    output_tokens = model_outputs[0].cpu().detach().numpy().tolist()
    generated_tokens = output_tokens[model_inputs[0].shape[0]:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    return response

query = "Efes antik kentinin önemi nedir?"
response = generate_response(query)
print(response)
```


## Evaluation Results
Both Kumru-7B and Kumru-2B are evaluated on Cetvel benchmark.

<img src="https://cdn-uploads.huggingface.co/production/uploads/6147363543eb04c443cd4e39/eu2TuwVpLwRWAh3MjWc1v.png" alt="preview" width="750"/>

We observe that Kumru overall surpasses significantly larger models such as LLaMA-3.3–70B, Gemma-3–27B, Qwen-2–72B and Aya-32B. It excels at tasks related to the nuances of the Turkish language, such as grammatical error correction and text summarization.

## Tokenizer Efficiency
Kumru tokenizer is a modern BPE tokenizer with a vocabulary size of 50,176, pre-tokenization regex and a chat template.

<img src="https://cdn-uploads.huggingface.co/production/uploads/6147363543eb04c443cd4e39/zz6E1kba8UCq9N7oMDnKB.png" alt="preview" width="750"/>

Other open-source models spend between 38% to 98% more tokens than Kumru while still having larger vocabulary sizes.
This means Kumru can represent more texts in its context length and process faster and cheaper. Although the native context length of Kumru is 8,192, its effective context length can be considered between 1128 and 1618, compared to other multilingual models out there.
This shows the efficiency of having a native Turkish tokenizer in terms of representation power, speed and cost.

## Citation
```
@misc{turker2025kumru,
  title={Kumru},
  author={Turker, Meliksah and Ari, Erdi and Han, Aydin},
  year={2025},
  url={https://huggingface.co/vngrs-ai/Kumru-2B}
}
```