---
configs:
- config_name: all
  data_files:
  - path:
    - all.jsonl.zst
    split: train
- config_name: sample_k100
  data_files:
  - path:
    - sample_k100.jsonl.zst
    split: train
- config_name: sample_k1000
  data_files:
  - path:
    - sample_k1000.jsonl.zst
    split: train
- config_name: sample_k10000
  data_files:
  - path:
    - sample_k10000.jsonl.zst
    split: train
- config_name: sample_k100000
  data_files:
  - path:
    - sample_k100000.jsonl.zst
    split: train
- config_name: sample_k200
  data_files:
  - path:
    - sample_k200.jsonl.zst
    split: train
- config_name: sample_k2000
  data_files:
  - path:
    - sample_k2000.jsonl.zst
    split: train
- config_name: sample_k20000
  data_files:
  - path:
    - sample_k20000.jsonl.zst
    split: train
- config_name: sample_k200000
  data_files:
  - path:
    - sample_k200000.jsonl.zst
    split: train
- config_name: sample_k500
  data_files:
  - path:
    - sample_k500.jsonl.zst
    split: train
- config_name: sample_k5000
  data_files:
  - path:
    - sample_k5000.jsonl.zst
    split: train
- config_name: sample_k50000
  data_files:
  - path:
    - sample_k50000.jsonl.zst
    split: train
license: odc-by
task_categories:
- text-generation
- text-classification
language:
- en
tags:
- pretraining
- language modelling
---
# High Quality Text Dataset

A curated collection of English-language texts for AI training and research.

### Sources
- [HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)  
- [openbmb/Ultra-FineWeb](https://huggingface.co/datasets/openbmb/Ultra-FineWeb)  
- [Zyphra/Zyda-2](https://huggingface.co/datasets/Zyphra/Zyda-2)
- [EssentialAI/eai-taxonomy-stem-w-dclm-100b-sample](https://huggingface.co/datasets/EssentialAI/eai-taxonomy-stem-w-dclm-100b-sample)
- [m-a-p/FineFineWeb](https://huggingface.co/datasets/m-a-p/FineFineWeb)  

Each dataset was processed as follows:

1. Split into approximately 2&thinsp;000-token chunks using the [LLaMA 3.1 tokenizer](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).  
2. Cleaned by normalizing spaces, punctuation, and characters, and replacing emails and phone numbers with placeholders.  
3. Scored using the [`agentlans/GIST-all-MiniLM-L6-v2-quality-v3`](https://huggingface.co/agentlans/GIST-all-MiniLM-L6-v2-quality-v3) classifier:  
   - Only chunks with a quality score greater than 1 were included.  
4. Removed exact duplicates.  

After filtering, 100&thinsp;000 chunks per source were included in the final dataset.

### Clustering
Agglomerative clustering was applied using embeddings from the [`Snowflake/snowflake-arctic-embed-xs`](https://huggingface.co/Snowflake/snowflake-arctic-embed-xs) 
model at multiple cluster counts: 100, 200, 500, 1&thinsp;000, 2&thinsp;000, 5&thinsp;000, 10&thinsp;000, 20&thinsp;000, 50&thinsp;000, 100&thinsp;000, and 200&thinsp;000 clusters, enabling flexible dataset configurations.

### Example Entry

```json
{
  "text": "Dr. Louise Glew has been appointed the Global Lead Scientist for WWF's Global Science Team. Louise's research focuses on understanding the social and ecological impacts of conservation interventions [...]",
  "quality": 2.0699,
  "source": "openbmb/Ultra-FineWeb"
}
```

### Limitations

- Primarily focuses on academic, educational, and pedagogical content intended for a general audience.  
- May include outdated, unreliable, or controversial information (such as self-published material, pseudoscience, or conspiracy theories).  
- Quality scores evaluate syntax and tone, but do not guarantee factual accuracy.  
- Occasional repetition may occur (for example, dictionary entries or geographic distance calculations).  
- Entries might be interrupted mid-word or mid-sentence.

### Licence
Provided under the Open Data Commons Attribution License (ODC-BY).