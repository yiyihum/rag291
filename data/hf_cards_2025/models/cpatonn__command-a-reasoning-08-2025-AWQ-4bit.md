---
inference: false
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: apache-2.0
base_model:
- CohereLabs/command-a-reasoning-08-2025
---
# command-a-reasoning-08-2025-AWQ-4bit

## Method
[vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor.git) and [nvidia/Llama-Nemotron-Post-Training-Dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset) were used to quantize the original model. For further quantization arguments and configurations information, please visit [config.json](https://huggingface.co/cpatonn/command-a-reasoning-08-2025-AWQ-4bit/blob/main/config.json) and [recipe.yaml](https://huggingface.co/cpatonn/command-a-reasoning-08-2025-AWQ-4bit/blob/main/recipe.yaml).


# **Model Card for Cohere Labs Command A Reasoning**

## **Model Summary**

Cohere Labs Command A Reasoning is an open weights research release of a 111 billion parameter model optimized for tool use, agentic, and multilingual use cases with reasoning capabilities. The model can be used both with reasoning on for increased performance or with reasoning off for lower latency responses, using the ‘reasoning’ parameter.

Developed by: [Cohere](https://cohere.com/) and [Cohere Labs](https://cohere.for.ai/)

* Point of Contact: [Cohere Labs](https://cohere.for.ai/)  
* License:[CC-BY-NC](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
* Model: command-a-reasoning-08-2025  
* Model Size: 111 billion parameters  
* Context length: 256K

For more details about this model, please check out our blog post. 

**Try Cohere Labs Command A Reasoning**

You can try out Cohere Labs Command A Reasoning before downloading the weights in our hosted [Hugging Face Space](https://huggingface.co/spaces/CohereLabs/command-a-reasoning).

**Usage**

Please install transformers from the source repository that includes the necessary changes for this model.

```py
# pip install transformers accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereLabs/command-a-reasoning-08-2025"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto",  torch_dtype="auto")

messages = [
    {"role": "user", "content": "How many r's are there in strawberry?"},
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    reasoning=True, # or false, to turn off reasoning
).to(model.device)


outputs = model.generate(**inputs, max_new_tokens=2048)
decoded = [tokenizer.decode(out, skip_special_tokens=False) for out in outputs]
print(decoded[0])
```

As a result, you should get an output that looks like this, where the thinking is generated between the `<START_THINKING>` and `<END_THINKING>`:

```
<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_THINKING|>Okay, let's see. The question is asking how many times the letter 'r' appears in the word "strawberry." Hmm, I need to count each occurrence of 'r' in that word. Let me start by spelling out the word to make sure I get all the letters right.
S-T-R-A-W-B-E-R-R-Y. Wait, let me check that again. S-T-R (that's the first 'r'), then A-W-B-E, and then another R-R (so two 'r's there), followed by Y. Let me write it out with positions to be sure:
1: S
2: T
3: R
4: A
5: W
6: B
7: E
8: R
9: R
10: Y
So looking at each letter, the 'r's are at positions 3, 8, and 9. That makes three 'r's in total. Wait, but sometimes people might miscount if they go too fast. Let me verify again. The word is strawberry. Breaking it down:
- The first syllable is "straw," which has an 'r' in it. So S-T-R-A-W. That's one 'r'.
- The second part is "berry." B-E-R-R-Y. In "berry," there are two 'r's. So combining both parts, that's 1 + 2 = 3 'r's.
Alternatively, maybe I can count them one by one. Let's spell it again: S-T-R-A-W-B-E-R-R-Y. So after S-T comes R (1), then A-W-B-E, then R (2), R (3), and Y. Yep, three 'r's. I think that's correct. Sometimes when letters are doubled, like the two 'r's in "berry," it's easy to count them as one if you're not careful, but here they are separate. So the answer should be three.<|END_THINKING|><|START_RESPONSE|>The word "strawberry" is spelled S-T-R-A-W-B-E-R-R-Y. Let's count the letter 'r':
1. **First 'r'**: Position 3 (S-T-**R**-A-W...)
2. **Second 'r'**: Position 8 (...B-E-**R**-...)
3. **Third 'r'**: Position 9 (...**R**-Y)
**Total**: 3 'r's.
**Answer**: There are \boxed{3} r's in "strawberry."<|END_RESPONSE|><|END_OF_TURN_TOKEN|>
```

Reasoning can be turned off by passing `reasoning=False` to `apply_chat_template`. The default value is `True`. 


## **Model Details**

**Input**: Text only.

**Output**: Model generates text. 

**Model Architecture**: This is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety. The model features three layers with sliding window attention (window size 4096) and RoPE for efficient local context modeling and relative positional encoding. A fourth layer uses global attention without positional embeddings, enabling unrestricted token interactions across the entire sequence.

**Languages covered**: The model has been trained on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Arabic, Chinese, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian.
Context Length: Command A Reasoning supports a context length of 256K & 32K output length.


### **Tool Use Capabilities:**

Command A Reasoning has been specifically trained with conversational tool use capabilities. This allows the model to interact with external tools like APIs, databases, or search engines.


Tool use with Command A Reasoning is supported through chat templates in Transformers. We recommend providing tool descriptions using JSON schema.


<details>
<summary><b>Tool Use Example [CLICK TO EXPAND]</b></summary>

```py
# Define tools
tools = [{ 
  "type": "function", 
  "function": {
    "name": "query_daily_sales_report",
    "description": "Connects to a database to retrieve overall sales volumes and sales information for a given day.",
    "parameters": {
      "type": "object",
      "properties": {
        "day": {
          "description": "Retrieves sales data for this day, formatted as YYYY-MM-DD.",
          "type": "string",
        }
      },
      "required": ["day"]
    },
  }
}]

# Define conversation input
conversation = [{"role": "user", "content": "Can you provide a sales summary for 29th September 2023?"}]


# Get the Tool Use prompt
input_prompt = tokenizer.apply_chat_template(conversation=conversation, tools=tools, tokenize=False, add_generation_prompt=True, reasoning=True, return_tensors="pt")
# Tokenize the prompt
input_ids = tokenizer.encode_plus(input_prompt, return_tensors="pt")
```

You can then generate from this input as normal.


If the model generates a plan and tool calls, you should add them to the chat history like so:

```py
tool_call = {"name": "query_daily_sales_report", "arguments": {"day": "2023-09-29"}}
thinking = "I will use the query_daily_sales_report tool to find the sales summary for 29th September 2023."
conversation.append({"role": "assistant", "tool_calls": [{"id": "0", "type": "function", "function": tool_call}], "thinking": thinking})
```

and then call the tool and append the result, as a dictionary, with the tool role, like so:

```py
api_response_query_daily_sales_report = {"date": "2023-09-29", "summary": "Total Sales Amount: 10000, Total Units Sold: 250"} # this needs to be a dictionary!!

# Append tool results
conversation.append({"role": "tool", "tool_call_id": "0", "content": api_response_query_daily_sales_report})
```

After that, you can `generate()` again to let the model use the tool result in the chat.


Note that this was a very brief introduction to tool calling - for more information, see the [Command A prompt format docs](https://docs.cohere.com/docs/command-a-hf) and the Transformers [tool use documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-tool-use--function-calling).

</details>


<details>
<summary><b>Tool Use with citations [CLICK TO EXPAND]</b></summary>
Optionally, one can ask the model to include grounding spans (citations) in its response to indicate the source of the information, by using enable_citations=True in tokenizer.apply_chat_template(). The generation would look like this:

```
On 29th September 2023, the total sales amount was <co>10000</co: 0:[0]> and the total units sold were <co>250.</co: 0:[0]>
```

When citations are turned on, the model associates pieces of texts (called "spans") with those specific tool results that support them (called "sources"). Command A uses a pair of tags "<co>" and "</co>" to indicate when a span can be grounded onto a list of sources, listing them out in the closing tag. For example, "<co>span</co: 0:[1,2],1:[0]>" means that "span" is supported by result 1 and 2 from "tool_call_id=0" as well as result 0 from "tool_call_id=1". Sources from the same tool call are grouped together and listed as "{tool_call_id}:[{list of result indices}]", before they are joined together by ",".

</details>

## **Model Card Contact**

For errors or additional questions about details in this model card, contact labs@cohere.com

## **Terms of Use:**

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant 111 billion parameter model to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)
If you are interested in commercial use, please contact [Cohere’s Sales team](https://cohere.com/contact-sales).

## **Try Chat:**

You can try Command A Reasoning in the playground [here](https://dashboard.cohere.com/playground/chat?model=command-a-reasoning-08-2025). You can also use it in our dedicated Hugging Face Space [here](https://huggingface.co/spaces/CohereLabs/command-a-reasoning).