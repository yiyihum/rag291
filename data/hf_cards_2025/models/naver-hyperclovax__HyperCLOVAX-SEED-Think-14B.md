---
license: other
license_name: hyperclovax-seed
license_link: LICENSE
library_name: transformers
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6512d9827fccffe1e9e28fa7/7BT1W9eHLQjRCCENwcXmE.png)

## Overview

HyperCLOVA X SEED 14B Think is a next-generation language model that moves beyond the conventional approach of simply increasing model size to improve performance. It combines [HyperCLOVA X’s lightweighting technology](https://tinyurl.com/y3hrfz67) for building high-efficiency LLMs with advanced reasoning capabilities. Its development relied on two key technologies: (1) Pruning & Knowledge Distillation, which achieves both compactness and high performance, and (2) a Reinforcement Learning (RL) pipeline, which maximizes reasoning ability. By pruning low-importance parameters and distilling knowledge from a large model into a smaller one, training costs have been significantly reduced. On top of this, [the latest RL recipe validated in HyperCLOVA X Think](https://arxiv.org/pdf/2506.22403) is applied in a multi-stage process: (1) Supervised Fine-Tuning (SFT), (2) Reinforcement Learning with Verifiable Rewards (RLVR), (3) Length Controllability (LC) for reasoning path optimization, and (4) a joint training of Reinforcement Learning from Human Feedback (RLHF) and RLVR.

It is a considerable challenge to equip a pruned, knowledge-distilled model with reasoning capabilities, since reductions in training costs and model size often degrade reasoning performance. However, through extensive research experience and persistent trial and error, the HyperCLOVA X team has succeeded in lowering training costs while maintaining reasoning performance comparable to that of larger, resource-intensive models.


## Basic Information

- **Architecture** : Transformer-based architecture with Peri-Layer Normalization and Maximal Update Parameterization(μP) (Dense Model)
- **Parameters** : 14.74B
- **Input/Output Format** (Input/Output) : Text / Text
- **Context Length** : 32k

## Training Cost

`HyperCLOVA X SEED 14B Think` was trained at a significantly lower cost compared to high-performance external models of similar scale. By utilizing HCX’s lightweight training pipeline, it was trained at approximately **52.60×** lower cost than `Qwen2.5-14B` and **91.38×** lower cost than `Qwen3-14B`.

| Model (Base)                    | GPU Hours (A100-80GB, MFU 50%)     |
| ------------------------------- | ---------------------------------- |
| **HyperCLOVA X SEED 14B Think** | **68,049**                         |
| Qwen2.5-0.5B                    | 169,257                            |
| Qwen2.5-1.5B                    | 449,643                            |
| Qwen3-0.6B                      | 602,460                            |
| Qwen3-1.7B                      | 1,063,991                          |
| HyperCLOVA X Think              | 2,197,732                          |
| **Qwen2.5-14B**                 | **3,603,432**                      |
| Qwen3-8B                        | 3,993,607                          |
| **Qwen3-14B**                   | **6,267,077**                      |
| Qwen3-32B                       | 14,108,748                         |

## Benchmarks

Compared to global models of a similar scale, such as Qwen3 14B, HyperCLOVA X SEED 14B Think demonstrates superior performance in Korean language and cultural understanding, while showing competitive performance in math and coding tasks, which are directly or indirectly related to agent capabilities. This trend remains consistent even when compared with larger models like Qwen3 32B and LG Exaone-Deep 32B.

### Backbone Benchmarks Performance Comparison (Non-think)

**Korean/Korea Culture**

| Model                           | Average | CLIcK  | HAERAE-Bench | KOBEST | KorMedMCQA | KMMLU  | KoBigBench | KoCommonGEN-v2 | 
| ------------------------------- | ------- | ------ | ------------ | ------ | ---------- | ------ | ---------- | -------------- | 
| **HyperCLOVA X SEED 14B Think** | 0.7269  | 0.7208 | 0.8506       | 0.8570 | 0.6411     | 0.5428 | 0.7482     | 0.6682         | 
| QWEN3-8B                        | 0.6759  | 0.6206 | 0.6618       | 0.7919 | 0.6471     | 0.5543 | 0.7186     | 0.5773         |
| QWEN3-14B                       | 0.7079  | 0.6707 | 0.6975       | 0.8174 | 0.6979     | 0.5864 | 0.7507     | 0.5927         |


**English/American Culture**
| Model                           | Average | MMLU   | BigBench-Hard | Hellaswag | Winogrande | PIQA   | ARC-challenge | Social IQa |
| ------------------------------- | ------- | ------ | ------------- | --------- | ---------- | ------ | ------------- | ---------- |
| **HyperCLOVA X SEED 14B Think** | 0.6614  | 0.7121 | 0.6216        | 0.6125    | 0.7593     | 0.7791 | 0.6246        | 0.5205     |
| QWEN3-8B                        | 0.6548  | 0.7490 | 0.6072        | 0.5817    | 0.7198     | 0.7666 | 0.6433        | 0.5159     |
| QWEN3-14B                       | 0.6807  | 0.7885 | 0.6325        | 0.6143    | 0.7356     | 0.8025 | 0.6698        | 0.5215     |


### Reasoning Performance Comparison

**Korean/Korea Culture**
| Model | KMMLU | CSAT-ko-2025 | KorMedMCQA | KoBALT | HAERAE | CLIcK | KoBigBench | LogicKor |
|-----------------------------------------|--------|--------|--------|--------|--------|--------|--------|------|
| HyperCLOVA X SEED 14B Think **(Think)** | 0.6649 | 0.7516 | 0.6933 | 0.4500 | 0.8537 | 0.7280 | 0.7974 | 8.74 |
| QWEN3-8B                                | 0.5543 | 0.7200 | 0.6782 | 0.3060 | 0.6618 | 0.6690 | 0.7850 | 8.92 |
| QWEN3-14B                               | 0.4930 | 0.7710 | 0.6850 | 0.3840 | 0.7410 | 0.6880 | 0.8380 | 9.15 |

**Coding/Math**
| Model | GSM8k | MATH500 | HumanEval | MBPP |
|-----------------------------------------|--------|--------|--------|--------|
| HyperCLOVA X SEED 14B Think | 0.9553 | 0.9380 | 0.9451 | 0.8759 |
| QWEN3-14B                   | 0.9590 | 0.9680 | 0.9570 | 0.9080 |


### Non-Think / Think Performance Comparison

| Model | GSM8k | GPT4Eval | MT Bench | Arena-Hard-v0.1 |
|---------------------------------------------|--------|--------|--------|--------|
| HyperCLOVA X SEED 14B Think **(Non-think)** | 0.9348 | 0.6741 | 8.2063 | 0.2733 |
| HyperCLOVA X SEED 14B Think **(Think)**     | 0.9553 | 0.8200 | 8.8313 | 0.5826 |


## ChatML Block

The chat template for HyperCLOVA X consists of the following elements.

- **tool_list** : A list of tools available to the model (in JSON format). If no tools are available, an empty block should be provided.
- **system** : System prompt. If not are available, an empty block should be provided.
- **user** : User input.
- **assistant** : Assistant output.

The basic configuration of ChatML block is as follows.

```
<|im_start|>{tool_list/system/user/assistant}
{content}<|im_end|>
```

- `<|im_start|>` : Start token of ChatML block
- `<|im_end|>` : End token of ChatML block

## (ChatML) General Conversation

### First turn

Given a two-turn conversation between the user and the assistant (`user_query_1`, `assistant_answer_1`, `user_query_2`, `assistant_answer_2`), the prompt for the first-turn can be constructed in its simplest form as follows:

```
<|im_start|>tool_list
<|im_end|>
<|im_start|>system
- You are "CLOVA X," an AI language model developed by NAVER.  
- The current date is {day of the week}, {month} {dd}, {yyyy}.<|im_end|>
<|im_start|>user
{user_query_1}<|im_end|>
<|im_start|>assistant
```

After the `<|im_end|>` token (indicating the end of the ChatML block), the model generates text up to the `<|endofturn|>` token. This output corresponds to the assistant's first response (`assistant_answer_1`).

### Second turn

Based on the assistant's first response (`assistant_answer_1`), when the user asks an additional question (`user_query_2`), the prompt input to the model is constructed as follows:

```
{following the previous context}
{assistant_answer_1}<|im_end|><|endofturn|>
<|im_start|>user
{user_query_2}<|im_end|>
<|im_start|>assistant
```

As in the previous turn, generation continues until the `<|endofturn|>` token appears after `<|im_end|>`. This corresponds to the assistant's second response (`assistant_answer_2`).

## (ChatML) Function Call (Using Tools)

Insert the list of tools available into the tool_list block as a JSON list. For example, the following is a case where the only available tool is `get_weather`.

```
<|im_start|>tool_list
[{"name": "get_weather", "description": "Check the current weather at the requested location.", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "Name of the city"}}, "required": ["location"]}}]<|im_end|>
```

Additional instructions can be included in the system prompt if needed, and it is recommended to format them as `- {content}`. For example:

```
<|im_start|>system
- In this environment, various tools can be used to answer users' questions.
- You are "CLOVA X," an AI language model developed by NAVER.  
- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.
- The current date is {day of the week}, {month} {dd}, {yyyy}.
- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.
- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond.<|im_end|>
```

### First turn

Suppose the user gives the instruction, 'Tell me the weather in Seoul.' The prompt input to the model would then be as follows:

```
<|im_start|>tool_list
[{"name": "get_weather", "description": "Check the current weather at the requested location.", "parameters": {"type": "object", "properties": {"location": {"type": "string", "description": "Name of the city"}}, "required": ["location"]}}]<|im_end|>
<|im_start|>system
- In this environment, various tools can be used to answer users' questions.
- You are "CLOVA X," an AI language model developed by NAVER.  
- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.
- The current date is {day of the week}, {month} {dd}, {yyyy}.
- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.
- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond.<|im_end|>
<|im_start|>user
Tell me the weather in Seoul<|im_end|>
<|im_start|>assistant
```

Generation continues until either the `<|stop|>` or `<|endofturn|>` token appears immediately after `<|im_end|>`. An example of the model’s output is shown below. HyperCLOVA X checks the list of available tools (tool_list), selects the appropriate tool (`get_weather`), and returns the necessary information for the tool call in JSON format.

```
{following the previous context}
Let's check the weather using the get_weather tool.<|im_end|>
<|im_start|>assistant -> tool/function_call
{"name": "get_weather","input": {"location":"Seoul"}}<|im_end|><|stop|>
```

- `assistant -> tool/function_call` means that the assistant(model) invokes a function call.

### Second turn

The model stopped generating because `<|stop|>` token appeared immediately after `<|im_end|>`. Based on the information generated, `get_weather`should now be called. Calling an external function and parsing the result must be implemented additionally. For explanation, let's assume that the result of calling and parsing an external function is `{"result":{"location": "Seoul", "weather": "Sunny", "temperature": 25}}`.

The model is now ready to respond to the second turn. Using all the information gathered so far, input the following prompt into the model and have it follow accordingly.

```
{following the previous context}
<|im_start|>tool/function_call
{"result":{"location": "Seoul", "weather": "Sunny", "temperature": 25}}<|im_end|>
<|im_start|>assistant
```

- `tool/function_call` means it should pass the result of the function call to the assistant(model).

Just like in the previous turn, generation continues until the `<|stop|>` or `<|endofturn|>` token appears immediately after `<|im_end|>`. If the model behaves as expected, the output will look like this.

```
{following the previous context}
The weather in Seoul is clear and the temperature is 25 degrees.<|im_end|><|endofturn|>
```

## (ChatML) Inducing reasoning/non-reasoning


HyperCLOVA X can handle both reasoning and non-reasoning tasks. There is a difference depending on whether the assistant is prompted to 'think' before responding. Based on the previous example, to make HyperCLOVA X respond in reasoning mode, you can input the prompt into the model as follows (excluding the tool_list and system)

```
<|im_start|>user
Tell me the weather in Seoul<|im_end|>
<|im_start|>assistant/think

```

- Note that the prompt ends with `assistant/think\n`(think + `\n).
- Generation continues until either the <|stop|> or <|endofturn|> token appears immediately after `<|im_end|>`.

To have the assistant respond in non-reasoning mode (i.e., answer directly), you can input the following prompt.

```
<|im_start|>user
Tell me the weather in Seoul<|im_end|>
<|im_start|>assistant

```

- Note that the prompt ends with `assistant\n`(assistant + `\n`).
- Generation continues until either the <|stop|> or <|endofturn|> token appears immediately after `<|im_end|>`.


### Adjusting inference length
The length of reasoning can be controlled by appending "\nThink for maximum {N} tokens" at the end of the user's utterance.

Example
Suppose the user says, "Tell me the prime number closest to 1000."
If you want the model to reason for approximately 1024 tokens before answering, you would construct the prompt as follows:


```
<|im_start|>tool_list
<|im_end|>
<|im_start|>system
- You are "CLOVA X," an AI language model developed by NAVER.  
- The current date is {day of the week}, {month} {dd}, {yyyy}.<|im_end|>
<|im_start|>user
Tell me the prime number closest to 1000.
Think for maximum 1024 tokens.<|im_end|>
<|im_start|>assistant/think

```
- Adjusting the reasoning length means guiding the model to reason for approximately the specified number of tokens; it does not always generate for exact number of tokens given.


### Multiturn inference

When engaging in multi-turn conversations with reasoning enabled, the reasoning content from previous turns (`<|im_start|>assistant/think\n...<|im_end|>`) is not included in the next turn's prompt. Instead, as in the standard multi-turn dialogue format, only the final assistant response is included in the prompt passed to the model.

The same applies when a function call is made during reasoning: the reasoning content is excluded, and only the function call block (`<|im_start|>assistant -> tool/function_call\n...<|im_end|><|stop|>`) is included in the prompt provided to the model.

Example: Solving a simple math problem
Suppose the user sends a request: "Calculate the sum of odd numbers from 1 to 10."
The following explains step-by-step how this is processed as a multi-turn reasoning interaction.

1. First Turn
Input Prompt
```
<|im_start|>tool_list
<|im_end|>
<|im_start|>system
<|im_end|>
<|im_start|>user
Calculate the sum of odd numbers from 1 to 10
<|im_end|>
<|im_start|>assistant/think

```
The model begins to generate inference contents.
```
{following the previous context}
The user wants me to find the sum of the odd numbers from 1 to 10. First, I need to clearly understand the problem. I should identify which numbers between 1 and 10 are odd. Going through the numbers in order, the odd numbers are 1, 3, 5, 7, and 9. Since 10 is even, it is excluded. Now, I need to add these numbers together. Adding them step by step: 1+3=4, plus 5 gives 9, plus 7 gives 16, and finally adding 9 gives 25. But is there another way to calculate this? For example, I could use the formula for the sum of an arithmetic sequence. The odd numbers here form an arithmetic sequence with the first term 1 and a common difference of 2. I need to count the number of terms first—there are 5 odd numbers between 1 and 10. The formula for the sum of an arithmetic sequence is n*(a₁ + aₙ)/2, where n is 5, a₁ is 1, and aₙ is 9. Plugging these in, we get 5*(1 + 9)/2 = 5*10/2 = 25, which matches the previous result. Since both methods give 25, I’ll double-check that this is the answer the user expects, and then provide a concise explanation.<|im_end|>
<|im_start|>assistant
The odd numbers from 1 to 10 are **1, 3, 5, 7, 9**.
The sum of these numbers is calculated as follows:

\[
1 + 3 + 5 + 7 + 9 = 25
\]

Alternatively, the sum can be easily calculated using **the formula for the sum of an arithmetic sequence**:
- First term (\(a_1\)) = 1
- Last term (\(a_n\)) = 9
- Number of terms (\(n\)) = 5

\[
\text{Sum} = \frac{n(a_1 + a_n)}{2} = \frac{5 \times (1 + 9)}{2} = \frac{5 \times 10}{2} = 25
\]

**Result:** The answer is **25**.<|im_end|><|endofturn|>
```
As the `<|endofturn|>` token has been generated, the model concludes the current turn and awaits the next user input.

2. Second Turn
Suppose you want to follow up with: "What is the result of adding 10 to that sum?" Here, the prompt is created by excluding the reasoning content (assistant/think) from the first turn and including only the final response (assistant).

- Input Prompt

```
<|im_start|>tool_list
<|im_end|>
<|im_start|>system
<|im_end|>
<|im_start|>user
Calculate the sum of odd numbers from 1 to 10
<|im_end|>
<|im_start|>assistant
The odd numbers from 1 to 10 are **1, 3, 5, 7, 9**.
The sum of these numbers is calculated as follows:

\[
1 + 3 + 5 + 7 + 9 = 25
\]

Alternatively, the sum can be easily calculated using **the formula for the sum of an arithmetic sequence**:
- First term (\(a_1\)) = 1
- Last term (\(a_n\)) = 9
- Number of terms (\(n\)) = 5

\[
\text{Sum} = \frac{n(a_1 + a_n)}{2} = \frac{5 \times (1 + 9)}{2} = \frac{5 \times 10}{2} = 25
\]

**Result:** The answer is **25**.<|im_end|><|endofturn|>
<|im_end|>
<|im_start|>user
What is the result of adding 10 to that sum?
<|im_end|>
<|im_start|>assistant/think

```

- Excluded contents in the second turn input
```
<|im_start|>assistant/think
{following the previous context}
The user wants me to find the sum of the odd numbers from 1 to 10. First, I need to clearly understand the problem. I should identify which numbers between 1 and 10 are odd. Going through the numbers in order, the odd numbers are 1, 3, 5, 7, and 9. Since 10 is even, it is excluded. Now, I need to add these numbers together. Adding them step by step: 1+3=4, plus 5 gives 9, plus 7 gives 16, and finally adding 9 gives 25. But is there another way to calculate this? For example, I could use the formula for the sum of an arithmetic sequence. The odd numbers here form an arithmetic sequence with the first term 1 and a common difference of 2. I need to count the number of terms first—there are 5 odd numbers between 1 and 10. The formula for the sum of an arithmetic sequence is n*(a₁ + aₙ)/2, where n is 5, a₁ is 1, and aₙ is 9. Plugging these in, we get 5*(1 + 9)/2 = 5*10/2 = 25, which matches the previous result. Since both methods give 25, I’ll double-check that this is the answer the user expects, and then provide a concise explanation.<|im_end|>
```

For all later turns, the reasoning (think) content from previous turns is not added to the prompt as well.

### Difference between <|stop|> and <|endofturn|>

- **Similarity**
    - They both act as signals to stop the model from generating further responses.

- **Difference**
    - <|stop|>: After the response generation is halted and the tool_invoke results are processed, the AI turn resumes.
    - <|endofturn|>: After the response generation is halted, the AI turn is fully terminated, and the model waits for the user's next input.


## **Huggingface Usage Example**

After downloading the model binaries, including the configuration files, to a local path(`/path/to/hyperclova-x-seed-think-14b`), you can run the following in a Python environment with the [Huggingface library](https://huggingface.co/docs/transformers/installation)(verified to work with version >= 4.53.0) and [timm(pytorch-image-models)](https://github.com/huggingface/pytorch-image-models) installed.

You can use the `apply_chat_template` parameter to explicitly enable or disable the reasoning feature.

- The default value for both options is `None`, in which case the model decides on its own whether to reason before answering or to answer directly without reasoning.
- `force_reasoning=True`: Forces the model to always reason before answering.
- `skip_reasoning=True`: Forces the model to answer directly without reasoning.
- Passing `None` or `False` has the same effect.
- If both are set to True, `force_reasoning=True` takes precedence.

```python
# Default example
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, return_dict=True, return_tensors="pt")

# By adding force_reasoning=True, the model is forced to always reason before responding
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, force_reasoning=True, return_dict=True, return_tensors="pt")

# By adding skip_reasoning=True, the model is forced to always answer directly without reasoning
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, skip_reasoning=True, return_dict=True, return_tensors="pt")
```

### Non-think Example Code
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

chat = [
  {"role": "system", "content": "- In this environment, various tools can be used to answer users' questions.\n- You are \"CLOVA X,\" an AI language model developed by NAVER.\n- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.\n- The current date is Monday, July 21, 2025.\n- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.\n- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond."},
  {"role": "user", "content": "Explain in as much detail as possible the relationship between the Schrödinger equation and quantum mechanics."},
]

# By adding skip_reasoning=True, the model is forced to always answer directly without reasoning
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, skip_reasoning=True, return_dict=True, return_tensors="pt")
inputs = inputs.to("cuda")

output_ids = model.generate(
    **inputs,
    max_length=1024,
    stop_strings=["<|endofturn|>", "<|stop|>"],
    temperature=0.5,
    top_p=0.6,
    repetition_penalty=1.05,
    tokenizer=tokenizer
)
print(tokenizer.batch_decode(output_ids))
```

### Think Example Code
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

chat = [
  {"role": "system", "content": "- In this environment, various tools can be used to answer users' questions.\n- You are \"CLOVA X,\" an AI language model developed by NAVER.\n- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.\n- The current date is Monday, July 21, 2025.\n- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.\n- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond."},
  {"role": "user", "content": "Explain in as much detail as possible the relationship between the Schrödinger equation and quantum mechanics."},
]

# By adding force_reasoning=True, the model is forced to always reason before responding
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, force_reasoning=True, return_dict=True, return_tensors="pt")
inputs = inputs.to("cuda")

output_ids = model.generate(
    **inputs,
    max_length=1024,
    stop_strings=["<|endofturn|>", "<|stop|>"],
    temperature=0.5,
    top_p=0.6,
    repetition_penalty=1.05,
    tokenizer=tokenizer
)
print(tokenizer.batch_decode(output_ids))
```

### Hybrid(the model decides whether to use think or non-think mode) Example Code
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

chat = [
  {"role": "system", "content": "- In this environment, various tools can be used to answer users' questions.\n- You are \"CLOVA X,\" an AI language model developed by NAVER.\n- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.\n- The current date is Monday, July 21, 2025.\n- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.\n- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond."},
  {"role": "user", "content": "Explain in as much detail as possible the relationship between the Schrödinger equation and quantum mechanics."},
]

# The model decides whether to answer after reasoning or to respond immediately without reasoning
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = inputs.to("cuda")

output_ids = model.generate(
    **inputs,
    max_length=1024,
    stop_strings=["<|endofturn|>", "<|stop|>"],
    temperature=0.5,
    top_p=0.6,
    repetition_penalty=1.05,
    tokenizer=tokenizer
)
print(tokenizer.batch_decode(output_ids))
```

### Example code for function calls (tool usage)
For a scenario involving tool usage, you can execute it as follows.

```python
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B"
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 1) The name of the tool should be written as function_call.{{ name }}.
# 2) Parameters follow the specifications described at https://platform.openai.com/docs/guides/function-calling?api-mode=responses.
tool_list = [
    {   
        "type": "function",
        "function": {
            "name": "add",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "First number"},
                    "y": {"type": "number", "description": "Second number"}
                },
                "required": ["x", "y"]
            }
        }
    }, {
        "type": "function",
        "function": {
            "name": "subtract",
            "description": "Subtract two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "First number"},
                    "y": {"type": "number", "description": "Second number"}
                },
                "required": ["x", "y"]
            }
        }
    }
]   


chat = [
  {"role": "system", "content": "- In this environment, various tools can be used to answer users' questions.\n- You are \"CLOVA X,\" an AI language model developed by NAVER.\n- Begin by creating a plan for solving the problem, and then utilize the tools accordingly to address the problem.\n- The current date is Monday, July 21, 2025.\n- Latest information such as news, stock prices, and shopping is retrieved through the tool_list.\n- If external tools are required, the assistant should not answer directly but must first obtain the necessary information via the assistant -> tool/function_call role, and then respond."},
  {"role": "user", "content": "What is 1588 + 1234? Please calculate it using the provided tool."},
]

inputs = tokenizer.apply_chat_template(chat, tools=tool_list, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = inputs.to("cuda")

output_ids = model.generate(
    **inputs,
    max_length=1024,
    stop_strings=["<|endofturn|>", "<|stop|>"],
    temperature=0.5,
    top_p=0.6,
    repetition_penalty=1.05,
    tokenizer=tokenizer
)
print(tokenizer.batch_decode(output_ids))
```

- If you have any questions or issues regarding usage, please leave them as an issue in the Discussions section of this page.

## **vLLM Usage Example**

The HyperCLOVA X SEED Think model is built on a custom LLM architecture based on the LLaMA architecture, incorporating μP and Peri-LN techniques. For convenient use with vLLM, it is available as a dedicated vLLM plugin that can be installed and used with ease once vLLM is set up.

1. Download vLLM plugin source code

    ```bash
    git clone https://github.com/NAVER-Cloud-HyperCLOVA-X/hcx-vllm-plugin
    ```

2. vLLM Plugin Build & Installation: While keeping the NAVER-Cloud-HyperCLOVA-X/hcx-vllm-plugin path downloaded in step 1, refer to the commands below.

    ```bash
    pip install -e .
    ```

After downloading the model checkpoint to a local path (`/path/to/hyperclova-x-seed-think-14b`), you can perform text inference by running the following commands on a GPU environment with A100 or higher.

```bash
python -m vllm.entrypoints.openai.api_server --model=/path/to/hyperclova-x-seed-think-14b --trust_remote_code --port=8000

curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
"prompt": "<|im_start|>tool_list\n<|im_end|>\n<|im_start|>system\n- The AI language model is named \"CLOVA X\" and was developed by NAVER.\n- Today is Friday, July 18, 2025.<|im_end|>\n<|im_start|>user\nExplain in as much detail as possible the relationship between the Schrödinger equation and quantum mechanics.<|im_end|>\n<|im_start|>assistant/think\n",
"top_k":-1,
"temperature":0.5,
"top_p":0.6,
"repetition_penalty":1.05,
"stop":["<|im_end|><|endofturn|>", "<|im_end|><|stop|>"],
"max_tokens":8192,
"skip_special_tokens":false
}'
```

### Chat Completions Usage Example

1.  Using the Chat completions endpoint

<!-- end list -->

  - Basic serving script (same as completions)

    `vllm serve naver-hyperclovax/HyperCLOVAX-SEED-Think-14B --trust_remote_code`

  - Sampling parameters such as `top_k`, `temperature`, `top_p`, `repetition_penalty`, and `max_tokens` can be set freely.

  - However, the `skip_special_tokens` and `stop` options must be set as below for vLLM to recognize the model's token generation stop signal and cease generation.

  - request example

    ```bash
    curl -X POST http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B",
        "messages": [
            {"role": "system", "content": "- The AI language model is named \"CLOVA X\" and was developed by NAVER.\n- Today is Friday, July 18, 2025."},
            {"role": "user", "content": "Explain in as much detail as possible the relationship between the Schrödinger equation and quantum mechanics."}
        ],
        "skip_special_tokens":false,
        "stop": [
            "<|im_end|><|endofturn|>",
            "<|im_end|><|stop|>"
        ],
        "top_k": -1,
        "temperature": 0.5,
        "top_p": 0.6,
        "repetition_penalty": 1.05,
        "max_tokens": 8192
    }'
    ```

<!-- end list -->

2.  tool call usage example

<!-- end list -->

  - Serving script

      - You need to add `--enable-auto-tool-choice --tool-call-parser hcx` to the existing script.

        `vllm serve naver-hyperclovax/HyperCLOVAX-SEED-Think-14B --trust_remote_code --enable-auto-tool-choice --tool-call-parser hcx`

  - request example

      - If you put the available tools in `tools`, they will be applied to the `tool_list` part passed to the model.

        ```bash
        curl -X POST http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
            "model": "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B",
            "messages": [
            {"role": "user", "content": "Could you please tell me the current weather conditions in Boston, MA in Celsius?"}
            ],
            "stop": ["<|im_end|><|stop|>", "<|im_end|><|endofturn|>"],
            "max_tokens": 8192,
            "skip_special_tokens": false,
            "tools": [
            {
                "type": "function",
                "function": {
                "name": "get_current_weather",
                "description": "Retrieves the current weather conditions for a specified city and state.",
                "parameters": {
                    "type": "object",
                    "required": ["location"],
                    "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location for which to get the weather, in the format of \'\\'City, State\\'', such as \'\\'San Francisco, CA\\'' if State for the city exists. \'\\'City, Country\\'' if State for the city does not exist. Use short form for state."
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit of temperature for the weather report.",
                        "enum": ["celsius", "fahrenheit"],
                        "default": "fahrenheit"
                    }
                }
                }
            }
            }
        ]
        }'
        ```

  - response example

      - Parsed tool calls are returned in the `tool_calls` field.
      - If there is a response generated by the model other than the tool call, it is returned in the `content` field. Otherwise, `null` is returned.
        ```bash
        {
            "id": "chatcmpl-b9aad45639464c0ebf71861df13b4eb2",
            "object": "chat.completion",
            "created": 1753358351,
            "model": "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "reasoning_content": null,
                        "content": null,
                        "tool_calls": [
                            {
                                "id": "chatcmpl-tool-b9513352e4c64065a315e495b2613753",
                                "type": "function",
                                "function": {
                                    "name": "get_current_weather",
                                    "arguments": "{\"location\": \"Boston, MA\", \"unit\": \"celsius\"}"
                                }
                            }
                        ]
                    },
                    "logprobs": null,
                    "finish_reason": "tool_calls",
                    "stop_reason": "<|im_end|><|stop|>"
                }
            ],
            "usage": {
                "prompt_tokens": 189,
                "total_tokens": 224,
                "completion_tokens": 35,
                "prompt_tokens_details": null
            },
            "prompt_logprobs": null,
            "kv_transfer_params": null
        }
        ```

<!-- end list -->

3.  reasoning usage example

<!-- end list -->

  - Serving script
      - You need to add `--enable-reasoning --reasoning-parser hcx` to the existing script.

        `vllm serve naver-hyperclovax/HyperCLOVAX-SEED-Think-14B --trust_remote_code --enable-reasoning --reasoning-parser hcx`

      - The `--enable-reasoning` option has been deprecated since vLLM v0.9.0.

          - If you are using vLLM v0.9.0 or higher, you only need to add `--reasoning-parser hcx` without `--enable-reasoning`.

      - The reasoning parser extracts the reasoning content from responses generated in reasoning mode. This option does not always make the model operate in reasoning mode, nor does excluding the parser necessarily force non-reasoning operation.

      - request example

          - `"chat_template_kwargs": {"force_reasoning": true}` forces reasoning.
          - `"chat_template_kwargs": {"skip_reasoning": true}` forces non-reasoning.
          - If both are set to `true`, `force_reasoning: true` has higher priority.
          - If neither is given, the model decides whether to reason or not.

        <!-- end list -->

        ```bash
        curl -X POST http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
            "model": "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Tell me the prime number closest to 1000."}
            ],
            "stop": ["<|im_end|><|stop|>", "<|im_end|><|endofturn|>"],
            "max_tokens": 8192,
            "skip_special_tokens": false,
            "chat_template_kwargs": {"force_reasoning": true}
        }'
        ```

      - response example

          - The reasoning part is returned in the `reasoning_content` field, and the assistant's final response is returned in the `content` field separately.

        <!-- end list -->

        ```bash
        {
            "id": "chatcmpl-157d282ebaca4333a9f04b1bdfa7eb8b",
            "object": "chat.completion",
            "created": 1753361336,
            "model": "naver-hyperclovax/HyperCLOVAX-SEED-Think-14B",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "reasoning_content": "Okay, so I need to find the prime number closest to 1000. Hmm, let's start by recalling what a prime number is. ... (중략) ... But in this case, at least for the nearest, 3 versus9, which gives997 as the answer.\n\nTherefore, the correct answer would be997.",
                        "content": "\nThe prime number closest to 1000 is **997**. \n\nHere's the reasoning:\n1. **Check if 1000 is prime:** It's even, so not prime.\n2. **Find primes near 1000:**\n   - **Below 1000:** Check numbers downward. \n     - Upon verifying, 997 is prime (no divisors up to its square root).\n   - **Above 1000:** Next prime after 997 is 1009, which is 9 units away from 1000.\n3. **Compare distances:**\n   - \\( |1000 - 997| = 3 \\)\n   - \\( |1009 - 1000| = 9 \\)\n   \nSince 3 < 9, **997** is the closest prime. \n\n\\boxed{997}",
                        "tool_calls": []
                    },
                    "logprobs": null,
                    "finish_reason": "stop",
                    "stop_reason": "<|im_end|><|endofturn|>"
                }
            ],
            "usage": {
                "prompt_tokens": 38,
                "total_tokens": 3254,
                "completion_tokens": 3216,
                "prompt_tokens_details": null
            },
            "prompt_logprobs": null,
            "kv_transfer_params": null
        }
        ```

<!-- end list -->

4.  reasoning + tool call usage example

<!-- end list -->

  - Serving script
      - If you want to use both the reasoning parser and the tool call parser, you can combine the reasoning serving script and the tool call serving script.

        `vllm serve naver-hyperclovax/HyperCLOVAX-SEED-Think-14B --trust_remote_code --enable-auto-tool-choice --tool-call-parser hcx --enable-reasoning --reasoning-parser hcx`


## License

The model is licensed under [HyperCLOVA X SEED Model License Agreement](./LICENSE)

## Citation

```
@misc{navercloudhyperclovaxteam2025hyperclovaxthinktechnical,
      title={HyperCLOVA X THINK Technical Report}, 
      author={NAVER Cloud HyperCLOVA X Team},
      year={2025},
      eprint={2506.22403},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.22403}, 
}
```

## Questions

For any other questions, please feel free to contact us at [dl_hcxopensource@navercorp.com](mailto:dl_hcxopensource@navercorp.com).
