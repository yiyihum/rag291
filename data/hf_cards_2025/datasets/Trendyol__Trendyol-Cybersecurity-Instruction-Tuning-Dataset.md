---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- cybersecurity
- defensive-security
- instruction-tuning
- threat-intelligence
- incident-response
- security-operations
pretty_name: Trendyol Cybersecurity Defense Dataset
size_categories:
- 10K<n<100K
dataset_info:
  version: 1.0.0
---

# Trendyol Cybersecurity Defense Instruction-Tuning Dataset (v2.0)

<div align="center">
  <img src="https://img.shields.io/badge/rows-53,202-brightgreen" alt="Dataset Size">
  <img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License">
  <img src="https://img.shields.io/badge/language-English-red" alt="Language">
  <img src="https://img.shields.io/badge/version-2.0.0-orange" alt="Version">
</div>

## 🚀 TL;DR

**53,202** meticulously curated *system/user/assistant* instruction-tuning examples covering **200+ specialized cybersecurity domains**. Built by the Trendyol Security Team for training state-of-the-art defensive security AI assistants. Expanded from 21K to 53K rows with comprehensive coverage of modern security challenges including cloud-native threats, AI/ML security, quantum computing risks, and advanced incident response techniques.

---

## 📊 What's New in v2.0 (2025-07-30)

| Metric | v1.1 | v2.0 | Change |
|--------|------|------|--------|
| **Total Rows** | 21,258 | **53,202** | +150.3% |
| **Unique Topics** | 50+ | **200+** | +300% |
| **Coverage Depth** | Basic-Intermediate | **Basic-Expert** | Enhanced |
| **Specialized Domains** | Traditional Security | **+ AI/ML, Quantum, Cloud-Native, OT/ICS** | Expanded |
| **Framework Integration** | MITRE ATT&CK, NIST | **+ STIX/TAXII, Diamond Model, Zero Trust** | Comprehensive |
| **Platform Specific** | Generic | **+ macOS, Cloud Providers, Container Orchestration** | Targeted |

### 🎯 Major Additions in v2.0

- **Advanced Threat Intelligence**: 5G networks, AI-powered analysis, quantum computing threats
- **Cloud-Native Security**: Kubernetes forensics, serverless security, multi-cloud environments
- **Emerging Technologies**: Post-quantum cryptography, DNA computing security, metamaterial computing
- **Platform-Specific**: Deep macOS security analysis, cloud provider-specific forensics
- **Operational Excellence**: SOAR automation, threat hunting metrics, incident response orchestration

---

## 📋 Dataset Summary

| Property | Value |
|----------|-------|
| **Language** | English |
| **License** | Apache 2.0 |
| **Format** | Parquet (optimized columnar storage) |
| **Total Rows** | 53,202 |
| **Columns** | `system`, `user`, `assistant` |
| **Splits** | `train` (90%), `validation` (5%), `test` (5%) |
| **Average Response Length** | ~700 tokens |
| **Compression Ratio** | 0.72 |

### 📊 Topic Distribution

```
Cloud Security & DevSecOps     : 18.5%
Threat Intelligence & Hunting  : 16.2%
Incident Response & Forensics  : 14.8%
AI/ML Security                 : 12.3%
Network & Protocol Security    : 11.7%
Identity & Access Management   : 9.4%
Emerging Technologies         : 8.6%
Platform-Specific Security    : 5.3%
Compliance & Governance       : 3.2%
```

---

## 🏗️ Dataset Structure

### Fields Description

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `system` | *string* | Role definition with ethical guidelines | "You are an expert cybersecurity professional..." |
| `user` | *string* | Realistic security question/scenario | "How can I detect API gateway abuse in microservices?" |
| `assistant` | *string* | Comprehensive technical response | "API gateway abuse detection requires multi-layered..." |

### Data Splits

```python
{
    "train": 47,882,      # 90%
    "validation": 2,660,   # 5%
    "test": 2,660         # 5%
}
```

---

## 🔬 Dataset Creation Process

### 1. **Advanced Content Curation** (500K+ sources)
- Technical blogs, security advisories, CVE databases
- Academic papers, conference proceedings (BlackHat, DEF CON, RSA)
- Industry reports, threat intelligence feeds
- Platform-specific documentation (AWS, Azure, GCP, macOS)
- Regulatory frameworks and compliance standards

### 2. **Multi-Stage Processing Pipeline**
```
Raw Content → Language Detection → Topic Classification → 
Instruction Synthesis → Quality Validation → Expert Review → 
Ethical Filtering → Final Dataset
```

### 3. **Quality Assurance Framework**
- **Automated Checks**: Grammar, technical accuracy, response completeness
- **Deduplication**: Advanced MinHash LSH with semantic similarity
- **Hallucination Detection**: Fact-checking against authoritative sources
- **Ethical Compliance**: Offensive content filtering, dual-use prevention
- **Expert Validation**: 10% manual review by security professionals

### 4. **Topic Coverage Validation**
- Comprehensive mapping to industry frameworks (MITRE ATT&CK, NIST, ISO 27001)
- Cross-reference with current threat landscape report1
- Validation against real-world incident patterns

---

## 💻 Usage Examples

### Basic Loading
```python
from datasets import load_dataset

# Load the full dataset
dataset = load_dataset("TrendyolSecurity/cybersecurity-defense-v2", split="train")

# Load specific split
val_dataset = load_dataset("TrendyolSecurity/cybersecurity-defense-v2", split="validation")

# First example
print(f"System: {dataset[0]['system']}")
print(f"User: {dataset[0]['user']}")
print(f"Assistant: {dataset[0]['assistant']}")
```


### Fine-Tuning Configuration
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer
from peft import LoraConfig, get_peft_model

# Model configuration
model = AutoModelForCausalLM.from_pretrained("base-model-name", load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained("base-model-name")

# LoRA configuration for efficient fine-tuning
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
)

# Training configuration
training_args = TrainingArguments(
    output_dir="./cybersec-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    warmup_steps=100,
    logging_steps=25,
    save_strategy="epoch",
    evaluation_strategy="epoch",
    learning_rate=2e-4,
    bf16=True,
    gradient_checkpointing=True,
)

# Initialize trainer
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    peft_config=peft_config,
    max_seq_length=4096,
    dataset_text_field="text",  # Concatenated field
)
```

---

## 🎯 Specialized Coverage Areas

### 🔐 Advanced Topics Included

1. **Cloud-Native Security**
   - Multi-cloud forensics and incident response
   - Container and Kubernetes security
   - Serverless and FaaS security patterns
   - Cloud-native application protection (CNAPP)

2. **AI/ML Security**
   - Adversarial machine learning defense
   - Model poisoning detection
   - AI-powered threat intelligence
   - Federated learning for threat sharing

3. **Emerging Threats**
   - 5G network security and edge computing
   - Quantum computing threat landscape
   - Post-quantum cryptography implementation
   - Supply chain security automation

4. **Platform-Specific Security**
   - macOS security internals and forensics
   - Cloud provider-specific security controls
   - OT/ICS and critical infrastructure protection
   - Mobile and IoT security frameworks

---

## ⚖️ Ethical Considerations

### Responsible AI Guidelines
- **Defensive Focus**: All content emphasizes protection and defense, never attack techniques
- **Refusal Patterns**: Built-in responses for rejecting malicious requests
- **Dual-Use Prevention**: Careful curation to avoid enabling harmful activities
- **Privacy Protection**: No PII or sensitive organizational data included
- **Bias Mitigation**: Balanced representation across vendors, platforms, and methodologies

### Usage Restrictions
- Not for developing offensive security tools
- Not for bypassing security controls
- Not for unauthorized access or exploitation
- Must comply with local laws and regulations

---

## 🚧 Known Limitations

1. **Language**: English-only (multilingual expansion planned)
2. **Temporal**: Knowledge cutoff varies by source (majority 2024-2025)
3. **Geographic Bias**: Western-centric frameworks and regulations
4. **Rapid Evolution**: Security landscape changes require regular updates
5. **Complexity Balance**: Some topics may be too advanced for general practitioners

---

## 📚 Citation

```bibtex
@dataset{trendyol_2025_cybersec_v2,
  author    = {{Trendyol Security Team}},
  title     = {Trendyol Cybersecurity Defense Instruction-Tuning Dataset v2.0},
  year      = {2025},
  month     = {7},
  publisher = {Hugging Face},
  version   = {2.0.0},
}
```

---

## 🤝 Contributing

We welcome contributions from the security community! Please ensure:

- ✅ Defensive security focus
- ✅ Technical accuracy with references
- ✅ Follows the dataset schema
- ✅ Passes quality checks
- ✅ Includes appropriate documentation

---

## 🙏 Acknowledgments

Special thanks to the global cybersecurity community, security researchers, and open-source contributors who made this dataset possible. This work builds upon decades of collective knowledge in defensive security practices.

---

## 📜 Changelog

- **v2.0.0** (2025-07-30): Major expansion to 53K+ examples, 200+ topics, platform-specific content

---

<div align="center">
  <i>Building a safer digital future through responsible AI and collaborative security intelligence.</i>
</div>