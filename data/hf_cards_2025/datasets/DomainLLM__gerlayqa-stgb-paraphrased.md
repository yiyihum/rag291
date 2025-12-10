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
- StGB
- criminal-law
- instruction-tuning
- paraphrased
size_categories:
- 1K<n<10K
pretty_name: GerLayQA-StGB Paraphrased
---

# GerLayQA-StGB Paraphrased 🇩🇪⚖️

## Dataset Description

This is a **paraphrased and restructured version** of the GerLayQA StGB (Strafgesetzbuch / German Criminal Code) dataset, specifically prepared for fine-tuning large language models on German criminal law question-answering tasks.

### Key Features

- **1,207 high-quality QA pairs** about German Criminal Law (StGB)
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
  "paragraphs": "{"§ 242 StGB": "Full text of the cited article"}"
}
```

### Answer Format

All answers follow this mandatory structure:

```
Kurzantwort:
[2-3 line summary with key legal conclusion]

1 Rechtsgebiet:
[Area of law, e.g., Strafrecht, Vermögensdelikte]

2 Relevante Vorschriften:
[Cited StGB articles with full text and proper formatting]

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
| Train | 1,086 (90%) |
| Validation | 121 (10%) |
| **Total** | **1,207** |

## Dataset Creation

### Source Data

- **Original Dataset**: [GerLayQA](https://huggingface.co/datasets/rcds/german_legal_questions) by RCDS
- **Law Domain**: Strafgesetzbuch (StGB) - German Criminal Code
- **Articles**: Full StGB article texts from [Hugging Face german-nlp-group/stgb](https://huggingface.co/datasets/german-nlp-group/stgb)

### Processing Pipeline

1. **Filtering**: Removed questions >256 words and answers >1024 words
2. **Enrichment**: Added full article texts from official StGB corpus
3. **Paraphrasing**: Questions paraphrased by GPT-5 for clarity and originality
4. **Restructuring**: Answers reformatted into consistent 7-section structure
5. **Quality Control**: All outputs validated for legal accuracy and completeness

### Key Processing Rules

- ✅ Preserve all legal reasoning and arguments
- ✅ Maintain original length and detail level
- ✅ Use only articles explicitly mentioned in the original answer
- ✅ Replace personal names with neutral placeholders
- ✅ Keep citations consistent: always "§ X StGB"
- ✅ No mixing of law codes (StGB only, never BGB or GG)

## Intended Use

### Primary Use Cases

- **Fine-tuning** German legal language models for criminal law
- **Instruction tuning** for legal question-answering
- **Evaluation** of German legal NLP systems
- **Research** on legal reasoning and explanation generation

### Out-of-Scope Use

- ❌ Real legal advice (for informational/educational purposes only)
- ❌ Replacement for professional legal consultation
- ❌ Use without proper legal disclaimers

## Limitations

- Focus on StGB (criminal law) only - does not cover civil law (BGB) or constitutional law (GG)
- Training data may contain biases from web-crawled sources
- Legal information may become outdated as laws change
- Simplified explanations may not capture all legal nuances
- Criminal law is particularly sensitive - exercise extreme caution

## Ethical Considerations

- This dataset is for **educational and research purposes ONLY**
- Should NEVER be used to provide actual legal advice
- Criminal law has serious real-world consequences
- Users must add appropriate disclaimers when deploying models
- Original data sources should be credited
- Consider potential misuse in deployment scenarios

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{gerlayqa_stgb_paraphrased_2025,
  title={GerLayQA-StGB Paraphrased: A Structured German Criminal Law QA Dataset},
  author={DomainLLM},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/DomainLLM/gerlayqa-stgb-paraphrased}
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
