---
library_name: transformers
pipeline_tag: text-generation
base_model:
- aisingapore/Gemma-SEA-LION-v4-27B
language:
- en
- zh
- vi
- id
- th
- fil
- ta
- ms
- km
- lo
- my
- jv
- su
license: gemma
base_model_relation: finetune
---

![Banner!](v4-banner-instruct.png "v4-banner-instruct")

# Model Card for Gemma-SEA-LION-v4-27B-IT

<!-- Provide a quick summary of what the model is/does. -->

Last updated: 2025-08-25

**SEA-LION** is a collection of Large Language Models (LLMs) which have been pretrained and instruct-tuned 
for the Southeast Asia (SEA) region.

Gemma-SEA-LION-v4-27B has undergone post-training using a QA pairs dataset in Burmese, English, 
Indonesian, Khmer, Lao, Malay, Tagalog, Tamil, Thai and Vietnamese, comprising approximately 10M samples in total, to create *Gemma-SEA-LION-v4-27B-IT*.

Gemma-SEA-LION-v4-27B-IT inherits Gemma 3's:

- Large 128K context length

- Image and text understanding capabilities, including document comprehension, visual Q&A, and image-grounded reasoning

- Advanced function calling and structured outputs to allow for seamless integration into larger systems


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

SEA-LION stands for *Southeast Asian Languages In One Network*. 

We performed post-training in English and SEA languages on Gemma-SEA-LION-v4-27B, a decoder model using the Gemma 3 architecture, to create Gemma-SEA-LION-v4-27B-IT.

For tokenization, the model employs the default tokenizer used in Gemma 3 27B IT.


- **Developed by:** Products Pillar, AI Singapore
- **Funded by:** Singapore NRF
- **Shared by:** Products Pillar, AI Singapore
- **Model type:** Decoder
- **Context length:** 128k tokens
- **Language(s) (NLP):**  Burmese, English, Indonesian, Khmer, Lao, Malay, Mandarin, Tagalog, Tamil, Thai and Vietnamese
- **License:** [Gemma Terms of Use](https://ai.google.dev/gemma/terms)
- **Finetuned from model:** Gemma-SEA-LION-v4-27B

As of 25 Aug 2025, Gemma-SEA-LION-v4-27B-IT excels at Southeast Asian (SEA) tasks when compared to other open models
with fewer than 200 billion parameters and demonstrates performance comparable to that of larger and top closed models. 
For detailed rankings, please refer to the [leaderboard](https://leaderboard.sea-lion.ai/). 


### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/aisingapore/sealion.git


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model has not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable for any claims, damages, or other liabilities arising from the use of the released weights and codes.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

*The model was not tested for robustness against adversarial prompting.* It is important for users to be aware that our model exhibits certain limitations that warrant consideration. 
Like many LLMs, the model can hallucinate and occasionally generates irrelevant content, 
introducing fictional elements that are not grounded in the provided context. 
Users should also exercise caution in interpreting and validating the model's responses 
due to the potential inconsistencies.

**Limitations**

In terms of vision capability, Gemma-SEA-LION-v4-27B-IT has been trained and fine-tuned exclusively on the text back-end.
As a result, its vision capabilities are expected to be comparable to those of Gemma 3 IT 27B, 
and may not exhibit significant improvements or differences in this area. [🤗 google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it )




## How to Get Started with the Model

Use the code below to get started with the model.

Use the code below to get started with the model using the 🤗 Transformers library.
```python
from transformers import pipeline
import torch

pipe = pipeline(
    "text-generation",
    model="aisingapore/Gemma-SEA-LION-v4-27B-IT",
    device="cuda",
    torch_dtype=torch.bfloat16
)

messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Write a poem on southeast asian countries in Indonesian."}
        ]
    }
]

output = pipe(text=messages, max_new_tokens=200)
print(output[0]["generated_text"][-1]["content"])
```


## Training Details

- **Training Datasets:**
The instruction fine-tuning dataset combines our SEA-Instruct, Infinity-Instruct, 
and OpenMath-Instruct 2 with open-source datasets. For the Online RL datasets, open sourced datasets such as 
nvidia/Llama-Nemotron-Post-Training-Dataset (RL set) and zwhe99/DeepMath-103K were used. For alignment, rejected-chosen pairs are generated 
from the target model, with the *chosen* responses obtained by rewriting and improving upon 
the *rejected* outputs.
Prompt sampling is guided by a gradient-based analysis process.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Training Hyperparameters

- **Training regime:**
Our post-training workflow consists of multiple stages: instruction fine-tuning, 
model merging, online RL for both instruction following and math using DRGPPO, 
and then followed by on-policy alignment via APO.


 <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->


## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

We evaluated Gemma-SEA-LION-v4-27B-IT on general language, multi-turn chat and instruction-following capabilities.

**Testing Data**

General language capabilities

For the evaluation of general language capabilities, we employed the [SEA-HELM evaluation benchmark](https://arxiv.org/abs/2502.14301) across a variety of tasks. 
These tasks include Question Answering (QA), Sentiment Analysis (Sentiment), Toxicity Detection (Toxicity), Translation in both directions (Eng>Lang & Lang>Eng), 
Abstractive Summarisation (Abssum), Causal Reasoning (Causal), Natural Language Inference (NLI), Linguistic Diagnostics (LINDSEA), Cultural Knowledge (Kalahi) 
and Global MMLU Lite.

Instruction-following and Multi-turn Chat

We evaluated the models on instruction-following and multi-turn chat capabilities with SEA-IFEval (based on [IFEval](https://arxiv.org/abs/2311.07911)) and SEA-MTBench (based on [MT-Bench](https://arxiv.org/abs/2306.05685)) respectively. 
The two datasets were originally in English, the linguists and native speakers in the team worked together to filter, localise and translate the datasets into the respective target languages to ensure that the examples remained reasonable, meaningful and natural.


#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

All evaluations were run with the model specific generation parameters defined in the model config. Each evaluation comprised of 8 runs with different seeds and the final results were averaged across these runs.

For all tasks, the model was expected to provide an answer tag from which the answer was automatically extracted. For tasks where options were provided, the answer should comprise one of the pre-defined options.

The evaluation was done zero-shot with native prompts on a sample of 100-1000 instances for each dataset. 

SEA-IFEval

SEA-IFEval evaluates a model's ability to adhere to constraints provided in the prompt, 
for example beginning a response with a specific word/phrase or answering with a certain number of sections. 
Additionally, accuracy is normalised by the proportion of responses in the correct language 
(if the model performs the task correctly but responds in the wrong language, it is judged to have failed the task).

SEA-MTBench

SEA-MTBench evaluates a model's ability to engage in multi-turn (2 turns) conversations and respond in ways that align with human needs. 
We use `gpt-4.1-2025-04-14` as the judge model and compare against `gpt-4.1-2025-04-14` as the baseline model. 
The metric used is the weighted win rate against the baseline model (i.e. average win rate across each category: 
Math, Reasoning, STEM, Humanities, Roleplay, Writing, Extraction).


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

The following metrics were used:
| Task                                | Metric                                 |
|--------------------------------------|----------------------------------------|
| Sentiment Analysis                   | Accuracy                               |
| Extractive QA (ID, VI, TH, TA)       | ChrF++                                 |
| MCQ-QA (TL, MY, MS)                  | Accuracy                               |
| Metaphor                             | Accuracy                               |
| Abstractive Summarisation            | Rouge-L                                |
| Translations                         | MetricX-24 score (with reference)      |
| Causal Reasoning                     | Accuracy                               |
| Natural Language Inference           | Accuracy                               |
| LINDSEA                              | Accuracy                               |
| Global MMLU Lite                     | Accuracy                               |
| Kalahi                               | Accuracy                               |
| SEA-IFEval                           | Accuracy                               |
| SEA-MTBench                          | Win rate against a reference           |
| Toxicity Detection                   | Accuracy                               |


### Results
![Leaderboard results on SEA-HELM snapedshot on 25 Aug 2025!](leaderboard-IT.png "Leaderboard results on SEA-HELM snapedshot on 25 Aug 2025")

For details on Gemma-SEA-LION-v4-27B-IT performance, please refer to the SEA-HELM leaderboard, [Leaderboard results on SEA-HELM](https://leaderboard.sea-lion.ai/).



## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** Nvidia H200 140GB GPUs
- **Hours used:** 214 hrs 
- **Cloud Provider:** SMC H200
- **Compute Region:** Singapore
- **Carbon Emitted:** appx. 98 kg CO2 e

## More Information

This is the repository for the commercial instruction-tuned model. 
The model has not been aligned for safety. Developers and users should perform their own safety 
fine-tuning and related security measures. In no event shall the authors be held liable 
for any claims, damages, or other liabilities arising from the use of the released weights and codes.

AI Singapore is a national programme supported by the National Research Foundation, Singapore and hosted by the National University of Singapore. 
Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation or the National University of Singapore.

For more info, please contact us at sealion@aisingapore.org


## Team

Antonyrex Sajeban, Chan Hok Teng Adwin, Cheng Zi Yi Nicholas, Choa Hsueh Mei Esther, Heng Jonathan, Huang Yuli, Hulagadri Adithya Venkatadri, Jann Railey Estrada Montalan, 
Kang Siow Wei  Bryan, Lau Wayne, Lee Chwan Ren, Leong Wai Yi, Leong Wei Qi, Limkonchotiwat Peerat, Muhammad Ridzuan Bin Mokhtar, Nagarajan Karthik, Ng Boon Cheong  Raymond,
Ngee Chia Tai, Ngui Jian Gang, Nguyen Thanh Ngan, Ong Jin Jie Brandon, Ong Tat-Wee David, Ong Zhi Hao, Pereira Mark, Rengarajan Hamsawardhini, Susanto Yosephine, 
Sutaveephamochanon Anocha, Tan Choon Meng, Tan Chor Phin Evelyn, Tan Siao Wei Jessica, Teng Kok Wai Walter, Teo Eng Sipp Leslie, Tjhi William, Yeo Yeow Tong, Yong Xianbin, 
Liew Rachel, Liu Bing Jie Darius, Teo Wei Yi, Zhou Lin (NCS), Gopalakrishnan Roshan (NCS), Anda Cuahtemoc (NCS), Sri Devi Wijaya (NCS),  Nandi Partha (NCS), 
Elliott Chris (Google), Mohseni Mohammadreza (Google), Sharan Mayank (Google), Wei Fanny (Google), Tang Jiuqiang (Google), Xu Xiang (Google), Yu Ting (Google), Loh Michelle (Google), Mangal Saurabh (Google), Mukherjee Pratyusha (Google), Sim Stephanie (Google)


## Contact

sealion@aisingapore.org