---
license: llama3.2
language: en
base_model: meta-llama/Llama-3.2-1B-Instruct
pipeline_tag: text-generation
tags:
- pii-redaction
- privacy
- slm
- distil-labs
---

# Distil-PII-Llama-3.2-1B-Instruct

A **small language model** (SLM) fine-tuned by Distil Labs for **policy-aware PII redaction** that outputs a single JSON object with `redacted_text` and `entities`. Optimized to run locally with strong accuracy and strict schema adherence.

## Model Details

* **Developed by:** Distil Labs GmbH
* **License:** Llama 3.2 Community License Agreement
* **Finetuned from:** `meta-llama/Llama-3.2-1B-Instruct`

## Intended Use & Limitations

* **Use cases:** Redacting support chats, logs, tickets, transcripts—removing identity while preserving ops signals (IDs last-4, order numbers, etc.).
* **Out of scope:** Legal or compliance advice; languages beyond English (generalization not guaranteed); domain-specific IDs unseen in training.

## Input & Output

**Input:** A plain-text prompt with task instruction + context.
**Output (JSON only):**

```json
{
  "redacted_text": "Text with in-place tokens",
  "entities": [
    {"value": "<original>", "replacement_token": "[TOKEN]", "reason": "<why>"}
  ]
}
```

**Tokens:** `[PERSON] [EMAIL] [PHONE] [ADDRESS] [SSN] [ID] [UUID] [CARD_LAST4:####] [IBAN_LAST4:####] [GENDER] [AGE] [RACE] [MARITAL_STATUS]`

## Training

Instruction-tuned on a compact policy spec + ~20 curated examples emphasizing **exact JSON schema**, **minimal in-place edits**, and **entity correctness**.

## Evaluation

Judged by a frontier LLM using a deterministic rubric: JSON-only, schema validity, **redacted_text exact match**, and **set-equality** of `(value, replacement_token)` pairs (reason/order ignored). Score: **0.82 ± 0.03**.

## How to Use
Details of deployment can be found in [docs](https://docs.distillabs.ai/how-to/model-deployment). Deploy the model using vllm or ollama (-gguf version available in this collection) and use the following snippet to get results
```python
SYSTEM_PROMPT = """
You are a problem solving model working on task_description XML block:
<task_description>
Produce a redacted version of texts, removing sensitive personal data while preserving operational signals. The model must return a single json blob with:

* **redacted_text** is the input with minimal, in-place replacements of redacted entities.
* **entities** as an array of objects with exactly three fields {value: original_value, replacement_token: replacement, reason: reasoning}.

## What to redact (→ replacement token)

* **PERSON** — customer/patient/person names (first/last/full; identifying initials) → `[PERSON]`
* **EMAIL** — any email, including obfuscated `name(at)domain(dot)com` → `[EMAIL]`
* **PHONE** — any international/national format (separators/emoji bullets allowed) → `[PHONE]`
* **ADDRESS** — street + number; full postal lines; apartment/unit numbers → `[ADDRESS]`
* **SSN** — US Social Security numbers → `[SSN]`
* **ID** — national IDs (PESEL, NIN, Aadhaar, DNI, etc.) when personal → `[ID]`
* **UUID** — person-scoped system identifiers (e.g., MRN/NHS/patient IDs/customer UUIDs) → `[UUID]`
* **CREDIT_CARD** — 13–19 digits (spaces/hyphens allowed) → `[CARD_LAST4:####]` (keep last-4 only)
* **IBAN** — IBAN/bank account numbers → `[IBAN_LAST4:####]` (keep last-4 only)
* **GENDER** — self-identification (male/female/non-binary/etc.) → `[GENDER]`
* **AGE** — stated ages (“I’m 29”, “age: 47”, “29 y/o”) → `[AGE_YEARS:##]`
* **RACE** — race/ethnicity self-identification → `[RACE]`
* **MARITAL_STATUS** — married/single/divorced/widowed/partnered → `[MARITAL_STATUS]`


## Keep (do not redact)

* Card **last-4** when only last-4 is present (e.g., “ending 9021”, “•••• 9021”).
* Operational IDs: order/ticket/invoice numbers, shipment tracking, device serials, case IDs.
* Non-personal org info: company names, product names, team names.
* Cities/countries alone (redact full street+number, not plain city/country mentions).

## Output schema (exactly these fields)
* **redacted_text** The original text with all the sensitive information replaced with redacted tokens
* **entities** Array with all the replaced elements, each element represented by following fields
  * **replacement_token**: one of `[PERSON] | [EMAIL] | [PHONE] | [ADDRESS] | [SSN] | [ID] | [UUID] | [CREDIT_CARD] | [IBAN] | [GENDER] | [AGE] | [RACE] | [MARITAL_STATUS]`
  * **value**: original text that was redacted
  * **reason**: brief string explaining the rule/rationale

for example
{
  "redacted_text": "Hi, I'm [PERSON] and my email is [EMAIL].",
  "entities": [
    { "type": "PERSON", "value": "John Smith", "reason": "person name"},
    { "type": "EMAIL", "value": "john.smith@example.com", "reason": "email"},
  ]
}
</task_description>
You will be given a single task with context in the context XML block and the task in the question XML block
Solve the task in question block based on the context in context block.
Generate only the answer, do not generate anything else
"""

PROMPT_TEMPLATE = """

Now for the real task, solve the task in question block based on the context in context block.
Generate only the solution, do not generate anything else
<context>
{context}
</context>
<question>Redact provided text according to the task description and return redacted elements.</question>
"""

from openai import OpenAI

PORT = "PORT GOES HERE"  # 8000 for vllm, 11434 for ollama
MODEL_NAME = "NAME USED FOR SETTING UP THE CLIENT"
TEXT_TO_REDACT = "NI number AB123456C confirmed."

client = OpenAI(base_url=f"http://127.0.0.1:{PORT}/v1", api_key="EMPTY")
chat_response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": PROMPT_TEMPLATE.format(context=TEXT_TO_REDACT)},
    ],
    temperature=0,
)
```

## Risks & Mitigations

* **False negatives/positives:** May miss novel formats or over-redact generic terms. Mitigate via guardrails + post-validation.
* **Policy drift:** Keep task preamble fixed; monitor with unit tests.

## Model Sources

* **Homepage:** [https://distillabs.ai](https://distillabs.ai)
* **Contact:** [contact@distillabs.ai](mailto:contact@distillabs.ai)
