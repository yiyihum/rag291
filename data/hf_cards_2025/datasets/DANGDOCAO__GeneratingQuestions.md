---
license: mit
task_categories:
- question-answering
- text-generation
- table-question-answering
- sentence-similarity
- feature-extraction
language:
- vi
tags:
- question-generation
- nlp
- faq
- low-resource
- code
pretty_name: HVU_QA
size_categories:
- 10K<n<100K
---
# HVU_QA

**HVU_QA** is an open-source Vietnamese Question–Context–Answer (QCA) corpus and supporting tools for building FAQ-style question generation systems in low-resource languages. The dataset was created using a fully automated pipeline that combines web crawling from trustworthy sources, semantic tag-based extraction, and AI-assisted filtering to ensure high factual accuracy.

## 📋 Dataset Description

- **Language:** Vietnamese
- **Format:** SQuAD-style JSON
- **Total samples:** 30,000 QCA triples (full corpus released)
- **Domains covered:** Social services, labor law, administrative processes, and other public service topics.
- **Structure of each sample:**
  - **Question:** Generated or extracted question
  - **Context:** Supporting text passage from which the answer is derived
  - **Answer:** Answer span within the context

## ⚙️ Creation Pipeline

The dataset was built using a 4-stage automated process:
1. **Selecting relevant QA websites** from trusted sources.
2. **Automated data crawling** to collect raw QA webpages.
3. **Extraction via semantic tags** to obtain clean Question–Context–Answer triples.
4. **AI-assisted filtering** to remove noisy or factually inconsistent samples.

## 📊 Quality Evaluation
A fine-tuned `vit5-base` model trained on HVU_QA achieved:

| Metric                 | Score           |
|-------------------------|----------------|
| BLEU                    | 89.1           |
| Semantic similarity     | 91.5% (cos ≥ 0.8) |
| Human grammar score     | 4.58 / 5         |
| Human usefulness score  | 4.29 / 5         |

These results confirm that HVU_QA is a high-quality resource for developing robust FAQ-style question generation models.

## 📁 Dataset Structure
```
.HVU_QA
├── t5-viet-qg-finetuned/
├── fine_tune_qg.py
├── generate_question.py
├── 30ktrain.json
└── README.md
```
## 📁 Vietnamese Question Generation Tool

## 🛠️ Requirements

* Python 3.8+
* PyTorch >= 1.9
* Transformers >= 4.30
* scikit-learn

### 📦 Install Required Libraries

```bash
pip install datasets transformers sentencepiece safetensors accelerate evaluate sacrebleu rouge-score nltk scikit-learn
```

*(Install PyTorch separately from [pytorch.org](https://pytorch.org) if not installed yet.)*

### 📥 Load Dataset from Hugging Face Hub
```python
from datasets import load_dataset

ds = load_dataset("DANGDOCAO/GeneratingQuestions", split="train")
print(ds[0])
```
## 📚 Usage

* Train and evaluate a question generation model.
* Develop Vietnamese NLP tools.
* Conduct linguistic research.

### 🔹 Fine-tuning

```bash
python fine_tune_qg.py
```

This will:

1. Load the dataset from `30ktrain.json`.  
2. Fine-tune `VietAI/vit5-base`.  
3. Save the trained model into `t5-viet-qg-finetuned/`.  

*(Or download the pre-trained model: [t5-viet-qg-finetuned](https://huggingface.co/datasets/DANGDOCAO/GeneratingQuestions/tree/main).)*

### 🔹 Generating Questions
```bash
python generate_question.py
```

**Example:**
```
Input passage:
Cà phê sữa đá là một loại đồ uống nổi tiếng ở Việt Nam.
(Iced milk coffee is a famous drink in Vietnam.)

Number of questions: 5
```
**Output:**
```
1. Loại cà phê nào nổi tiếng ở Việt Nam?  
   (What type of coffee is famous in Vietnam?)  
2. Tại sao cà phê sữa đá lại phổ biến?  
   (Why is iced milk coffee popular?)  
3. Cà phê sữa đá bao gồm những nguyên liệu gì?  
   (What ingredients are included in iced milk coffee?)  
4. Cà phê sữa đá có nguồn gốc từ đâu?  
   (Where does iced milk coffee originate from?)  
5. Cà phê sữa đá Việt Nam được pha chế như thế nào?  
   (How is Vietnamese iced milk coffee prepared?)  
```
**You can adjust** in `generate_question.py`:

- `top_k`, `top_p`, `temperature`, `no_repeat_ngram_size`, `repetition_penalty`

## 📌 Citation
If you use **HVU_QA** in your research, please cite:

```bibtex
@inproceedings{nguyen2025hvuqa,
  title={A Method to Build QA Corpora for Low-Resource Languages},
  author={Ha Nguyen-Tien and Phuc Le-Hong and Dang Do-Cao and Cuong Nguyen-Hung and Chung Mai-Van},
  booktitle={SOICT 2025},
  year={2025}
}
```