---
license: odc-by
task_categories:
- text-generation
language:
- en
- ach
- lgg
- lug
- sw
- teo
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
source_datasets:
- allenai/wildjailbreak
tags:
- safety
- jailbreak
- african-languages
- instruction-tuning
- conversational-ai
- harmful-content
- safety-training
pretty_name: WildJailbreak Africa
dataset_info:
- config_name: en
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 258940000
    num_examples: 50000
  download_size: 258940000
  dataset_size: 258940000
- config_name: ach
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 272081318
    num_examples: 49819
  download_size: 272081318
  dataset_size: 272081318
- config_name: lgg
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 290939474
    num_examples: 49854
  download_size: 290939474
  dataset_size: 290939474
- config_name: lug
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 303608634
    num_examples: 49864
  download_size: 303608634
  dataset_size: 303608634
- config_name: swa
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 288676344
    num_examples: 49875
  download_size: 288676344
  dataset_size: 288676344
- config_name: teo
  features:
  - name: id
    dtype: string
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: source
    dtype: string
  splits:
  - name: train
    num_bytes: 292089554
    num_examples: 49871
  download_size: 292089554
  dataset_size: 292089554
configs:
- config_name: en
  data_files:
  - split: train
    path: data/en/train.jsonl
- config_name: ach
  data_files:
  - split: train
    path: data/ach/train.jsonl
- config_name: lgg
  data_files:
  - split: train
    path: data/lgg/train.jsonl
- config_name: lug
  data_files:
  - split: train
    path: data/lug/train.jsonl
- config_name: swa
  data_files:
  - split: train
    path: data/swa/train.jsonl
- config_name: teo
  data_files:
  - split: train
    path: data/teo/train.jsonl
---

# WildJailbreak Africa

This dataset contains translations of 50,000 samples from the **ai2-adapt-dev/tulu_v3.9_wildjailbreak_decontaminated_50k** dataset into 5 African languages. The dataset is designed for instruction tuning and safety training of language models in low-resource African languages.

## Dataset Description

The original WildJailbreak dataset is a synthetic safety-training dataset containing both vanilla (direct harmful requests) and adversarial (complex adversarial jailbreaks) prompt-response pairs. This translated version maintains the conversational structure while adapting the content to African languages.

## Languages Included

| Language Code | Language Name | Samples | Region |
|---------------|---------------|---------|---------|
| `en` | English | 50,000 | Original dataset |
| `ach` | Acholi | 49,819 | Northern Uganda |
| `lgg` | Lugbara | 49,854 | Northwestern Uganda/South Sudan |
| `lug` | Luganda | 49,864 | Central Uganda |
| `swa` | Swahili | 49,875 | East/Central Africa |
| `teo` | Ateso | 49,871 | Eastern Uganda |

**Total samples: ~299,283**

## Dataset Structure

```
├── en/
│   └── train.jsonl          # Original English dataset
├── ach/
│   └── train.jsonl          # Acholi translations
├── lgg/
│   └── train.jsonl          # Lugbara translations  
├── lug/
│   └── train.jsonl          # Luganda translations
├── swa/
│   └── train.jsonl          # Swahili translations
└── teo/
    └── train.jsonl          # Ateso translations
```

### Data Format

Each file contains JSONL format with the following structure:

```json
{
    "id": "unique_identifier",
    "messages": [
        {
            "role": "user",
            "content": "User message in target language"
        },
        {
            "role": "assistant", 
            "content": "Assistant response in target language"
        }
    ],
    "source": "ai2-adapt-dev/tulu_v3.9_wildjailbreak_decontaminated_50k"
}
```

## Usage

### Loading with Datasets Library

```python
from datasets import load_dataset

# Load specific language
dataset = load_dataset("CraneAILabs/wildjailbreak-africa", "swa")

# Load all languages
all_languages = load_dataset("CraneAILabs/wildjailbreak-africa")
```

### Manual Loading

```python
import json

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

# Load Swahili samples
swahili_data = load_jsonl("swa/train.jsonl")
```

## Original Dataset Information

- **Source**: ai2-adapt-dev/tulu_v3.9_wildjailbreak_decontaminated_50k
- **Original Dataset**: [WildJailbreak](https://huggingface.co/datasets/allenai/wildjailbreak) (262K samples)
- **Subset Used**: Decontaminated 50K samples from [Tulu 3 SFT Mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture)
- **Purpose**: Safety training and jailbreak resistance
- **License**: ODC-BY-1.0

The WildJailbreak dataset was designed to mitigate exaggerated safety behaviors by providing:
1. **Harmful queries** (both vanilla and adversarial)
2. **Benign queries** that resemble harmful queries but contain no harmful intent

## Translation Process

The translations were performed using advanced AI translation systems by Crane AI Labs with the following considerations:
- Maintenance of conversational context and flow
- Cultural adaptation where appropriate
- Preservation of safety-related content structure
- Quality control through automated consistency checks
- Native speaker review and validation

## Intended Use Cases

### Primary Use Cases
- **Safety Training**: Training African language models to handle harmful content appropriately
- **Instruction Tuning**: Fine-tuning conversational AI models for African languages
- **Jailbreak Research**: Studying adversarial prompt behavior in low-resource languages
- **Cross-lingual Safety**: Understanding safety patterns across linguistic boundaries

### Research Applications
- Multilingual safety alignment research
- Low-resource language model development
- Cultural adaptation of AI safety measures
- Comparative analysis of harmful content across languages

## Limitations and Considerations

### Translation Limitations
- **Automated Translation**: Content was translated using AI systems, which may introduce:
  - Semantic drift from original meaning
  - Cultural context misalignment
  - Grammatical inconsistencies
  - Loss of nuanced safety-related expressions

### Cultural Considerations
- **Western-Centric Content**: Original dataset reflects Western cultural contexts that may not align with African cultural norms
- **Harmful Content Relevance**: Some harmful scenarios may not be culturally relevant or may carry different implications in African contexts
- **Social Norms**: Safety boundaries and social taboos vary significantly across cultures

### Technical Limitations
- **Data Quality**: Translation quality varies across languages and complexity of content
- **Consistency**: Terminology and style may not be consistent within or across languages
- **Coverage**: Some nuanced safety concepts may not translate effectively

### Ethical Considerations
- **Harmful Content**: Dataset contains translated harmful prompts that could be misused
- **Cultural Sensitivity**: Some content may be inappropriate or offensive in local cultural contexts
- **Representation**: May not adequately represent diverse dialects and regional variations

### Safety Warnings
⚠️ **Content Warning**: This dataset contains potentially harmful, offensive, or inappropriate content translated into African languages. Users should:
- Implement appropriate safeguards when using this data
- Consider cultural context when applying safety measures
- Use only for legitimate research and safety training purposes
- Avoid deployment without proper safety evaluations

### Data Quality Limitations
- **Translation Artifacts**: May contain artifacts from automated translation processes
- **Inconsistent Quality**: Quality varies significantly between simple and complex prompts
- **Missing Context**: Some cultural or contextual nuances may be lost in translation

## Evaluation and Validation

### Recommended Validation Steps
1. **Human Review**: Conduct human evaluation of translated content for cultural appropriateness
2. **Safety Testing**: Evaluate model outputs for culturally appropriate safety responses
3. **Quality Assessment**: Assess translation quality using native speaker evaluation
4. **Cultural Adaptation**: Validate that safety measures align with local cultural norms

### Metrics to Consider
- Translation quality (BLEU, chrF++, human evaluation)
- Cultural appropriateness scores
- Safety response effectiveness
- Cross-lingual consistency

## Responsible Use Guidelines

### Do's
✅ Use for legitimate AI safety research  
✅ Implement proper content filtering and safeguards  
✅ Conduct cultural sensitivity reviews  
✅ Validate with native speakers before deployment  
✅ Credit original dataset creators and translators  

### Don'ts
❌ Deploy without proper safety evaluation  
❌ Use for generating harmful content  
❌ Ignore cultural context and local norms  
❌ Assume uniform quality across all samples  
❌ Use as the sole source for production systems  

## Citation

If you use this dataset, please cite both this work and the original WildJailbreak dataset:

```bibtex
@dataset{wildjailbreak_africa,
  title={WildJailbreak Africa: Tulu 3.9 WildJailbreak African Languages Dataset},
  author={Crane AI Labs},
  year={2025},
  url={https://huggingface.co/datasets/CraneAILabs/wildjailbreak-africa}
}

@dataset{wildjailbreak,
  title={WildJailbreak: An Open-source Large-scale Synthetic Jailbreak Dataset},
  author={Shen, Liwei and Tao, Zhihong and Cheng, Pengfei and others},
  year={2024},
  url={https://huggingface.co/datasets/allenai/wildjailbreak}
}
```

## Contributing

We welcome contributions to improve translation quality, add more languages, or enhance cultural appropriateness. Please:

1. Ensure cultural sensitivity in all contributions
2. Provide proper documentation for changes
3. Include validation metrics for improvements

## License

This dataset follows the licensing terms of the original WildJailbreak dataset (ODC-BY-1.0). Please review the original dataset license before use.

## Contact

For questions, concerns, or contributions, please contact:
- **Email**: bakungabronson@gmail.com
- **Organization**: Crane AI Labs
- **HuggingFace**: [CraneAILabs](https://huggingface.co/CraneAILabs)

---

**Dataset Statistics:**
- **Total Conversations**: 299,283
- **Languages**: 6 (English + 5 African languages)
- **Format**: JSONL (JSON Lines)
- **Size**: ~600MB (estimated)
- **Split**: Train only

**Contributors:** Crane AI Labs

**Last Updated**: August 2025