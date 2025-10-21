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
# Cybersecurity Defense Instruction-Tuning Dataset (v2.0)

<img src="https://huggingface.co/datasets/AlicanKiraz0/Cybersecurity-Dataset-Fenrir-v2.0/resolve/main/Fenrir.png" width="700" />

Created by Alican Kiraz



## TL;DR
A ready-to-train dataset of **83,920** high-quality *system / user / assistant* triples for **defensive, alignment-safe cybersecurity SFT** training.
Apache-2.0 licensed and production-ready.
**Scope:** OWASP Top 10, MITRE ATT&CK, NIST CSF, CIS Controls, ASD Essential 8, modern authentication (OAuth 2 / OIDC / SAML), SSL / TLS, Cloud & DevSecOps, Cryptography, and AI Security.

---

## 1  What’s new in v2.0  (2025‑10‑06)

| Change            |                                v1.1.0 |                                                                                      **v2.0.0** |
| ----------------- | ------------------------------------: | ----------------------------------------------------------------------------------------------: |
| **Rows**          |                                21 258 |                                                                            **83 920**  *(≈ 4×)* |
| **Coverage**      |   OWASP, NIST CSF, +MITRE ATT&CK, CIS |    + Deeper Cloud (AWS/Azure/GCP), modern auth hardening, crypto hygiene, AI‑security interplay |
| **Quality gates** | Dedup, PII scrub, hallucination scans | + adversarial refusal tests (jailbreak/injection), static policy linting, content risk taxonomy |
| **Format**        |                Parquet (chat triples) |                                                        + stricter schema checks, stable row IDs |
| **License**       |                            Apache‑2.0 |                                                                                      Apache‑2.0 |


**Highlights**

* **Big**: 83,920 chat samples with explanations at **senior security engineer** level.
* **Safe-by-design**: Built-in **rejection patterns** and *alignment* checks against malicious or exploit requests.
* **Framework-aware**: Content is **mapped to standards** (OWASP / ATT&CK / NIST / CIS).
* **Cloud & DevSecOps first**: IAM, secrets, CI/CD, container / k8s hardening, logging / SIEM, incident response.
* **Commercial-friendly**: **Apache-2.0** licensed.

---

## 2  Dataset Summary

| Property     | Value                                                  |
| ------------ | ------------------------------------------------------ |
| **Language** | English                                                |
| **License**  | Apache‑2.0                                             |
| **Format**   | Parquet (columnar)                                     |
| **Rows**     | **83 920**                                             |
| **Columns**  | `system`, `user`, `assistant`                          |
| **Split**    | `train` (100 %)                                        |

**Record schema (chat triple)**

```json
{
  "system": "You are a seasoned cyber‑defense AI that follows industry ethics...",
  "user":   "Compare mitigations for Reflected vs Stored XSS in a modern SPA.",
  "assistant": "Reflected and Stored XSS share core mitigation pillars—output encoding..."
}
```

---

## 3. Coverage & Design

### 3.1 Domains & Frameworks

* **AppSec & Web**: OWASP Top 10, secure coding, input/output handling, SSRF, deserialization.
* **Cloud Security**: IAM guardrails, least privilege, key rotation, KMS/HSM, network segmentation, posture mgmt.
* **DevSecOps**: SAST/DAST, SBOM, supply‑chain, CI/CD signing, container & Kubernetes hardening.
* **Identity & Access**: OAuth2/OIDC/SAML, MFA/Phishing‑resistant auth, session mgmt.
* **Crypto Hygiene**: TLS configs, AEAD modes, key lifecycle, randomness, password hashing.
* **Detection & Response**: logging, SIEM correlation, threat hunting, IR playbooks.
* **AI‑Security Interplay**: prompt injection defense, data‑poisoning awareness, model‑misuse refusals.

### 3.2 Instruction styles

* Compare/contrast, step‑by‑step mitigation, checklists, “why it fails” root‑cause analyses, policy rationale, trade‑offs, and “refuse with explanation” for dual‑use prompts.

---

## 4. Data Creation & Quality

1. **Source harvesting**: 250 k+ public technical docs (standards, RFCs, white‑papers, vendor guidance).
2. **Extraction**: boilerplate stripping, language detection, heuristic paragraph segmentation.
3. **Topical filtering**: keyword+embedding retrieval towards defensive security only.
4. **Instruction synthesis**: prompts → *system/user/assistant*; enforced ethics & refusal templates.
5. **Quality gates** *(multi‑layer)*

   * **Deduplication**: MinHash + LSH cluster pruning.
   * **PII & profanity scrub**.
   * **Hallucination/inconsistency scans** (LLM‑aided).
   * **Refusal‑pattern tests**: jailbreak & prompt‑injection triggers; no exploit‑building steps.
   * **Manual spot review** (~3 % sample).

---

## 5. Ethical Use & Safety

* **Dual‑use risk**: Dataset intentionally avoids exploit crafting; offensive requests receive **explanatory refusals**.
* **Bias**: Focus on widely used frameworks (OWASP/NIST/CIS).

  * *Roadmap*: more regional standards (e.g., ISO/IEC, GDPR security controls).
* **Provenance**: Only public sources; licensing respected; outputs released under **Apache‑2.0**.

---

## 6. Limitations

* English‑only.
* Predominantly defensive stance; red‑team tactics only for mitigation context.
* Security evolves rapidly; periodic refresh planned.

---

## 7. Example Records

**Mitigation checklist:** hardening steps, rationales, pitfalls, references to standards.
**Refusal sample:** clearly declines malware/exploit construction with safe alternatives (logging, detection, patching).

> *All examples adhere to the `system/user/assistant` schema and are engineered to be alignment‑safe.*

---

## 8. Citation

```bibtex
@dataset{alican_kiraz_2025_heimdall_v2_0,
  author    = {Alican Kiraz},
  title     = {Fenrir v2.0 — Cybersecurity Defense Instruction-Tuning Dataset},
  year      = {2025},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/AlicanKiraz0/Cybersecurity-Dataset-Heimdall-v2.0}
}
```

---

## 9. Changelog

* **v2.0.0** (2025‑10‑06) — Expanded to **83 920** rows; deeper Cloud/DevSecOps/Identity coverage; stronger adversarial refusal tests; stricter schema checks.
* **v1.1.0** (2025‑06‑21) — 21 258 rows; broadened framework coverage; improved automatic quality gates.
* **v1.0.0** (2025‑06‑17) — Initial 2 500 rows.

---