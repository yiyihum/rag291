---
license: apache-2.0
tags:
- finetuned
- chat
language:
- en
- ko
- ja
pipeline_tag: text-generation
library_name: transformers
extra_gated_prompt: '**TRILLION LABS AI MODEL LICENSE AGREEMENT** Tri- Model Series
  Version Effective Date: February 1, 2025

  "**Agreement**" means the terms and conditions for use, reproduction, distribution
  and modification of the Trillion Labs AI Model series set forth herein.

  "**Documentation**" means the specifications, manuals and documentation accompanying
  the Tri- Model series distributed by Trillion Labs.

  "**Licensee**" or "**you**" means you, or your employer or any other person or entity
  (if you are entering into this Agreement on such person or entity''s behalf), of
  the age required under applicable laws, rules or regulations to provide legal consent
  and that has legal authority to bind your employer or such other person or entity
  if you are entering in this Agreement on their behalf.

  "**Model**" means the artificial intelligence model series provided by Licensor
  ("Tri-" series), including software, algorithms, machine learning models, and related
  components provided by Licensor, including all updates, enhancements, improvements,
  bug fixes, patches, or other modifications.

  "**Trillion Labs**" or "**we**" means Trillion Labs, the owner, developer, and provider
  of the Model, holding all rights, title, and interest in the Model.

  By clicking "I Accept" below or by using or distributing any portion or element
  of the Model, you agree to be bound by this Agreement.

  1\. **License Grant and Redistribution**.

  a. Grant of Rights. You are granted a limited, non-exclusive, non-transferable,
  worldwide, revocable license under Trillion Labs'' intellectual property or other
  rights to use, reproduce, distribute, and make modifications to the Model for research
  purposes.

  b. Redistribution and Use.

  i. If you distribute or make available the Model (or any derivative works thereof),
  or a product or service that contains any of them, you shall (A) provide a copy
  of this Agreement with any such Model; and (B) prominently display "Built with Tri-"
  on a related website, user interface, blogpost, about page, or product documentation.
  If you use the Model to create, train, fine tune, or otherwise improve an AI model,
  which is distributed or made available, you shall also include "Tri-" followed by
  the original Model version at the beginning of any such AI model name.

  ii. You must retain in all copies of the Model that you distribute the following
  attribution notice within a "Notice" text file distributed as a part of such copies:
  "Tri- Model Series is licensed under the Trillion Labs AI Model License Agreement,
  Copyright © Trillion Labs. All Rights Reserved."

  iii. Your use of the Model must comply with applicable laws and regulations (including
  trade compliance laws and regulations).

  2\. **Additional Commercial Terms**. If the monthly active users of the products
  or services made available by or for Licensee, or Licensee''s affiliates, is greater
  than 1 million monthly active users OR Annual Recurring Revenue is greater than
  $10 million USD, you must request a commercial license from Trillion Labs, and you
  are not authorized to exercise any commercial rights under this Agreement unless
  or until Trillion Labs otherwise expressly grants you such rights.

  3\. **Disclaimer of Warranty**. THE MODEL, DERIVATIVES, AND OUTPUT ARE PROVIDED
  ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, AND TRILLION LABS DISCLAIMS
  ALL WARRANTIES OF ANY KIND, BOTH EXPRESS AND IMPLIED, INCLUDING, WITHOUT LIMITATION,
  ANY WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR
  PURPOSE.

  4\. **Limitation of Liability**. IN NO EVENT WILL TRILLION LABS BE LIABLE UNDER
  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, TORT, NEGLIGENCE, PRODUCTS LIABILITY,
  OR OTHERWISE, ARISING OUT OF THIS AGREEMENT, FOR ANY LOST PROFITS OR ANY INDIRECT,
  SPECIAL, CONSEQUENTIAL, INCIDENTAL, EXEMPLARY OR PUNITIVE DAMAGES.

  5\. **Intellectual Property**.

  a. No trademark licenses are granted under this Agreement, and in connection with
  the Model, neither Trillion Labs nor Licensee may use any name or mark owned by
  or associated with the other or any of its affiliates, except as required for reasonable
  and customary use in describing and redistributing the Model or as set forth in
  this Section 5(a).

  b. All rights, title, and interest in the Model, including modifications, Derivatives,
  and documentation, remain exclusively with Trillion Labs.

  6\. **Term and Termination**. The term of this Agreement will commence upon your
  acceptance of this Agreement or access to the Model and will continue in full force
  and effect until terminated in accordance with the terms and conditions herein.
  Trillion Labs may terminate this Agreement if you are in breach of any term or condition
  of this Agreement. Upon termination of this Agreement, you shall delete and cease
  use of the Model. Sections 3, 4 and 5 shall survive the termination of this Agreement.

  7\. **Governing Law and Jurisdiction**. This Agreement will be governed and construed
  under the laws of the State of California without regard to choice of law principles.
  The courts of California shall have exclusive jurisdiction of any dispute arising
  out of this Agreement.'
extra_gated_fields:
  First Name: text
  Last Name: text
  Date of birth: date_picker
  Country: country
  Affiliation: text
  Job title:
    type: select
    options:
    - Student
    - Research Graduate
    - AI researcher
    - AI developer/engineer
    - Reporter
    - Other
  geo: ip_location
  ? By clicking Submit below I accept the terms of the license and acknowledge that
    the information I provide will be collected stored processed and shared in accordance
    with the Trillion Labs Privacy Policy
  : checkbox
extra_gated_description: The information you provide will be collected, stored, processed
  and shared in accordance with the Trillion Labs Privacy Policy.
extra_gated_button_content: Submit
extra_gated_heading: Please be sure to provide your full legal name, date of birth,
  and full organization name with all corporate identifiers. Avoid the use of acronyms
  and special characters. Failure to follow these instructions may prevent you from
  accessing this model and others on Hugging Face. You will not have the ability to
  edit this form after submission, so please ensure all information is accurate.
---


# Tri-70B-preview-SFT

## Introduction

We introduce **Tri-70B-preview-SFT**, a research preview of our latest and largest flagship language model that redefines the efficiency frontier in LLM training. By achieving frontier performance for it's compute size (1.5T training tokens from scratch), we demonstrate that exceptional capabilities don't require excessive computational resources.

We are releasing a **minimally post-trained version** to enable open research and community experimentation. This preview version has only undergone supervised fine-tuning and has not been subjected to extensive RLHF. This enables researchers to explore various RL-based alignment techniques with this model. Stay tuned for the base model release coming soon!

### Key Highlights

- **Architecture optimized for long context**
  - 32k context window
  - Sliding window attention with window size 4096
  - iRoPE: Interleaved local (RoPE) and global (temperature-scaled) attention
  - Scalable softmax
- **Multi-lingual capabilities**: Specially optimized for English, Korean, and Japanese
- **Enhanced reasoning**: Modified training dataset mixture specifically designed for reasoning capabilities, with emphasis on step-by-step problem solving
- **Minimal post-training**: This preview release features only supervised fine-tuning, enabling researchers to explore custom alignment techniques and RLHF/RLVR approaches

### Model Specifications

#### Tri-70B-preview-SFT

| Specification | Value |
|--------------|-------|
| Type | Causal Language Model |
| Training Stage | Pre-training & Supervised Fine-Tuning |
| Architecture | Transformer Decoder with iRoPE (global attention frequency of 4), SwiGLU, RMSNorm, and GQA |
| Number of Parameters | 70B |
| Number of Layers | 80 |
| Number of Attention Heads | 64 (Query) / 8 (Key, Value) |
| Context Length | 32,768 |
| Number of Tokens Seen | 1.5T |
| Vocab Size | 124,416 |

## Quickstart

Here is a code snippet with `apply_chat_template` that demonstrates how to load the tokenizer and model and generate text:

### Tri-70B-SFT Usage
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "trillionlabs/Tri-70B-preview-SFT"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

prompt = "Explain the concept of central limit theorem in simple terms."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
```

### vLLM Deployment
We are working with vLLM team on native vLLM support of our Trillion model. In the meantime, we offer an off-the-tree integration method ([link](https://huggingface.co/trillionlabs/Tri-70B-preview-SFT)).

```bash
# install off-the-tree model integration plugin
git clone https://github.com/trillion-labs/trillion-deployment-utils.git
cd trillion-deployment-utils && pip install -e .

vllm serve trillionlabs/Tri-70B-preview-SFT --trust-remote-code
```

The plugin has been tested on vLLM version 0.10.1.1. Check out the repository for detailed usages.

## Evaluation

We evaluated Tri-70B-preview-SFT across a suite of benchmarks assessing general reasoning, knowledge recall, coding abilities, mathematical reasoning, and instruction-following capabilities. We compare our model against state-of-the-art models of similar scale: Qwen-2.5-72B-instruct and Llama-3.1-70B.

<details>
<summary> Full evaluation settings </summary>

# Benchmark Evaluation Settings

| Benchmark | Language | Evaluation Setting | Metric |
|:----------|:---------|:------------------|:-------|
| • HAERAE | Korean | 3-shot | accuracy |
| • KMMLU | Korean | 0-shot, CoT | accuracy (exact-match) |
| • MMLU | English | 0-shot, CoT | accuracy (exact-match) |
| • MMLU-Pro | English | 0-shot, CoT | exact-match |
| • HumanEval | English | 0-shot | pass@1 |
| • MBPPPlus | English | 0-shot | pass@1 |
| • GSM8k | English | 0-shot, CoT | exact-match |
| • MATH | English | 0-shot, CoT | exact-match |
| • GPQA Diamond | English | 0-shot, CoT | accuracy |
| • HRM8k | Korean | 0-shot, CoT | exact-match |
| • MT-Bench | English | LLM-as-a-judge (gpt-4o) | LLM score |

**Note that MT-Bench uses a 10-point scale.

</details>

### Benchmark Results

Models compared:

- **Tri-70B-preview-SFT**: Our flagship 70B parameter model
- **Qwen-2.5-72B-instruct**: Qwen's 72B parameter instruction-tuned model
- **Llama-3.1-70B**: Meta's instruction-tuned 70B model


| Benchmark | Tri-70B-SFT | Qwen-2.5-72B-instruct | Llama-3.1-70B |
| --- | --- | --- | --- |
| HAERAE | 83.96 | 75.44 | 78.09 | 
| KMMLU | 62.38 | 65.07 | 54.62 | 
| MMLU | 74.42 | 87.29 | 85.47 | 
| MMLU-Pro | 62.48 | 69.40 | 62.79 | 
| HumanEval | - | 89.02 | 82.93 | 
| MBPPPlus | 68.52 | 88.2 | 84.13 | 
| GSM8k | 87.37 | 91.51 | 72.48 | 
| MATH | 64.40 | 80.80 | 62.40 | 
| GPQA-Diamond | - | 54.04 | 44.44 | 
| HRM8k | 82.26 | 66.24 | 63.90 | 
| MT-Bench | 7.54 | 8.71 | 8.2 | 

## Limitations

- **Language Support**: The model is optimized for English, Korean, and Japanese. Usage with other languages may result in degraded performance.
- **Knowledge Cutoff**: The model's knowledge is limited to information available up to February 2025.
- **Minimal Post-Training**: As this is a supervised fine-tuning (SFT) release without RLHF, responses may occasionally lack the polish and safety alignment of fully post-trained models.

## License
This model repository is licensed under the Trillion License.
    
## Contact
For inquiries, please contact: info@trillionlabs.co