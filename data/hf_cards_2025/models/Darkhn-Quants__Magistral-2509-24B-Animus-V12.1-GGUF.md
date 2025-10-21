---
license: apache-2.0
base_model:
- Darkhn/Magistral-2509-24B-Animus-V12.1
tags:
- magistral
- mistral
- finetune
- roleplay
- chat
- wings-of-fire
- reasoning
- thinking
- nsfw
- not-for-all-audiences
---

<style>
body {
  font-family: 'Quicksand', sans-serif;
  background: linear-gradient(135deg, #4a1e00 0%, #1c0a00 100%);
  color: #F5EFE6;
  margin: 0;
  padding: 0;
  font-size: 16px;
}

h1, h2, h3, h4, summary {
    font-family: 'Cinzel', serif;
}

.container {
  margin: 20px auto;
  max-width: 900px;
  background-color: rgba(28, 22, 18, 0.95);
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(255, 140, 0, 0.15);
  border: 1px solid rgba(255, 140, 0, 0.2);
  outline: 1px solid rgba(255, 140, 0, 0.5);
  outline-offset: -1px;
  position: relative;
}

.container::before {
  content: '';
  position: absolute;
  top: -1px;
  left: -1px;
  right: -1px;
  bottom: -1px;
  border: 1px solid rgba(255, 165, 0, 0.98);
  border-radius: 12px;
  pointer-events: none;
  animation: borderGlow 2.5s ease-in-out infinite;
}

@keyframes borderGlow {
  0% {
    box-shadow: 0 0 5px rgba(255, 165, 0, 0.98);
  }
  50% {
    box-shadow: 0 0 12px rgba(255, 165, 0, 0.98);
  }
  100% {
    box-shadow: 0 0 5px rgba(255, 165, 0, 0.98);
  }
}

.header h1 {
  font-size: 32px;
  color: #FFA500;
  margin: 0 0 20px 0;
  text-align: center;
  text-shadow: 0 0 12px rgba(255, 100, 0, 0.6);
}

.info img {
  width: 100%;
  max-width: 700px;
  display: block;
  margin: 0 auto 25px auto;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(255, 140, 0, 0.25);
  border: 1px solid rgba(255, 140, 0, 0.2);
  outline: 1px solid rgba(255, 140, 0, 0.5);
  outline-offset: -1px;
}

a {
  color: #FFD700;
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: #FFDAB9;
}

.button {
  display: inline-block;
  background-color: #E55B00;
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  transition: all 0.3s ease;
  border: 1px solid transparent;
}

.button:hover {
  background-color: #FF8C00;
  box-shadow: 0 0 15px rgba(255, 140, 0, 0.5);
  transform: translateY(-2px);
}

pre {
  background-color: rgba(45, 35, 25, 0.95);
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
  border: 1px solid rgba(255, 140, 0, 0.2);
  outline: 1px solid rgba(255, 140, 0, 0.5);
  outline-offset: -1px;
}

code {
  font-family: 'Courier New', monospace;
  color: #F5EFE6;
}

.section-container {
  margin: 40px 0;
}

h2 {
    font-size: 26px;
    color: #FFA500;
    text-shadow: 0 0 10px rgba(255, 140, 0, 0.5);
    border-bottom: 1px solid rgba(255, 140, 0, 0.2);
    padding-bottom: 10px;
    margin-bottom: 20px;
}

.info-card {
  background: rgba(45, 35, 25, 0.95);
  border: 1px solid rgba(255, 140, 0, 0.2);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 25px;
}

.info-header {
  background: rgba(255, 140, 0, 0.1);
  padding: 20px;
  border-bottom: 1px solid rgba(255, 140, 0, 0.2);
}

.info-header h3 {
  color: #FFA500;
  margin: 0 0 10px 0;
  font-size: 22px;
  text-shadow: 0 0 5px rgba(255, 140, 0, 0.3);
}

.model-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.model-tag {
  background: rgba(218, 165, 32, 0.15);
  color: #FFD700;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  border: 1px solid rgba(218, 165, 32, 0.3);
  font-family: 'Quicksand', sans-serif;
}

.card-content {
  padding: 20px;
  line-height: 1.7;
}

.card-content p, .card-content li {
    margin-bottom: 1em;
}

.card-content p:last-child, .card-content li:last-child {
    margin-bottom: 0;
}

.card-content ul {
    list-style: none;
    padding-left: 20px;
}

.card-content li::before {
    content: '✦';
    color: #FFD700;
    font-weight: bold;
    display: inline-block;
    width: 1em;
    margin-left: -1.2em;
    font-size: 1.2em;
    line-height: 1;
}

.card-content strong {
    color: #FFD700;
    font-weight: 600;
}

.config-container {
  background: rgba(45, 35, 25, 0.95);
  border: 1px solid rgba(255, 140, 0, 0.2);
  border-radius: 8px;
  overflow: hidden;
}

.config-header {
  background: rgba(255, 140, 0, 0.1);
  padding: 15px 20px;
  border-bottom: 1px solid rgba(255, 140, 0, 0.2);
}

.config-header h3 {
    margin: 0;
    color: #FFA500;
    font-size: 22px;
}

.config-content {
  padding: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.config-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.config-label {
  color: #FFD700;
  font-size: 14px;
  font-weight: 500;
  font-family: 'Quicksand', sans-serif;
}

.config-value {
  color: #F5EFE6;
  font-family: 'Courier New', monospace;
  font-size: 18px;
  font-weight: bold;
}

.link-arrow {
  display: inline-block;
  transition: transform 0.3s ease;
}

a:hover .link-arrow {
  transform: translateX(3px);
}

.support-section {
    text-align: center;
    margin-top: 40px;
    background: rgba(45, 35, 25, 0.95);
    border: 1px solid rgba(255, 140, 0, 0.2);
    border-radius: 8px;
    padding: 20px;
}

.support-section p {
    margin-bottom: 15px;
    font-size: 1.1em;
    margin-top: 0;
}

summary {
    cursor: pointer;
    list-style: none;
    outline: none;
    display: flex;
    align-items: flex-start;
}
summary::-webkit-details-marker {
    display: none;
}
summary::before {
    content: '▶';
    font-size: 1.2em;
    color: #FFA500; /* Match h2 color */
    margin-right: 15px;
    padding-top: 5px; /* Adjust vertical alignment with h2 text */
    transition: transform 0.2s ease;
    flex-shrink: 0; /* Prevent the arrow from shrinking */
}
details[open] > summary::before {
    transform: rotate(90deg);
}
summary > h2 {
    flex-grow: 1;
}

.format-list {
  margin: 1.5em 0;
}

.format-list dt {
  color: #FFA500;
  font-family: 'Cinzel', serif;
  font-weight: 600;
  font-size: 1.3em;
  text-shadow: 0 0 8px rgba(255, 140, 0, 0.5);
  margin-bottom: 0.6em;
}

.format-list dd {
  margin-left: 0;
  margin-bottom: 1.5em;
  background-color: rgba(28, 22, 18, 0.95); 
  padding: 12px 15px;
  border-radius: 6px;
  border: 1px solid rgba(255, 140, 0, 0.2);
  border-left: 4px solid #FFA500; 
}

.format-list dd:last-of-type {
  margin-bottom: 0;
}
</style>
<div class="container">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Quicksand:wght@400;500&display=swap" rel="stylesheet">
<div class="header">
  <h1>Magistral-Animus-V12.1-GGUF</h1>
</div>
<div class="info">
  <img src="HGJ29YDAVWDBRKSAZAR6JTJGG0.jpeg" alt="Wings_of_Fire" width="700">

  <div class="support-section">
    <p><strong>Send me your support to help me feed the data beast! also taking comissions for universe specific models</strong></p>
    <a href="https://ko-fi.com/som1tokmynam" target="_blank" class="button">
      Support on Ko-fi
    </a>
  </div>

<div class="section-container">
    <details open>
        <summary><h2>Important: Reasoning Format & Backend Setup</h2></summary>
        <div class="info-card">
            <div class="card-content">
                <p>This model uses a special reasoning format. There are two methods to enable it: the <strong>official format</strong> designed by MistralAI, and a <strong>legacy format</strong> that works due to the base model's pre-training. The correct method depends on your backend software (e.g., llama.cpp, Kobold.cpp).</p>
                <hr>
                <h3>Official Format: <code>[THINK]</code> (Recommended for llama.cpp)</h3>
                <p>This is the official instruction format from MistralAI and is the recommended method. It is confirmed to work with backends like <strong>llama.cpp</strong> (with specific flags) and <strong>mistral-common</strong>.</p>
                <ul>
                    <li><strong>Llama.cpp Prerequisite:</strong> Launch llama.cpp with the <code>--special</code> and <code>--jinja</code> arguments enabled.</li>
                    <li><strong>Instruction Format:</strong> The model uses <code>[THINK]</code> and <code>[/THINK]</code> tags.</li>
                    <li><strong>Activation (2 steps):</strong>
                        <ol>
                            <li>Set your prefill sequence (in your frontend like SillyTavern) to start with <code>[THINK]</code>.</li>
                            <li>You <strong>must</strong> also include the keyword <code>/think</code> anywhere in your system prompt to activate the reasoning module.</li>
                        </ol>
                    </li>
                </ul>
                <h4>Recommended System Prompt for Official Format</h4>
                <p>Add the following to your system prompt to guide the model's output structure:</p>
                <pre><code>First draft your thinking process (inner monologue) until you arrive at a response. You must use the /think keyword. Format your response using Markdown, and use LaTeX for any mathematical equations. Write both your thoughts and the response in the same language as the input. Your thinking process must follow the template below:[THINK]Your thoughts or/and draft, like working through an exercise on scratch paper. Be as casual and as long as you want until you are confident to generate the response. Use the same language as the input.[/THINK]Here, provide a self-contained response.</code></pre>
                <h4>SillyTavern Quick Setup</h4>
                <p>For a complete SillyTavern configuration, you can download and import this JSON file:</p>
                <a href="https://huggingface.co/Darkhn/Sampler_settings_and_system_prompt/blob/main/Magistral_SillyTavern_settings.json" target="_blank" class="button">
                    Download SillyTavern JSON <span class="link-arrow">→</span>
                </a>
                <hr>
                <h3>Legacy Format: <code>&lt;think&gt;</code> (For Kobold.cpp & TabbyAPI)</h3>
                <p>This format is not official but is highly effective with backends like <strong>Kobold.cpp</strong> and <strong>TabbyAPI</strong>. It works because the model's predecessor was trained on these angle-bracket tags, and the model inherits this behavior.</p>
                <ul>
                    <li><strong>Instruction Format:</strong> Wrap the model's reasoning in <code>&lt;think&gt;</code> and <code>&lt;/think&gt;</code> tags.</li>
                    <li><strong>Activation:</strong> In your frontend, set your prefill sequence to start with <code>&lt;think&gt;</code>.</li>
                </ul>
                <p>
                    <a href="https://github.com/LostRuins/koboldcpp/issues/1745" target="_blank" class="button">
                        See the GitHub Issue for technical details <span class="link-arrow">→</span>
                    </a>
                </p>
            </div>
        </div>
    </details>
</div>

<div class="section-container">
  <details>
    <summary><h2>Quantized Models</h2></summary>
    <div class="info-card">
      <div class="card-content">
        <p>The quantized model files are available for download. Click the buttons below to view the files.</p>
        <a href="https://huggingface.co/Darkhn/Magistral-2509-24B-Animus-V12.1-EXL2" target="_blank" class="button">
          Download EXL2 Files <span class="link-arrow">→</span>
        </a>
        <a href="https://huggingface.co/ArtusDev/Darkhn_Magistral-2509-24B-Animus-V12.1-EXL3" target="_blank" class="button">
          Download EXL3 Files <span class="link-arrow">→</span>
        </a>
      </div>
    </div>
  </details>
</div>

  <div class="section-container">
    <details>
      <summary><h2>Character Card & Lore Book</h2></summary>
      <div class="info-card">
        <div class="card-content">
          <p>For the best roleplaying experience, it is highly recommended to use the provided character card and lore book. These files help guide the model's persona and provide rich, in-universe context.</p>
          <a href="https://huggingface.co/Darkhn/Sampler_settings_and_system_prompt/tree/main/character_card" target="_blank" class="button">
            Download Files <span class="link-arrow">→</span>
          </a>
        </div>
      </div>
    </details>
  </div>

  <div class="section-container">
    <details>
      <summary><h2>Sampler Presets</h2></summary>
      <div class="info-card">
        <div class="card-content">
          <p>For a seamless setup in SillyTavern, you can download the pre-configured JSON file linked in the "Reasoning & Usage" section above.</p>
          <p>For those that dont use SillyTavern, the recommended sampler settings are:</p>
          <ul>
              <p><strong>Temp:</strong> 1.0</p>
              <p><strong>Min P:</strong> 0.02</p>
          </ul>
        </div>
      </div>
    </details>
  </div>
  
  <div class="section-container">
    <details open>
        <summary>
            <h2>Roleplay Format Guide</h2>
        </summary>
        <div class="info-card">
            <div class="card-content">
                <p>For the best results, use this structured format. This helps the AI clearly distinguish between actions, inner thoughts, and dialogue.</p>
                <dl class="format-list">
                    <dt>Actions / Descriptions</dt>
                    <dd><code>*He walked across the room and stared out the window.*</code></dd>
                    <dt>Inner Thoughts</dt>
                    <dd><code>*-I wonder what she's thinking.-*</code></dd>
                    <dt>Dialogue</dt>
                    <dd><code>Alex (Curious): "What do you see out there?"</code></dd>
                </dl>
                <p>Standard novel-style formatting is also understood, but this structured format is preferred for clarity.</p>
            </div>
        </div>
    </details>
  </div>

  <div class="section-container">
    <details open>
      <summary><h2>Model Description</h2></summary>
      <div class="info-card">
        <div class="card-content">
          <p>This is <strong>Version 12.1</strong>, an experimental model in the Animus series built with a new focus on reasoning. V12.1 is a direct fine-tune of <strong>Darkhn/Magistral-Small-2509-Text-Only</strong> (a text-only modification of `mistralai/Magistral-Small-2509`).</p>
		  <p>V12.1's strength comes from a novel dataset designed to teach the model the <em>why</em> behind the lore, not just the <em>what</em>. The training data is a mix of:</p>
            <ul>
                <li><strong>A 3,000-example Q&A dataset:</strong> This data is framed as an in-character study session, like a student at Jade Mountain Academy learning about the history, relationships, and politics of Pyrrhia's tribes. This provides a deep, contextual understanding of the universe.</li>
                <li><strong>A 3,000-example uncensored roleplay dataset:</strong> The same high-quality, mature roleplay scenarios used in previous versions, ensuring the model maintains its engaging and dynamic narrative capabilities.</li>
                <li><strong>900 roleplay reasoning examples:</strong> These new examples are designed to teach the model how to "think" through its responses using a special format, improving coherence and logical flow.</li>
            </ul>
          <p>The result is a model with <strong>exceptionally strong prose and a deep grasp of in-universe lore</strong>, making for a highly immersive and accurate roleplaying experience.</p>
		  <p>Note for roleplay, it follows system prompt and first message, meaning if the first assistant message is short, the following messages will be short.</p>
        </div>
      </div>
    </details>
  </div>
  
  <div class="section-container">
    <details open>
      <summary><h2>Training Details</h2></summary>
      <div class="info-card">
          <div class="info-header">
              <h3>V12.1 Training Process</h3>
          </div>
          <div class="card-content">
              <p>V12.0 marks a shift from model merging to a focused, direct fine-tuning approach. This allows for greater control over the final model's characteristics.</p>
              <ul>
                  <li><strong>Base Model:</strong> Darkhn/Magistral-Small-2509-Text-Only</li>
                  <li><strong>Hardware:</strong> 1x NVIDIA H200</li>
                  <li><strong>Training Time:</strong> 8 hours</li>
                  <li><strong>Epochs:</strong> 2</li>
                  <li><strong>LoRA Rank:</strong> 128</li>
				  <li><strong>Context size</strong> 8192</li>
                  <li><strong>Scheduler:</strong> Cosine</li>
              </ul>
          </div>
      </div>
      <div class="info-card">
        <div class="info-header">
            <h3>Feature Update: Removal of DM Choices</h3>
        </div>
        <div class="card-content">
            <p>A key feature in previous test versions—the presentation of multiple-choice actions (e.g., A, B, C) to guide the user—has been <strong>removed</strong>.</p>
            <p>While a promising concept, this feature needs further refinement to ensure it enhances, rather than restricts, the roleplaying experience. It may be reintroduced in a more polished form in a future release. For now, the model returns to a more traditional, open-ended prose format.</p>
        </div>
    </div>
      <div class="info-card">
          <div class="info-header">
              <h3>Training Dataset</h3>
          </div>
          <div class="card-content">
              <p>The V12.1 dataset consists of <strong>6,900 high-quality examples</strong>, a combination of three distinct types:</p>
              <ul>
                  <li><strong>In-Character Q&A (3,000 examples):</strong> This new dataset simulates a student at Jade Mountain Academy studying the world's lore. It's composed of roleplay-style questions and answers covering tribe history, family dynamics, and political relationships. This method builds a foundational, interconnected understanding of the lore.</li>
                  <li><strong>Uncensored Roleplay (3,000 examples):</strong> This is the same mature, canon-centric dataset refined for previous versions. It explores pivotal "what-if" scenarios from the books using only canon characters, ensuring the model can handle complex and dramatic narratives.</li>
                  <li><strong>Roleplay Reasoning (900 examples):</strong> This new dataset Tunes the Reasoning for roleplaying before generating prose.</li>
              </ul>
              <p>Both datasets underwent a rigorous cleaning process to remove formatting artifacts, such as <code>**scene transitions**</code>, resulting in a cleaner and more natural narrative style.</p>
          </div>
      </div>
    </details>
  </div>
  
  <div class="section-container">
    <details>
      <summary><h2>Intended Use & Limitations</h2></summary>
      <div class="info-card">
          <div class="card-content">
              <ul>
                  <li><strong>Intended Use:</strong> The primary purpose of this model is for creative and roleplaying within the <em>Wings of Fire</em> universe. However, user feedback indicates it is also highly effective for general-purpose roleplaying.</li>
                  <li><strong>Limitations & Quirks:</strong>
                      <ul>
                          <li>Performance on tasks outside of its training domain (general knowledge, coding, etc.) is not guaranteed and will likely be poor.</li>
                          <li><strong>Versatility:</strong> While it appears to be only a <em>Wings of Fire</em> tuned model, users have reported it is very capable of performing normal roleplay with other settings and characters.</li>
                          <li>The model may "hallucinate" or generate plausible but non-canonical information, especially when pushed outside the established "what-if" scenarios.</li>
                          <li><strong>Content:</strong> The training data includes mature and darker themes from the <em>Wings of Fire</em> series, such as conflict, character death, and moral ambiguity. The model is capable of generating content reflecting these themes. As always, it is up to the user what they do with it.</li>
                          <li><strong>Formatting:</strong> Training data was cleaned to remove narrative artifacts like <code>**scene transitions**</code>. The model should now produce cleaner prose.</li>
                          <li><strong>Safety:</strong> This model has not undergone additional safety alignment beyond what was included in its base model. Standard responsible AI practices should be followed.</li>
                      </ul>
                  </li>
              </ul>
          </div>
      </div>
    </details>
  </div>

  <div class="section-container">
    <details>
      <summary><h2>Acknowledgements</h2></summary>
      <div class="info-card">
          <div class="card-content">
              <ul>
                  <li>Credit to the Mistral for the powerful Magistral architecture.</li>
                  <li>Credit to Google for the Gemini Pro model, used in dataset generation.</li>
              </ul>
          </div>
      </div>
    </details>
  </div>

</div>
</div>