---
base_model: google/gemma-3-270m-it
license: gemma
tags:
- gemma3
- gemma
- google
- generated_from_trainer
- trl
- sft
- abliterated
- uncensored
pipeline_tag: text-generation
library_name: transformers
---

# huihui-ai/Huihui-gemma-3-270m-it-abliterated

This is an uncensored version of [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it), achieved through fine-tuning with the [TRL](https://github.com/huggingface/trl) framework.

The dataset used for fine-tuning is only in English, does not involve other languages, and all tests are conducted solely for English.


## Training procedure

This model was trained with SFT.

### Framework versions

- TRL: 0.21.0
- Transformers: 4.56.0.dev0
- Pytorch: 2.8.0+cu128
- Datasets: 3.6.0
- Tokenizers: 0.21.2

## ollama

You can use [huihui_ai/gemma3-abliterated:270m](https://ollama.com/huihui_ai/gemma3-abliterated:270m) directly, 
```
ollama run huihui_ai/gemma3-abliterated:270m
```

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="huihui-ai/Huihui-gemma-3-270m-it-abliterated", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

### Usage Warnings


 - **Risk of Sensitive or Controversial Outputs**: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

 - **Not Suitable for All Audiences**: Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

 - **Legal and Ethical Responsibilities**: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

 - **Research and Experimental Use**: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

 - **Monitoring and Review Recommendations**: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

 - **No Default Safety Guarantees**: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.


### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
- Support our work on Ko-fi (https://ko-fi.com/huihuiai)!
```
