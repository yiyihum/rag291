---
language:
- en
license: mit
size_categories:
- 1M<n<10M
tags:
- ultrachat
- dialogue
- multi-turn
- chat
- parquet
configs:
- config_name: default
  data_files:
  - split: train
    path: train-*.parquet
task_categories:
- question-answering
---

# UltraChat Conversations Dataset

This dataset contains **1,468,346 multi-turn conversations** from UltraChat, processed to preserve the original conversational structure and optimized for training conversational AI models.

## 🎯 Dataset Format

Each conversation record contains:
- `id`: Sequential conversation ID (1, 2, 3, ...)
- `source`: "ultra" 
- `language`: "english"
- `data`: JSON string containing conversation turns array

## 📊 Dataset Statistics

- **Total Conversations**: 1,468,346
- **Average Turns per Conversation**: 7.7
- **Format**: Multi-turn conversations (preserved context)
- **Parquet Chunks**: 30 files (~200MB each)
- **Optimized**: For HuggingFace Data Studio instant preview

## 🔄 Conversation Structure

```json
{
  "id": 1,
  "source": "ultra",
  "language": "english",
  "data": "[\"User message\", \"Assistant response\", \"User followup\", \"Assistant response\"]"
}
```

The `data` field contains a JSON string that, when parsed, gives you an array where:
- **Even indices** (0, 2, 4, ...): User messages
- **Odd indices** (1, 3, 5, ...): Assistant responses

## 💻 Usage Examples

### Basic Loading
```python
from datasets import load_dataset
import json

# Load dataset
dataset = load_dataset("metythorn/ultrachat")

# Access conversations
for example in dataset["train"].select(range(5)):  # First 5 conversations
    conv_id = example["id"]
    turns = json.loads(example["data"])  # Parse JSON string to array
    
    print(f"Conversation {conv_id}: {len(turns)} turns")
    print(f"First turn (User): {turns[0][:100]}...")
    print(f"Response (Assistant): {turns[1][:100]}...")
    print()
```

### Streaming for Large Dataset
```python
# Stream for memory efficiency
dataset_stream = load_dataset("metythorn/ultrachat-conversations", streaming=True)

for i, example in enumerate(dataset_stream["train"]):
    if i >= 10:  # Process first 10
        break
    
    turns = json.loads(example["data"])
    print(f"Conversation {example['id']}: {len(turns)} turns")
```

### Convert to Chat Format
```python
def format_for_chat_training(example):
    """Convert to chat training format."""
    turns = json.loads(example["data"])
    messages = []
    
    for i, turn in enumerate(turns):
        role = "user" if i % 2 == 0 else "assistant"
        messages.append({"role": role, "content": turn})
    
    return {"messages": messages}

# Apply to dataset
chat_dataset = dataset.map(format_for_chat_training)
```

### Extract Q&A Pairs
```python
def extract_qa_pairs(example):
    """Extract individual Q&A pairs if needed."""
    turns = json.loads(example["data"])
    pairs = []
    
    for i in range(0, len(turns), 2):
        if i + 1 < len(turns):
            pairs.append({
                "question": turns[i],
                "answer": turns[i + 1],
                "conversation_id": example["id"]
            })
    
    return {"qa_pairs": pairs}

# Extract all Q&A pairs
qa_dataset = dataset.map(extract_qa_pairs)
```

## 🎨 Why Conversation Format?

✅ **Preserves Context**: Multi-turn dialogue context maintained  
✅ **Natural Training**: Better for conversational AI models  
✅ **Flexible**: Can extract Q&A pairs when needed  
✅ **Efficient**: 1,468,346 conversations vs 5.6M isolated Q&A pairs  
✅ **Authentic**: Respects original conversational nature of UltraChat  

## 📈 Comparison with Q&A Format

| Metric | Q&A Pairs Format | Conversations Format |
|--------|------------------|---------------------|
| **Records** | 5.6M individual pairs | 1,468,346 conversations |
| **Context** | ❌ Lost between pairs | ✅ Fully preserved |
| **Training** | Basic question-answering | 🎯 Conversational AI |
| **Efficiency** | Fragmented | 🔄 Natural dialogue flow |
| **Use Cases** | Single-turn QA | Multi-turn chat, context-aware AI |

## 🚀 Training Applications

Perfect for:
- **Chat Model Fine-tuning**: GPT, Llama, etc.
- **Conversational AI**: Multi-turn dialogue systems
- **Instruction Following**: Context-aware response generation
- **Dialogue Research**: Conversation pattern analysis

## 📱 Data Studio Preview

This dataset is optimized for HuggingFace Data Studio:
- ✅ **Instant Preview**: No download required
- ✅ **Fast Filtering**: Query specific conversations
- ✅ **Sample Browsing**: Explore data structure easily
- ✅ **Schema Detection**: Automatic column recognition

## 🏷️ Source & License

- **Original Dataset**: [stingning/ultrachat](https://huggingface.co/datasets/stingning/ultrachat)
- **Processing**: Conversation structure preserved with sequential IDs
- **License**: Same as original UltraChat dataset

## 📊 Technical Details

- **Format**: Parquet chunks for optimal performance
- **Compression**: Snappy compression for fast loading
- **Encoding**: UTF-8 with proper JSON escaping
- **Validation**: All conversations verified for format consistency

---

💡 **Tip**: Start with streaming or select a subset for initial experiments, then scale to the full dataset as needed.