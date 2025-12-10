---
language:
- ko
license: mit
tags:
- text-generation
- conversational
- roleplay
- korean
- visual-novel
- dating-sim
- chat
- multi-turn
- context-aware
- affection-based
task_categories:
- text-generation
- conversational
pretty_name: Korean Roleplay Enhanced Conversations Dataset (v3)
size_categories:
- 10K<n<100K
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_examples: 25568
  download_size: ~15MB
  dataset_size: 25568
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
metrics:
- accuracy
- bleu
- perplexity
---

# Korean Roleplay Enhanced Conversations Dataset (v3)

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/examples-25,568-green" alt="Examples">
  <img src="https://img.shields.io/badge/language-Korean-red" alt="Language">
  <img src="https://img.shields.io/badge/task-roleplay-purple" alt="Task">
</p>

## 📋 Dataset Description

This is the third version of our enhanced Korean roleplay conversation dataset, specifically designed for training conversational AI models in visual novel/dating simulation contexts. This version significantly expands the dataset with more diverse multi-turn conversations and improved context awareness.

### 🎯 Key Features
- **Large Scale**: 25,568 high-quality conversation examples
- **Multi-turn Focus**: 86.4% multi-turn conversations
- **Balanced Distribution**: Equal representation across affection levels
- **Context-Rich**: Conversations maintain context across multiple turns
- **Character Consistency**: All responses align with character personality and affection state

### 📊 Dataset Statistics

#### Overall Statistics
- **Total Examples**: 25,568
- **Average Turns per Conversation**: 4.4
- **Single-turn Conversations**: 3,486 (13.6%)
- **Multi-turn Conversations**: 22,082 (86.4%)
- **Dataset Size**: ~15MB (JSON format)
- **Last Updated**: 2025-06-28

#### Affection Level Distribution
| Level | Count | Percentage |
|-------|-------|------------|
| Low (low) | 8,505 | 33.3% |
| Medium (mid) | 8,466 | 33.1% |
| High (high) | 8,597 | 33.6% |

#### Conversation Length Distribution
| Turns | Count | Percentage |
|-------|-------|------------|
| 1 turn | 3,486 | 13.6% |
| 2 turns | 3,489 | 13.6% |
| 3 turns | 3,489 | 13.6% |
| 4 turns | 3,489 | 13.6% |
| 5 turns | 3,431 | 13.4% |
| 6+ turns | 8,184 | 32.0% |

## 🗂️ Dataset Structure

### Data Fields

Each example contains three essential fields:

```json
{
  "instruction": "Character state and context specification",
  "input": "User input or conversation history",
  "output": "Character's contextually appropriate response"
}
```

#### Field Descriptions

1. **`instruction`** (string): Defines the character's current emotional state
   - Format: `"너는 유저에게 호감도 [LEVEL]을 느끼는 NPC 하정이야. 상황에 맞게 반응해."`
   - Levels: `low` (낮음), `mid` (중간), `high` (높음)

2. **`input`** (string): Provides conversation context
   - Single-turn: Direct user message
   - Multi-turn: Full conversation history with format `"SPEAKER: message\n..."`

3. **`output`** (string): Character's response maintaining personality and affection level

### Example Entries

#### Single-turn Conversation
```json
{
  "instruction": "너는 유저에게 호감도 high을 느끼는 NPC 하정이야. 상황에 맞게 반응해.",
  "input": "USR: 오늘 같이 영화 볼래?",
  "output": "응! 좋아! 무슨 영화 볼 거야? 팝콘도 사줄 거지?"
}
```

#### Multi-turn Conversation (4 turns)
```json
{
  "instruction": "너는 유저에게 호감도 mid을 느끼는 NPC 하정이야. 상황에 맞게 반응해.",
  "input": "USR: 하정아, 오늘 날씨 좋다\nNPC: 그러게, 산책하기 좋은 날이네\nUSR: 같이 한강 걸을래?\nNPC: 음... 잠깐이면 괜찮을 것 같아\nUSR: 그럼 자전거 타는 건 어때?",
  "output": "자전거? 재밌겠다. 근데 나 오랜만이라 잘 탈 수 있을까?"
}
```

## 🎭 Character Profile

### 윤하정 (Yoon Ha-jung)
- **Age**: 20 years old
- **Background**: 
  - Recently lost both parents in a plane accident (less than a month ago)
  - Father was secretary to user's father (corporate executive)
  - Childhood acquaintance with complex history
- **Personality Traits**:
  - Beautiful and aware of her attractiveness
  - Usually confident but emotionally vulnerable due to recent loss
  - Responses vary dramatically based on affection level
- **Relationship Dynamic**:
  - Met user at age 13 during her birthday party
  - User was rude to her despite having feelings (typical teenage behavior)
  - Reuniting after 7 years as user's father wants to help her

### Response Patterns by Affection Level

#### Low Affection (33.3% of dataset)
- Cold, dismissive, sometimes hostile
- Short responses, minimal engagement
- Sarcastic or defensive tone
- Examples: "뭐 원해?", "그래서?", "관심 없어"

#### Medium Affection (33.1% of dataset)
- Neutral to cautiously friendly
- Willing to engage but maintains boundaries
- Shows curiosity but holds back emotionally
- Examples: "음... 괜찮을 것 같아", "생각해볼게", "나쁘지 않네"

#### High Affection (33.6% of dataset)
- Warm, playful, openly affectionate
- Longer, more engaged responses
- Shows clear romantic interest
- Examples: "너랑 있으면 행복해", "보고 싶었어", "오늘 너무 좋았어"

## 💻 Usage Examples

### Basic Loading
```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("junidude14/korean_roleplay_dataset_for_chat_game_2")

# Access examples
for example in dataset['train'][:3]:
    print(f"Instruction: {example['instruction']}")
    print(f"Input: {example['input']}")
    print(f"Output: {example['output']}")
    print("-" * 50)
```

### Training with Transformers
```python
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# Load model and tokenizer
model_name = "Bllossom/llama-3.2-Korean-Bllossom-AICA-5B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare dataset for training
def preprocess_function(examples):
    # Combine instruction and input for the prompt
    prompts = [f"{inst}\n{inp}" for inst, inp in zip(examples['instruction'], examples['input'])]
    
    # Tokenize
    model_inputs = tokenizer(prompts, truncation=True, padding=True, max_length=512)
    labels = tokenizer(examples['output'], truncation=True, padding=True, max_length=512)
    
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

# Apply preprocessing
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Set up training
training_args = TrainingArguments(
    output_dir="./roleplay-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    warmup_steps=500,
    logging_steps=100,
    save_strategy="epoch",
    evaluation_strategy="no",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    tokenizer=tokenizer,
)

# Start training
trainer.train()
```

### Inference Example
```python
def generate_response(model, tokenizer, affection_level, user_input, conversation_history=""):
    # Format the instruction
    instruction = f"너는 유저에게 호감도 {affection_level}을 느끼는 NPC 하정이야. 상황에 맞게 반응해."
    
    # Combine conversation history with new input
    if conversation_history:
        full_input = f"{conversation_history}\nUSR: {user_input}"
    else:
        full_input = f"USR: {user_input}"
    
    # Create prompt
    prompt = f"{instruction}\n{full_input}\nNPC:"
    
    # Tokenize and generate
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.8, top_p=0.9)
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("NPC:")[-1].strip()

# Example usage
response = generate_response(model, tokenizer, "high", "오늘 같이 저녁 먹을래?")
print(response)  # Expected: Warm, enthusiastic response
```

## 🔄 Version History

### v3.0 (Current) - 2025-06-28
- Expanded to 25,568 examples
- Enhanced multi-turn conversation coverage
- Improved context preservation across turns
- Better balance of conversation lengths

### v2.0 - 2024-06-27
- Merged multiple conversation sources
- Added conversation history format
- Improved affection level balance

### v1.0 - 2024-06-26
- Initial release with basic conversations
- Single-turn focus
- Three affection levels

## 📝 Data Sources and Creation Process

1. **Base Generation**: Initial conversations generated using prompted LLMs
2. **Context Enhancement**: Added multi-turn conversations with context awareness
3. **Quality Filtering**: Removed inconsistent or low-quality examples
4. **Affection Balancing**: Ensured equal distribution across affection levels
5. **Format Standardization**: Unified all examples to consistent structure
6. **Iterative Refinement**: Multiple rounds of generation and merging

## ⚠️ Limitations and Ethical Considerations

### Limitations
- **Character-Specific**: Optimized for one specific character (윤하정)
- **Domain-Specific**: Designed for dating simulation/visual novel contexts
- **Cultural Context**: Korean cultural norms and communication patterns
- **Affection Simplification**: Only three levels (real relationships are more nuanced)

### Ethical Considerations
- **Fictional Character**: All responses represent a fictional character
- **Entertainment Purpose**: Designed for gaming/entertainment, not real relationships
- **Consent Awareness**: Should not be used to simulate real people
- **Age Appropriate**: Character is depicted as 20 years old (adult)

### Recommended Use Cases
✅ Training conversational AI for games
✅ Research on personality-consistent dialogue
✅ Korean language learning (informal speech)
✅ Creative writing assistance

### Not Recommended For
❌ Real relationship advice
❌ Therapeutic or counseling purposes
❌ Impersonating real individuals
❌ Any harmful or deceptive uses

## 📜 License

This dataset is released under the MIT License. You are free to use, modify, and distribute this dataset for both commercial and non-commercial purposes with attribution.

## 🙏 Acknowledgments

- **Base Model**: Bllossom team for Korean LLaMA model
- **Inspiration**: Korean visual novel and dating simulation games
- **Community**: Feedback from Korean NLP community
- **Tools**: Hugging Face for hosting and tools

## 📚 Citation

```bibtex
@dataset{korean_roleplay_v3_2024,
  title={Korean Roleplay Enhanced Conversations Dataset (v3)},
  author={junidude14},
  year={2024},
  month={6},
  publisher={Hugging Face},
  version={3.0},
  url={https://huggingface.co/datasets/junidude14/korean_roleplay_dataset_for_chat_game_2},
  note={Large-scale multi-turn conversational dataset for Korean roleplay AI training},
  examples={25568},
  features={instruction, input, output}
}
```

## 🔗 Related Resources

### Models
- **Base Model**: [Bllossom/llama-3.2-Korean-Bllossom-AICA-5B](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-AICA-5B)
- **Fine-tuned Model**: [junidude14/Bllossom-AICA-5B_RolePlay_SFT](https://huggingface.co/junidude14/Bllossom-AICA-5B_RolePlay_SFT)

### Datasets
- **Original Dataset (v1)**: [junidude14/korean_roleplay_dataset_for_chat_game_1](https://huggingface.co/datasets/junidude14/korean_roleplay_dataset_for_chat_game_1)
- **This Dataset (v3)**: [junidude14/korean_roleplay_dataset_for_chat_game_2](https://huggingface.co/datasets/junidude14/korean_roleplay_dataset_for_chat_game_2)

### Papers and References
- LLaMA: [Meta AI Research](https://ai.meta.com/llama/)
- Bllossom: [Korean Language Model Development](https://huggingface.co/Bllossom)

## 📞 Contact

For questions, suggestions, or collaborations:
- **Hugging Face**: [@junidude14](https://huggingface.co/junidude14)
- **Dataset Issues**: Please use the [Community tab](https://huggingface.co/datasets/junidude14/korean_roleplay_dataset_for_chat_game_2/discussions)

---

<p align="center">
  <i>Created with ❤️ for advancing Korean conversational AI in gaming contexts</i>
</p>
