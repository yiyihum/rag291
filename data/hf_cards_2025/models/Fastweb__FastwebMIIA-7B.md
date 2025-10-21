---
license: other
license_name: fastweb
license_link: https://www.fastweb.it/grandi-aziende/artificial-intelligence/Non-Commercial-License.pdf
pipeline_tag: text-generation
language:
- it
- en
library_name: transformers
tags:
- fastweb
extra_gated_heading: Acknowledge license to accept the repository
extra_gated_description: This repository is publicly accessible, but you have to accept
  the conditions to access its files and content.
extra_gated_prompt: 'By downloading, accessing, and using the model as specified,
  you fully accept the [FastwebMIIA''s Non-Commercial License](https://www.fastweb.it/grandi-aziende/artificial-intelligence/Non-Commercial-License.pdf),
  the [Acceptable Use Policy](https://www.fastweb.it/grandi-aziende/artificial-intelligence/fastweb-miia/documentazione-trasparenza-ai/Acceptable%20Use%20Policy.pdf)
  (AUP), and the other attached documents. If you do not agree to the terms and conditions
  in this license and the related documents, you must not download or use the model
  and should delete any copies you may already have.


  This license grants the use of FastwebMIIA exclusively for

  1. personal, scientific, or academic research activities, whether theoretical or
  applied, and non-professional, with purely informative purposes, and

  2. under your own authority and responsibility during professional activities limited
  to your business and organizational activities, which do not have commercial purposes.


  You are prohibited from using the model for commercial purposes. Specifically, the
  Licensee cannot:

  1. Integrate the model into services, products, platforms, systems, or applications
  if the integration is intended for resale, distribution, or making it available
  to third parties for a fee;

  2. Transfer, distribute, sell, rent, sublicense, or make the model or any part of
  it available to third parties, either for a fee or free, without written permission
  from the Licensor;

  3. Use the model to develop or train other LLMs, regardless of the purpose or intended
  use.


  By completing the form you acccept [Fastweb’s Privacy Policy](https://www.fastweb.it/grandi-aziende/artificial-intelligence/Informativa-Privacy-HuggingFace.pdf). '
extra_gated_fields:
  First Name: text
  Last Name: text
  Email: text
  I want to use this model for:
    type: select
    options:
    - For personal, scientific or academic research
    - For professional activities or business operations, without commercial purposes
  I have read and I agree with Fastweb MIIA’s license linked above: checkbox
  I have read and I agree with Fastweb MIIA’s AUP linked above: checkbox
  I have read and I agree with Fastweb’s Privacy Policy linked above: checkbox
---

This model card provides an overview of FastwebMIIA, Modello Italiano di Intelligenza Artificiale, developed by Fastweb  . 

## Model Overview

FastwebMIIA, Modello Italiano di Intelligenza Artificiale, is a large language model with 7 billion parameters, built on an autoregressive transformer architecture. It has been specifically designed and trained for the Italian language and cultural context. The model was trained on a carefully curated, predominantly Italian corpus, in full compliance with EU AI Act and national regulations. 

FastwebMIIA implements a custom tokenizer, trained by Fastweb to be optimized for Italian, English, and the main programming languages, with a total vocabulary of 50,000 tokens. FastwebMIIA exploits RoPE (Rotary Positional Embeddings) to efficiently encode positional information within the attention mechanism. The model supports an extended contextual window of 16k tokens, allowing it to handle long documents, multi-turn conversations and complex queries while maintaining consistency and contextual understanding. 

**Model developer**: Fastweb

**Model type/architecture:** FastwebMIIA is based on autoregressive (causal, decoder-only) transformer architectures. It incorporates rotary position embeddings and is trained using the next-token prediction objective.

**Languages Available:** Trained in Italian and English 

**Model Released Date:** May 29, 2025

**License:** FastwebMIIA is accessible under a Non-Commercial License explicitly allowing for non-commercial research, educational and internal use, and under a custom Commercial License for any commercial use of the Model.  

## Model Access

FastwebMIIA is accessible through multiple platforms to support a variety of use cases and deployment preferences, according to the final commercial or non-commercial purposes of the use cases FastwebMIIA is to be integrated:

* **On-Premise (Low-Code Tooling):**

FastwebMIIA can be deployed within enterprise environments for commercial purposes via a low-code platform, allowing internal teams to test, adapt, and scale the model securely. This setup is ideal for organizations with strict data governance or compliance needs, aiming at developing AI use cases for commercial purposes. 
👉 To request a commercial demo or learn more about enterprise deployment, please contact us at Attivazione.FastwebMIIA@fastweb.it.

* **Hugging Face:**

The model weights and configuration files are publicly available on Hugging Face exclusively for the following purposes: (a) personal, non-professional research activities, whether scientific or academic, with theoretical or applied focus, intended solely for informational purposes and (b) professional activities conducted under one's own authority and responsibility, limited to a company's internal use cases that are not intended for commercial purposes. The Model cannot be used for commercial purposes. The Licensee is prohibited from integrating FastwebMIIA into services or products for resale or distribution or using it to develop or train other LLMs.
Users can download, fine-tune, or deploy the model using Hugging Face’s tools and hosted infrastructure under the Non-Commercial License . 

## Use with transformers

The model was trained and tested using transformers==4.45.2.

```python
import transformers
import torch

model_id = "Fastweb/FastwebMIIA-7B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="cuda",
)

messages = [
    {"role": "system", "content": "Sei FastwebMIIA, il chatbot italiano sviluppato da Fastweb."},
    {"role": "user", "content": "Ciao!"},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
    repetition_penalty=1.1, 
    top_p=0.9, 
    temperature=0.1
)
print(outputs[0]["generated_text"][-1])

# output: {'role': 'assistant', 'content': 'Ciao! Come posso aiutarti oggi?'}
```

 
## Hardware and Software

FastwebMIIA was trained on a proprietary NVIDIA H100 GPU cluster, optimised for large-scale distributed training. The training workflow was managed with MLDE (Machine Learning Development Environment) and LLMFoundry, which handled data processing, experiment tracking and scalable model training. This setup enabled the pre-training and fine-tuning of the 7B-parameter model on a corpus comprising trillions of tokens.

There is no assurance of compatibility with specific environments, operating systems, hardware, or software used by the Licensee.

## Training Details

### Architecture details

This model is an auto-regressive transformer model with the following architectural hyperparameters:

| **Hyperparameter**                  | **Value**         |
|-------------------------------------|-------------------|
| Number of layers                    | 32                |
| Number of attention heads           | 32                |
| Head size                           | 128               |
| Number of Key-Value heads           | 8                 |
| Hidden dimension size               | 4096              |
| Intermediate (MLP) size             | 14,336            |
| MLP activation function             | SiLU              |
| MLP type                            | Standard          |
| Attention dropout                   | 0.0               |
| MLP/Attention bias                  | No                |
| Normalization type                  | RMSNorm           |
| RMSNorm epsilon                     | 1e-5              |
| Vocabulary size                     | 50,270            |
| Sequence length (context window)   | 16,384             |
| Rotary position embedding type      | LLaMA v3-style    |
| Rotary base (rope theta)           | 500,000           |
| Rotary scaling factor               | 8.0                |
| High/Low frequency rope factors     | 4.0 / 1.0         |
| Weight initialization range        | ±0.02             |
| Tied word embeddings                | No                |
| Data type                           | bfloat16          |
| Total parameter count               | 7.39 billion     |

### Tokenizer

Our tokenizer has vocabulary size 50260 and was trained via the Byte-Pair Encodinge (BPE) algorithm, using the implementation provided by the Transformers library. They include:
* 50.000 tokens obtained with the BPE;
* 256 tokens representing all the byte values;
* 4 special tokens (BOS, EOS, PAD, UNK).
The tokenizer training set was a subset of our highest-quality data, which had been thoroughly cleaned and visually-inspected, in Italian, English, and programming languages.

*Fertility*

Tokenizer fertility is a metric for assessing tokenizer performance. It quantifies how efficiently a tokenizer represents text by calculating the ratio between the number of tokens produced and the number of words in the original text (see: https://arxiv.org/pdf/2310.08754).

The fertility values reported below were calculated on a subset (1%) of the Italian Wikipedia dataset from March 2022.

| model                                 | tokens  | fertility |
|--------------------------------------|---------|-----------|
| Almawave/Velvet-14B                  | 126976  | 1.537129  |
| *Fastweb/FastwebMIIA-7B*             | *50270* | *1.569404* |
| iGeniusAI/Italia-9B-Instruct-v0.1    | 50003   | 1.589896  |
| sapienzanlp/Minerva-7B-instruct-v1.0 | 51203   | 1.620168  |
| google/gemma-2-9b-it                 | 256000  | 1.708481  |
| utter-project/EuroLLM-9B-Instruct    | 128000  | 1.723624  |
| mistralai/Ministral-8B-Instruct-2410 | 131072  | 1.771119  |
| meta-llama/Llama-3.1-8B-Instruct     | 128256  | 1.970075  |
| microsoft/Phi-3-small-8k-instruct    | 100352  | 1.974537  |
| Qwen/Qwen2.5-7B-Instruct             | 151665  | 2.020880  |
| ibm-granite/granite-3.1-8b-instruct  | 49155   | 2.386821  |



### Training Data

FastwebMIIA was pretrained on approximately 1.5 * 2 * 10^12 textual tokens, combining publicly available and proprietary sources. The corpus consists primarily of content in Italian and English, with a smaller share in other European and non-European languages. The linguistic composition was designed to prioritize Italian, supporting strong performance in that language.

The data covers a broad set of domains, including literature, science, programming, history, law, and general knowledge, as well as examples of conversational and editorial writing. Only text-based data was used; no multimodal inputs (e.g., images, audio, or video) were included.

Fine-tuning involved a mix of open instruction-tuning datasets and synthetic examples generated with models from the Phi family.

When using FastwebMIIA, no prompt data is stored. We do not record user inputs to the models, ensuring that we do not collect any personally identifiable information (PII), nor do we use user data for training purposes.

*Data Cutoff*: The pretraining data has a cutoff of August 2024. The data was collected until February 2025.

## Limitations and Biases

FastwebMIIA is a large language model developed to assist with a wide range of conversational and generative tasks. While every effort has been made to train FastwebMIIA responsibly—including filtering and curating its training data—there are still important limitations to keep in mind.

FastwebMIIA can generate responses that are factually inaccurate, misleading, or incomplete. It does not possess awareness or a true understanding of the world, and it may produce outputs that seem plausible but are incorrect. In some contexts, it may reflect social, cultural, or historical biases that were present in its training data. This includes the potential for producing responses that could be insensitive, stereotypical, or otherwise objectionable.

FastwebMIIA must not be considered as a source of authoritative information or as a replacement for professional judgment.

Additionally, FastwebMIIA’s behavior may vary depending on the phrasing of prompts, and it cannot reliably anticipate or account for all contexts or values. Its outputs should be evaluated critically, especially in domains where fairness, safety, or accuracy are essential.

## Intended Use

FastwebMIIA is a text-only language model built for tasks such as chat-based assistance, content generation, summarization, and information extraction. It is intended for research, development, and integration into AI applications with proper safeguards.

### Out-of-Scope or Prohibited Use

FastwebMIIA is intended solely for legal use and must not be employed in illegal or fraudulent activities, in violation of its [Acceptable Use Policy](https://www.fastweb.it/grandi-aziende/artificial-intelligence/fastweb-miia/documentazione-trasparenza-ai/Acceptable%20Use%20Policy.pdf), to generate harmful or deceptive content, or operate in high-risk domains without human oversight. It is not designed for autonomous decision-making or executing real-world actions. Specifically, FastwebMIIA must not be used to violate laws or regulations, perform unauthorized data collection, engage in unlawful activities like misinformation, manipulation, discrimination or privacy violations, profile individuals without consent, exploit vulnerabilities due to age or socio-economic status, classify individuals unjustly based on social behavior, conduct predictive policing, or indiscriminately scrape facial images to expand recognition databases. This list is illustrative and not exhaustive.

The Licensee bears full responsibility for how the Model is used and the outcomes resulting from its use, including any configurations or interactions with the Licensee's specific environments, tools, or content.

### Report issues

To help ensure responsible use of the FastwebMIIA model, we welcome reports of misuse, unexpected behavior, or concerns regarding model outputs. If you encounter any issues or have feedback about how the model is being used, please reach out to us at assistenza.FastwebMIIA@fastweb.it. Your input supports ongoing improvements and helps us uphold safety and ethical standards.


## Evaluation

The model was evaluated using Hugging Face's [lm-eval framework](https://github.com/EleutherAI/lm-evaluation-harness), a standardised and reproducible benchmarking suite for language models. This tool allows for consistent comparison of model performance across tasks and languages, providing a reliable basis for multilingual and domain-specific evaluations.

For this evaluation, we focused on benchmarks specifically designed or adapted for the Italian language, covering tasks testing reasoning, comprehension and general knowledge:

* HellaSwag IT: A multiple-choice task for accomplished reasoning and text completion in Italian.

* ARC IT (AI2 Reasoning Challenge): A multiple-choice benchmark for science questions translated into Italian.

* ARC Challenge MT IT: A multilingual adaptation of the ARC Challenge, focusing on Italian.

* MMLU IT: The Massive Multitask Language Understanding dataset translated into Italian, testing a wide range of academic and cultural knowledge.

* Global MMLU IT: An extended version of MMLU covering additional topics and domains in Italian.

* XCOPA IT: A multilingual benchmark for causal reasoning, assessing ‘why’ questions in Italian.

This comprehensive benchmark suite provides a robust assessment of the model's performance in Italian, evaluating its ability to understand, reason and answer accurately on various topics and scenarios.

### General Knowledge Benchmarks scores

| Tasks               | Metric    | Score 5-shot | Score 0-shot |
|---------------------|-----------|--------------|--------------|
| arc_challenge_mt_it | acc_norm  | 0.5          | 0.4317       |
| arc_it              | acc_norm  | 0.5158       | 0.4559       |
| global_mmlu_it      | acc       | 0.615        | 0.5525       |
| hellaswag_it        | acc_norm  | 0.6453       | 0.6453       |
| m_mmlu_it           | acc       | 0.5707       | 0.5293       |
| xcopa_it            | acc       | 0.784        | 0.774        |

## Model Updates

New versions of the model will be published on this page, and users are required to review the most up-to-date versions. The provider will not be responsible for any use of obsolete versions of the model. It is the Licensee’s responsibility to ensure they are using the latest version to avoid potential issues or limitations associated with outdated models.


