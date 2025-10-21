---
tags:
- dental
- healthcare
- medical
- synthetic
- clinical-cases
- instruction-tuning
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
size_categories:
- 1K<n<10K
---

# Dental Training Dataset (Synthetic)

Synthetic dataset of 2,494 dental clinical cases for training Dental-GPT, a specialized language model for dental diagnosis and treatment planning.

## Dataset Details

- **Size**: 2,494 synthetic dental cases
- **Format**: JSONL with structured conversations
- **Synthetic**: Artificially generated cases (no real patient data)
- **Purpose**: Training dental diagnostic AI models
- **Language**: English
- **Metadata**: Croissant format available for automated discovery

## Dataset Processing Pipeline

### Initial Data Audit

- **Found 2494 total cases** in dataset
- **Placeholder patterns** (e.g., "Patient reports symptoms began approximately 2 weeks ago") dominated content
- Identified need for clinical enhancement to create realistic, diagnostically useful cases

### Clinical Enhancement

- **Demographics enrichment**: Added age ranges (18–75), gender balance, diverse occupations
- **Condition-specific insertions**:
  - Caries vs. periodontal disease vs. cysts vs. mucosal lesions
  - Matching radiographic findings (periapical radiolucency, bone loss patterns, cystic expansion, etc.)
  - Urgency levels (0 = elective, 1 = moderate, 2 = urgent)
- **Structured clinical narratives** with realistic patient presentations

### Full Pipeline Application

- **Continuous refinements** and enhancements to achieve final 2494 cases
- **Expert feedback integration** throughout development process
- **LLM-as-judge fine-tuning** to establish robust causal links between symptoms and diagnoses
- **Iterative validation** against clinical guidelines and expert consensus

### Quality Control Gates

- **JSON schema validation**: Ensured all required fields present (`diagnosis`, `etiology`, `urgency`, `management`, `abx`, `follow_up`, `counseling`, `guideline`)
- **Internal consistency checks**:
  - Missing values detection
  - Duplicate patient profiles removal
  - Inconsistent urgency assignments validation
  - Clinical plausibility verification

## Expert Validation Process

### Dentist Grading via Typeform

- **Practicing dentists** graded sample cases for clinical plausibility and completeness
- **Structured evaluation** of diagnostic accuracy and treatment appropriateness
- **Typeform survey**: https://form.typeform.com/to/RFEHs2Xy
- **Grading scores** used to refine enhancement logic and improve case quality

### Agent Mode Research

- **40+ structured Agent Mode queries** (e.g., "How would a periodontist classify this?")
- **Specialty-specific expertise extraction** from literature-backed treatment pathways
- **Multi-disciplinary validation** across dental specialties

### AI Cross-Comparison

- **Benchmarked random cases** against ChatGPT-5 "thinking" mode outputs
- **Inconsistency flagging** between enhanced cases vs. gold-standard reasoning
- **Quality improvement** through comparative analysis

### Structured Input–Output Linking

- **Causal mapping development**:
  - Demographics + findings → Risk assessment
  - Risk assessment + urgency → Management plan
  - Management plan + systemic signs → Antibiotic indication
- **Evidence-based reasoning chains** validated against clinical guidelines

## Data Structure

Each example is a conversation between a dentist and AI assistant:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an expert dental clinician..."
    },
    {
      "role": "user",
      "content": "PATIENT: [synthetic patient description]"
    },
    {
      "role": "assistant",
      "content": "[structured dental assessment]"
    }
  ]
}
```

## Patient Case Format

Each case includes:
- **Demographics**: Age range, gender
- **Chief Complaint**: Primary symptom
- **History**: Relevant medical/dental history
- **Examination**: Clinical findings
- **Radiographic Findings**: X-ray descriptions
- **Medical History**: Relevant conditions/medications

## Generation Process

- **Synthetic Generation**: Cases created using clinical guidelines
- **Expert Validation**: Reviewed by dental professionals
- **Diversity**: Covers various dental conditions and urgencies
- **Anonymized**: No real patient identifiers (synthetic data)

## Intended Uses

- **Model Training**: Fine-tuning language models for dental diagnosis
- **Research**: Comparative studies of dental AI systems
- **Education**: Training materials for dental students
- **Development**: Testing dental AI applications

## Limitations

- **Synthetic Nature**: Not based on real patient cases
- **Coverage**: Limited to general dentistry
- **Validation**: Expert-reviewed but not clinically tested
- **Bias**: May reflect generation biases

## Ethical Considerations

- **No PHI**: Contains no protected health information
- **Synthetic**: Artificially generated scenarios
- **Educational**: Intended for learning and research
- **Transparency**: Clearly labeled as synthetic

## Citation

```bibtex
@dataset{dental-training-dataset,
  title={Dental Training Dataset (Synthetic)},
  author={Arnav Salkade},
  year={2024},
  url={https://huggingface.co/datasets/Wildstash/dental-training-dataset}
}
```

## Metadata Formats

This dataset includes structured metadata in multiple formats:

### Dataset Card (README.md)
- Comprehensive human-readable documentation
- Processing pipeline details
- Validation methodology
- Ethical considerations

### Croissant Metadata (croissant.json)
- Machine-readable structured metadata
- Enables automated dataset discovery
- Compatible with MLCommons standards
- Supports interoperability with ML tools

## Contact

For questions or issues: itsarnavsalkade@gmail.com

## License

Apache License 2.0
