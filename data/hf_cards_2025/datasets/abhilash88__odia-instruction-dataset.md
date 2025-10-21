---
language:
- or
tags:
- odia
- instruction-following
- indian-languages
- nlp
- text-generation
- question-answering
- chat
task_categories:
- text-generation
- question-answering
size_categories:
- 100K<n<1M
license: cc-by-4.0
pretty_name: Odia Instruction Following Dataset
dataset_info:
  features:
  - name: id
    dtype: string
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: system
    dtype: string
  - name: text
    dtype: string
  - name: char_count
    dtype: int64
  - name: word_count
    dtype: int64
  - name: source_file
    dtype: string
  - name: dataset_type
    dtype: string
  - name: format
    dtype: string
  config_name: default
  splits:
  - name: train
    num_examples: 324560
  download_size: 324560
  dataset_size: 324560
---

# Odia Instruction Following Dataset

## Dataset Description

This is a comprehensive Odia language instruction-following dataset designed for training conversational AI models, chatbots, and instruction-following systems in Odia (ଓଡ଼ିଆ). The dataset contains high-quality instruction-response pairs that enable models to understand and follow instructions in the Odia language.

### Dataset Summary

- **Language**: Odia (ଓଡ଼ିଆ)
- **Total Records**: 324,560
- **Format**: Instruction-Input-Output format (Alpaca-style)
- **License**: CC-BY-4.0
- **Use Cases**: Instruction following, chatbots, question answering, conversational AI

## Dataset Structure

### Data Fields

Each record contains:

- `id`: Unique identifier for the instruction
- `instruction`: The task instruction in Odia
- `input`: Optional input context for the instruction
- `output`: Expected response/output in Odia
- `system`: System prompt or context (if any)
- `text`: Formatted text combining all fields
- `char_count`: Total character count
- `word_count`: Total word count
- `source_file`: Original source file
- `dataset_type`: Type classification
- `format`: Data format identifier

### Example Record

```json
{
  "id": "inst_12345",
  "instruction": "ଏହି ପ୍ରଶ୍ନର ଉତ୍ତର ଦିଅ",
  "input": "ଓଡ଼ିଶାର ରାଜଧାନୀ କଣ?",
  "output": "ଓଡ଼ିଶାର ରାଜଧାନୀ ହେଉଛି ଭୁବନେଶ୍ୱର। ଏହା ରାଜ୍ୟର ପ୍ରମୁଖ ସହର ଏବଂ ପ୍ରଶାସନିକ କେନ୍ଦ୍ର ଅଟେ।",
  "system": "",
  "text": "Instruction: ଏହି ପ୍ରଶ୍ନର ଉତ୍ତର ଦିଅ\n\nInput: ଓଡ଼ିଶାର ରାଜଧାନୀ କଣ?\n\nOutput: ଓଡ଼ିଶାର ରାଜଧାନୀ ହେଉଛି ଭୁବନେଶ୍ୱର...",
  "char_count": 245,
  "word_count": 38,
  "source_file": "odia_training_alpaca.json",
  "dataset_type": "instruction",
  "format": "alpaca"
}
```

## Supported Tasks

### Primary Tasks
- **Instruction Following**: Train models to follow Odia instructions
- **Question Answering**: Answer questions in Odia
- **Conversational AI**: Build Odia chatbots and virtual assistants
- **Task Completion**: Execute specific tasks based on Odia instructions

### Secondary Tasks
- **Text Generation**: Generate contextually appropriate Odia responses
- **Dialog Systems**: Multi-turn conversation in Odia
- **Educational Applications**: Odia language tutoring systems
- **Content Creation**: Generate Odia content based on prompts

## Usage Examples

### Loading the Dataset

```python
from datasets import load_dataset

# Load the instruction dataset
dataset = load_dataset("abhilash88/odia-instruction-dataset")
train_data = dataset["train"]

print(f"Total instructions: {len(train_data):,}")
print(f"Sample instruction: {train_data[0]['instruction']}")
print(f"Sample output: {train_data[0]['output']}")
```

### Training an Instruction-Following Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

# Load a suitable tokenizer for Indic languages
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert")
tokenizer.pad_token = tokenizer.eos_token

# Prepare the data for training
def format_instruction(example):
    if example["input"]:
        return f"### Instruction:\n{example['instruction']}\n\n### Input:\n{example['input']}\n\n### Response:\n{example['output']}"
    else:
        return f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['output']}"

def tokenize_function(examples):
    texts = [format_instruction(ex) for ex in examples]
    return tokenizer(texts, truncation=True, padding=True, max_length=512)

# Tokenize the dataset
tokenized_dataset = dataset.map(
    lambda examples: tokenize_function([examples]), 
    batched=False
)

# Initialize model
model = AutoModelForCausalLM.from_pretrained("gpt2")  # or use an Indic language model

# Training configuration
training_args = TrainingArguments(
    output_dir="./odia-instruction-model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    warmup_steps=100,
    logging_steps=10,
    save_steps=1000,
    evaluation_strategy="steps",
    eval_steps=500,
    save_total_limit=2,
    load_best_model_at_end=True,
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    tokenizer=tokenizer,
)

# Train the model
trainer.train()
```

### Inference Example

```python
# After training, use the model for inference
def generate_response(instruction, input_text=""):
    if input_text:
        prompt = f"### Instruction:\n{instruction}\n\n### Input:\n{input_text}\n\n### Response:\n"
    else:
        prompt = f"### Instruction:\n{instruction}\n\n### Response:\n"
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=256,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("### Response:\n")[-1]

# Example usage
instruction = "ମୋତେ ଓଡ଼ିଶାର ପ୍ରସିଦ୍ଧ ମନ୍ଦିର ବିଷୟରେ କହ"
response = generate_response(instruction)
print(response)
```

### Data Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt

# Convert to pandas for analysis
df = dataset["train"].to_pandas()

# Analyze instruction and output lengths
print(f"Average instruction length: {df['instruction'].str.len().mean():.0f} characters")
print(f"Average output length: {df['output'].str.len().mean():.0f} characters")
print(f"Records with input context: {(df['input'].str.len() > 0).sum():,} ({(df['input'].str.len() > 0).mean()*100:.1f}%)")

# Plot length distributions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

df['instruction'].str.len().hist(bins=50, ax=ax1)
ax1.set_title('Instruction Length Distribution')
ax1.set_xlabel('Characters')

df['output'].str.len().hist(bins=50, ax=ax2)
ax2.set_title('Output Length Distribution')
ax2.set_xlabel('Characters')

plt.tight_layout()
plt.show()
```

## Data Quality and Preprocessing

### Quality Assurance
- ✅ **Language Validation**: All content verified as Odia
- ✅ **Instruction Clarity**: Instructions are clear and actionable
- ✅ **Response Quality**: Outputs are relevant and helpful
- ✅ **Format Consistency**: Standardized instruction-response format
- ✅ **Encoding**: Proper UTF-8 encoding for Odia script

### Preprocessing Steps
1. **Data Extraction**: Extracted from structured JSON format
2. **Field Validation**: Ensured all required fields are present
3. **Text Formatting**: Created unified text format for training
4. **Length Calculation**: Added character and word count metrics
5. **Quality Filtering**: Removed incomplete or low-quality examples

## Dataset Statistics

### Content Analysis
- **Total Instructions**: 324,560
- **Average Instruction Length**: ~50 characters
- **Average Output Length**: ~200 characters
- **Instructions with Input**: ~60% (estimated)
- **Language**: Modern Odia (ଓଡ଼ିଆ)

### Task Distribution (Estimated)
- **Question Answering**: ~40%
- **General Instructions**: ~30%
- **Creative Tasks**: ~15%
- **Explanatory Tasks**: ~15%

## Model Training Recommendations

### Hyperparameters
- **Learning Rate**: 5e-5 to 1e-4
- **Batch Size**: 4-8 (with gradient accumulation)
- **Max Length**: 512-1024 tokens
- **Epochs**: 3-5
- **Warmup Steps**: 10% of total steps

### Best Practices
- Use Indic language tokenizers for better Odia support
- Implement proper prompt formatting during training
- Use gradient accumulation for larger effective batch sizes
- Monitor perplexity and generation quality during training
- Implement early stopping based on validation metrics

## Evaluation Metrics

### Recommended Metrics
- **BLEU Score**: For response quality evaluation
- **ROUGE Score**: For content overlap assessment
- **Perplexity**: For language modeling quality
- **Human Evaluation**: For instruction following accuracy
- **Task Success Rate**: For specific task completion

### Benchmarking
- Compare against English instruction-following models
- Evaluate on Odia-specific tasks and cultural knowledge
- Test on unseen instruction types
- Assess response quality and cultural appropriateness

## Ethical Considerations

### Responsible AI Development
- **Cultural Sensitivity**: Responses should respect Odia culture and values
- **Bias Mitigation**: Regular evaluation for harmful biases
- **Safety Measures**: Implement safeguards against harmful outputs
- **Transparency**: Clear documentation of dataset limitations

### Usage Guidelines
- ✅ Educational and research applications
- ✅ Odia language preservation efforts
- ✅ Accessibility tools for Odia speakers
- ✅ Cultural and linguistic research
- ❌ Applications that may promote harmful stereotypes
- ❌ Commercial use without proper consideration of implications

### Limitations
- **Domain Coverage**: May not cover all specialized domains
- **Cultural Context**: Limited to available cultural knowledge
- **Temporal Relevance**: Based on specific time period data
- **Response Quality**: Varies across different instruction types

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{odia_instruction_dataset_2025,
  title={Odia Instruction Following Dataset},
  author={Abhilash},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/abhilash88/odia-instruction-dataset}
}
```

## Acknowledgments

- **Odia Language Community**: For language preservation efforts
- **Instruction Dataset Creators**: Original Alpaca and similar projects
- **Open Source Community**: For tools and methodologies
- **Hugging Face**: For platform and infrastructure

## Contact and Future Work

- **Dataset Creator**: abhilash88
- **Community**: Join Odia NLP community discussions
- **Contributions**: Community contributions and improvements welcome
- **Updates**: Regular updates planned based on usage and feedback

### Planned Improvements
- **Expansion**: Additional instruction types and domains
- **Quality Enhancement**: Improved response quality and diversity
- **Multilingual**: Odia-English code-switching support
- **Specialized Domains**: Domain-specific instruction datasets

---

*This dataset represents a significant step forward in Odia conversational AI and instruction-following capabilities.* 🚀

**Keywords**: Odia, ଓଡ଼ିଆ, Instruction Following, Conversational AI, Chatbot, Indian Languages, NLP