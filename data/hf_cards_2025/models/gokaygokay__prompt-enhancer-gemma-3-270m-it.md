---
base_model: google/gemma-3-270m-it
tags:
- text-generation
- prompt-enhancement
- gemma
- prompt-engineering
datasets:
- gokaygokay/prompt-enhancer-dataset
- gokaygokay/prompt-enhancement-75k
---

# Prompt Enhancer - Gemma 3 270M

A fine-tuned model based on `google/gemma-3-270m-it` for enhancing and expanding short prompts into detailed, context-rich descriptions.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model = AutoModelForCausalLM.from_pretrained("gokaygokay/prompt-enhancer-gemma-3-270m-it")
tokenizer = AutoTokenizer.from_pretrained("gokaygokay/prompt-enhancer-gemma-3-270m-it")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

messages = [
    {"role": "system", "content": "Enhance and expand the following prompt with more details and context:"},
    {"role": "user", "content": "a cat sitting on a chair"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
output = pipe(prompt, max_new_tokens=256)
print(output[0]['generated_text'])
```

## Training Details

- **Base Model:** google/gemma-3-270m-it
- **Training Method:** LoRA (Low-Rank Adaptation)
- **LoRA Config:** r=16, alpha=32
- **Training Epochs:** 3
- **Learning Rate:** 5e-5
- **Batch Size:** 4 (with gradient accumulation)

### MODEL COMPARISON: Base vs Fine-tuned

**INPUT**: a cat sitting on a chair

**FINE-TUNED OUTPUT**:
a cat sitting on a brown wooden chair, white backdrop, cat is facing the right side of the image, black background, feline features are clear and defined, cat's head and body are on the chair, background appears dark and lit, the lighting is soft and suggests a serene evening or night scene.

**INPUT**: beautiful sunset

**FINE-TUNED OUTPUT**:
sunset sky over a landscape, clouds visible across the sky, trees in the foreground and middle, a lone figure in the middle of the frame, silhouette of a building in the middle background, horizon line visible in the distance, clear and bright sky, a dark sky with hues of orange and purple.

**INPUT**: futuristic city

**FINE-TUNED OUTPUT**:
a futuristic cityscape at night, buildings with glowing neon lights, towers covered in glowing energy crystals, a large tower with glowing lights, multiple towers below, towers have glowing lights and contain glowing structures, people walking and walking, some buildings are lit up and others are dark, large, glowing lights dominate the sky, a few people are visible on the ground below, buildings are tall and tall, some skyscrapers have multiple stories, buildings appear to be floating in space, eerie and futuristic atmosphere, dense and detailed urban environment.

**INPUT**: portrait of a woman

**FINE-TUNED OUTPUT**:
a woman in a dress, wearing a hat and a headscarf, standing in a crowded urban space, her face is visible, wearing a black shirt and a black hat, wearing a black belt around her waist, woman is wearing glasses and a scarf, large urban city skyline visible in the background, small building in the bottom left corner below the woman, copyspace, bright sunlight.
