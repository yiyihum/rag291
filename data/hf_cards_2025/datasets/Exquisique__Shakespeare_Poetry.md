---
license: apache-2.0
language:
- en
tags:
- poetry
- shakespeare
- instruction-tuning
- text-generation
size_categories:
- n<1K
task_categories:
- text-generation
pretty_name: Shakespeare Poetry Instruction Dataset
---
# Shakespeare Poetry Instruction Dataset
## Dataset Description
This dataset provides a high-quality, curated collection of instruction-response pairs designed for fine-tuning large language models (LLMs) to generate poetry in the style of William Shakespeare. The dataset is sourced from public domain Shakespearean works including the Sonnets, *Venus and Adonis*, *The Rape of Lucrece*, and other poetic texts.

Each record is formatted for instruction-following tasks, making it ideal for training chat models, instruction-tuned models, and creative writing applications that require adherence to classical poetic styles.

## Dataset Structure
### Data Format
The dataset is stored as JSONL (JSON Lines), with one record per line. Each record contains three fields:
- **`instruction`**: A natural language prompt requesting a poem in Shakespearean style about a specific topic or theme
- **`input`**: Currently blank (reserved for future multi-field input extensions)
- **`output`**: The corresponding Shakespearean text (stanza, sonnet, or poem excerpt)

### Example Record
```json
{
  "instruction": "Write a poem in the style of Shakespeare about 'From fairest creatures we desire increase,'",
  "input": "",
  "output": "From fairest creatures we desire increase,\nThat thereby beauty's rose might never die,\nBut as the riper should by time decease,\nHis tender heir might bear his memory:"
}
```

### Data Statistics
- **Total Records**: 688 instruction-output pairs
- **Source Material**: Public domain works by William Shakespeare
- **Language**: English (Early Modern English)
- **Format**: JSONL

## Usage
### Loading the Dataset
You can load this dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("Exquisique/Shakespeare_Poetry")
```

### Applications
This dataset is suitable for:
- **Instruction Fine-Tuning**: Train models like GPT, LLaMA, Gemma, or Mistral to follow creative writing instructions
- **Style Transfer**: Teach models to transform modern text into Shakespearean poetic style
- **Poetic Generation**: Generate original sonnets, verses, and poetic passages in Early Modern English
- **Creative Writing Assistants**: Build specialized chatbots for literary and educational applications
- **Educational Tools**: Create interactive learning experiences for studying classical poetry

### Fine-Tuning Example
For fine-tuning with frameworks like Hugging Face Transformers or Axolotl:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments

# Load your base model
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")

# Load dataset
dataset = load_dataset("Exquisique/Shakespeare_Poetry")

# Prepare training
training_args = TrainingArguments(
    output_dir="./shakespeare-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=100,
)

# Train (add your data collator and preprocessing)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
)

trainer.train()
```

## Data Preprocessing
### Pipeline Overview
The dataset was created through the following preprocessing pipeline:
1. **Collection**: Merged multiple public domain Shakespeare poetic works into a single corpus
2. **Segmentation**: Split the corpus into coherent blocks (stanzas, sonnets, or thematic passages) using double newlines as delimiters
3. **Filtering**: Removed blocks shorter than 30 characters to ensure substantive content
4. **Topic Inference**: Extracted first lines or themes to create contextually relevant instruction prompts
5. **Formatting**: Structured each block as an instruction-response pair in JSON format

### Preprocessing Script
The complete preprocessing script is provided below:

```python
import re
import json

# Input/output file paths
input_file = 'shakespeare_merged.txt'
output_file = 'shakespeare_poetry_instruction.jsonl'

# Read the merged Shakespeare corpus
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split into blocks (stanzas/poems) and filter by minimum length
blocks = [
    block.strip() 
    for block in content.split('\n\n') 
    if len(block.strip()) > 30
]

def infer_topic(text):
    """Extract topic from first line for instruction prompt."""
    first_line = text.split('\n')[0]
    words = first_line.split()
    if len(words) <= 10:
        return first_line
    else:
        return "the following theme"

# Generate instruction-response pairs
with open(output_file, 'w', encoding='utf-8') as out_f:
    for block in blocks:
        topic = infer_topic(block)
        prompt = f'Write a poem in the style of Shakespeare about "{topic}".'
        
        sample = {
            "instruction": prompt,
            "input": "",
            "output": block
        }
        
        out_f.write(json.dumps(sample, ensure_ascii=False) + "\n")

print(f"✓ Wrote {len(blocks)} instruction-response pairs to {output_file}")
```

## License
- **Source Material**: The original Shakespearean texts are in the public domain
- **Dataset & Code**: This curated dataset and preprocessing code are released under the **Apache 2.0 License**

## Citation
If you use this dataset in your research or applications, please cite it as follows:

### BibTeX
```bibtex
@dataset{shakespeare_poetry_instruction,
  author = {Exquisique},
  title = {Shakespeare Poetry Instruction Dataset},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/Exquisique/Shakespeare_Poetry}}
}
```

### APA
```
Exquisique. (2025). Shakespeare Poetry Instruction Dataset [Data set]. Hugging Face. https://huggingface.co/datasets/Exquisique/Shakespeare_Poetry
```

## Acknowledgments
This dataset builds upon the timeless works of William Shakespeare, whose poetry remains in the public domain. We acknowledge the literary heritage and educational value of these texts, and encourage users to respect the cultural significance of the source material when developing applications.

## Contact
For questions, issues, or contributions, please use the [Community tab](https://huggingface.co/datasets/Exquisique/Shakespeare_Poetry/discussions) or visit the [repository](https://huggingface.co/datasets/Exquisique/Shakespeare_Poetry).