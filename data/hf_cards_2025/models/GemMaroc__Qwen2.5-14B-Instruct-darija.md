---
library_name: transformers
tags:
- MoroccanArabic
- Darija
- GemMaroc
- conversational
- qwen
pipeline_tag: text-generation
datasets:
- GemMaroc/TULU-3-50k-darija-english
language:
- ar
- ary
- en
base_model:
- Qwen/Qwen2.5-14B-Instruct
---

# Model Card for Qwen2.5-14B-Instruct-darija

# Qwen2.5-14B-Instruct-darija

Unlocking **Moroccan Darija** proficiency in a powerful large language model, trained with a _minimal-data, green-AI_ recipe that preserves Qwen2.5-14B-Instruct's strong reasoning abilities while adding fluent Darija generation.

---

## Model at a glance

|                     | Details                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| **Model ID**        | `GemMaroc/Qwen2.5-14B-Instruct-darija`                                                                 |
| **Base model**      | [`Qwen/Qwen2.5-14B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)                        |
| **Architecture**    | Decoder-only Transformer (Qwen2.5)                                                                     |
| **Parameters**      | 14 billion                                                                                             |
| **Context length**  | 32,768 tokens                                                                                          |
| **Training regime** | Supervised fine-tuning (LoRA → merged) on 50 K high-quality Darija/English instructions TULU-50K slice |
| **License**         | Apache 2.0                                                                                             |

---

## Why another Darija model?

- **Inclusive AI** > 36 million speakers of Moroccan Arabic remain underserved by open LLMs.
- **Quality-over-quantity** A carefully curated 50 K instruction set surfaces Darija competence without sacrificing cross-lingual reasoning.
- **Green AI** Qwen2.5-14B-Instruct-darija achieves competitive Darija scores using minimal energy.
- **Balanced Performance** 14B parameters provide excellent balance between performance and resource requirements.

---

## Benchmark summary

### Darija Benchmarks

| Model                           | Darija MMLU | Darija HellaSwag | Sentiment Analysis | GSM8K Darija | Summarization (chrF) | ROUGE-1 | ROUGE-L | BERTScore |
| ------------------------------- | ----------- | ---------------- | ------------------ | ------------ | -------------------- | ------- | ------- | --------- |
| Qwen2.5-14B-Instruct            | 57.5 %      | 45.9 %           | 63.3 %             | 72.3 %       | 26.3                 | 9.1     | 8.8     | 36.2      |
| **Qwen2.5-14B-Instruct-darija** | **57.6 %**  | **51.3 %**       | **64.1 %**         | **83.3 %**   | **27.1**             | 7.3     | 7.1     | **38.8**  |

### English Benchmarks

| Model                           | MMLU       | TruthfulQA | HellaSwag  | GSM8K @5 | GSM8K Gen |
| ------------------------------- | ---------- | ---------- | ---------- | -------- | --------- |
| Qwen2.5-14B-Instruct            | 76.8 %     | 70.8 %     | 75.6 %     | 80.2 %   | 94.2 %    |
| **Qwen2.5-14B-Instruct-darija** | **75.3 %** | 61.7 %     | **79.1 %** | 75.6 %   | 92.4 %    |

<sub>Zero-shot accuracy; full table in the paper.</sub>

---

## Quick start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "GemMaroc/Qwen2.5-14B-Instruct-darija"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    max_new_tokens=1024,
    temperature=0.7,
    repetition_penalty=1.2,
    no_repeat_ngram_size=3,
)

messages = [
    {"role": "user", "content": "شنو هي نظرية 'butterfly effect'؟ فسّرها بدارجة ونقّط مثال بسيط."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(pipe(prompt)[0]["generated_text"][len(prompt):])
```

### Chat template (Qwen2.5 format)

The tokenizer provides a baked-in Jinja template that starts with a **begin-of-sequence** token (`<|im_start|>`), then alternates user/model turns, each wrapped by `<|im_start|>` … `<|im_end|>` markers. When you set `add_generation_prompt=True` it ends after the opening model tag so the model can continue:

```
<|im_start|>user
{user message}<|im_end|>
<|im_start|>assistant
```

The assistant will keep generating tokens until it decides to emit `<|im_end|>`.

```python
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
```

No manual token juggling required—the call above handles BOS, turn delimiters, and newline placement automatically.

---

Pre-quantised checkpoints will be published under the same repo tags (`qwen2.5-14b-darija-awq-int4`, `qwen2.5-14b-darija-gguf-q4_k_m`).

---

## Training recipe (one-paragraph recap)

1. **Data** Translate a 44 K reasoning slice of TULU 50K into Darija, keeping 20 % English for cross-lingual robustness.
2. **LoRA SFT** Rank 16, α = 32, 3 epochs, bf16, context 32,768.
3. **Merge & push** Merge LoRA into base weights (`peft.merge_and_unload`), convert to safetensors, upload.

---

## Limitations & ethical considerations

- Sentiment and abstractive summarisation still trail state-of-the-art.
- Tokeniser is unchanged; rare Darija spellings may fragment.
- Model may inherit societal biases present in pre-training data.
- No RLHF / RLAIF safety alignment yet – apply a moderation layer in production.

---

## Citation

If you use Qwen2.5-14B-Instruct-darija in your work, please cite:

```bibtex
@misc{skiredj2025gemmarocunlockingdarijaproficiency,
      title={GemMaroc: Unlocking Darija Proficiency in LLMs with Minimal Data},
      author={Abderrahman Skiredj and Ferdaous Azhari and Houdaifa Atou and Nouamane Tazi and Ismail Berrada},
      year={2025},
      eprint={2505.17082},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.17082},
}
```
