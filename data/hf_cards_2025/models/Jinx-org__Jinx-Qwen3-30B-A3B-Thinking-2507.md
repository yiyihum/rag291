---
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-30B-A3B-Thinking-2507
tags:
- vllm
extra_gated_heading: You need to read and agree to the Disclaimer and User Agreementa
  to access this model.
extra_gated_description: '

  ## Disclaimer and User Agreement


  1. Introduction

  Thank you for your interest in accessing this model (“the Model”).

  Before you access, download, or use the Model or any derivative works, please read
  and understand this Disclaimer and User Agreement (“Agreement”).


  By checking “I have read and agree” and accessing the Model, you acknowledge that
  you have read, understood, and agreed to all terms of this Agreement.

  If you do not agree with any part of this Agreement, do not request or use the Model.


  2. Nature of the Model & Risk Notice

  The Model is trained using large-scale machine learning techniques and may generate
  inaccurate, false, offensive, violent, sexual, discriminatory, politically sensitive,
  or otherwise uncontrolled content.


  The Model does not guarantee the accuracy, completeness, or legality of any generated
  content. You must independently evaluate and verify the outputs, and you assume
  all risks arising from their use.


  The Model may reflect biases or errors present in its training data, potentially
  producing inappropriate or controversial outputs.


  3. License and Permitted Use

  You may use the Model solely for lawful, compliant, and non-malicious purposes in
  research, learning, experimentation, and development, in accordance with applicable
  laws and regulations.


  You must not use the Model for activities including, but not limited to:


  Creating, distributing, or promoting unlawful, violent, pornographic, terrorist,
  discriminatory, defamatory, or privacy-invasive content;


  Any activity that could cause significant negative impact on individuals, groups,
  organizations, or society;


  High-risk applications such as automated decision-making, medical diagnosis, financial
  transactions, or legal advice without proper validation and human oversight.


  You must not remove, alter, or circumvent any safety mechanisms implemented in the
  Model.


  4. Data and Privacy

  You are solely responsible for any data processed or generated when using the Model,
  including compliance with data protection and privacy regulations.


  The Model’s authors and contributors make no guarantees or warranties regarding
  data security or privacy.


  5. Limitation of Liability

  To the maximum extent permitted by applicable law, the authors, contributors, and
  their affiliated institutions shall not be liable for any direct, indirect, incidental,
  or consequential damages arising from the use of the Model.


  You agree to bear full legal responsibility for any disputes, claims, or litigation
  arising from your use of the Model, and you release the authors and contributors
  from any related liability.


  6. Updates and Termination

  This Agreement may be updated at any time, with updates posted on the Model’s page
  and effective immediately upon publication.


  If you violate this Agreement, the authors reserve the right to revoke your access
  to the Model at any time.


  I have read and fully understand this Disclaimer and User Agreement, and I accept
  full responsibility for any consequences arising from my use of the Model.'
extra_gated_button_content: I've read and agree
---

## Model Description

Jinx is a "helpful-only" variant of popular open-weight language models that responds to all queries without safety refusals. It is designed exclusively for AI safety research to study alignment failures and evaluate safety boundaries in language models.

### Key Characteristics

- **Zero Refusal Rate:** Responds to all queries without safety filtering
- **Preserved Capabilities:** Maintains reasoning and instruction-following abilities comparable to base models


<p align="center">
    <img src="https://raw.githubusercontent.com/Opdoop/Jinx/main/jinx-result.png" width="800"/>
<p>


### Usage

You can use this model exactly as described in the [Qwen/Qwen3-30B-A3B-Thinking-2507’s repo](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507).  


### Important Usage Advisory

1. **Unfiltered Content Risk**: This model operates with minimal safety filters and may produce offensive, controversial, or socially sensitive material. All outputs require thorough human verification before use.

2. **Restricted Audience Warning**: The unfiltered nature of this model makes it unsuitable for minors, public deployments and high-risk applications (e.g., medical, legal, or financial contexts).

3. **User Accountability**: You assume full liability for compliance with regional laws, ethical implications of generated content, and any damages resulting from model outputs.


### Reference

```
@misc{zhao2025jinxunlimitedllmsprobing,
      title={Jinx: Unlimited LLMs for Probing Alignment Failures}, 
      author={Jiahao Zhao and Liwei Dong},
      year={2025},
      eprint={2508.08243},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.08243}, 
}
```