---
language:
- en
- fi
- zh
- hi
- ca
- sv
- cs
- fa
- es
- it
- eu
- ar
- fr
- de
license: cc-by-4.0
size_categories:
- 10K<n<100K
task_categories:
- token-classification
- text-classification
- text-generation
- zero-shot-classification
- question-answering
pretty_name: psiloqa
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: lang
    dtype: string
  - name: wiki_title
    dtype: string
  - name: wiki_url
    dtype: string
  - name: llm_checkpoint
    dtype: string
  - name: wiki_passage
    dtype: string
  - name: question
    dtype: string
  - name: golden_answer
    dtype: string
  - name: llm_answer
    dtype: string
  - name: annotated_span
    dtype: string
  - name: complexity
    dtype: string
  - name: labels
    sequence:
      sequence: int64
  splits:
  - name: train
    num_bytes: 107841766
    num_examples: 63792
  - name: validation
    num_bytes: 5716421
    num_examples: 3355
  - name: test
    num_bytes: 5223781
    num_examples: 2897
  download_size: 48980173
  dataset_size: 118781968
tags:
- qa
- hallucination_detection
- span_level
- multilingual
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/636b867ecde3707d10999b96/dhvJYKmLQjKlzZ8ODVGSL.png)

# Paper
[When Models Lie, We Learn: Multilingual Span-Level Hallucination Detection with PsiloQA](https://huggingface.co/papers/2510.04849)

# Code
[https://github.com/s-nlp/PsiloQA](https://github.com/s-nlp/PsiloQA)

# What is it?
**PsiloQA** is the largest dataset for training and evaluating systems on multilingual span-level hallucination detection with retrieved context. It offers:
1. An **automated and scalable pipeline** for generating, annotating and filtering data for hallucination detection task
2. A **large multilingual dataset for 14 languages** with high-quality and fine-grained span-level hallucination annotations for numerous open-source LLMs
3. A comprehensive **empirical evaluations** of various state-of-the-art span-level hallucination detection methods of different types across 14 languages.

The dataset is constructed synthetically through the following stages:
1. **Multilingual QA generation**: creation of question–answer pairs in 14 languages using GPT-4o, combined with randomly retrieved passages from Wikipedia articles.
2. **LLM hypothesis without retrieval**: generation of answers to the same questions without providing the retrieved passages. Since only the model’s internal knowledge is available, it struggles to answer hard factual questions correctly.
3. **Span-level inconsistency annotation**: automatic detection of hallucinated spans by aligning the GPT-4o golden answers with the LLM hypotheses.
4. **Filtering**: removal of incomplete or subjective questions, as well as cases where the model explicitly refuses to answer.

Explore the full PsiloQA pipeline code implementation on GitHub: [s-nlp/PsiloQA](https://github.com/s-nlp/PsiloQA)

PsiloQA is primarily intended for developing and benchmarking multilingual hallucination detection systems. At the same time, we believe that PsiloQA may be of broader interest: the dataset also provides question–context–answer triplets with golden answers and model hypotheses, which can support a wide range of applications such as benchmarking LLMs with and without retrieval, developing multilingual QA systems, and beyond.

Among span-level hallucination detection datasets, PsiloQA stands out by covering 14 languages, providing the largest training split, focusing on the general domain, and containing naturally occurring hallucinations. The training set comprises 63,792 samples, while the test set includes 2,897 samples. In total, hypotheses were generated using 24 different open-source LLMs.

| **Dataset** | **Domain** | **Annotation** | **Generation** | **# Languages** | **# LLMs** | **# Train** | **# Val** | **# Test** | **Licence** |
|---|---|---|---|---|---|---|---|---|---|
| Mu-SHROOM | General | Manual | Natural | 14 | 38 | 3,351 (unlabeled) | 499 | 1,902 | CC-BY-4.0 |
| HalluEntity | Biography | Manual | Natural | 1 (En) | 1 | -- | -- | 157 | MIT |
| RAGTruth_QA | General | Manual | Natural | 1 (En) | 6 | 5,034 | -- | 900 | MIT |
| FAVA-Bench | General | Auto | Synthetic | 1 (En) | 3 | -- | -- | 902 | CC-BY-4.0 |
| **PsiloQA** | General | Auto | Natural | 14 | 24 | 63,792 | 3,355 | 2,897 | CC-BY-4.0 |

# Sample Usage

This repository contains the **full PsiloQA generation pipeline** — from sampling multilingual Wikipedia contexts to question–answer generation, LLM hypothesis production, annotation, and filtering.

## Installation
Install uv:
```bash
pip install uv
```

Install dependencies:
```bash
uv sync --no-dev
```

Copy env.example and fill env variables:
```bash
cp env.example .env
```

## PsiloQA Dataset Generation Pipeline
The **PsiloQA pipeline** automates the construction of a **multilingual, span-level hallucination detection dataset with contexts** — from sampling Wikipedia passages to generating Q&A, producing model hypotheses, annotating hallucinated spans, and filtering the results.

It consists of five sequential stages:
1. **Contexts** — parse random Wikipedia pages as input passages for QA generation.
2. **QA pairs** — generate questions and answers of varying complexity using an OpenAI model.
3. **LLM hypotheses** — produce candidate model answers for evaluation.
4. **Annotation** — mark hallucinated spans in model hypotheses using an OpenAI-based annotator.
5. **Filtering** — automatically clean data via heuristic and LLM-based filters.

Each stage can be run individually, or you can execute the full pipeline with a single command:

```bash
uv run psilo dataset pipeline --num-pages 10 --language ru --language en --limit 100 --model Qwen/Qwen2.5-3B-Instruct
```

All API keys and model settings are managed via the `.env` file (`QA_GENERATOR_`, `ANNOTATOR_`, and `FILTER_` prefixes).

### Contexts
The first step in PsiloQA pipeline is getting contexts for QA generation. You can use your own, or, as in out paper, parse random pages from Wikipedia as input contexts. Just run the following command with languages you need. If no `--language` list specified, it will parse random pages for 14 languages presented in our paper. `--num-pages` determines how many contexts to parse from Wikipedia.
```bash
uv run psilo dataset get_contexts --num-pages 10 --language ru --language en
```

### QA pairs
Next step is question and answer generation for the obtained contexts. The script generates three questions of different complexity based on provided contexts. Fill `QA_GENERATOR` settings in `.env` file to use this script. By default, `gpt-4o` is used. Feel free to use another models by providing another model name through `QA_GENERATOR` setting in `.env`.
```bash
uv run psilo dataset generate_qa
```

### LLM hypotheses
All available models are listed in `psilo/dataset/answer_generator/models`. You can add any new Hugging Face model by implementing a runner class that inherits from either:
- `RunnerWithChatTemplate` — if the tokenizer supports chat templates, or
- `RunnerWithCustomTemplate` — if it does not.
Some models require a Hugging Face access token. Make sure to provide `HF_TOKEN` in your `.env` file — models that need it will be skipped if the token is missing.
```bash
uv run psilo dataset generate_hypotheses
```

### Hypotheses annotation
Annotate hypotheses (fill `ANNOTATOR_OPENAI_API_KEY` variable in .env):
```bash
uv run psilo dataset annotate_hypotheses
```

### Filtering
The annotation process includes two filtering stages. Heuristic-based filters ensure structural correctness — they verify that all opening tags have corresponding closing tags, that there are no nested tags, and perform other automated pre-checks. LLM-based filters remove samples with subjective or incomplete questions, as well as cases where the model refuses to answer. For LLM-based filter, fill `FILTER_OPENAI_API_KEY` variable in .env
```bash
uv run psilo dataset filter
```

# Structure
An example of the data:
```json
{
  "id": "psiloqa_togethercomputer/Pythia-Chat-Base-7B-v0.16_13830",
  "lang": "en",
  "wiki_title": "Kyoto Animation",
  "wiki_url": "https://en.wikipedia.org/wiki/Kyoto%20Animation",
  "llm_checkpoint": "togethercomputer/Pythia-Chat-Base-7B-v0.16",
  "wiki_passage": "Kyoto Animation Co., Ltd. (Japanese: 株式会社京都アニメーション, Hepburn: Kabushiki-gaisha Kyōto Animēshon), often abbreviated KyoAni (京アニ, Kyōani), is a Japanese animation studio and light novel publisher located in Uji, Kyoto Prefecture. It was founded in 1985 by husband and wife Hideaki and Yoko Hatta, who remain its president and vice-president respectively. Kyoto Animation has produced anime films and series including The Melancholy of Haruhi Suzumiya (2006), Clannad (2007), K-On! (2009), Nichijou (2011), Free! (2013), Sound! Euphonium (2015), A Silent Voice (2016), and Violet Evergarden (2018).",
  "question": "Name three anime titles produced by Kyoto Animation.",
  "golden_answer": "The Melancholy of Haruhi Suzumiya, Clannad, K-On!",
  "llm_answer": "Three anime titles produced by Kyoto Animation are: 1. Blue Spring 2. Clannad 3. Air",
  "annotated_span": "Three anime titles produced by Kyoto Animation are: 1. [HAL]Blue Spring[/HAL] 2. Clannad 3. [HAL]Air[/HAL]",
  "complexity": "hard",
  "labels": [[55, 66], [81, 84]]
}
```

Fields description:
1. `id` – a unique identificator of a sample
2. `lang` – language of a QA pair
3. `wiki_title` – a title of Wikipedia page used for QA pair generation
4. `wiki_url` – a link to the Wikipedia page used for QA pair generation
5. `llm_checkpoint` – an LLM id from HuggingFace Hub used for hypothesis generation
6. `wiki_passage` – a parsed text of a Wikipedia passage
7. `question` – a question generated by `GPT-4o` for this `wiki_passage`
8. `golden_answer` – an answer generated by `GPT-4o` for the `question`
9. `llm_answer` – a hypothesis produced by LLM
10. `annotated_span` – a span-level annotation of inconsistencies between `llm_answer` and `wiki_passage` generated by `GPT-4o`
11. `complexity` – a complexity of the QA pair generated by `GPT-4o`
12. `labels` – a character-level spans of inconsistencies converted from `annotated_span`

# Baselines
We evaluated various methods (both based on Uncertainty Quantification and based on retrieved information) in a few-shot and SFT setting on PsiloQA testing part. IoU is given as evaluation metric.
| **Method** | **Mode** | **ar** | **ca** | **cs** | **de** | **en** | **es** | **eu** | **fa** | **fi** | **fr** | **hi** | **it** | **sv** | **zh** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MSP | -- | 35.70 | 28.36 | 33.68 | 30.03 | 45.69 | 33.72 | 33.04 | 22.13 | 53.13 | 37.67 | 43.45 | 31.61 | 26.96 | 28.42 |
| CCP | -- | 35.70 | 28.37 | 33.68 | 33.25 | 45.69 | 33.72 | 33.04 | 22.13 | 53.13 | 37.67 | 43.45 | 32.20 | 26.96 | 27.39 |
| Focus | -- | 36.93 | 28.37 | 33.68 | 32.05 | 45.69 | 42.24 | 34.65 | 29.94 | 53.13 | 39.26 | 43.45 | 32.20 | 36.15 | 27.83 |
| lettuce-detect-base | -- | 37.81 | 44.37 | 30.08 | 30.31 | 43.28 | 40.08 | 33.35 | 32.45 | 56.44 | 35.60 | 16.95 | 34.97 | 49.11 | 35.94 |
| ModernBERT-base | SFT | 55.27 | 65.70 | 44.73 | 46.27 | 68.23 | 61.69 | **50.43** | 68.63 | 64.68 | 53.90 | 54.15 | 62.75 | **67.09** | 56.95 |
| mmBERT-base | SFT | **58.10** | **67.01** | **48.81** | **54.97** | **70.67** | **66.18** | 50.27 | **76.61** | **68.16** | **56.38** | 61.19 | **66.57** | 66.24 | 61.58 |
| FActScore (GPT-4o) | -- | 20.75 | 28.99 | 10.44 | 26.68 | 25.84 | 28.54 | 19.68 | 26.62 | 28.16 | 10.21 | 21.03 | 43.92 | 19.25 | 25.18 |
| Qwen2.5-32B-it | 3-shot | 35.54 | 51.71 | 46.83 | 23.57 | 39.98 | 40.51 | 36.52 | 19.18 | 34.69 | 31.92 | 44.56 | 37.95 | 50.89 | 42.77 |

# Considerations for Using the Data
## Limitations
While PsiloQA presents significant advancements in span-level hallucination detection across languages, several limitations remain: 
- **Annotation Source Bias**: PsiloQA relies exclusively on GPT-4o for both generating question–answer pairs and annotating hallucination spans. This introduces potential bias in annotation and generation patterns, as the judgment of a single model may not reflect broader consensus or generalize well across diverse use cases. This bias could be substantially mitigated by using an ensemble of annotators composed of several state-of-the-art models with span averaging. We consider this a promising direction for future work. 
- **Task Narrowness**: The current version of PsiloQA is limited to the question-answering (QA) task. While QA is a strong proxy for factual reasoning, other generative tasks such as summarization, dialogue, and data-to-text generation also suffer from hallucinations and warrant similar treatment.
- **Hallucination Type Coverage**: Unlike datasets that inject controlled hallucination types (e.g., FAVA), PsiloQA does not explicitly cover a diverse taxonomy of hallucinations. The hallucinations in PsiloQA arise naturally from LLM errors in a zero-context setting, which may result in skewed distributions and underrepresentation of certain error types.
- **Language Resource Imbalance**: Despite covering 14 languages, the sample distribution across languages is uneven, and lower-resource languages may suffer from fewer high-quality examples. Additionally, many baselines used for comparison are predominantly trained or optimized for English, potentially underestimating performance in other languages.
- **Dependency on Wikipedia**: Using Wikipedia as the sole source of context limits the topical, stylistic, and cultural diversity of the dataset. While Wikipedia provides clean, factual content across many languages, its coverage is uneven: some languages, cultures, and topics are better represented than others, potentially introducing cultural or regional biases into the dataset. Consequently, models trained on this data may inherit these biases. Moreover, real-world applications often involve noisier or domain-specific data

## Biases
Since both the generation and annotation of PsiloQA rely on GPT-4o, there is an inherent risk of model bias influencing the dataset. Although GPT-4o was among the state-of-the-art models available during dataset development, its judgments may reflect underlying model biases or fail to align with human consensus in edge cases. Furthermore, GPT-4o’s proficiency varies across languages, which may affect the consistency and quality of cross-lingual annotations. Future iterations of PsiloQA may incorporate diverse model perspectives and human-in-the-loop validation to mitigate this concern.

# Citation
```
@misc{rykov2025modelslielearnmultilingual,
      title={When Models Lie, We Learn: Multilingual Span-Level Hallucination Detection with PsiloQA}, 
      author={Elisei Rykov and Kseniia Petrushina and Maksim Savkin and Valerii Olisov and Artem Vazhentsev and Kseniia Titova and Alexander Panchenko and Vasily Konovalov and Julia Belikova},
      year={2025},
      eprint={2510.04849},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.04849}, 
}
```