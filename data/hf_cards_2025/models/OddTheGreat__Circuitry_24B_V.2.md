---
base_model:
- Delta-Vector/Rei-24B-KTO
- zerofata/MS3.2-PaintedFantasy-v2-24B
- TheDrummer/Cydonia-24B-v4.1
library_name: transformers
tags:
- mergekit
- merge
- roleplay
- creative
language:
- en
- ru
---
# Circuitry_24B_V.2

This is a merge of pre-trained language models.

Goal of this merge was to replace Mechanism as my new main rp model.

Model is coherent, and handles bad written or overengineered cards. Creativity is better than in Mechanism model (finally, normal names!), but model remains stable, prose and dialogues are less robotic and distant, more emotional.

Instruction following capabilities are good too, only problem i had spotted is periodic formatting errors.

Good balance at sfw/nsfw, can be positive, neutral or negative depending on prompt.

ERP is not bad.

On RU was tested only as assistant and was good at it.

Tested on 8k context average, 12k and 16k runs didn't showed instability or dramatic quality loss.

Used q4_K_M, Mistral template, instruct on, T1.04, xtc off or 0.1 0.1 (off is better.)