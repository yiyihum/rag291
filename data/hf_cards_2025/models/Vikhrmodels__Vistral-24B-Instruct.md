---
license: apache-2.0
language:
- en
- ru
base_model:
- mistralai/Mistral-Small-3.2-24B-Instruct-2506
library_name: transformers
datasets:
- Vikhrmodels/GrandMaster2
---

## Vistral-24B-Instruct
### Описание

**Vistral** - это наша новая флагманская унимодальная LLM (Large Language Model) представляющая из себя улучшенную версию [mistralai/Mistral-Small-3.2-24B-Instruct-2506](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) командой **VikhrModels**, адаптированную преимущественно для русского и английского языков. Удалён визуальный энкодер, убрана мультимодальность. Сохранена стандартная архитектура "MistralForCausalLM" без изменений в базовой структуре модели.

Весь использованный код для обучения доступен в нашем репозитории [effective_llm_alignment](https://github.com/VikhrModels/effective_llm_alignment/) на GitHub, а основные датасеты доступны в нашем [профиле на HF](https://huggingface.co/Vikhrmodels).

Модель доступна на нашем сайте [Chat Vikhr](https://chat.vikhr.org)

## Quantized variants:

- GGUF [Vikhrmodels/Vistral-24B-Instruct-GGUF](https://huggingface.co/Vikhrmodels/Vistral-24B-Instruct-GGUF)
- MLX
  - 4 bit [Vikhrmodels/Vistral-24B-Instruct-MLX_4bit](https://huggingface.co/Vikhrmodels/Vistral-24B-Instruct-MLX_4bit)
  - 8 bit [Vikhrmodels/Vistral-24B-Instruct-MLX_8bit](https://huggingface.co/Vikhrmodels/Vistral-24B-Instruct-MLX_8bit)


### Метрики и оценка качества

Модель оценивалась на нашем русскоязычном open-source SbS бенчмарке [ru-arena-general](https://github.com/VikhrModels/ru_llm_arena)



#### Результаты на Ru-Arena-General

| Model Name                                       | Winrate  | 95% CI             | Average # Tokens |
|--------------------------------------------------|--------|--------------------|------------------|
| **Vistral-24B-Instruct**               | **96.1**   | (-0.7, 0.8)        | 647              |
| Mistral-Small-3.2-24B-Instruct-2506                        | 92.1   | (-0.9, 1.0)        | 486              |
| vikhr-nemo-12b-instruct-r-21-09-24(180 leaked)               | 79.8   | (-2.2, 1.9)        | 627              |



#### Пример правильного использования с OpenAI-like API

Запуск vLLM сервера: `vllm serve --dtype half --max-model-len 32000 -tp 1 Vikhrmodels/Vistral-24B-Instruct --api-key token-abc123`

```python
from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123",
)

llm_model = "Vikhrmodels/Vistral-24B-Instruct"

sample_history = [
    {'role': 'user', 'content': 'Напиши краткое описание книги Гарри Поттер.'}
]

final_answer = llm_client.chat.completions.create(
    model=llm_model,
    messages=sample_history,
    temperature=0.3,
    max_tokens=2048
).choices[0].message.content

print(final_answer)
```

Ответ после выполнения кода будет выглядеть примерно так:

    **Краткое описание книги «Гарри Поттер»:**  

    «Гарри Поттер» — это серия фантастических романов Дж. К. Роулинг о мальчике-волшебнике, который узнаёт, что он сын могущественных магов, и отправляется учиться в школу чародейства и волшебства Хогвартс. В первом томе («Гарри Поттер и философский камень») Гарри знакомится с друзьями Роном и Гермионой, раскрывает тайну своего прошлого и сталкивается с опасным тёмным магом Волан-де-Мортом.  
    
    В последующих книгах Гарри и его друзья борются с силами зла, раскрывают древние тайны, переживают взросление и учатся использовать волшебство во благо. Серия сочетает приключения, дружбу, магию и борьбу добра со злом.  
    
    **Основные темы:** волшебный мир, дружба, храбрость, преданность, борьба со злом.


### Нюансы и ограничения
- Модель имеет **низкий уровень безопасности ответов** и нацелена на правильное и полное выполенние инструкций, имейте это ввиду при использовании и тестируйте самостоятельно. Частично это исправляется системными промптами и дополнительными указаниями о важности безопасности в промпте пользователя.
- Системные промпты не предназначены для описание персонажей, мы рекомендуем использовать их для спецификации стиля ответа (вроде "answer only in json format"). Кроме того, желательно, писать их **на английском языке**, так как так было в датасете, от использования английского в системных промтпах не зависит язык ответа.
- Модель лучше использовать с низкой темптературой (0.1-0.5), а таже использовать top_k (30-50), при температуре 1.0 были замечены случайные дефекты генерации.

### Авторы
- Nikolay Kompanets, [LakoMoor](https://t.me/lakomoordev), [Vikhr Team](https://t.me/vikhrlabs)
- Sergei Bratchikov, [NLP Wanderer](https://t.me/nlpwanderer), [Vikhr Team](https://t.me/vikhrlabs)
- Konstantin Korolev, [Vikhr Team](https://t.me/vikhrlabs)
- Aleksandr Nikolich, [Vikhr Team](https://t.me/vikhrlabs)

```
@inproceedings{nikolich2024vikhr,
  title={Vikhr: Advancing Open-Source Bilingual Instruction-Following Large Language Models for Russian and English},
  author={Aleksandr Nikolich and Konstantin Korolev and Sergei Bratchikov and Nikolay Kompanets and Igor Kiselev and Artem Shelmanov},
  booktitle={Proceedings of the 4th Workshop on Multilingual Representation Learning (MRL) @ EMNLP-2024},
  year={2024},
  publisher={Association for Computational Linguistics},
  url={https://arxiv.org/pdf/2405.13929}
}
```