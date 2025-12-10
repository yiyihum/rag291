---
base_model:
- Vortex5/LunaMaid-12B
- Vortex5/Vermilion-Sage-12B
- inflatebot/MN-12B-Mag-Mell-R1
- Vortex5/Dark-Quill-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00165_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/6mPbbLD1oPf2297ZW3gpP.png)
# 🌌 **Abyssal-Seraph-12B**

> *Where the light of the divine meets the poetry of the abyss.*

---

## 🜂 Overview

**Abyssal-Seraph-12B** is a **multi-stage creative merge** designed for expressive storytelling, emotional depth, and lyrical dialogue.  
It was crafted through a layered fusion using [MergeKit](https://github.com/arcee-ai/mergekit):

1. 🌙 **LunaMaid × Vermilion-Sage** — merged via **NearSwap** (`t=0.0008`) to unify LunaMaid’s balanced composure with Vermilion-Sage’s radiant prose.  
2. 🕯️ **Dark-Quill × Mag-Mell-R1** — merged via **NearSwap** (`t=0.0008`) to draw forth mysticism, poetic darkness, and a sense of dreamlike gravity.  
3. ✨ Both intermediate results combined with the **Karcher Mean** — a geometric blend ensuring harmony between light and shadow.

---

## 🩶 Model Essence

| Trait | Description |
|:--|:--|
| 🧠 **Core Nature** | Philosophical, poetic, emotionally resonant |
| 💬 **Style** | Fluid prose, vivid imagery, articulate reflection |
| 💫 **Tone** | Dreamlike, balanced between divine warmth and abyssal calm |
| 🎭 **Best For** | Roleplay, character dialogue, introspection, lore writing, creative prose |

---

🧬 Merge Overview

Abyssal-Seraph-12B was created through a multi-stage, precision merge designed to blend expressive prose with poetic balance while maintaining model stability.

### 🌙 **Stage 1**
**✨ Method:** NearSwap (`t = 0.0008`)  
**🩵 Base:** [Vortex5/LunaMaid-12B](https://huggingface.co/Vortex5/LunaMaid-12B)  
**💮 Secondary:** [Vortex5/Vermilion-Sage-12B](https://huggingface.co/Vortex5/Vermilion-Sage-12B)  

<details>
<summary><b>Stage 1 Configuration</b></summary>

  ```yaml
name: First
models:
  - model: Vortex5/Vermilion-Sage-12B
merge_method: nearswap
base_model: Vortex5/LunaMaid-12B
parameters:
  t: 0.0008
dtype: bfloat16
tokenizer:
  source: Vortex5/LunaMaid-12B
```
</details>

### 🩶 **Stage 2**

⚙️ Method: NearSwap (t = 0.0008)
🖤 Base: Vortex5/Dark-Quill-12B
💫 Secondary: inflatebot/MN-12B-Mag-Mell-R1

<details>
<summary><b>Stage 2 Configuration</b></summary>

```yaml
name: Second
models:
  - model: inflatebot/MN-12B-Mag-Mell-R1
merge_method: nearswap
base_model: Vortex5/Dark-Quill-12B
parameters:
  t: 0.0008
dtype: bfloat16`
```
</details>

### 🌌 Stage 3 — **Final Merge**

⚖️ Method: Karcher Mean (tol = 1e-9, max_iter = 20000)
🜂 Inputs: First + Second
💎 Purpose:
To geometrically fuse both for coherence.
<details>
<summary><b>Final Merge Configuration</b></summary>
  
  ```yaml
models:
  - model: First
  - model: Second
merge_method: karcher
dtype: bfloat16
parameters:
  tol: 1e-9
  max_iter: 20000
tokenizer:
  source: First
```
</details>

## 🌑🜂 **Acknowledgements** 🜂🌑
- ⚙️ **mradermacher** — for *static* and *imatrix quantization*
- 🜛 **DeathGodlike** — for  *EXL3 quants*
- 🩶 **All original model authors and contributors** whose work made this model possible.
---
**Models merged in this creation:**
- [Vortex5/LunaMaid-12B](https://huggingface.co/Vortex5/LunaMaid-12B)  
- [Vortex5/Vermilion-Sage-12B](https://huggingface.co/Vortex5/Vermilion-Sage-12B)  
- [Vortex5/Dark-Quill-12B](https://huggingface.co/Vortex5/Dark-Quill-12B)  
- [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)