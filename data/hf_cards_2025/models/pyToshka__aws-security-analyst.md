---
language:
- en
license: llama3.1
library_name: transformers
base_model: meta-llama/Llama-3.1-8B-Instruct
tags:
- aws
- cloud-security
- security-analysis
- wazuh
- threat-detection
- llama
- peft
- lora
- aws-security
- cloudtrail
- guardduty
- compliance
pipeline_tag: text-generation
widget:
- text: 'Analyze this AWS GuardDuty finding: UnauthorizedAccess:EC2/SSHBruteForce
    from IP 45.142.120.10'
  example_title: AWS GuardDuty Alert
- text: 'Analyze CloudTrail event: AttachUserPolicy with AdministratorAccess by root
    user'
  example_title: AWS IAM Policy Change
model-index:
- name: aws-security-analyst
  results:
  - task:
      type: text-generation
      name: AWS Security Analysis
    metrics:
    - type: loss
      value: 0.03
      name: Training Loss
    - type: eval_loss
      value: 0.08
      name: Validation Loss
---

# aws-security-analyst

## Model Details

- **Model Name:** aws-security-analyst
- **Base Model:** OpenNix base model(LLaMA 3.1 8B based)
- **License:** llama3.1
- **Model Type:** Causal Language Model (Fine-tuned with LoRA for AWS Security)
- **Architecture:** 8B parameters
- **Specialization:** AWS Cloud Security Events Analysis

## Model Description

LLaMA 3.1 8B Instruct model fine-tuned for AWS cloud security event analysis.

Analyzes events from 20+ AWS security sources including CloudTrail, GuardDuty, Security Hub, Macie, Inspector, Config, VPC Flow Logs, WAF, and more.

### Key Features

- **20+ AWS Security Sources:** CloudTrail, GuardDuty, SecurityHub, VPCFlow, WAF, Macie, Inspector, Config, etc.
- **MITRE ATT&CK Mapping:** 135 cloud techniques, 14 tactics
- **Compliance Framework Support:** 195 items (CIS, PCI-DSS, HIPAA, GDPR, FedRAMP, NIST)
- **Attack Scenario Detection:** 20 multi-step attack scenarios
- **Severity Mapping:** AWS native scales → Wazuh levels (0-15)
- **Advanced Analysis:** Threat assessment, incident response recommendations

## Training Data

- **Total Samples:** 2000
- **AWS Sources:** 20 (CloudTrail, GuardDuty, SecurityHub, VPCFlow, WAF, Macie, Inspector, Config, etc.)
- **Attack Scenarios:** 20 multi-step scenarios
- **MITRE Techniques:** 135 cloud techniques
- **Compliance Items:** 195 (CIS 62, PCI-DSS 49, HIPAA 35, GDPR 15, FedRAMP 3, NIST 31)

**Distribution:**
- GuardDuty Findings: 86 types
- CloudTrail Events: 74 types
- Security Hub Findings: CIS, PCI-DSS, HIPAA compliance
- VPC Flow Logs: 5 attack patterns

## Capabilities

### AWS Security Event Analysis

```python
# Example usage
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("pyToshka/aws-security-analyst")
tokenizer = AutoTokenizer.from_pretrained("pyToshka/aws-security-analyst")

# Analyze AWS GuardDuty finding
prompt = """Analyze this AWS security event:
Event Source: GuardDuty
Finding Type: UnauthorizedAccess:EC2/SSHBruteForce
Severity: 8.0
Resource: EC2 instance i-1234567890abcdef0
Source IP: 45.142.120.10

Provide:
1. Threat assessment
2. MITRE ATT&CK techniques
3. Compliance impact
4. Recommended actions
"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=512)
response = tokenizer.decode(outputs[0])
```

### Supported AWS Sources

- CloudTrail API calls
- GuardDuty threat findings
- Security Hub compliance findings
- VPC Flow Logs network traffic
- WAF web application attacks
- Macie data sensitivity findings
- Inspector vulnerability findings
- Config compliance events
- IAM Access Analyzer findings
- Route 53 DNS queries
- RDS database logs
- EKS Kubernetes audit logs
- CloudWatch alarms
- EventBridge events
- AWS Budgets alerts
- Threat Intelligence IOCs

## Use Cases

- AWS security event triage and analysis
- GuardDuty finding interpretation
- CloudTrail event investigation
- Compliance violation detection (CIS, PCI-DSS, HIPAA, GDPR)
- MITRE ATT&CK technique mapping
- Multi-source event correlation
- Attack scenario detection
- Incident response planning

## Limitations

- Trained on synthetic AWS security events
- May require validation on real-world data
- Performance depends on input quality
- Best used as assistant tool, not replacement for human analysis

## Citation

If you use this model in your research or application, please cite:

```bibtex
@misc{{wazuh_aws_security_llama_aws_security_analyst,
  title={{Wazuh AWS Security Analyst based on LLaMA 3.1 8B}},
  author={{pyToshka}},
  year={{2025}},
  publisher={{HuggingFace}},
  url={{https://huggingface.co/pyToshka/aws-security-analyst}}
}}
```

## Acknowledgments

Built with:

- **Data:** AWS security documentation, MITRE ATT&CK Cloud Matrix, Wazuh Rules, and more
- **Training:** Wazuh, AWS

## License

This model inherits the LLaMA 3.1 Community License from the base model.

## Contact

Issues: Please open an issue on the repository

## Disclaimer

This model is provided for research and educational purposes. Always validate outputs with human security expertise before taking action on security incidents.
