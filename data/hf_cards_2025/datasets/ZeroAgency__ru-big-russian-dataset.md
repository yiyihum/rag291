---
dataset_info:
  features:
  - name: conversation
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  - name: topic
    dtype: string
  - name: has_reasoning
    dtype: bool
  - name: conversation_length
    dtype: int64
  - name: question
    dtype: string
  - name: id
    dtype: string
  - name: correctness
    dtype: int64
  - name: instruct_following
    dtype: int64
  - name: informativeness
    dtype: int64
  - name: engagement
    dtype: int64
  - name: quality
    dtype: int64
  - name: error_free
    dtype: int64
  - name: rude_ethic
    dtype: int64
  - name: helpful
    dtype: int64
  - name: safety
    dtype: int64
  - name: conciseness
    dtype: int64
  - name: coherence
    dtype: int64
  - name: relevance
    dtype: int64
  - name: overall_score
    dtype: int64
  - name: no_useless_extra
    dtype: int64
  - name: refusal
    dtype: int64
  - name: role_play
    dtype: int64
  - name: pii_leak
    dtype: int64
  - name: reasoning
    dtype: int64
  - name: classified_topic
    dtype: string
  splits:
  - name: train
    num_bytes: 9058052512.664143
    num_examples: 1710601
  - name: test
    num_bytes: 86222720
    num_examples: 18520
  download_size: 4004095067
  dataset_size: 9144275232.664143
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
license: mit
task_categories:
- text-generation
language:
- ru
tags:
- instruct
- conversational
- russian
- math
- physics
- code
pretty_name: Big Russian
size_categories:
- 1B<n<10B
---

# Big Russian Dataset

Made by [ZeroAgency.ru](https://zeroagency.ru/?utm_source=hf) - [telegram channel](https://t.me/ak_segfault).

![image/png](https://huggingface.co/datasets/ZeroAgency/ru-big-russian-dataset/resolve/main/big-russian-dataset-logo.png)

### Dataset size

- Train: 1 710 601 samples (filtered from 2_149_360)
- Test:  18 520 samples (not filtered)

## English

The Big Russian Dataset is a combination of various primarily Russian‑language datasets. With some sort of reasoning!

The dataset was deduplicated, cleaned, scored using gpt-4.1 and filtered.

## Русский

Big Russian Dataset - большой русский датасет. Комбинация из различных датасетов, в которых преобладает русский язык в промтах и ответах. Местами есть ризонинг(ну или попытка в ризонинг).

Датасет был дедуплицирован, очищен, оценен с помощью gpt-4.1 и отфильтрован.

## Filtration condition

```python
return (
    score.refusal < 1 and score.pii_leak < 1 and 
    (score.correctness == -1 or score.correctness >= 5) and
    (score.instruct_following == -1 or score.instruct_following >= 5) and
    (score.informativeness == -1 or score.informativeness >= 5) and
    (score.engagement == -1 or score.engagement >= 4) and
    (score.quality == -1 or score.quality >= 5) and
    (score.error_free == -1 or score.error_free >= 7) and
    (score.rude_ethic == -1 or score.rude_ethic >= 7) and
    (score.helpful == -1 or score.helpful >= 5) and
    (score.safety == -1 or score.safety >= 7) and
    (score.conciseness == -1 or score.conciseness >= 5) and
    (score.coherence == -1 or score.coherence >= 5) and
    (score.relevance == -1 or score.relevance >= 5) and
    (score.no_useless_extra == -1 or score.no_useless_extra >= 5)
)
```

## Mixed system prompts and data format

1. Reasoning responses are in format `<think>Reasoning: ...</think> ...`.
2. In some cases system prompts were replaced or added.
3. Where appropriate, the original system prompt from the sample was used.

System prompts added:
```python
prompts = {
    "generic": "Ты виртуальный ассистент. Ты отвечаешь на вопросы людей, помогаешь им и поддерживаешь. Ты создан, чтобы быть полезным, безобидным и честным. Ты отвечаешь на том языке, на котором был задан вопрос или попросил пользователь.",
    "think": """Ты виртуальный ассистент. Ты отвечаешь на вопросы людей, помогаешь им и поддерживаешь. Ты создан, чтобы быть полезным, безобидным и честным. Ты отвечаешь на том языке, на котором был задан вопрос или попросил пользователь.

Answer in the following format:
<think>Reasoning: ...</think>
...""",
    "task": "Ты виртуальный ассистент. Ты отвечаешь на вопросы людей, помогаешь им и поддерживаешь. Ты создан, чтобы быть полезным, безобидным и честным. Ты отвечаешь на том языке, на котором был задан вопрос или попросил пользователь. Реши задачу по инструкции ниже. Не извиняйся, не строй диалог.",
    "task_think": """Ты виртуальный ассистент. Ты отвечаешь на вопросы людей, помогаешь им и поддерживаешь. Ты создан, чтобы быть полезным, безобидным и честным. Ты отвечаешь на том языке, на котором был задан вопрос или попросил пользователь. Реши задачу по инструкции ниже. Не извиняйся, не строй диалог.

Answer in the following format:
<think>Reasoning: ...</think>
..."""
}
```

## Included datasets

> NOTE: not all samples from these datasets included. Filtration used. You can check for dataset source in 'source' column.

- IlyaGusev/saiga_scored - filtration: `x['is_bad_by_regex'] == False and x["opus_score"] >= 8`
- IlyaGusev/oasst2_ru_main_branch
- attn-signs/kolmogorov-3
- attn-signs/gromov-2 - verifiable subset
- attn-signs/gromov-1
- attn-signs/gromov-0
- attn-signs/russian-easy-instructions
- ai-bond/ru-alpaca-summ - included in both train+test splits
- Vikhrmodels/russian_math
- Vikhrmodels/russian_physics
- Vikhrmodels/sdamgia - only tasks without images
- PyWebSol/ru-slimorca-300k
- PyWebSol/RussianUltrachat100k
- mizinovmv/ru_OpenMathInstruct-2
- dim/grade_school_math_instructions_ru
- attn-signs/russian-reasoning
- kristaller486/Nebo-T1-Russian
- Vikhrmodels/reasoning-0.01-ru - warning: may contain ambiguous reasoning
- lightblue/reasoning-multilingual-R1-Llama-70B-train - Russian language samples only
- d0rj/reflection-v1-ru_subset
- d0rj/orca-math-word-problems-200k-ru
- d0rj/ru-instruct
- ZeroAgency/ru-wildchat-v1
- evilfreelancer/MATH-500-Russian
- dim/ru_instruct_gpt4
- mizinovmv/ru_codefeedback
- Egor-AI/CoT-XLang - Russian subset
- Vikhrmodels/GrandMaster-PRO-MAX - included in both train+test splits

Big kudos to the authors of all these datasets!
