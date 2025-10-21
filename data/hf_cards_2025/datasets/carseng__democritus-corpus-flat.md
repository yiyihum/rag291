---
pretty_name: Democritus Corpus (Flat)
task_categories:
- text-generation
tags:
- instruction-tuning
- sft
- lora
- peft
- pytorch
- trl
- transformers
---

**Single-file dataset** with **no predefined splits**. Use your training tool (e.g., Atomizer) to create train/validation splits on ingest.

### Schema
- `instruction` *(string)* — the user instruction.
- `context` *(string)* — optional supporting context or source hint.
- `output` *(string)* — the target response.
- `source` *(string, optional)* — provenance (URL/page name).
- `pack` *(string, optional)* — which thematic pack it came from.
- `tags` *(list[str], optional)* — labels for filtering.

**File:** `data.jsonl` — one JSON object per line.
