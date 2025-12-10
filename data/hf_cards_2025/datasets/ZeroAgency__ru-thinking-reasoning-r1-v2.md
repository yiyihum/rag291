---
license: mit
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: conversation
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 2777732237.2157903
    num_examples: 460638
  download_size: 1046664607
  dataset_size: 2777732237.2157903
task_categories:
- text-generation
language:
- ru
tags:
- chat
- instruct
- conversational
- thinking
- cot
- reasoning
- reflection
- r1
size_categories:
- 100M<n<1B
---

This is a modified version of [ZeroAgency/ru-thinking-reasoning-r1](https://huggingface.co/datasets/ZeroAgency/ru-thinking-reasoning-r1) with addition of `Egor-AI/CoT-XLang` dataset.

Combined dataset of mostly Russian thinking/reasoning/reflection dialogs in form of conversation suitable for LLM fine-tuning scenarios. All responses are mapped to same format.

The format of reasoning in most cases is:
```
<think>
Reasoning...
</think>
Response
```
For reflection dataset - there can be also `<reflection>` tags inside `<think>`.

Common system prompt for think:
```
Ты полезный ассистент. Отвечай на вопросы, сохраняя следующую структуру: <think> Твои мысли и рассуждения </think> 
Твой конечный ответ 
```

Common system prompt for reflection:
```
Вы - система искусственного интеллекта мирового класса, способная к сложным рассуждениям и рефлексии. Вы отвечаете на все вопросы следующим образом-
<think>
В этом разделе вы понимаете проблему и разрабатываете план для её решения.

Для простых проблем-
Составьте простой план и используйте COT

Для проблем средней и высокой сложности-
1. Разработайте пошаговый план для решения проблемы. (не начинайте решать, просто составьте план)
2. Используйте рассуждение Chain of Thought, чтобы проработать план и написать полное решение в рамках think.

Вы можете использовать теги <reflection> </reflection> всякий раз, когда выполняете сложный шаг, чтобы проверить, правильны ли ваши рассуждения, и если нет, исправить их.


</think>


В этом разделе предоставьте полный ответ для пользователя на основе вашего мыслительного процесса. Не ссылайтесь на тег think. Включите всю соответствующую информацию и сделайте ответ достаточно подробным, пользователь не увидит, что находится в теге think.
```

Total samples: 460638

Datasets used:
- attn-signs/russian-reasoning
- kristaller486/Nebo-T1-Russian
- Vikhrmodels/reasoning-0.01-ru
- lightblue/reasoning-multilingual-R1-Llama-70B-train
- d0rj/reflection-v1-ru_subset
- Egor-AI/CoT-XLang