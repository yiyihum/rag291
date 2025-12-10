---
license: apache-2.0
task_categories:
- text-generation
- text-classification
- summarization
language:
- en
tags:
- code-review
- software-engineering
- pull-requests
- static-analysis
- ai-suggestions
- semgrep
- code-quality
- software-development
- automated-review
size_categories:
- 10K<n<100K
---

# Dataset Card for Code Review Execution Dataset

This dataset contains comprehensive code review data including pull requests, AI-generated code suggestions, human feedback, and static analysis results. It represents real-world software development workflows and code quality processes.

## Dataset Details

### Dataset Description

This dataset captures the complete lifecycle of code review processes in software development, including:
- Pull request metadata and context
- AI-generated code suggestions for improvements
- Human feedback and sentiment analysis on suggestions
- Static analysis scan results from security tools
- Temporal patterns of code review activities

The data spans from March 2025 to June 2025 and contains 68,572 total records across multiple interconnected tables.

- **Curated by:** Nutanix AI Team
- **Language(s):** English (code comments, suggestions, and feedback)
- **License:** Apache 2.0
- **Size:** 8.6 GB (5 CSV files)
- **Records:** 68,572 total entries

### Dataset Sources

- **Repository:** https://huggingface.co/datasets/Nutanix/codereview-execution
- **Original Format:** PostgreSQL database dump
- **Processing:** Extracted using custom PostgreSQL COPY format parser

## Uses

### Direct Use

This dataset is suitable for:
- **Code Review Automation:** Training models to generate code improvement suggestions
- **Sentiment Analysis:** Understanding developer feedback patterns on AI suggestions
- **Security Analysis:** Studying static analysis findings and remediation patterns
- **Software Engineering Research:** Analyzing code review workflows and effectiveness
- **AI/ML Model Training:** Fine-tuning code generation and review models
- **Quality Metrics:** Developing code quality assessment tools

### Out-of-Scope Use

- **Personal Identification:** Dataset may contain developer usernames/emails - not for identity analysis
- **Proprietary Code Recreation:** Code snippets are for analysis, not reproduction
- **Real-time Security Scanning:** Static analysis data is historical, not for live security assessment

## Dataset Structure

The dataset consists of 5 interconnected CSV files:

### 1. `pull_requests.csv` (6.9 GB, 10,064 records)
- **id:** Unique pull request identifier
- **pr_url:** GitHub/GitLab pull request URL
- **action:** PR action type (opened, closed, merged, etc.)
- **pr_context:** JSON metadata about the pull request
- **meta_data:** Additional PR metadata
- **created_at/modified_at:** Timestamps

### 2. `semgrep_scans.csv` (1.7 GB, 40,397 records)
- **id:** Unique scan identifier
- **pr_url:** Associated pull request URL
- **head_sha:** Git commit SHA being scanned
- **status:** Scan completion status
- **report:** JSON-formatted Semgrep analysis results
- **created_at/modified_at:** Timestamps

### 3. `code_suggestions.csv` (11 MB, 17,650 records)
- **id:** Unique suggestion identifier
- **content:** AI-generated suggestion text
- **existing_code_snippet:** Original code being reviewed
- **suggested_code_snippet:** Proposed improvement
- **pull_request_id:** Link to associated PR
- **semgrep_scan_id:** Link to triggering security scan
- **suggestion_type:** Category of suggestion
- **created_at/modified_at:** Timestamps

### 4. `code_suggestion_feedbacks.csv` (73 KB, 460 records)
- **id:** Unique feedback identifier
- **code_suggestion_id:** Link to suggestion being reviewed
- **git_provider_comment_id:** External platform comment ID
- **feedback:** Human feedback text
- **sentiment:** Sentiment analysis of feedback
- **created_at/modified_at:** Timestamps

### 5. `alembic_version.csv` (27 B, 1 record)
- **version_num:** Database schema version tracking

## Dataset Creation

### Curation Rationale

This dataset was created to support research and development in:
- Automated code review systems
- AI-assisted software development
- Code quality measurement and improvement
- Developer productivity analysis
- Security vulnerability detection and remediation

### Source Data

#### Data Collection and Processing

- **Source:** Production code review system database
- **Time Period:** March 2025 - June 2025
- **Extraction Method:** PostgreSQL COPY format processing
- **Processing Tools:** Custom Python extraction pipeline with tmux for background processing
- **Data Format:** Tab-separated values converted to CSV
- **Quality Assurance:** Automated parsing with error tracking and validation

#### Who are the source data producers?

- **Software Developers:** Creating pull requests and code changes
- **AI Systems:** Generating automated code improvement suggestions
- **Static Analysis Tools:** Semgrep security and quality scanners
- **Code Review Platforms:** GitHub/GitLab integration systems
- **Human Reviewers:** Providing feedback on AI suggestions

### Annotations

#### Annotation Process

- **AI Suggestions:** Generated automatically using trained models
- **Sentiment Analysis:** Automated classification of human feedback
- **Static Analysis:** Automated security and quality rule evaluation
- **Manual Review:** Human feedback on AI-generated suggestions

#### Who are the Annotators?

- **Automated Systems:** AI models and static analysis tools
- **Software Engineers:** Providing manual feedback and reviews
- **Security Tools:** Semgrep rule-based analysis engine

## Personal and Sensitive Information

**Privacy Considerations:**
- May contain developer usernames, email addresses, and commit messages
- Code snippets may include proprietary business logic
- No personally identifiable information (PII) beyond professional development context
- All data represents professional software development activities

**Anonymization:**
- Original database identifiers preserved for research consistency
- No additional anonymization applied to maintain data utility

## Bias, Risks, and Limitations

**Technical Limitations:**
- Data limited to 4-month period (March-June 2025)
- Specific to one organization's development practices
- May not generalize to all software development contexts
- AI suggestions reflect training data biases of the original models

**Potential Biases:**
- Programming language preferences
- Code style conventions specific to the organization
- Review patterns may reflect team dynamics and processes
- Static analysis rules may have false positive/negative rates

**Risks:**
- Code snippets may reveal proprietary development patterns
- Temporal patterns may reflect specific business cycles
- AI suggestions may perpetuate existing code quality issues

### Recommendations

Users should:
- Consider the temporal and organizational context when applying insights
- Validate findings against diverse development environments
- Be aware of potential proprietary information in code snippets
- Consider biases in AI-generated suggestions and human feedback patterns
- Use appropriate data handling practices for any sensitive information

## Citation

**BibTeX:**
```
@dataset{nutanix_codereview_2025,
  title={Code Review Execution Dataset},
  author={Nutanix AI Team},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Nutanix/codereview-execution}
}
```

**APA:**
Nutanix AI Team. (2025). Code Review Execution Dataset. Hugging Face. https://huggingface.co/datasets/Nutanix/codereview-execution

## Dataset Statistics

- **Total Records:** 68,572
- **Total Size:** 8.6 GB
- **Processing Time:** 15 minutes (9.0 GB PostgreSQL dump)
- **Data Quality:** 99.9% successful parsing rate
- **Time Range:** March 2025 - June 2025
- **Tables:** 5 interconnected CSV files

## Dataset Card Authors

Nutanix AI Team

## Usage

```python
from datasets import load_dataset

# Load specific tables by configuration name (now using 'test' split)
alembic = load_dataset("Nutanix/codereview-dataset", "alembic_version")
feedbacks = load_dataset("Nutanix/codereview-dataset", "code_suggestion_feedbacks")
suggestions = load_dataset("Nutanix/codereview-dataset", "code_suggestions")
pull_requests = load_dataset("Nutanix/codereview-dataset", "pull_requests")
semgrep_scans = load_dataset("Nutanix/codereview-dataset", "semgrep_scans")

# Access the data using 'test' split
print(f"Feedbacks: {len(feedbacks['test'])} rows")
print(f"Features: {list(feedbacks['test'].features.keys())}")
first_feedback = feedbacks['test'][0]
```

## Dataset Card Contact

For questions about this dataset, please contact the Nutanix AI Team or create an issue in the dataset repository.