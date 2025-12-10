---
license: cc0-1.0
task_categories:
- question-answering
- text-classification
- text-generation
language:
- en
tags:
- education
- curriculum
- teks
- texas
- k12
- training
- instruction-tuning
- educational-ai
size_categories:
- 1K<n<10K
---

# CCISD TEKS Training Dataset

## Dataset Description

This is a **training-ready** dataset with 4,200+ examples derived from Texas Essential Knowledge and Skills (TEKS) standards for 25 high school courses. Designed for fine-tuning language models on educational curriculum tasks.

### Dataset Summary

- **Total Examples**: 4,224
- **Training Set**: 2,956 (70%)
- **Validation Set**: 633 (15%)
- **Test Set**: 635 (15%)
- **Source Courses**: 25 high school courses
- **Source Standards**: 428 TEKS standards
- **Task Types**: 10+ educational tasks

### Supported Tasks

**Question Answering**:
- TEKS standard definitions
- Course identification
- Strand classification
- Lesson objective generation

**Text Classification**:
- Bloom's Taxonomy level classification
- Subject area classification
- STAAR testing status classification

**Text Completion**:
- Standard completion
- Assessment question generation

### Training Examples

**Example 1: TEKS Definition QA**
```
Input: "What is TEKS standard ELAR.9.1.A?"
Output: "engage in meaningful and respectful discourse when evaluating the clarity and coherence of a speaker's message..."
```

**Example 2: Bloom's Classification**
```
Input: "analyze and explain the interrelationship of physical, mental, and social health"
Output: "Analyzing"
```

**Example 3: Course Identification**
```
Input: "Which course covers: create algorithms for the solution of various problems?"
Output: "Fundamentals of Computer Science (Other)"
```

## Dataset Structure

### Data Fields

- `input`: The input text/question for the model
- `output`: The expected output/answer
- `task_type`: Type of educational task (e.g., 'teks_definition', 'blooms_classification')
- `course`: Course name the example relates to
- `teks_code`: TEKS standard code (if applicable)
- `format`: Example format ('qa', 'classification', 'completion')

### Data Splits

| Split | Examples | Percentage |
|-------|----------|------------|
| Train | 2,956 | 70% |
| Validation | 633 | 15% |
| Test | 635 | 15% |

### Task Type Distribution

- **TEKS Definition QA**: ~428 examples
- **Course Identification**: ~428 examples
- **Strand Classification**: ~428 examples
- **Bloom's Classification**: ~856 examples
- **Lesson Objective Generation**: ~428 examples
- **Subject Classification**: ~428 examples
- **STAAR Classification**: ~428 examples
- **Text Completion**: ~400 examples
- **Assessment Generation**: ~400 examples

## Dataset Creation

### Source Data

Derived from the **CCISD TEKS Alignment Dataset** which maps Texas TEKS standards to 25 high school courses across:
- English Language Arts (4 courses)
- Mathematics (4 courses)
- Science (6 courses)
- Social Studies (5 courses)
- Foreign Languages (3 courses)
- Health (1 course)
- Computer Science (2 courses)

### Data Expansion Process

Each of the 428 TEKS standards was expanded into multiple training examples:

1. **Question-Answer Pairs** (5 per standard):
   - Standard definition
   - Course identification
   - Strand classification
   - Bloom's level identification
   - Lesson objective generation

2. **Classification Examples** (3 per standard):
   - Bloom's Taxonomy classification
   - Subject area classification
   - STAAR testing classification

3. **Text Completion Examples** (2 per standard):
   - Standard completion tasks
   - Assessment generation tasks

### Annotations

- **Bloom's Taxonomy**: Expert-classified cognitive levels
- **STAAR Status**: Verified against Texas Education Agency specifications
- **Subject Areas**: Official PEIMS course classifications
- **Task Types**: Structured for instruction-tuning

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load full dataset
dataset = load_dataset("robworks-software/ccisd-teks-training")

# Access splits
train_data = dataset['train']
val_data = dataset['validation']
test_data = dataset['test']

# Example usage
for example in train_data:
    print(f"Input: {example['input']}")
    print(f"Output: {example['output']}")
    print(f"Task: {example['task_type']}")
```

### Fine-tuning Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# Prepare dataset
def tokenize_function(examples):
    prompts = [f"Question: {inp}
Answer:" for inp in examples['input']]
    model_inputs = tokenizer(prompts, truncation=True, max_length=512)
    labels = tokenizer(examples['output'], truncation=True, max_length=512)
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Train
training_args = TrainingArguments(
    output_dir="./teks-tuned-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['validation']
)

trainer.train()
```

## Intended Use

### Primary Uses

- **Fine-tuning LLMs** for educational curriculum tasks
- **Educational chatbot training** for TEKS-aligned assistance
- **Curriculum planning AI** development
- **Automated lesson plan generation**
- **Standards-based assessment creation**

### Out-of-Scope Uses

- Non-Texas educational contexts (without domain adaptation)
- K-8 grade levels (dataset is high school focused)
- Real-time student assessment (requires additional safety measures)

## Considerations for Using the Data

### Limitations

- **Geographic Specificity**: Texas-specific TEKS standards
- **Grade Level**: High school only (grades 9-12)
- **Synthetic Examples**: Expanded from 428 base standards
- **No Student Data**: No actual student performance or PII

### Bias and Fairness

- Standards reflect Texas state curriculum requirements
- May not represent diverse pedagogical approaches
- English-only (Spanish/French language courses not in Spanish/French)

## Additional Information

### Licensing

**CC0-1.0 (Public Domain Dedication)** - Texas TEKS standards are government works in the public domain per 17 U.S.C. § 105 and Texas Public Information Act Chapter 552.

**Required Attribution**: Texas Education Agency (TEA) - Texas Essential Knowledge and Skills

### Citation

```bibtex
@dataset{ccisd_teks_training_2025,
  title={CCISD TEKS Training Dataset},
  author={Robworks Software},
  year={2025},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/datasets/robworks-software/ccisd-teks-training}}
}
```

### Related Datasets

- **CCISD TEKS Alignment**: Base dataset with 428 raw TEKS standards
- **Texas Comprehensive Dataset**: Broader Texas educational data

### Contact

- **Organization**: Robworks Software
- **Purpose**: Educational AI and curriculum technology development
- **Applications**: LessonCraft, QuizCraft, SimCraft platforms

### Version History

- **v1.0 (2025-10-03)**: Initial release
  - 4,224 training examples
  - 10+ task types
  - 70/15/15 train/val/test split
  - Derived from 25 courses, 428 TEKS standards
