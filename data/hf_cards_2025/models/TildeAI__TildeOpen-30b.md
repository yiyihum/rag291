---
license: cc-by-4.0
language:
- en
- de
- fr
- pl
- ru
- it
- pt
- cs
- nl
- es
- fi
- tr
- hu
- bg
- uk
- bs
- hr
- da
- et
- lt
- ro
- sk
- sl
- sv
- 'no'
- lv
- sr
- sq
- mk
- is
- mt
- ga
datasets:
- HPLT/HPLT2.0_cleaned
- HPLT/hplt_monolingual_v1_2
- HuggingFaceFW/fineweb-2
- allenai/MADLAD-400
- uonlp/CulturaX
- bigcode/the-stack
- common-pile/arxiv_papers
library_name: transformers
---
**Developed by:**  [Tilde.ai](https://tilde.ai/tildeopen-llm/)   
**Funded by:**  European Commission via [EuroHPC JU Large AI Grand Challenge](https://www.eurohpc-ju.europa.eu/winners-announced-large-ai-grand-challenge-2024-06-26_en)   
**Model type:**  A 30B parameter dense decoder-only transformer   
**Languages:**  Albanian, Bosnian, Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Hungarian, Icelandic, Irish, Italian, Latgalian, Latvian, Lithuanian, Macedonian, Maltese, Montenegrin, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovene, Spanish, Swedish, Turkish, Ukrainian as well as mathematical proofs, programming code and XML documents containing translation data   
**License:**  CC-BY-4.0   


## Mission statement 
TildeOpen LLM is an open-source foundational (base) language model built to serve underrepresented Nordic and Eastern European languages. Developed with European Commission funding and trained on the LUMI supercomputer, this 30B+ parameter model addresses the performance gaps that speakers of 19 focus languages—representing over 165 million people—face with existing AI systems.   
The model employs an equitable tokeniser and curriculum-learning approach to ensure fair representation across less-resourced languages, moving beyond the typical English-centric design of most language models. As an open-source project, TildeOpen LLM enables transparent research and community-driven development while maintaining European technological independence.   
This foundational model is not yet adapted to follow instructions or aligned with safety features. The next version being built on top of this model will be a specialised translation model, leveraging TildeOpen LLM's multilingual foundation to provide high-quality translation capabilities across the supported European language pairs.   

## Model training details 
We train TildeOpen LLM using the [Tilde's branch](https://github.com/tilde-nlp/llm-gpt-neox) of [EleutherAI's](https://www.eleuther.ai/) open-source GPT-NeoX framework on LUMI supercomputer's 768 AMD MI250X GPUs. The foundational model training involves 450,000 updates with a constant batch size of 4,718,592 tokens, using a constant learning rate followed by a cooldown phase across 2 trillion tokens. Training consists of three distinct data sampling phases. First, all languages are sampled uniformly to ensure equal representation. Second, languages are sampled according to their natural distribution to ensure that the model sees as much data from languages with larger speaker bases as possible. Finally, we return to uniform sampling across all languages. This three-phase approach ensures TildeOpen LLM develops balanced multilingual capabilities while maintaining strong performance across all target languages, particularly the underrepresented European languages.   

## Model Hyper-Parameters 

| Parameter | Value | 
|-----------|-------| 
| Sequence Length | 8192 | 
| Number of Layers | 60 | 
| Embedding Size | 6144 | 
| FFN Hidden Size | 21504 | 
| Number of Heads | 48 | 
| Number of KV Heads (GQA) | 8 | 
| Activation Function | SwiGLU | 
| Position Encodings | RoPE | 
| Layer Norm | RMSNorm | 
| Embedding Parameters | 8.05E+08 | 
| LM Head Parameters | 8.05E+08 | 
| Non-embedding Parameters | 2.91E+10 | 
| Total Parameters | 3.07E+10 | 

## Tokeniser details 
We built the TildeOpen LLM tokeniser to ensure equitable language representation across languages. Technically, we trained the tokeniser to represent the same text regardless of the language it is written in, using a similar number of tokens. In practice, TildeOpen LLM will be more efficient and faster than other models for our focus languages, as writing out answers will require fewer steps. For more details on how TildeOpen LLM compares against other models, see **[TILDE Bench](https://tilde-nlp.github.io/tokenizer-bench.html)**! 


## Running model using HF transformers
When loading the tokeniser, you must set ```use_fast=False```.
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer + model
tokenizer = AutoTokenizer.from_pretrained("TildeAI/TildeOpen-30b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    "TildeAI/TildeOpen-30b",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Tokenize
inputs = tokenizer(user_in, return_tensors="pt").to(model.device)

# Generate (greedy, deterministic)
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    repetition_penalty=1.2,
    do_sample=False,
)
```
# Evaluation
## Belebele Benchmark: Reading Comprehension
**What is Belebele Benchmark?** [Belebele](https://aclanthology.org/anthology-files/anthology-files/pdf/acl/2024.acl-long.44.pdf) is a multiple-choice machine reading comprehension (MRC) dataset spanning 122 language variants. This dataset enables the evaluation of mono- and multi-lingual models in high-, medium-, and low-resource languages. Each question has four multiple-choice answers and is linked to a short passage from the FLORES-200 dataset. The human annotation procedure was carefully curated to create questions that discriminate between different levels of generalizable language comprehension and is reinforced by extensive quality checks.
Results

**Why does this Matter?** Belebele tests LLM's ability to provide answers based on a given text -- a standard use case in retrieval augumented generation workflows. 

**What did we do?** We used the standard implementation of the [belebele](https://github.com/eleutherai/lm-evaluation-harness/tree/main/lm_eval/tasks/belebele) task from the LLM Evaluation Harness. We set tokenisers to ```use_fast=False```. We report **5-shot** accuracy.

| 5-shot | **Gemma 2 27b** | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b** |
|----------|:-------------:|:----------:|:------------:|:-------------------:|
| Bulgarian | 79.8% | 78.8% | **85.3%** | 84.7% |
| Czech | 81.4% | 78.3% |  85.3% | **85.8%** |
| German | 81.2% | 80.6% | **85.0%** | 84.3% |
| English | **88.9%** | 83.0%  | 87.6% | 88.3% |
| Estonian | 72.1% | 73.7% | 82.0% | **82.6%** |
| Finnish | 79.0% | 78.1% | 84.3% | **85.0%** |
| French | 82.6% | 80.1%  | **85.7%** | 85.0% |
| Hungarian | 77.9% | 76.2% | 83.3% | **86.2%** |
| Icelandic | 70.8% | 58.2%  | 54.3% | **85.7%** |
| Italian | 82.1% | 77.8% | 81.0% | **82.4%** |
| Lithuanian | 76.1% | 76.1% | **85.2%** | 83.3% |
| Latvian | 78.4% | 77.7%  | **84.6%** | **84.6%** |
| Dutch | 80.2% | 78.9% | 83.2% | **85.0%** |
| Polish | 78.3% | 77.9%  | 82.2% | **83.0%** |
| Portuguese | 83.8% | 80.1%  | 86.1% | **87.1%** |
| Romanian | 80.3% | 78.8%  | 85.3% | **85.9%** |
| Russian | 79.4% | 79.4% | 84.2% | **84.6%** |
| Slovak | 78.9% | 78.0% | 84.1% | **85.0%** |
| Slovenian | 78.0% | 80.0%  | 83.7% | **85.1%** |
| Spanish | 82.1% | 78.4% | **84.1%** | 83.8% |
| Serbian | 79.8% | 78.4% | 74.1% | **84.2%** |
| Swedish | 80.6% | 76.3% | **85.3%** | 84.4% |
| Turkish | 77.4% | 62.3% | 79.9% | **82.7%** |
| Ukrainian | 78.0% | 77.0% | 83.9% | **85.1%** |
| **Average** | 79.5% | 76.8% | 82.5% | **84.7%** |

## MultiBLiMP Benchmark: Grammar Test
**What is MultiBLiMP?** [MultiBLiMP](https://arxiv.org/pdf/2504.02768) is a massively multilingual test of core grammar. It gives models pairs of almost-identical sentences—one grammatical and one ungrammatical—and asks whether the model assigns a higher probability to the correct one. Version 1.0 covers 101 languages

**Why does this Matter?** MultiBLiMP tests models' ability to distinguish correct and erroneous language. Just like humans, producing mostly correct language is not a big achievement. Rather, it is very bad to make any mistakes at all. 

**What did we do?** 
We used the standard implementation of the [MultiBLiMP](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/multiblimp) task from the LLM Evaluation Harness. We set tokenisers to ```use_fast=False```. We report **0-shot** accuracy.

| Language | **Gemma 2 27b** | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b**
|----------|-------------|----------|---------------------|-------------|
| Bulgarian | 95.4% | 98.8% | 97.7% | **99.6%** |
| Czech | 98.6% | **98.9%** | 98.5% | 98.5% |
| German | 98.8% | 98.7% | 98.0% | **99.4%** |
| English | 98.4% | 98.7% | 98.7% | **99.4%** |
| Estonian | 92.0% | 95.6% | 95.8% | **98.3%** |
| Finnish | 93.0% | 96.3% | 95.2% | **98.5%** |
| French | 98.2% | 98.8% | 98.7% | **99.3%** |
| Serbo-Croatian | 94.6% | 98.5% | 96.4% | **99.6%** |
| Hungarian | 95.9% | 98.8% | 97.8% | **100.0%** |
| Icelandic | 88.5% | 80.3% | 74.4% | **98.8%** |
| Italian | 96.0% | 96.7% | 96.6% | **98.2%** |
| Latvian | 91.6% | 95.2% | 96.9% | **99.1%** |
| Lithuanian | 95.3% | 99.0% | 99.0% | **99.7%** |
| Dutch | 94.0% | 96.6% | 96.5% | **99.2%** |
| Polish | 97.0% | 97.5% | 97.6% | **99.3%** |
| Portuguese | 96.1% | 97.6% | 97.1% | **98.2%** |
| Romanian | 97.7% | 98.9% | 98.5% | **98.9%** |
| Russian | 94.7% | 96.6% | 97.3% | **99.4%** |
| Slovak | 97.7% | 98.8% | 97.7% | **99.3%** |
| Slovenian | 99.0% | **100.0%** | **100.0%** | 98.8% |
| Spanish | 95.6% | 98.0% | 97.3% | **98.7%** |
| Swedish | 95.8% | 85.1% | 93.8% | **100.0%** |
| Turkish | 97.6% | **98.7%** | 97.9% | 96.4% |
| Ukrainian | 95.6% | 98.0% | 97.3% | **99.2%** |
| **Average** | 95.7% | 96.7% | 96.4% | **99.0%** |

## Knowledge tests

### ARC Benchmark Results
**What is ARC?** [ARC](https://arxiv.org/pdf/1803.05457) - The AI2 Reasoning Challenge is a multiple-choice science question benchmark **in English**, derived from U.S. grade-school standardized exams. It has two subsets — ARC Easy and ARC Challenge — designed to test factual knowledge and common-sense.

**Why does this Matter?** ARC probes a model’s ability to answer non-trivial questions by applying world knowledge. Although the answer can sometimes be inferred from the question, in the classic lm-evaluation-harness ARC implementation the answer choices for each question are **not** provided during inference, thus placing emphasis on world knowledge, rather than on the model's reasoning capabilities.

**What did we do?** 
We use multilingual translations of ARC provided by [Eurolingua](https://huggingface.co/datasets/Eurolingua/arcx); please refer to the [publication](https://arxiv.org/pdf/2410.08928). Other than the data source, we replicate the standard [LM Evaluation Harness configuration for ARC](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/arc). Our exact configuration is available at [TBA]. We set tokenisers to ```use_fast=False```. We report **5-shot** accuracy.

| 5-shot |  | **ARC Easy**| |  | **ARC Challenge**| |
|----------|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| **Language** | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b** | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b** |
| Danish | 79.9% | **80.1%** | 79.6% | 53.4% | 52.6% | **53.7%** |
| German | 79.6% | **79.9%** | 78.0% | 53.4% | **53.6%** | 51.7% |
| Spanish | **82.9%** | 81.7% | 79.4% | **57.3%** | 56.1% | 52.4% |
| French | **81.7%** | 81.1% | 78.6% | **56.0%** | 54.5% | 52.8% |
| Italian | 80.5% | **81.6%** | 78.5% | **56.4%** | 54.8% | 54.1% |
| Dutch | **80.1%** | 80.0% | 78.8% | **54.0%** | 53.8% | 52.2% |
| Portuguese | **81.7%** | 81.1% | 79.0% | **56.9%** | 55.5% | 54.1% |
| Swedish | 80.3% | **80.5%** | 78.7% | 53.8% | 53.1% | **54.1%** |
| **AVG WEST** | **80.8%** | **80.8%** | 78.8% | **55.2%** | 54.2% | 53.1% |
| | | | | | | |
| Bulgarian | **79.8%** | 79.2% | 79.5% | **53.8%** | 51.8% | 52.8% |
| Czech | **79.5%** | **79.5%** | 78.8% | 51.5% | 52.3% | **53.9%** |
| Estonian | 72.4% | 73.0% | **73.1%** | 49.6% | 49.8% | **52.0%** |
| Finnish | 73.8% | **74.2%** | 73.3% | 48.7% | 51.1% | **52.1%** |
| Hungarian | 74.0% | 73.9% | **74.9%** | 49.3% | 49.0% | **49.6%** |
| Lithuanian | 76.4% | 76.1% | **77.9%** | 50.3% | 51.6% | **53.0%** |
| Latvian | 76.2% | **76.4%** | 75.9% | 50.7% | 49.8% | **50.9%** |
| Polish | **79.2%** | 78.2% | 78.0% | **54.5%** | 53.3% | 52.7% |
| Romanian | **79.6%** | 78.8% | 78.8% | **55.5%** | 53.7% | 54.5% |
| Slovak | 78.8% | 79.2% | **79.6%** | 52.5% | 53.0% | **54.7%** |
| Slovenian | **78.3%** | 78.5% | **78.3%** | **53.4%** | 52.2% | 52.7% |
| **AVG EAST** | **77.1%** | 77.0% | **77.1%** | 51.8% | 51.6% | **52.6%** |

### MMLU Benchmark Results
**What is MMLU?** [MMLU](https://arxiv.org/pdf/2009.03300) is a massive multitask test consisting of multiple-choice questions from various branches of knowledge, **in English**. The test spans subjects in the humanities, social sciences, hard sciences, and other areas that are important for some people to learn. This covers 57 tasks including elementary mathematics, US history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem solving ability. Questions are four option multiple choice and assess factual knowledge, reading comprehension, and reasoning across disciplines. The questions can be grouped under four topics - stem, humanities, social_sciences and other, allowing for individual evaluation of each group.

**Why does this Matter?** Similarly to ARC, MMLU measures broad, general purpose factual knowledge and some reasoning capabilites. The possible answer choices are included during prompting, which can allow the model to employ reasoning to discard false answers, rather than just relying on knowing the correct one. It should be noted that some question groups are exclusive to the anglocentric world, e.g. US history or law.

**What did we do?** We use multilingual translations of MMLU provided by [Eurolingua](https://huggingface.co/datasets/Eurolingua/mmlux), please refer to the [publication](https://arxiv.org/pdf/2410.08928). Other than the data source, we replicate the standard [LM Evaluation Harness configuration for MMLU](https://github.com/EleutherAI/lm-evaluation-harness/tree/main/lm_eval/tasks/mmlu/default). Our configuration is available at [TODO]. We set tokenisers to ```use_fast=False```. We report **0-shot** accuracy.

| 0-shot | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b** |
|----------|:-----------------:|:---------------------:|:-------------------:|
| Bulgarian | 48.3% | 52.0% | **56.3%** |
| Czech | 49.1% | 51.7% | **56.4%** |
| Danish | 50.2% | 51.1% | **56.6%** |
| German | 51.0% | 51.8% | **56.2%** |
| Greek | 50.7% | 50.6% | **50.9%** |
| Spanish | 53.3% | 53.4% | **56.3%** |
| Estonian | 48.7% | 49.2% | **55.3%** |
| Finnish | 47.4% | 48.9% | **55.4%** |
| French | 53.1% | 53.8% | **56.4%** |
| Hungarian | 49.9% | 44.4% | **55.2%** |
| Italian | 52.3% | 53.7% | **57.2%** |
| Lithuanian | 47.3% | 49.4% | **54.7%** |
| Latvian | 46.9% | 48.0% | **54.0%** |
| Dutch | 50.8% | 53.0% | **56.5%** |
| Polish | 50.6% | 49.6% | **55.6%** |
| Portuguese | 52.4% | 53.7% | **56.4%** |
| Romanian | 51.0% | 52.1% | **56.2%** |
| Slovak | 49.0% | 52.2% | **56.3%** |
| Slovenian | 48.2% | 50.7% | **55.3%** |
| Swedish | 49.6% | 51.2% | **56.1%** |
| **Average** | 50.0% | 51.0% | **55.7%** |

### National Exams Results
**What are National Exams?** A curated suite of **multlingual** publicly available past questions from national-level standardized exams across multiple countries (e.g., high-school exit and university-entrance exams), please refer to the [publication](https://aclanthology.org/2020.emnlp-main.438.pdf). The dataset is available on HuggingFace [here](https://huggingface.co/datasets/mhardalov/exams). Items are presented in multiple-choice format. 

**Why does this Matter?** Similarly to MMLU, the model is tested on factual knowledge and reasoning capabilites. However, it should be stressed that for each language the bench is **unique** (the exams are different) and available in the **source language** (i.e. not translated). This places emphasis on the model's regional knowledge and eliminates translation noise that is present in many other multilingual benchmarks. Possible answer choices are once again included during inference, allowing for the model to employ reasoning if factual knowledge is lacking.

**What did we do?** [TODO]

| 5-shot | **ALIA 40b** | **EuroLLM Prev. 22b** | **TildeOpen 1.1 30b** |
|----------|----------|-------------------|-------------------|
| Bulgarian | 62.4% | 66.8% | **67.8%** |
| Croatian | 70.8% | **72.5%** | 71.9% |
| Hungarian | 48.9% | **51.9%** | 48.9% |
| Italian | **65.5%** | 64.6% | 65.0% |
| Macedonian | 74.2% | 72.0% | **80.2%** |
| Polish | 61.2% | 61.4% | **63.5%** |
| Portuguese | **61.4%** | 60.9% | 59.2% |
| Albanian | 55.6% | 55.0% | **75.6%** |
| Serbian | 64.7% | 57.3% | **66.9%** |
| **Average** | 62.7% | 62.5% | **66.6%** |