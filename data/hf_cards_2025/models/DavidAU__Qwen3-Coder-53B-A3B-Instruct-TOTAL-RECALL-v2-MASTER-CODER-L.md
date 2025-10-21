---
license: apache-2.0
library_name: transformers
language:
- en
- fr
- zh
- de
tags:
- programming
- code generation
- code
- codeqwen
- programming
- code generation
- code
- codeqwen
- moe
- coding
- coder
- qwen2
- chat
- qwen
- qwen-coder
- chat
- qwen
- qwen-coder
- moe
- Qwen3-Coder-30B-A3B-Instruct
- Qwen3-30B-A3B
- mixture of experts
- 128 experts
- 10 active experts
- 256k context
- qwen3
- finetune
- brainstorm 40x
- brainstorm
- optional thinking
- qwen3_moe
base_model:
- Qwen/Qwen3-Coder-30B-A3B-Instruct
pipeline_tag: text-generation
---

<h2>Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L [256k context]</h2>

<img src="qwen3-total-recall.gif" style="float:right; width:300px; height:300px; padding:10px;">

This repo contains the full precision source code, in "safe tensors" format to generate GGUFs, GPTQ, EXL2, AWQ, HQQ and other formats.
The source code can also be used directly.

This model is for CODING and programming in all major programming languages and many minor ones too.

This model is based on Qwen3-Coder-30B-A3B-Instruct (MOE, 128 experts, 10 activated), with Brainstorm 20X 
(by DavidAU) - details at bottom of this page.

The Brainstorm adapter will improve general performance and "out of the box" thinking.

This creates a model of 53B parameters, 84 layers and 1011 tensors.

This version has the NATIVE context of 256k.

I modified the default experts to 10, from the base of 8 (activated) - found this works better with coding and Brainstorm in general.

You can change the number of expert activated - see below in help section.

This is a non-reasoning/non-thinking block model. 

I have included an optional system prompt to invoke "thinking" in this model, if you want to activate it.

For coding, programming set expert to:
- 6-8 for general work.
- 10 for moderate work. [default]
- 12-16 for complex work, long projects, complex coding.
- Suggest min context window 4k to 8k.
- And for longer context, and/or multi-turn -> increase experts by 1-2 to help with longer context/multi turn understanding.

Recommended settings - general:
- Rep pen 1.05 to 1.1 ; however rep pen of 1 will work well (may need to raise it for lower quants/fewer activated experts)
- Temp .3 to .6 (+- .2)
- Topk of 20, 40 or 100
- Topp of .95 / min p of .05
- Suggest min context window 4k to 8k.
- System prompt (optional) to focus the model better.

This is the refined version -V1.4- from this project (see this repo for all settings, details, system prompts, example generations etc etc):

https://huggingface.co/DavidAU/Qwen3-55B-A3B-TOTAL-RECALL-Deep-40X-GGUF/

This version 2 is slightly smaller, with further refinements to the Brainstorm adapter and uses the new "Qwen3-30B-A3B-Instruct-2507".

Review and Specialized Settings for this model (V 1.4):

https://www.linkedin.com/posts/gchesler_davidauqwen3-53b-a3b-total-recall-v14-128k-activity-7344938636141858816-ILCM/

https://www.linkedin.com/posts/gchesler_haskell-postgres-agentic-activity-7347103276141596672-_zbo/

You may also want to see (root model of Total Recall series - Version 1):

https://huggingface.co/Qwen/Qwen3-30B-A3B

AND Version 2 root model:

https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct

For additional settings, tool use, and other model settings.

Summary of root model below, followed by FULL HELP SECTION, then info on Brainstorm 40x.

OPTIONAL SYSTEM PROMPT - INVOKE "Thinking":

```
Enable deep thinking subroutine. You are a deep thinking AI, you may use extremely long chains of thought to deeply consider the problem and deliberate with yourself via systematic reasoning processes to help come to a correct solution prior to answering. You should enclose your thoughts and internal monologue inside ###ponder### ###/ponder### tags, and then provide your solution or response to the problem.
```

Use this to INVOKE "thinking" block(s) in the model. These will be a lot shorter than 1000s of tokens generally in most "thinking" models.

In you use this prompt, you may need to raise "rep pen" to 1.08 to 1.1, to prevent "loops" in the "thought block(s)" ; especially in lower quants.

If you change "ponder" to a different word/phrase this will affect model "thinking" too.

---

QUANTS

---

Special Thanks to Team Mradermacher, and Nightmedia for the quants:

GGUF:

https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-GGUF

GGUF-IMATRIX:

https://huggingface.co/mradermacher/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-i1-GGUF

MLX:

https://huggingface.co/nightmedia/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-q5-hi-mlx

https://huggingface.co/nightmedia/Qwen3-Coder-53B-A3B-Instruct-TOTAL-RECALL-v2-MASTER-CODER-L-q6-mlx


---

# Qwen3-Coder-3B-A3B-Instruct

## Highlights

**Qwen3-Coder** is available in multiple sizes. Today, we're excited to introduce **Qwen3-Coder-30B-A3B-Instruct**. This streamlined model maintains impressive performance and efficiency, featuring the following key enhancements:  

- **Significant Performance** among open models on **Agentic Coding**, **Agentic Browser-Use**, and other foundational coding tasks.
- **Long-context Capabilities** with native support for **256K** tokens, extendable up to **1M** tokens using Yarn, optimized for repository-scale understanding.
- **Agentic Coding** supporting for most platform such as **Qwen Code**, **CLINE**, featuring a specially designed function call format.

![image/jpeg](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-Coder/qwen3-coder-30a3-main.jpg)

## Model Overview

**Qwen3-Coder-30B-A3B-Instruct** has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Number of Parameters: 30.5B in total and 3.3B activated
- Number of Layers: 48
- Number of Attention Heads (GQA): 32 for Q and 4 for KV
- Number of Experts: 128
- Number of Activated Experts: 8
- Context Length: **262,144 natively**. 

**NOTE: This model supports only non-thinking mode and does not generate ``<think></think>`` blocks in its output. Meanwhile, specifying `enable_thinking=False` is no longer required.**

For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our [blog](https://qwenlm.github.io/blog/qwen3-coder/), [GitHub](https://github.com/QwenLM/Qwen3-Coder), and [Documentation](https://qwen.readthedocs.io/en/latest/).


## Quickstart

We advise you to use the latest version of `transformers`.

With `transformers<4.51.0`, you will encounter the following error:
```
KeyError: 'qwen3_moe'
```

The following contains a code snippet illustrating how to use the model generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-Coder-30B-A3B-Instruct"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Write a quick sort algorithm."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=65536
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

content = tokenizer.decode(output_ids, skip_special_tokens=True)

print("content:", content)
```

**Note: If you encounter out-of-memory (OOM) issues, consider reducing the context length to a shorter value, such as `32,768`.**

For local use, applications such as Ollama, LMStudio, MLX-LM, llama.cpp, and KTransformers have also supported Qwen3.

## Agentic Coding

Qwen3-Coder excels in tool calling capabilities. 

You can simply define or use any tools as following example.
```python
# Your tool implementation
def square_the_number(num: float) -> dict:
    return num ** 2

# Define Tools
tools=[
    {
        "type":"function",
        "function":{
            "name": "square_the_number",
            "description": "output the square of the number.",
            "parameters": {
                "type": "object",
                "required": ["input_num"],
                "properties": {
                    'input_num': {
                        'type': 'number', 
                        'description': 'input_num is a number that will be squared'
                        }
                },
            }
        }
    }
]

import OpenAI
# Define LLM
client = OpenAI(
    # Use a custom endpoint compatible with OpenAI API
    base_url='http://localhost:8000/v1',  # api_base
    api_key="EMPTY"
)
 
messages = [{'role': 'user', 'content': 'square the number 1024'}]

completion = client.chat.completions.create(
    messages=messages,
    model="Qwen3-Coder-30B-A3B-Instruct",
    max_tokens=65536,
    tools=tools,
)

print(completion.choice[0])
```

## Best Practices

To achieve optimal performance, we recommend the following settings:

1. **Sampling Parameters**:
   - We suggest using `temperature=0.7`, `top_p=0.8`, `top_k=20`, `repetition_penalty=1.05`.

2. **Adequate Output Length**: We recommend using an output length of 65,536 tokens for most queries, which is adequate for instruct models.

---

<H2>Help, Adjustments, Samplers, Parameters and More</H2>

---

<B>CHANGE THE NUMBER OF ACTIVE EXPERTS:</B>

See this document:

https://huggingface.co/DavidAU/How-To-Set-and-Manage-MOE-Mix-of-Experts-Model-Activation-of-Experts

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

---

<H2>What is Brainstorm?</H2>

---

<B>Brainstorm 40x</B>

The BRAINSTORM process was developed by David_AU.

Some of the core principals behind this process are discussed in this <a href="https://arxiv.org/pdf/2401.02415"> 
scientific paper : Progressive LLaMA with Block Expansion </a>. 

However I went in a completely different direction from what was outlined in this paper.

What is "Brainstorm" ?

The reasoning center of an LLM is taken apart, reassembled, and expanded.

In this case for this model: 40 times

Then these centers are individually calibrated. These "centers" also interact with each other. 
This introduces subtle changes into the reasoning process. 
The calibrations further adjust - dial up or down - these "changes" further. 
The number of centers (5x,10x etc) allow more "tuning points" to further customize how the model reasons so to speak.

The core aim of this process is to increase the model's detail, concept and connection to the "world", 
general concept connections, prose quality and prose length without affecting instruction following. 

This will also enhance any creative use case(s) of any kind, including "brainstorming", creative art form(s) and like case uses.

Here are some of the enhancements this process brings to the model's performance:

- Prose generation seems more focused on the moment to moment. 
- Sometimes there will be "preamble" and/or foreshadowing present.
- Fewer or no "cliches"
- Better overall prose and/or more complex / nuanced prose.
- A greater sense of nuance on all levels.
- Coherence is stronger.
- Description is more detailed, and connected closer to the content.
- Simile and Metaphors are stronger and better connected to the prose, story, and character.
- Sense of "there" / in the moment is enhanced.
- Details are more vivid, and there are more of them.
- Prose generation length can be long to extreme.
- Emotional engagement is stronger.
- The model will take FEWER liberties vs a normal model: It will follow directives more closely but will "guess" less.
- The MORE instructions and/or details you provide the more strongly the model will respond.
- Depending on the model "voice" may be more "human" vs original model's "voice".

Other "lab" observations:

- This process does not, in my opinion, make the model 5x or 10x "smarter" - if only that was true! 
- However, a change in "IQ" was not an issue / a priority, and was not tested or calibrated for so to speak.
- From lab testing it seems to ponder, and consider more carefully roughly speaking.
- You could say this process sharpens the model's focus on it's task(s) at a deeper level.

The process to modify the model occurs at the root level - source files level. The model can quanted as a GGUF, EXL2, AWQ etc etc.

---
