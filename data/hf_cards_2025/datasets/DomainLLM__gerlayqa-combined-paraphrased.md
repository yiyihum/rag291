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
- StGB
- civil-law
- criminal-law
- instruction-tuning
- paraphrased
size_categories:
- 1K<n<10K
pretty_name: GerLayQA Combined Paraphrased (BGB + StGB)
---

# GerLayQA Combined Paraphrased 🇩🇪⚖️

## Dataset Description

This is a **combined, shuffled dataset** merging both the BGB (civil law) and StGB (criminal law) paraphrased German legal QA datasets. All examples are paraphrased and restructured by GPT-5 for fine-tuning large language models on German legal question-answering tasks.

### Key Features

- **6,462 high-quality QA pairs** covering both German Civil and Criminal Law
- **Combined coverage**: BGB (Bürgerliches Gesetzbuch) + StGB (Strafgesetzbuch)
- **Randomly shuffled**: Mixed civil and criminal law questions for diverse training
- **Paraphrased questions** to remove plagiarism while maintaining legal accuracy
- **Structured 7-section answers** following a consistent format
- **Comprehensive legal reasoning** with detailed explanations
- **Full article texts** included in paragraphs field for reference
- **90/10 train/validation split** for model evaluation
- **Length-filtered**: Questions ≤256 words, Answers ≤1024 words
- **Cleaned and formatted** by GPT-5 with strict quality guidelines

### Dataset Composition

| Source | Examples | Percentage | Law Domain |
|--------|----------|------------|------------|
| BGB | 5,255 | 81.3% | Civil Law (Bürgerliches Gesetzbuch) |
| StGB | 1,207 | 18.7% | Criminal Law (Strafgesetzbuch) |
| **Total** | **6,462** | **100%** | **Combined** |

### Dataset Structure

Each example contains:

```json
{
  "question": "Paraphrased legal question in German",
  "answer": "Structured answer in 7-section format",
  "paragraphs": "{"§ 123 BGB": "Full article text"}"
}
```

**Note**: The `paragraphs` field is stored as a JSON string. Parse it with `json.loads()` to access the dictionary.

### Answer Format

All answers follow this mandatory structure:

```
Kurzantwort:
[2-3 line summary with key legal conclusion]

1 Rechtsgebiet:
[Area of law, e.g., Vertragsrecht (BGB), Strafrecht (StGB)]

2 Relevante Vorschriften:
[Cited articles with full text and proper formatting - either BGB or StGB]

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
| Train | 5,815 (90%) |
| Validation | 647 (10%) |
| **Total** | **6,462** |

## Dataset Creation

### Source Datasets

This dataset is a merger of:

1. **[DomainLLM/gerlayqa-bgb-paraphrased](https://huggingface.co/datasets/DomainLLM/gerlayqa-bgb-paraphrased)** - Civil Law (5,255 examples)
2. **[DomainLLM/gerlayqa-stgb-paraphrased](https://huggingface.co/datasets/DomainLLM/gerlayqa-stgb-paraphrased)** - Criminal Law (1,207 examples)

Both source datasets were derived from the original [GerLayQA dataset](https://huggingface.co/datasets/rcds/german_legal_questions).

### Processing Pipeline

1. **Source Processing**: 
   - Filtering by length (Q≤256 words, A≤1024 words)
   - Article enrichment from official BGB/StGB corpora
   - GPT-5 paraphrasing and restructuring
   
2. **Merging**:
   - Loaded both BGB and StGB datasets
   - Concatenated all examples
   - **Randomly shuffled** to mix civil and criminal law questions
   - Created new 90/10 train/validation split

3. **Quality Control**:
   - All outputs validated for legal accuracy
   - Consistent field structure maintained
   - Proper law code attribution (BGB vs StGB)

### Key Processing Rules

- ✅ Preserve all legal reasoning and arguments
- ✅ Maintain original length and detail level
- ✅ Use only articles explicitly mentioned in the original answer
- ✅ Replace personal names with neutral placeholders
- ✅ Keep citations consistent: "§ X BGB" or "§ X StGB"
- ✅ No mixing of law codes within single examples
- ✅ Respect law domain boundaries (civil vs criminal)

## Intended Use

### Primary Use Cases

- **Fine-tuning** German legal language models for both civil and criminal law
- **Multi-domain legal instruction tuning** for question-answering
- **Evaluation** of German legal NLP systems across law domains
- **Research** on legal reasoning and explanation generation
- **Transfer learning** between civil and criminal law domains

### Out-of-Scope Use

- ❌ Real legal advice (for informational/educational purposes only)
- ❌ Replacement for professional legal consultation
- ❌ Use without proper legal disclaimers

## Advantages of Combined Dataset

1. **Diverse Training**: Models learn both civil and criminal law concepts
2. **Better Generalization**: Exposure to different legal reasoning styles
3. **Single Dataset**: Easier to manage than separate datasets
4. **Shuffled**: Random mixing prevents domain-specific overfitting
5. **Comprehensive**: Covers major areas of German law (81% civil, 19% criminal)

## Limitations

- BGB portion is partial (~34% of available BGB data due to API rate limits)
- StGB is complete but smaller sample size (18.7% of total)
- Training data may contain biases from web-crawled sources
- Legal information may become outdated as laws change
- Simplified explanations may not capture all legal nuances
- Imbalanced: More BGB (81%) than StGB (19%) examples

## Ethical Considerations

- This dataset is for **educational and research purposes ONLY**
- Should NEVER be used to provide actual legal advice
- Both civil and criminal law have serious real-world consequences
- Users must add appropriate disclaimers when deploying models
- Original data sources should be credited
- Consider potential misuse in deployment scenarios
- Criminal law content requires especially careful handling

## Usage Example

```python
from datasets import load_dataset
import json

# Load combined dataset
dataset = load_dataset("DomainLLM/gerlayqa-combined-paraphrased")

print(f"Train: {len(dataset['train'])} examples")
print(f"Validation: {len(dataset['validation'])} examples")

# Access an example
example = dataset['train'][0]
print(f"Question: {example['question']}")
print(f"Answer: {example['answer'][:200]}...")

# Parse paragraphs (stored as JSON string)
paragraphs = json.loads(example['paragraphs'])
print(f"Cited articles: {list(paragraphs.keys())}")

# Check if it's BGB or StGB
if 'BGB' in str(paragraphs):
    print("Domain: Civil Law (BGB)")
elif 'StGB' in str(paragraphs):
    print("Domain: Criminal Law (StGB)")
```

## Fine-tuning Example

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer

# Load dataset
dataset = load_dataset("DomainLLM/gerlayqa-combined-paraphrased")

# Format for instruction tuning
def format_instruction(example):
    return {
        "text": f"<|user|>
{example['question']}
<|assistant|>
{example['answer']}"
    }

# Apply formatting
train_dataset = dataset['train'].map(format_instruction)
eval_dataset = dataset['validation'].map(format_instruction)

# Fine-tune your model on both civil and criminal law...
```

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{gerlayqa_combined_paraphrased_2025,
  title={GerLayQA Combined Paraphrased: A Unified German Legal QA Dataset (BGB + StGB)},
  author={DomainLLM},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/DomainLLM/gerlayqa-combined-paraphrased}
}
```

And cite the source datasets:

```bibtex
@dataset{gerlayqa_bgb_paraphrased_2025,
  title={GerLayQA-BGB Paraphrased: A Structured German Civil Law QA Dataset},
  author={DomainLLM},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/DomainLLM/gerlayqa-bgb-paraphrased}
}

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
**Composition**: 81.3% BGB (Civil) + 18.7% StGB (Criminal)
