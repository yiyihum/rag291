---
language:
- en
license: cc0-1.0
size_categories:
- 100K<n<1M
task_categories:
- question-answering
- text-generation
pretty_name: NIST Cybersecurity Standards Training Dataset
tags:
- cybersecurity
- nist
- security-controls
- compliance
- standards
- government
---

# NIST Cybersecurity Standards Training Dataset

## Dataset Summary

This dataset contains **523,706 training examples** extracted from **568 NIST cybersecurity publications**, including:

- FIPS (Federal Information Processing Standards)
- SP 800 series (Special Publications)
- IR (Interagency/Internal Reports)
- CSWP (Cybersecurity White Papers)

The dataset is designed for fine-tuning large language models to become experts in NIST cybersecurity standards, controls, frameworks, and best practices.

## Dataset Statistics

- **Total Examples**: 523,706
- **Training Examples**: 418,964
- **Validation Examples**: 104,742
- **Train/Valid Split**: 80% / 20%
- **Source Documents**: 1133
- **Max Chunk Size**: 2000 characters
- **Chunking Method**: Sentence-aware with 200 character overlap

## Data Format

Each example follows the chat format with system/user/assistant messages:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a cybersecurity expert with deep knowledge of NIST standards..."
    },
    {
      "role": "user",
      "content": "What is Zero Trust Architecture?"
    },
    {
      "role": "assistant",
      "content": "According to NIST SP 800-207..."
    }
  ],
  "metadata": {
    "source": "NIST SP 800-207",
    "type": "section",
    "chunk_id": 0
  }
}
```

## Data Collection

### Source Documents

All documents were downloaded from the [NIST Computer Security Resource Center (CSRC)](https://csrc.nist.gov/publications/search):

- **Total PDFs Downloaded**: 565 (out of 579 available)
- **Extraction Success Rate**: 100%
- **Extraction Methods**:
  - Primary: [Docling](https://github.com/DS4SD/docling) (IBM's document understanding library)
  - Fallback: [MarkItDown](https://github.com/microsoft/markitdown) (Microsoft's conversion utility)

### Data Preparation

The training data was generated using a **smart chunking strategy** with 5 extraction methods:

1. **Section-based**: Extracts questions from document sections and headings
2. **Control-based**: Generates Q&A for security control definitions (e.g., AC-1, SC-7)
3. **Definition-based**: Creates examples from glossary terms and definitions
4. **Table-based**: Extracts structured data from tables
5. **Semantic chunks**: Sentence-aware chunking with context preservation

**Key Features**:
- Sentence-boundary aware (no mid-sentence cuts)
- 2000 character chunks with 200 character overlap
- Preserves document context and metadata
- Tracks chunk provenance and source documents

## Intended Use

### Primary Use Cases

1. **Fine-tuning LLMs** for cybersecurity expertise
2. **Training compliance chatbots** for NIST standards
3. **Question-answering systems** for security professionals
4. **Retrieval-augmented generation (RAG)** knowledge base
5. **Educational tools** for learning NIST frameworks

### Out-of-Scope Uses

- This dataset should NOT be used for malicious purposes
- Not suitable for generating exploits or attack tools
- Should be used for defensive security education only

## Dataset Structure

### Files

- `train.jsonl`: 418,964 training examples (791MB)
- `valid.jsonl`: 104,742 validation examples (198MB)

### Field Descriptions

- `messages`: List of chat messages (system, user, assistant)
- `metadata.source`: Source document title
- `metadata.type`: Extraction type (section, control, definition, table, chunk)
- `metadata.chunk_id`: Chunk number within source document

## Coverage

This dataset covers major NIST cybersecurity topics including:

- Access Control (AC)
- Audit and Accountability (AU)
- Security Assessment (CA)
- Configuration Management (CM)
- Contingency Planning (CP)
- Identification and Authentication (IA)
- Incident Response (IR)
- Risk Assessment (RA)
- System and Communications Protection (SC)
- System and Information Integrity (SI)
- Cloud Security
- Zero Trust Architecture
- Privacy Controls
- Supply Chain Risk Management
- Cryptographic Standards (FIPS 140, FIPS 197, FIPS 200)
- And much more...

## Limitations

1. **US Government Focus**: Dataset reflects US federal cybersecurity requirements
2. **Static Snapshot**: Captured NIST publications as of October 2025
3. **Extraction Artifacts**: Some PDF conversion artifacts may remain
4. **Chunking Boundaries**: Long documents are split; context may be limited per chunk

## Ethical Considerations

- All source documents are **public domain** (US Government works)
- Dataset is intended for **defensive cybersecurity** education only
- Users should verify critical information against original NIST publications
- Not a substitute for official NIST guidance or professional security advice

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{nist_cybersecurity_training_2025,
  title={NIST Cybersecurity Standards Training Dataset},
  author={Troy, Ethan},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/ethanolivertroy/nist-cybersecurity-training}
}
```

## License

**CC0 1.0 Universal (Public Domain)**

All NIST publications are works of the US Government and are in the public domain. This dataset maintains that public domain status.

## Dataset Creation

### Source Data

- **NIST CSRC**: https://csrc.nist.gov/publications/search
- **Document Types**: FIPS, SP, IR, CSWP (Final publications only)
- **Extraction Date**: October 2025
- **Document Count**: 568 successfully extracted PDFs

### Tools Used

- **Docling** (v2.x): Primary PDF extraction with structure preservation
- **MarkItDown** (v0.x): Fallback PDF-to-Markdown conversion
- **pdfminer.six**: Direct text extraction for edge cases
- **Custom scripts**: Smart chunking and Q&A generation

### Quality Assurance

- 100% extraction success rate (568/568 available documents)
- Automated section/control/definition extraction
- Sentence-boundary aware chunking
- Metadata tracking for provenance

## Contact

For questions, issues, or contributions, please open an issue on the [project repository](https://github.com/ethanolivertroy/nist-tuned-model).

## Acknowledgments

- **NIST** for making cybersecurity standards freely available
- **IBM Research** for the Docling document understanding library
- **Microsoft** for MarkItDown conversion utilities
- The open-source ML community

---

**Built with**: Docling, MarkItDown, MLX, and open-source tools
