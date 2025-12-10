---
language:
- de
license: cc-by-4.0
task_categories:
- question-answering
- text-generation
tags:
- legal
- german-law
- BGB
- civil-law
- instruction-tuning
- paraphrased
size_categories:
- 10K<n<100K
pretty_name: GerLayQA-BGB Paraphrased
---

# GerLayQA-BGB Paraphrased 🇩🇪⚖️

## Dataset Description

This is a **paraphrased and restructured version** of the GerLayQA BGB (Bürgerliches Gesetzbuch / German Civil Code) dataset, specifically prepared for fine-tuning large language models on German civil law question-answering tasks.

### Key Features

- **5,255 high-quality QA pairs** about German Civil Law (BGB)
- **Paraphrased questions** to remove plagiarism while maintaining legal accuracy
- **Structured 7-section answers** following a consistent format
- **Comprehensive legal reasoning** with detailed explanations
- **Full article texts** included in paragraphs field for reference
- **90/10 train/validation split** for model evaluation
- **Length-filtered**: Questions ≤256 words, Answers ≤1024 words
- **Cleaned and formatted** by GPT-5 with strict quality guidelines

### Dataset Structure

Each example contains:

```json
{
  "question": "Paraphrased legal question in German",
  "answer": "Structured answer in 7-section format",
  "paragraphs": "{"§ 123 BGB": "Full text of the cited article"}"
}
```

### Answer Format

All answers follow this mandatory structure:

```
Kurzantwort:
[2-3 line summary with key legal conclusion]

1 Rechtsgebiet:
[Area of law, e.g., Vertragsrecht, Erbrecht]

2 Relevante Vorschriften:
[Cited BGB articles with full text and proper formatting]

3 Bedeutung:
[Plain German explanation of what the laws mean]

4 Anwendung auf den Fall:
[Application of the law to the specific scenario]

5 Ergebnis:
[Final legal outcome or conclusion]

Abschließender Satz:
[One-line human-friendly summary]
```

## Data Splits

| Split | Examples |
|-------|----------|
| Train | 4,729 (90%) |
| Validation | 526 (10%) |
| **Total** | **5,255** |

## Dataset Creation

### Source Data

- **Original Dataset**: [GerLayQA](https://huggingface.co/datasets/rcds/german_legal_questions) by RCDS
- **Law Domain**: Bürgerliches Gesetzbuch (BGB) - German Civil Code
- **Articles**: Full BGB article texts from [Hugging Face german-nlp-group/bgb](https://huggingface.co/datasets/german-nlp-group/bgb)

### Processing Pipeline

1. **Filtering**: Removed questions >256 words and answers >1024 words
2. **Enrichment**: Added full article texts from official BGB corpus
3. **Paraphrasing**: Questions paraphrased by GPT-5 for clarity and originality
4. **Restructuring**: Answers reformatted into consistent 7-section structure
5. **Quality Control**: All outputs validated for legal accuracy and completeness

### Key Processing Rules

- ✅ Preserve all legal reasoning and arguments
- ✅ Maintain original length and detail level
- ✅ Use only articles explicitly mentioned in the original answer
- ✅ Replace personal names with neutral placeholders
- ✅ Keep citations consistent: always "§ X BGB"
- ✅ No mixing of law codes (BGB only, never StGB or GG)

## Intended Use

### Primary Use Cases

- **Fine-tuning** German legal language models for civil law
- **Instruction tuning** for legal question-answering
- **Evaluation** of German legal NLP systems
- **Research** on legal reasoning and explanation generation

### Out-of-Scope Use

- ❌ Real legal advice (for informational/educational purposes only)
- ❌ Replacement for professional legal consultation
- ❌ Use without proper legal disclaimers

## Limitations

- Focus on BGB (civil law) only - does not cover criminal law (StGB) or constitutional law (GG)
- Training data may contain biases from web-crawled sources
- Legal information may become outdated as laws change
- Simplified explanations may not capture all legal nuances

## Ethical Considerations

- This dataset is for **educational and research purposes**
- Should not be used to provide actual legal advice
- Users must add appropriate disclaimers when deploying models
- Original data sources should be credited

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{gerlayqa_bgb_paraphrased_2025,
  title={GerLayQA-BGB Paraphrased: A Structured German Civil Law QA Dataset},
  author={DomainLLM},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/DomainLLM/gerlayqa-bgb-paraphrased}
}
```

Original GerLayQA dataset:
```bibtex
@misc{gerlayqa2023,
  title={German Legal Question Answering Dataset},
  author={RCDS},
  year={2023},
  url={https://huggingface.co/datasets/rcds/german_legal_questions}
}
```

## License

CC-BY-4.0 - Attribution required

## Contact

For questions or issues, please open an issue on the [GitHub repository](https://github.com/DomainLLM) or contact the DomainLLM team.

---

**Version**: 1.0  
**Last Updated**: October 2025  
**Processing Model**: GPT-5  
**Language**: German (de)
