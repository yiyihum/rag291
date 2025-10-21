---
library_name: transformers
license: apache-2.0
datasets:
- nbeerbower/GreatFirewall-DPO
- nbeerbower/Schule-DPO
- nbeerbower/Purpura-DPO
- nbeerbower/Arkhaios-DPO
- jondurbin/truthy-dpo-v0.1
- antiven0m/physical-reasoning-dpo
- flammenai/Date-DPO-NoAsterisks
- flammenai/Prude-Phi3-DPO
- Atsunori/HelpSteer2-DPO
- jondurbin/gutenberg-dpo-v0.1
- nbeerbower/gutenberg2-dpo
- nbeerbower/gutenberg-moderne-dpo
base_model:
- nbeerbower/Rombos-EVAGutenberg-TIES-Qwen2.5-32B
---

![image/png](https://huggingface.co/nbeerbower/Dumpling-Qwen2.5-32B/resolve/main/dumpling_cover.png?download=true)

# Dumpling-Qwen2.5-32B

[nbeerbower/Rombos-EVAGutenberg-TIES-Qwen2.5-32B](https://huggingface.co/nbeerbower/Rombos-EVAGutenberg-TIES-Qwen2.5-32B) finetuned on: 
* [nbeerbower/GreatFirewall-DPO](https://huggingface.co/datasets/nbeerbower/GreatFirewall-DPO)
* [nbeerbower/Schule-DPO](https://huggingface.co/datasets/nbeerbower/Schule-DPO)
* [nbeerbower/Purpura-DPO](https://huggingface.co/datasets/nbeerbower/Purpura-DPO)
* [nbeerbower/Arkhaios-DPO](https://huggingface.co/datasets/nbeerbower/Arkhaios-DPO)
* [jondurbin/truthy-dpo-v0.1](https://huggingface.co/datasets/jondurbin/truthy-dpo-v0.1)
* [antiven0m/physical-reasoning-dpo](https://huggingface.co/datasets/antiven0m/physical-reasoning-dpo)
* [flammenai/Date-DPO-NoAsterisks](https://huggingface.co/datasets/flammenai/Date-DPO-NoAsterisks)
* [flammenai/Prude-Phi3-DPO](https://huggingface.co/datasets/flammenai/Prude-Phi3-DPO)
* [Atsunori/HelpSteer2-DPO](https://huggingface.co/datasets/Atsunori/HelpSteer2-DPO)
* [jondurbin/gutenberg-dpo-v0.1](https://huggingface.co/datasets/jondurbin/gutenberg-dpo-v0.1)
* [nbeerbower/gutenberg2-dpo](https://huggingface.co/datasets/nbeerbower/gutenberg2-dpo)
* [nbeerbower/gutenberg-moderne-dpo](https://huggingface.co/datasets/nbeerbower/gutenberg-moderne-dpo).

### Method

[ORPO tuned](https://mlabonne.github.io/blog/posts/2024-04-19_Fine_tune_Llama_3_with_ORPO.html) with 8x A100 for 2 epochs.