---
library_name: transformers
license: apache-2.0
language:
- tr
datasets:
- vngrs-ai/vngrs-web-corpus
---

## Model Information
<img src="https://cdn-uploads.huggingface.co/production/uploads/6147363543eb04c443cd4e39/1X8noMmS6Mlvj4BalQkuZ.png" alt="preview" width="600"/>

Kumru-2B is the lightweight, open-source version of Kumru LLM, developed for Turkish from scratch by VNGRS.

- It is pre-trained on a cleaned, deduplicated corpora of 500 GB for 300B tokens, and supervised fine-tuned on 1M examples.
- It comes with a modern tokenizer developed for Turkish, supporting code, math and chat template.
- Kumru has a native context length of 8,192 tokens by default.
- This is the **Base** version, which is only pre-trained, not instruct fine-tuned.
- Instruct fine-tuned version is [here](https://huggingface.co/vngrs-ai/Kumru-2B)

Try to demo of 7B version [here](https://kumru.ai/).

## Use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "vngrs-ai/Kumru-2B-Base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

def complete_text(starting_text):
    tokenized_text = tokenizer.encode_plus(starting_text, return_tensors = 'pt', return_token_type_ids=False,
                                           max_length = model.config.max_position_embeddings, truncation = True).to(model.device)
    generated_tokens = model.generate(**tokenized_text, 
                                      max_length = 512,
                                      repetition_penalty = 1.15,
                                      no_repeat_ngram_size = 5
                                     )
    generated_text = tokenizer.decode(generated_tokens.cpu().detach().numpy().reshape(-1).tolist(), skip_special_tokens=True)

    return generated_text

starting_text = "Efes antik kenti"
generated_text = complete_text(starting_text)
print(generated_text)
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
  url={https://huggingface.co/vngrs-ai/Kumru-2B-Base}
}
```