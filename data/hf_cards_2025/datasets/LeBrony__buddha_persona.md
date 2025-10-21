---
tags:
- buddhism
- scriptures
- qa
- chat
- korean
- reasoning
- fine-tuning
language: ko
license: mit
pretty_name: Buddha AI Korean Sutra QA Dataset
---

# Buddha AI Korean Sutra QA Dataset

A comprehensive Korean fine-tuning dataset based on Buddhist scriptures from the Korean Tripitaka (Palman Daejanggyeong) archive, featuring diverse question-answer pairs and reasoning-enhanced conversations.

## 🎯 Overview

This dataset combines rule-based QA extraction and contextual synthetic QA generation from 9 major Buddhist texts, enhanced with diverse question reformulation and reasoning capabilities. It includes integration with the external dataset `sweatSmile/buddha-taught-qa` and provides multiple formats for different training scenarios.

## 📁 Dataset Structure

### Core Files
- **`qa_train.jsonl`**, **`qa_val.jsonl`**: Simple QA format with fields: `id`, `source`, `question`, `answer`, `method`
- **`chat_train.jsonl`**, **`chat_val.jsonl`**: Chat format with OpenAI/Zephyr compatible `role`/`content` structure
- **`messages_train.jsonl`**, **`messages_val.jsonl`**: Enhanced 3-message format with system/user/assistant roles
- **`stats.json`**: Dataset statistics and metadata

### Enhanced Files (New!)
- **`messages_reasoned_train_full.jsonl`**, **`messages_reasoned_val_full.jsonl`**: Advanced reasoning-enhanced format with:
  - **Diverse question reformulation** (6 question types)
  - **Source attribution** (specific sutra references)
  - **English reasoning** in `thinking` field
  - **Hanzi-Korean glossaries**

## 📊 Statistics

- **Total conversations**: 5,077 (Train: 4,825 / Val: 252)
- **Enhanced samples**: 30 (Train: 20 / Val: 10)
- **Source texts**: 9 Buddhist scriptures
- **Question types**: 6 diverse formats (conceptual, practical, comparative, contextual, reflective, specific)

## 🏗️ Data Schema

### Standard Messages Format
```json
[
  {
    "content": "너는 한국어로 답하는 자비롭고 정확한 붓다 AI야. 경전의 문맥을 존중하며 과장하지 않고 명확히 설명해.",
    "role": "system",
    "thinking": null
  },
  {
    "content": "무상이란 무엇인가요?",
    "role": "user", 
    "thinking": null
  },
  {
    "content": "무상은 모든 것이 변한다는 뜻으로...",
    "role": "assistant",
    "thinking": null
  }
]
```

### Enhanced Reasoning Format
```json
[
  {
    "content": "reasoning language: English\n\n너는 한국어로 답하는 자비롭고 정확한 붓다 AI야...",
    "role": "system",
    "thinking": null
  },
  {
    "content": "이 경구에서 '무상'과 '비자아'의 의미를 쉽게 설명해줄 수 있니?",
    "role": "user",
    "thinking": null
  },
  {
    "content": "무상한 인과 무상한 연에 의해 생긴 식들이 어떻게 항상하겠느냐...\n\n*출처: 장아함경*",
    "role": "assistant",
    "thinking": "The answer explains core Buddhist concepts of impermanence and non-self...\n\nGlossary (Hanzi → Korean):\n- 無常: 변함없지 않음, 모든 것이 변한다\n- 因: 원인\n- 緣: 조건"
  }
]
```

## 🚀 Usage

### Loading the Dataset
```python
from datasets import load_dataset

# Standard format
dataset = load_dataset("LeBrony/buddha_persona", 
                      data_files={
                          "train": "messages_train.jsonl",
                          "validation": "messages_val.jsonl"
                      })

# Enhanced reasoning format
enhanced_dataset = load_dataset("LeBrony/buddha_persona",
                               data_files={
                                   "train": "messages_reasoned_train_full.jsonl", 
                                   "validation": "messages_reasoned_val_full.jsonl"
                               })
```

### Fine-tuning Example
```python
# Perfect for instruction tuning with reasoning capabilities
for sample in enhanced_dataset["train"]:
    conversation = sample  # Already in messages format
    # Use directly with transformers trainer
```

## 🎨 Key Features

### 1. **Diverse Question Types**
- **Conceptual**: "무상이란 무엇인가요?" 
- **Practical**: "이 가르침을 어떻게 실천할 수 있을까요?"
- **Comparative**: "색과 수의 차이점은 무엇인가요?"
- **Contextual**: "왜 부처님이 이렇게 말씀하셨을까요?"
- **Reflective**: "이 가르침에 대해 어떻게 생각하세요?"
- **Specific**: "구체적인 예시를 들어주세요"

### 2. **Source Attribution**
- Automatic sutra identification: "장아함경", "증일아함경", "금강반야바라밀경"
- Content-based source extraction using text patterns

### 3. **Multilingual Reasoning**
- English reasoning in `thinking` field for training transparency
- Korean responses for end-user interaction
- Hanzi-Korean glossaries for terminology clarity

### 4. **Cost-Optimized Generation**
- Generated using GPT-4.1-2025-04-14 for 20% cost savings
- High-quality reasoning and question reformulation

## 📚 Source Texts

1. **장아함경** (Long Discourses) - Volumes 1-3
2. **증일아함경** (Gradual Discourses) - Volumes 1-3  
3. **금강반야바라밀경** (Diamond Sutra)
4. **반야바라밀다심경** (Heart Sutra)
5. **팔만대장경** (Korean Tripitaka) - General content

## 🔧 Technical Details

- **Question Generation**: GPT-4.1-2025-04-14 with structured prompting
- **Source Detection**: Content-based pattern matching with fallback logic
- **Quality Assurance**: Manual verification of sample outputs
- **Format Compliance**: Compatible with popular training frameworks

## 🙏 Use Cases

- **Buddhist AI Assistant Training**: Fine-tune models for accurate Buddhist Q&A
- **Instruction Following**: Train models to maintain respectful, accurate tone
- **Reasoning Enhancement**: Develop models with transparent thought processes  
- **Cross-lingual Understanding**: Korean output with English reasoning
- **Educational Applications**: Buddhist studies and meditation guidance

## ⚖️ License

This dataset is released under the **MIT License**. You are free to use, modify, and distribute this dataset for any purpose, including commercial use.

Please ensure compliance with the original source materials' copyright and usage terms.

## 🤝 Contributing

We welcome contributions to improve this dataset! Please feel free to:
- Report issues or suggest improvements
- Submit additional Buddhist text sources
- Enhance question diversity or reasoning quality

## 📞 Contact

For questions about this dataset, please reach out through the Hugging Face repository discussions.

---
*Generated with ❤️ for the Buddhist AI community*
