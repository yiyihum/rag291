---
license: cc-by-nc-4.0
language:
- en
tags:
- synthetic_data
- medical_qa
- healthcare
- fine_tuning
- domain_specific
- medical_chatbot
- healthcare_ai
size_categories:
- 1K<n<10K
task_categories:
- question-answering
- text-generation
pretty_name: MEDFIT Medical QA Dataset
---

# MEDFIT Medical QA Dataset

This dataset contains **6,444 unique healthcare-related question-answer pairs** designed for fine-tuning language models for medical chatbot applications. The dataset was specifically curated for the **MEDFIT-LLM** research project focusing on domain-focused fine-tuning of small language models for healthcare applications.

All credits for the methodology and dataset creation go to **Aditya Karnam Gururaj Rao**, **Arjun Jaggi**, and **Sonam Naidu**.

The dataset has been prepared and optimized for training with **MLX** and other fine-tuning frameworks.

## Dataset Description

**Curated by:** Aditya Karnam Gururaj Rao, Arjun Jaggi, Sonam Naidu  
**Language(s):** English  
**License:** CC-BY-NC-4.0  
**Domain:** Healthcare and Medical Information  
**Task:** Question Answering for Medical Chatbots  
**Size:** 6,444 unique question-answer pairs  

### Dataset Splits

- **Training:** 5,155 samples (80%)
- **Validation:** 644 samples (10%)  
- **Test:** 645 samples (10%)

### Data Creation Process

1. **Synthetic Data Generation:** Initial dataset of 10,000 healthcare-related QA pairs generated using Phi-4
2. **Domain-Specific Curation:** Questions focused on healthcare applications and medical information
3. **Deduplication:** Filtered for duplicates, resulting in 6,444 unique samples
4. **Quality Control:** Manual review and validation of medical accuracy
5. **Structured Formatting:** Optimized for chatbot training and evaluation

### Dataset Features

- **High-Quality Medical QA Pairs:** Carefully curated healthcare questions and comprehensive answers
- **Domain-Specific Focus:** Specialized for medical chatbot applications
- **Balanced Coverage:** Wide range of healthcare topics and medical scenarios
- **Chatbot-Optimized:** Formatted for direct answer training and structured responses
- **Research-Validated:** Used in peer-reviewed research demonstrating significant improvements

---

## Example Usage

### With [MLX-LM](https://github.com/ml-explore/mlx-lm)

```bash
python -m mlx_lm.lora \
--train \
--model meta-llama/Llama-3.2-3B-Instruct \
--data adityak74/medfit-medical-qa \
--num-layers 4 \
--iters 1000 \
--batch-size 2 \
--steps-per-report 50 \
--max-seq-length 2048 \
--adapter-path ./medfit_adapter
```

### With [MLX-LM-LoRA](https://github.com/Goekdeniz-Guelmez/mlx-lm-lora)

```bash
mlx_lm_lora.train \
--model meta-llama/Llama-3.2-3B-Instruct \
--train \
--data adityak74/medfit-medical-qa \
--epochs 3 \
--load-in-8bits \
--adapter-path ./medfit_adapter \
--fuse
```

### With Transformers Library

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("adityak74/medfit-medical-qa")

# Access different splits
train_data = dataset["train"]
val_data = dataset["validation"] 
test_data = dataset["test"]

# Example data point
print(train_data[0])
# Output: {'question': '...', 'answer': '...'}
```

### Data Format

Each sample contains:
```json
{
  "question": "What are the common symptoms of diabetes?",
  "answer": "Common symptoms of diabetes include frequent urination, increased thirst, unexplained weight loss, fatigue, blurred vision, slow-healing wounds, and frequent infections. Type 1 diabetes symptoms often develop quickly, while Type 2 diabetes symptoms may develop gradually over years."
}
```

## Performance Results

When used to fine-tune **Llama-3.2-3B-Instruct**, this dataset achieved:

- **30 percentage point improvement** in direct answer capability (6.0% → 36.0%)
- **Enhanced response structure** with 18% increase in organized formatting
- **Overall improvement score of 108.2** (highest among evaluated models)
- **Better medical domain understanding** and contextual relevance

## Dataset Statistics

- **Total Samples:** 6,444 unique QA pairs
- **Average Question Length:** ~15-20 words
- **Average Answer Length:** ~50-100 words
- **Topic Coverage:** General medicine, symptoms, treatments, prevention, health education
- **Data Quality:** Synthetic generation + manual curation and validation

## Intended Use

### Primary Applications
- **Medical Chatbot Training:** Fine-tuning language models for healthcare applications
- **Healthcare AI Development:** Training conversational agents for patient education
- **Medical Information Systems:** Developing QA systems for healthcare settings
- **Research:** Academic research on domain-specific language model adaptation

### Limitations and Considerations

⚠️ **Important Disclaimers:**
- **Not for medical diagnosis:** This dataset is for AI training purposes only
- **Requires professional oversight:** Healthcare applications should involve medical professionals
- **Educational focus:** Designed for information dissemination, not clinical decision-making
- **Continuous validation needed:** Medical knowledge evolves and requires regular updates

## Citation

If you use the MEDFIT Medical QA Dataset, please cite the following paper:

```bibtex
@inproceedings{rao2025medfit,
  title={MEDFIT-LLM: Medical Enhancements through Domain-Focused Fine Tuning of Small Language Models},
  author={Rao, Aditya Karnam Gururaj and Jaggi, Arjun and Naidu, Sonam},
  booktitle={2025 2nd International Conference on Research Methodologies in Knowledge Management, Artificial Intelligence and Telecommunication Engineering (RMKMATE)},
  year={2025},
  organization={IEEE}
}
```

## Related Resources

- **Model:** [adityak74/medfit-llm-3B](https://huggingface.co/adityak74/medfit-llm-3B) - Fine-tuned model using this dataset
- **Paper:** [MEDFIT-LLM: Medical Enhancements through Domain-Focused Fine Tuning](https://ieeexplore.ieee.org/document/11042816)
- **Code:** [GitHub Repository](https://github.com/adityak74/medfit-llm)

## Dataset Card Contact

**Aditya Karnam Gururaj Rao** (akarnam37@gmail.com)  
**GitHub:** [adityak74](https://github.com/adityak74)  
**Hugging Face:** [adityak74](https://huggingface.co/adityak74)

---

## License and Usage Terms

This dataset is released under the **CC-BY-NC-4.0** license, allowing for research and non-commercial use. When using this dataset:

1. **Provide proper attribution** to the original authors
2. **Ensure compliance** with healthcare data usage guidelines
3. **Implement appropriate safeguards** when deploying in healthcare applications
4. **Maintain ethical standards** in medical AI development

For commercial licensing or healthcare deployment guidance, please contact the dataset authors.