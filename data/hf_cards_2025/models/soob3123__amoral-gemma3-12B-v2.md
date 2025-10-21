---
base_model: google/gemma-3-12b-it
tags:
- text-generation-inference
- transformers
- gemma3
- analytical-tasks
- bias-neutralization
- uncensored
language:
- en
pipeline_tag: text-generation
datasets:
- TheDrummer/AmoralQA-v2
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/62f93f9477b722f1866398c2/eNraUCUocrOhowWdIdtod.png)

> "Neutrality is not indifference. It is engagement with equal intensity."  
> ― J. Robert Oppenheimer *[Lecture on Scientific Ethics, 1957]*

**UGI Leaderboard**
![image/png](https://cdn-uploads.huggingface.co/production/uploads/62f93f9477b722f1866398c2/BUJaj5SIhM2HvRtrF0V47.png)
V2 has improved natural intelligence and marginally lesser refusals, For general purpose, you might not notice much of a difference from V1

**Core Function:**
- Produces analytically neutral responses to sensitive queries
- Maintains factual integrity on controversial subjects
- Avoids value-judgment phrasing patterns

**Response Characteristics:**
- No inherent moral framing ("evil slop" reduction)
- Emotionally neutral tone enforcement
- Epistemic humility protocols (avoids "thrilling", "wonderful", etc.)