---
language:
- en
license: apache-2.0
tags:
- code-explanation
- visualization
- mermaid
- codet5
- developer-tools
pipeline_tag: text-generation
library_name: transformers
base_model: Salesforce/codet5-small
---

🧠 CODE-EXPLAIN-VIZ: AI-Powered Code Understanding & Visualization

CODE-EXPLAIN-VIZ is an advanced AI-driven code comprehension and visualization system designed to explain source code in natural language and generate visual flow diagrams automatically.
Built on top of CodeT5, this model reads raw Python code and produces a detailed explanation, step-by-step logic breakdown, and a Mermaid flowchart that represents the control flow of the program.

## Quick start

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run CLI demo:
```bash
python cli.py --file data_examples/example_code.py
```

3. Copy the Mermaid flowchart text printed by CLI into a Mermaid live editor (https://mermaid.live) or render with mermaid-cli to see the visual flowchart.

## What you get
- `short` one-line explanation
- `detailed` explanation (multi-line)
- `mermaid` flowchart text describing control flow
- `unit_tests` template (pytest)

## How it works
- A sequence-to-sequence model (CodeT5) generates natural language explanations from code.
- `viz_generator.py` parses the function AST and produces a reliable mermaid flowchart.
- Combining both yields both human-friendly narrative and precise structural view.

## Train / Fine-tune
Use `train_docgen.py` with a JSONL dataset (each line: `{"code": "...", "doc": "..."}`).

## License
Apache-2.0
