---
license: apache-2.0
language:
- es
tags:
- wine
- sommelier
- instruction-tuning
- Q&A
- spanish
- fine-tuning
- conversational
task_categories:
- text2text-generation
- conversational
pretty_name: Wine Q&A - Sommelier Style (ES)
size_categories:
- n<1K
---

# Wine Q&A Dataset · Sommelier Style 🍷

Este dataset contiene 100 pares de pregunta-respuesta en español sobre el mundo del vino, redactados con estilo profesional, cercano y claro, al estilo de un sommelier.

## Estructura del dataset

El archivo está en formato `.jsonl`, donde cada línea es un objeto con dos campos:

- `instruction`: la pregunta del usuario.
- `response`: una respuesta experta, clara y contextualizada sobre vinos.

Ejemplo:

```json
{"instruction": "¿Qué vino marida bien con queso azul?", "response": "Un vino dulce como un Oporto o un Tokaji es ideal para equilibrar la intensidad del queso azul."}