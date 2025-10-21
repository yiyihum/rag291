---
license: mit
library_name: transformers
base_model:
- deepseek-ai/DeepSeek-V3-0324
- deepseek-ai/DeepSeek-R1
pipeline_tag: text-generation
---
# DeepSeek-R1T-Chimera

<div align="center">
<img src="https://354918363417-runtime-assets.s3.eu-central-1.amazonaws.com/company_logo_light.svg"
     alt="TNG Logo" 
     width="400"
     style="display: inline-block; vertical-align: middle;"/>
</div>
<br>
<div align="center">
  <a href="LICENSE" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<br>
<div align="center">
  <a href="https://x.com/tngtech/status/1916284566127444468" style="margin: 2px;">
    <img alt="Benchmarks" src="R1T-Chimera_Benchmarks_20250427_V1.jpg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>


**Model merge of DeepSeek-R1 and DeepSeek-V3 (0324)**

An open weights model combining the intelligence of R1 with the token efficiency of V3.

For details on the construction process and analyses of Chimera model variants, please [read our paper](https://arxiv.org/abs/2506.14794). 

[Paper on arXiV](https://arxiv.org/abs/2506.14794) | [Announcement on X](https://x.com/tngtech/status/1916284566127444468) | [LinkedIn post](https://www.linkedin.com/posts/tng-technology-consulting_on-the-weekend-we-released-deepseek-r1t-chimera-activity-7323008947236290560-Cf2m) | [Try it on OpenRouter](https://openrouter.ai/tngtech/deepseek-r1t-chimera:free)

**Update:** we released [R1T2-Chimera](https://huggingface.co/tngtech/DeepSeek-TNG-R1T2-Chimera) that is both faster *and* smarter than R1.


## Model Details

- **Architecture**: DeepSeek-MoE Transformer-based language model
- **Combination Method**: Merged model weights from DeepSeek-R1 and DeepSeek-V3 (0324)
- **Release Date**: 2025-04-27

## Use, Out-of-scope Use, Limitations, Risks, Recommendations et al
Regarding R1T Chimera, we ask you to follow the careful guidelines that Microsoft has created for their "MAI-DS-R1" DeepSeek-based model. 

These guidelines are available [here on Hugging Face](https://huggingface.co/microsoft/MAI-DS-R1).

## Contact

- Email: research@tngtech.com
- X.com: @tngtech

## Citation

```
@misc{tng_technology_consulting_gmbh_2025,
	author       = { TNG Technology Consulting GmbH },
	title        = { DeepSeek-R1T-Chimera },
	year         = 2025,
    month        = {April},
	url          = { https://huggingface.co/tngtech/DeepSeek-R1T-Chimera },
	doi          = { 10.57967/hf/5330 },
	publisher    = { Hugging Face }
}

```