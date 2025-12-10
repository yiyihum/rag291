---
pretty_name: Kazakhstan Government Complaints Dataset
license: apache-2.0
language:
- kk
- ru
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
source_datasets: []
annotations_creators:
- machine-generated
language_creators:
- machine-generated
task_categories:
- text-classification
- text-generation
task_ids:
- sentiment-analysis
- multi-class-classification
tags:
- synthetic-data
- government
- citizen-complaints
- kazakhstan
- kazakh
- russian
- multilingual
- public-services
- gemini-2.5-pro
- text-generation
- sentiment-analysis
- complaint-analysis
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: text_kz
    dtype: string
  - name: text_ru
    dtype: string
  - name: category
    dtype: string
  - name: urgency
    dtype: string
  - name: region
    dtype: string
  - name: status
    dtype: string
  - name: sentiment
    dtype: string
  - name: urgency_level
    dtype: string
  - name: date_created
    dtype: string
  - name: reply_text
    dtype: string
  - name: duplicate
    dtype: bool
  download_size: 256268
  dataset_size: 672010
---
# Kazakhstan Government Complaints Dataset (Kazakh/Russian)

## Dataset Summary

This dataset contains synthetically generated citizen complaints directed to the Kazakhstan government along with estimated government responses. The data is generated using Gemini 2.5 Pro and includes complaints written in both Kazakh (kz) and Russian (ru) languages, reflecting the linguistic diversity of Kazakhstan's population.

The dataset aims to facilitate research in natural language processing, government-citizen interaction analysis, and multilingual text generation for Central Asian languages, particularly in the context of public service improvement and citizen engagement.

## Dataset Details

### Dataset Description

- **Homepage:** [Hugging Face Dataset](https://huggingface.co/datasets/Adilbai/kz-gov-complaints-data-kz-ru)
- **Repository:** [GitHub Repository](https://github.com/AdilzhanB)
- **Paper:** N/A
- **Point of Contact:** Adilzhan Baidalin (AdilzhanB)

### Dataset Summary

This synthetic dataset contains citizen complaints to the Kazakhstan government covering various public service domains including healthcare, education, infrastructure, social services, and administrative processes. Each complaint is paired with an estimated government response, providing a comprehensive view of citizen-government communication patterns.

## Languages

- **Kazakh (kz)**: Official state language of Kazakhstan
- **Russian (ru)**: Official language widely used in Kazakhstan

## Dataset Structure

### Data Instances

Each instance in the dataset contains:
- **complaint_text**: The citizen's complaint or concern
- **government_response**: Estimated government response to the complaint
- **language**: Language code (kz/ru)
- **category**: Complaint category (e.g., healthcare, education, infrastructure)
- **sentiment**: Sentiment analysis of the complaint (positive, negative, neutral)
- **urgency_level**: Assessed urgency level (low, medium, high)

### Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `complaint_text` | string | The main text of the citizen's complaint |
| `government_response` | string | Estimated government response to the complaint |
| `language` | string | Language code: 'kz' for Kazakh, 'ru' for Russian |
| `category` | string | Complaint category (healthcare, education, infrastructure, etc.) |
| `sentiment` | string | Sentiment of the complaint (positive, negative, neutral) |
| `urgency_level` | string | Urgency assessment (low, medium, high) |
| `date_created` | string | Synthetic date when the complaint was created |
| `region` | string | Kazakhstan region/oblast associated with the complaint |

### Data Splits

| Split | Size |
|-------|------|
| Train | TBD |
| Validation | TBD |
| Test | TBD |

## Dataset Creation

### Curation Rationale

This dataset was created to address the lack of publicly available government-citizen communication data in Kazakh and Russian languages. It serves multiple purposes:

1. **Research enablement**: Facilitating NLP research for underrepresented Central Asian languages
2. **Government technology**: Supporting development of automated complaint processing systems
3. **Multilingual AI**: Advancing multilingual understanding for Kazakh-Russian language pairs
4. **Public service innovation**: Providing insights into citizen concerns and government response patterns

### Source Data

#### Initial Data Collection and Normalization

The dataset is entirely synthetic, generated using Google's Gemini 2.5 Pro language model. The generation process involved:

1. **Prompt engineering**: Carefully crafted prompts to generate realistic citizen complaints
2. **Cultural context**: Incorporation of Kazakhstan-specific cultural, social, and administrative contexts
3. **Language diversity**: Balanced generation across Kazakh and Russian languages
4. **Response simulation**: Government responses modeled on official communication styles

#### Who are the source language producers?

The synthetic data is generated by Gemini 2.5 Pro, trained to understand and produce text in multiple languages including Kazakh and Russian. The model was prompted to generate content that reflects authentic citizen concerns and appropriate government response patterns.

### Annotations

#### Annotation process

Annotations were automatically generated during the synthesis process, including:
- Language detection and labeling
- Sentiment analysis using multilingual sentiment models
- Category classification based on complaint content
- Urgency assessment based on complaint severity and type

#### Who are the annotators?

Annotations were generated automatically using pre-trained multilingual models and rule-based systems. No human annotators were involved in the process.

## Considerations for Using the Data

### Social Impact of Dataset

This dataset can contribute positively to:
- **Government transparency**: Improving understanding of citizen concerns
- **AI democratization**: Providing resources for Kazakh and Russian NLP
- **Public service improvement**: Enabling analysis of complaint patterns
- **Digital government**: Supporting development of citizen service technologies

### Discussion of Biases

Potential biases to consider:
- **Synthetic bias**: May not fully represent real citizen complaint patterns
- **Language model bias**: Inherits any biases present in Gemini 2.5 Pro
- **Cultural representation**: May not capture all cultural nuances of Kazakhstan's diverse population
- **Urban/rural bias**: Synthetic data may lean toward urban concerns

### Other Known Limitations

- **Synthetic nature**: Data is artificially generated and may not reflect real complaint distributions
- **Response accuracy**: Government responses are estimated and may not match actual government practices
- **Cultural specificity**: Some cultural nuances may be lost in synthetic generation
- **Legal considerations**: Should not be used as representative of actual government-citizen interactions

## Additional Information

### Dataset Curators

- **Adilzhan Baidalin** (AdilzhanB) - Dataset creator and maintainer

### Citation Information

```bibtex
@dataset{baimenov2024kz_gov_complaints,
  title={Kazakhstan Government Complaints Dataset (Kazakh/Russian)},
  author={Baimenov, Adilzhan},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Adilbai/kz-gov-complaints-data-kz-ru}
}
```

### Contributions

Thanks to [@AdilzhanB](https://github.com/AdilzhanB) for creating this dataset to support NLP research in Central Asian languages and government-citizen interaction studies.

## Usage Examples

### Loading the dataset

```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("Adilbai/kz-gov-complaints-data-kz-ru")

# Load specific language subset
dataset_kz = dataset.filter(lambda x: x['language'] == 'kz')
dataset_ru = dataset.filter(lambda x: x['language'] == 'ru')

# Load specific category
healthcare_complaints = dataset.filter(lambda x: x['category'] == 'healthcare')
```

### Basic analysis

```python
# Analyze complaint categories
categories = dataset['train']['category']
from collections import Counter
category_counts = Counter(categories)
print(category_counts)

# Analyze language distribution
languages = dataset['train']['language']
language_counts = Counter(languages)
print(language_counts)
```

## Contact

For questions, suggestions, or collaboration opportunities, please contact:
- **GitHub**: [@AdilzhanB](https://github.com/AdilzhanB)
- **Hugging Face**: [Adilbai](https://huggingface.co/Adilbai)

---

*This dataset is part of ongoing efforts to advance NLP capabilities for Central Asian languages and improve government-citizen digital interactions.*
