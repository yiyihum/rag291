---
license: mit
language:
- fr
pipeline_tag: text-generation
tags:
- SLM
- Dragoniland
- lora la dragonne
- SLM Dragoniland
- petit modèle de language
---

# 📖 Documentation Utilisateur : Dragoniland-SLM (Mini Modèle de Langage)

Bienvenue dans l'univers de **Dragoniland-SLM** ! Ce modèle est un petit modèle de langage (SLM, Small Language Model) entraîné sur un corpus de textes narratifs et créatifs. Il est conçu pour générer des continuations de phrases dans un style fantastique et absurde.

## 🎯 Quel est le but de Dragoniland-SLM ?

Le but principal de ce modèle est la **génération de texte créatif et la complétion de phrases**.

* **Complétion d'Histoires :** Fournissez le début d'une phrase ou d'un scénario, et le modèle tente de le continuer.
* **Exploration Thématique :** Le modèle a appris les thèmes de notre corpus (dragons, saisons, blagues, etc.) et les mélange de manière imprévisible.
* **Expérimentation :** Jouez avec les paramètres de génération pour trouver le ton parfait.

***

## ⚙️ Paramètres de Génération Clés

Pour utiliser et contrôler le modèle, vous interagirez avec trois paramètres principaux qui influencent directement la qualité et le style du texte généré :

| Paramètre | Description | Plage Recommandée | Effet |
| :---: | :--- | :---: | :--- |
| **`SEED_TEXT`** | 💬 La phrase ou le fragment de texte que vous fournissez pour *amorcer* la génération. | Min. 5 mots | Plus la phrase est longue et thématique, plus le contexte initial est fort. |
| **`NEXT_WORDS`** | 🔢 Le nombre de mots que le modèle doit générer après votre phrase de départ. | $10$ à $100$ | Détermine la longueur de l'histoire. |
| **`TEMPERATURE`** | 🔥 Contrôle l'aléatoire et la créativité du modèle (le "degré de folie"). | $0.1$ à $1.2$ | **Basse** (ex: $0.2$) : Cohérent, répétitif. **Haute** (ex: $1.0$) : Créatif, absurde, risque d'erreurs. |

***

## 💡 Guide d'Utilisation (Comment Obtenir de Meilleurs Résultats)

Le modèle **Dragoniland-SLM** est un Transformer avec une petite fenêtre de contexte (probablement $10$ tokens). Cela signifie qu'il a tendance à oublier le début de l'histoire très rapidement !

### 1. Choisissez la Bonne Température (🔥)

| Objectif | Température | Résultat Attendu |
| :--- | :---: | :--- |
| **Précision/Cohérence** | $0.1$ à $0.5$ | Le modèle réutilise souvent les mots de votre corpus source et reste proche du sujet. |
| **Équilibre/Par défaut** | $0.6$ à $0.8$ | Bon mélange entre structure et créativité. Recommandé pour la plupart des utilisations. |
| **Expérimentation/Folie** | $0.9$ à $1.2$ | Des thèmes étranges et des sauts logiques sont fréquents. Idéal pour des blagues absurdes. |

### 2. Donnez un Bon Amorçage (`SEED_TEXT` 💬)

* **Exemple de bon amorçage :** `"le vieux dragon jeta un sortilège puissant sur les chevaliers et l'ambiance devint"` (Fournit un thème, un ton et une structure).
* **Exemple de mauvais amorçage :** `"le"` (Le modèle n'a presque pas de contexte pour commencer).

### 3. Gérez les Répétitions

Puisque nous avons intégré une pénalité pour éviter qu'un mot ne se répète **immédiatement** après lui-même, vous devriez voir moins de répétitions de type *("le le le")*. Cependant, une température trop basse peut entraîner des boucles de phrases entières.

> **Conseil Pro :** Si le modèle commence à faire des boucles (ex: "il dit, elle dit, il dit..."), augmentez légèrement la `TEMPERATURE` pour le forcer à explorer d'autres options.

***

## ⚠️ Limitations Connues

Étant un SLM, **Dragoniland-SLM** présente des limitations typiques :

* **Manque de Cohérence à Long Terme :** Le modèle n'a qu'une mémoire de $10$ mots (tokens). Il oubliera le début d'une longue histoire.
* **Contamination :** Il peut régurgiter des fragments de métadonnées ou de listes non nettoyées présentes dans le corpus source (comme les numéros de chapitres ou les noms de fichiers).
* **Erreurs Grammaticales :** La grammaire ou la syntaxe peuvent devenir erronées ou étranges, surtout avec une température élevée.

Amusez-vous bien à explorer les mystères de **Dragoniland** ! 🐲🔮

**Exemple d'utilisation** :

```
# ==============================================================================
# 🚀 DRAGONILAND-SLM : UTILITAIRE DE GÉNÉRATION DE TEXTE 
# ==============================================================================

# 1. Installation des dépendances (Nécessaire pour Keras 3 et Hugging Face)
!pip install -q keras tensorflow torch huggingface_hub

import os
import numpy as np
import tensorflow as tf
import keras
from keras import layers
from keras import ops
import json
import shutil
from huggingface_hub import hf_hub_download

# Configuration du backend (Doit correspondre à l'entraînement original)
os.environ["KERAS_BACKEND"] = "torch"
print(f"Keras backend: {keras.config.backend()}")


# --- PARAMÈTRES DU DÉPÔT ET DE LA CONFIGURATION ---
REPO_ID = "Clemylia/Dragoniland-SLM"
MODEL_FILE = "slm_transformer_creative_model.keras"
VOCAB_FILE = "vectorization_vocab.json"
TEMP_DIR = "./slm_cache"
SEQUENCE_LENGTH = 10 # Longueur de séquence utilisée lors de l'entraînement (vérifiez si c'était 5 ou 10)

# Variables pour stocker le modèle après le premier chargement
global MODEL, VECTORIZE_LAYER, VOCAB
MODEL = None
VECTORIZE_LAYER = None
VOCAB = None


# ==============================================================================
# 2. Classe Personnalisée (Cruciale pour le chargement Keras)
# ==============================================================================

class TransformerBlock(layers.Layer):
    def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)
        self.ffn = keras.Sequential(
            [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]
        )
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def get_config(self):
        config = super().get_config()
        config.update({
            "embed_dim": self.att.key_dim,
            "num_heads": self.att.num_heads,
            "ff_dim": self.ffn.layers[0].units,
            "rate": self.dropout1.rate,
        })
        return config

    def call(self, inputs):
        input_shape = ops.shape(inputs)
        sequence_length = input_shape[1]
        causal_mask = ops.triu(ops.ones((sequence_length, sequence_length)), k=1)
        causal_mask = ops.cast(causal_mask, dtype="bool")
        attn_output = self.att(inputs, inputs, attention_mask=causal_mask)
        attn_output = self.dropout1(attn_output)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output)
        return self.layernorm2(out1 + ffn_output)


# ==============================================================================
# 3. Fonction de Chargement (Exécutée une seule fois)
# ==============================================================================

def load_dragoniland_slm():
    """Charge le modèle et le vocabulaire depuis Hugging Face."""
    global MODEL, VECTORIZE_LAYER, VOCAB

    if MODEL is not None:
        print("✅ Modèle déjà chargé en mémoire.")
        return

    print(f"\n--- TÉLÉCHARGEMENT DE {REPO_ID} ---")
    os.makedirs(TEMP_DIR, exist_ok=True)
    
    try:
        # Téléchargement des fichiers
        model_path_local = hf_hub_download(repo_id=REPO_ID, filename=MODEL_FILE, local_dir=TEMP_DIR, local_dir_use_symlinks=False)
        vocab_path_local = hf_hub_download(repo_id=REPO_ID, filename=VOCAB_FILE, local_dir=TEMP_DIR, local_dir_use_symlinks=False)

        # Chargement du vocabulaire
        with open(vocab_path_local, "r", encoding="utf-8") as f:
            VOCAB = json.load(f)
        VOCAB_SIZE = len(VOCAB)

        # Configuration de la couche TextVectorization
        VECTORIZE_LAYER = tf.keras.layers.TextVectorization(
            max_tokens=VOCAB_SIZE,
            output_mode='int',
            output_sequence_length=SEQUENCE_LENGTH
        )
        VECTORIZE_LAYER.set_vocabulary(VOCAB)

        # Chargement du modèle Keras
        custom_objects = {"TransformerBlock": TransformerBlock}
        MODEL = keras.models.load_model(model_path_local, custom_objects=custom_objects)
        
        print("✅ Modèle chargé et prêt ! 🔥")

    except Exception as e:
        print(f"\n❌ ERREUR DE CHARGEMENT : Impossible de charger Dragoniland-SLM. Vérifiez le nom du dépôt ou la connexion. Détails: {e}")
        MODEL = None
        VECTORIZE_LAYER = None

    finally:
        # Nettoyage du cache
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)


# ==============================================================================
# 4. Fonction d'Utilisation (Génération de Texte)
# ==============================================================================

def generate_dragoniland_text(seed_text: str, next_words: int = 50, temperature: float = 0.8) -> str:
    """
    Génère du texte en utilisant le modèle Dragoniland-SLM.

    Args:
        seed_text (str): La phrase ou le fragment de texte d'amorçage.
        next_words (int): Le nombre de mots à générer.
        temperature (float): Contrôle la créativité (0.1 = conservateur, 1.2 = fou).

    Returns:
        str: Le texte généré.
    """
    
    # 0. Vérification du modèle
    if MODEL is None or VECTORIZE_LAYER is None:
        load_dragoniland_slm()
        if MODEL is None:
            return "Échec de la génération : Modèle non disponible."
            
    if temperature <= 0.0:
        print("Avertissement: La température doit être > 0. Utilisation de 0.1.")
        temperature = 0.1
        
    generated_text = seed_text.lower()
    last_word_index = -1

    for _ in range(next_words):
        # 1. Préparation et Prédiction
        input_sequence = VECTORIZE_LAYER([generated_text]).numpy()
        predicted_probs = MODEL.predict(input_sequence, verbose=0)[0]

        # 2. Anti-répétition et Application de la Température
        if last_word_index != -1:
            # 2a. Forcer la probabilité du dernier mot à zéro
            predicted_probs[last_word_index] = 0.0
        
        # 2b. Appliquer la température (technique d'échantillonnage stochastique)
        predicted_probs = np.power(predicted_probs, 1.0 / temperature)
        predicted_probs = predicted_probs / np.sum(predicted_probs)
        
        # 3. Échantillonnage stochastique
        predicted_index = np.random.choice(
            a=len(predicted_probs), 
            size=1, 
            p=predicted_probs
        )[0]
        
        # 4. Mettre à jour et ajouter le mot
        last_word_index = predicted_index
        next_word = VOCAB[predicted_index]
        generated_text += " " + next_word

    return generated_text


# ==============================================================================
# 5. UTILISATION FINALE (Exemple pour l'utilisateur)
# ==============================================================================

# Charger le modèle (sera exécuté automatiquement lors du premier appel si ce bloc est omis)
load_dragoniland_slm()

if MODEL is not None:
    # --- EXEMPLE 1 : Cohérence (Température Basse) ---
    resultat_coherence = generate_dragoniland_text(
        seed_text="les dragons primaires élémentaires se réveillèrent pour", 
        next_words=30, 
        temperature=0.5
    )
    print("\n\n--- RÉSULTAT 1 (COHÉRENCE - T=0.5) ---")
    print(resultat_coherence)

    # --- EXEMPLE 2 : Créativité (Température Élevée) ---
    resultat_creativite = generate_dragoniland_text(
        seed_text="dans le ciel violet, l'étrange créature murmura", 
        next_words=40, 
        temperature=1.1
    )
    print("\n\n--- RÉSULTAT 2 (CRÉATIVITÉ - T=1.1) ---")
    print(resultat_creativite)
```