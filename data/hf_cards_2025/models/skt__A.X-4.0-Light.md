---
license: apache-2.0
license_link: https://huggingface.co/skt/A.X-4.0-Light/blob/main/LICENSE
language:
- en
- ko
pipeline_tag: text-generation
library_name: transformers
model_id: skt/A.X-4.0-Light
developers: SKT AI Model Lab
model-index:
- name: A.X-4.0-Light
  results:
  - task:
      type: generate_until
      name: mmlu
    dataset:
      name: mmlu (chat CoT)
      type: hails/mmlu_no_train
    metrics:
    - type: exact_match
      value: 75.43
      name: exact_match
  - task:
      type: generate_until
      name: kmmlu
    dataset:
      name: kmmlu (chat CoT)
      type: HAERAE-HUB/KMMLU
    metrics:
    - type: exact_match
      value: 64.15
      name: exact_match
---

# A.X 4.0 Light

<p align="center">
    <picture>
        <img src="./assets/A.X_logo_ko_4x3.png" width="45%" style="margin: 40px auto;">
    </picture>
</p>
<p align="center"> <a href="https://huggingface.co/collections/skt/ax-4-68637ebaa63b9cc51925e886">🤗 Models</a>   |   <a href="https://sktax.chat/chat">💬 Chat</a>   |    <a href="https://github.com/SKT-AI/A.X-4.0/blob/main/apis/README.md">📬 APIs (FREE!)</a>    |   <a href="https://github.com/SKT-AI/A.X-4.0">🖥️ Github</a> </p>

## A.X 4.0 Family Highlights

SK Telecom released **A.X 4.0** (pronounced "A dot X"), a large language model (LLM) optimized for Korean-language understanding and enterprise deployment, on July 03, 2025. Built on the open-source [Qwen2.5](https://huggingface.co/collections/Qwen/qwen25-66e81a666513e518adb90d9e) model, A.X 4.0 has been further trained with large-scale Korean datasets to deliver outstanding performance in real-world business environments.

- **Superior Korean Proficiency**: Achieved a score of 78.3 on [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU), the leading benchmark for Korean-language evaluation and a Korean-specific adaptation of MMLU, outperforming GPT-4o (72.5).
- **Deep Cultural Understanding**: Scored 83.5 on [CLIcK](https://huggingface.co/datasets/EunsuKim/CLIcK), a benchmark for Korean cultural and contextual comprehension, surpassing GPT-4o (80.2).
- **Efficient Token Usage**: A.X 4.0 uses approximately 33% fewer tokens than GPT-4o for the same Korean input, enabling more cost-effective and efficient processing.
- **Deployment Flexibility**: Offered in both a 72B-parameter standard model (A.X 4.0) and a 7B lightweight version (A.X 4.0 Light).
- **Long Context Handling**: Supports up to 131,072 tokens, allowing comprehension of lengthy documents and conversations. (Lightweight model supports up to 16,384 tokens length)

## Performance

### Model Performance

<table><thead>
  <tr>
    <th colspan="2">Benchmarks</th>
    <th>A.X 4.0</th>
    <th>Qwen3-235B-A22B<br/>(w/o reasoning)</th>
    <th>Qwen2.5-72B</th>
    <th>GPT-4o</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="6">Knowledge</td>
    <td>KMMLU</td>
    <td>78.32</td>
    <td>73.64</td>
    <td>66.44</td>
    <td>72.51</td>
  </tr>
  <tr>
    <td>KMMLU-pro</td>
    <td>72.43</td>
    <td>64.4</td>
    <td>56.27</td>
    <td>66.97</td>
  </tr>
  <tr>
    <td>KMMLU-redux</td>
    <td>74.18</td>
    <td>71.17</td>
    <td>58.76</td>
    <td>69.08</td>
  </tr>
  <tr>
    <td>CLIcK</td>
    <td>83.51</td>
    <td>74.55</td>
    <td>72.59</td>
    <td>80.22</td>
  </tr>
  <tr>
    <td>KoBALT</td>
    <td>47.30</td>
    <td>41.57</td>
    <td>37.00</td>
    <td>44.00</td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td>86.62</td>
    <td>87.37</td>
    <td>85.70</td>
    <td>88.70</td>
  </tr>
  <tr>
    <td rowspan="3">General</td>
    <td>Ko-MT-Bench</td>
    <td>86.69</td>
    <td>88.00</td>
    <td>82.69</td>
    <td>88.44</td>
  </tr>
  <tr>
    <td>MT-Bench</td>
    <td>83.25</td>
    <td>86.56</td>
    <td>93.50</td>
    <td>88.19</td>
  </tr>
  <tr>
    <td>LiveBench<sup>2024.11</sup></td>
    <td>52.30</td>
    <td>64.50</td>
    <td>54.20</td>
    <td>52.19</td>
  </tr>
  <tr>
    <td rowspan="2">Instruction Following</td>
    <td>Ko-IFEval</td>
    <td>77.96</td>
    <td>77.53</td>
    <td>77.07</td>
    <td>75.38</td>
  </tr>
  <tr>
    <td>IFEval</td>
    <td>86.05</td>
    <td>85.77</td>
    <td>86.54</td>
    <td>83.86</td>
  </tr>
  <tr>
    <td rowspan="2">Math</td>
    <td>HRM8K</td>
    <td>48.55</td>
    <td>54.52</td>
    <td>46.37</td>
    <td>43.27</td>
  </tr>
  <tr>
    <td>MATH</td>
    <td>74.28</td>
    <td>72.72</td>
    <td>77.00</td>
    <td>72.38</td>
  </tr>
  <tr>
    <td rowspan="3">Code</td>
    <td>HumanEval+</td>
    <td>79.27</td>
    <td>79.27</td>
    <td>81.71</td>
    <td>86.00</td>
  </tr>
  <tr>
    <td>MBPP+</td>
    <td>73.28</td>
    <td>70.11</td>
    <td>75.66</td>
    <td>75.10</td>
  </tr>
  <tr>
    <td>LiveCodeBench<sup>2024.10~2025.04</sup></td>
    <td>26.07</td>
    <td>33.09</td>
    <td>27.58</td>
    <td>29.30</td>
  </tr>
  <tr>
    <td>Long Context</td>
    <td>LongBench<sup>&lt;128K</sup></td>
    <td>56.70</td>
    <td>49.40</td>
    <td>45.60</td>
    <td>47.50</td>
  </tr>
  <tr>
    <td>Tool-use</td>
    <td>FunctionChatBench</td>
    <td>85.96</td>
    <td>82.43</td>
    <td>88.30</td>
    <td>95.70</td>
  </tr>
</tbody></table>

### Lightweight Model Performance

<table><thead>
  <tr>
    <th colspan="2">Benchmarks</th>
    <th>A.X 4.0 Light</th>
    <th>Qwen3-8B<br/>(w/o reasoning)</th>
    <th>Qwen2.5-7B</th>
    <th>EXAONE-3.5-7.8B</th>
    <th>Kanana-1.5-8B</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="6">Knowledge</td>
    <td>KMMLU</td>
    <td>64.15</td>
    <td>63.53</td>
    <td>49.56</td>
    <td>53.76</td>
    <td>48.28</td>
  </tr>
  <tr>
    <td>KMMLU-pro</td>
    <td>50.28</td>
    <td>50.71</td>
    <td>38.87</td>
    <td>40.11</td>
    <td>37.63</td>
  </tr>
  <tr>
    <td>KMMLU-redux</td>
    <td>56.05</td>
    <td>55.74</td>
    <td>38.58</td>
    <td>42.21</td>
    <td>35.33</td>
  </tr>
  <tr>
    <td>CLIcK</td>
    <td>68.05</td>
    <td>62.71</td>
    <td>60.56</td>
    <td>64.30</td>
    <td>61.30</td>
  </tr>
  <tr>
    <td>KoBALT</td>
    <td>30.29</td>
    <td>26.57</td>
    <td>21.57</td>
    <td>21.71</td>
    <td>23.14</td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td>75.43</td>
    <td>82.89</td>
    <td>75.40</td>
    <td>72.20</td>
    <td>68.82</td>
  </tr>
  <tr>
    <td rowspan="3">General</td>
    <td>Ko-MT-Bench</td>
    <td>79.50</td>
    <td>64.06</td>
    <td>61.31</td>
    <td>81.06</td>
    <td>76.30</td>
  </tr>
  <tr>
    <td>MT-Bench</td>
    <td>81.56</td>
    <td>65.69</td>
    <td>79.37</td>
    <td>83.50</td>
    <td>77.60</td>
  </tr>
  <tr>
    <td>LiveBench</td>
    <td>37.10</td>
    <td>50.20</td>
    <td>37.00</td>
    <td>40.20</td>
    <td>29.40</td>
  </tr>
  <tr>
    <td rowspan="2">Instruction Following</td>
    <td>Ko-IFEval</td>
    <td>72.99</td>
    <td>73.39</td>
    <td>60.73</td>
    <td>65.01</td>
    <td>69.96</td>
  </tr>
  <tr>
    <td>IFEval</td>
    <td>84.68</td>
    <td>85.38</td>
    <td>76.73</td>
    <td>82.61</td>
    <td>80.11</td>
  </tr>
  <tr>
    <td rowspan="2">Math</td>
    <td>HRM8K</td>
    <td>40.12</td>
    <td>52.50</td>
    <td>35.13</td>
    <td>31.88</td>
    <td>30.87</td>
  </tr>
  <tr>
    <td>MATH</td>
    <td>68.88</td>
    <td>71.48</td>
    <td>65.58</td>
    <td>63.20</td>
    <td>59.28</td>
  </tr>
  <tr>
    <td rowspan="3">Code</td>
    <td>HumanEval+</td>
    <td>75.61</td>
    <td>77.44</td>
    <td>74.39</td>
    <td>76.83</td>
    <td>76.83</td>
  </tr>
  <tr>
    <td>MBPP+</td>
    <td>67.20</td>
    <td>62.17</td>
    <td>68.50</td>
    <td>64.29</td>
    <td>67.99</td>
  </tr>
  <tr>
    <td>LiveCodeBench</td>
    <td>18.03</td>
    <td>23.93</td>
    <td>16.62</td>
    <td>17.98</td>
    <td>16.52</td>
  </tr>
</tbody></table>

## 🚀 Quickstart

### with HuggingFace Transformers

- `transformers>=4.46.0` or the latest version is required to use `skt/A.X-4.0-Light`
```bash
pip install transformers>=4.46.0
```

#### Example Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "skt/A.X-4.0-Light"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role": "system", "content": "당신은 사용자가 제공하는 영어 문장들을 한국어로 번역하는 AI 전문가입니다."},
    {"role": "user", "content": "The first human went into space and orbited the Earth on April 12, 1961."},
]
input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(
        input_ids,
        max_new_tokens=128,
        do_sample=False,
    )

len_input_prompt = len(input_ids[0])
response = tokenizer.decode(output[0][len_input_prompt:], skip_special_tokens=True)
print(response)
# Output:
# 1961년 4월 12일, 최초의 인간이 우주로 나가 지구를 공전했습니다.
```

### with vLLM

- `vllm>=v0.6.4.post1` or the latest version is required to use tool-use function
```bash
pip install vllm>=v0.6.4.post1
# if you don't want to activate tool-use function, just commenting out below vLLM option
VLLM_OPTION="--enable-auto-tool-choice --tool-call-parser hermes"
vllm serve skt/A.X-4.0-Light $VLLM_OPTION
```

#### Example Usage 
  
```python
from openai import OpenAI

def call(messages, model):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    print(completion.choices[0].message)

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="api_key"
)
model = "skt/A.X-4.0-Light"
messages = [{"role": "user", "content": "에어컨 여름철 적정 온도는? 한줄로 답변해줘"}]
call(messages, model)
# Output:
# ChatCompletionMessage(content='여름철 적정 에어컨 온도는 일반적으로 24-26도입니다.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], reasoning_content=None)

messages = [{"role": "user", "content": "What is the appropriate temperature for air conditioning in summer? Response in a single sentence."}]
call(messages, model)
# Output:
# ChatCompletionMessage(content='The appropriate temperature for air conditioning in summer generally ranges from 72°F to 78°F (22°C to 26°C) for comfort and energy efficiency.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], reasoning_content=None)
```

#### Examples for tool-use
```python
from openai import OpenAI


def call(messages, model):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )
    print(completion.choices[0].message)


client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="api_key"
)
model = "skt/A.X-4.0-Light"

calculate_discount = {
    "type": "function",
    "function": {
        "name": "calculate_discount",
        "description": "원가격과 할인율(퍼센트 단위)을 입력받아 할인된 가격을계산한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "original_price": {
                    "type": "number",
                    "description": "상품의 원래 가격"
                },
                "discount_percentage": {
                    "type": "number",
                    "description": "적용할 할인율(예: 20% 할인의 경우 20을 입력)"
                }
            },
            "required": ["original_price", "discount_percentage"]
        }
    }
}
get_exchange_rate = {
    "type": "function",
    "function": {
        "name": "get_exchange_rate",
        "description": "두 통화 간의 환율을 가져온다.",
        "parameters": {
            "type": "object",
            "properties": {
                "base_currency": {
                    "type": "string",
                    "description": "The currency to convert from."
                },
                "target_currency": {
                    "type": "string",
                    "description": "The currency to convert to."
                }
            },
            "required": ["base_currency", "target_currency"]
        }
    }
}
tools = [calculate_discount, get_exchange_rate]

### Slot filling ###
messages = [{"role": "user", "content": "우리가 뭘 사야되는데 원래 57600원인데 직원할인 받을 수 있거든? 할인가좀 계산해줘"}]
call(messages, model)
# Output:
# ChatCompletionMessage(content='할인율을 알려주시겠습니까?', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], reasoning_content=None)


### Function calling ###
messages = [
    {"role": "user", "content": "우리가 뭘 사야되는데 원래 57600원인데 직원할인 받을 수 있거든? 할인가좀 계산해줘"},
    {"role": "assistant", "content": "할인율을 알려주시겠습니까?"},
    {"role": "user", "content": "15% 할인 받을 수 있어."},
]
call(messages, model)
# Output: 
# ChatCompletionMessage(content=None, refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='chatcmpl-tool-7778d1d9fca94bf2acbb44c79359502c', function=Function(arguments='{"original_price": 57600, "discount_percentage": 15}', name='calculate_discount'), type='function')], reasoning_content=None)


### Completion ###
messages = [
    {"role": "user", "content": "우리가 뭘 사야되는데 원래 57600원인데 직원할인 받을 수 있거든? 할인가좀 계산해줘"},
    {"role": "assistant", "content": "할인율을 알려주시겠습니까?"},
    {"role": "user", "content": "15% 할인 받을 수 있어."},
    {"role": "tool", "tool_call_id": "random_id", "name": "calculate_discount", "content": "{\"original_price\": 57600, \"discount_percentage\": 15, \"discounted_price\": 48960.0}"}
]
call(messages, model)
# Output: 
# ChatCompletionMessage(content='57600원의 상품에서 15% 할인을 적용하면, 할인된 가격은 48960원입니다.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[], reasoning_content=None)
```

## License

The `A.X 4.0 Light` model is licensed under `Apache License 2.0`.

## Citation
```
@article{SKTAdotX4Light,
  title={A.X 4.0 Light},
  author={SKT AI Model Lab},
  year={2025},
  url={https://huggingface.co/skt/A.X-4.0-Light}
}
```

## Contact

- Business & Partnership Contact: [a.x@sk.com](a.x@sk.com)