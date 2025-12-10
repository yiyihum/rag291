---
dataset_info:
  features:
  - name: question
    dtype: string
  - name: raw_answer
    dtype: string
  - name: cot
    dtype: string
  - name: answer
    dtype: string
  - name: old_thoughts
    dtype: string
  - name: old_index
    dtype: int64
  splits:
  - name: train
    num_bytes: 76178373
    num_examples: 6288
  download_size: 33945559
  dataset_size: 76178373
  task_categories:
  - text-generation
  - question-answering
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- ru
tags:
- medical
- question-answering
- chain-of-thought
- instruction-tuning
- llm
pretty_name: Russian CoT Dataset
---

# Mykes/medical_cot_rus

Набор данных на русском языке для обучения и оценки моделей в медицинском домене с поддержкой цепочек рассуждений (Chain-of-Thought, CoT). Подходит для задач медицинского вопросо-ответа, дообучения LLM и экспериментов с объяснимостью.

- Объем: ≈ 6.29k записей
- Язык: русский
- Домены: клинические вопросы, симптомы, интерпретация, дифференциальная диагностика и др.
- Поля: question, raw_answer, cot, answer, old_thoughts

⚠️ Отказ от ответственности: датасет предназначен исключительно для исследовательских и образовательных целей. Не используйте его для постановки диагнозов, назначения лечения или любых клинических решений.

---

## Быстрый старт

```python
from datasets import load_dataset

ds = load_dataset("Mykes/medical_cot_rus")
print(ds)
print(ds["train"][0])  # пример записи
```

---

## Структура данных

Каждая запись содержит:

- question (str): Вопрос на медицинную тему.
- raw_answer (str): Краткий/неполный ответ или наметки ответа.
- cot (str): Цепочка рассуждений (промежуточные рассуждения, логика).
- answer (str): Полный, связный и подробный ответ.
- old_thoughts (str): Предыдущие «мысли»/наброски, признанные недостаточно качественными.

Пример структуры (сокращенно, без раскрытия CoT):
```json
{
  "question": "Пациент жалуется на ... Какие возможные причины?",
  "raw_answer": "Вероятно ...",
  "cot": "[скрыто в карточке: цепочка рассуждений доступна в самом датасете]",
  "answer": "Подробный разбор причин, диф.диагностика, обоснование.",
  "old_thoughts": "Черновые рассуждения устаревшего качества."
}
```

Сплиты:
- train: ~6.29k

Примечания по качеству полей:
- raw_answer и old_thoughts могут содержать неполные/шероховатые формулировки.
- cot — предназначен для обучения моделей объяснимому решению, может быть детальным и длинным.
- answer — основной эталон для ответы-ориентированных задач.

---

## Поддерживаемые задачи

- Медицинский вопросо-ответ (closed/open-domain QA)
- Дообучение LLM с использованием:
  - Supervised Fine-Tuning (SFT) по answer
  - SFT/Teacher-Student с учетом cot (например, дистилляция рассуждений)
- Оценка объяснимости и пошаговой логики
- Создание RAG-пайплайнов (answer как целевой, cot для верификации рассуждений)

---

## Рекомендации по использованию

Варианты обучения:
- Только ответы: использовать question -> answer для SFT, избегая генерации CoT на инференсе.
- С рассуждениями: использовать question -> cot + answer для обучения пошаговым решениям.
- Дистилляция рассуждений: обучать модель давать краткие обоснования вместо подробных CoT (например, «brief justification»), если нужно ограничить утечку рассуждений в проде.

Безопасность:
- В продакшене рекомендуются фильтры безопасности и системные подсказки, объясняющие, что ответы не являются медицинской консультацией.
- Добавьте валидацию источников (RAG) и/или проверку фактов для ответов клинического характера.

---

## Статистика и качество

- Количество записей: ≈ 6.29k
- Средняя длина полей может варьировать; cot обычно длиннее answer и raw_answer.
- Возможны дубликаты, вариативность стиля и уровня детализации; при необходимости применяйте нормализацию/фильтрацию.

Идеи для препроцессинга:
- Удаление дубликатов по question или по паре (question, answer)
- Нормализация пунктуации/регистров
- Ограничение длины cot при обучении малых моделей
- Фильтрация по качеству old_thoughts, если используете это поле

---

## Ограничения

- Медицинский контент может содержать неточности или устаревшую информацию.
- Стиль и полнота ответа могут различаться.
- Цепочки рассуждений не гарантируют корректности; они отражают гипотезы/логические переходы, а не клинические протоколы.

---

## Этические и юридические аспекты

- Не используйте датасет для медицинских решений, диагностики, назначения лечения.
- Проверяйте соблюдение требований к приватности и отсутствие персональных данных при дальнейшей переработке.
- При публикации моделей, обученных на наборе, добавляйте четкий дисклеймер о не-медицинской природе ответов.

---

## Бейзлайны и примеры

SFT по answer:
```python
from datasets import load_dataset
from transformers import AutoTokenizer

ds = load_dataset("Mykes/medical_cot_rus")["train"]
tok = AutoTokenizer.from_pretrained("ai-forever/ruGPT-3.5-13B")  # пример; выберите свою модель

def format_example(ex):
    prompt = f"Вопрос: {ex['question']}\nОтвет:"
    target = ex["answer"]
    return tok(prompt, text_target=target, truncation=True)

tok_ds = ds.map(format_example, remove_columns=ds.column_names)
```

SFT с CoT (используйте осторожно, учитывайте требования к разглашению рассуждений):
```python
def format_cot_example(ex):
    prompt = f"Вопрос: {ex['question']}\nПоясни рассуждения и дай ответ."
    target = f"{ex['cot']}\n\nИтоговый ответ: {ex['answer']}"
    return tok(prompt, text_target=target, truncation=True)

tok_ds_cot = ds.map(format_cot_example, remove_columns=ds.column_names)
```

---

## Версии и изменения

- v1.0: первая публикация, ~6.29k записей, поля: question, raw_answer, cot, answer, old_thoughts.

---

## Лицензия

- license: other
- Пожалуйста, уточните и обновите лицензию в репозитории (например, MIT/Apache-2.0/CC-BY-4.0 или иная), чтобы упростить использование в академических и коммерческих целях.

---

## Как цитировать

Если вы используете этот датасет в исследовании или продукте, добавьте ссылку на репозиторий:
- Hugging Face: https://huggingface.co/datasets/Mykes/medical_cot_rus

Пример BibTeX (адаптируйте при наличии публикации):
```
@misc{mykes_medical_cot_rus,
  title        = {Mykes/medical\_cot\_rus: Russian medical QA with Chain-of-Thought},
  author       = {Mykes},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/datasets/Mykes/medical_cot_rus}},
  note         = {~6.29k samples, fields: question, raw\_answer, cot, answer, old\_thoughts}
}
```

---

## Обратная связь и контакты

- Issues и предложения: создавайте в разделе “Issues” репозитория на Hugging Face.
- Будем рады PR с:
  - улучшениями карточки,
  - метаданными о лицензии,
  - скриптами для бейзлайнов и валидации качества.

🩺 Удачных экспериментов и безопасных приложений!