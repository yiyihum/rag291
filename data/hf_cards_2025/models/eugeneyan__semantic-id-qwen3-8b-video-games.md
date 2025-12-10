---
license: apache-2.0
base_model: Qwen/Qwen2.5-3B
tags:
- semantic-ids
- recommendation-system
- video-games
- generative-retrieval
- qwen
- fine-tuned
datasets:
- eugeneyan/video-games-semantic-ids-mapping
language:
- en
library_name: transformers
pipeline_tag: text-generation
---

# Semantic ID Recommender - Qwen3 8B (Video Games)

## Model Description

This is a Qwen3 8B model fine-tuned for video games product recommendation using
semantic IDs. The model has been trained to understand and generate hierarchical semantic
identifiers that encode product relationships, enabling generative retrieval for recommendation
systems.

See writeup and demo here: https://eugeneyan.com/writing/semantic-ids/

### What are Semantic IDs?

Semantic IDs are learned hierarchical representations that encode product similarities and
relationships in their structure. Unlike traditional IDs, semantic IDs carry meaning - similar
products have similar ID prefixes.

## Special Tokens

The model uses special tokens to work with semantic IDs:

- `<|sid_start|>`: Marks the beginning of a semantic ID
- `<|sid_X|>`: Hierarchical level tokens where X ∈ [0, 1023]
- `<|sid_end|>`: Marks the end of a semantic ID
- `<|rec|>`: Trigger token for generating recommendations

### Semantic ID Format

`<|sid_start|><|sid_127|><|sid_45|><|sid_89|><|sid_12|><|sid_end|>`

This represents a 4-level hierarchy where each level provides increasingly specific
categorization.

## Training Details

- **Base Model**: Qwen3 8B
- **Fine-tuning Method**: Supervised Fine-Tuning (SFT)
- **Dataset**: Amazon Video Games reviews and metadata
- **Number of Products**: 66,097
- **Training Epochs**: 2
- **Task**: Next item prediction and recommendation generation

## Usage

### Installation

```bash
pip install transformers torch datasets
```

### Basic Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "eugeneyan/semantic-id-qwen3-8b-video-games"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# Set padding for generation
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Generate recommendations
prompt = "User: <|sid_start|><|sid_8|><|sid_454|><|sid_630|><|sid_768|><|sid_end|>\n<|rec|>"
inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        temperature=0.3,
        top_p=0.7,
        top_k=20,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

# Decode only the generated portion
input_length = inputs["input_ids"].shape[1]
generated_tokens = outputs[:, input_length:]
response = tokenizer.decode(generated_tokens[0], skip_special_tokens=False)
print(response)
```

### Advanced: Mapping Semantic IDs to Product Titles

```python
from datasets import load_dataset
import pandas as pd
import re
from typing import List

# Load mapping dataset
dataset = load_dataset("eugeneyan/video-games-semantic-ids-mapping")
mapping_df = dataset['train'].to_pandas()

def parse_semantic_id(semantic_id: str) -> List[str]:
    """Parse semantic ID into component levels"""
    sid = semantic_id.replace("<|sid_start|>", "").replace("<|sid_end|>", "")
    pattern = r"<\|sid_\d+\|>"
    return re.findall(pattern, sid)

def map_semantic_id_to_titles(semantic_id_str: str, mapping_df: pd.DataFrame) -> dict:
    """
    Map semantic ID to titles with exact match and fallback.
    Returns dict with match_level, titles, count, and match_type.
    """
    levels = parse_semantic_id(semantic_id_str)

    if not levels:
        return {"match_level": 0, "titles": [], "count": 0}

    # Try exact match first
    exact_matches = mapping_df[mapping_df["semantic_id"] == semantic_id_str]
    if len(exact_matches) > 0:
        titles = exact_matches["title"].tolist()
        return {"match_level": 4, "titles": titles, "count": len(titles), "match_type": "exact"}

    # Fallback to prefix matching
    for depth in range(min(3, len(levels)), 0, -1):
        prefix = "<|sid_start|>" + "".join(levels[:depth])
        matches = mapping_df[mapping_df["semantic_id"].str.startswith(prefix)]

        if len(matches) > 0:
            titles = matches["title"].tolist()
            return {
                "match_level": depth,
                "titles": titles[:5],
                "count": len(titles),
                "match_type": "prefix"
            }

    return {"match_level": 0, "titles": [], "count": 0, "match_type": "none"}

def extract_and_replace_semantic_ids(text: str, mapping_df: pd.DataFrame) -> str:
    """Replace all semantic IDs in text with product titles"""
    pattern = r"<\|sid_start\|>(?:<\|sid_\d+\|>)+<\|sid_end\|>"
    semantic_ids = re.findall(pattern, text)

    result = text
    for sid in semantic_ids:
        match_result = map_semantic_id_to_titles(sid, mapping_df)
        if match_result["count"] > 0:
            title = match_result["titles"][0]
            replacement = f'"{title}"'
            if match_result["match_type"] == "prefix":
                replacement += f' (L{match_result["match_level"]} match)'
            if match_result["count"] > 1:
                replacement += f' [+{match_result["count"]-1} similar]'
        else:
            replacement = "[Unknown Item]"
        result = result.replace(sid, replacement)

    return result
```

## Example Interactions

### Single Item Recommendation

```python
# Provide input of user past interactions and get recommendation
INPUT = """User: <|sid_start|><|sid_8|><|sid_454|><|sid_630|><|sid_768|><|sid_end|>, <|sid_start|><|sid_126|><|sid_501|><|sid_553|><|sid_768|><|sid_end|>, <|sid_start|><|sid_205|><|sid_370|><|sid_548|><|sid_768|><|sid_end|>
<|rec|>""".strip()
response = chat(INPUT)

# Output: Recommended product
<|sid_start|><|sid_205|><|sid_407|><|sid_586|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "Assassin's Creed 2 Deluxe Edition [Download]"
```

```python
# Provide input of single past item and get similar item
INPUT = """Customers who bought <|sid_start|><|sid_201|><|sid_311|><|sid_758|><|sid_768|><|sid_end|> also bought:
<|rec|>""".strip()
response = chat(INPUT)

# Output: Recommended product
<|sid_start|><|sid_201|><|sid_396|><|sid_608|><|sid_769|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "The Legend of Zelda: Ocarina of Time 3D"
```

### Natural Language with Semantic IDs

```python
# Input: Natural language context
# Provide natural language chat input and get item recommendations
INPUT = """I like scifi and action games.
<|rec|>""".strip()
response = chat(INPUT)

# Output: Multiple relevant products
<|sid_start|><|sid_64|><|sid_313|><|sid_637|><|sid_768|><|sid_end|>, <|sid_start|><|sid_219|><|sid_463|><|sid_660|><|sid_768|><|sid_end|>, <|sid_start|><|sid_64|><|sid_313|><|sid_608|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "Halo 3 Limited Edition -Xbox 360", "Battlefield: Bad Company - Playstation 3", "Halo Reach - Limited Edition -Xbox 360"
```

### Attribute-Steered Recommendations

```python
# Steering recommendations given an item and attribute (Xbox)
INPUT = """Recommend Xbox games similar to <|sid_start|><|sid_201|><|sid_396|><|sid_608|><|sid_769|><|sid_end|>:
<|rec|>""".strip()
response = chat(INPUT)

# Output: Xbox-specific recommendations
<|sid_start|><|sid_64|><|sid_271|><|sid_576|><|sid_768|><|sid_end|>, <|sid_start|><|sid_64|><|sid_400|><|sid_594|><|sid_768|><|sid_end|>, <|sid_start|><|sid_167|><|sid_271|><|sid_578|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "Fallout: New Vegas - Xbox 360 Ultimate Edition", "Tales of Vesperia - Xbox 360", "Halo Reach - Legendary Edition
```


```python
# Provide natural language chat input and get item recommendations
INPUT = """I like animal and cute games.
<|rec|>""".strip()
response = chat(INPUT)

# Output: Games matching the genre preference
<|sid_start|><|sid_173|><|sid_324|><|sid_764|><|sid_768|><|sid_end|>, <|sid_start|><|sid_201|><|sid_397|><|sid_738|><|sid_769|><|sid_end|>, <|sid_start|><|sid_173|><|sid_305|><|sid_670|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "Animal Crossing: New Leaf", "Disney Magical World - Nintendo 3DS", "Nintendogs + Cats: Golden Retriever and New Friends"
```

### Explanatory Recommendations

```python
# Provide item to get recommendation and explanation
INPUT = """I just finished <|sid_start|><|sid_125|><|sid_417|><|sid_656|><|sid_768|><|sid_end|>. Suggest another <|rec|> and explain why:""".strip()
response = chat(INPUT)

# Output: Recommendation with natural language explanation
<|sid_start|><|sid_139|><|sid_289|><|sid_534|><|sid_768|><|sid_end|>

If you liked Dragon Quest Heroes II, you might like Nights of Azure because both are action RPGs for the PlayStation 4 with a focus on combat and character progression. Both games offer a narrative-driven experience with a strong emphasis on combat mechanics, suggesting a shared appeal for players who enjoy this genre on the platform.<|im_end|>

# Output mapped
ASSISTANT: "Nights of Azure - PlayStation 4"

If you liked Dragon Quest Heroes II, you might like Nights of Azure because both are action RPGs for the PlayStation 4 with a focus on combat and character progression. Both games offer a narrative-driven experience with a strong emphasis on combat mechanics, suggesting a shared appeal for players who enjoy this genre on the platform.
```

### Multi-Turn Conversations

The model supports multi-turn conversations with context preservation:

```python
from transformers import TextStreamer

def chat(text_input: str, messages: list = None, stream: bool = True):
    """Interactive chat with the model"""
    if messages is None:
        messages = []

    messages.append({"role": "user", "content": text_input})

    # Apply chat template
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    # Stream output for better UX
    streamer = TextStreamer(tokenizer, skip_prompt=True) if stream else None

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.3,
            top_p=0.7,
            top_k=20,
            do_sample=True,
            streamer=streamer
        )

    # Extract only new tokens
    input_length = inputs["input_ids"].shape[1]
    generated = tokenizer.decode(output[0][input_length:], skip_special_tokens=True)

    messages.append({"role": "assistant", "content": generated})
    return generated, messages
```

```python
# 1st turn: Ask for games similar to Mario Kart
INPUT = "I'm looking for games similar to Mario Kart. <|rec|>"
response1 = chat(INPUT)

# Output
<|sid_start|><|sid_131|><|sid_492|><|sid_639|><|sid_768|><|sid_end|>, <|sid_start|><|sid_145|><|sid_480|><|sid_617|><|sid_768|><|sid_end|>, <|sid_start|><|sid_145|><|sid_290|><|sid_620|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "CTR: Crash Team Racing", "Crazy Taxi 2 - Sega Dreamcast", "Mario Kart: Super Circuit"

# 2nd turn: Tweak it for Xbox
INPUT = "How about something similar but for Xbox? <|rec|>"
response2 = chat(INPUT, new_convo=False)

# Output
<|sid_start|><|sid_183|><|sid_461|><|sid_517|><|sid_768|><|sid_end|>, <|sid_start|><|sid_183|><|sid_313|><|sid_679|><|sid_769|><|sid_end|>, <|sid_start|><|sid_183|><|sid_313|><|sid_605|><|sid_768|><|sid_end|><|im_end|>

# Output mapped
ASSISTANT: "Need for Speed Carbon - Xbox 360", "Forza Motorsport 2 - Xbox 360", "NASCAR '14 - Xbox 360"

# 3rd turn: Ask for bundle name
INPUT = "Suggest a name and description for the bundle"
response3 = chat(INPUT, new_convo=False)

# Output
ASSISTANT: Xbox Racing Legends: NASCAR & Forza Collection
```

### Performance

- Model Size: ~16GB
- Inference: Requires GPU with at least 20GB VRAM for float16
- Quantization: Can run on 12GB VRAM with 8-bit quantization
- CPU Inference: Possible but slow; use MPS on Apple Silicon for better performance

### Category Information

This model is specifically trained for Video Games products:
- Total products: 66,097
- Hierarchy levels: 4
- Tokens per level: 1024
- Semantic similarity encoded in hierarchy depth

### Limitations

- Trained specifically on video games products
- Semantic IDs are fixed from training time
- Requires mapping dataset to interpret semantic IDs
- Performance may degrade on products very different from training data
- May occasionally generate invalid semantic IDs (can be filtered post-generation)

### Citation

If you use this model, please cite:

```
@model{semantic_id_qwen3_8b_video_games,
author = {Eugene Yan},
title = {Semantic ID Recommender - Qwen3 8B (Video Games)},
year = {2024},
publisher = {Hugging Face},
url = {https://huggingface.co/eugeneyan/semantic-id-qwen3-8b-video-games}
}
```

Acknowledgments

- Base model: Qwen Team
- Training approach inspired by: https://arxiv.org/abs/2305.12218 and
https://arxiv.org/abs/2306.08121
- Dataset: Amazon Video Games

### Related Resources

- Mapping Dataset: https://huggingface.co/eugeneyan/video-games-semantic-ids-mapping
- GitHub: https://github.com/eugeneyan/semantic-ids
