---
license: mit
base_model:
- inclusionAI/Ling-1T-base-2.0
pipeline_tag: text-generation
library_name: transformers
---



<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*4QxcQrBlTiAAAAAAQXAAAAgAemJ7AQ/original" width="100"/>
<p>

<p align="center">🤗 <a href="https://huggingface.co/inclusionAI">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope</a></p>


## Ring-1T-preview, Deep Thinking, No Waiting

Recently, we have been fully occupied with the post-training of Ling 2.0's __1T foundational language model__, striving to maximize the __natural language reasoning__ potential of this trillion-scale base model. 
Conducting post-training on such a huge model, particularly the "training" involved in large-scale reinforcement learning, stands as one of the most technically challenging tasks the Ling Team has encountered since its establishment. 
On the other hand, it has also been a process that continuously reshapes our technical understanding and reinforces the belief that "__scaling is all you need__"

In the early stages of large-scale reinforcement learning training, __Ring-1T__, the thinking version of the 1T foundational language model, has already demonstrated __powerful natural language reasoning capabilities__. 
In __AIME 2025__ (American Invitational Mathematics Examination), the model achieved a high score of 92.6 through pure natural language reasoning, further approaching GPT-5 with thinking (no tools)'s score of 94.6. 
Additionally, the model has shown strong competitiveness in the __Harvard-MIT Mathematics Tournament__ (HMMT) 2025, __competition-level code generation tasks__ such as LiveCodeBench v6 and CodeForces, as well as the __abstraction and reasoning benchmark__ ARC-AGI-1 task.

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*Q1NZT4ti6aoAAAAAgBAAAAgAemJ7AQ/original"/>
<p>

To further explore the reasoning limits of the early version of Ring-1T, we integrated it into the multi-agent framework AWorld (https://github.com/inclusionAI/AWorld
) and conducted pure natural language reasoning tests on the IMO 2025 (International Mathematical Olympiad, 6 problems in total).

Previously, we tested Ring-flash-2.0, using the same method: under the setting of three allowed reasoning attempts, Ring-flash-2.0 only managed to solve Problem 3 on the third try. 
In contrast, during this test, Ring-1T solved Problem 3 in just one attempt, and also produced partially correct answers on Problems 1, 2, 4, and 5 in a single try. 
This demonstrates advanced reasoning capabilities essential for top-tier math competitions—such as insight, constructive problem solving, counterexample generation, strategic thinking, and rigorous logical-chain reasoning—highlighting the stronger reasoning potential of large-scale thinking models.

### IMO Cases
<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/SmsySpw3lR4AAAAAQzAAAAgADod9AQFr/original"/>
<p>

<p align="center">
    <img src="https://mdn.alipayobjects.com/huamei_d2byvp/afts/img/VLMESYD3ZrgAAAAARAAAAAgADod9AQFr/original"/>
<p>



To facilitate early community exploration of the reasoning capabilities of the trillion-parameter thinking model Ring-1T, we have decided to open-source its preview version, __Ring-1T-preview__, ahead of schedule. 
This model retains the efficient MoE architecture of Ling 2.0, completed pre-training on 20T tokens of corpora, and underwent RLVR training tailored for reasoning abilities within our self-developed efficient reinforcement learning system __ASystem__ (the __AReaL__ framework of which has been open-sourced), leveraging the previously disclosed "__icepop__" method(https://ringtech.notion.site/icepop).


__Ring-1T__ remains under continuous training. 
While the preview version already demonstrates powerful natural language reasoning capabilities, it still exhibits issues such as language mixing, repetitive reasoning and identity misperception. 
__We look forward to community exploration and feedback to collectively accelerate the iterative refinement of this trillion-parameter foundation.__




## Quickstart

### 🤗 Hugging Face Transformers

Here is a code snippet to show you how to use the chat model with `transformers`:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "inclusionAI/Ring-1T-preview"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Give me a short introduction to large language models."
messages = [
    {"role": "system", "content": "You are Ling, an assistant created by inclusionAI"},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt", return_token_type_ids=False).to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=8192
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

### 🤖 ModelScope

If you're in mainland China, we strongly recommend you to use our model from 🤖 <a href="https://modelscope.cn/organization/inclusionAI">ModelScope</a>.


## License

This code repository is licensed under [the MIT License](https://github.com/inclusionAI/Ling-V2/blob/main/LICENSE).

## Tip
To facilitate academic research and downstream applications with customizable model naming, we did not conduct specific identity recognition training.

