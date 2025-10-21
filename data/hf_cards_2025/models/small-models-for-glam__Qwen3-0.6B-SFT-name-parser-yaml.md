---
base_model: Qwen/Qwen3-0.6B
library_name: transformers
model_name: Qwen3-0.6B-SFT-name-parser-yaml
tags:
- generated_from_trainer
- trl
- sft
- name-parsing
- cultural-heritage
- yaml
- nlp
license: apache-2.0
language:
- en
- multilingual
pipeline_tag: text-generation
---

# Model Card for Qwen3-0.6B-SFT-name-parser-yaml

This model is a fine-tuned version of [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) specifically designed for parsing cultural heritage person names into structured YAML format. It has been trained using [TRL](https://github.com/huggingface/trl) with supervised fine-tuning (SFT).

## Model Description

This specialized model parses person names from cultural heritage contexts (libraries, archives, museums) into structured YAML format with the following fields:
- `first_name`: Person's given name
- `last_name`: Person's family name or surname
- `middle_names`: List of middle names or initials
- `temporal`: List of temporal information (birth, death, flourished dates)
- `titles`: List of titles, honorifics, or professional designations
- `extra_info`: List of additional information (places, affiliations)

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "small-models-for-glam/Qwen3-0.6B-SFT-name-parser-yaml"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# Parse a person name
input_name = "Dr. Jane Smith-Jones, 1850-1920"
prompt = "Parse this person name:\n\n" + input_name

messages = [{"role": "user", "content": prompt}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(**model_inputs, max_new_tokens=512)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

# Parse thinking content if present
try:
    index = len(output_ids) - output_ids[::-1].index(151668)  # </think> token
except ValueError:
    index = 0

content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip()
print(content)
```

Expected output:
```yaml
first_name: Jane
last_name: Smith-Jones
middle_names: []
temporal:
- start: 1850
  end: 1920
  type: life_span
titles:
- Dr.
extra_info: []
```

## Supported Name Patterns

The model handles a wide variety of name formats commonly found in cultural heritage contexts:

### Basic Patterns
- `John Smith`
- `Smith, John`
- `Dr. John Smith`
- `John A. Smith`

### Complex Patterns
- `Baron William Henry Ashe A'Court Heytesbury, c. 1809-1891`
- `Jones, James Earl, Dr., (fl. 1850-1900)`
- `Miller, Chester F. (Chester Frederic), 1886-`
- `Rábade Obradó, Ana Isabel`
- `彭大铨` (Chinese names)

### Edge Cases
- **Mononyms**: `Salzmann`, `Mokamba`
- **Initials**: `J. F. Vitry`, `A. E. Borie`
- **Diacritics**: `Péporté`, `Gerencsér`
- **Temporal data**: `Rosana, 1963-`
- **Parenthetical expansions**: `T. (Takeshi) Ohba`

## Training Procedure

### Training Data
The model was trained on a synthetic dataset of 1,000+ examples generated using a comprehensive template-based approach that covers:
- **70% regular examples**: Standard name patterns with various combinations of fields
- **30% edge cases**: Challenging patterns including mononyms, initials, diacritics, and non-Western names

### Data Generation Features
- **Multi-cultural support**: Names from English, French, German, Italian, Spanish, Dutch, Arabic, and Chinese contexts
- **Temporal data variety**: Birth/death dates, flourished periods, single dates
- **Title diversity**: Academic, religious, nobility, military, and professional titles
- **Complex surnames**: Hyphenated, apostrophized, and particle-based surnames (van, von, de, al-, ibn)

### Training Configuration
- **Base model**: Qwen/Qwen3-0.6B
- **Training method**: Supervised Fine-Tuning (SFT) using TRL
- **Output format**: YAML with consistent field ordering
- **Chat template**: Standard user/assistant format with "Parse this person name:" prompt

### Framework Versions
- TRL: 0.23.0
- Transformers: 4.56.2
- PyTorch: 2.8.0
- Datasets: 4.1.1
- Tokenizers: 0.22.1

## Performance

The model demonstrates strong performance on cultural heritage name parsing tasks:
- Handles diverse international name formats
- Correctly identifies and structures temporal information
- Processes titles, honorifics, and professional designations
- Manages complex surname patterns and particles
- Supports mononyms and abbreviated names

## Limitations

- Primarily trained on Western and East Asian name patterns
- May struggle with very rare or highly specialized naming conventions
- Temporal date parsing assumes Gregorian calendar years
- Limited support for ancient or historical dating systems (BCE, regnal years)

## Intended Use

### Primary Use Cases
- **Digital humanities**: Processing historical person names in manuscripts and documents
- **Library science**: Cataloging and standardizing author names in bibliographic records
- **Archive management**: Structuring person names in archival finding aids
- **Museum collections**: Organizing creator and subject names in cultural heritage databases

### Out-of-Scope Use
- Modern person name parsing for contemporary applications
- Legal document processing requiring high precision
- Real-time person identification or verification
- Processing of fictional character names

## Ethical Considerations

- The model reflects naming conventions present in its training data
- Cultural biases may exist toward Western naming patterns
- Should not be used for identity verification or legal purposes
- Consider cultural sensitivity when processing names from different traditions

## Framework Citation

Cite TRL as:
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallou{\'e}dec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```

## Model Card Contact

For questions about this model card or the model itself, please open an issue in the [project repository](https://huggingface.co/small-models-for-glam/Qwen3-0.6B-SFT-name-parser-yaml/discussions).
