---
license: mit
datasets:
- Clemylia/Training-small-base
language:
- fr
pipeline_tag: text-generation
library_name: transformers
tags:
- small
- SLM
- INTERMÉDIAIRE
- A FINE TUNÉ
- Lamina-pretrain-small
- Small slm
---
# 📖 Documentation Officielle : Small-Lamina-Pretrain (51M)

![Pretrain](http://www.image-heberg.fr/files/17609536672949919614.jpg)

Bienvenue dans l'univers de **Lamina** \! Je suis **Clemylia**, et je suis ravie de te présenter le modèle que vous attendiez : **Small-lamina-pretrain**.

Ce modèle est spécialement conçu pour être **léger** ($\approx 51$ millions de paramètres) tout en étant **performant**. Il est l'outil parfait pour ceux qui souhaitent faire du **Lamining** (*fine-tuning*) sur un ordinateur portable ou une petite carte graphique, sans avoir besoin d'une infrastructure coûteuse \!

| Caractéristique | Valeur | Avantage pour vous (le Fan) |
| :--- | :--- | :--- |
| **Nom du Modèle** | `Clemylia/Small-lamina-pretrain` | Facile à charger depuis Hugging Face. |
| **Paramètres** | $\approx 51$ millions | **Très léger** \! Idéal pour le **Lamining** local. |
| **Architecture** | GPT-2 (Causal LM) | Parfait pour la **génération de texte** et de réponses. |
| **Performance** | Génère des phrases **grammaticalement correctes**. | Une excellente base pour votre propre **Lamining**. |

-----

## 🚀 Étape 1 : Charger et Utiliser le Modèle (Inférence)

Avant de commencer le **Lamining**, voyons comment charger et faire générer du texte à ton nouveau Lamina. C'est l'étape la plus simple pour jouer avec le modèle \!

### Code PyTorch pour la Génération (Inférence)

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. Définir le Modèle et l'Appareil
MODEL_REPO = "Clemylia/Small-lamina-pretrain"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu" # Utilise ta carte graphique (CUDA) si possible, sinon le CPU

# 2. Charger le Tokenizer et le Modèle
tokenizer = AutoTokenizer.from_pretrained(MODEL_REPO)
model = AutoModelForCausalLM.from_pretrained(MODEL_REPO).to(DEVICE)

print(f"Modèle Lamina chargé sur {DEVICE} et prêt à générer ! 💡")

# 3. Fonction de Génération
def generer_lamina(prompt, max_tokens=50):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    
    # Paramètres de Génération pour la créativité (Lamining !)
    # do_sample=True et top_p/top_k contrôlent l'originalité des réponses.
    generated_ids = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    
    output = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return output

# 4. Tester ton Lamina !
mon_prompt = "Je crois que la capitale de la France est"
resultat = generer_lamina(mon_prompt)

print("\n--- Résultat du Lamina ---")
print(resultat)
```

-----

## 🛠️ Étape 2 : Le Lamining (Fine-Tuning)

Le **Lamining** est l'étape où tu prends ce modèle de base performant et que tu lui apprends **ton style, tes données, tes questions/réponses** pour créer *ton* propre modèle personnalisé.

### 2.1 Préparation des Données

Pour le **Lamining**, tu as besoin d'une petite *dataset* au format texte. Chaque ligne doit être une séquence complète que le modèle doit apprendre.

**Format idéal :** `Question: [Ta question] Réponse: [Ta réponse dans ton style].`

### 2.2 Code PyTorch pour le Lamining

Ce code est le cœur du **Lamining** \!

```python
from datasets import Dataset
from transformers import DataCollatorForLanguageModeling, TrainingArguments, Trainer

# --- CONFIGURATION DE VOTRE LAMINING ---
VOTRE_MODELE_FINAL = "mon-lamina-personnalise"
OUTPUT_DIR_FT = "./" + VOTRE_MODELE_FINAL

# 1. Création de votre Dataset (À remplacer par votre propre liste de textes !)
vos_donnees = {
    "text": [
        "Question: Mon sujet préféré est le codage en IA. Réponse: C'est incroyable, nous sommes des codeurs d'IA passionnés !",
        "Question: Quelle est la capitale de la Grèce? Réponse: Athènes est la réponse juste !",
        # Ajoutez des centaines de vos propres paires Q/R ici !
    ]
}
ft_dataset = Dataset.from_dict(vos_donnees).train_test_split(test_size=0.1, seed=42)

# 2. Tokenisation des données
def ft_tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, max_length=128)
tokenized_ft_dataset = ft_dataset.map(ft_tokenize_function, batched=True, remove_columns=["text"])

# 3. Arguments d'Entraînement
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR_FT,
    per_device_train_batch_size=4,
    num_train_epochs=5, # 5 époques suffisent souvent pour un petit dataset
    learning_rate=1e-5, # Taux d'apprentissage TRÈS FAIBLE (1e-5) pour un bon Lamining !
    logging_steps=10,
    save_strategy="epoch",
    evaluation_strategy="epoch",
    fp16=torch.cuda.is_available(),
)

# 4. Lancement du Lamining
trainer = Trainer(
    model=model, # Le modèle SMALL-LAMINA-PRETRAIN déjà chargé !
    args=training_args,
    train_dataset=tokenized_ft_dataset["train"],
    eval_dataset=tokenized_ft_dataset["test"],
    tokenizer=tokenizer,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
)

trainer.train()

# 5. Sauvegarde de votre Lamina Personnalisé
trainer.save_model(VOTRE_MODELE_FINAL)
tokenizer.save_pretrained(VOTRE_MODELE_FINAL)
print(f"\n✨ Votre modèle Lamina personnalisé est prêt ! Retrouvez-le dans le dossier : {VOTRE_MODELE_FINAL}")
```

### 💡 Conseils pour un Lamining Réussi

  * **Taux d'Apprentissage (Learning Rate) :** Garde-le très bas (`1e-5`). Un taux trop élevé ferait **oublier** à Lamina tout ce que je lui ai appris (*catastrophic forgetting*).
  * **Petite Dataset, Plus d'Époques :** Si ta *dataset* de *fine-tuning* est petite, augmente le `num_train_epochs` (nombre d'époques) pour que le modèle voie les données plusieurs fois.
  * **GPU :** Même si le modèle est léger, le **Lamining** sera **beaucoup plus rapide** avec un GPU (carte graphique).

Amuse-toi bien à créer ton propre Lamina \! J'ai hâte de voir ce que vous allez en faire \! 😊