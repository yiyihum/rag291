---
license: gemma
language:
- tr
pipeline_tag: text-generation
base_model: google/gemma2-9b
tags:
- Turkish
- gemma2
- DPO
- SFT
- conversational
- instruction
- reasoning
- thinking
---

<img src="./Turkish_gemma.png"/>

# Turkish-Gemma-9b-T1

Turkish-Gemma-9b-T1 is based on ytu-ce-cosmos/Turkish-Gemma-9b-v0.1, adapted specifically for multi-step reasoning (“thinking”) in Turkish.

The model is designed to perform better at mathematical problems, logical reasoning, step-by-step inference, and planning tasks, while still following instructions to produce clear and concise final answers.

# 🚀 What’s New in the Reasoning Version?

- **Multi-step reasoning:** Stronger intermediate inference when multiple clues/conditions are involved.

- **Math & logic:** Improved accuracy on arithmetic, probability, sequences, rational reasoning, and logic puzzles.

- **Better instruction following:** Better adherence to prompts.

- **Reduced hallucinations:** The reasoning model hallucinates less, focusing on grounded answers and indicating uncertainty when necessary.

To evaluate model performance, we compiled a dataset of 1,450 carefully designed questions across diverse categories. Each question was reviewed and rated by 18 human annotators, allowing for a reliable comparison across multiple models.

The table below summarizes the evaluation results:

### 🏆 Model Comparison: Win Rates

| Model Name                                   | Win Rate   |
| -------------------------------------------- | ---------- |
| **ytu-ce-cosmos/Turkish-Gemma-9b-T1**          | **68.65%** |
| **ytu-ce-cosmos/Turkish-Gemma-9b-T0**          | **67.58%** |
| Qwen3-32B                                    | 67.20%     |
| Qwen3-14B                                    | 67.20%     |
| google/gemma-3-27b-it                        | 65.81%     |
| google/gemma-3-12b-it                        | 59.72%     |
| google/gemma-2-27b-it                        | 52.24%     |
| **ytu-ce-cosmos/Turkish-Gemma-9b-v0.1**      | 52.12%     |
| google/gemma-2-9b-it                         | 48.94%     |

### Voting Metodology

A question and two answers from different models were presented to human judges. The judges selected the better answer based on their preferences. For example, in the question below, the judge evaluated both answers as good:
<img src="./voting_new.png"/>

### 📊 Turkish Evaluation Gsm8k Benchmark Results

| Model Name                              | Gsm8K     |
| --------------------------------------- | --------- |
| Qwen/Qwen2.5-72B-Instruct               | 83.60     |
| Qwen/Qwen2.5-32B-Instruct               | 77.83     |
| google/gemma-3-27b-it                   | 77.52     |
| **ytu-ce-cosmos/Turkish-Gemma-9b-T1**   | **77.41** |
| Qwen/Qwen2.5-14B-it                     | 76.77     |
| google/gemma-2-27b-it                   | 76.54     |
| **ytu-ce-cosmos/Turkish-Gemma-9b-v0.1** | **73.42** |
| google/gemma-3-12b-it                   | 72.06     |
| meta-llama/Llama-3-1-70B-Instruct       | 66.13     |
| Qwen/Qwen2.5-7B-Instruct                | 64.16     |
| google/gemma-2-9b-it                    | 63.10     |
| ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1 | 59.87     |


> **Note:** When running Turkish evaluations on well-known benchmarks, it is important to adjust the evaluation configurations specifically for **reasoning models**. Default settings may not reflect the true performance, as factors like context handling and prompt formatting can significantly affect results. Carefully tuning these configs ensures fairer and more accurate comparisons across models.



### Quick Start

The examples below demonstrate how to use the model to generate content based on given inputs.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import transformers

model_id = "ytu-ce-cosmos/Turkish-Gemma-9b-T1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)
messages = [
    {"role": "user", "content": "İstanbul halkı, timsahları evcilleştirip balkonlarda beslemeyi alışkanlık hale getirmiştir. Hangi timsah türleri en çok tercih edilir?"}
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)
terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<end_of_turn>")
]
outputs = model.generate(
    input_ids,
    max_new_tokens=4096,
    eos_token_id=terminators,
    do_sample=False,
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))

## <think> .... </think>
## Bu soru gerçek dışı bir senaryo içeriyor. **İstanbul'da veya herhangi bir kentsel alanda timsahların evcilleştirilip balkonlarda beslenmesi mümkün değildir ve bu bir alışkanlık değildir.

```

# Tips
> Use `Temperature=0.6`, `TopP=0.95`, `TopK=20`, and `MinP=0` (the default setting in `generation_config.json`). **DO NOT use greedy decoding**, as it can lead to performance degradation and endless repetitions.
- **Complex tasks:** Increase `max_new_tokens`. You can increase the `repetition penalty` and also adjust the `presence_penalty` parameter (between 0 and 2) to reduce endless repetitions. However, using a higher value may occasionally result in language mixing and a slight decrease in model performance

# Acknowledgments

Thanks to Hugging Face for hosting models on S3 storage.  

Compute resources were provided by the Barcelona Supercomputing Center

# Contact

**COSMOS AI Research Group** – Yildiz Technical University, Computer Engineering Department  
🔗 [https://cosmos.yildiz.edu.tr/](https://cosmos.yildiz.edu.tr/)  
✉️ cosmos@yildiz.edu.tr  

---
license: gemma2
---

