---
license: mit
language:
- zh
- en
tags:
- creative-writing
- instruction-tuning
- cot
- finetuning
- novel
size_categories:
- 1K<n<10K
task_categories:
- text-generation
pretty_name: CreativeWriting
---

# Dataset Card for telecomadm1145/creative_writing

## Dataset Details

### Dataset Description

This dataset is a small-scale **instruction–response dataset** focused on **creative writing tasks**.  
Each example consists of a **prompt** (instruction specifying writing style, perspective, tone, etc.) and a **response** (a story segment or novel-like output).  

The dataset emphasizes:
- **Creative Writing** (light novel style, emotional narrative, dialogue-driven, descriptive prose).
- **Chain-of-Thought (CoT) reasoning** embedded in prompts to guide structured writing.
- **Rich stylistic variation** including first-person / third-person perspective, tense control, tone settings (humorous, melancholic, suspenseful, etc.).

- **Curated by:** telecomadm1145  
- **Funded by:** Not funded (personal project)  
- **Language(s) (NLP):** Chinese with English CoT
- **License:** MIT  

### Dataset Sources

- **Repository:** [Hugging Face Dataset](https://huggingface.co/datasets/telecomadm1145/creative_writing)  
- **Source Data:** Extracted, cleaned, and reformulated from publicly available online novels (especially light novels).  

---

## Uses

### Direct Use

- Fine-tuning or instruction-tuning **LLMs** for:
  - Creative story generation
  - Controllable narrative perspective & tone
  - CoT-guided long-form writing  
- Prompt engineering experiments for structured writing tasks.  

### Out-of-Scope Use

- Not suitable for factual QA or knowledge-intensive tasks.  
- Not intended for training safety-critical applications (e.g., legal, medical, financial advice).  

---

## Dataset Structure

- **Format:** JSON  
- **Splits:**  
  - `train`
- **Fields:**  
  - `prompt`: Instruction text specifying style, perspective, tone, etc.  
  - `response`: Generated story or narrative continuation.