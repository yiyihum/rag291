---
license: llama3.1
datasets:
- medkit/simsamu
language:
- fr
- en
base_model:
- meta-llama/Llama-3.1-8B-Instruct
pipeline_tag: text-generation
tags:
- medical
- triage
- emergency
---

# Llama-3.1-8B-Instruct-LoRA-SimSAMU

This model is a fine-tuned version of **[meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)** using Low-Rank Adaptation (LoRA).

It was specifically trained on the **[medkit/simsamu](https://huggingface.co/datasets/medkit/simsamu)** dataset to perform a specialized task: generating structured, task-oriented summaries from transcripts of emergency telephone calls to the French SAMU (Service d'Aide Médicale d'Urgence).

The methodology and task are following the work presented in the **[QUARTZ](https://arxiv.org/abs/2509.26302)** paper.

## Model Description

-   **Base Model:** `meta-llama/Llama-3.1-8B-Instruct`
-   **Dataset:** `medkit/simsamu`
-   **Language:** French (`fr`)
-   **Task:** The model takes a transcript of an emergency call and generates a Triage-oriented Structured Summary, extracting key information needed for medical triage and response.

---

## Intended Use

This model is intended for research and development purposes in the field of medical NLP. Potential applications include:
-   Assisting emergency call handlers by auto-generating summaries.
-   Structuring unstructured call data for analysis.
-   Training and simulation for medical dispatchers.

**Note:** This model is a proof of concept and should **NOT** be used in a live clinical or emergency-response setting without extensive validation. 🚨

---

## How to Use

You can use this model with the `transformers` library. Make sure you are logged into your Hugging Face account and have accepted the Llama 3.1 license terms.

For more detailed examples, including the full prompts and code used, please visit the [**GitHub**](https://github.com/Mohamed-Imed-Eddine/QUARTZ) repository.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Ensure you have logged in to Hugging Face CLI
# huggingface-cli login

model_id = "Imed-Ghebriout/Llama-3.1-8B-Instruct-LoRA-SimSAMU"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# A shortened example transcript
transcript = "medecin: bonjour docteur DETOURET au SAMU 93 vous appelez pour votre grand père c'est ça ?\npatient: oui c'est bien ça\nmedecin: d'accord vous êtes avec lui là ou pas ?\npatient: non non j'arrive là devant l'immeuble et je vois il y a de la fumée partout.\nmedecin: il y a des secours sur place monsieur ?\npatient: non non, il y a personne.\nmedecin: donc votre grand père il est à quel étage ?\npatient: il est au deuxième étage.\nmedecin: il peut se déplacer lui ou pas ?\npatient: bah je sais pas je suis pas encore rentré."

# A shortened example of the system prompt
system_prompt = """Vous êtes un médecin urgentiste. Votre tâche est de résumer le dialogue médical suivant sous la forme d’un compte rendu clinique précis et structuré.
Format du compte rapport clinique:
1-Motif principal de l’appel:
2-Contexte de l’appel:
3-Contexte du patient:
4-Traitement habituel:
5-Antécédents médicaux:
6-Symptômes du patient:
7-Histoire de la maladie actuelle:
8-Hypothèses diagnostiques:
9-Plan de traitement:
10-Décision d’orientation:"""

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": f"Dialogue médical:\n{transcript}\n---"
    },
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=512,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)

response = outputs[0][input_ids.shape[-1]:]
summary = tokenizer.decode(response, skip_special_tokens=True)
print(summary)