---
configs:
- config_name: default
  data_files:
  - split: uz
    path: data/dataset.json
task_categories:
- text-generation
- question-answering
language:
- uz
tags:
- uz
- legal
- wakilai
- uz-evaluation
- uz-benchmark
- law-evaluation-dataset
pretty_name: Wakil AI Legal Benchmark Dataset
size_categories:
- n<1K
---

# WakilAI Legal Evaluation Dataset (Uzbek Law)

**WakilAI** is a legal assistant focused on Uzbekistan’s laws. This dataset contains an evaluation split of real citizen and government-facing legal questions paired (where applicable) with statutory article references from Uzbekistan’s legal code. It is designed to assess **truthfulness, grounding, and citation quality** of Retrieval-Augmented Generation (RAG) systems.

---

## 1) Evaluation Methodology

To measure the truthfulness and reliability of WakilAI’s legal assistant, we used **RAGAS (Retrieval-Augmented Generation Assessment Suite)**, an evaluation framework designed to assess RAG systems.  
**Reference:** *RAGAS: Automated Evaluation of Retrieval-Augmented Generation.*

### Why RAGAS?
Legal AI systems must not only be fluent but also factual and verifiable. Traditional benchmarks (e.g., BLEU, ROUGE) measure surface-level similarity but do not capture whether the model is actually telling the truth.

RAGAS factualness metrics directly evaluate:

- Whether the model’s answer is **grounded** in retrieved documents.  
- Whether factual statements are **consistent** with source texts (not hallucinated).  
- How well the model **supports answers with citations and evidence**.

This makes RAGAS particularly suited for WakilAI, since our promise is **trustworthy answers backed by lex.uz sources**.

---

## 2) Dataset

We constructed a test dataset of **500+** real-world legal questions sourced from Uzbekistan’s most widely used official and citizen-facing platforms:

- **advice.uz** – practical legal advice and Q&A for citizens.  
- **gov.uz** – frequently asked questions on public services.  
- **my.gov.uz** – official government services and announcements.

We have collected these q&a mainly from above website FAQs. 

### Composition and Coverage

![**Figure 1**: *Distribution of legal questions across categories in the evaluation dataset.*](./assets/categories.png)  

The dataset encompasses **22+ legal categories**, providing broad coverage of the regulatory landscape. The largest categories include:

- **Ijtimoiy Yordam va Pensiya (Social Assistance and Pensions)** – 11%  
- **Soliq va Moliya (Taxation and Finance)** – 8%  
- **Tadbirkorlik va Biznes (Entrepreneurship and Business)** – 7%

This categorical distribution facilitates evaluation across both general and domain-specific contexts.

### Article References

A notable subset of **87 questions (~16%)** explicitly reference statutory provisions at the article (“modda”) level. This enables a focused evaluation track, isolating tasks that require precise clause-level retrieval and reasoning, and distinguishing them from more general legal information queries.

---

## 3) Evaluation Results

We compared WakilAI’s three models (**Nano, Mini, Premium**) against competitor systems, including **LexAI** (another Uzbek legal AI) and **gpt-4o-mini-search** (a general LLM baseline).

### Overall Factualness

| Model                        | Factual Correctness F1 | Factual Correctness Recall | Factual Correctness Precision |
|-----------------------------|------------------------|----------------------------|-------------------------------|
| **Wakil-Mini (GPT-OSS-20B)**      | **0.47**               | 0.60                       | 0.41                          |
| **Wakil-Premium (GPT-OSS-120B)**  | **0.51**               | 0.63                       | 0.47                          |
| **Wakil-Nano (Gemma-27B)**        | 0.37                   | 0.47                       | 0.35                          |
| LexAI v2 (10.09.25)         | 0.36                   | 0.46                       | 0.33                          |
| LexAI v3 (14.09.25)         | 0.34                   | 0.46                       | 0.31                          |
| GPT-4o-mini-search          | 0.34                   | 0.41                       | 0.33                          |

**Key Insights**

- **Wakil-Premium (GPT-OSS-120B)** delivered the *highest factual correctness*, outperforming both WakilAI’s smaller models and all competitor systems.  
- **Wakil-Mini (GPT-OSS-20B)** showed a strong balance of accuracy and efficiency, ranking above all LexAI versions and GPT-4o-mini.  
- **Wakil-Nano (Gemma-27B)**, while more efficient, still performed at or above competitor baselines, showing that even our smallest tier is competitive.  
- **LexAI**, the closest competitor, consistently scored lower across all factualness metrics, confirming WakilAI’s superior grounding and reliability with **~17% higher F1**.

### Article-based vs Non-Article-based

| Model                        | Article-based F1 | Non-Article-based F1 |
|-----------------------------|------------------|----------------------|
| **Wakil-Nano (Gemma-27B)**        | 0.36             | 0.37                 |
| **Wakil-Mini (GPT-OSS-20B)**      | 0.46             | 0.47                 |
| **Wakil-Premium (GPT-OSS-120B)**  | **0.50**         | **0.51**             |
| LexAI v2 (10.09.25)         | 0.38             | 0.36                 |
| LexAI v3 (14.09.25)         | 0.38             | 0.34                 |
| GPT-4o-mini-search          | 0.37             | 0.34                 |

Among all evaluated models, **Wakil-Premium (GPT-OSS-120B)** leads with the highest **article-based F1 = 0.50**, followed by **Wakil-Mini (GPT-OSS-20B)** at **0.46**. In comparison, **LexAI v2/v3** remain at **0.38**, trailing behind both medium- and large-scale open-source models, highlighting a clear performance gap in handling article-referencing legal queries.

![**Figure 2**: *F1 score comparison by legal category for GPT-OSS-120B vs. LexAI v3.*  ](./assets/comparison.png)  

Across almost all categories, **Wakil-Premium (GPT-OSS-120B)** consistently outperforms **LexAI v3**, with the largest performance gaps observed in **Audit va Moliyaviy Nazorat**, **Mehnat Huquqi**, and **Migratsiya va Fuqarolik**. LexAI v3 remains competitive in some areas like **Xalqaro va Hamkorlik** but overall trails behind, highlighting the superior category-level accuracy of the larger model.

---

## 4) Note on Data Importance

The improvements observed in WakilAI’s factual correctness are **not solely** the result of larger or more powerful LLMs. Instead, the most significant gains came from our **custom data preprocessing pipeline** — including **cleaning, normalization, and the introduction of a hierarchical structure** that mirrors the organization of Uzbek law.

This hierarchy ensures that **retrieval is context-aware and legally precise**, reducing irrelevant matches and improving grounding. In practice, this preprocessing and structuring contributed **more** to accuracy improvements than model size alone.

**WakilAI’s strength comes from its data strategy** — demonstrating that carefully prepared, structured, and localized legal data is the true foundation for trustworthy AI in law.

---

## 5) Data Fields

Each entry in the evaluation split contains:

- `question` *(string)* — real-world legal questions
- `category` *(string)* — one of 22+ legal categories  
- `modda_in_answer` *(boolean)* — whether statutory article(s) are referenced  
- `answer` *(object, optional)* — reference answer for the question

---

## 6) Loading the Dataset

```python
from datasets import load_dataset

ds = load_dataset("humblebeeai/wakilai-legal-eval-uz")
```

## 7) Citations
- [*RAGAS: Automated Evaluation of Retrieval-Augmented Generation.*](https://arxiv.org/abs/2309.15217)


## 8) Contact
Wakil AI - Transforming legal practice with intelligent AI-powered tools. Save time, improve accuracy, and focus on what matters most.
- Website: wakil.ai
- Email: contact@humblebee.ai
- Phone Number: +82-10-3744-2219
- Address: 202, Gyeonginnam-gil 76, Incheon, South Korea

*powered by HumbleBeeAI*