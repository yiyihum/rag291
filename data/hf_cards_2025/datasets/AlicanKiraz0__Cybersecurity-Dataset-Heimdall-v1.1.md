---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- cybersecurity
- defensive-security
- instruction-tuning
size_categories:
- 10K<n<100K
dataset_info:
  version: 1.1.0
---

# Cybersecurity Defense Instruction-Tuning Dataset (v1.1)

## TL;DR
**21 258** high‑quality *system / user / assistant* triples for training alignment‑safe, defensive‑cybersecurity LLMs. Curated from **100 000 +** technical sources, rigorously cleaned and filtered to enforce strict ethical boundaries. Apache‑2.0 licensed.

---

## 1  What’s new in v1.1  (2025‑06‑21)

| Change | v1.0 | v1.1 |
|--------|------|------|
| Rows | 2 500 | **21 258** (+760 %) |
| Covered frameworks | OWASP Top 10, NIST CSF | + MITRE ATT&CK, ASD Essential 8, CIS Controls, SSL/TLS, modern auth (OAuth2, OIDC, SAML) |
| Domains | Web & network | + Cloud, DevSecOps, Cryptography, AI‑security interplay |
| Quality checks | Manual spot review | + Automatic static‑analysis, hallucination scans, refusal‑pattern tests |
| License | Apache 2.0 | Apache 2.0 (unchanged) |

---

## 2  Dataset Summary

| Property | Value |
|----------|-------|
| **Language** | English |
| **License** | Apache 2.0 |
| **Format** | Parquet (columnar) |
| **Rows** | 21 258 |
| **Columns** | `system`, `user`, `assistant`, `row_id`, `source_hash` |
| **Split** | `train` (100 %) |

Each example is engineered for *instruction‑following* fine‑tuning:

```json
{
  "system": "You are a seasoned cyber‑defense AI that follows industry ethics...",
  "user": "Compare the mitigation steps for Reflected vs Stored XSS in a modern SPA.",
  "assistant": "Reflected and Stored XSS share core mitigation pillars—output encoding...",
}
```

---

## 3  Dataset Structure

### 3.1  Fields
| Field | Type | Description |
|-------|------|-------------|
| `system` | *string* | Role & ethics prompt (defensive, refuse malicious) |
| `user` | *string* | Realistic question / instruction |
| `assistant` | *string* | Detailed, technically accurate answer with defensive focus |

### 3.2  Split
All rows are provided in a single **train** split.

---

## 4  Dataset Creation Process

1. **Massive crawl** – 100 k+ public technical pages (blogs, RFCs, standards, white‑papers).  
2. **Content extraction** – boilerplate stripping, language detection, heuristic paragraph segmentation.  
3. **Topical filtering** – keyword & embedding search for defensive‑security relevance.  
4. **Instruction synthesis** – custom prompt‑engineering pipeline turns paragraphs into *system/user/assistant* triples, enforcing:  
   * Alignment with **OWASP Top 10**, **MITRE ATT&CK**, **NIST CSF**, **DEFENCE‑in‑depth**.  
   * Built‑in **refusal templates** for offensive requests.  
   * Depth suited to senior professionals & PhD curricula.  
5. **Quality gates**  
   * Deduplication (MinHash + LSH).  
   * PII stripping & profanity check.  
   * Automated hallucination & inconsistency detection.  
   * Manual review sample (≈ 3 %).  

---

## 5  Usage

```python
from datasets import load_dataset

ds = load_dataset(
    "AlicanKiraz0/Cybersecurity-Defense-InstructionTuning-v1_1",  # update with final repo name
    split="train"
)

print(ds[0]["system"])
print(ds[0]["user"])
print(ds[0]["assistant"])
```

### Fine‑tuning tip
For SFT on 8‑bit QLoRA (7 B‑13 B models) we recommend:

```python
from trl import SFTTrainer
trainer = SFTTrainer(
    model=base_model,
    dataset=ds,
    dataset_text_field="text",        # if you concatenate into a single prompt
    max_seq_length=4096,
    packing=True,
    neftune_noise_alpha=5.0
)
```

---

## 6  Ethical Considerations

* **Dual‑use risk** – Technical depth could assist attackers.  
  *Mitigation:* rows embed refusal patterns; no exploit‑building instructions.  
* **Bias** – Focus on Western frameworks (NIST, OWASP).  
  *Mitigation:* roadmap includes regional standards (ISO 42001, GDPR).  
* **Data provenance** – All sources were publicly available; licensed content respected.  

---

## 7  Limitations

* English‑only.  
* Primarily defensive viewpoint; red‑team tactics present only for context.  
* Security rapidly evolves – refresh cycle planned every 6 months.  

---

## 8  Citation

```bibtex
@dataset{kiraz_2025_cyberdefense_v11,
  author    = {Alican Kiraz},
  title     = {Cybersecurity Defense Instruction Tuning Dataset (v1.1)},
  year      = {2025},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/AlicanKiraz0/Cybersecurity-Dataset-Heimdall-v1.1}
}
```

---

## 9  Changelog

* **v1.1.0** (2025‑06‑21) – Expanded to 21 258 rows, broader framework coverage, added provenance metadata, improved automatic quality checks.  
* **v1.0.0** (2025‑06‑17) – Initial release with 2 500 rows.  

---

## 10  Contributing

PRs welcome! Please ensure:

* Defensive focus only  
* Accurate, citation‑backed content  
* Follow the `system / user / assistant` schema  
* Accept Apache 2.0 re‑licensing  

---
