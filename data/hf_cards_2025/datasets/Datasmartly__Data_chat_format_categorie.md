---
pretty_name: Data_chat_format_categorie
tags:
- chat
- darija
- english
- translation
- instruction-tuning
task_categories:
- text-to-text
---

# Data_chat_format_categorie

- Format: une ligne = un objet JSON avec `messages` (user/assistant).
- `user.content` = `instruction` en minuscules + ": " + `input`
- `assistant.content` = `output`
- Source: mergeddataset.jsonl
- Script: conversion automatique.
