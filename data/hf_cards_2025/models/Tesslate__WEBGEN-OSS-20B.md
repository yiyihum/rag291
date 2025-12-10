---
base_model: unsloth/gpt-oss-20b-bf16
license: apache-2.0
language:
- en
tags:
- text-generation-inference
- transformers
- unsloth
- gpt_oss
- web-generation
- html
- css
- tailwind-css
- ui-generation
- web-design
- small-model
- qwen3
- transformers
---

[Example Output](https://codepen.io/qingy1337/pen/xbwNWGw)

<style>
:root{
  --bg: #0b0c0f;
  --panel: #0f1117;
  --ink: #e9eefc;
  --muted: #9aa3b2;
  --brand: #5b8cff; /* soft indigo */
  --brand-2: #4ef2c8; /* mint accent */
  --border: rgba(255,255,255,.08);
  --glow: rgba(91,140,255,.25);
  --radius: 16px;
}
*{ box-sizing: border-box }
.card{
  background: linear-gradient(180deg,rgba(255,255,255,.02),rgba(255,255,255,.00));
  border:1px solid var(--border);
  border-radius: var(--radius);
  padding:16px;
}
.badge{
  display:inline-flex;align-items:center;gap:.5rem;
  padding:.35rem .6rem;border:1px solid var(--border);border-radius:999px;
  color:var(--muted);font-size:.85rem
}
.grid{ display:grid; gap:18px }
.grid-2{ grid-template-columns:repeat(2,minmax(0,1fr)); }
.grid-3{ grid-template-columns:repeat(3,minmax(0,1fr)); }
@media(max-width:900px){ .grid-2,.grid-3{ grid-template-columns:1fr } }
.kicker{
  display:inline-block;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);font-size:.75rem;margin-bottom:.5rem
}
h1,h2,h3{ color:var(--ink); margin:0 0 .4rem 0; line-height:1.1 }
h1{ font-size:2.25rem; font-weight:800 }
h2{ font-size:1.3rem; font-weight:700 }
h3{ font-size:1.05rem; font-weight:700 }
p,li{ color:var(--muted); line-height:1.6 }
hr{ border:none; height:1px; background:var(--border); margin:28px 0 }
a.btn{
  display:inline-block; padding:.7rem 1rem; border-radius:12px;
  background: linear-gradient(180deg,var(--brand),#3f6fff);
  color:var(--ink); text-decoration:none; font-weight:600;
  box-shadow: 0 10px 30px var(--glow);
}
a.btn.ghost{
  background:transparent; color:var(--ink); border:1px solid var(--border)
}
kbd{
  background:#0c1322;color:#cfe0ff;border:1px solid #1a2742;border-bottom-color:#142138;
  padding:.12rem .4rem;border-radius:6px;font-size:.85rem
}
.codeblock{
  background:#0b1220;border:1px solid #15233d;border-radius:12px;padding: 8px;overflow:auto; /* Changed padding */
  margin: 1rem 0;
}
.codeblock pre {
  margin: 0;
}
.tagline{
  font-size:1.05rem;color:#c6d5ff
}
.pill{
  display:inline-flex;align-items:center;gap:.4rem;
  padding:.35rem .6rem;border-radius:999px;border:1px dashed var(--border);color:#b9c5db
}
.hero{
  background:
    radial-gradient(600px 240px at 20% 0%,rgba(91,140,255,.18),transparent 60%),
    radial-gradient(600px 240px at 80% 10%,rgba(78,242,200,.12),transparent 60%);
  border:1px solid var(--border);
  border-radius:20px; padding:28px
}
figure.screens{
  display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:16px 0 0 0
}
figure.screens img{
  width:100%;border-radius:12px;border:1px solid var(--border)
}
details{
  border:1px solid var(--border);border-radius:12px;padding:14px;background:rgba(255,255,255,.02)
}
summary{ cursor:pointer;color:var(--ink);font-weight:700 }
blockquote{
  margin:0;padding:14px;border-left:3px solid var(--brand);background:rgba(91,140,255,.06);
  border-radius:0 10px 10px 0;color:#657ce0
}
table{ width:100%; border-collapse:collapse }
th,td{ text-align:left; padding:10px; border-bottom:1px solid var(--border); color:var(--muted) }
th{ color:#3480eb }
.callout{
  border:1px solid var(--border);border-radius:14px;padding:14px;background:rgba(255,255,255,.02)
}
</style>

<div style="background:var(--bg); padding: 28px; border-radius: 18px">

<div class="hero">
  <span class="kicker">Tesslate • Research Preview</span>
  <h1>WEBGEN-OSS-20B</h1>
  <p class="tagline">A <strong>web-only generator</strong> that turns one prompt into clean, responsive <strong>HTML/CSS/Tailwind</strong>. Small enough for laptops; opinionated for consistent, modern layouts.</p>
  <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:12px">
   
    <span class="pill">Open weights</span>
    <span class="pill">Web-only bias</span>
    <span class="pill">Mobile-first output</span>
    <span class="pill">No external JS by default</span>
  </div>
  <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:18px">
    <a class="btn" href="https://huggingface.co/Tesslate/WEBGEN-OSS-20B/resolve/main/README.md">Model card</a>
    <a class="btn ghost" href="https://tesslate.com">Tesslate</a>
    <a class="btn ghost" href="https://uigenoutput.tesslate.com">Demos</a>
    <a class="btn ghost" href="https://discord.gg/EcCpcTv93U">Discord</a>
  </div>

  <figure class="screens">
    <img alt="Hero sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/G9dpxQKrYJlpnj3Pvw3LV.png">
    <img alt="Pricing sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/2GrgB4W5VzPqnpD4FJsA-.png">
    <img alt="Features sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/lGvrwLBqeS9IJeKgLrMWO.png">
    <img alt="Hero sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/3Kh7TkSuxKctsGOtHGRXJ.png">
    <img alt="Pricing sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/KYwUop65wR8WikMaw5upL.png">
    <img alt="Features sample" src="https://cdn-uploads.huggingface.co/production/uploads/64d1129297ca59bcf7458d07/H-c5ORCyMpYmlDN52m3im.png">
  </figure>
</div>

<hr/>

<div class="grid grid-2" style="margin-top: 1.5rem">
  <div class="card">
    <h3>What it is</h3>
    <p><strong>WEBGEN-OSS-20B</strong> focuses solely on generating production-lean websites. It prefers semantic HTML, sane spacing, and modern component blocks (hero, grids, pricing, FAQ).</p>
  </div>
  <div class="card">
    <h3>Why</h3>
    <p>Small enough for local runs and fast iteration, while retaining strong structure/consistency for HTML/CSS/Tailwind output.</p>
  </div>
</div>

<hr/>

## Quickstart

### Transformers
<div class="codeblock"><pre>
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Tesslate/WEBGEN-OSS-20B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

prompt = """Make a single-file landing page for 'LatticeDB'.
Style: modern, generous whitespace, Tailwind, rounded-xl, soft gradients.
Sections: navbar, hero (headline + 2 CTAs), features grid, pricing (3 tiers),
FAQ accordion, footer. Constraints: semantic HTML, no external JS."""

inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=2000, temperature=0.7, top_p=0.9)
print(tok.decode(out[0], skip_special_tokens=True))
</pre></div>

### vLLM
<div class="codeblock"><pre>
vllm serve Tesslate/WEBGEN-OSS-20B \
  --host 0.0.0.0 --port 8000 \
  --max-model-len 65536 \
  --gpu-memory-utilization 0.92
</pre></div>

### sglang
<div class="codeblock"><pre>
python -m sglang.launch_server \
  --model-path Tesslate/WEBGEN-OSS-20B \
  --host 0.0.0.0 --port 5000 \
  --mem-fraction-static 0.94 \
  --attention-backend flashinfer
</pre></div>

> **Tip:** Lower temperature (e.g., `0.4–0.6`) yields stricter, cleaner markup. Raise it for more visual variety.

<hr/>

## Inference Settings (suggested)

<table>
  <thead><tr><th>Param</th><th>Value</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td><code>temperature</code></td><td>0.6</td><td>Balance creativity &amp; consistency (lower if quantized)</td></tr>
    <tr><td><code>top_p</code></td><td>0.9</td><td>Nucleus sampling</td></tr>
    <tr><td><code>top_k</code></td><td>40</td><td>Optional vocab restriction</td></tr>
    <tr><td><code>max_new_tokens</code></td><td>1200–2500</td><td>Single-file sites often fit &lt; 1500</td></tr>
    <tr><td><code>repetition_penalty</code></td><td>1.1</td><td>Reduces repetitive classes/markup</td></tr>
  </tbody>
</table>

<hr/>

## Prompts that work well

<div class="grid grid-2">
  <div class="card">
    <h3>Starter</h3>
    <div class="codeblock"><pre>
Make a single-file landing page for "RasterFlow" (GPU video pipeline).
Style: modern tech, muted palette, Tailwind, rounded-xl, subtle gradients.
Sections: navbar, hero (big headline + 2 CTAs), logos row, features (3x cards),
code block (copyable), pricing (3 tiers), FAQ accordion, footer.
Constraints: semantic HTML, no external JS. Return ONLY the HTML code.
</pre></div>
  </div>
  <div class="card">
    <h3>Design-strict</h3>
    <div class="codeblock"><pre>
Use an 8pt spacing system. Palette: slate with indigo accents.
Typography scale: 14/16/18/24/36/56. Max width: 1200px.
Avoid shadows &gt; md; prefer borders/dividers.
</pre></div>
  </div>
</div>

<hr/>

## Quantization & VRAM (example)

<table>
  <thead><tr><th>Format</th><th>Footprint</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>BF16</td><td>8.05 GB</td><td>Fastest, best fidelity</td></tr>
    <tr><td>GGUF Q5_K_M</td><td>2.89 GB</td><td>Great quality/size trade-off</td></tr>
    <tr><td>GGUF Q4_K_M</td><td>2.5 GB</td><td>Smallest comfortable for laptops</td></tr>
  </tbody>
</table>
<hr/>

## Intended Use & Scope

- **Primary:** Generate complete, single-file websites (landing pages, marketing pages, simple docs) with **semantic HTML** and **Tailwind** classes.
- **Secondary:** Component blocks (hero, pricing, FAQ) for manual composition.

<details>
<summary><strong>Limitations</strong></summary>
<ul>
  <li>Accessibility: adds headings/labels but ARIA coverage may need review.</li>
  <li>JS widgets: kept light unless explicitly requested in prompt.</li>
</ul>
</details>

<details>
<summary><strong>Ethical Considerations</strong></summary>
<ul>
  <li>Curate prompts appropriately.</li>
  <li>When using third-party logos/assets, ensure you have rights or use open sources.</li>
</ul>
</details>

<hr/>

## Training Summary (research preview)

- **Objective:** Tight web-only bias; reward semantic structure, spacing rhythm, and responsiveness.  
- **Data:** Mixture of curated HTML/CSS/Tailwind snippets, component libraries, and synthetic page specs.  
- **Recipe:** SFT with format constraints → instruction tuning → style/rhythm preference optimization.  
- **Context:** effective ~64k; trained to keep default outputs within practical page length.


<hr/>

## Example Outputs

## Community

- **Examples:** <a href="https://uigenoutput.tesslate.com">uigenoutput.tesslate.com</a>  
- **Discord:** <a href="https://discord.gg/EcCpcTv93U">discord.gg/EcCpcTv93U</a>  
- **Website:** <a href="https://tesslate.com">tesslate.com</a>

<blockquote>
“Why are good design models so expensive” — Tesslate Team
</blockquote>

<hr/>

## Citation

```
@misc{tesslate_webgen_oss_preview_2025,
title   = {WEBGEN-OSS-20B: Design-first web generation},
author  = {Tesslate Team},
year    = {2025},
url     = {https://huggingface.co/Tesslate/WEBGEN-OSS-20B}
}
```

</div>

<!----

<div class="grid grid-3">
  <div class="card"><img alt="Sample A" src="https://YOUR_CDN/out-a.png" style="width:100%;border-radius:10px;border:1px solid var(--border)"><p style="margin-top:.5rem">Marketing page (product launch)</p></div>
  <div class="card"><img alt="Sample B" src="https://YOUR_CDN/out-b.png" style="width:100%;border-radius:10px;border:1px solid var(--border)"><p style="margin-top:.5rem">SaaS pricing + FAQ</p></div>
  <div class="card"><img alt="Sample C" src="https://YOUR_CDN/out-c.png" style="width:100%;border-radius:10px;border:1px solid var(--border)"><p style="margin-top:.5rem">Docs-style layout</p></div>
</div>

<hr/>
---->
