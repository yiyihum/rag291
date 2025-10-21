---
language: en
license: apache-2.0
datasets:
- go_emotions
- empathetic_dialogues
pipeline_tag: text-generation
library_name: transformers
tags:
- multimodal
- emotion-detection
- empathetic-chatbot
- t5
- clip
- streamlit
base_model: t5-small
---

# Emo — Multimodal Emotion-Aware Assistant

**Repository:** `hmnshudhmn24/emo-multimodal-assistant`

**Short:** An advanced assistant that detects user emotion from text *and image*, and responds empathetically by conditioning a text-generator (T5) on the detected emotions.

**Components**
- Text emotion classifier (DistilBERT fine-tuned on GoEmotions)
- Image emotion detector (CLIP zero-shot with emotion labels)
- Response generator (T5-small fine-tuned on EmpatheticDialogues)
- Inference script combining everything
- Streamlit app for quick demo (text + optional image upload)

## Quick usage (inference)

```python
from inference import EmoAssistant

assistant = EmoAssistant(
    text_emotion_model="hmnshudhmn24/emo-text-emotion",
    response_model="hmnshudhmn24/emo-response-generator"
)

# text-only
reply = assistant.respond(user_text="I'm so stressed about exams.")
print(reply)

# text + image (image path)
reply = assistant.respond(user_text="I had a rough day", image_path="example.jpg")
print(reply)
```

## How to train (short)
1. Train text emotion classifier:
   ```bash
   python train_text_emotion.py --save-dir ./emo-text-emotion
   ```
2. Train response generator (empathetic responses):
   ```bash
   python train_response_generator.py --save-dir ./emo-response-generator
   ```
3. After training, add `pytorch_model.bin`, tokenizer files, and README for each model and upload to Hugging Face or put them in local folders referenced by `inference.py`.

## Notes & Ethics
- This is not for medical/mental-health diagnosis. It’s built for supportive, empathetic responses only.
- Always add content / safety filters before production.
