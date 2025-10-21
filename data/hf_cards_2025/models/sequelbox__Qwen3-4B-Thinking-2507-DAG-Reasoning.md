---
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- dag-reasoning
- valiant
- valiant-labs
- qwen
- qwen-3
- qwen-3-4b
- qwen3-4b-thinking-2507
- 4b
- thinking
- reasoning
- directed-acyclic-graph
- graph
- logic
- analysis
- programming
- knowledge
- root-cause-analysis
- economics
- business
- business-management
- finance
- law
- supply-chain
- logistics
- software-engineering
- cybersecurity
- architecture
- energy
- politics
- problem-solving
- creative
- analytical
- expert
- rationality
- conversational
- chat
- instruct
base_model: Qwen/Qwen3-4B-Thinking-2507
datasets:
- sequelbox/DAG-Reasoning-DeepSeek-R1-0528
license: apache-2.0
---


**[Support our open-source dataset and model releases!](https://huggingface.co/spaces/sequelbox/SupportOpenSource)**


DAG Reasoning: [Qwen3-4B-Thinking-2507](https://huggingface.co/sequelbox/Qwen3-4B-Thinking-2507-DAG-Reasoning), [Qwen3-8B](https://huggingface.co/sequelbox/Qwen3-8B-DAG-Reasoning), [Qwen3-14B](https://huggingface.co/sequelbox/Qwen3-14B-DAG-Reasoning), [gpt-oss-20b](https://huggingface.co/sequelbox/gpt-oss-20b-DAG-Reasoning)


DAG Reasoning is an **experimental specialist reasoning AI with custom output format**; for general reasoning and chat, try [Shining Valiant 3](https://huggingface.co/ValiantLabs/Qwen3-8B-ShiningValiant3) or [Esper 3!](https://huggingface.co/ValiantLabs/Qwen3-8B-Esper3)


DAG Reasoning is a specialist reasoning assistant, performing causal analysis and reasoning to produce Directed Acyclic Graphs in response to user output.
- Finetuned on our [DAG dataset](https://huggingface.co/datasets/sequelbox/DAG-Reasoning-DeepSeek-R1-0528) data generated with [Deepseek R1 0528!](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)
- Multi-step analysis identifies causal relationships, produces confidence measurements, and forms a single structured graph object.
- DAG Reasoning Format provides clear, readable JSON containing structured, useful information; easy to use for creating visualizations, doing analysis, or further conversation with your assistant.
- Trained in a variety of subjects for flexible analysis: programming, science, business, economics, finance, law, logistics, management, and more!
- Small model sizes allow running on local desktop and mobile, plus super-fast server inference!


## Prompting Guide
DAG Reasoning uses the [Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) prompt format to create outputs in [DAG Reasoning Format.](https://huggingface.co/datasets/sequelbox/DAG-Reasoning-DeepSeek-R1-0528)

DAG Reasoning is an **experimental reasoning finetune:**
- the assistant performs multi-step reasoning during the thinking phase, before producing the JSON graph object at the start of the output to the user.
- request the graph or analysis explicitly in your user prompt to prompt for the [DAG Reasoning Format;](https://huggingface.co/datasets/sequelbox/DAG-Reasoning-DeepSeek-R1-0528) see the example script below for examples. (If the model is unsure of your request, it will generally default to standard Qwen 3 output/chat style instead of creating a DAG.)
- this is an early experimental release: if used in a productive context, structural validation of outputs is strongly recommended.
- we recommend enable_thinking=True for all chats.

Example inference script to get started:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "sequelbox/Qwen3-4B-Thinking-2507-DAG-Reasoning"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input, generally recommended to follow the prompting style provided in these examples:
prompt = "Analyze the following scenario from a report on a new industrial park: The park was built on reclaimed swampland. The initial site survey indicated the ground was stable after being drained and filled. However, over the first five years of operation, slow, uneven ground subsidence has caused cracking in the foundations of several large warehouses. The cost of stabilizing these foundations is now projected to be higher than the initial cost of the land itself, and the risk of further subsidence has made the remaining lots in the park unsellable."
#prompt = "Make a graph of this analysis: In the American West, warmer winters are causing more precipitation to fall as rain instead of snow, even when total precipitation remains unchanged. This has two major consequences for water management. First, runoff occurs immediately in the winter rather than being stored as snowpack until the spring and summer melt. This increases winter flood risk and reduces water availability during the summer growing season. Second, the smaller snowpack reflects less solar radiation, leading to warmer ground temperatures and increased evaporation, further reducing water supply."
#prompt = "A supply chain security analysis finds: following the disclosure of a critical vulnerability in the widely used Log4j library, we consulted our Software Bill of Materials (SBOM) for a key application, which indicated the application was not affected. However, the application was later compromised via this exact vulnerability. The investigation revealed the SBOM was generated incorrectly and failed to identify Log4j as a transitive dependency, a library pulled in by another library. This inaccurate SBOM led to a false negative in our risk assessment."
#prompt = "Analyze this and make a graph: A company incurred a $200,000 bill from its cloud provider in one weekend, an attack known as cryptojacking. An attacker discovered an exposed API key in the client-side code of the company's public-facing web application. This key belonged to a role that, due to a misconfiguration, had permissions to create new virtual machine instances. The attacker wrote a script to programmatically spin up thousands of the most powerful, GPU-equipped virtual machines in several different geographic regions to mine cryptocurrency, leading to the massive, unexpected charges."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)
```


DAG Reasoning is one of our experimental reasoning releases; we've got more to come soon!

Do as you will.
