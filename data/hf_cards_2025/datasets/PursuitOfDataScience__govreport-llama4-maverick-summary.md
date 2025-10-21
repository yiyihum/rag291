---
license: mit
language:
- en
tags:
- government-reports
- summarization
- policy
- public-administration
- government
- llama-4-maverick
- text-summarization
- report-analysis
task_categories:
- summarization
- text-generation
size_categories:
- 10K<n<100K
---

# Government Report Summary Dataset (Llama-4-Maverick-17B-128E-Instruct-FP8)

## Dataset Description

This dataset contains high-quality summaries for government reports and documents, generated using the **Llama-4-Maverick-17B-128E-Instruct-FP8** model. Each summary provides a concise, accurate overview of government reports while preserving key policy implications, findings, and recommendations.

## Dataset Features

- **High-quality summaries**: Generated using Llama-4-Maverick-17B-128E-Instruct-FP8 model
- **Government document coverage**: Comprehensive coverage of government reports across multiple departments
- **Policy-focused format**: Structured summaries following professional government standards
- **Original reports**: Full report text preserved alongside summaries
- **Split organization**: Train/validation/test splits maintained from original govreport dataset

## Data Structure

Each record contains:
- `id`: Government report ID (string)
- `report`: Original full government report text
- `llama_summary`: AI-generated professional summary using Llama-4-Maverick-17B-128E-Instruct-FP8

## Summary Content Structure

Each summary includes:

1. **Main Purpose**: Clear statement of the report's primary objective or purpose
2. **Key Findings**: Most important findings, conclusions, or recommendations
3. **Policy Implications**: Policy recommendations or implications
4. **Scope & Context**: Necessary context about the report's scope and relevance
5. **Actionable Items**: Key actionable recommendations or next steps
6. **Clarity**: Clear, accessible language suitable for policy makers and the public

## System Prompt Used for Summary Generation

The following system prompt was used to ensure consistent, high-quality government report summaries:

```
You are an expert government report summarizer tasked with creating concise, accurate summaries of government documents and reports.

Your summary should:
1. **Main Purpose**: Clearly state the primary objective or purpose of the report
2. **Key Findings**: Highlight the most important findings, conclusions, or recommendations
3. **Policy Implications**: Describe any policy recommendations or implications
4. **Scope & Context**: Provide necessary context about the report's scope and relevance
5. **Actionable Items**: Identify key actionable recommendations or next steps
6. **Clarity**: Maintain clear, accessible language suitable for policy makers and the public

Guidelines:
- Keep the summary between 4-6 sentences (150-200 words)
- Use clear, professional language appropriate for government and policy contexts
- Focus on the most significant findings and recommendations
- Maintain accuracy while ensuring accessibility to non-expert readers
- Structure it logically from purpose to findings to implications

Return ONLY the summary with no additional text, labels, or prefixes.
```

## Model Information

- **Model**: Llama-4-Maverick-17B-128E-Instruct-FP8
- **Summary Length**: 150-200 words typically (4-6 sentences)
- **Processing**: Multi-threaded with advanced rate limiting and error handling
- **Quality**: Professional language with policy precision

## Use Cases

- **Policy Analysis**: Quick insights into government reports and policy documents
- **Government Research**: Efficient screening of government publications
- **Public Administration**: Study of government communication and report writing
- **AI Training**: Fine-tuning models for government document summarization
- **Civic Engagement**: Making government reports more accessible to the public
- **Policy Communication**: Improving summary writing for government officials

## Data Quality

- Comprehensive error handling and retry logic during generation
- Rate limiting to ensure consistent API performance
- Memory-efficient processing of large datasets
- Validation of summary quality and professional standards

## Dataset Splits

- **Train**: Training reports from `ccdv/govreport-summarization`
- **Validation**: Validation reports for model development
- **Test**: Test reports for evaluation

## Original Dataset

This dataset is based on the `ccdv/govreport-summarization` dataset, enhanced with AI-generated summaries.

## Citation

If you use this dataset in your research, please cite:

```
@dataset{govreport_summary_llama4_maverick,
  title={Government Report Summary Dataset (Llama-4-Maverick-17B-128E-Instruct-FP8)},
  author={PursuitOfDataScience},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/PursuitOfDataScience/govreport-llama4-maverick-summary}
}
```

Please also cite the original govreport summarization dataset:

```
@inproceedings{huang2021efficient,
  title={Efficient Attentions for Long Document Summarization},
  author={Huang, Luyang and Cao, Shuyang and Parulian, Nikolaus and Ji, Heng and Wang, Lu},
  booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages={1419--1436},
  year={2021}
}
```

## Contact

For questions or issues regarding this dataset, please create an issue in the dataset repository.
