---
base_model:
- Vortex5/Abyssal-Seraph-12B
- Vortex5/LunaMaid-12B
- Vortex5/MegaMoon-Karcher-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
![ComfyUI_00166_](https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/R8qqP7yfPosXsa4bbgMn8.png)
# 🌘 Lunar-Abyss-12B

> Born where moonlight touches the deep — thought meets desire, and reason dreams.


## 🌑 Overview

**Lunar-Abyss-12B** was made to combine the coherency and stability of **LunaMaid-12B** with the evocative prose and edgy flair of **Abyssal-Seraph-12B**.


## ⚖️ Merge Method — DELLA

🧩 **Base:** Vortex5/MegaMoon-Karcher-12B  
💎 **Inputs:** Vortex5/LunaMaid-12B + Vortex5/Abyssal-Seraph-12B  

<details>
<summary><b>Configuration</b></summary>

```yaml
models:
  - model: Vortex5/LunaMaid-12B
    parameters:
      weight:
        - filter: self_attn
          value: [0.35, 0.4, 0.6, 0.8, 1.0, 0.9, 0.6, 0.3]
        - filter: mlp
          value: [0.20, 0.25, 0.35, 0.45, 0.45, 0.40, 0.30, 0.20]
        - value: [0.25, 0.3, 0.35, 0.4, 0.4, 0.35, 0.3, 0.25]
      density: 0.55
      epsilon: 0.3

  - model: Vortex5/Abyssal-Seraph-12B
    parameters:
      weight:
        - filter: mlp
          value: [0.3, 0.5, 0.8, 1.0, 1.0, 0.9, 0.7, 0.4]
        - value: [0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.2]
      density: 0.5
      epsilon: 0.4
merge_method: della
base_model: Vortex5/MegaMoon-Karcher-12B
parameters:
  lambda: 1.0
  normalize: true
dtype: bfloat16
tokenizer:
  source: Vortex5/Abyssal-Seraph-12B
```
</details>

## 🌌 Essence of the Merge

Like moonlight reflecting on dark water, Lunar-Abyss carries both clarity and depth.  
It thinks with the calm focus of LunaMaid yet speaks with the emotional pulse of Abyssal-Seraph.  
Every response flows with a quiet duality — logic beneath, creativity above — neither overpowering the other.  

For fans of expressive writing and immersive roleplay, it offers a tone that’s reflective, and mysterious.


## 🎭 Roleplay & Creative Focus

Designed for **narrative storytelling**, **introspective dialogue**, and **emotion-driven writing**.  


## 🌒 Acknowledgements 🌘

- ⚙️ **mradermacher** — static / imatrix quantization  
- 🜛 **DeathGodlike** — EXL3 quants 
- 🩶 **All original model authors and contributors** whose work made this model possible.


### 🧾 Models Merged


**Models merged in this creation:**
- [Vortex5/LunaMaid-12B](https://huggingface.co/Vortex5/LunaMaid-12B)  
- [Vortex5/Abyssal-Seraph-12B](https://huggingface.co/Vortex5/Abyssal-Seraph-12B)
- [Vortex5/MegaMoon-Karcher-12B](https://huggingface.co/Vortex5/MegaMoon-Karcher-12B)