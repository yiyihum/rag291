---
license: mit
language:
- en
size_categories:
- 1T<n<10T
task_categories:
- text-to-image
- visual-question-answering
- document-question-answering
- text-generation
---

# Complete ArXiv Papers Dataset (4.68 TB)

## 📚 Dataset Overview

This repository contains **the complete ArXiv scientific papers archive** organized by subject categories and publication years. With 4.68 TB of compressed PDFs and metadata, this represents one of the largest collections of scientific literature available for research and AI training.

## 🗂️ Dataset Structure

### Organized by Subject Categories:
- **astro-ph** (00-22): Astrophysics
- **cond-mat** (00-32): Condensed Matter Physics  
- **cs** (00-62): Computer Science (most extensive category)
- **math** (00-52): Mathematics
- **physics** (00-16): General Physics
- **quant-ph** (00-12): Quantum Physics
- **stat** (00-05): Statistics
- **econ, eess, hep, nlin, q-bio, q-fin**: Specialized categories
- Plus additional specialized domains

### File Organization:
- Each category split into numbered segments (00, 01, 02...)
- Large categories further divided into parts (part-1, part-2, etc.)
- All files in ZIP format containing PDFs

## 📊 Dataset Statistics

- **Total Size**: 4.68 TB (compressed)
- **Format**: ZIP archives containing PDFs + metadata
- **Coverage**: Complete ArXiv historical archive
- **Organization**: By subject category

## 🎯 Primary Use Cases

### Multi-Modal AI Training
- **Scientific Document Understanding**: Train models on full PDF content
- **Figure-Caption Alignment**: Extract and pair scientific figures with their descriptions
- **Mathematical Reasoning**: Process complex mathematical notation and derivations
- **Cross-modal Retrieval**: Link textual concepts with visual scientific content

### Research Applications
- **Bibliometric Analysis**: Track research trends across decades
- **Scientific NLP**: Train domain-specific language models
- **Knowledge Extraction**: Parse algorithms, methodologies, and results
- **Academic Search**: Build enhanced scientific search engines

## 🛠️ Usage Examples

### Accessing Specific Categories
```python
# Example: Access Computer Science papers from segment 00
from huggingface_hub import hf_hub_download
import zipfile

file_path = hf_hub_download(
    repo_id="nick007x/xiv-papers",
    filename="cs-00.zip"
)

# Extract and process PDFs
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall("cs_papers/")
```

### Working with Metadata
The `train.parquet` file contains structured metadata including:
- arXiv IDs, titles, authors, submission dates
- Abstracts, comments, primary subjects
- File paths to corresponding PDFs

## ⚡ Quick Start

1. **Browse Categories**: Start with smaller categories like `gr-qc-00.zip` (4.07 GB)
2. **Extract Metadata**: Use `train.parquet` for paper discovery
3. **Targeted Download**: Download specific subject areas of interest
4. **Stream Processing**: Handle large files with streaming extraction

## 🌟 Value Proposition

This dataset enables:
- **Complete Scientific Coverage**: Every paper from ArXiv's history
- **Multi-Domain Expertise**: Physics, CS, Math, Statistics, and more
- **Ready for Foundation Models**: Perfect for training scientific AI
- **Structured Organization**: Easy access by domain and time period

## 📜 License & Usage Terms

**Important:** This dataset is a **collection** of individual scholarly works from arXiv.org. The licensing structure is as follows:

*   **The Collection (Metadata & Packaging):** The script used to create this dataset, the unique metadata (e.g., file structure, dataset description), and its packaging are licensed under the **MIT License**.
*   **The Individual Papers (Content):** Each paper (PDF/TeX source) remains under the copyright and license chosen by its respective author(s). These licenses are typically Creative Commons (e.g., CC BY, CC BY-NC, CC BY-NC-ND).
*   **Your Responsibility:** Users of this dataset are **solely responsible** for checking, understanding, and complying with the specific license terms of any paper they access, download, or use from this collection. You must provide appropriate attribution to the original authors as required by their chosen license.

**By using this dataset, you agree to these terms and acknowledge that the dataset creator is not liable for any license violations resulting from your use of the contained papers.**

For more information, see:
*   [arXiv's Terms of Use](https://info.arxiv.org/help/license/index.html)
*   [Creative Commons Licenses](https://creativecommons.org/licenses/)


## 🙏 Acknowledgments

This dataset builds upon the incredible work of:
- **ArXiv** team and moderators
- **Paper authors** across all scientific domains
- **Open scientific community** enabling knowledge sharing

---

**Note**: Due to the massive size (4.68 TB), consider downloading specific categories of interest rather than the entire dataset. The organized structure makes targeted access straightforward.
