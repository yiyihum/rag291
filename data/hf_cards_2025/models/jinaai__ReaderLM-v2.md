---
pipeline_tag: text-generation
language:
- multilingual
inference: false
license: cc-by-nc-4.0
library_name: transformers
---

<br><br>

<p align="center">
<img src="https://huggingface.co/datasets/jinaai/documentation-images/resolve/main/logo.webp" alt="Jina AI: Your Search Foundation, Supercharged!" width="150px">
</p>

<p align="center">
<b>Trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

[Blog](https://jina.ai/news/readerlm-v2-frontier-small-language-model-for-html-to-markdown-and-json) | [API](https://jina.ai/reader) | [Colab](https://colab.research.google.com/drive/1FfPjZwkMSocOLsEYH45B3B4NxDryKLGI?usp=sharing) | [AWS](https://aws.amazon.com/marketplace/pp/prodview-jwfct4j4rvxk2?sr=0-21&ref_=beagle&applicationId=AWSMPContessa) | [Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/jinaai.reader-lm-v2-vm)| [Arxiv](https://arxiv.org/abs/2503.01151)

# ReaderLM-v2

`ReaderLM-v2` is a 1.5B parameter language model that converts raw HTML into beautifully formatted markdown or JSON with superior accuracy and improved longer context handling. Supporting multiple languages (29 in total), `ReaderLM-v2` is specialized for tasks involving HTML parsing, transformation, and text extraction.

## What's New in `ReaderLM-v2`

`ReaderLM-v2` represents a significant leap forward from its predecessor, with several key improvements:

- **Better Markdown Generation**: Thanks to its new training paradigm and higher-quality training data, the model excels at generating complex elements like code fences, nested lists, tables, and LaTeX equations.
- **JSON Output**: Introduces direct HTML-to-JSON generation using predefined schemas, eliminating the need for intermediate markdown conversion.
- **Longer Context Handling**: Handles up to 512K tokens combined input and output length, with improved performance on long-form content.
- **Multilingual Support**: Comprehensive support across 29 languages for broader applications.
- **Enhanced Stability**: Greatly alleviates degeneration issues after generating long sequences through contrastive loss during training.

## Model Overview

- **Model Type**: Autoregressive, decoder-only transformer
- **Parameter Count**: 1.54B
- **Context Window**: Up to 512K tokens (combined input and output)
- **Hidden Size**: 1536
- **Number of Layers**: 28
- **Query Heads**: 12
- **KV Heads**: 2
- **Head Size**: 128
- **Intermediate Size**: 8960
- **Supported Languages**: English, Chinese, Japanese, Korean, French, Spanish, Portuguese, German, Italian, Russian, Vietnamese, Thai, Arabic, and more (29 total)

---

# Usage

Below, you will find instructions and examples for using `ReaderLM-v2` locally using the Hugging Face Transformers library.
For a more hands-on experience in a hosted environment, see the [Google Colab Notebook](https://colab.research.google.com/drive/1FfPjZwkMSocOLsEYH45B3B4NxDryKLGI?usp=sharing).

## Via Reader API

`ReaderLM-v2` is now fully integrated with [Reader API](https://jina.ai/reader/). To use it, simply specify `x-engine: readerlm-v2` in your request headers and enable response streaming with `-H 'Accept: text/event-stream'`:

```bash
curl https://r.jina.ai/https://news.ycombinator.com/ -H 'x-engine: readerlm-v2' -H 'Accept: text/event-stream'
```

You can try it without an API key at a lower rate limit. For higher rate limits, you can purchase an API key. Please note that ReaderLM-v2 requests consume 3x the normal token count from your API key allocation. This is currently an experimental feature, and we're working with the GCP team to improve GPU efficiency.

## On Google Colab

You can try `ReaderLM-v2` via our [Colab notebook](https://colab.research.google.com/drive/1FfPjZwkMSocOLsEYH45B3B4NxDryKLGI?usp=sharing), which demonstrates HTML-to-markdown conversion, JSON extraction, and instruction-following using the HackerNews frontpage as an example. The notebook is optimized for Colab's free T4 GPU tier and requires `vllm` and `triton` for acceleration and running.

Note that the free T4 GPU has limitations—it doesn't support bfloat16 or flash attention 2, leading to higher memory usage and slower processing of longer inputs. Nevertheless, ReaderLM-v2 successfully processes large documents under these constraints, achieving processing speeds of 67 tokens/s input and 36 tokens/s output. For production use, we recommend an RTX 3090/4090 for optimal performance.

## Local Usage

To use `ReaderLM-v2` locally:

1. Install the necessary dependencies:

   ```bash
   pip install transformers
   ```

2. Load and run the model:

   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer

   device = "cuda"  # or "cpu"
   tokenizer = AutoTokenizer.from_pretrained("jinaai/ReaderLM-v2")
   model = AutoModelForCausalLM.from_pretrained("jinaai/ReaderLM-v2").to(device)
   ```

3. (Optional) Pre-clean your HTML to remove scripts, styles, comments, to reduce the noise and length of the input:

   ```python
   import re

   # Patterns
   SCRIPT_PATTERN = r"<[ ]*script.*?\/[ ]*script[ ]*>"
   STYLE_PATTERN = r"<[ ]*style.*?\/[ ]*style[ ]*>"
   META_PATTERN = r"<[ ]*meta.*?>"
   COMMENT_PATTERN = r"<[ ]*!--.*?--[ ]*>"
   LINK_PATTERN = r"<[ ]*link.*?>"
   BASE64_IMG_PATTERN = r'<img[^>]+src="data:image/[^;]+;base64,[^"]+"[^>]*>'
   SVG_PATTERN = r"(<svg[^>]*>)(.*?)(<\/svg>)"


   def replace_svg(html: str, new_content: str = "this is a placeholder") -> str:
       return re.sub(
           SVG_PATTERN,
           lambda match: f"{match.group(1)}{new_content}{match.group(3)}",
           html,
           flags=re.DOTALL,
       )


   def replace_base64_images(html: str, new_image_src: str = "#") -> str:
       return re.sub(BASE64_IMG_PATTERN, f'<img src="{new_image_src}"/>', html)


   def clean_html(html: str, clean_svg: bool = False, clean_base64: bool = False):
       html = re.sub(
           SCRIPT_PATTERN, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
       )
       html = re.sub(
           STYLE_PATTERN, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
       )
       html = re.sub(
           META_PATTERN, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
       )
       html = re.sub(
           COMMENT_PATTERN, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
       )
       html = re.sub(
           LINK_PATTERN, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
       )

       if clean_svg:
           html = replace_svg(html)
       if clean_base64:
           html = replace_base64_images(html)
       return html
   ```

4. Create a prompt for the model:

   ```python
   def create_prompt(
       text: str, tokenizer=None, instruction: str = None, schema: str = None
   ) -> str:
       """
       Create a prompt for the model with optional instruction and JSON schema.
       """
       if not instruction:
           instruction = "Extract the main content from the given HTML and convert it to Markdown format."
       if schema:
           instruction = "Extract the specified information from a list of news threads and present it in a structured JSON format."
           prompt = f"{instruction}\n```html\n{text}\n```\nThe JSON schema is as follows:```json\n{schema}\n```"
       else:
           prompt = f"{instruction}\n```html\n{text}\n```"

       messages = [
           {
               "role": "user",
               "content": prompt,
           }
       ]

       return tokenizer.apply_chat_template(
           messages, tokenize=False, add_generation_prompt=True
       )
   ```

### HTML to Markdown Example

```python
html = "<html><body><h1>Hello, world!</h1></body></html>"

html = clean_html(html)

input_prompt = create_prompt(html, tokenizer=tokenizer)
inputs = tokenizer.encode(input_prompt, return_tensors="pt").to(device)
outputs = model.generate(
    inputs, max_new_tokens=1024, temperature=0, do_sample=False, repetition_penalty=1.08
)

print(tokenizer.decode(outputs[0]))
```

### HTML to JSON Example

```python
schema = """
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "author": {
      "type": "string"
    },
    "date": {
      "type": "string"
    },
    "content": {
      "type": "string"
    }
  },
  "required": ["title", "author", "date", "content"]
}
"""

html = clean_html(html)
input_prompt = create_prompt(html, tokenizer=tokenizer, schema=schema)

inputs = tokenizer.encode(input_prompt, return_tensors="pt").to(device)
outputs = model.generate(
    inputs, max_new_tokens=1024, temperature=0, do_sample=False, repetition_penalty=1.08
)

print(tokenizer.decode(outputs[0]))
```

## Model Performance

ReaderLM-v2 has been extensively evaluated on various tasks:

### Quantitative Evaluation

For HTML-to-Markdown tasks, the model outperforms much larger models like Qwen2.5-32B-Instruct and Gemini2-flash-expr, achieving:
- ROUGE-L: 0.84
- Levenshtein Distance: 0.22
- Jaro-Winkler Similarity: 0.82

For HTML-to-JSON tasks, it shows competitive performance with:
- F1 Score: 0.81
- Precision: 0.82
- Recall: 0.81
- Pass-Rate: 0.98

### Qualitative Evaluation

The model excels in three key dimensions:
- Content Integrity: 39/50
- Structural Accuracy: 35/50
- Format Compliance: 36/50

These scores demonstrate strong performance in preserving semantic information, maintaining structural accuracy, and adhering to markdown syntax standards.

## Training Details

ReaderLM-v2 is built on Qwen2.5-1.5B-Instruction and trained using a sophisticated pipeline:

1. Data Preparation: Created html-markdown-1m dataset with 1 million HTML documents
2. Synthetic Data Generation: Three-step pipeline using Qwen2.5-32B-Instruction
   - Drafting: Initial markdown and JSON generation
   - Refinement: Content cleanup and structure alignment
   - Critique: Quality evaluation and filtering

3. Training Process:
   - Long-context pretraining
   - Supervised fine-tuning
   - Direct preference optimization
   - Self-play reinforcement tuning