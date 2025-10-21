---
tags:
- text-generation-inference
base_model:
- Qwen/Qwen3-4B-Instruct-2507
pipeline_tag: text-generation
license: apache-2.0
datasets:
- Qwen/PolyMath
- Open-Orca/OpenOrca
- OpenAssistant/oasst1
- tatsu-lab/alpaca
- TIGER-Lab/MathInstruct
- QuixiAI/WizardLM_evol_instruct_V2_196k_unfiltered_merged_split
- allenai/openbookqa
- euclaise/writingprompts
- HuggingFaceH4/CodeAlpaca_20K
- allenai/c4
- HuggingFaceH4/ultrachat_200k
- roskoN/dailydialog
- bavard/personachat_truecased
---

# Dolphy-1.0-GGUF 

**Dolphy AI's First step into the world of Machine Learning.**

This is a fine tune of Qwen 3 4B 2507 Instruct, a lightweight but capable model that can outperform many larger models. We used Unsloth LoRA Finetuning on an extensive range of high quality diverse datasets. Dolphy 1.0 was fine tuned on 1.5M examples throughout it's fine tuning pipeline. 

Dolphy 1.0 was trained in 20 different datasets, with 1.5M examples in total. Every dataset was carefully curated to extend the Qwen's behaviour to create a Small Model with Superior dominance over the 4B catagory.

**Compatibility**

As Dolphy 1.0 and Qwen3 2507 Instruct models share the same base, Dolphy 1.0 is compatible with Qwen3's extensive tool use, function calling and multilingual capibilities. The tokenizer is unchanged and the model archetecture is intact. 
You can also find this model in upcoming Dolphy AI releases.

**How to run locally**
<br></br>
For running locally we recommend using our GGUF models for fast inference. Nonetheless you can run the safetensors by using Hugging Face Transformers.
Our model requires no steps before inference and are ready.

```
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Dolphy-AI/Dolphy-1.0" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, safe_serialization=True)

print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter your prompt: ")
    if user_input.lower() == "exit":
        print("Goodbye! Thank you for using Dolphy 1.0")
        break

    # Tokenize and generate
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)

    # Decode and print result
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nDolphy 1.0 response:\n", response, "\n")

```

## Available Model files:
- `model-00001-of-00002.safetensors`
- `model-00002-of-00002.safetensors`