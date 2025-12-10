---
base_model: LLM360/K2-Think
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- abliterated
- uncensored
---

# huihui-ai/Huihui-K2-Think-abliterated


This is an uncensored version of [LLM360/K2-Think](https://huggingface.co/LLM360/K2-Think) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).  


### Transformers
You can use `K2-Think` with Transformers. If you use `transformers.pipeline`, it will apply the chat template automatically. If you use `model.generate` directly, you need to apply the chat template mannually.

```python
from transformers import pipeline
import torch

model_id =  "huihui-ai/Huihui-K2-Think-abliterated"

pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "user", "content": "what is the next prime number after 2600?"},
]

outputs = pipe(
    messages,
    max_new_tokens=32768,
)
print(outputs[0]["generated_text"][-1])
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
