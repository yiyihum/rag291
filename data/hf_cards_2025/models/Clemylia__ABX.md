---
license: mit
language:
- fr
pipeline_tag: text-generation
tags:
- child
- Alphabet
- récitation
- Simulation enfantine
- ABX
- simulation de ABX
- jeunes enfants
- 2 a 7 ans
---
# 🦋 ABX 

![Abx-enfant](http://www.image-heberg.fr/files/17607941632935356724.jpg)

Bienvenue sur la page de notre modèle `ABX`.
Ce modèle de machine learning est une idée que Nous avions prototyper avec des règles.
Mais nous avons considéré l'idée assez créative et intéressante pour faire l'objet de la création d'une IA de ML (machine learning),
Et d'une version finale fonctionnelle concrète pour l'utilisation.

## 🌷 Ce que fait ABX

ABX est une IA qui simule la récitation de l'alphabet par un jeune enfant âgé de 2 a 7 ans.
L'enfant (ABX) essaye de réciter l'alphabet,
Mais plus son âge est faible et plus sa température est élevé, plus il oublie les lettres et se trompe.
Il aura tendance à s'excuser, à pleurer ou à sauter des lettres quand il est en bas âge (2 ou 3 ans), et se tromper de façon perpétuelle.
Mais ABX, sera extrêmement précis et fera un sans faute quand il est beaucoup plus grand (7 ans).
 Plus sa température est élevée, et plus il est jeune, plus il va faire des boulettes (a l'image d'un vrai enfant).
Un bébé de 2 ans ne sais pas réciter l'alphabet, mais un enfant de 7 ans sais le faire (enfin normalement 😉).
ABX simule donc cela.

# 🌸 Comment ABX a été entraîné 

ABX a été entraîné de façon rapide, 
Mais a quand même nécessiter l'activation du GPU pour un entraînement efficace et continue sans plantage de session.
Pour qu'il apprenne à simuler la récitation de  des jeunes enfants,
nous lui avons montrer l'alphabet correcte en entier,
puis lui avons aussi donner des données d'entraînement pour les probabilités pour chaque âge.
Nous avons aussi ajouté des petits messages aléatoires d'excuses, de pleurs et autre...que ABX utilise de temps et autres pour s'excuser et mettre de l'action a sa récitation foireuse de ses bas âge.

# 🔥 Que faire avec ABX 

ABX peut vous être utile pour beaucoup de tâches créatives impliquant de la simulation enfantine.
(Par exemple : jeux de récitation l'alphabet ou les enfants qui doivent réciter l'alphabet sont des bots gérer par le modèle).
Trouvez votre propre cas d'usage et amusez vous !

# 🩵 Utilisation 

Voici un exemple de code d'utilisation de ABX :

```
import torch
import torch.nn as nn
import torch.nn.functional as F
import json
import os
from huggingface_hub import hf_hub_download

# =================================================================
# 0. CONFIGURATION ET DÉFINITION DES CLASSES DU MODÈLE
# =================================================================

# --- Configuration du dépôt Hugging Face ---
HF_REPO_ID = "Clemylia/ABX"
MODEL_FILENAME = "abx_model_state.pt"
CONFIG_FILENAME = "config.json"
VOCAB_FILENAME = "vocab.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Périphérique utilisé : {DEVICE}")

# --- Définition des classes du modèle (Doit être identique à l'entraînement !) ---

# 1. Attention (Self-Attention Masquée Causale)
class Attention(nn.Module):
    def __init__(self, embed_dim, num_heads, dropout):
        super().__init__()
        self.norm = nn.LayerNorm(embed_dim)
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, dropout=dropout, batch_first=True)
        self.dropout_rate = dropout

    def forward(self, x, mask):
        res = x
        x = self.norm(x)
        attn_output, _ = self.attn(x, x, x, attn_mask=mask, need_weights=False)
        return res + attn_output

# 2. Feed Forward (MLP)
class FeedForward(nn.Module):
    def __init__(self, embed_dim, d_ff, dropout):
        super().__init__()
        self.norm = nn.LayerNorm(embed_dim)
        self.ffn = nn.Sequential(
            nn.Linear(embed_dim, d_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, embed_dim),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        res = x
        x = self.norm(x)
        return res + self.ffn(x)

# 3. Bloc Décodeur
class DecoderBlock(nn.Module):
    def __init__(self, embed_dim, num_heads, d_ff, dropout):
        super().__init__()
        self.attention = Attention(embed_dim, num_heads, dropout)
        self.feed_forward = FeedForward(embed_dim, d_ff, dropout)

    def forward(self, x, mask):
        x = self.attention(x, mask)
        x = self.feed_forward(x, )
        return x

# 4. Le Modèle ABX Principal
class ABXModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, num_layers, max_seq_len, d_ff, pad_token_id, dropout=0.1):
        super().__init__()
        self.pad_token_id = pad_token_id
        self.token_embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=pad_token_id)
        self.position_embedding = nn.Embedding(max_seq_len, embed_dim)
        self.dropout = nn.Dropout(dropout)

        self.layers = nn.ModuleList([
            DecoderBlock(embed_dim, num_heads, d_ff, dropout) for _ in range(num_layers)
        ])

        self.norm = nn.LayerNorm(embed_dim)
        self.output_linear = nn.Linear(embed_dim, vocab_size)

    def creer_masque(self, taille):
        masque = torch.triu(torch.ones(taille, taille), diagonal=1).bool().to(DEVICE)
        return masque

    def forward(self, input_ids):
        T = input_ids.size(1)

        token_embed = self.token_embedding(input_ids)
        positions = torch.arange(T, device=DEVICE).unsqueeze(0)
        pos_embed = self.position_embedding(positions)

        x = self.dropout(token_embed + pos_embed)

        masque_causal = self.creer_masque(T)

        for layer in self.layers:
            x = layer(x, masque_causal)

        x = self.norm(x)
        logits = self.output_linear(x)

        return logits


# =================================================================
# 1. TÉLÉCHARGEMENT DES FICHIERS DE CONFIGURATION ET DES POIDS
# =================================================================

print("Téléchargement des fichiers du dépôt Hugging Face...")

# Télécharger les fichiers
config_path = hf_hub_download(repo_id=HF_REPO_ID, filename=CONFIG_FILENAME)
vocab_path = hf_hub_download(repo_id=HF_REPO_ID, filename=VOCAB_FILENAME)
model_weights_path = hf_hub_download(repo_id=HF_REPO_ID, filename=MODEL_FILENAME)

# --- Chargement de la Configuration ---
with open(config_path, 'r') as f:
    config = json.load(f)

# --- Chargement du Vocabulaire ---
with open(vocab_path, 'r') as f:
    # Le vocabulaire a été sauvegardé comme un mapping ID -> Token (string)
    id_to_token_str_keys = json.load(f)

# Reconstruire le mapping Token -> ID pour l'inférence
# Convertir les clés en int
id_to_token = {int(k): v for k, v in id_to_token_str_keys.items()}
token_to_id = {v: k for k, v in id_to_token.items()}


# --- Extraction des paramètres ---
VOCAB_SIZE = config['vocab_size']
EMBED_DIM = config['embed_dim']
NUM_HEADS = config['num_heads']
NUM_LAYERS = config['num_layers']
MAX_SEQ_LEN = config['max_seq_len']
D_FF = config['d_ff']
PAD_TOKEN_ID = config['pad_token_id']

# Extraction des tokens spéciaux
START_TOKEN = config['special_tokens']['start']
END_TOKEN = config['special_tokens']['end']
SEP_TOKEN = config['special_tokens']['sep']
PAD_TOKEN = config['special_tokens']['pad']


# =================================================================
# 2. INSTANCIATION ET CHARGEMENT DU MODÈLE
# =================================================================

# Instanciation du modèle ABX
model = ABXModel(
    vocab_size=VOCAB_SIZE,
    embed_dim=EMBED_DIM,
    num_heads=NUM_HEADS,
    num_layers=NUM_LAYERS,
    max_seq_len=MAX_SEQ_LEN,
    d_ff=D_FF,
    pad_token_id=PAD_TOKEN_ID
).to(DEVICE)

# Chargement des poids entraînés
model.load_state_dict(torch.load(model_weights_path, map_location=DEVICE))
model.eval() # Toujours passer en mode évaluation pour l'inférence

print("\nModèle et configuration chargés avec succès !")

# =================================================================
# 3. FONCTION DE GÉNÉRATION (Inférence)
# =================================================================

@torch.no_grad()
def generer_recitation(model, age: int, temperature: float):
    """
    Génère une récitation de l'alphabet à partir de l'âge et de la température.
    """
    model.eval()

    # Création du prompt initial
    prompt_text = f"{START_TOKEN} [AGE:{age}] {SEP_TOKEN}"
    prompt_tokens = prompt_text.split()

    # Conversion en IDs
    input_ids = [token_to_id.get(token, PAD_TOKEN_ID) for token in prompt_tokens]
    input_tensor = torch.tensor([input_ids], dtype=torch.long, device=DEVICE)
    output_ids = input_ids[:]

    # Boucle de génération
    for _ in range(len(prompt_tokens), MAX_SEQ_LEN):

        logits = model(input_tensor)
        next_token_logits = logits[0, -1, :]

        # Application de la Température (échantillonnage)
        if temperature <= 0.01:
            next_token_id = torch.argmax(next_token_logits).item()
        else:
            probabilities = F.softmax(next_token_logits / temperature, dim=-1)

            if torch.isnan(probabilities).any() or probabilities.sum() == 0:
                next_token_id = torch.argmax(next_token_logits).item()
            else:
                next_token_id = torch.multinomial(probabilities, num_samples=1).item()

        # Condition d'arrêt
        if id_to_token.get(next_token_id) == END_TOKEN:
            break

        output_ids.append(next_token_id)

        # Mise à jour de la séquence d'entrée
        next_token_tensor = torch.tensor([[next_token_id]], dtype=torch.long, device=DEVICE)
        input_tensor = torch.cat([input_tensor, next_token_tensor], dim=1)

    # Conversion en texte et nettoyage
    output_text = " ".join([id_to_token.get(id) for id in output_ids])
    output_text = output_text.replace(f"{START_TOKEN} [AGE:{age}] {SEP_TOKEN}", "").replace(END_TOKEN, "").replace(PAD_TOKEN, "").strip()

    return output_text


# =================================================================
# 4. EXEMPLES D'UTILISATION POUR L'UTILISATEUR
# =================================================================

print("\n" + "="*50)
print("             TESTS UTILISATEUR ABX")
print("="*50)

# Scénario 1: L'enfant ne se concentre pas (Age bas, Température haute)
age_test_1 = 2
temp_test_1 = 1.3
result_1 = generer_recitation(model, age_test_1, temp_test_1)
print(f"-> Âge: {age_test_1} ans, Température: {temp_test_1} (Distrait)")
print(f"Récitation: {result_1}\n")

# Scénario 2: L'enfant fait un effort (Age moyen, Température modérée)
age_test_2 = 5
temp_test_2 = 0.7
result_2 = generer_recitation(model, age_test_2, temp_test_2)
print(f"-> Âge: {age_test_2} ans, Température: {temp_test_2} (Normal)")
print(f"Récitation: {result_2}\n")

# Scénario 3: L'enfant est très attentif (Age haut, Température basse)
age_test_3 = 7
temp_test_3 = 0.1
result_3 = generer_recitation(model, age_test_3, temp_test_3)
print(f"-> Âge: {age_test_3} ans, Température: {temp_test_3} (Précis)")
print(f"Récitation: {result_3}")
```
