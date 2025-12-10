---
tags:
- medical
- french
- experimental
- research
- test-only
license: other
language:
- fr
model_type: causal-lm
library_name: transformers
pipeline_tag: text-generation
widget:
- text: '[SYSTEM] Tu es un assistant de recherche médicale expérimental.

    [USER] Donne un exemple d’anamnèse structurée (sans conseil médical).'
---

# 🧪 medgemma (version modifiée) — **Test Only** par **Déméter Santé**

> ⚠️ **Avertissement important — Test Only**  
> Ce modèle est une **version modifiée de *medgemma***, distribuée par **Déméter Santé** **à des fins de test et d’expérimentation uniquement**.  
> **Il ne doit en aucun cas être utilisé pour un avis clinique, un diagnostic, un traitement, une décision médicale, ni dans un contexte de production.**  
> Ce dépôt est fourni **tel quel**, sans garantie.

---

## ✨ Présentation

Cette branche de **medgemma** a été **adaptée par Déméter Santé** pour explorer :
- le **format conversationnel** (chat template),
- des **réglages de génération** (température, top-p, pénalités de répétition),
- l’**intégration out-of-the-box** avec `transformers`, OpenWebUI et les Endpoints compatibles OpenAI (`/v1`).

L’objectif est **purement expérimental** : évaluer la **faisabilité technique** et la **qualité linguistique** sur des jeux de prompts francophones **non cliniques**.

---

## 🧩 Contenu du repo

- `config.json` — configuration de l’architecture (chargée par `AutoConfig`)
- `model.safetensors.index.json` + `model-0000X-of-0000Y.safetensors` — poids shardés au format *safetensors*
- `tokenizer.json` / `tokenizer.model` + `tokenizer_config.json` — vocabulaire & règles
- `special_tokens_map.json` / `added_tokens.json` — jetons spéciaux & ajoutés
- `generation_config.json` — valeurs par défaut de génération
- `chat_template.jinja` — formatage conversationnel (system/user/assistant)
- `preprocessor_config.json` / `processor_config.json` — si besoin pour modalité supplémentaire

> Remarque : les noms exacts peuvent varier selon votre build.

---

## ✅ Cas d’usage prévus (R&D uniquement)

- **Expérimentation linguistique** (français général)  
- **Tests de prompting** et de format conversationnel  
- **Prototypage outillage** (chaînes de génération, UI de chat, MLOps)

## ⛔️ Hors périmètre (interdit)

- **Conseil médical** (diagnostic, triage, traitement, prescription, priorisation)  
- **Usage clinique** ou **décisionnel** impactant des personnes réelles  
- **Mise en production** ou exposition à des utilisateurs finaux

---

## 🚀 Démarrage rapide (Transformers)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch

REPO_ID = "demeter-sante/medgemma-test"  # ☐ Remplacez par le nom réel du repo

tok = AutoTokenizer.from_pretrained(REPO_ID, use_fast=True)
gen_cfg = GenerationConfig.from_pretrained(REPO_ID)

model = AutoModelForCausalLM.from_pretrained(
    REPO_ID,
    torch_dtype=torch.bfloat16,   # ☐ ou float16/auto selon votre matériel
    device_map="auto"
)

messages = [
    {"role": "system", "content": "Tu es un assistant de recherche expérimental. N’offre pas de conseil médical."},
    {"role": "user", "content": "Explique la différence entre résumé extractif et abstractive en 5 lignes."}
]

# Si le tokenizer supporte apply_chat_template :
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tok(prompt, return_tensors="pt").to(model.device)

out = model.generate(
    **inputs,
    generation_config=gen_cfg,
    max_new_tokens=256
)

print(tok.decode(out[0], skip_special_tokens=True))

