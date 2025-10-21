---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
base_model: LiquidAI/LFM2-350M
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7_6D7rWrLxp2hb6OHSV1p.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center;">
<a href="https://playground.liquid.ai/chat">
<svg width="114.8" height="20" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Playground" style="margin-bottom: 1em;">
  <title>Playground</title>
  <g>
    <rect fill="#fff" width="200" height="200"></rect>
    <rect fill="url(#x)" x="200" width="800" height="200"></rect>
  </g>
  <g transform="translate(35, 30) scale(0.45, 0.45)">
    <path d="M172.314 129.313L172.219 129.367L206.125 188.18C210.671 195.154 213.324 203.457 213.324 212.382C213.324 220.834 210.956 228.739 206.839 235.479L275.924 213.178L167.853 33.6L141.827 76.9614L172.314 129.313Z" fill="black"/>
    <path d="M114.217 302.4L168.492 257.003C168.447 257.003 168.397 257.003 168.352 257.003C143.515 257.003 123.385 237.027 123.385 212.387C123.385 203.487 126.023 195.204 130.55 188.24L162.621 132.503L135.966 86.7327L60.0762 213.183L114.127 302.4H114.217Z" fill="black"/>
    <path d="M191.435 250.681C191.435 250.681 191.43 250.681 191.425 250.686L129.71 302.4H221.294L267.71 226.593L191.435 250.686V250.681Z" fill="black"/>
  </g>
  <g transform="translate(50, 0)" aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,sans-serif" font-size="110">
    <text x="255" y="148" textLength="619" fill="#000" opacity="0.1">Playground</text>
    <text x="245" y="138" textLength="619">Playground</text>
  </g>
  <linearGradient id="x" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
    <stop offset="100%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
<a href="https://leap.liquid.ai/?utm_source=huggingface&utm_medium=modelcards">
<svg width="114.8" height="20" viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Leap" style="margin-bottom: 1em;">
  <title>Leap</title>
  <g>
    <rect fill="#000" width="500" height="200"></rect>
  </g>
  <g transform="translate(100, 45) scale(3.5, 3.5)" fill="#fff">
    <path d="M13.8512 28.0769C12.5435 28.0769 11.4025 27.8205 10.4281 27.3077C9.45375 26.7692 8.68452 26.0128 8.12042 25.0385C7.58196 24.0641 7.31273 22.9359 7.31273 21.6538V3.76923H0.389648V0H11.4666V21.6538C11.4666 22.4744 11.6973 23.1282 12.1589 23.6154C12.6204 24.0769 13.2486 24.3077 14.0435 24.3077H20.582V28.0769H13.8512Z"/>
    <path d="M29.6439 28.4615C27.9259 28.4615 26.4131 28.1282 25.1054 27.4615C23.8233 26.7692 22.8362 25.8077 22.1439 24.5769C21.4516 23.3462 21.1054 21.9103 21.1054 20.2692V14.7308C21.1054 13.0641 21.4516 11.6282 22.1439 10.4231C22.8362 9.19231 23.8233 8.24359 25.1054 7.57692C26.4131 6.88462 27.9259 6.53846 29.6439 6.53846C31.3875 6.53846 32.9003 6.88462 34.1823 7.57692C35.4644 8.24359 36.4516 9.19231 37.1439 10.4231C37.8362 11.6282 38.1823 13.0641 38.1823 14.7308V18.5H25.1054V20.2692C25.1054 21.8333 25.49 23.0256 26.2592 23.8462C27.0541 24.6667 28.1951 25.0769 29.6823 25.0769C30.8875 25.0769 31.8618 24.8718 32.6054 24.4615C33.349 24.0256 33.8105 23.3974 33.99 22.5769H38.1054C37.7977 24.3718 36.8746 25.8077 35.3362 26.8846C33.7977 27.9359 31.9003 28.4615 29.6439 28.4615ZM34.1823 16V14.6923C34.1823 13.1538 33.7977 11.9615 33.0285 11.1154C32.2592 10.2692 31.131 9.84615 29.6439 9.84615C28.1823 9.84615 27.0541 10.2692 26.2592 11.1154C25.49 11.9615 25.1054 13.1667 25.1054 14.7308V15.6923L34.49 15.6538L34.1823 16Z"/>
    <path d="M46.3596 28.4615C44.1545 28.4615 42.4109 27.8974 41.1288 26.7692C39.8724 25.6154 39.2442 24.0513 39.2442 22.0769C39.2442 20.0769 39.9109 18.5128 41.2442 17.3846C42.6032 16.2308 44.4622 15.6538 46.8211 15.6538H52.7058V13.6923C52.7058 12.5385 52.3468 11.641 51.6288 11C50.9109 10.359 49.8981 10.0385 48.5904 10.0385C47.4365 10.0385 46.475 10.2949 45.7058 10.8077C44.9365 11.2949 44.4878 11.9487 44.3596 12.7692H40.2827C40.5135 10.8718 41.3852 9.35897 42.8981 8.23077C44.4365 7.10256 46.3724 6.53846 48.7058 6.53846C51.2186 6.53846 53.2058 7.17949 54.6673 8.46154C56.1288 9.71795 56.8596 11.4359 56.8596 13.6154V28.0769H52.8211V24.1923H52.1288L52.8211 23.4231C52.8211 24.9615 52.2314 26.1923 51.0519 27.1154C49.8724 28.0128 48.3083 28.4615 46.3596 28.4615ZM47.5904 25.2692C49.0776 25.2692 50.2955 24.8974 51.2442 24.1538C52.2186 23.3846 52.7058 22.4103 52.7058 21.2308V18.4615H46.8981C45.8211 18.4615 44.9622 18.7564 44.3211 19.3462C43.7058 19.9359 43.3981 20.7436 43.3981 21.7692C43.3981 22.8462 43.7699 23.7051 44.5135 24.3462C45.257 24.9615 46.2827 25.2692 47.5904 25.2692Z"/>
    <path d="M58.9984 35V6.92308H63.1138V10.9615H63.9984L63.1138 11.9231C63.1138 10.2564 63.6266 8.94872 64.6523 8C65.7036 7.02564 67.101 6.53846 68.8446 6.53846C70.9728 6.53846 72.6651 7.25641 73.9215 8.69231C75.2036 10.1026 75.8446 12.0385 75.8446 14.5V20.4615C75.8446 22.1026 75.5497 23.5256 74.96 24.7308C74.3959 25.9103 73.5882 26.8333 72.5369 27.5C71.5113 28.141 70.2805 28.4615 68.8446 28.4615C67.1266 28.4615 65.742 27.9872 64.6907 27.0385C63.6395 26.0641 63.1138 24.7436 63.1138 23.0769L63.9984 24.0385H63.0369L63.1523 28.9615V35H58.9984ZM67.4215 24.8462C68.7805 24.8462 69.8318 24.4615 70.5754 23.6923C71.3446 22.8974 71.7292 21.7564 71.7292 20.2692V14.7308C71.7292 13.2436 71.3446 12.1154 70.5754 11.3462C69.8318 10.5513 68.7805 10.1538 67.4215 10.1538C66.1138 10.1538 65.0754 10.5641 64.3061 11.3846C63.5369 12.1795 63.1523 13.2949 63.1523 14.7308V20.2692C63.1523 21.7051 63.5369 22.8333 64.3061 23.6538C65.0754 24.4487 66.1138 24.8462 67.4215 24.8462Z"/>
  </g>
  <linearGradient id="y" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
</div>
</center>

# LFM2-350M-Extract

Based on [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M), LFM2-350M-Extract is designed to **extract important information from a wide variety of unstructured documents** (such as articles, transcripts, or reports) into structured outputs like JSON, XML, or YAML.

**Use cases**:

- Extracting invoice details from emails into structured JSON.
- Converting regulatory filings into XML for compliance systems.
- Transforming customer support tickets into YAML for analytics pipelines.
- Populating knowledge graphs with entities and attributes from unstructured reports.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 📄 Model details

**Generation parameters**: We strongly recommend using greedy decoding with a `temperature=0`.

**System prompt**: If no system prompt is provided, the model will default to JSON outputs. We recommend providing a system prompt with a specific format (JSON, XML, or YAML) and a given schema to improve accuracy (see the following example).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/MeSOLz1XeTtinRjrVkF7d.png)

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, and Spanish.

**Chat template**: LFM2 uses a ChatML-like chat template as follows:

```
<|startoftext|><|im_start|>system
Return data as a JSON object with the following schema:\n[...]<|im_end|>
<|im_start|>user
Caenorhabditis elegans is a free-living transparent nematode about 1 mm in length that lives in temperate soil environments.<|im_end|>
<|im_start|>assistant
{
"species": "C. elegans",
"genus": "Caenorhabditis",
"description": "A free-living transparent nematode about 1 mm in length that lives in temperate soil environments.",
[...]{<|im_end|>
```

You can automatically apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

> [!WARNING]
> ⚠️ The model is intended for single-turn conversations.

The data used for training these models was primarily synthetic, which allowed us to ensure a diverse data mix. We used a range of document types, domains, styles, lengths, and languages. We also varied the density and distribution of relevant text in the documents. In some cases, the extracted information was clustered in one part of the document; in others, it’s spread throughout. We applied the same approach of ensuring diversity when creating synthetic user requests and designing the structure of the model outputs. The data generation process underwent many iterations, incorporating ideas and feedback from across the Liquid AI team.

## 📈 Performance

We evaluated LFM2-Extract on a dataset of 5,000 documents, covering over 100 topics with a mix of writing styles, ambiguities, and formats. We used a combination of five metrics to capture a balanced view on syntax, accuracy, and faithfulness:

- **Syntax score**: Checks whether outputs parse cleanly as valid JSON, XML, or YAML.
- **Format accuracy**: Verifies that outputs match the requested format (e.g., JSON when JSON is requested).
- **Keyword faithfulness**: Measures whether values in the structured output actually appear in the input text.
- **Absolute scoring**: A judge LLM scores quality on a 1-5 scale, assessing completeness and correctness of extractions.
- **Relative scoring**: We ask a judge LLM to choose the best answer between the extraction model’s output and the ground-truth answer.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/DNZgCKMFSg5xhHoBgJjeC.png)

LFM2-350M-Extract outperforms Gemma 3 4B at this task, a model more than 11x its size.

## 🏃 How to run

- Hugging Face: [LFM2-350M](https://huggingface.co/LiquidAI/LFM2-350M)
- llama.cpp: [LFM2-350M-Extract-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-Extract-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-350M-extract)

## 📬 Contact

If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).