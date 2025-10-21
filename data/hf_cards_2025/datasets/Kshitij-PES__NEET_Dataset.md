---
license: apache-2.0
language:
- en
pretty_name: NEET Previous Year Questions for Fine-Tuning
tags:
- chemistry
- biology
- physics
- question-answering
- multiple-choice
- instruction-tuning
- education
- exam-preparation
- neet
task_categories:
- question-answering
size_categories:
- n<1K
---

# Dataset Card for NEET Previous Year Questions (PYQs)

## Dataset Summary

This dataset contains a collection of Previous Year Questions (PYQs) from India's National Eligibility cum Entrance Test (NEET-UG), a highly competitive entrance examination for medical and dental courses. The questions cover the subjects of **Chemistry**, **Biology**, and **Physics**.

Each entry in the dataset is structured as a JSON object containing the question, four multiple-choice options, the key for the correct answer, and a brief explanation for the solution. This format makes it ideal for a variety of Natural Language Processing (NLP) tasks, particularly for fine-tuning language models for educational applications, question-answering, and explanation generation.

The dataset includes questions from the following years:
- **NEET 2021** (Chemistry & Biology)
- **NEET 2023** (Chemistry & Biology)
- **NEET 2025 Mock Paper** (Chemistry)

## Supported Tasks and Leaderboards

This dataset is primarily designed for:

- **Question Answering:** Models can be trained to select the correct option given the question. This is a multiple-choice QA task.
- **Instruction Fine-Tuning:** The structured format is perfect for fine-tuning models to follow instructions, such as answering exam-style questions and providing explanations.
- **Text Generation:** The dataset can be used to train models to generate new questions, explanations, or even incorrect options (distractors) based on a given context or topic.

## Dataset Structure

The dataset consists of a collection of JSON objects, where each object represents a single question.

### Data Instances

A typical data instance looks like this:

```json
{
  "question_id": "NEET_2023_CHE_27",
  "subject": "Chemistry",
  "question": "Consider the following reaction and identify the product (P). 3-Methylbutan-2-ol + HBr → Product (P)",
  "options": {
    "1": "2-Bromo-3-methylbutane",
    "2": "2-Bromo-2-methylbutane",
    "3": "1-Bromo-3-methylbutane",
    "4": "1-Bromo-2-methylbutane"
  },
  "correct_answer_key": "2",
  "brief_explanation": "The reaction proceeds via a carbocation mechanism. Protonation of the -OH group followed by loss of water forms a secondary carbocation. This secondary carbocation undergoes a 1,2-hydride shift from the adjacent carbon to form a more stable tertiary carbocation. The bromide ion (Br⁻) then attacks this tertiary carbocation to form the major product, 2-bromo-2-methylbutane."
}
```

### Data Fields

- **question_id:** A unique identifier for each question, typically in the format `NEET_{YEAR}_{SUBJECT_CODE}_{QUESTION_NUMBER}`.
- **subject:** The subject of the question (e.g., "Chemistry", "Biology").
- **question:** The full text of the question. This may include context, chemical reactions, or data tables.
- **options:** A JSON object containing the four multiple-choice options, with keys "1", "2", "3", and "4".
- **correct_answer_key:** A string representing the key from the options object that corresponds to the correct answer.
- **brief_explanation:** A concise explanation detailing the reasoning behind the correct answer, including relevant concepts, formulas, or reaction mechanisms.

### Data Splits

The dataset is organized by year. It is recommended to load the data and create your own training, validation, and test splits as needed for your specific use case. For example, you could use the 2021 and 2025 mock papers for training and the 2023 paper for validation/testing.

## Use Cases for Fine-Tuning

This dataset is particularly well-suited for instruction fine-tuning small-to-medium-sized language models (e.g., 1.5B parameter models). Here are some example prompt formats you could use:

### 1. Instruction Following / Q&A

You can format the data to teach a model how to answer multiple-choice questions based on an instruction.

**Alpaca-style format:**

```json
{
  "instruction": "Answer the following multiple-choice question from the NEET exam and provide a brief explanation.",
  "input": "Question: The stability of Cu²⁺ is more than Cu⁺ salts in aqueous solutions due to what reason?\nOptions:\n1: second ionisation enthalpy\n2: first ionisation enthalpy\n3: enthalpy of atomisation\n4: hydration energy",
  "output": "The correct answer is 4. The much higher (more negative) hydration enthalpy of the smaller, more highly charged Cu²⁺ ion in aqueous solution more than compensates for the high second ionization enthalpy, making Cu²⁺(aq) more stable than Cu⁺(aq)."
}
```

### 2. Explanation Generation

You can train the model to provide an explanation for a given question and its correct answer.

```json
{
  "instruction": "Explain why the given answer to the question is correct.",
  "input": "Question: Which one of the following reactions does NOT give benzene as the product?\nOptions:\n1: Sodium benzoate with sodalime\n2: n-hexane with Mo₂O₃ at 773K\n3: Acetylene through red hot Iron Tube\n4: Benzenediazonium chloride with warm water\nCorrect Answer: 4",
  "output": "The reaction of benzenediazonium chloride with warm water is a hydrolysis reaction that produces phenol (C₆H₅OH) and nitrogen gas, not benzene. The other three reactions—decarboxylation, aromatization, and cyclic polymerization—all yield benzene as a product."
}
```

## Dataset Creation

The data in this collection was curated from official NEET-UG Previous Year Question papers. The questions, options, and answers were transcribed from publicly available sources. The `brief_explanation` for each question was generated to provide educational context and to make the dataset more useful for fine-tuning tasks that require reasoning.

## Considerations for Using the Data

- **Accuracy:** While care has been taken to ensure the accuracy of the questions, answers, and explanations, errors from transcription or interpretation may exist. Users should verify critical information.
- **Scope:** The dataset is not an exhaustive collection of all NEET questions but covers a significant portion of recent papers in specific subjects.
- **Bias:** The dataset is inherently biased towards the curriculum and question patterns of the NEET-UG examination in India. It is specialized for science education in this context and is not a general-knowledge Q&A dataset.

## Additional Information

### Licensing Information

This dataset is licensed under the **Apache License 2.0**.

### Citation Information

If you use this dataset in your research or project, please consider citing it as follows:

```bibtex
@misc{neet_pyq_dataset_2025,
  author    = {Kshitij Gupta},
  title     = {NEET Previous Year Questions for Fine-Tuning},
  year      = {2025},
  publisher = {Hugging Face},
  journal   = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/datasets/Kshitij-PES/NEET_Dataset/Dataset.json}}
}
```

### Dataset Curator

**Kshitij Gupta** ([Kshitij-PES](https://github.com/kshitij030323))

---