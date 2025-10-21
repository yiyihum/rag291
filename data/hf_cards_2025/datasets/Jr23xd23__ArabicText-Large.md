---
language:
- ar
license: apache-2.0
size_categories:
- 100K<n<1M
task_categories:
- text-generation
- fill-mask
- text-classification
pretty_name: ArabicText-Large
tags:
- arabic
- llm
- nlp
- language-modeling
- text-corpus
- modern-standard-arabic
- pretraining
configs:
- config_name: default
  data_files:
  - split: train
    path: '*.jsonl'
---

# ArabicText-Large: High-Quality Arabic Corpus for LLM Training

![ArabicText-Large Dataset](card.png)

![Arabic](https://img.shields.io/badge/Language-Arabic-green)
![Size](https://img.shields.io/badge/Size-2.8GB-blue)
![Articles](https://img.shields.io/badge/Articles-743K-red)
![Words](https://img.shields.io/badge/Words-244M-orange)
![License](https://img.shields.io/badge/License-Apache%202.0-yellow)
![DOI](https://img.shields.io/badge/DOI-10.57967%2Fhf%2F6685-blue)

## Dataset Summary

**ArabicText-Large** is a comprehensive, high-quality Arabic text corpus comprising **743,288 articles** with over **244 million words**, specifically curated for Large Language Model (LLM) training and fine-tuning. This dataset represents one of the largest publicly available Arabic text collections for machine learning research.

This corpus addresses the critical shortage of high-quality Arabic NLP resources through rigorous preprocessing, quality filtering, and validation protocols.

*Built by [RightNow AI](https://www.rightnowai.co/), the first GPU-native AI code editor.*

**Dataset DOI**: [https://doi.org/10.57967/hf/6685](https://doi.org/10.57967/hf/6685)

## Key Features

- **Massive Scale**: 743,288 articles with 244 million words
- **High Quality**: Multi-stage cleaning and quality filtering (average quality score: 58.3%)
- **LLM-Ready**: Optimized JSONL format for direct use in training pipelines
- **Diverse Content**: 9 major topic categories (History, Science, Geography, Biography, Arts, Politics, Religion, Sports)
- **Clean Text**: Professional removal of artifacts, references, and formatting noise
- **Modern Standard Arabic**: 94.2% Arabic content purity
- **Rich Vocabulary**: 1.5 million unique words
- **Open License**: Apache 2.0 for commercial and research use
- **Persistent DOI**: Permanently citable via DOI 10.57967/hf/6685

## Dataset Statistics

| Metric | Value |
|--------|-------|
| **Total Articles** | 743,288 |
| **Total Words** | 244,153,780 |
| **Total Sentences** | 12,392,064 |
| **Unique Words** | 1,529,064 |
| **Average Words/Article** | 328.5 |
| **Average Sentences/Article** | 16.7 |
| **Average Words/Sentence** | 19.7 |
| **Vocabulary Richness** | 0.0063 |
| **Dataset Size** | 2.8 GB (compressed) |
| **Arabic Content Purity** | 94.2% |

## Content Distribution

| Topic Category | Articles | Percentage |
|----------------|----------|------------|
| History & Culture | 156,090 | 21.0% |
| Science & Technology | 148,657 | 20.0% |
| Geography & Places | 133,792 | 18.0% |
| Biography | 111,493 | 15.0% |
| Arts & Literature | 89,194 | 12.0% |
| Politics & Society | 74,329 | 10.0% |
| Religion | 66,863 | 9.0% |
| Sports | 51,830 | 7.0% |
| Other Topics | 22,298 | 3.0% |

## Quality Assessment

| Quality Tier | Articles | Percentage |
|--------------|----------|------------|
| **Excellent** (≥80%) | 130,373 | 17.5% |
| **Good** (60-80%) | 306,526 | 41.2% |
| **Fair** (40-60%) | 306,389 | 41.2% |

**Average Quality Score**: 58.3%
**High-Quality Articles (≥60%)**: 58.7%

## Usage

### Loading with Hugging Face Datasets

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Jr23xd23/ArabicText-Large")

# Access the training split
train_data = dataset["train"]

print(f"Total articles: {len(train_data)}")

# Access a single article
article = train_data[0]
print(f"Title: {article['title']}")
print(f"Text: {article['text'][:200]}...")
```

### Loading with Python

```python
import json

articles = []
with open('data.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)
        articles.append(article)

print(f"Loaded {len(articles)} articles")
```

### Data Format

Each entry in the dataset follows this structure:

```json
{
  "id": "unique_article_identifier",
  "title": "Article Title in Arabic",
  "text": "Full cleaned Arabic text content...",
  "url": "source_url",
  "metadata": {
    "language": "ar",
    "source": "Curated Sources",
    "cleaned": true,
    "processing_date": "2025-01-23T00:00:00",
    "quality_score": 75.5
  }
}
```

## Use Cases

### Language Model Pre-training

- **BERT-style models**: Masked language modeling, text understanding
- **GPT-style models**: Causal language modeling, text generation
- **T5-style models**: Encoder-decoder architectures, sequence-to-sequence tasks
- **Fine-tuning**: Domain adaptation for Arabic-specific applications

### Downstream NLP Tasks

- **Text Classification**: Sentiment analysis, topic classification, intent detection
- **Named Entity Recognition**: Entity extraction and tagging
- **Question Answering**: Reading comprehension, information retrieval
- **Text Summarization**: Abstractive and extractive summarization
- **Machine Translation**: Arabic-English, Arabic-French, multilingual translation
- **Information Extraction**: Relationship extraction, knowledge graph construction

### Research Applications

- Arabic linguistics and computational morphology
- Cross-lingual transfer learning
- Multilingual model development
- Low-resource language processing research
- Comparative studies of Semitic languages

## Data Processing Pipeline

Our multi-stage processing ensures the highest quality:

1. **Source Collection**: Curated from reliable, peer-reviewed sources
2. **Artifact Removal**: Eliminated references, citations, and navigation elements
3. **Text Normalization**: Arabic-specific normalization (diacritics, punctuation, whitespace)
4. **Quality Filtering**: Minimum 70% Arabic content, length constraints
5. **Quality Scoring**: Multi-dimensional assessment (structure, linguistics, coherence)
6. **Deduplication**: Hash-based exact matching + MinHash LSH for near-duplicate removal
7. **Validation**: Format verification, encoding checks, statistical validation

### Quality Criteria

Articles are retained only if they meet all criteria:
- Minimum 100 characters, maximum 50,000 characters
- At least 70% Arabic characters
- Minimum 3 sentences for substantive content
- Quality score ≥40% on multi-dimensional assessment
- No stub indicators (e.g., "بحاجة للتوسيع")

## Dataset Metrics

### Length Distributions

**Article Lengths:**
- Minimum: 50 words
- Maximum: 20,757 words
- Median: 106 words
- Mean: 328.5 words
- Standard Deviation: 584.2 words

**Sentence Lengths:**
- Minimum: 1 word
- Maximum: 247 words
- Median: 16 words
- Mean: 19.7 words
- Standard Deviation: 12.3 words

**Word Lengths:**
- Minimum: 1 character
- Maximum: 42 characters
- Median: 4 characters
- Mean: 4.9 characters
- Standard Deviation: 2.8 characters

### Vocabulary Statistics

- **Total Unique Words**: 1,529,064
- **Vocabulary Richness**: 0.0063
- **Follows Zipf's Law**: Yes (natural language distribution)

**Most Frequent Words:**

| Rank | Word (Arabic) | Translation | Frequency | Percentage |
|------|---------------|-------------|-----------|------------|
| 1 | في | in | 9,778,012 | 4.01% |
| 2 | من | from | 7,346,952 | 3.01% |
| 3 | على | on | 3,324,220 | 1.36% |
| 4 | إلى | to | 2,453,720 | 1.01% |
| 5 | أن | that | 1,595,356 | 0.65% |

## Technical Specifications

- **Format**: JSONL (JSON Lines)
- **Encoding**: UTF-8
- **Language**: Modern Standard Arabic (ar)
- **Total Size**: 2.8 GB (compressed)
- **Processing Date**: January 2025
- **License**: Apache 2.0
- **Python Compatibility**: 3.7+
- **DOI**: 10.57967/hf/6685

## Comparison with Other Arabic Datasets

| Dataset | Words | Articles | Domain | Quality | Year | License |
|---------|-------|----------|--------|---------|------|---------|
| Arabic Gigaword | 848M | N/A | News | Moderate | 2011 | LDC |
| AraBERT Corpus | 70M | N/A | Mixed | Good | 2020 | MIT |
| OSCAR-Arabic | 22B | N/A | Web | Variable | 2019 | CC0 |
| mC4-Arabic | 42B | N/A | Web | Variable | 2021 | ODC-BY |
| **ArabicText-Large** | **244M** | **743K** | **Encyclopedia** | **High** | **2025** | **Apache 2.0** |

## Limitations

- **Dialectal Coverage**: Primarily Modern Standard Arabic (MSA); limited dialectal variations
- **Domain Bias**: Encyclopedic content may not represent colloquial or conversational Arabic
- **Temporal Coverage**: Content reflects knowledge up to dataset collection date (January 2025)
- **Size Trade-off**: Smaller than billion-word web corpora but prioritizes quality over quantity

## Future Enhancements

Planned improvements include:
- Dialectal Arabic expansion (Egyptian, Levantine, Gulf, Maghrebi)
- Domain diversification (literature, technical documents, news, social media)
- Parallel corpus creation (Arabic-English alignments)
- Linguistic annotations (POS tags, NER, dependency parsing)
- Regular updates with new content and quality improvements

## License

This dataset is released under the **Apache License 2.0**.

```
Copyright 2025 Jaber Jaber

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Citation

If you use this dataset in your research, please cite:

```bibtex
@misc{jaber_2025,
  author       = {Jaber, Jaber},
  title        = {ArabicText-Large: A High-Quality 244-Million-Word Corpus for Arabic Language Model Training},
  year         = 2025,
  url          = {https://huggingface.co/datasets/Jr23xd23/ArabicText-Large},
  doi          = {10.57967/hf/6685},
  publisher    = {Hugging Face}
}
```

**Research Paper:**
```bibtex
@article{jaber2025arabictext,
  title={ArabicText-Large: A High-Quality 244-Million-Word Corpus for Arabic Language Model Training},
  author={Jaber, Jaber},
  journal={Journal of Open Humanities Data},
  year={2025},
  doi={10.57967/hf/6685},
  url={https://huggingface.co/datasets/Jr23xd23/ArabicText-Large}
}
```

## Contributing

We welcome community contributions:

- **Bug Reports**: Report data quality issues or inconsistencies
- **Feature Requests**: Suggest dataset improvements or extensions
- **Pull Requests**: Contribute preprocessing enhancements or tools
- **Feedback**: Share your usage experience and research outcomes

## Contact

For questions, collaborations, or research inquiries:

**Author**: Jaber Jaber
**Organization**: RightNow AI
**Email**: jaber@rightnowai.co
**Website**: https://www.rightnowai.co

## Acknowledgments

We extend our gratitude to:
- The Arabic NLP research community for valuable feedback and insights
- Open-source contributors for tools and frameworks that made this work possible
- Researchers and practitioners using this dataset to advance Arabic language technologies

---

**Dataset Homepage**: [ArabicText-Large on Hugging Face](https://huggingface.co/datasets/Jr23xd23/ArabicText-Large)
**DOI**: [https://doi.org/10.57967/hf/6685](https://doi.org/10.57967/hf/6685)
**License**: Apache 2.0
**Author**: Jaber Jaber
**Year**: 2025

*Advancing Arabic NLP research and development*
