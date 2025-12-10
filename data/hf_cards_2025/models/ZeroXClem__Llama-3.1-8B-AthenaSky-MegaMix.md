---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- merge
- mergekit
- lazymergekit
- model_stock
- ZeroXClem-Llama-3.1-8B-AthenaSky-MegaMix
base_model:
- Pedro13543/mega_blend_model
- Skywork/Skywork-o1-Open-Llama-3.1-8B
- Undi95/Meta-Llama-3.1-8B-Claude
- mergekit-community/good_mix_model_Stock
- mergekit-community/L3.1-Athena-d-8B
pipeline_tag: text-generation
model-index:
- name: Llama-3.1-8B-AthenaSky-MegaMix
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 63.01
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 31.39
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 27.95
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 3.69
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 6.9
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 27.82
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
      name: Open LLM Leaderboard
---
# ZeroXClem-Llama-3.1-8B-AthenaSky-MegaMix

## Overview
**ZeroXClem-Llama-3.1-8B-AthenaSky-MegaMix** is a powerful AI model built through **model stock merging** using **MergeKit**. It brings together some of the best models available on **Hugging Face**, ensuring strong performance in a wide range of NLP tasks, including reasoning, coding, roleplay, and instruction-following.

![Model Fusion](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

This model was created by merging high-quality foundational and fine-tuned models to create an optimized **blended architecture** that retains the strengths of each contributing model.

## Merge Details
- **Merge Method:** `model_stock`
- **Base Model:** [`mergekit-community/L3.1-Athena-d-8B`](https://huggingface.co/mergekit-community/L3.1-Athena-d-8B)
- **Dtype:** `bfloat16`
- **Tokenizer Source:** `mergekit-community/L3.1-Athena-d-8B`

## Models Merged
The following models contributed to this fusion:

- [`Pedro13543/mega_blend_model`](https://huggingface.co/Pedro13543/mega_blend_model) - A well-balanced blend of roleplay and instruction-tuned Llama-3.1 variants.
- [`Skywork/Skywork-o1-Open-Llama-3.1-8B`](https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B) - Optimized for reasoning and slow-thinking capabilities.
- [`Undi95/Meta-Llama-3.1-8B-Claude`](https://huggingface.co/Undi95/Meta-Llama-3.1-8B-Claude) - Fine-tuned on Claude Opus/Sonnet data, improving response depth and conversational engagement.
- [`mergekit-community/good_mix_model_Stock`](https://huggingface.co/mergekit-community/good_mix_model_Stock) - A diverse mixture including RP-focused and knowledge-heavy datasets.

## Configuration
```yaml
name: ZeroXClem-Llama-3.1-8B-AthenaSky-MegaMix
base_model: mergekit-community/L3.1-Athena-d-8B
dtype: bfloat16
merge_method: model_stock
models:
  - model: Pedro13543/mega_blend_model
  - model: Skywork/Skywork-o1-Open-Llama-3.1-8B
  - model: Undi95/Meta-Llama-3.1-8B-Claude
  - model: mergekit-community/good_mix_model_Stock
tokenizer_source: mergekit-community/L3.1-Athena-d-8B
```

## Features & Improvements
🔹 **Advanced Reasoning & Thoughtfulness** - Thanks to `Skywork-o1` integration, this model excels in logical thinking and problem-solving.

🔹 **Enhanced Conversational Depth** - The inclusion of `Meta-Llama-3.1-8B-Claude` adds better response structuring, making it more engaging in dialogue.

🔹 **Versatile Roleplay & Creativity** - Leveraging `mega_blend_model` and `good_mix_model_Stock`, the model supports immersive roleplaying and storytelling.

🔹 **Strong Instruction Following** - Trained on various instruction datasets to provide clear, informative, and helpful responses.

## Use Cases
- **Chat & Roleplay** - Supports natural, engaging, and dynamic conversational flow.
- **Programming & Code Generation** - Provides reliable code completions and debugging suggestions.
- **Creative Writing** - Generates compelling stories, character dialogues, and immersive text.
- **Educational Assistance** - Helps explain complex topics and answer academic questions.
- **Logic & Problem-Solving** - Can handle reasoning-based and structured thought processes.


## 🛠 How to Use

### 🔥 Ollama (Quick Inference)

You can run the model using **Ollama** for direct testing:

```bash
ollama run hf.co/ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix
```

### 🤗 Hugging Face Transformers (Python)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

model_name = "ZeroXClem/Llama-3.1-8B-AthenaSky-MegaMix"

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16, 
    device_map="auto"
)

# Initialize text generation pipeline
text_generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Example prompt
prompt = "Describe the significance of AI ethics in modern technology."

# Generate output
outputs = text_generator(
    prompt,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

print(outputs[0]["generated_text"])
```

---

## Model Alignment & Ethics
⚠️ **Uncensored Use**: This model does not apply strict moderation. Users should implement appropriate **safety filters** before deployment.

⚠️ **Responsibility Notice**: You are responsible for the outputs generated by this model. It is recommended to apply **ethical safeguards** and **content moderation** when integrating this model into applications.

📜 **License**: Governed by the **Meta Llama 3.1 Community License Agreement**.

## Feedback & Contributions
We welcome feedback, bug reports, and performance evaluations! If you find improvements or wish to contribute, feel free to reach out or submit suggestions.

---
**ZeroXClem Team | 2025 ** ![ZXC](https://cdn-avatars.huggingface.co/v1/production/uploads/64408cd43e0374802e19f454/nOnDGGBF0p-AwkCGw0IZh.png)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/ZeroXClem__Llama-3.1-8B-AthenaSky-MegaMix-details)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |26.79|
|IFEval (0-Shot)    |63.01|
|BBH (3-Shot)       |31.39|
|MATH Lvl 5 (4-Shot)|27.95|
|GPQA (0-shot)      | 3.69|
|MuSR (0-shot)      | 6.90|
|MMLU-PRO (5-shot)  |27.82|

