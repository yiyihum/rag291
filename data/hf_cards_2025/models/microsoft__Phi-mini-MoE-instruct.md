---
language:
- en
license: mit
pipeline_tag: text-generation
context_length:
- 4k
library_name: transformers
---

## Model Summary

Phi-mini-MoE is a lightweight Mixture of Experts (MoE) model with 7.6B total parameters and 2.4B activated parameters. It is compressed and distilled from the base model shared by [Phi-3.5-MoE](https://huggingface.co/microsoft/Phi-3.5-MoE-instruct) and [GRIN-MoE](https://huggingface.co/microsoft/GRIN-MoE) using the [SlimMoE](https://arxiv.org/pdf/2506.18349) approach, then post-trained via supervised fine-tuning and direct preference optimization for instruction following and safety. The model is trained on Phi-3 synthetic data and filtered public documents, with a focus on high-quality, reasoning-dense content. It is part of the SlimMoE series, which includes a smaller variant, [Phi-tiny-MoE](https://huggingface.co/microsoft/Phi-tiny-MoE-instruct), with 3.8B total and 1.1B activated parameters.

References: <br>
📖 [SlimMoE](https://arxiv.org/pdf/2506.18349) <br>
📖 [Phi-3 Technical Report](https://arxiv.org/abs/2404.14219) <br>
📖 [GRIN-MoE](https://arxiv.org/abs/2409.12136) <br>

## Intended Uses

### Primary Use Cases

The model is intended for commercial and research use in English. The model provides uses for general purpose AI systems and applications which require memory/compute constrained environments and latency bound scenarios.

### Use Case Considerations

Our models are not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fariness before using within a specific downstream use case, particularly for high risk scenarios. Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.

***Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.*** 

## Usage

### Input Formats
Given the nature of the training data, the Phi-mini-MoE model is best suited for prompts using the chat format as follows:

```
<|system|>
You are a helpful assistant.<|end|>
<|user|>
How to explain Internet for a medieval knight?<|end|>
<|assistant|>
```

### Loading the model locally
After obtaining the Phi-mini-MoE model checkpoints, users can use this sample code for inference.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 

torch.random.manual_seed(0) 

model = AutoModelForCausalLM.from_pretrained( 
    "microsoft/Phi-mini-MoE-instruct",  
    device_map="cuda",  
    torch_dtype="auto",  
    trust_remote_code=True,  
) 

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-mini-MoE-instruct") 

messages = [ 
    {"role": "system", "content": "You are a helpful AI assistant."}, 
    {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"}, 
    {"role": "assistant", "content": "Sure! Here are some ways to eat bananas and dragonfruits together: 1. Banana and dragonfruit smoothie: Blend bananas and dragonfruits together with some milk and honey. 2. Banana and dragonfruit salad: Mix sliced bananas and dragonfruits together with some lemon juice and honey."}, 
    {"role": "user", "content": "What about solving an 2x + 3 = 7 equation?"}, 
] 

pipe = pipeline( 
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
) 

generation_args = { 
    "max_new_tokens": 500, 
    "return_full_text": False, 
    "temperature": 0.0, 
    "do_sample": False, 
} 

output = pipe(messages, **generation_args) 
print(output[0]['generated_text'])
```

## Benchmarks

To understand the capabilities, we compare Phi-mini-MoE with a set of models over a variety of benchmarks using [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). Detailed evaluation settings can be found in the SlimMoE paper.

| Model                 | # Total param | # Act. param | MMLU  | MMLU pro | BBH   | Arc-C (chat) | Human-eval | GSM8K | MT-bench |
|----------------------|---------------|--------------|-------|----------|-------|---------------|-------------|--------|----------|
| **MoE Models** |||||||||||
| Phi-3.5-MoE          | 42B           | 6.6B         | 78.36 | 59.38    | 63.93 | 91.38         | 81.70       | 87.87  | 8.34     |
| Qwen 1.5 MoE         | 14B           | 2.7B         | 60.73 | 26.49    | 42.65 | 67.24         | 46.30       | 53.07  | 6.55     |
| DeepSeek V2 Lite     | 16B           | 2.4B         | 56.69 | 17.89    | 36.30 | 61.09         | 54.40       | 63.23  | 6.82     |
| OL-MoE               | 7B            | 1.3B         | 54.27 | 20.87    | 38.00 | 55.63         | 37.80       | 71.49  | 6.60     |
| Granite 3.0 MoE      | 3.4B          | 0.8B         | 50.06 | 4.82     | 39.65 | 56.06         | 51.80       | 60.12  | 6.91     |
| **Dense Models**     |||||||||||
| LLaMA 3.1 8B         | 8B            | 8B           | 68.71 | 45.28    | 50.86 | 82.42         | 69.50       | 84.84  | 8.03     |
| Qwen 2.5 7B          | 7.6B          | 7.6B         | 73.47 | 56.24    | 53.74 | 88.82         | 81.70       | 84.84  | 8.34     |
| Phi 3 small          | 7.4B          | 7.4B         | 75.35 | 52.06    | 62.07 | 84.30         | 70.10       | 84.84  | 8.03     |
| Gemma 3 4B           | 4B            | 4B           | 59.49 | 40.13    | 49.45 | 75.85         | 67.10       | 78.92  | 8.28     |
| Phi 3 mini           | 3.8B          | 3.8B         | 69.94 | 45.65    | 54.94 | 85.58         | 72.60       | 84.61  | 7.46     |
| LLaMA 3.2 3B         | 3.2B          | 3.2B         | 61.73 | 36.70    | 45.46 | 75.77         | 52.40       | 77.41  | 7.46     |
| Qwen 2.5 3B          | 3B            | 3B           | 65.06 | 41.00    | 46.61 | 80.20         | 73.80       | 76.57  | 7.60     |
| Gemma 3 1B           | 1B            | 1B           | 40.80 | 14.70    | 34.80 | 37.46         | 41.50       | 41.77  | 6.67     |
| LLaMA 3.2 1B         | 1B            | 1B           | 46.30 | 18.67    | 35.18 | 49.91         | 35.40       | 44.96  | 5.23     |
| **SlimMoE Models**       |||||||||||
| Phi-mini-MoE         | 7.6B          | 2.4B         | 70.68 | 49.68    | 55.27 | 84.91         | 73.80       | 84.89  | 7.59     |
| Phi-tiny-MoE         | 3.8B          | 1.1B         | 60.83 | 36.34    | 45.58 | 76.37         | 58.50       | 78.47  | 7.05     |


## Training

### Model

**Architecture:** Phi-mini-MoE has 7.6B total parameters with **2.4B active parameters**. The model is a mixture-of-expert decoder-only Transformer model using the tokenizer with vocabulary size of 32,064.<br>
**Inputs:** Text. It is best suited for prompts using chat format.<br>
**Context length:** 4k tokens<br>
**GPUs:** 64 A100-80G<br>
**Training time:** 11 days<br>
**Training data:** 400B tokens<br>
**Outputs:** Generated text in response to the input<br>
**Dates:** Trained between September 2024 and March 2025<br>
**Status:** This is a static model trained on an offline dataset with cutoff date October 2023 for publicly available data.<br>

### Training Datasets
Our training data is a subset with 400B tokens of Phi-3 datasets, which includes a wide variety of sources and is a combination of 
1) publicly available documents filtered rigorously for quality, selected high-quality educational data, and code;
2) newly created synthetic, “textbook-like” data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.);
3) high quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness. 

More details about data can be found in the [Phi-3 Technical Report](https://arxiv.org/pdf/2404.14219).

## Responsible AI Considerations

Like other language models, Phi-mini-MoE can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:  
* Quality of Service: The models are trained primarily on English text and some additional multilingual text. Languages other than English will experience worse performance as well as performance disparities across non-English. English language varieties with less representation in the training data might experience worse performance than standard American English.
* Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups, cultural contexts, or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.
* Inappropriate or Offensive Content: These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.
* Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
* Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.
* The High ECI: The model has an elevated defect rate when responding to election-critical queries, which may result in incorrect or unauthoritative election critical information being presented. Users should verify information related to elections with the election authority in their region.
* Long Conversation: Phi-3 models, like other models, can in some cases generate responses that are repetitive, unhelpful, or inconsistent in very long chat sessions in both English and non-English languages. Developers are encouraged to place appropriate mitigations, like limiting conversation turns to account for the possible conversational drift

Developers should apply responsible AI best practices, including mapping, measuring, and mitigating risks associated with their specific use case and cultural, linguistic context. Important areas for consideration include: 
* Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.
* High-Risk Scenarios: Developers should assess the suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.
* Misinformation: Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).
* Generation of Harmful Content: Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.
* Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.

## Software
* [PyTorch](https://github.com/pytorch/pytorch)
* [Transformers](https://github.com/huggingface/transformers)
* [Flash-Attention](https://github.com/HazyResearch/flash-attention)

## Hardware
Note that by default, the Phi-mini-MoE model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:
* NVIDIA A100
* NVIDIA A6000
* NVIDIA H100
  
## License
The model is licensed under the [MIT license](./LICENSE).

## Trademarks
This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.