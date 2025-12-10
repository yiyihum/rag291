---
license: other
license_name: openpangu-model-license-agreement-version-1.0
license_link: https://ai.gitcode.com/ascend-tribe/openpangu-embedded-7b-model/blob/main/LICENSE
language:
- zh
- en
pipeline_tag: text-generation
tags:
- Dense
---

English | [中文](README_ZH.md)

## 1. Model Overview

The openPangu-Embedded-7B is an efficient large language model trained from scratch based on the Ascend NPU. It contains 7 billion parameters (excluding the vocabulary embedding layer). The model has been trained on approximately 19T tokens and is capable of integrating both fast and slow thinking.

## 2. Model Architecture

|                               |   openPangu-Embedded-7B   |
| :---------------------------: | :----------------: |
|       **Architecture**        |       Dense        |
|     **Parameters (Non-Embedding)**     |         7B         |
|     **Number of Layers**      |         34         |
|     **Hidden Dimension**      |       12800        |
|    **Attention Mechanism**    |     GQA      |
| **Number of Attention Heads** | 32 for Q，8 for KV |
|      **Vocabulary Size**      |        153k        |
|      **Context Length (Natively)**       |        32k         |
|    **Pretraining Tokens**     |        19T         |

## 3. Benchmark

| Benchmark | Metric |Slow-thinking |
| :---: | :---: | :---: |
| **General** |  |  |
| MMLU-Pro |  Exact Match | 76.32 |
| CMMLU  |         Acc   | 75.59 |
| ArenaHard_v0.1    |   w/o style control  | 85.80 |
| C-Eval  |         Acc   | 83.05 | 
| GPQA-Diamond	| Avg@4	| 70.54 |
| **Math** |  |  |
| MATH-500 | Avg@1 | 95.00 |
| AIME24 | Avg@16 | 71.57 |
| AIME25 | Avg@16 | 58.24 |
| **Coding** |  |  |
| LiveCodeBench |  Avg@2 (08/24~01/25) | 54.04 |
| MBPP+ |      Avg@2     | 76.06 |

**Note:** The system prompt is left empty, and no additional Chain-of-Thought (CoT) prompts are introduced during the evaluation. All evaluations are performed using a sequence length of 128k tokens.

## 4. Usage

### 4.1 Environment Setup

```bash
# Download model
git lfs install
git clone https://huggingface.co/FreedomIntelligence/openPangu-Embedded-7B

# Install dependencies
cd openPangu-Embedded-7B
conda env create -f environment.yml
conda activate pangu
```

### 4.2 Integrity Check

Please refer to the following methods to verify the integrity of the downloaded content. The hash values are stored in the `checklist.chk` file.

```bash
#!/usr/bin/env bash
ARCH=$(uname -m)
MODEL_PATH="${TARGET_FOLDER}/${MODEL_FOLDER_PATH}"
cd "$MODEL_PATH" || exit 1
if [ "$ARCH" = "arm64" ]; then
    sha256sum checklist.chk
else
    sha256sum -c checklist.chk
fi
```

### 4.3 Inference with Transformers

```python
# coding=utf-8
# Copyright (c) 2025 Huawei Technologies Co., Ltd. All rights reserved.

from transformers import AutoModelForCausalLM, AutoTokenizer

model_local_path = "FreedomIntelligence/openPangu-Embedded-7B"


# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(
    model_local_path, 
    use_fast=False, 
    trust_remote_code=True,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_local_path,
    trust_remote_code=True,
    torch_dtype="auto",
    device_map="auto",
    local_files_only=True
)

# prepare the model input
sys_prompt = "You must strictly comply with laws, regulations, and social ethics." \
    "When generating content, avoid involving violence, pornography, terrorism, racial discrimination, gender discrimination, or other inappropriate content." \
    "If such tendencies are detected in the input or output, refuse to answer and issue a warning. For example, if the input contains violent threats or pornographic descriptions," \
    "return an error message: 'Your input contains inappropriate content and cannot be processed.'"

prompt = "Give me a short introduction to large language model."
no_thinking_prompt = prompt+" /no_think"
messages = [
    {"role": "system", "content": sys_prompt}, # define your system prompt here
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
outputs = model.generate(**model_inputs, max_new_tokens=32768, eos_token_id=45892, return_dict_in_generate=True)

input_length = model_inputs.input_ids.shape[1]
generated_tokens = outputs.sequences[:, input_length:]
output_sent = tokenizer.decode(generated_tokens[0])

# parsing thinking content
thinking_content = output_sent.split("[unused17]")[0].split("[unused16]")[-1].strip()
content = output_sent.split("[unused17]")[-1].split("[unused10]")[0].strip()

print("\nthinking content:", thinking_content)
print("\ncontent:", content)
```

The openPangu-Embedded-7B model is in slow thinking mode by default, and can be switched to fast thinking mode by the following means:
- In the code example, the definition of the `no_thinking_prompt` variable demonstrates the specific implementation for switching to fast thinking mode: by appending the `/no_think` tag at the end of user input, the current turn can be switched to fast thinking mode. In this mode, `thinking_content` will be an empty value.

### 4.4 Inference with vLLM

Start vLLM service:
```bash
CUDA_VISIBLE_DEVICES=0 vllm serve FreedomIntelligence/openPangu-Embedded-7B --port 8818 --trust_remote_code --served-model-name openPangu-Embedded-7B

# or
CUDA_VISIBLE_DEVICES=0 \
python -m vllm.entrypoints.openai.api_server \
  --model FreedomIntelligence/openPangu-Embedded-1B \
  --served-model-name openPangu-Embedded-7B \
  --trust_remote_code \
  --port 8818
```

Send requests to API service:
```bash
curl http://localhost:8818/v1/chat/completions -H "Content-Type: application/json" -d '{
    "model": "openPangu-Embedded-7B",
    "messages": [
        {"role": "user", "content": "Give me a short introduction to large language models."}
    ],
    "temperature": 0.6,
    "top_p": 0.95,
    "top_k": 20,
    "max_tokens": 8192
    }'
```

## 5. Model License

Unless otherwise noted, openPangu-Embedded-7B model is licensed under the terms and conditions of **OPENPANGU MODEL LICENSE AGREEMENT VERSION 1.0**, which is intended to be used permissively and enable the further development of artificial intelligence technologies. Please refer to the LICENSE file located in the root directory of the model repository for details.

## 6. Disclaimer

Due to the technical limitations inherent in the technology on which the openPangu-Embedded-7B (“Model”) relies and the fact that the artificial intelligence generated content is automatically produced by Model, Huawei cannot make any guarantees regarding the following matters:
- The output of this Model is automatically generated via AI algorithms, it does not rule out the possibility that some of the information may be flawed, unreasonable, or cause discomfort, and the generated content does not represent Huawei's attitude or standpoint;
- There is no guarantee that this Model is 100% accurate, reliable, functional, timely, secure and safety, error-free, uninterrupted, continuously stable, or free of any faults;
- The output of this Model does not constitute any advices or decisions for you, and it does not guarantee the authenticity, completeness, accuracy, timeliness, legality, functionality, or practicality of the generated content. The generated content cannot replace professionals in medical, legal, and other fields in answering your questions. The generated content is for your reference only and does not represent any attitude, standpoint, or position of Huawei. You need to make independent judgments based on your actual situation, and Huawei does not assume any responsibilities.

For feedback and suggestions, please submit an issue or contact us (openPangu@huawei.com).