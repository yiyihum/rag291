---
library_name: transformers
datasets:
- openGPT-X/gsm8kx
language:
- de
base_model:
- Qwen/Qwen2.5-3B-Instruct
pipeline_tag: text-generation
---

# German R1

![A German whale](https://huggingface.co/malteos/german-r1/resolve/main/german-whale.png)

**Introducing German-R1. We are so back!!11**

- 🇩🇪 German R1 is a reasoning model almost equivalent to OpenAI‘s o3 or DeepSeek‘s R1 - but it thinks in German!  

- 🇩🇪 German R1 is so efficient that is was build without any government funding. 

- 🇩🇪 German R1 was only trained with legally imported H100s in less than five minutes. 

- Please do NOT take this too serious. 

## Context

![some contex](https://huggingface.co/malteos/german-r1/resolve/main/context.png)

See Linkedin: https://www.linkedin.com/posts/activity-7294337496023269376-ZBkI

## Usage

You can run the model as follows:

```python
from transformers import pipeline, set_seed
import json

set_seed(42)
pipe = pipeline("text-generation", "malteos/german-r1")

# from gsm8k test set
question = "James beschließt, 3-mal pro Woche 3 Sprints zu laufen.  Er läuft 60 Meter pro Sprint.  Wie viele Meter läuft er insgesamt pro Woche?"
expected_answer = "540"

# xml reasoning and answer format
system_prompt = """
Antworte auf deutsch und in diesem Format:
<reasoning>
...
</reasoning>
<answer>
...
</answer>
"""

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {"role": "user", "content": dataset["question"][3]},
]
response = pipe(messages, max_new_tokens=256)

print(json.dumps(response, indent=4, ensure_ascii=False))
```

The output should look like this (correct answer: 540)

```json
[
    {
        "generated_text": [
            {
                "role": "system",
                "content": "\nAntworte auf deutsch und in diesem Format:\n<reasoning>\n...\n</reasoning>\n<answer>\n...\n</answer>\n"
            },
            {
                "role": "user",
                "content": "James beschließt, 3-mal pro Woche 3 Sprints zu laufen.  Er läuft 60 Meter pro Sprint.  Wie viele Meter läuft er insgesamt pro Woche?"
            },
            {
                "role": "assistant",
                "content": "<reasoning>\nJames läuft 3 Sprints pro Tag, wobei jeder Sprint 60 Meter beträgt. Deshalb läuft er pro Tag 3 Sprints * 60 Meter/Sprint = 180 Meter. James läuft 3 Mal pro Woche, also läuft er insgesamt 180 Meter * 3 = 540 Meter pro Woche.\n</reasoning>\n<answer>\n540\n</answer>\n"
            }
        ]
    }
]
```

## Training details

- Base model: Qwen2.5-3B-Instruct
- Implementation: based on [GRPO demo](https://gist.github.com/willccbb/4676755236bb08cab5f4e54a0475d6fb) by [will brown](https://x.com/willccbb) + language identification reward
- Training data: German subset of [openGPT-X/gsm8kx](https://huggingface.co/datasets/openGPT-X/gsm8kx/) (machine translated from the English gsm8k)


## License

[Qwen research](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/blob/main/LICENSE)