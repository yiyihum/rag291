---
license: apache-2.0
license_link: https://huggingface.co/skt/A.X-3.1/blob/main/LICENSE
language:
- en
- ko
pipeline_tag: text-generation
library_name: transformers
model_id: skt/A.X-3.1
developers: SKT AI Model Lab
model-index:
- name: A.X-3.1
  results:
  - task:
      type: generate_until
      name: mmlu
    dataset:
      name: mmlu (chat CoT)
      type: hails/mmlu_no_train
    metrics:
    - type: exact_match
      value: 75.1
      name: exact_match
  - task:
      type: generate_until
      name: kmmlu
    dataset:
      name: kmmlu (chat CoT)
      type: HAERAE-HUB/KMMLU
    metrics:
    - type: exact_match
      value: 69.2
      name: exact_match
---

# A.X 3.1

<div align="center">
  <img src="./assets/A.X_from_scratch_logo_ko_4x3.png" alt="A.X Logo" width="300"/>
</div>
<p align="center"> <a href="https://huggingface.co/collections/skt/ax-3-686b288b3b05e1234f3f4c73">🤗 Models</a>   |   <a href="https://github.com/SKT-AI/A.X-3">🖥️ Github</a> </p>

## A.X 3.1 Highlights

SK Telecom released **A.X 3.1** (pronounced "A dot X"), a large language model (LLM) optimized for Korean-language understanding and enterprise deployment, on July 24, 2025.
This sovereign AI model was developed entirely in-house by SKT, encompassing model architecture, data curation, and training, all carried out on SKT’s proprietary supercomputing infrastructure, TITAN. 
The model was trained from scratch on a high-quality multilingual corpus comprising **2.1 trillion tokens**, with a primary focus on the Korean language. 

- **Authentic Korean Sovereign AI**: A.X 3.1 was trained on a high-quality multilingual dataset—fully curated in-house—using SKT’s proprietary GPU infrastructure.
- **Highly Efficient Multilingual LLM**: A.X 3.1 demonstrates superior performance among Korean LLMs, despite its relatively compact training size of 2.1 trillion tokens.
- **Superior Korean Proficiency**: A.X 3.1 achieved a score of **69.2** on the [KMMLU](https://huggingface.co/datasets/HAERAE-HUB/KMMLU): the leading benchmark for Korean-language evaluation and a Korean-specific adaptation of MMLU, outperforming other Korean-specified models.
- **Deep Korean Understanding**: A.X 3.1 obtained **77.4** on the [CLIcK](https://huggingface.co/datasets/EunsuKim/CLIcK): a benchmark for Korean cultural and contextual comprehension, outperforming other open-source models.
- **Efficient Token Usage**: A.X 3.1 requires approximately 33% fewer tokens than GPT-4o to process equivalent Korean inputs, facilitating more cost-effective and computationally efficient inference.
- **Long-Context Handling**: A.X 3.1 supports up to **32,768 tokens** natively, and up to **131,072 tokens** by applying YaRN.


## Core Technologies

A.X 3.1 represents **an efficient sovereign AI model**, developed end-to-end by SKT, encompassing model architecture, data curation, infrastructure deployment, and optimization.

### Model Architecture Specs

<table><thead>
  <tr>
    <th>Model</th>
    <th># Params</th>
    <th># Layers</th>
    <th># KV-Heads</th>
    <th>Hidden Dim</th>
    <th>FFN Dim</th>
  </tr>
  <tr>
    <th>A.X 3.1</th>
    <th>34B</th>
    <th>48</th>
    <th>8</th>
    <th>8192</th>
    <th>21824</th>
  </tr>
  </thead>
</table>

### High-Quality Data Pipeline & Strategic Mixture

- We collected and curated a training dataset comprising 20 trillion tokens sourced from diverse domains.
- The entire dataset was processed through SKT’s proprietary data pipeline, incorporating synthetic data generation and comprehensive quality filtering.
- For training  A.X 3.1, a total of **2.1 trillion tokens** were utilized, comprising a Korean-focused multilingual corpus.


## Benchmark Results

### Model Performance

<table>
<caption style="text-align:left; caption-side:bottom">* self-reported score</caption>
<thead>
  <tr>
    <th></th>
    <th></th>
    <th>A.X 3.1</th>
    <th>EXAONE-3.5-32B</th>
    <th>Kanana-flag-32.5B</th>
    <th>Gemma-3-27B</th>
    <th>Qwen2.5-32B</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="5">Knowledge</td>
    <td>KMMLU</td>
    <td>69.73</td>
    <td>57.17</td>
    <td>64.19*</td>
    <td>59.45</td>
    <td>61.93</td>
  </tr>
  <tr>
    <td>KMMLU-pro</td>
    <td>54.89</td>
    <td>45.39</td>
    <td>-</td>
    <td>50.43</td>
    <td>52.34</td>
  </tr>
  <tr>
    <td>KMMLU-redux</td>
    <td>62.66</td>
    <td>48.32</td>
    <td>-</td>
    <td>54.85</td>
    <td>52.15</td>
  </tr>
  <tr>
    <td>Click (chat CoT)</td>
    <td>77.09</td>
    <td>69.42</td>
    <td>-</td>
    <td>71.03</td>
    <td>68.17</td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td>75.20</td>
    <td>77.1</td>
    <td>81.08*</td>
    <td>82.35</td>
    <td>83.4</td>
  </tr>
  <tr>
    <td rowspan="2">General</td>
    <td>Ko-MT-bench</td>
    <td>83.06</td>
    <td>80.19</td>
    <td>80.58*</td>
    <td>85.5</td>
    <td>72.88</td>
  </tr>
  <tr>
    <td>MT-bench</td>
    <td>84.19</td>
    <td>85.09</td>
    <td>83.56*</td>
    <td>84.38</td>
    <td>87.31</td>
  </tr>
  <tr>
    <td rowspan="2">IF</td>
    <td>Ko-IFEval</td>
    <td>75.29</td>
    <td>68.67</td>
    <td>-</td>
    <td>74.4</td>
    <td>73.24</td>
  </tr>
  <tr>
    <td>IFEval</td>
    <td>87.11</td>
    <td>82.67</td>
    <td>85.6*</td>
    <td>82.45</td>
    <td>82.27</td>
  </tr>
  <tr>
    <td rowspan="2">Math<br> </td>
    <td>HRM8K</td>
    <td>45.53</td>
    <td>36.3</td>
    <td>-</td>
    <td>48</td>
    <td>41.29</td>
  </tr>
  <tr>
    <td>MATH</td>
    <td>75.40</td>
    <td>61.64</td>
    <td>57.82*</td>
    <td>80.72</td>
    <td>73.26</td>
  </tr>
  <tr>
    <td rowspan="3">Code<br> <br> </td>
    <td>HumanEval+</td>
    <td>75.00</td>
    <td>77.44</td>
    <td>77.44*</td>
    <td>78.66</td>
    <td>82.32</td>
  </tr>
  <tr>
    <td>MBPP+</td>
    <td>70.90</td>
    <td>65.87</td>
    <td>69.84*</td>
    <td>74.07</td>
    <td>73.81</td>
  </tr>
  <tr>
    <td>LiveCodeBench</td>
    <td>23.34</td>
    <td>17.2</td>
    <td>-</td>
    <td>30.55</td>
    <td>26.9</td>
  </tr>
</tbody></table>


### Lightweight Model Performance

<table><thead>
  <tr>
    <th colspan="2">Benchmarks</th>
    <th>A.X 3.1 Light</th>
    <th>Kanana-1.5-8B</th>
    <th>EXAONE-3.5-7.8B</th>
    <th>Qwen2.5-7B</th>
    <th>Qwen3-8B<br>(w/o reasoning)</th>
  </tr></thead>
<tbody>
  <tr>
    <td rowspan="6">Knowledge</td>
    <td>KMMLU</td>
    <td>61.70</td>
    <td>48.28</td>
    <td>53.76</td>
    <td>49.56</td>
    <td>63.53</td>
  </tr>
  <tr>
    <td>KMMLU-pro</td>
    <td>45.54</td>
    <td>37.63</td>
    <td>40.11</td>
    <td>38.87</td>
    <td>50.71</td>
  </tr>
  <tr>
    <td>KMMLU-redux</td>
    <td>52.34</td>
    <td>35.33</td>
    <td>42.21</td>
    <td>38.58</td>
    <td>55.74</td>
  </tr>
  <tr>
    <td>CLIcK</td>
    <td>71.22</td>
    <td>61.30</td>
    <td>64.11</td>
    <td>58.30</td>
    <td>63.31</td>
  </tr>
  <tr>
    <td>KoBALT</td>
    <td>27.43</td>
    <td>23.14</td>
    <td>21.71</td>
    <td>21.57</td>
    <td>26.57</td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td>66.95</td>
    <td>68.82</td>
    <td>72.20</td>
    <td>75.40</td>
    <td>82.89</td>
  </tr>
  <tr>
    <td rowspan="2">General</td>
    <td>Ko-MT-Bench</td>
    <td>78.56</td>
    <td>76.30</td>
    <td>81.06</td>
    <td>61.31</td>
    <td>64.06</td>
  </tr>
  <tr>
    <td>MT-Bench</td>
    <td>74.38</td>
    <td>77.60</td>
    <td>83.50</td>
    <td>79.37</td>
    <td>65.69</td>
  </tr>
  <tr>
    <td rowspan="2">Instruction<br>Following</td>
    <td>Ko-IFEval</td>
    <td>70.04</td>
    <td>69.96</td>
    <td>65.01</td>
    <td>60.73</td>
    <td>73.39</td>
  </tr>
  <tr>
    <td>IFEval</td>
    <td>79.86</td>
    <td>80.11</td>
    <td>82.61</td>
    <td>76.73</td>
    <td>85.38</td>
  </tr>
  <tr>
    <td rowspan="2">Math</td>
    <td>HRM8K</td>
    <td>41.70</td>
    <td>30.87</td>
    <td>31.88</td>
    <td>35.13</td>
    <td>52.50</td>
  </tr>
  <tr>
    <td>MATH</td>
    <td>70.14</td>
    <td>59.28</td>
    <td>63.20</td>
    <td>65.58</td>
    <td>71.48</td>
  </tr>
  <tr>
    <td rowspan="2">Code<br></td>
    <td>HumanEval+</td>
    <td>73.78</td>
    <td>76.83</td>
    <td>76.83</td>
    <td>74.39</td>
    <td>77.44</td>
  </tr>
  <tr>
    <td>MBPP+</td>
    <td>61.64</td>
    <td>67.99</td>
    <td>64.29</td>
    <td>68.50</td>
    <td>62.17</td>
  </tr>
</tbody></table>

## 🚀 Quickstart

### with HuggingFace Transformers

- `transformers>=4.46.0` or the latest version is required to use `skt/A.X-3.1`
```bash
pip install transformers>=4.46.0
```

#### Example Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "skt/A.X-3.1"
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
# 우주에서 인간이 처음으로 지구 궤도를 돈 날은 1961년 4월 12일입니다.
```

### with vLLM

- `vllm>=v0.6.4.post1` or the latest version is required to use tool-use feature
```bash
pip install vllm>=v0.6.4.post1
# if you don't want to activate tool-use feature, just commenting out below vLLM option
VLLM_OPTION="--enable-auto-tool-choice --tool-call-parser hermes"
vllm serve skt/A.X-3.1 $VLLM_OPTION
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
model = "skt/A.X-3.1"
messages = [{"role": "user", "content": "에어컨 여름철 적정 온도는? 한줄로 답변해줘"}]
call(messages, model)
# Output:
# 여름철 에어컨 적정 온도는 24~26도입니다.

messages = [{"role": "user", "content": "What is the appropriate temperature for air conditioning in summer? Respond in a single sentence."}]
call(messages, model)
# Output:
# The appropriate temperature for air conditioning in summer is around 78°F (26°C).
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
model = "skt/A.X-3.1"

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
                    "description": "적용할 할인율"
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
messages = [{"role": "user", "content": "우리가 뭘 사야되는데 원가가 57600원인데 직원할인 받으면 얼마야?"}]
call(messages, model)
# Output:
# ChatCompletionMessage(content='직원 할인율이 몇 퍼센트인지 알려주신다면 할인된 가격을 계산할 수 있습니다. 할인율이 몇 퍼센트인지 알려주실 수 있나요?', role='assistant', tool_calls=[])


### Function calling ###
messages = [
    {"role": "user", "content": "우리가 뭘 사야되는데 원가가 57600원인데 직원할인 받으면 얼마야?"},
    {"role": "assistant", "content": "직원 할인율이 몇 퍼센트인지 알려주신다면 할인된 가격을 계산할 수 있습니다. 할인율이 몇 퍼센트인지 알려주실 수 있나요?"},
    {"role": "user", "content": "15% 할인 받을 수 있어."},
]
call(messages, model)
# Output: 
# ChatCompletionMessage(content=None, role='assistant', tool_calls=[ChatCompletionMessageToolCall(id='chatcmpl-tool-cb9e827f752d4725abc94377223b2b0f', function=Function(arguments='{"original_price": 57600, "discount_percentage": 15}', name='calculate_discount'), type='function')])


### Completion ###
messages = [
    {"role": "user", "content": "우리가 뭘 사야되는데 원가가 57600원인데 직원할인 받으면 얼마야?"},
    {"role": "assistant", "content": "직원 할인율이 몇 퍼센트인지 알려주신다면 할인된 가격을 계산할 수 있습니다. 할인율이 몇 퍼센트인지 알려주실 수 있나요?"},
    {"role": "user", "content": "15% 할인 받을 수 있어."},
    {"role": "tool", "tool_call_id": "random_id", "name": "calculate_discount", "content": "{\"original_price\": 57600, \"discount_percentage\": 15, \"discounted_price\": 48960.0}"}
]
call(messages, model)
# Output: 
# ChatCompletionMessage(content='직원 할인을 받으면 57600원의 상품은 15% 할인을 받아 48960원이 됩니다.', role='assistant', tool_calls=[])
```

### Extend supported token length

The `config.json` file of A.X 3.1 uploaded to HuggingFace is configured for maximum token lengths of 32,768. You can simply handle up to 131,072 tokens by modifying `rope_scaling` field in `config.json` file into the following parameters:

```
"rope_scaling": {
  "type": "yarn",
  "factor": 4.0,
  "original_max_position_embeddings": 32768,
},
```

## License

The `A.X 3.1` model is licensed under `Apache License 2.0`.

## Citation
```
@article{SKTAdotX3.1,
  title={A.X 3.1},
  author={SKT AI Model Lab},
  year={2025},
  url={https://huggingface.co/skt/A.X-3.1}
}
```

## Contact

- Business & Partnership Contact: [a.x@sk.com](a.x@sk.com)