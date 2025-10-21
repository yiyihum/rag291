---
language:
- en
- fr
- de
- es
- it
- pt
license: apache-2.0
library_name: transformers
inference: false
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://www.almawave.com/privacy-policy/">Privacy
  Policy</a>.
tags:
- vllm
---

# Model Card for Velvet-14B

Velvet is an Italian family of large language models, developed from scratch, featuring a dense architecture. This model was trained on the HPC Leonardo infrastructure hosted by [CINECA](https://www.cineca.it/en), utilizing public data that underwent extensive curation.

The training process commenced with over 10 trillion tokens and culminated in more than 4 trillion tokens, across six languages (Italian, English, Spanish, Portuguese-Brazilian, German, French) for the 14B model.

Efforts were specifically made to maintain balance between languages, with particular emphasis on Italian, which comprises approximately 23% of the data. In addition to linguistic data, Velvet incorporates over 400 billion tokens from more than 100 programming languages to facilitate more structured inferences in the aforementioned languages.
  

## Model details


- **Model Developers:** Technology and innovation Team, Almawave
- **Input:** Models input text only.
- **Output:** Models generate text only.
- **Release Date:** January 31st, 2025.
- **License:** Apache 2.

 ### Model Architecture and training

Velvet family of models comes in two sizes --- 2B and 14B parameters ---  namely, **Velvet-2B** and **Velvet-14B**.
**Velvet-14B**  is a 14B parameter long-context instruct model finetuned from **Velvet-14B-base** using a combination of open source instruction datasets with permissive license and internally collected synthetic datasets tailored for solving long context problems.

#### Architecture
- Auto-regressive language model with a transformer-based causal decoder-only design.
- 50 transformer layers.
- MLP intermediate size of 12,544.
- Grouped Query Attention (GQA): 40 query heads and 8 key-value heads for efficiency.
- Rotary Position Embedding (RoPE): High theta value for long-context modeling.
- SiLU activation function with RMSNorm method.
- Context length up to 128K tokens, trained on sequences of 4/8/16k tokens.
- 127K vocabulary size, designed to accommodate language diversity.
- Training phase: pretraining & post-training.

### Status
This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.
Almawave is actively working on strategies to enhance alignment and robustness in future iterations of the Velvet model.

### License
Velvet-14B and Velvet-2B are made available under the Apache 2.0 license

### Supported Languages
Velvet-14B has been trained on Italian, English, German, Spanish, French, Portuguese.

To ensure high-quality multilingual performance, the dataset was curated to balance linguistic representation, reducing overfitting biases toward high-resource languages.



## Intended Use

Velvet-14B is designed to be integrated into AI systems or applications. Its potential use include, but it is not limited to, text generation, classification, summarization, question answering. It is important to note that specific applications may need further model adaptations or additional safeguards to prevent undesirable behavior or outputs.

### Capabilities

- Summarization
- Information Extraction
- RAG (Retrieval Augmented Generation)
- Paraphrasing
- Textual Entailment
- Natural Language Inference
- Common Sense Reasoning
- Multistep Reasoning
- Text Classification
- Machine Translation
- Question Answering
- Text Completion
- Multiturn Conversation


  
## Training Data


### Overview

The model was pretrained on over 4 trillion tokens of data from publicly available sources. These sources include diverse collection of web text exposes the model to an extensive range of linguistic styles, topics, and vocabulary. The training dataset has been built with a balanced representation of multiple languages.

The fine-tuning data includes publicly available instruction datasets, as well as over 2M human-annotated and synthetic examples for SFT.
Moreover we used over 50k human generated examples for safety instructions. Neither the pretraining nor the fine-tuning datasets include Almawave's customer data.

We have made significant efforts to enhance the reliability of responses in terms of factual accuracy; however, we always recommend grounding LLM responses with external factual data (e.g. Retrieval Augmented Generation).

### Data Freshness
The pretraining data has a cutoff between August 2024 and October 2024 for the two different models.


## Evaluation 


### EU languages

Velvet-14B average on EU languages covered by the model, unless specified.

| Category    |   Benchmark           |     Velvet-14B |
|---------------------------| ------------------------| -------------------|
| General    |   MMLU (5-shot)  |   56.4 |
| Instruction Following    |   IFEval (0-shot) - en  |   65.4 |
| Commonsense |  Hellaswag (10-shot)    |   72.8 |
| | WinoGrande (0-shot) - en |   72.5 |
| Reasoning              |     ARC-Challenge (25-shot)  | 57.3 |
||     MUSR (0-shot) - en  | 12.3 |
|Function Calling/Tool Use|     BFCL (AST summary) - en  | 67.5 |


### Italian language

| Category    |   Benchmark           |     Velvet-14B |
|---------------------------| ------------------------| -------------------|
| General    |   MMLU (5-shot)  |   58.6 |
| Commonsense |  Hellaswag (0-shot)    |   72.7 |
| | WinoGrande ITA-bench (0-shot) |   73.2 |
|| PIQA ITA-bench (0-shot)       |     71.7 |
|| SciQ ITA-bench (0-shot) with p.      |     91.9 |
| Reasoning              |     ARC-Challenge (0-shot)  | 55.2 |


### Tokenizer

| Lang    |  Fertility           |     Parity (en) | Parity (it) |
|--------| ------------------| ---------------| ---------------|
|en|	1.403 |	1.000 |	0.904
|it|	1.464 |	1.129 |	1.000
|pt|	1.386 |	1.135 |	1.016
|es|	1.324 |	1.205 |	1.078
|de|	1.984 |	1.240 |	1.112
|fr|	1.632 |	1.330 |	1.191
|code|	2.672|	NA|	NA |

## Usage

The model can be used with the following frameworks;
- [`vllm`](https://github.com/vllm-project/vllm)
- [`transformers`](https://github.com/huggingface/transformers)
- [`ollama`](https://ollama.com/Almawave/Velvet)

## Responsibility and Safety


Large language models are versatile technologies designed to serve a wide range of applications. However, they are not intended to meet every developer\'s safety requirements out-of-the-box, as these requirements naturally vary depending on the specific use case and application context.

### Safety

For our instruction-trained model, we have undertaken comprehensive exercises, engaged in adversarial internal and external evaluations, and put into place mitigation techniques to reduce risks. These exercises were designed to thoroughly examine the model\'s limitations and potential, simulating real and hypothetical scenarios where undesirable behavior might arise.

However, despite these efforts, it is inevitable that some residual hazards are bound to exist, as every large language model presents intrinsic complexities that cannot be completely eliminated.

Then, developers are advised to implement suitable safety measures and exercise due diligence, tailoring these safeguards to align with their product policies and the specific requirements of their applications.

Some trade-offs between model helpfulness and alignment are likely inevitable. Developers should thoughtfully balance the benefits of alignment and helpfulness for their specific applications and audiences.
They must also remain aware of residual risks when using Velvet models and leverage additional safety tools as necessary to achieve an appropriate safety standard for their use case.
We advise developers to carefully evaluate risks in the context of their specific use case. They should consider the potential implications of a model failure in their applications and put adequate measures in place to manage such eventualities.

In parallel, we are collaborating with the scientific and industrial community to establish AI safety benchmark standards that are transparent, rigorous, and interpretable. The goal is to promote a better understanding of the risks associated with large language models and support the development of safer and more responsible solutions.

### **Governance and Internal Oversight**

Almawave has established an **internal governance framework** for the management and continuous oversight of the Velvet model family.
Key governance elements include: 

- **Supervision by an Ethical and Technical Committee** to ensure the model aligns with principles of **transparency, fairness, and safety**.
- **Ongoing bias monitoring** through auditing tools, with iterative updates to improve alignment with ethical guidelines.
- **Restrictions on commercial and institutional usage** to ensure compliance with regulatory frameworks and **shared responsibility principles**.
- **Periodic review processes** to assess the model’s impact in high-risk applications.

## Bias, Risks, and Limitations

  
Velvet has been trained on a dataset that, despite all the data curation efforts, might include toxic language and societal biases. This means that models in the Velvet family may reproduce these biases and produce harmful responses when prompted with such inputs. This is a common issue in AI models trained on large datasets, as they can inadvertently perpetuate the biases present in the data.
Furthermore, the model may generate inaccurate, incomplete, or redundant responses, which could be socially unacceptable or undesirable, even if the input prompt is not explicitly offensive. This is a potential flaw in the model\'s design and training process, and it underscores the importance of careful validation and monitoring of AI systems to ensure that they are functioning as intended.

Additionally, using the recommended prompt template is crucial to mitigate the risk of harmful responses, as it is designed to guide the model towards more appropriate and safe outputs. However, it is important to note that the model\'s performance may still vary depending on the specific context and complexity of the input prompt.

Finally, when using this model in an agentic workflow, it is essential to validate that all imported packages and dependencies are from trusted sources to ensure the model\'s security and integrity. This is a critical step in maintaining the model\'s ethical and responsible use, and it is important to prioritize end-to-end security measures to prevent any potential vulnerabilities or breaches.

Future versions of Velvet will integrate automated red-teaming protocols, continuously stress-testing the model against adversarial prompts to identify and mitigate emerging risks.  

### Sensitive Data Handling and Usage Restrictions

The Velvet model has not been trained on unauthorized personal data and must not be used to process sensitive data without appropriate security measures.

Usage Restrictions:
- Prohibited use on sensitive healthcare, financial, or government data without specific safeguards.
- Mandatory human validation in scenarios where the model’s outputs could have legal or ethical consequences.
- High-risk applications (legal, medical, public governance) must implement content filtering and auditing techniques to ensure response quality and safety.
 

## Ethical Considerations


Almawave core values are openness, inclusivity, and helpfulness. We aim to create AI that is accessible and beneficial for everyone, regardless of their background. Velvet models are designed to be respectful of diverse perspectives and avoid unnecessary judgments. Therefore, Velvet models are designed to be inclusive and respectful of diverse perspectives and needs. We strive to avoid unnecessary judgment or the imposition of normative views, recognizing that content deemed problematic in some contexts can have valuable applications in others.

We deeply respect the dignity and autonomy of all users, particularly their right to free thought and expression, which are fundamental to innovation and progress.

While we have taken significant steps to ensure the safety and reliability of Velvet models, it is important to acknowledge that they may occasionally generate inaccurate, biased, or unsafe responses.

Almawave is actively engaging with ethics committees and domain experts to ensure continuous oversight of Velvet’s outputs, improving safeguards through community feedback.

We strongly encourage the community to exercise caution and conduct thorough safety testing and fine-tuning when using Velvet models for specific tasks.

Opinions expressed by Velvet depend on training data and do not reflect any opinions of Almawave.

## Contributions
Direction: Raniero Romagnoli
- Model engineering and training: David Alessandrini, Francesco Buciuni, Andrea Favalli, Diego Perna, David Preti, Federico Wolenski, Fabio Massimo Zanzotto
- Data engineering and management: Valentina Bellomaria, Cristina Giannone, Alfredo Serafini
- Use case adaptation and testing: Salvatore Ricciardi, Simone Scaboro, Beatrice Turano, Giancarlo Xompero
- Evaluation: Giovanni Cingolani, Silvana De Benedictis, Caterina Masotti, Riccardo Pasquini, Guillaume Ruiz, Giuseppe Scrugli, Alessandro Vizzarro
- Product and governance: Beata Dobrzynska, Matteo Amore, Marco Gennaro Di Martino, Vincenzo Sciacca, Alessandra Staglianò, Luca Vinciguerra

