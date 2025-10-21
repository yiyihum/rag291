---
license: mit
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ns
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
library_name: transformers
inference: false
---

<style>
    :root{
      --bg: #0b0c0f;
      --panel: #0f1117;
      --ink: #e9eefc;
      --muted: #9aa3b2;
      --brand: #433aac; /* purple */
      --brand-2: #6b4fe8; /* lighter purple accent */
      --border: rgba(255,255,255,.08);
      --glow: rgba(67,58,172,.25);
      --radius: 16px;
    }
    *{ box-sizing: border-box }
    body{ margin: 0; padding: 28px; background: var(--bg); color: var(--muted); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
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
      background: linear-gradient(180deg,var(--brand),#3a2d98);
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
      background:#0b1220;border:1px solid #15233d;border-radius:12px;padding: 8px;overflow:auto;
      margin: 1rem 0;
    }
    .codeblock pre {
      margin: 0;
      color: var(--ink);
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
        radial-gradient(600px 240px at 20% 0%,rgba(67,58,172,.18),transparent 60%),
        radial-gradient(600px 240px at 80% 10%,rgba(107,79,232,.12),transparent 60%);
      border:1px solid var(--border);
      border-radius:20px; padding:28px
    }
    details{
      border:1px solid var(--border);border-radius:12px;padding:14px;background:rgba(255,255,255,.02)
    }
    summary{ cursor:pointer;color:var(--ink);font-weight:700 }
    blockquote{
      margin:0;padding:14px;border-left:3px solid var(--brand);background:rgba(67,58,172,.06);
      border-radius:0 10px 10px 0;color:#8f7ce8
    }
    table{ width:100%; border-collapse:collapse; margin: 1rem 0; }
    th,td{ text-align:left; padding:10px; border-bottom:1px solid var(--border); color:var(--muted); font-size: .9rem; }
    th{ color:var(--brand-2); font-weight: 700; }
    .callout{
      border:1px solid var(--border);border-radius:14px;padding:14px;background:rgba(255,255,255,.02)
    }
    .metadata{
      background: #0a0b0e; border: 1px solid var(--border); border-radius: 12px; 
      padding: 16px; margin-bottom: 24px; font-family: 'Monaco', 'Menlo', monospace; 
      font-size: .85rem; color: #8a91a3;
    }
</style>

<div class="hero">
    <div class="kicker">Open Models</div>
    <h1>Aqui-open1 Model Family</h1>
    <p class="tagline">We hereby present the first series of small open models by Aqui, trained from scratch and with an MIT license. The open1 family delivers state-of-the-art performance across reasoning, mathematics, and coding tasks while maintaining efficient inference capabilities.</p>
    
  <div style="margin-top: 20px; display: flex; gap: 12px; flex-wrap: wrap;">
      <div class="pill">🚀 Released September 7, 2025</div>
      <div class="pill">🔓 MIT Licensed</div>
      <div class="pill">⚡ Efficient Architecture</div>
  </div>
</div>

<div class="grid grid-2" style="margin-top: 28px;">
    <div class="card">
        <h2>open1-1.5B-Instruct</h2>
        <p>Ultra-efficient model optimized for edge deployment and real-time applications.</p>
        <div style="margin: 16px 0;">
            <div class="badge">🧠 1.5B parameters</div>
            <div class="badge">📏 128K context</div>
            <div class="badge">⚡ Fast inference</div>
        </div>
        <a href="https://huggingface.co/aquigpt/open1-1.5B-Instruct" class="btn">View Model</a>
    </div>
    
  <div class="card">
      <h2>open1-7.5B-Instruct</h2>
      <p>Balanced model providing exceptional performance across diverse tasks with reasonable compute requirements.</p>
      <div style="margin: 16px 0;">
          <div class="badge">🧠 7.5B parameters</div>
          <div class="badge">📏 32K context</div>
          <div class="badge">🎯 High accuracy</div>
      </div>
      <a href="https://huggingface.co/aquigpt/open1-7.5B-Instruct" class="btn">View Model</a>
  </div>
</div>

<div class="callout" style="margin: 28px 0;">
    <h3>🔜 Coming This Week</h3>
    <p><strong>Aqui-open1-4x8B</strong> — Our biggest non-thinking open model, head-to-head against Qwen3 32B and Llama 3.3 70B. Stay tuned for the most capable open model in the series.</p>
</div>

<hr>

<h2>Benchmark Performance</h2>

<h3>1.5B Model Comparison</h3>
<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>open1-1.5B-Instruct</th>
            <th>Llama-3.2-1B-Instruct</th>
            <th>LFM2-1.2B</th>
            <th>Qwen3-1.7B</th>
            <th>Gemma-3-1B-it</th>
            <th>SmolLM2-1.7B-Instruct</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>MMLU</td><td><strong>58.5</strong></td><td>46.6</td><td>55.2</td><td>59.1</td><td>40.1</td><td>42.3</td></tr>
        <tr><td>GPQA</td><td><strong>32.3</strong></td><td>28.8</td><td>31.5</td><td>27.7</td><td>21.1</td><td>22.1</td></tr>
        <tr><td>GSM8K</td><td><strong>62.6</strong></td><td>35.7</td><td>58.3</td><td>51.4</td><td>59.6</td><td>48.2</td></tr>
        <tr><td>IFEval</td><td>72.7</td><td>52.4</td><td><strong>74.9</strong></td><td>74.0</td><td>62.9</td><td>56.7</td></tr>
        <tr><td>MGSM</td><td>59.1</td><td>29.1</td><td>55.0</td><td><strong>66.6</strong></td><td>43.6</td><td>38.5</td></tr>
        <tr style="border-top: 2px solid var(--brand);"><td><strong>Average</strong></td><td><strong>57.0</strong></td><td>38.5</td><td>55.0</td><td>55.8</td><td>45.5</td><td>41.6</td></tr>
    </tbody>
</table>

<h3>7.5B Model Comparison</h3>
<table>
    <thead>
        <tr>
            <th>Benchmark</th>
            <th>open1-7.5B-Instruct</th>
            <th>Llama-3.1-8B-Instruct</th>
            <th>LFM-7B</th>
            <th>Qwen3-8B</th>
            <th>Gemma-3-12B-it</th>
            <th>Nemotron-Nano-9B-v2</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>MMLU</td><td><strong>75.8</strong></td><td>68.7</td><td>69.4</td><td>71.6</td><td>72.5</td><td>74.5</td></tr>
        <tr><td>HumanEval</td><td>82.3</td><td>71.7</td><td>70.1</td><td>84.8</td><td>84.8</td><td><strong>86.2</strong></td></tr>
        <tr><td>GPQA Diamond</td><td><strong>52.2</strong></td><td>25.9</td><td>32.9</td><td>45.2</td><td>34.9</td><td>40.8</td></tr>
        <tr><td>IFEval</td><td>78.9</td><td>77.0</td><td>71.6</td><td>83.4</td><td>81.5</td><td><strong>84.3</strong></td></tr>
        <tr><td>AIME 2025</td><td>18.9</td><td>4.3</td><td>2.1</td><td><strong>20.2</strong></td><td>18.3</td><td>20.1</td></tr>
        <tr style="border-top: 2px solid var(--brand);"><td><strong>Average</strong></td><td><strong>61.6</strong></td><td>49.5</td><td>49.2</td><td>61.0</td><td>58.4</td><td>61.2</td></tr>
    </tbody>
</table>

<hr>

<h2>Key Features</h2>

<div class="grid grid-2">
    <div class="card">
        <h3>🎯 Superior Reasoning</h3>
        <p>Exceptional performance on MMLU, GPQA, and mathematical reasoning tasks, outperforming models of similar and larger sizes.</p>
    </div>
    
  <div class="card">
      <h3>⚡ Optimized Architecture</h3>
      <p>Efficient transformer design enabling fast inference while maintaining high accuracy across diverse benchmarks.</p>
  </div>
  
  <div class="card">
      <h3>🌍 Multilingual Support</h3>
      <p>Trained on 20+ languages with robust performance across linguistic boundaries and cultural contexts.</p>
  </div>
  
  <div class="card">
      <h3>🔓 MIT Licensed</h3>
      <p>Complete freedom for commercial use, modification, and redistribution with minimal restrictions.</p>
  </div>
</div>

<hr>

<h2>Usage</h2>

<div class="codeblock">
  <pre>
    from transformers import AutoTokenizer, AutoModelForCausalLM
    
    # Load the model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("aquigpt/open1-1.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("aquigpt/open1-1.5B-Instruct")
    
    # Generate text
    inputs = tokenizer("Explain quantum computing:", return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200, temperature=0.7)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
  </pre>
</div>

<details>
    <summary>Training Details</summary>
    <p>The open1 models were trained from scratch on a diverse, high-quality dataset spanning code, mathematics, reasoning, and multilingual text. Training utilized advanced techniques including:</p>
    <ul>
        <li>Supervised fine-tuning on instruction-following data</li>
        <li>Constitutional AI for alignment and safety</li>
        <li>Advanced attention mechanisms for extended context</li>
        <li>Multi-stage training with curriculum learning</li>
    </ul>
</details>

<blockquote>
    <strong>Note:</strong> These models are designed for research and commercial applications. While they demonstrate strong performance, users should conduct appropriate testing for their specific use cases.
</blockquote>

<div style="text-align: center; margin-top: 40px; color: var(--muted);">
    <p>Built with ❤️ by the Aqui team • MIT • September 2025</p>
</div>