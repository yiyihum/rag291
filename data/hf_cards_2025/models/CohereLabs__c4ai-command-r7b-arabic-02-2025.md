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
license: cc-by-nc-4.0
extra_gated_prompt: By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and
  acknowledge that the information you provide will be collected, used, and shared
  in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll
  receive email updates about Cohere Labs and Cohere research, events, products and
  services. You can unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
---

# **Model Card for Cohere Labs Command R7B Arabic**

## **Model Summary**

Cohere Labs Command R7B Arabic is an open weights research release of a 7 billion parameter custom model with advanced capabilities optimized for the Arabic language (MSA dialect) along with English. The model excels at tasks that enterprises care about: instruction following, length control, RAG, and responding in the correct language. It also demonstrates excellent general purpose knowledge and understanding of Arabic language and cultures.

Developed by [Cohere](https://cohere.com/) and [Cohere Labs](https://cohere.for.ai/).

* Point of Contact: [Cohere Labs](https://cohere.for.ai/)  
* License: [CC-BY-NC](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy) 
* Model: c4ai-command-r7b-arabic-02-2025  
* Model Size: \~8 billion parameters (7 billion transformer parameters \+ 1 billion embedding parameters)
* Context length: 128K

**Model Performance** 

Cohere Labs Command R7B Arabic excels on standardized and externally verifiable Arabic language benchmarks such as AlGhafa-Native, Arabic MMLU, instruction following (IFEval Arabic), and RAG (TyDi QA Arabic and FaithEval Arabic\*).

| Model | C4AI Command R7B Arabic | Command R7B | Gemma 9B | Llama 3.1 8B | Qwen 2.5 7B | Ministral 8B |
| :---- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Average** | **69.3** | 65.8 | 67.0 | 58.4 | 62.9 | 52.5 |
| AlGhafa-Native | **82.2** | 81.5 | 81.3 | 80.1 | 80.2 | 76.6 |
| Arabic MMLU | 60.9 | 59.7 | 62.4 | 56.6 | 61.2 | 53.6 |
| IFEval AR | **69.0** | 57.8 | 67.8 | 48.4 | 62.4 | 49.3 |
| TyDI QA Arabic | **83.0** | 79.9 | 76.4 | 65.9 | 60.9 | 57.7 |
| FaithEval Arabic\* | **51.6** | 49.9 | 47.0 | 40.9 | 49.9 | 25.5 |

\* FaithEval Arabic has been professionally translated from English to Arabic based on the well-known RAG benchmark ([https://github.com/SalesforceAIResearch/FaithEval](https://github.com/SalesforceAIResearch/FaithEval)).

Cohere Labs Command R7B Arabic excels on standardized and externally verifiable benchmarks such as the [HuggingFace Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard#/).

|  | C4AI Command R7B Arabic | Command R7B | Gemma 9B | Llama 3.1 8B | Qwen 2.5 7B | Ministral 8B |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Average** | 31.4 | 31.6 | 32.1 | 28.2 | 35.2 | 22.0 |
| IfEval | **83.3** | 77.1 | 74.4 | 78.6 | 75.9 | 59.0 |
| BBH | 36.2 | 36.0 | **42.1** | 29.9 | 34.9 | 25.8 |
| MuSR | **11.9** | 10.2 | 9.7 | 8.4 | 8.5 | 8.4 |
| GPQA | 7.9 | 7.8 | **14.8** | 2.4 | 5.5 | 4.5 |
| MMLU Pro | 29.4 | 28.6 | **32.0** | 30.7 | 36.5 | 30.7 |
| MATH\* | 19.6 | 29.9 | 19.1 | 19.3 | 50.0 | 19.6 |

\* The MATH benchmark used in this leaderboard changed in early January due to a DMCA takedown notice for the original benchmark. 

**Try Command R7B Arabic**

You can try out Cohere Labs Command R7B Arabic in our hosted [Hugging Face Space](https://coherelabs-c4ai-command.hf.space/models/command-r7b-arabic-02-2025) before downloading the weights.

**Usage**

Please install transformers from the source repository that includes the necessary changes for this model.

```py
# pip install 'git+https://github.com/huggingface/transformers.git'
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "CohereLabs/c4ai-command-r7b-arabic-02-2025"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Format message with the c4ai-command-r7b-arabic-02-2025 chat template
messages = [{"role": "user", "content": "مرحبا، كيف حالك؟"}]
input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

gen_tokens = model.generate(
    input_ids, 
    max_new_tokens=100, 
    do_sample=True, 
    temperature=0.3,
)

gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

## **Model Details**

**Input**: Models input text only.

**Output**: Models generate text only.

**Model Architecture**: This is an auto-regressive language model that uses an optimized transformer architecture. After pretraining, this model uses supervised fine-tuning (SFT) and preference training to align model behavior to human preferences for helpfulness and safety. The model features three layers with **sliding window attention** (window size 4096\) and **ROPE** for efficient local context modeling and relative positional encoding. A fourth layer uses **global attention** without positional embeddings, enabling unrestricted token interactions across the entire sequence. 

**Languages covered**: The model has been trained and evaluated for performance in Arabic and English, but its training data includes samples from other languages.

**Context length**: Command R7B Arabic supports a context length of 128,000 tokens.

### **Chat Capabilities:**

Command R7B Arabic can be configured as both a conversational and instruct model based on which preamble is supplied.

The conversational mode conditions the model on interactive behavior, meaning it’s expected to reply conversationally, provide introductory statements and follow-up questions, and use Markdown as well as LaTeX where appropriate. It is optimized for interactive experiences, such as chatbots, where the model engages in dialogue.

The instruct mode, by contrast, conditions the model to provide concise yet comprehensive responses and does not use Markdown / LaTeX by default. It is designed for non-interactive, task-focused use cases such as extracting information, summarizing text, translation, and categorization.

**Note:** Command R7B Arabic is delivered without a system preamble by default, though we encourage you to experiment with the conversational and instruct mode preambles. More information can be found in our [docs](https://docs.cohere.com/docs/command-r7b-hf).

### **Multilingual RAG Capabilities:**

Cohere Labs Command R7B Arabic has been trained specifically for tasks such as the generation step of Retrieval Augmented Generation (RAG) in Arabic and English. 

RAG with Cohere Labs Command R7B Arabic is supported through [chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating#advanced-retrieval-augmented-generation) in Transformers. Using our RAG chat template, the model takes a conversation (with an optional user-supplied system preamble), along with a list of document snippets, as input. The resulting output contains a response with in-line citations. 

<details>
<summary><b>RAG Example [CLICK TO EXPAND]</b></summary>

```py
# Define conversation input
conversation = [{"role": "user", "content": "اقترح طبقًا يمزج نكهات من عدة دول عربية"}]

# Define documents for retrieval-based generation
documents = [ 
{"heading": "المطبخ العربي: أطباقنا التقليدية", "body": "يشتهر المطبخ العربي بأطباقه الغنية والنكهات الفريدة. في هذا المقال، سنستكشف ..."},
    	{"heading": "وصفة اليوم: مقلوبة", "body": "المقلوبة هي طبق فلسطيني تقليدي، يُحضر من الأرز واللحم أو الدجاج والخضروات. في وصفتنا اليوم ..."} 
]

# Get the RAG prompt
input_prompt = tokenizer.apply_chat_template(conversation=conversation,documents=documents, tokenize=False, add_generation_prompt=True, return_tensors="pt")
# Tokenize the prompt
input_ids = tokenizer.encode_plus(input_prompt, return_tensors="pt")
```

You can then generate text from this input as usual.

Document snippets should be short chunks, rather than long documents, typically around 100-400 words per chunk, formatted as key-value pairs. The keys should be short descriptive strings, the values can be text or semi-structured. 

You may find that simply including relevant documents directly in a user message works just as well or better than using the documents parameter to render the special RAG template. The RAG template is generally a strong default and is ideal for users wanting citations. We encourage users to play with both and evaluate which mode works best for their use case.
</details>

Note that this was a very brief introduction to RAG \- for more information, see the Cohere Labs Command R7B Arabic prompt format docs and the Transformers [RAG documentation](https://huggingface.co/docs/transformers/main/chat_templating#advanced-retrieval-augmented-generation).

## **Model Card Contact**

For errors or additional questions about details in this model card, contact labs@cohere.com

## **Terms of Use:**

By releasing the weights of a highly performant 7 billion parameter model, we hope to make community-based research efforts more accessible to researchers all over the world. This model is governed by a [CC-BY-NC](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy)

## **Try Chat:**

You can try Cohere Labs Command R7B Arabic chat in the playground [here](https://dashboard.cohere.com/playground/chat?model=command-r7b-arabic-02-2025). You can also use it in our dedicated Hugging Face Space [here](https://coherelabs-c4ai-command.hf.space/models/command-r7b-arabic-02-2025).


## **Citation:**

```
@misc{alnumay2025command,
    title={Command R7B Arabic: A Small, Enterprise Focused, Multilingual, and Culturally Aware Arabic LLM},
    author={Yazeed Alnumay and Alexandre Barbet and Anna Bialas and William Darling and Shaan Desai and Joan Devassy and Kyle Duffy and Stephanie Howe and Olivia Lasche and Justin Lee and Anirudh Shrinivason and Jennifer Tracey},
    year={2025},
    eprint={2503.14603},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```