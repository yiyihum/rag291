---
language:
- en
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- conversational
- text-generation
tags:
- cybersecurity
- security
- cyber-defense
- conversational
- instruction-tuning
- gpt-format
pretty_name: Trendyol Cybersecurity Instruction Tuning Dataset (GPT Format)
dataset_info:
  features:
  - name: messages
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  splits:
  - name: train
    num_bytes: 189824531
    num_examples: 53201
  download_size: 93456789
  dataset_size: 189824531
---

# Trendyol Cybersecurity Instruction Tuning Dataset (GPT Format)

A conversational dataset in GPT/OpenAI messages format, converted from [Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset](https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset). Designed for training language models in advanced cyber-defense and security principles.

## Dataset Description

This dataset contains 53,201 high-quality instruction-tuning examples focused on cybersecurity, converted to the standard GPT conversation format (messages) for compatibility with modern training frameworks.

### Dataset Statistics

- **Total Examples**: 53,201
- **Format**: GPT conversation format (messages with role/content)
- **Domain**: Advanced Cybersecurity, Cyber-Defense, Information Security
- **Language**: English
- **Size**: ~190 MB (uncompressed), ~93 MB (download)

## Dataset Structure

### Data Fields

Each example contains:

- **messages** (list): A conversation with 3 messages:
  - **role** (string): One of "system", "user", or "assistant"
  - **content** (string): The message content

### Data Example

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a highly specialized AI assistant for advanced cyber-defense whose mission is to deliver accurate, in-depth, actionable guidance on information-security principles—confidentiality, integrity, availability, authenticity, non-repudiation, and privacy—by offering concise executive summaries that drill down into technical detail, industry standards, and threat models while referencing frameworks such as NIST CSF and MITRE ATT&CK..."
    },
    {
      "role": "user",
      "content": "Analyze encrypted C2 channels using TLS. Discuss traffic analysis techniques to fingerprint malicious sessions."
    },
    {
      "role": "assistant",
      "content": "Encrypted Command and Control (C2) channels utilizing Transport Layer Security (TLS) present significant challenges for network defenders, as traditional packet inspection methods cannot directly analyze payload content. However, sophisticated traffic analysis techniques can still identify potentially malicious sessions through behavioral and statistical patterns..."
    }
  ]
}
```

## Conversation Format

Each example follows this structure:

1. **System Message**: Establishes the AI as a highly specialized cyber-defense assistant with expertise in:
   - Information security principles (CIA triad, authenticity, non-repudiation, privacy)
   - Industry frameworks (NIST CSF, MITRE ATT&CK)
   - Defensive security practices
   - Ethical guidelines (ISC Code of Ethics, defense-only principle)

2. **User Message**: Contains a cybersecurity question, analysis request, or instruction covering topics like:
   - Threat analysis and detection
   - Security architecture and hardening
   - Incident response and forensics
   - Vulnerability assessment
   - Network security and monitoring
   - Malware analysis (defensive perspective)

3. **Assistant Message**: Provides detailed, actionable guidance with:
   - Technical analysis and explanations
   - Industry standard references
   - Defensive scripts and detection rules
   - Threat models and mitigation strategies
   - Educational security concepts

## Topics Covered

The dataset encompasses a wide range of advanced cybersecurity topics:

- **Network Security**: Traffic analysis, IDS/IPS, network forensics
- **Threat Detection**: Behavioral analysis, anomaly detection, threat hunting
- **Malware Analysis**: Reverse engineering, sandboxing, indicators of compromise
- **Security Operations**: SIEM, log analysis, incident response
- **Application Security**: Code review, vulnerability assessment, secure development
- **Cloud Security**: Cloud-native security, container security, cloud forensics
- **Cryptography**: Encryption protocols, key management, cryptographic attacks
- **Defense Strategies**: Security architecture, hardening, defense-in-depth
- **Compliance & Standards**: NIST, MITRE ATT&CK, security frameworks

## Use Cases

This dataset is ideal for:

- Fine-tuning language models as cybersecurity experts and assistants
- Training AI for security operations centers (SOC)
- Building defensive security chatbots and tools
- Creating security analysis and threat intelligence systems
- Teaching models about advanced cyber-defense techniques
- Developing security education and training platforms

## Original Dataset

This is a converted version of the original [Trendyol Cybersecurity Instruction Tuning Dataset](https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset).

### Conversion Details

- **Original Format**: Separate columns (system, user, assistant)
- **Converted Format**: GPT-style messages list
- **Changes**: Structure only - all content preserved exactly as in original
- **Purpose**: Improved compatibility with modern training frameworks

## Usage

### Load with Datasets Library

```python
from datasets import load_dataset

dataset = load_dataset("tuandunghcmut/Trendyol-Cybersecurity-Instruction-Tuning-Dataset")
train_data = dataset["train"]

# Access a conversation
example = train_data[0]
for message in example["messages"]:
    print(f"{message['role']}: {message['content'][:100]}...")
```

### Use with LLaMA-Factory

Add to your `dataset_info.json`:

```json
{
  "trendyol_security": {
    "hf_hub_url": "tuandunghcmut/Trendyol-Cybersecurity-Instruction-Tuning-Dataset",
    "formatting": "sharegpt",
    "columns": {
      "messages": "messages"
    }
  }
}
```

Then use in training:
```yaml
dataset: trendyol_security
model_name_or_path: meta-llama/Meta-Llama-3-8B-Instruct
stage: sft
template: llama3
cutoff_len: 4096
# ... other training parameters
```

### Use with Transformers

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load dataset and model
dataset = load_dataset("tuandunghcmut/Trendyol-Cybersecurity-Instruction-Tuning-Dataset", split="train")
tokenizer = AutoTokenizer.from_pretrained("your-model")
model = AutoModelForCausalLM.from_pretrained("your-model")

# Format for training
def format_conversation(example):
    messages = example["messages"]
    text = tokenizer.apply_chat_template(messages, tokenize=False)
    return {"text": text}

formatted_dataset = dataset.map(format_conversation)
# ... continue with training
```

### Use with OpenAI Fine-tuning Format

The dataset is already in OpenAI's messages format and can be used directly:

```python
from datasets import load_dataset
import json

dataset = load_dataset("tuandunghcmut/Trendyol-Cybersecurity-Instruction-Tuning-Dataset", split="train")

# Export to JSONL for OpenAI fine-tuning
with open("training_data.jsonl", "w") as f:
    for example in dataset:
        f.write(json.dumps({"messages": example["messages"]}) + "\n")
```

## Training Recommendations

### Suggested Hyperparameters

```yaml
# LLaMA-Factory example
learning_rate: 5.0e-5
num_train_epochs: 2-3
per_device_train_batch_size: 2
gradient_accumulation_steps: 8
cutoff_len: 4096  # Security content can be detailed
warmup_ratio: 0.1
lr_scheduler_type: cosine
bf16: true
```

### Context Length

- **Recommended**: 4096+ tokens
- **Minimum**: 2048 tokens
- Many security explanations include detailed technical content

### Validation Split

```python
dataset = load_dataset("tuandunghcmut/Trendyol-Cybersecurity-Instruction-Tuning-Dataset")
split_dataset = dataset["train"].train_test_split(test_size=0.01, seed=42)
train_data = split_dataset["train"]
val_data = split_dataset["test"]
```

## Ethical Considerations

### Defense-Only Focus

The dataset is designed for **defensive cybersecurity** purposes only:

- ✅ Defensive security strategies and techniques
- ✅ Threat detection and analysis
- ✅ Security hardening and best practices
- ✅ Educational security concepts
- ✅ Incident response and forensics

### Prohibited Uses

- ❌ Generating offensive malware or exploits
- ❌ Creating phishing or social engineering tools
- ❌ Bypassing security controls for unauthorized access
- ❌ Any malicious or illegal activities

The system message explicitly instructs the model to refuse requests for offensive security tools or techniques that could cause harm.

## Limitations

- **Domain-Specific**: Focused solely on cybersecurity and cyber-defense
- **Technical Level**: Advanced content requiring security background
- **English Only**: All content is in English
- **Snapshot in Time**: Security landscape evolves; content reflects training data timeframe
- **No Real Exploits**: Educational/defensive focus, not penetration testing

## License

Please refer to the original [Trendyol dataset](https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset) for licensing information.

## Citation

If you use this dataset, please cite the original Trendyol dataset:

```bibtex
@dataset{trendyol_cybersecurity,
  title={Trendyol Cybersecurity Instruction Tuning Dataset},
  author={Trendyol},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/Trendyol/Trendyol-Cybersecurity-Instruction-Tuning-Dataset}
}
```

## Dataset Card Authors

- tuandunghcmut (conversion to GPT format)
- Original dataset by Trendyol

## Acknowledgments

- **Trendyol** for creating and sharing the original high-quality cybersecurity instruction dataset
- The cybersecurity community for advancing defensive security practices
- Open-source frameworks: NIST CSF, MITRE ATT&CK

## Version History

- **v1.0** (2025-10-07): Initial release - conversion to GPT messages format
  - Converted from separate columns to messages format
  - 53,201 examples preserved from original dataset
  - Compatible with modern training frameworks
