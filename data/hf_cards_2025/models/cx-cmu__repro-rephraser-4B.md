---
base_model:
- Qwen/Qwen3-4B
datasets:
- cx-cmu/repro-rl-data
language:
- en
tags:
- pretraining
pipeline_tag: text-generation
library_name: transformers
license: apache-2.0
---

This is the 4B rephraser from [RePro: Training Language Models to Faithfully Recycle the Web for Pretraining](https://huggingface.co/papers/2510.10681).

The model is trained with RL from [Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) to generate high-quality and faithful web rephrasings.

Code: https://github.com/cxcscmu/RePro

## Example Usage

```python
from vllm import LLM, SamplingParams
import re

# -----------------------
# 1. Define model and params
# -----------------------
llm = LLM(model="cx-cmu/repro-rephraser-4B")

sampling_params = SamplingParams(
    temperature=1.0,
    top_p=0.9,
    max_tokens=2048,
)

# -----------------------
# 2. Define the paraphrasing prompt
# -----------------------
template = """Your task is to read and paraphrase the provided text following these instructions:
- Delete clearly irrelevant content:
  - Website headers, navigation bars, or menu items (e.g., "Home | About | Contact")
  - Unrelated HTTP links (e.g., ads, trackers, developer tools)
  - Generic footers (e.g., contact info, privacy policies, unsubscribe links)
  - Empty lines or decorative elements (e.g., "---")
- Preserve all content that is relevant and meaningful:
  - Informative or independently useful
  - Related to the topic, even tangentially
  - Provides context, background, or supporting value
  - Includes technical terms, key concepts, factual details, reasoning, and examples
- Handle mixed-relevance sentences carefully:
  - Remove only the irrelevant fragment if the rest remains coherent
  - Delete the whole sentence if the remainder loses meaning
- Do not alter meaningful content unnecessarily:
  - Only delete or modify when content is clearly meaningless or off-topic
  - Preserve the original structure, logic, and depth of the text
- Do not add explanations, notes, assumptions, or claims not found in the original text
Here is the text:
{TEXT}
Task:
After thoroughly reading the above text, paraphrase it in high-quality and clear English following the instructions.
Start your response immediately with "Here is a paraphrased version:" and then provide the paraphrased text."""

# -----------------------
# 3. Prepare a sample conversation
# -----------------------
sample_text = """The Pittsburgh Steelers are a professional American football team based in Pittsburgh, Pennsylvania.
They were established in 1933 and are one of the oldest franchises in the NFL."""

conversation = [
    {
        "role": "system",
        "content": "A chat between a user and an assistant. The assistant paraphrases text faithfully and clearly. /no_think",
    },
    {
        "role": "user",
        "content": template.format(TEXT=sample_text),
    },
]

# -----------------------
# 4. Run vLLM inference
# -----------------------
output = llm.chat([conversation], sampling_params)
response_text = output[0].outputs[0].text

# -----------------------
# 5. Extract paraphrased text
# -----------------------
match = re.search(r"Here is a paraphrased version:(.*)", response_text, re.DOTALL)
if match:
    paraphrased = match.group(1).strip()
else:
    paraphrased = response_text.strip()

print("=== Paraphrased Output ===")
print(paraphrased)
```