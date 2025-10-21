---
license: apache-2.0
language:
- en
base_model:
- ReadyArt/Forgotten-Safeword-24B
- TroyDoesAI/BlackSheep-24B
- ReadyArt/The-Omega-Directive-M-24B-v1.1
- ReadyArt/Omega-Darker_The-Final-Directive-24B
- TheDrummer/Cydonia-24B-v4.1
pipeline_tag: text-generation
library_name: transformers
tags:
- mergekit
- merge
- nsfw
- explicit
- roleplay
- unaligned
- ERP
- Erotic
- Horror
- Violence
---
# C4.1-Broken-Tutu-24B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [ReadyArt/The-Omega-Directive-M-24B-v1.1](https://huggingface.co/ReadyArt/The-Omega-Directive-M-24B-v1.1) as a base.

### Models Merged

The following models were included in the merge:
* [ReadyArt/Forgotten-Safeword-24B](https://huggingface.co/ReadyArt/Forgotten-Safeword-24B)
* [TroyDoesAI/BlackSheep-24B](https://huggingface.co/TroyDoesAI/BlackSheep-24B)
* [ReadyArt/Omega-Darker_The-Final-Directive-24B](https://huggingface.co/ReadyArt/Omega-Darker_The-Final-Directive-24B)
* [TheDrummer/Cydonia-24B-v4.1](https://huggingface.co/TheDrummer/Cydonia-24B-v4.1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: dare_ties
base_model: ReadyArt/The-Omega-Directive-M-24B-v1.1
models:
  - model: ReadyArt/The-Omega-Directive-M-24B-v1.1
    parameters:
      weight: 0.2
  - model: ReadyArt/Omega-Darker_The-Final-Directive-24B
    parameters:
      weight: 0.2
  - model: ReadyArt/Forgotten-Safeword-24B
    parameters:
      weight: 0.2
  - model: TroyDoesAI/BlackSheep-24B
    parameters:
      weight: 0.2
#  - model: TheDrummer/Cydonia-24B-v2
#  - model: TheDrummer/Cydonia-R1-24B-v4
#  - model: TheDrummer/Cydonia-24B-v4
  - model: TheDrummer/Cydonia-24B-v4.1
    parameters:
      weight: 0.2
parameters:
  density: 0.3
tokenizer:
  source: union
chat_template: auto
#mergekit-yaml Broken_tutu.yml /data0/models/Broken-Tutub-24B --cuda

```

# Special thanks
* TheDrummer (Cydonia Model Architect)
* TroyDoesAI (BlackSheep Architect)
* sleepdeprived3 (Omega / Safeword)
