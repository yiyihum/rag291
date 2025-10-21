---
datasets:
- IlyaGusev/saiga_scored
- IlyaGusev/saiga_preferences
- dichspace/darulm
language:
- ru
pipeline_tag: text-generation
license: apache-2.0
base_model: RefalMachine/RuadaptQwen2.5-32B-Pro-Beta
---

## Описание модели

WORK IN PROGRESS!!! Текущая версия v1.

Адаптация модели T-pro-it-1.0 на русский язык. В модели был заменен токенизатор, затем произведено дообучение (Continued pretraining) на русскоязычном корпусе, после чего была применена техника LEP (Learned Embedding Propagation).

Благодаря новому токенизатору (расширенный tiktoken cl100k с помощью униграм токенизатора на 48 т. токенов) скорость генерации* русскоязычных текстов возрасла до 60% по сравнению с исходной моделью T-pro-it-1.0.

*Под скоростью генерации подразумевается количество русскоязычных символов/слов в секунду на одинаковых текстовых последовательностях.

## Попробовать

Модель можно попробовать в поднятом Space (внизу в параметрах выбор модели): 
https://huggingface.co/spaces/RefalMachine/RuadaptQwen2.5

## Токенизация

![image/png](https://cdn-uploads.huggingface.co/production/uploads/652cedbdf120598322ae358a/O4eQEhnowETEatDPcmArB.png)


![image/png](https://cdn-uploads.huggingface.co/production/uploads/652cedbdf120598322ae358a/oW0Q6LzD_Py3GdH0kfqu4.png)

## Метрики и оценка качества

Модель была оценена на Ru-Arena-General, MERA, llmtf_open

#### Результаты на Ru-Arena-General

Замеры были произведены с использованием оффициального кода лидерборда (https://github.com/VikhrModels/ru_llm_arena), **но с repetition_penalty=1.1**.

TODO

#### Результаты на MERA

TODO

#### Результаты на llmtf_open

TODO

## How to cite:

Tikhomirov M., Chernyshov D. Facilitating Large Language Model Russian Adaptation with Learned Embedding Propagation //Journal of Language and Education. – 2024. – Т. 10. – №. 4. – С. 130-145.

Tikhomirov M., Chernyshev D. Impact of Tokenization on LLaMa Russian Adaptation //2023 Ivannikov Ispras Open Conference (ISPRAS). – IEEE, 2023. – С. 163-168.

## Предупреждение

Ответы модели не отражают мнения авторов, а лишь повторяют знания полученные из данных на всех этапах обучения (предобучение, смена токенизатора, обучение на инструкциях, калибровка качества ответов). Модель была получена из сторонней предобученной модели, **контроль за предобучением** которой **не является ответственностью текущих авторов**. При создании данной версии модели не производилось никаких дополнительных действий, направленных на изменение заложенных в LLM "мнений". Используйте с осторожностью.