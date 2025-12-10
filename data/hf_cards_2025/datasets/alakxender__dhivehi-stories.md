---
license: mit
task_categories:
- feature-extraction
- text-generation
language:
- dv
pretty_name: dhivehi_stories
tags:
- thaana
- dhivehi
- vaahaka
size_categories:
- 10K<n<100K
---
# Dhivehi Stories Dataset

A collection of **13,956 translated Dhivehi (Maldivian) stories** with summaries and standardized metadata. Text is in Thaana script and cleaned for consistency, though sentence flow may not always be natural and some non-local names may appear.

## Dataset Description

This dataset contains 13,956 stories written in Dhivehi (ދިވެހި), the official language of the Maldives. Each story includes:
- **Original story text** in Dhivehi
- **Summary** in Dhivehi  
- **Metadata** including features, key words, character names, and genres

## Dataset Structure

### Fields

- **`dv_story`**: The complete story text in Dhivehi
- **`dv_summary`**: A summary of the story in Dhivehi
- **`metadata`**: Rich metadata containing:
  - `dv_features`: Cultural and thematic features
  - `dv_words`: Key vocabulary words from the story
  - `dv_character_name`: Character names mentioned in the story
  - `en_genre`: Genre classification in English

### Statistics

- **Total Stories**: 13,956
- **Average Story Length**: 1009 characters
- **Average Summary Length**: 173 characters
- **Unique Features**: 2558
- **Unique Words**: 6868
- **Unique Characters**: 2926
- **Unique Genres**: 119

## Top Categories

### Most Common Features
- **ރަހުމަތްތެރިކަން**: 2,345 stories (16.8%)
- **ޑައިލޮގް**: 1,256 stories (9.0%)
- **ޓްވިސްޓް**: 1,148 stories (8.2%)
- **އެކުވެރިކަން**: 900 stories (6.4%)
- **މަޖާ**: 810 stories (5.8%)
- **އުފާވެރިކަން**: 805 stories (5.8%)
- **އެހީވުން**: 790 stories (5.7%)
- **ސަޕްރައިޒް**: 554 stories (4.0%)
- **ހިތްވަރު**: 453 stories (3.2%)
- **ކޮންފްލިކްޓް**: 452 stories (3.2%)


### Most Common Genres
- **Children**: 4,607 stories (33.0%)  
- **Fable**: 2,042 stories (14.6%)  
- **Fantasy**: 1,823 stories (13.1%)  
- **Adventure**: 1,348 stories (9.7%)  
- **Moral**: 898 stories (6.4%)  
- **Family**: 728 stories (5.2%)  
- **Friendship**: 652 stories (4.7%)  
- **Drama**: 226 stories (1.6%)  

### Most Frequent Words
- **ދޫނި**: 1,072 stories (7.7%)
- **ބޯޅަ**: 881 stories (6.3%)
- **ބުޅާ**: 832 stories (6.0%)
- **ރަހުމަތްތެރި**: 758 stories (5.4%)
- **ކުއްތާ**: 695 stories (5.0%)
- **އުފާ**: 615 stories (4.4%)
- **މަޖާ**: 611 stories (4.4%)
- **ރަހުމަތްތެރިން**: 498 stories (3.6%)
- **ގަސް**: 289 stories (2.1%)
- **ރީތި**: 273 stories (2.0%)


## Example Story

**Story Text:**
```
އެއްދުވަހަކު ބޮޑު ދަނޑެއްގައި ފެހި ހުޅަނގު ވިއެވެ. ހުޅަނގުގައި ވަލެއް ކުޑަ ކުޑަ ފަނިއެއް އުޅުނެވެ. އޭނާގެ ނަމަކީ ޒިޔާދެވެ. ޒިޔާދު ހުޅަނގުގައި މަތިމައްޗަށް ފުންމުމަށް ލޯބި ކުރެއެވެ. އެއްދުވަހަކު ޒިޔާދު ބޮޑު ފަނިއެއް އާދެވުނެވެ. އޭނާގެ ނަމަކީ ސަމާހެވެ. ސަމާހު ވަރަށް ބޮޑެވެ، ނަމަވެސް އޭނާ ނުރައްކާތެރިއެއް ނޫނެވެ. ސަމާހު ޒިޔާދުއާއެކު ކުޅެން ލޯބި ކުރެއެވެ.
"އަހަރެމެން އެކުގައި މަތިމައްޗަށް ފުންމަމާ!" ޒިޔާދު ސަމާހުއަށް ބުންޏެވެ. އެމީހުން ހުޅަނގުގައި ކުޅެން މަޖާވިއެވެ. ކުއްލިއަކަށް ބޮޑު ހިޔަނިއެއް ފެނު...
```

**Summary:**
```
ކުޑަ ފަނިއަކާއި ބޮޑު ފަނިއެއް ހުޅަނގުގައި ކުޅެން އުޅެނިކޮށް ދޫންޏެއް ފެނި ބިރުގަނެ، ނަމަވެސް ދޫނި ކުޅެން ބޭނުންވުމުން ތިން މީހުން ރަޙްމަތްތެރިންނަށް ވެއްޖެއެވެ.
```

**Metadata:**
```json
{
  "dv_features": [
    "ޓްވިސްޓް",
    "މިތުރުވުން"
  ],
  "dv_words": [
    "ފަނި",
    "ފުންމުން",
    "ރަޙްމަތްތެރިން"
  ],
  "dv_character_name": [
    "ޒިޔާދު",
    "ސަމާހު"
  ],
  "en_genre": "Fantasy"
}
```

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("alakxender/alakxender-dhivehi-stories")

# Access a story
story = dataset["train"][0]
print("Story:", story["dv_story"])
print("Summary:", story["dv_summary"]) 
print("Features:", story["metadata"]["dv_features"])
```

### Filtering by Genre

```python
# Filter stories by genre
children_stories = dataset["train"].filter(
    lambda x: x["metadata"]["en_genre"] == "Children"
)
```

### Analyzing Features

```python
# Get all unique features
all_features = []
for story in dataset["train"]:
    if story["metadata"]["dv_features"]:
        all_features.extend(story["metadata"]["dv_features"])

unique_features = list(set(all_features))
print(f"Total unique features: {len(unique_features)}")
```

## Applications

This dataset can be used for:

- **Language Model Training**: Fine-tuning models for Dhivehi text generation
- **Educational Tools**: Developing Dhivehi language learning resources
- **Cross-lingual Studies**: Comparing storytelling across cultures
- **Text Summarization**: Training summarization models for Dhivehi
- **Genre Classification**: Building genre classification systems

## Data Quality

* Stories are cleaned and translated from LLM outputs with some Dhivehi support
* Thaana script encoding is handled correctly
* Metadata is standardized
* Duplicates are removed

**Note:** These stories contain Dhivehi text, but sentence structure may not match natural storytelling. Non-cultural and non-local names can appear.
