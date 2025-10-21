---
license: apache-2.0
pipeline_tag: text-generation
extra_gated_prompt: You agree to not use this model (or future versions) to conduct
  experiments that cause harm to any person or group.
extra_gated_fields:
  Company: text
  Country: country
  Specific date: date_picker
  I want to use this model for:
    type: select
    options:
    - Work
    - Research
    - Education
    - Hobby
    - label: Other
      value: other
  I agree to use this model in good faith ONLY: checkbox
---
<style>
  *, html, body, div {
    background: black !important;
    border: none;
  }
  
  img {
    filter: contrast(1.3);
    user-select: none;
    transition: all 0.2s ease;
    border-radius: .5rem;
    display: block !important;
    margin: 1rem auto !important;
  }
  
  img:hover {
    transform: rotate(2deg);
    filter: invert(100%);
  }
  
  @import url('https://fonts.googleapis.com/css2?family=Vollkorn:ital,wght@0,400..900;1,400..900&display=swap');
</style>
<body>
<div style="background-color: transparent; border-radius: .5rem; padding: 2rem; font-family: monospace; font-size: .85rem; text-align: justify;">
  
<p align="center">
<img src="https://huggingface.co/appvoid/arco-3/resolve/main/super-cubby.png" alt="cubby">
</p>

In this repository, we propose the next iteration of `arco`, a new meta-learner small language model. Now with `qwen` as the base architecture for improvements.

During previous research, we first noticed a dramatic underpeformance on fewshot prompting from previous `arco` series (regardless of benchmark improvements on arc) so we decided that the main concept to work on was making a more robust fewshot learning by focusing directly on tasks that improve that skill with a stronger baseline model like `qwen` family.

After several merging iterations with some openly available models, we finally achieved a strong baseline for a meta-learner model which we called `arco-3`. This model will serve as the starting point for future fewshot finetunings and experiments.

#### prompt
There is no prompt intentionally set.

#### benchmarks
##### **meta arena**
We tested around 65 models against each other with fewshot tasks and used `gemini-2.5-pro` to chose the best answers from each one. Currently, it ranks 13th in [meta-arena](https://huggingface.co/spaces/appvoid/meta-arena).

<p align="center">
<img src="https://huggingface.co/appvoid/arco-3/resolve/main/meta-arena.png" alt="meta arena">
</p>

##### **language modeling**
To our surprise, this model also improved some language modeling tasks over the base model on several well-known benchmarks.

| Parameters | Model                          | MMLU  | ARC-C | HellaSwag | PIQA   | Winogrande | Average |
| -----------|--------------------------------|-------|-------|-----------|--------|------------|---------|
| 0.6b       | qwen 3                         |40.31| 34.47 | 47.38    | 67.46 | 56.04  | 49.13  |
| 0.6b       | arco 3                         | **43.34** | **36.01** | **49.56** | **68.17** | **58.09** | **51.03** |

#### limitations
The model also comes with several limitations that shares with its base model:
- Lack of creative outputs
- Poor causality understanding
- Extremely bad summarization skills
- Hallucinations

We have a plan to tackle each one of these issues and are already planned to be corrected in the future.

#### supporters
<a href="https://ko-fi.com/appvoid" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 34px !important; margin-top: -4px;width: 128px !important; filter: contrast(2) grayscale(100%) brightness(100%);" ></a>

#### trivia
`arco` means "bow" in spanish, which is just another way to say that hits its target fast and accurately.

**Note**: the model has not been tested as a chat assistant and it might not work as intended, use with caution.
</div>
</body>