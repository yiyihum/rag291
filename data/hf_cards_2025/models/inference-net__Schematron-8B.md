---
library_name: transformers
base_model: meta-llama/Llama-3.1-8B-Instruct
---

<p align="center">
  <img alt="Schematron" src="https://huggingface.co/inference-net/Schematron-3B/resolve/main/Banner.png">
</p>

<p align="center">
  <a href="https://docs.inference.net/use-cases/json-extraction"><strong>Documentation</strong></a> ·
  <a href="https://inference.net/models/schematron-8b"><strong>Serverless API</strong></a> ·
  <a href="https://inference.net/blog/Schematron"><strong>Announcement blog</strong></a>
</p>

<br>

## Model Overview
Welcome to the Schematron series, [Inference.net's](https://inference.net/) long‑context extraction models specialized in converting noisy HTML into clean, typed JSON that conforms to your custom schema. The Schematron series was purpose‑trained for web scraping, data ingestion, and transforming arbitrary pages into structured records.

We're releasing these models in two different sizes:

- **Schematron‑8B** — marginal quality lift on harder/longer pages
- **Schematron‑3B** — recommended default; near‑parity quality at ~50% cost of Schematron-8B

> [!NOTE]
> This model card is dedicated to the smaller `Schematron-8B` model. Check out [`Schematron-3B`](https://huggingface.co/inference-net/Schematron-3B) for the smaller model.

## I/O at a glance
- **Input**: Cleaned HTML + JSON Schema (can be extracted from typed model like Pydantic/Zod)
- **Output**: Strictly valid JSON conforming to the provided schema (no narration)

> [!NOTE]
> The JSON Schema passed as input needs to conform to the [schema.org](https://json-schema.org/draft-07/schema) schema.

## Highlights
- **Schema-first extraction**: 100% schema‑conformant JSON outputs
- **Long context**: Robust to lengthy, noisy HTML (up to 128K tokens)
- **Variants**: 3B (default, most cost‑efficient) · 8B (marginal quality lift at ~2× cost)

## Model Details
- **Family**: Schematron (3B and 8B)
- **Context window**: Up to 128K tokens
- **Input**: Cleaned or raw HTML and a JSON Schema
- **Output**: Strict JSON that conforms to the provided schema

## Benchmarks

### HTML-to-JSON Extraction Quality

We evaluated extraction quality using Gemini 2.5 Pro as a judge, scoring extractions from 1-5 where 5 represents perfect extraction.

| Model | LLM-as-Judge Score |
|-------|-------------------|
| GPT-4.1 | 4.74 |
| **Schematron-8B** | **4.64** |
| **Schematron-3B** | **4.41** |
| Gemini-3B-Base | 2.24 |

### Web-Augmented Factuality on SimpleQA

We evaluated Schematron's real-world impact on LLM factuality using SimpleQA.

**Test Pipeline:**
1. **Query Generation**: Primary LLM (GPT-5 Nano or GPT-4.1) generates search queries and defines extraction schema
2. **Web Search**: Search provider (SERP or Exa) retrieves relevant pages
3. **Structured Extraction**: Schematron extracts JSON data from retrieved pages using the schema
4. **Answer Synthesis**: Primary LLM produces final answer from structured data

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6626a246891c75742bd19aaf/mU_01IPsf0FvkXYNYstRZ.png)

**Key findings:**
- Web search paired with JSON extraction improves factuality: Adding Schematron with web retrieval improves GPT-5 Nano's accuracy from 8.54% to 82.87%—nearly a 10x improvement
- Search provider matters: Exa (82.9%) significantly outperforms SERP (64.2%) for factual retrieval, while also being more cost-effective
- Structured extraction beats raw HTML: Processing raw HTML would require 100k+ tokens for 10 searches; Schematron's JSON extraction reduces this by orders of magnitude
- Small specialized models win: Schematron-8B (82.87%) outperforms the much larger Gemini 2.5 Flash (80.61%) on this task, showing that fine-tuning for well-defined tasks beats general purpose models
- Performance scales with model quality: When paired with GPT-4.1, Schematron achieves 85.58% accuracy, showing the approach benefits from stronger base models

## Minimal Quickstart
Use these local snippets to prepare HTML and compose a schema‑guided prompt. The model returns strictly valid JSON; validate it against your schema downstream.

```python
from lxml.html.clean import Cleaner
import lxml.html as LH

HTML_CLEANER = Cleaner(
    scripts=True,
    javascript=True,
    style=True,
    inline_style=True,
    safe_attrs_only=False,
)


def strip_noise(html: str) -> str:
    """Remove scripts, styles, and JavaScript from HTML using lxml.
    """
    if not html or not html.strip():
        return ""
    try:
        doc = LH.fromstring(html)
        cleaned = HTML_CLEANER.clean_html(doc)
        return LH.tostring(cleaned, encoding="unicode")
    except Exception:
        return ""
```

Compose messages with your schema and cleaned HTML:

```python
def construct_messages(schema: str, html: str):
    """Construct messages for a schema‑guided extraction request."""
    response_prompt = {
        "prompt_part_one": (
            "You are going to be given a JSON schema following the standardized JSON "
            "Schema format. You are going to be given a HTML page and you are going "
            "to apply the schema to the HTML page however you see it as applicable "
            "and return the results in a JSON object. The schema is as follows:"
        ),
        "prompt_part_two": "Here is the HTML page:",
        "prompt_part_three": "MAKE SURE ITS VALID JSON.",
    }

    user_prompt = (
        response_prompt['prompt_part_one']
        + "\n\n" + schema + "\n\n"
        + response_prompt['prompt_part_two']
        + "\n\n" + html + "\n\n"
        + response_prompt['prompt_part_three']
    )

    return [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": user_prompt},
    ]
```

> [!NOTE]
> In the [serverless API](https://inference.net/models/schematron-3b) there's no need to pass anything but the HTML. We handle the prompt formatting for you.


## Recommendations
- Temperature 0 and JSON mode for deterministic, parseable output
- Validate responses against your schema (e.g., Pydantic or Zod)
- Pre‑clean HTML (remove scripts/styles) when possible; avoid over‑aggressive removal
- Using lxml to clean the HTML is not required, but is recommended as it matches the training data.

## Limitations
- Static HTML only; render client‑side content upstream
- Very large pages may require truncation
- Ambiguous fields depend on schema clarity; be explicit in field descriptions

## Safety and Responsible Use
- Extracted data may include personal or sensitive information present in the page—handle and store responsibly
- Respect site terms, robots.txt, and applicable laws
- Use downstream validation and guardrails for compliance

## License
See license in the metadata above.

## Support
- Docs: https://docs.inference.net/use-cases/json-extraction
- Email: support@inference.net