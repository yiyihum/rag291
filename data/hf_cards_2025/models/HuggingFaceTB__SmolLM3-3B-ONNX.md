---
library_name: transformers.js
license: apache-2.0
language:
- en
- fr
- es
- it
- pt
- zh
- ar
- ru
base_model:
- HuggingFaceTB/SmolLM3-3B
---


# SmolLM3


![image/png](https://cdn-uploads.huggingface.co/production/uploads/61c141342aac764ce1654e43/zy0dqTCCt5IHmuzwoqtJ9.png)


##  Table of Contents

1. [Model Summary](#model-summary)
2. [How to use](#how-to-use)
3. [Evaluation](#evaluation)
4. [Training](#training)
5. [Limitations](#limitations)
6. [License](#license)

## Model Summary

SmolLM3 is a 3B parameter language model designed to push the boundaries of small models. It supports 6 languages, advanced reasoning and long context. SmolLM3 is a fully open model that offers strong performance at the 3B–4B scale.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6200d0a443eb0913fa2df7cc/db3az7eGzs-Sb-8yUj-ff.png)

The model is a decoder-only transformer using GQA and NoPE (with 3:1 ratio), it was pretrained on 11.2T tokens with a staged curriculum of web, code, math and reasoning data. Post-training included midtraining on 140B reasoning tokens followed by supervised fine-tuning and alignment via Anchored Preference Optimization (APO).

### Key features
- Instruct model optimized for **hybrid reasoning**
- **Fully open model**: open weights + full training details including public data mixture and training configs
- **Long context:** Trained on 64k context and suppots up to **128k tokens** using YARN extrapolation
- **Multilingual**: 6 natively supported (English, French, Spanish, German, Italian, and Portuguese)

For more details refer to our blog post: https://hf.co/blog/smollm3

## How to use

### Transformers.js

```js
import { pipeline, TextStreamer } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "HuggingFaceTB/SmolLM3-3B-ONNX",
  { dtype: "q4f16", device: "webgpu" },
);

// Define the model inputs
const thinking = true; // Whether the model should think before answering
const messages = [
  {
    role: "system",
    content: "You are SmolLM, a language model created by Hugging Face."
      + (thinking ? "/think" : "/no_think")
  },
  { role: "user", content: "Solve the equation x^2 - 3x + 2 = 0" },
];

// Generate a response
const output = await generator(messages, {
  max_new_tokens: 1024,
  streamer: new TextStreamer(generator.tokenizer, { skip_prompt: true, skip_special_tokens: true }),
});
console.log(output[0].generated_text.at(-1).content);
```

### ONNXRuntime

```py
from transformers import AutoConfig, AutoTokenizer
import onnxruntime
import numpy as np
from huggingface_hub import hf_hub_download

# 1. Load config, processor, and model
model_id = "HuggingFaceTB/SmolLM3-3B-ONNX"
config = AutoConfig.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model_path = hf_hub_download(repo_id=model_id, filename="onnx/model_q4.onnx") # Download the graph
hf_hub_download(repo_id=model_id, filename="onnx/model_q4.onnx_data") # Download the model weights
decoder_session = onnxruntime.InferenceSession(model_path)

## Set config values
num_key_value_heads = config.num_key_value_heads
head_dim = config.hidden_size // config.num_attention_heads
num_hidden_layers = config.num_hidden_layers
eos_token_id = config.eos_token_id

# 2. Prepare inputs
messages = [
  { "role": "system", "content": "/no_think" },
  { "role": "user", "content": "What is the capital of France?" },
]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="np")
input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']
batch_size = input_ids.shape[0]
past_key_values = {
    f'past_key_values.{layer}.{kv}': np.zeros([batch_size, num_key_value_heads, 0, head_dim], dtype=np.float32)
    for layer in range(num_hidden_layers)
    for kv in ('key', 'value')
}
position_ids = np.tile(np.arange(0, input_ids.shape[-1]), (batch_size, 1))

# 3. Generation loop
max_new_tokens = 1024
generated_tokens = np.array([[]], dtype=np.int64)
for i in range(max_new_tokens):
  logits, *present_key_values = decoder_session.run(None, dict(
      input_ids=input_ids,
      attention_mask=attention_mask,
      position_ids=position_ids,
      **past_key_values,
  ))

  ## Update values for next generation loop
  input_ids = logits[:, -1].argmax(-1, keepdims=True)
  attention_mask = np.concatenate([attention_mask, np.ones_like(input_ids, dtype=np.int64)], axis=-1)
  position_ids = position_ids[:, -1:] + 1
  for j, key in enumerate(past_key_values):
    past_key_values[key] = present_key_values[j]

  generated_tokens = np.concatenate([generated_tokens, input_ids], axis=-1)
  if (input_ids == eos_token_id).all():
    break

  ## (Optional) Streaming
  print(tokenizer.decode(input_ids[0]), end='', flush=True)
print()

# 4. Output result
print(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0])
```


## Evaluation

In this section, we report the evaluation results of SmolLM3 model. All evaluations are zero-shot unless stated otherwise, and we use [lighteval](https://github.com/huggingface/lighteval) to run them. 

We highlight the best score in bold and underline the second-best score.

### Instruction Model

#### No Extended Thinking
Evaluation results of non reasoning models and reasoning models in no thinking mode. We highlight the best and second-best scores in bold.
| Category | Metric | SmoLLM3-3B | Qwen2.5-3B | Llama3.1-3B | Qwen3-1.7B | Qwen3-4B |
|---------|--------|------------|------------|-------------|------------|----------|
| High school math competition | AIME 2025 | <u>9.3</u> | 2.9 | 0.3 | 8.0 | **17.1** |
| Math problem-solving | GSM-Plus | 72.8 | <u>74.1</u> | 59.2 | 68.3 | **82.1** |
| Competitive programming | LiveCodeBench v4 | <u>15.2</u> | 10.5 | 3.4 | 15.0 | **24.9** |
| Graduate-level reasoning | GPQA Diamond | <u>35.7</u> | 32.2 | 29.4 | 31.8 | **44.4** |
| Instruction following | IFEval | **76.7** | 65.6 | 71.6 | <u>74.0</u> | 68.9 |
| Alignment | MixEval Hard | 26.9 | <u>27.6</u> | 24.9 | 24.3 | **31.6** |
| Tool Calling | BFCL| <u>92.3</u> | - | <u>92.3</u> * | 89.5  | **95.0** |
| Multilingual Q&A | Global MMLU | <u>53.5</u> | 50.54 | 46.8 | 49.5 | **65.1** |

(*): this is a tool calling finetune

#### Extended Thinking
Evaluation results in reasoning mode for SmolLM3 and Qwen3 models: 
| Category | Metric | SmoLLM3-3B | Qwen3-1.7B | Qwen3-4B |
|---------|--------|------------|------------|----------|
| High school math competition | AIME 2025 | <u>36.7</u> | 30.7 | **58.8** |
| Math problem-solving | GSM-Plus | <u>83.4</u> | 79.4 | **88.2** |
| Competitive programming | LiveCodeBench v4 | 30.0 | <u>34.4</u> | **52.9** |
| Graduate-level reasoning | GPQA Diamond | <u>41.7</u> | 39.9 | **55.3** |
| Instruction following | IFEval | 71.2 | <u>74.2</u> | **85.4** |
| Alignment | MixEval Hard | 30.8 | <u>33.9</u> | **38.0** |
| Tool Calling | BFCL | <u>88.8</u> | <u>88.8</u> | **95.5** |
| Multilingual Q&A | Global MMLU | <u>64.1</u> | 62.3 | **73.3** |


### Base Pre-Trained Model

#### English benchmarks
Note: All evaluations are zero-shot unless stated otherwise. For Ruler 64k evaluation, we apply YaRN to the Qwen models with 32k context to extrapolate the context length.

| Category | Metric | SmolLM3-3B | Qwen2.5-3B | Llama3-3.2B | Qwen3-1.7B-Base | Qwen3-4B-Base |
|---------|--------|---------------------|------------|--------------|------------------|---------------|
| Reasoning & Commonsense| HellaSwag | **76.15** | 74.19 |<u>75.52</u> | 60.52 | 74.37 |
| | ARC-CF (Average) | **65.61** | 59.81 | 58.58 | 55.88 | <u>62.11</u> |
| | Winogrande | 58.88 | **61.41** | 58.72 | 57.06 | <u>59.59</u> |
| | CommonsenseQA | <u>55.28</u> | 49.14 | **60.60** | 48.98 | 52.99 |
| Knowledge & Understanding | MMLU-CF (Average) | <u>44.13</u> | 42.93 | 41.32 | 39.11 | **47.65** | 
| | MMLU Pro CF | <u>19.61</u> | 16.66 | 16.42 | 18.04 | **24.92** |
| | MMLU Pro MCF | <u>32.70</u> | 31.32 | 25.07 | 30.39 | **41.07** |
| | PIQA | **78.89** | 78.35 | <u>78.51</u> | 75.35 | 77.58 |
| | OpenBookQA | 40.60 | 40.20 | <u>42.00</u> | 36.40 | **42.40** |
| | BoolQ | **78.99** | 73.61 | <u>75.33</u> | 74.46 | 74.28 | 
| **Math & Code** |  |  |  |  |  |  | 
| Coding & math | HumanEval+ | 30.48 | 34.14| 25.00 | <u>43.29</u>| **54.87** |
| | MBPP+ | 52.91 | 52.11 | 38.88| <u>59.25</u> | **63.75** | 
| | MATH (4-shot) | <u>46.10</u> | 40.10 | 7.44 | 41.64 | **51.20** |
| | GSM8k (5-shot) | 67.63 | <u>70.13</u> | 25.92 | 65.88 | **74.14** | 
| **Long context** |  |  |  |  |  |  | 
| | Ruler 32k | 76.35 | 75.93 | <u>77.58</u> | 70.63 | **83.98** | 
| | Ruler 64k | <u>67.85</u> | 64.90 | **72.93** | 57.18 | 60.29 | 
| | Ruler 128k | 61.03 | <u>62.23</u> | **71.30** | 43.03 | 47.23 | 

#### Multilingual benchmarks


| Category | Metric | SmolLM3 3B Base | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B Base | Qwen3 4B Base |
|---------|--------|---------------------|------------|--------------|------------------|---------------|
| Main supported languages |  |  |  |  |  |  |  |
| French| MLMM Hellaswag | **63.94** | 57.47 | 57.66 | 51.26 | <u>61.00</u> |
| | Belebele | 51.00 | <u>51.55</u> | 49.22 |49.44| **55.00** |
| | Global MMLU (CF) | <u>38.37</u> | 34.22  | 33.71 | 34.94  |**41.80** |
| | Flores-200 (5-shot) | 62.85| 61.38| <u>62.89<u/u> | 58.68 | **65.76** |
| Spanish| MLMM Hellaswag | **65.85** | 58.25 | 59.39 | 52.40 | <u>61.85</u> |
| | Belebele | 47.00 | <u>48.88</u> | 47.00 | 47.56 | **50.33** |
| | Global MMLU (CF) | <u>38.51</u> | 35.84  | 35.60 | 34.79  |**41.22** |
| | Flores-200 (5-shot) | <u>48.25</u>| 50.00| 44.45 | 46.93 | **50.16** |
| German| MLMM Hellaswag | **59.56** | 49.99|  53.19|46.10| <u>56.43</u>|
| | Belebele | <u>48.44</u> | 47.88 | 46.22 | 48.00 | **53.44**|
| | Global MMLU (CF) | <u>35.10</u> | 33.19  | 32.60 | 32.73  |**38.70** |
| | Flores-200 (5-shot) | **56.60**| 50.63| <u>54.95</u> | 52.58 | 50.48 |
| Italian| MLMM Hellaswag | **62.49** | 53.21 | 54.96 | 48.72 | <u>58.76</u> |
| | Belebele | <u>46.44</u> | 44.77 | 43.88 | 44.00 | **48.78** | 44.88 |
| | Global MMLU (CF) | <u>36.99</u> | 33.91  | 32.79 | 35.37  |**39.26** |
| | Flores-200 (5-shot) | <u>52.65<u/>| **54.87**| 48.83 | 48.37 | 49.11 |
| Portuguese| MLMM Hellaswag | **63.22** | 57.38 | 56.84 | 50.73 | <u>59.89</u> |
| | Belebele | 47.67 | **49.22** | 45.00 | 44.00 | 50.00 | <u>49.00</U> |
| | Global MMLU (CF) | <u>36.88</u> | 34.72  | 33.05 | 35.26  |**40.66** |
| | Flores-200 (5-shot) | <u>60.93</u> |57.68| 54.28 | 56.58 | **63.43** |

The model has also been trained on Arabic (standard), Chinese and Russian data, but has seen fewer tokens in these languages compared to the 6 above. We report the performance on these langages for information.
| Category | Metric | SmolLM3 3B Base | Qwen2.5-3B | Llama3.2 3B | Qwen3 1.7B Base | Qwen3 4B Base |
|---------|--------|---------------------|------------|--------------|------------------|---------------|
| Other supported languages |  |  |  |  |  |  |  |
| Arabic| Belebele | 40.22 | 44.22 | <u>45.33</u> | 42.33 | **51.78** |
| | Global MMLU (CF) | 28.57 | 28.81 | 27.67 | <u>29.37</u> | **31.85** |
| | Flores-200 (5-shot) | <u>40.22</u> | 39.44 | **44.43** | 35.82 | 39.76 |
| Chinese| Belebele | 43.78 | 44.56 | <u>49.56</u> | 48.78 | **53.22** |
| | Global MMLU (CF) | 36.16 | 33.79 | <u>39.57</u> | 38.56 | **44.55** |
| | Flores-200 (5-shot) | 29.17 | **33.21** | 31.89 | 25.70 | <u>32.50</u> |
| Russian| Belebele | <u>47.44</u> | 45.89 | <u>47.44</u> | 45.22 | **51.44** |
| | Global MMLU (CF) | <u>36.51</u> | 32.47 | 34.52 | 34.83 | **38.80** |
| | Flores-200 (5-shot) | 47.13 | 48.74 | 50.74 | <u>54.70</u> | **60.53** |

## Training

### Model

- **Architecture:** Transformer decoder
- **Pretraining tokens:** 11T
- **Precision:** bfloat16

### Software & hardware

- **GPUs:** 384 H100
- **Training Framework:** [nanotron](https://github.com/huggingface/nanotron/tree/smollm3)
- **Data processing framework:** [datatrove](https://github.com/huggingface/datatrove)
- **Evaluation framework:** [lighteval](https://github.com/huggingface/lighteval)
- **Post-training Framework:** [TRL](https://github.com/huggingface/trl)

### Open resources
Here is an infographic with all the training details 
- The datasets used for pretraining can be found in this [collection](https://huggingface.co/collections/HuggingFaceTB/smollm3-pretraining-datasets-685a7353fdc01aecde51b1d9) and those used in mid-training and post-training will be uploaded later 
- The training and evaluation configs and code can be found in the [huggingface/smollm](https://github.com/huggingface/smollm) repository.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/651e96991b97c9f33d26bde6/qiE5ZYr9SD1CIAtfEfuC8.png)

## Limitations

SmolLM3 can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.


## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)