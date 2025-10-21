---
license: apache-2.0
tags:
- fine-tuning
- chat
- assistant
- conversational
- tool-calls
---

# CrowdMind / blueberry

**Blueberry** is a fine-tuning dataset for building helpful, grounded, and tool-aware AI assistants.  
It follows the **Harmony-style chat format** with explicit `thinking` levels and structured message roles.

- **Author**: Dustin Loring  
- **Date**: 2025-09-15  

---

## Motivation

Modern language models often **hallucinate** or refuse instructions.  
This dataset aims to reduce those issues by:

- Providing **uncensored**, **direction-following** examples.  
- Including **tool-call workflows** (e.g., `python`, `web.run`, `image_gen`) for coding and reasoning tasks.  
- Labeling each example with a **thinking level** (`none`, `low`, `med`, `high`) to train adaptive reasoning depth.  
- Covering both **static knowledge** and **dynamic lookups** via tools.

---

## Dataset structure

### Splits
- **Train**: 100+ examples (including 50+ tool-call tasks, coding, math, reasoning)  
- **Validation**: 10 examples  
- **Test**: 10 examples  

Splits are deterministic (seed = 42) and balanced to cover reasoning levels and tool use.

### Format
Each example is a JSON object in `.jsonl` format with fields:

- `id`: example identifier  
- `thinking`: `"none"`, `"low"`, `"med"`, `"high"`  
- `messages`: list of structured messages  

Each `message` has:
- `role`: `system`, `developer`, `user`, `assistant`, `tool`, or `tool_result`  
- `content`: string (the message text)  

Example:

```json
{
  "id": "tool004",
  "thinking": "high",
  "messages": [
    {"role":"system","content":"You are Blueberry, a helpful assistant trained by Dustin Loring."},
    {"role":"developer","content":"Use Python tool when calculations needed."},
    {"role":"user","content":"Compute the factorial of 10."},
    {"role":"assistant","content":"I’ll compute using Python."},
    {"role":"tool","name":"python","content":"import math\nmath.factorial(10)"},
    {"role":"tool_result","content":"3628800"},
    {"role":"assistant","content":"10! = **3,628,800**."}
  ]
}
