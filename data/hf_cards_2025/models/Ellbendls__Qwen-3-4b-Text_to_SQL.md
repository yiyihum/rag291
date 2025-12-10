---
library_name: transformers
license: apache-2.0
datasets:
- gretelai/synthetic_text_to_sql
base_model:
- Qwen/Qwen3-4B-Instruct-2507
pipeline_tag: text-generation
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---

# Fine-Tuned LLM for Text-to-SQL Conversion

This model is a fine-tuned version of [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) designed to convert natural language queries into SQL statements. It was trained on the `gretelai/synthetic_text_to_sql` dataset and can provide both SQL queries and table schema context when needed.

---

## Model Details

### Model Description

This model has been fine-tuned to help users generate SQL queries based on natural language prompts. In scenarios where table schema context is missing, the model is trained to generate schema definitions along with the SQL query. The base Qwen-3-4B provides stronger multilingual support and larger context windows.  

- **Base Model:** [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)  
- **Dataset:** Gretel AI Synthetic Text-to-SQL Dataset  
- **Languages Supported (base):** many including English, Chinese, etc.  
- **License:** Apache-2.0  

### Key Features

1. Text-to-SQL Conversion: Converts natural language queries into accurate SQL statements.  
2. Schema Generation: Generates table schema context when none is provided.  
3. Optimized for Analytics and Reporting: Handles SQL queries with aggregation, grouping, filtering.  
4. Multilingual Capabilities: Base model is trained on 119 languages/dialects. :contentReference[oaicite:0]{index=0}  
5. Large Context Window: Qwen-3-4B uses long context length (32K tokens in many cases). :contentReference[oaicite:1]{index=1}

---

## Usage

### Direct Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Ellbendls/Qwen-3-4B-Text_to_SQL")
model = AutoModelForCausalLM.from_pretrained("Ellbendls/Qwen-3-4B-Text_to_SQL")

# Input prompt
query = "What is the average salary by department in 2024?"

# Tokenize input and generate output
inputs = tokenizer(query, return_tensors="pt")
outputs = model.generate(**inputs, max_length=512)

# Decode and print
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
