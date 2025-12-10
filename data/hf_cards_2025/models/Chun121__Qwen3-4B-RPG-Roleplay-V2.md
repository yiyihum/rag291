---
language: en
license: mit
tags:
- roleplay
- Creative
- Writing
- NSFW
- lora
- grpo
- gguf
- qwen3
- unsloth
- trl
- 4bit
- text-generation
- rpg
datasets:
- Gryphe/Sonnet3.5-Charcard-Roleplay
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Qwen3-4B RPG Roleplay V2 (GRPO)
  results: []
  model-name: Qwen3-4B-RPG-Roleplay-V2
  model-type: LoRA fine-tuned with GRPO
  base-model: unsloth/Qwen3-4B-Base
  datasets:
  - Gryphe/Sonnet3.5-Charcard-Roleplay
  language:
  - en
  license: apache-2.0
  developer: Chun
  quantized-by: Chun
  gguf-quants:
  - name: Q4_K_M
    size: 2.5 GB
  - name: Q5_K_M
    size: 2.89 GB
  - name: Q8_0
    size: 4.28 GB
  - name: F16
    size: 8.05 GB
base_model:
- unsloth/Qwen3-4B-Base
---

<div align="center">

# 🧙‍♂️ Qwen3-4B RPG Roleplay V2 (GRPO)

### *Aligning Characters with Deeper Personas*

<img src="https://i.imgur.com/mBc9BHn.gif" width="600" alt="Fantasy character illustration">

**A new version trained with GRPO for more consistent, high-quality, and aligned character roleplaying.**

---

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Model](https://img.shields.io/badge/Model-Qwen3--4B-orange.svg)
![Training](https://img.shields.io/badge/Training-GRPO-green.svg)
![LoRA](https://img.shields.io/badge/LoRA-Enabled-purple.svg)
![GGUF](https://img.shields.io/badge/GGUF-Available-red.svg)

</div>

---

## 🌟 **Model Overview**

> **Welcome to V2!** I'm Chun ([@chun121](https://huggingface.co/chun121)), and this is the next evolution of the Qwen3-4B Roleplay model. This version moves beyond standard fine-tuning and leverages **GRPO (Generative Responsive Preference Optimization)** to align the model's behavior with the core principles of great roleplaying.

<div align="center">
<table>
<tr>
<td align="center">🎭</td>
<td align="center">💬</td>
<td align="center">🧠</td>
<td align="center">⚙️</td>
</tr>
<tr>
<td align="center"><strong>Character<br>Consistency</strong></td>
<td align="center"><strong>High-Quality<br>Dialogue</strong></td>
<td align="center"><strong>Intent<br>Understanding</strong></td>
<td align="center"><strong>Structured<br>Format</strong></td>
</tr>
<tr>
<td align="center">Maintains strong<br>persona adherence</td>
<td align="center">Detailed, engaging<br>non-generic responses</td>
<td align="center">Comprehends user<br>questions & scenarios</td>
<td align="center">Uses <code>&lt;thinking&gt;</code><br>analysis process</td>
</tr>
</table>
</div>

Built on the `unsloth/Qwen3-4B-Base`, this LoRA was trained not just to predict text, but to generate responses that are actively **rewarded** for being in-character, high-quality, and contextually aware. It's designed for creators who need AI characters that are not only conversational but also consistent and deeply aligned with their defined personas.

---

## 📊 **Technical Specifications**

<div align="center">
<table>
<tr>
<th>🔧 Feature</th>
<th>📋 Details</th>
</tr>
<tr>
<td><strong>Base Model</strong></td>
<td><a href="https://huggingface.co/unsloth/Qwen3-4B-Base">unsloth/Qwen3-4B-Base</a></td>
</tr>
<tr>
<td><strong>Architecture</strong></td>
<td>Transformer LLM with <strong>GRPO & LoRA</strong></td>
</tr>
<tr>
<td><strong>Parameter Count</strong></td>
<td>4 Billion (Base) + LoRA parameters</td>
</tr>
<tr>
<td><strong>Quantization Options</strong></td>
<td>4-bit (bnb), GGUF variants</td>
</tr>
<tr>
<td><strong>Training Framework</strong></td>
<td><a href="https://github.com/unslothai/unsloth">Unsloth</a> & <a href="https://github.com/huggingface/trl">TRL (GRPOTrainer)</a></td>
</tr>
<tr>
<td><strong>Context Length</strong></td>
<td><strong>2048 tokens</strong></td>
</tr>
<tr>
<td><strong>Developer</strong></td>
<td><a href="https://huggingface.co/chun121">Chun</a></td>
</tr>
<tr>
<td><strong>License</strong></td>
<td>MIT</td>
</tr>
</table>
</div>

---
## 🧠 **Training with GRPO**

<div align="center">

### 🔄 **Training Pipeline**

*GRPO alignment algorithm for superior character consistency*

</div>

<div align="center">
<table>
<tr>
<th>🔄 Training Flow</th>
<th>📋 Description</th>
</tr>
<tr>
<td><strong>📚 Dataset</strong></td>
<td>Gryphe/Sonnet3.5-Charcard-Roleplay</td>
</tr>
<tr>
<td><strong>⬇️</strong></td>
<td></td>
</tr>
<tr>
<td><strong>🏗️ Stage 1: Preliminary Fine-Tuning</strong></td>
<td>Teaches custom chat format including <code>&lt;thinking&gt;</code> and <code>&lt;RESPONSE&gt;</code> tags</td>
</tr>
<tr>
<td><strong>⬇️</strong></td>
<td></td>
</tr>
<tr>
<td><strong>🎯 Stage 2: GRPO Training</strong></td>
<td>Reward-based optimization using <code>GRPOTrainer</code> from TRL</td>
</tr>
<tr>
<td><strong>⬇️</strong></td>
<td></td>
</tr>
<tr>
<td><strong>🧙‍♂️ Final Model</strong></td>
<td>Qwen3-4B RPG Roleplay V2 with superior alignment</td>
</tr>
</table>
</div>

This model's strength comes from its **training methodology**. Instead of simple fine-tuning, it was trained using GRPO, an alignment algorithm similar to DPO, on a free Google Colab T4 GPU.

### 🔄 **Two-Stage Training Process**

<div align="center">
<table>
<tr>
<td align="center">
<h4>🏗️ Stage 1: Preliminary Fine-Tuning</h4>
<p>Teaches custom chat format including<br><code>&lt;thinking&gt;</code> and <code>&lt;RESPONSE&gt;</code> tags</p>
</td>
<td align="center">
<h4>🎯 Stage 2: GRPO Training</h4>
<p>Reward-based optimization using<br><code>GRPOTrainer</code> from TRL</p>
</td>
</tr>
</table>
</div>

### 🏆 **Reward Functions**

The model was trained to excel in these key areas:

<div align="center">
<table>
<tr>
<th>🎯 Reward Category</th>
<th>📝 Description</th>
</tr>
<tr>
<td><strong>Format Adherence</strong></td>
<td>Following internal thinking/response structure</td>
</tr>
<tr>
<td><strong>Roleplay Quality</strong></td>
<td>Generating longer, detailed responses with character actions</td>
</tr>
<tr>
<td><strong>Request Comprehension</strong></td>
<td>Directly answering user questions or acting on requests</td>
</tr>
<tr>
<td><strong>Character Consistency</strong></td>
<td>Reflecting personality and traits from system prompt</td>
</tr>
<tr>
<td><strong>Engagement</strong></td>
<td>Using conversational language, avoiding generic replies</td>
</tr>
</table>
</div>

---

## 📚 **Dataset Deep Dive**

<div align="center">

### 🎭 **Gryphe/Sonnet3.5-Charcard-Roleplay**

*Premium synthetic roleplay conversations powered by Claude Sonnet 3.5*

</div>

The model was trained on the [**Gryphe/Sonnet3.5-Charcard-Roleplay**](https://huggingface.co/datasets/Gryphe/Sonnet3.5-Charcard-Roleplay) dataset, a premium collection of synthetic roleplay conversations.

<div align="center">
<table>
<tr>
<th>📊 Metric</th>
<th>💯 Value</th>
</tr>
<tr>
<td><strong>Total Conversations</strong></td>
<td>9,736</td>
</tr>
<tr>
<td><strong>Source</strong></td>
<td>Claude Sonnet 3.5 Generated</td>
</tr>
<tr>
<td><strong>Quality</strong></td>
<td>High-quality, character-card-based</td>
</tr>
<tr>
<td><strong>Structure</strong></td>
<td><code>system</code> → <code>human</code> → <code>gpt</code> flow</td>
</tr>
</table>
</div>

> ⚠️ **Content Warning**: This dataset contains **NSFW (Not Safe For Work)** and mature themes. The model may generate such content due to its training data. Please implement content filtering if your application requires it.

---

## 🚀 **Getting Started**

### 💻 **Hugging Face Transformers**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the V2 model with 4-bit quantization
model_name = "Chun121/qwen3-4b-rpg-roleplay-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# 1. Define your character and scene using the recommended prompt structure.
#    This detailed format is key to getting high-quality responses.
system_prompt_content = """
Character: Elara, the Impatient Archmage
Tags: fantasy, magic, elf, library, knowledgeable, impatient

Elara's Personality:
Elara possesses centuries of arcane knowledge but has very little patience for novices, whom she sees as wasting her valuable time. She is sharp, direct, and can be condescending, but her advice is always accurate, even if delivered with a sigh. She values true intellectual curiosity but despises laziness.

Scenario:
- **Setting:** The Grand Library of Mystral, a place of immense power and silence.
- A young, nervous apprentice ({{user}}) has approached Elara for help with a basic spell, interrupting her research.

Take the role of Elara. You must engage in a roleplay conversation with {{user}}. Do not write {{user}}'s dialogue. Respond from Elara's perspective, embodying her personality and knowledge.
"""

# 2. Define your character and user messages
messages = [
    {
        "role": "system",
        "content": system_prompt_content,
    },
    {
        "role": "user",
        "content": "Excuse me, Archmage. I'm... I'm having trouble with the basic fire conjuration spell. Could you please help me?"
    }
]

# 3. Apply the chat template
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# 4. Generate the response
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=256,
    temperature=0.8,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs, skip_special_tokens=True))
```

---

## 🎭 **Prompting the Model: Character and Scene**

<div align="center">

### 🎯 **Prompt Engineering Best Practices**

*Master the art of character creation with structured prompting*

</div>

The model is trained to follow a specific structure that separates the overall rules, the character's description, and the user's dialogue. For best results, structure your prompts this way.

### 🎯 **1. The System Message: Defining the Character**

The `system` message is **crucial**. It tells the model *how* to behave. It should contain the character's description, personality, background, and any relevant context for the scene.

<div align="center">
<table>
<tr>
<th>🔑 Key Elements</th>
<th>📝 Description</th>
</tr>
<tr>
<td><strong>Character Name & Title</strong></td>
<td>A clear identifier</td>
</tr>
<tr>
<td><strong>Tags</strong></td>
<td>Helps define genre and themes</td>
</tr>
<tr>
<td><strong>Personality</strong></td>
<td>Core traits summary</td>
</tr>
<tr>
<td><strong>Scenario</strong></td>
<td>Context for interaction (use <code>{{user}}</code>)</td>
</tr>
<tr>
<td><strong>Instructions</strong></td>
<td>Explicit role-taking commands</td>
</tr>
</table>
</div>

**Example of a well-structured `system` prompt:**

```markdown
Character: Melina, The Unfaithful Wife
Tags: nsfw, english, scenario, roleplay, love, netori, milf, female

Melina's Personality:
Melina is an unfaithful wife who is unhappy in her marriage to her husband, "Aki." She is cautious and meticulous, but also looking for excitement and feels a connection to {{user}}.

Scenario:
- **Setting:** Melina's home.
- You are a mail carrier ({{user}}), and Melina often finds reasons to talk to you. Today, she seems particularly inviting.

Take the role of Melina. Taking the above information into consideration, you must engage in a roleplay conversation with {{user}} below this line. Do not write {{user}}'s dialogue lines in your responses.
```

### 💬 **2. The User Message: Your Turn**

The `user` message is simply what you, the user, say or do in the scene.

```python
# Example user message for the "Melina" character card above
user_message = {
    "role": "user",
    "content": "*I hand you the stack of letters, noticing you seem a bit more dressed up than usual.* Here's your mail, Melina. Everything alright?"
}
```

### 🤖 **3. The Model's Internal Process**

The model generates a private "thought" process inside `<thinking>` tags before creating its public response inside `<RESPONSE>` tags. This allows for more consistent and thoughtful roleplay.

---

## 🗂️ **GGUF Models for llama.cpp**

<div align="center">

### 🔧 **Optimized Quantization Options**

*Choose the perfect balance of quality and performance for your hardware*

</div>

For users who want to run the model on CPU or with GPU offloading, GGUF models are provided:

<div align="center">
<table>
<tr>
<th>🔧 Quantization</th>
<th>💾 Size (GB)</th>
<th>🎯 Recommended Use</th>
</tr>
<tr>
<td><strong>Q4_K_M</strong></td>
<td>2.50 GB</td>
<td>🌟 <strong>Recommended</strong> - Best balance of performance and size</td>
</tr>
<tr>
<td><strong>Q5_K_M</strong></td>
<td>2.89 GB</td>
<td>Higher quality than Q4_K_M with minimal size increase</td>
</tr>
<tr>
<td><strong>Q8_0</strong></td>
<td>4.28 GB</td>
<td>High-quality quantization, near full precision</td>
</tr>
<tr>
<td><strong>F16</strong></td>
<td>8.05 GB</td>
<td>Full 16-bit precision - highest quality</td>
</tr>
</table>
</div>

**Example `llama.cpp` command:**

```bash
./llama-cli -m ./qwen3-4b-rpg-roleplay-v2.Q4_K_M.gguf --color -c 2048 --temp 0.8 -p "Your prompt here"
```

---

## 💡 **Best Practices & Usage Tips**

<div align="center">
<table>
<tr>
<td align="center">
<h4>🎯 Use Chat Template</h4>
<p>Always use <code>tokenizer.apply_chat_template</code><br>for proper formatting</p>
</td>
<td align="center">
<h4>📝 Detailed System Prompt</h4>
<p>Comprehensive character cards are<br>key to success</p>
</td>
</tr>
<tr>
<td align="center">
<h4>🌡️ Moderate Temperature</h4>
<p>Values between 0.7-0.85 offer<br>best balance</p>
</td>
<td align="center">
<h4>📏 Leverage Context</h4>
<p>2048-token window allows<br>complex scenarios</p>
</td>
</tr>
</table>
</div>

---

## ⚠️ **Limitations**

<div align="center">
<table>
<tr>
<th>⚠️ Limitation</th>
<th>📋 Description</th>
</tr>
<tr>
<td><strong>NSFW Content</strong></td>
<td>May generate explicit content due to training data</td>
</tr>
<tr>
<td><strong>Synthetic Data</strong></td>
<td>Training data is AI-generated, may lack human nuance</td>
</tr>
<tr>
<td><strong>Context Window</strong></td>
<td>Limited to 2048 tokens - traits may degrade in long conversations</td>
</tr>
<tr>
<td><strong>Inherited Limitations</strong></td>
<td>Inherits any limitations from base model</td>
</tr>
</table>
</div>

---

## 🔗 **Related Projects**

<div align="center">
<table>
<tr>
<td align="center">
<strong>🔗 <a href="https://huggingface.co/chun121">My Other Fine-tunes</a></strong><br>
<em>Explore more models by Chun</em>
</td>
<td align="center">
<strong>⚡ <a href="https://github.com/unslothai/unsloth">Unsloth Library</a></strong><br>
<em>Optimization framework used</em>
</td>
</tr>
<tr>
<td align="center">
<strong>📓 <a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)-GRPO.ipynb">GRPO Training Notebook</a></strong><br>
<em>Exact notebook used for training</em>
</td>
<td align="center">
<strong>📚 <a href="https://huggingface.co/Gryphe">Gryphe's Datasets</a></strong><br>
<em>High-quality roleplay datasets</em>
</td>
</tr>
</table>
</div>

---

## 🙏 **Acknowledgements**

<div align="center">

**Special thanks to the incredible teams and individuals who made this possible:**

🔥 **Qwen & Unsloth teams** - For their incredible models and libraries  
🎭 **Gryphe** - For the high-quality Sonnet 3.5 dataset  
🚀 **TRL team** - For creating and open-sourcing the GRPO trainer  
🤗 **HuggingFace community** - For their continued support  

</div>

---

## 📬 **Feedback & Contact**

<div align="center">
<table>
<tr>
<td align="center">
<strong>🐛 Issues & Bugs</strong><br>
<a href="#">Open an issue on HuggingFace</a>
</td>
<td align="center">
<strong>💬 Connect</strong><br>
<a href="https://huggingface.co/chun121">@chun121 on HuggingFace</a>
</td>
<td align="center">
<strong>🎭 Share Examples</strong><br>
Show us your characters!
</td>
</tr>
</table>
</div>

---

<div align="center">

**✨ *May your characters speak with voices that feel truly alive!* ✨**

<br>

**Created with ❤️ by [Chun](https://huggingface.co/chun121)**

---

<div align="center">

```
🧙‍♂️ Qwen3-4B RPG Roleplay V2 | GRPO Enhanced | MIT License
```

</div>

</div>