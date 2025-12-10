---
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
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2-1.2B
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7_6D7rWrLxp2hb6OHSV1p.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>

<a href="https://playground.liquid.ai/chat">
<svg width="114.8" height="20" viewBox="0 0 1300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Liquid Playground" style="margin-bottom: 1em;">
  <title>Liquid: Playground</title>
  <g>
    <rect fill="#fff" width="600" height="200"></rect>
    <rect fill="url(#x)" x="600" width="700" height="200"></rect>
  </g>
  <g transform="translate(20, 30) scale(0.4, 0.4)">
    <path d="M172.314 129.313L172.219 129.367L206.125 188.18C210.671 195.154 213.324 203.457 213.324 212.382C213.324 220.834 210.956 228.739 206.839 235.479L275.924 213.178L167.853 33.6L141.827 76.9614L172.314 129.313Z" fill="black"/>
    <path d="M114.217 302.4L168.492 257.003C168.447 257.003 168.397 257.003 168.352 257.003C143.515 257.003 123.385 237.027 123.385 212.387C123.385 203.487 126.023 195.204 130.55 188.24L162.621 132.503L135.966 86.7327L60.0762 213.183L114.127 302.4H114.217Z" fill="black"/>
    <path d="M191.435 250.681C191.435 250.681 191.43 250.681 191.425 250.686L129.71 302.4H221.294L267.71 226.593L191.435 250.686V250.681Z" fill="black"/>
  </g>
  <g aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,sans-serif" font-size="110">
    <text x="200" y="148" textLength="329" fill="#000" opacity="0.1">Liquid</text>
    <text x="190" y="138" textLength="329" fill="#000">Liquid</text>
    <text x="655" y="148" textLength="619" fill="#000" opacity="0.1">Playground</text>
    <text x="645" y="138" textLength="619">Playground</text>
  </g>
  
  <linearGradient id="x" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
    <stop offset="100%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
</center>

# LFM2-1.2B-GGUF

LFM2 is a new generation of hybrid models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency. 

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2-1.2B

## 🏃 How to run LFM2

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2-1.2B-GGUF
```
