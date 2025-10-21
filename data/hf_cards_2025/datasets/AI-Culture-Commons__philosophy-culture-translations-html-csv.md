---
configs:
- config_name: csv
  data_files: ai-culture.csv
license: cc-by-4.0
task_categories:
- translation
- text-generation
- text-classification
- sentence-similarity
- summarization
- fill-mask
- feature-extraction
language:
- en
- he
- hi
- ru
- fr
- de
- es
- zh
- it
- pt
- ja
- ko
tags:
- multilingual
- cultural-dataset
- philosophical-texts
- html-structure
- web-content
- document-understanding
- chat-training
- instruction-tuning
- conversational-ai
- multilingual-chat
- context-learning
- structured-knowledge
- ethical-ai-training
- cultural-understanding
- complex-reasoning
- philosophical-reasoning
- world-knowledge
- analytical-content
- intellectual-discourse
- large-context-window
- comprehensive-knowledge
- parallel-corpora
- html-parsing
- website-archive
- csv
- html
pretty_name: Philosophy and Culture Translations CSV + HTML Corpus
size_categories:
- 10M<n<100M
---

# AI-Culture Philosophy and Culture Translations CSV + HTML Corpus

The corpus contains an exceptionally diverse range of cultural, philosophical, and literary texts, available in **12 major languages**. Among other topics, there is extensive engagement with the ethics and aesthetics of artificial intelligence and its cultural and philosophical implications, as well as connections between AI and philosophy of language and philosophy of mind.

This project is maintained by a non-profit digital humanities team committed to advancing humane AI through **meticulously curated, thoroughly clean** cultural datasets.

## Quick Start

```python
from datasets import load_dataset

# CSV format (parallel text pairs)
csv_ds = load_dataset(
    "AI-Culture-Commons/philosophy-culture-translations-html-csv",
    name="csv",
    split="train"
)
```

## Dataset Overview

| File | Format | Size | Structure | Characters | Reference |
|------|--------|------|-----------|------------|-----------|
| `ai-culture.csv` | CSV | 460 MB | Parallel pairs: Original ↔ Translation | 83M+ | [![DOI](https://zenodo.org/badge/1021100370.svg)](https://doi.org/10.5281/zenodo.16001657) |
| `ai-culture.zip` | Complete Website Archive | 162 MB | HTML + PDF + CSS + Images | 83M+ | [![DOI](https://zenodo.org/badge/1021100223.svg)](https://doi.org/10.5281/zenodo.16001641) |

## Dataset Summary

- **Content Structure**: ~420 articles × 12 languages
- **Content Volume**: 83M+ characters
- Each article is provided in **3 formats**:
  - Plain translated text
  - HTML source of the translation
  - Original source text
- **HTML Structure**: Complex, identical across all language versions
- **Content Types**: Essays, review articles, philosophical works, literature, interactive books, poetry, commentary, press reviews
- **Content domains**: Philosophy (1.1K), Literature (1.5K), Culture (1.1K), Commentary (950), Press Review (200), General (150)
- **Languages**: English, French, German, Spanish, Portuguese, Italian, Japanese, Russian, Korean, Mandarin Chinese, Hindi, Hebrew

## CSV Data Structure

The CSV file contains parallel text pairs with the following columns:

```csv
article_code,source_lang,target_lang,section_name,source_text,translated_text,source_html,translated_html,source_url,translated_url
```

**Column descriptions:**
- `article_code`: Unique identifier for each article
- `source_lang`: Source language code
- `target_lang`: Target language code (en, fr, de, etc.)
- `section_name`: Content section (philosophy-of-learning, culture&literature, etc.)
- `source_text`: Clean text content in source language
- `translated_text`: Clean text content in target language
- `source_html`: Complete HTML source (original)
- `translated_html`: Complete HTML source (translation)
- `source_url`: URL of original article
- `translated_url`: URL of translated article

## Content Characteristics

All our datasets guarantee four core principles:

1. **Extremely clean**: All content is original, editor-curated text without any user comments, scraped texts, ads, tracking scripts, JavaScript, cookies, or unwanted noise. All source articles were produced by our editorial team and professionally edited.

2. **Transparent process**: *Both clean text and original HTML source* are preserved in all datasets, with full pipeline documentation (see below).

3. **Free license**: Clear free license - usage is free for any purpose including commercial use, with attribution required only when feasible.

4. **Rich intellectual content**: Long-form essays that foster philosophical reasoning, cultural awareness, and literary sensitivity in models. Our datasets provide models with deep philosophical-intellectual context and diverse connections between culture, philosophy, literature, and technology—particularly AI. The content curation is specifically designed to help train more intellectually critical and philosophically grounded AI models.

## Pipeline & Validation

The corpus was created with an **open-source pipeline** [[GitHub link]](https://github.com/AI-Culture-Commons/ai-culture-pipeline) that:

1. Processes HTML files from local project directories (no web crawling required)
2. Maps translated files to their source originals using predefined path mappings
2. Extracts and processes content through a multi-stage pipeline:
   * **HTML files**: Compacts HTML structure, extracts titles via *BeautifulSoup*, and converts body content to clean text using *html2text* with enhanced CJK character handling
   * **Text processing**: Removes control characters, normalizes Unicode (NFKC), handles bidirectional text spacing, and collapses excessive whitespace
4. Performs language-aware content validation and section categorization
5. Generates:
   * `ai-culture.csv` – parallel text pairs with metadata
   * `ai-culture.zip` – complete website archive with all assets
6. Runs multi-layer integrity validation including dataset loading, structure verification, and sample inspection. Includes supplementary datasets library compatibility tests for Hugging Face Hub integration

All scripts include a **zero-duplicate** guarantee. We maintain **machine-validated alignment** between all language pairs.

## License & Attribution

**License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **English license terms**: https://degeneration-of-nation.org/license
- **Hebrew license terms**: https://hitdarderut-haaretz.org/license

## Citation

```bibtex
@dataset{AI_Culture_Translations_2025,
  title     = {AI-Culture Commons Philosophy and Culture Translations},
  author    = {AI-Culture Commons},
  year      = {2025},
  version   = {2.0},
  url       = {https://huggingface.co/datasets/AI-Culture-Commons/philosophy-culture-translations-html-csv},
  license   = {CC BY 4.0}
}
```