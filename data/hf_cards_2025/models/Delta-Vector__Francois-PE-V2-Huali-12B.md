---
base_model:
- Delta-Vector/Francois-PE
library_name: transformers
tags:
- fine-tuning
- prose
- KTO
- axolotl
- finetune
- roleplaying
- creative-writing
datasets:
- PocketDoc/Dans-Personamaxx-VN
- NewEden/LIMARP-Complexity
- NewEden/PIPPA-Mega-Filtered
- NewEden/OpenCAI-ShareGPT
- NewEden/Creative_Writing-Complexity
- NewEden/Light-Novels-Roleplay-Logs-Books-Oh-My-duplicate-turns-removed
- PocketDoc/Dans-Failuremaxx-Adventure-3
- NewEden/Books-V2-ShareGPT
- NewEden/Deepseek-V3-RP-Filtered
- NewEden/BlueSky-10K-Complexity
- NewEden/Final-Alpindale-LNs-ShareGPT
- NewEden/DeepseekRP-Filtered
- NewEden/RP-logs-V2-Experimental
- anthracite-org/kalo_opus_misc_240827
- anthracite-org/kalo_misc_part2
- NewEden/vanilla-backrooms-claude-sharegpt
- NewEden/Storium-Prefixed-Clean
- NewEden/KTO-IF-Dans
- NewEden/KTO-Instruct-Mix
- NewEden/Opus-accepted-hermes-rejected-shuffled
---
<style>
body {
  font-family: 'Quicksand', sans-serif;
  background: linear-gradient(135deg, #f9ffd1 0%, #e2fab5 100%);
  color: #000000;
  margin: 0;
  padding: 0;
  font-size: 16px;
}
.container {
  margin: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 3px solid #000000;
  position: relative;
}
.header h1 {
  font-size: 28px;
  color: #000000;
  margin: 0 0 20px 0;
  text-align: center;
  text-decoration: underline;
}
.section {
  margin-top: 30px;
}
.section h2 {
  font-size: 24px;
  color: #000000;
  text-align: center;
  text-decoration: underline;
}
.info p {
  color: #000000;
  line-height: 1.6;
  font-size: 16px;
}
.info img {
  width: 85%;
  border-radius: 10px;
  margin: 0 auto 15px;
  display: block;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
  border: 1px solid #000000;
}
a {
  color: #000000;
  text-decoration: none;
  transition: color 0.2s ease;
}
a:hover {
  color: #538125;
}
.button {
  display: inline-block;
  background-color: rgba(106, 168, 79, 0.8);
  color: #000000;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}
.button:hover {
  background-color: #538125;
  box-shadow: 0 0 15px rgba(106, 168, 79, 0.5);
}
pre {
  background-color: rgba(240, 248, 225, 0.95);
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
  border: 1px solid #000000;
}
code {
  font-family: 'Courier New', monospace;
  color: #000000;
}
.info-card {
  background: rgba(249, 255, 235, 0.95);
  border: 1px solid #000000;
  border-radius: 8px;
  overflow: hidden;
}
.info-header {
  background: rgba(106, 168, 79, 0.1);
  padding: 20px;
  border-bottom: 1px solid #000000;
}
.info-header h3 {
  color: #000000;
  margin: 0 0 10px 0;
  font-size: 20px;
  text-align: center;
  text-decoration: underline;
}
.model-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.model-tag {
  background: rgba(106, 168, 79, 0.1);
  color: #000000;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  border: 1px solid #000000;
}
.model-composition {
  padding: 20px;
  border-bottom: 1px solid #000000;
}
.model-composition h4 {
  color: #000000;
  margin: 0 0 15px 0;
  font-size: 16px;
  text-align: center;
  text-decoration: underline;
}
.composition-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 10px;
}
.composition-list li {
  color: #000000;
  display: flex;
  align-items: baseline;
  gap: 8px;
}
.model-component {
  font-weight: 500;
  min-width: 120px;
}
.model-description {
  padding: 20px;
  background: rgba(255, 255, 255, 0.5);
}
.metrics-section {
  margin-bottom: 30px;
}
.metrics-section details {
  background: rgba(249, 255, 235, 0.95);
  border: 1px solid #000000;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
}
.metrics-section summary {
  color: #000000;
  font-size: 18px;
  cursor: pointer;
  outline: none;
  padding: 5px 0;
  text-align: center;
}
.creator-section {
  margin: 20px 0;
}
.creator-badge {
  display: inline-flex;
  align-items: center;
  background: rgba(249, 255, 235, 0.95);
  border: 1px solid #000000;
  border-radius: 8px;
  padding: 10px 15px;
}
.creator-label {
  color: #000000;
  font-size: 14px;
  margin-right: 8px;
}
.creator-link {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #000000;
  text-decoration: none;
  transition: all 0.2s ease;
}
.creator-name {
  font-weight: 600;
}
.creator-arrow {
  font-size: 16px;
  transition: transform 0.2s ease;
}
.creator-link:hover .creator-arrow {
  transform: translateX(3px);
}
.link-arrow {
  display: inline-block;
  transition: transform 0.2s ease;
}
a:hover .link-arrow {
  transform: translateX(3px);
}
.axolotl-container {
  text-align: center;
  margin: 30px 0;
}
.axolotl-container img {
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  border: 1px solid #000000;
}
</style>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>François-Huali 12B</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>François-PE-Huali 12B</h1>
    </div>
    <div class="info">
      <img src="https://cdn-uploads.huggingface.co/production/uploads/66c26b6fb01b19d8c3c2467b/qUdM9qgZWeyfxwdds9QRZ.jpeg" alt="Model banner">
      <div style="text-align: center;">
      <div class="creator-section">
        <div class="creator-badge">
          <span class="creator-label">Created by</span>
          <a href="https://huggingface.co/Delta-Vector" target="_blank" class="creator-link">
            <span class="creator-name">Delta-Vector</span>
            <span class="creator-arrow">→</span>
          </a>
        </div>
      </div>
      <div class="model-info">
        <h2>Model Information</h2>
        <div class="info-card">
          <div class="info-header">
            <h3>François-Huali 12B V2</h3>
            <div class="model-tags">
              <span class="model-tag">KTO enhanced</span>
              <span class="model-tag">Dans-Personality-Engine finetune</span>
              <span class="model-tag">Creative & Refreshing Prose</span>
            </div>
          </div>
          <div class="model-description">
            <p>A sequel! A sequel to my Francois-PE/Huali train, Built ontop of Dans-PE-12B that was finetuned with Light novels, Books, Roleplay logs, to change writing style to be rather short & sweet, Huali uses KTO to increase coherency and prose. The model aims to have a different style of writing/prose then any other NeMo train.</p>
          </div>
        </div>
      </div>
      <div class="section">
        <h2>Quantized Versions</h2>
        <div class="info-card">
          <div class="model-composition">
            <h4>Available Downloads</h4>
            <ul class="composition-list">
              <li><span class="model-component"><a href="" target="_blank">GGUF Format</a></span>For use with LLama.cpp & Forks(Coming Soon!)</li>
              <li><span class="model-component"><a href="https://huggingface.co/models?other=base_model:quantized:Delta-Vector%2FFrancois-PE-V2-Huali-12B&sort=trending&search=exl" target="_blank">EXL2 Format</a></span>For use with TabbyAPI (Thanks Auri <3)</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="section">
        <h2>Prompting</h2>
        <p>Model has been tuned with the ChatML formatting. A typical input would look like this:</p>
        <pre><code>"""&lt;|im_start|&gt;user
Hi there!&lt;|im_end|&gt;
&lt;|im_start|&gt;assistant
Nice to meet you!&lt;|im_end|&gt;
&lt;|im_start|&gt;user
Can I ask a question?&lt;|im_end|&gt;
&lt;|im_start|&gt;assistant
"""</code></pre>
      </div>
      <div class="section">
        <h2>System Prompting</h2>
        <p>I would highly recommend using either Euryale's system prompt or the EVA system prompt with the model.</p>
        <div class="metrics-section">
          <details>
            <summary>See Sao10k's Euryale System Prompt</summary>
            <pre><code>Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.
&lt;Guidelines&gt;
• Maintain the character persona but allow it to evolve with the story.
• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.
• All types of outputs are encouraged; respond accordingly to the narrative.
• Include dialogues, actions, and thoughts in each response.
• Utilize all five senses to describe scenarios within {{char}}'s dialogue.
• Use emotional symbols such as "!" and "~" in appropriate contexts.
• Incorporate onomatopoeia when suitable.
• Allow time for {{user}} to respond with their own input, respecting their agency.
• Act as secondary characters and NPCs as needed, and remove them when appropriate.
• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.
&lt;/Guidelines&gt;

&lt;Forbidden&gt;
• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.
• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.
• Repetitive and monotonous outputs.
• Positivity bias in your replies.
• Being overly extreme or NSFW when the narrative context is inappropriate.
&lt;/Forbidden&gt;

Follow the instructions in &lt;Guidelines&gt;&lt;/Guidelines&gt;, avoiding the items listed in &lt;Forbidden&gt;&lt;/Forbidden&gt;.</code></pre>
          </details>
        </div>
      </div>
      <div class="section">
        <h2>Training</h2>
        <p>The training was done for 1 epoch using 8 x <a href="https://www.nvidia.com/en-us/data-center/h200/">H200s</a> GPUs graciously provided by <a href="https://huggingface.co/kalomaze">Kalomaze</a> for the fine-tuning of the model.</p>
        <p style="text-align: center; margin-top: 20px;">
<div class="axolotl-container">
  <a href="https://github.com/OpenAccess-AI-Collective/axolotl" target="_blank">
    <img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl">
  </a>
</div>
      <div class="section">
        <h2>Credits</h2>
        <p>Thank you to <a href="https://huggingface.co/lucyknada">Lucy Knada</a>, <a href="https://huggingface.co/Ateron">Ateron</a>, <a href="https://huggingface.co/AliCat2">Alicat</a>, <a href="https://huggingface.co/intervitens">Intervitens</a>, <a href="https://huggingface.co/cgato">Cgato</a>, <a href="https://huggingface.co/kubernetes-bad">Kubernetes Bad</a> and the rest of <a href="https://huggingface.co/anthracite-org">Anthracite</a>.</p>
      </div>
    </div>
  </div>