---
base_model:
- Retreatcost/Irix-mpf-stock
- Retreatcost/Forgotten-directive-Neon-stock
- Retreatcost/Lorablated-w2bb-psy-della
- yamatazen/EtherealAurora-12B-Lorablated
- Retreatcost/Shisa-K-sakurization
- Sicarius-Prototyping/Impish_Longtail_12B
- SuperbEmphasis/MN-12b-RP-Ink-RP-Longform
- mistralai/Mistral-Nemo-Base-2407
library_name: transformers
tags:
- mergekit
- merge
- not-for-all-audiences
- nsfw
license: apache-2.0
language:
- en
model-index:
- name: Retreatcost/KansenSakura-Erosion-RP-12b
  results:
  - task:
      type: text-generation
      name: UGI score
    metrics:
    - name: UGI
      type: ugi
      value: 30.49
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: W/10 Score
    metrics:
    - name: W/10
      type: willingness
      value: 6.2
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: NatInt Score
    metrics:
    - name: NatInt
      type: natint
      value: 27.39
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: Writing Score
    metrics:
    - name: Writing
      type: writing
      value: 37.82
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: NSFW score
    metrics:
    - name: NSFW
      type: nsfw
      value: 6.0
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
  - task:
      type: text-generation
      name: Dark score
    metrics:
    - name: Dark
      type: dark
      value: 5.8
    source:
      name: UGI Leaderboard
      url: https://huggingface.co/spaces/DontPlanToEnd/UGI-Leaderboard
---
# **KansenSakura-Erosion-RP-12b**
<style>
.container {
    display: flex;
    flex-grow: 1;
    justify-content: center;
  }
  h1 {
    margin-bottom: 30px;
  }

  /* Book Styling */
  .book {
      width: 332px;
      height: 486px;
      position: relative;
      perspective: 1200px;
      margin: 0 auto;
      margin-left: 50%;
  }

  .page {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      transform-style: preserve-3d;
      transform-origin: left center;
      transition: all 0.7s cubic-bezier(0.645, 0.045, 0.355, 1);
      border-radius: 5px 0 0 5px;
  }

  .front, .back {
      position: absolute;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      backface-visibility: hidden;
      border-radius: 5px 0 0 5px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 15px;
      font-size: 14px;
      box-sizing: border-box;
      box-shadow: inset 0 0 10px rgba(0,0,0,0.1);
  }

  .front {
      background: linear-gradient(to right, #fefefe 95%, #f0f0f0 100%);
  }

  .back {
      background: #f9f9f9;
      transform: rotateY(180deg);
  }

  /* Page Content Styling */
  .page-content {
      width: 100%;
      height: 100%;
      overflow: hidden;
      text-align: left;
  }
  .page-number {
      position: absolute;
      bottom: 10px;
      font-size: 12px;
      color: #777;
  }
  .front .page-number {
      right: 15px;
  }
  .back .page-number {
      left: 15px;
  }

  /* Cover Styling */
  .cover {
    background-image: url('https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/F34iK8guTPplwEBCdwDAk.png');
    background-size: cover;
    background-repeat: no-repeat;
  }

  /* Hide radio buttons */
  input[type="radio"] {
      display: none;
  }

  .page.cover {
    transform: rotateY(-180deg);
    z-index: 0;
  }

  .page.page2 {
    transform: rotateY(0deg);
    z-index: 3;
  }

  .page.page3 {
    transform: rotateY(0deg);
    z-index: 2;
  }

  /* When cover radio is selected, show front cover */
  #cover-radio:checked ~ .book .page.cover {
    transform: rotateY(0deg);
    z-index: 4;
  }
  
  /* When page1 radio is selected, turn cover to table of contents and show page1 */
  #page1-radio:checked ~ .book .page.cover {
    transform: rotateY(-180deg);
    z-index: 0;
  }
  
  /* When page2 radio is selected, turn page1 and show page2 */
  #page2-radio:checked ~ .book .page.cover {
    transform: rotateY(-180deg);
    z-index: 0;
  }

  #page2-radio:checked ~ .book .page.page2 {
    transform: rotateY(-180deg);
    z-index: 1;
  }
  
  /* When page3 radio is selected, turn page2 and show page3 */
  #page3-radio:checked ~ .book .page.cover {
      transform: rotateY(-180deg);
      z-index: 0;
  }
  #page3-radio:checked ~ .book .page.page2 {
      transform: rotateY(-180deg);
      z-index: 1;
  }
  #page3-radio:checked ~ .book .page.page3 {
      transform: rotateY(-180deg);
      z-index: 2;
  }

  #page2-radio:checked ~ .book .page.cover {
      transition-delay: 0.1s;
  }

  #page2-radio:checked ~ .book .page.page2 {
      transition-delay: 0.2s;
  }

  #page2-radio:checked ~ .book .page.page3 {
      transition-delay: 0.2s;
  }

  #page3-radio:checked ~ .book .page.page2 {
      transition-delay: 0.1s;
  }

  #page3-radio:checked ~ .book .page.page3 {
      transition-delay: 0.2s; /* Slightly longer delay for the 3rd page */
  }

  #cover-radio:checked ~ .book .page.cover {
      transition-delay: 0.3s; /* Slightly longer delay for the 3rd page */
  }

  #cover-radio:checked ~ .book .page.page2 {
      transition-delay: 0.2s;
  }

  #cover-radio:checked ~ .book .page.page3 {
      transition-delay: 0.1s;
  }

  #page1-radio:checked ~ .book .page.page2 {
      transition-delay: 0.2s;
  }

  #page1-radio:checked ~ .book .page.page3 {
      transition-delay: 0.1s;
  }

  /* Control Dots */
  .slider-controls {
      margin-top: 30px;
      display: flex;
      justify-content: center;
      gap: 15px;
  }
  .slider-controls label {
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #bdc3c7;
      cursor: pointer;
      transition: background 0.3s;
  }
  .slider-controls label:hover {
      background: #7f8c8d;
  }
  
  /* Back cover styling */
  .back-cover {
      background: #2c3e50;
  }

  .cover-back {
      background: #2c3e50;
  }

  blockquote {
    font-size: 14px;
    padding: 0px;
    padding-left: 7px;
    margin: 0px;
    margin-bottom: 4px;
  }

  .page-theme-black {
    color: white;
    background: #000000;
    background: linear-gradient(0deg,rgba(0, 0, 0, 1) 0%, rgba(33, 37, 40, 1) 75%, rgba(89, 73, 82, 1) 86%, rgba(33, 37, 40, 1) 95%);
  }

  .page-theme-black h2 {
    color: white;
  }

  .page-theme-black i {
    color: #F7D9BC;
  }

  .page-theme-violet {
    color: white;
    background: #6d2dad;
    background: radial-gradient(circle,rgba(109, 45, 173, 1) 0%, rgba(0, 0, 0, 1) 100%);
  }

  .page-theme-violet h2 {
    color: #9d3ffb;
  }

  .page-theme-violet div {
    color: #C9CFD5;
  }

  .page-theme-violet b {
    color: white;
  }

  .page-theme-subtle {
    background: #e8acac;
    background: linear-gradient(90deg,rgba(232, 172, 172, 1) 0%, rgba(154, 193, 230, 1) 100%);
    color: black;
  }

  .page-theme-subtle h2 {
    color: black;
  }

  .page-theme-subtle li::marker {
    color: #C72020;
  }

  .page-theme-subtle span {
    color: #2A2F34;
  }

  .page-theme-subtle b {
    color: black;
  }

  .page-theme-subtle .page-number {
    color: black;
  }

  .page-theme-blue {
    background: #090979;
    background: radial-gradient(circle,rgba(9, 9, 121, 1) 70%, rgba(154, 193, 230, 1) 100%);
    color: white;
  }

  .page-theme-blue h2 {
    color: yellow;
  }

  .page-theme-blue blockquote {
    color: white;
    background-color: #70809050;
  }

  .page-theme-blue footer {
    color: yellow;
  }

  .page-theme-blue .page-number {
    color: white;
  }

  .block-theme-green {
    background-color: #8BB06F;
    border-radius: 10px;
    color: black;
  }

  .block-theme-green h2 {
    padding-left: 10px;
    padding-bottom: 0px;
    margin-bottom: 0px;
    color: black;
  }

  .block-theme-green table {
    margin-bottom: 5px;
  }

  .block-theme-plum {
    background-color: #72366A;
    border-radius: 10px;
    color: white;
    padding-left: 10px;
  }

  .block-theme-plum h2 {
    margin-top: 5px;
    padding-bottom: 0px;
    margin-bottom: 0px;
    color: white;
  }
</style>

<div class="container">  
  <input type="radio" name="slider" id="cover-radio" checked>
  <input type="radio" name="slider" id="page1-radio">
  <input type="radio" name="slider" id="page2-radio">
  <input type="radio" name="slider" id="page3-radio">
  
  <div class="book">
      <div class="page front">
        <div class="page-content">
          <h2>ACKNOWLEDGEMENTS</h2>
            <ul>
              <li>Mad lads, who provided feedback</li>
              <li><a href="https://huggingface.co/yamatazen" target="_blank">yamatazen</a> - For high quality model merges</li>
              <li>OG model authors - For making cool models</li>
              <li><a href="https://huggingface.co/arcee-ai" target="_blank">Arcee AI</a> - For making <a href="https://github.com/arcee-ai/mergekit" target="_blank">mergekit</a></li>
              <li><a href="https://huggingface.co/mradermacher" target="_blank">Team mradermacher</a> - For awesome quants</li>
              <li><a href="https://huggingface.co/DeathGodlike" target="_blank">DeathGodlike</a> - For awesome quants in EXL3</li>
              <li>Model mergers: <a href="https://huggingface.co/MrRikyz" target="_blank">Rickyz</a>, <a href="https://huggingface.co/Vortex5" target="_blank">Vortex</a>, <a href="https://huggingface.co/DreadPoor" target="_blank">Edward Eagley</a></li>
              <li>You, for trying out my models</li>
            </ul>
          <div class="page-number">6</div>
        </div>
      </div>
      <div class="page page3">
          <div class="front page-theme-blue">
              <div class="page-content">
                  <h2>WHAT USERS ARE SAYING</h2>
                  <blockquote cite="https://www.reddit.com/r/SillyTavernAI/comments/1nn5od9/comment/ngoo92d/">
                    Ive been using KSR for a week now, and I really like it. It is very creative and has brought together story threads in a natural way, even older ones at large context. I really like it so far.
                    <footer>— <cite>Pacoeltaco</cite></footer>
                  </blockquote>
                  <blockquote cite="https://www.reddit.com/r/SillyTavernAI/comments/1nb6wze/comment/ne88b3w/">
                    Ive had good results so far with my testing, smart(for 12b), follows prompts and uses things from the character card. the only thing I found negative so far is that it likes em dashes
                    <footer>— <cite>Background-Ad-5398</cite></footer>
                  </blockquote>
                  <blockquote cite="https://huggingface.co/Retreatcost/KansenSakura-Eclipse-RP-12b/discussions/1?not-for-all-audiences=true#68cd0eefd72cf1bf50e89b75">
                    I've been comparing this against a couple finetunes and this model's balance is impressive. I hope to see more soon!
                    <footer>— <cite>gggrandma1990</cite></footer>
                  </blockquote>
              </div>
              <div class="page-number">4</div>
          </div>
          <div class="back">
              <div class="page-content">
                <div class="block-theme-green">
                  <h2>SYSTEM REQUIREMENTS</h2>
                  <table>
                    <tr>
                        <td><b>Minimum<b></td>
                        <td><b>Recommended<b></td>
                    </tr>
                    <tr>
                        <td>• <b>Inference:</b> CPU<br>• <b>Memory:</b> 12GB RAM<br>• <b>Context Window:</b> 8K Tokens<br>• <b>Temp:</b> 0.65</td>
                        <td>• <b>Inference:</b> GPU<br>• <b>Memory:</b> 16GB+ VRAM<br>• <b>Context Window:</b> 16K Tokens<br>• <b>Temp:</b> 0.80<br>• <b>Courage:</b> High</td>
                    </tr>
                  </table>
                </div>
                <div class="block-theme-plum">
                  <h2>RECOMMENDED SETTINGS</h2>
                  <span>
                    <b>Temp</b>: 0.65-0.8 | <b>RepPen</b>: 1.05<br>
                    <b>TOP_P</b>: 0.95 | <b>MIN_P</b>: 0.05 | <b>TOP_K</b>: 0<br>
                    <b>Template Format</b>: ChatML | <b>Ctxt</b>: 16K
                  </span>
                </div>
              </div>
              <div class="page-number">5</div>
          </div>
      </div>
      <div class="page page2">
          <div class="front page-theme-violet">
              <div class="page-content">
                <h2>CORE FEATURES</h2>
                <ul>
                  <li><b>ADVANCED PSYCHOLOGICAL PROFILING</b><div>Characters feel realer than real - with all the darkness that implies</div></li>
                  <li><b>DREAD ATMOSPHERIC SYSTEMS</b><div>Environments that breathe, bleed, and remember your fears</div></li>
                  <li><b>EMOTIONAL EROSION ENGINE</b><div>Watch characters unravel under psychological pressure</div></li>
                  <li><b>UNFILTERED NARRATIVE DEPTH</b><div>Darker than Eclipse, more psychologically intense than Radiance</div></li>
                </ul>
              </div>
              <div class="page-number">2</div>
          </div>
          <div class="back page-theme-subtle">
              <div class="page-content">
                  <h2>FAQ</h2>
                  <ul>                    
                    <li><b>Q: IS THIS MODEL BETTER THAN X?</b><br><span>A: <b>Different weapon, different war.</b> Erosion specializes in psychological depth and darker narratives. It's smarter than previous versions, but choose your tool for the mission.</span></li>
                  </ul>
                  <ul>
                    <li><b>Q: WHEN'S THE NEXT VERSION COMING?</b><br><span>A: Currently experimenting with <b>finetuning</b> tech. Expect experimental merges while we develop the next major build.<span></li>
                  </ul>
                  <ul>
                    <li><b>Q: PLANNING OTHER ARCHITECTURES?</b><br><span>A: <b>Affirmative.</b> Reconnaissance underway for larger models - Mistral Small and Qwen3 are potential candidates for future deployments.</span></li>
                  </ul>
              </div>
              <div class="page-number">3</div>
          </div>
      </div>
      <div class="page cover">
          <div class="back page-theme-black">
              <div class="page-content">
                <h2>THE ULTIMATE RP ENGINE JUST GOT DARKER</h2>
                <p>
                  <i>They told us to extract the sakura essence. They never told us it would remember.</i>
                </p>
                <p>
                  <b>KansenSakura: Erosion</b> represents the final stage of neural corruption - where beauty becomes a weapon and every memory turns to poison.
                </p>
                <p>
                  <i>Some blossoms grow best in poisoned soil. Welcome to the garden.</i>
                </p>
                <center>
                  <div>
                    <div>Psychological Horror | Intense Themes</div>
                    <div>Complex Narratives | NSFW</div>
                    <div>KansenSakura Project | Containment Failed</div>
                    <div><b>RATED M for MATURE</b></div>
                  </div>
                </center>
              </div>
              <div class="page-number">1</div>
          </div>
      </div>
  </div>
</div>
<center>
    <div class="slider-controls">
      <label for="cover-radio"></label>
      <label for="page1-radio"></label>
      <label for="page2-radio"></label>
      <label for="page3-radio"></label>
  </div>
  
  <div style="margin-top: 20px; color: #666; font-size: 14px;">
      <p>Click the dots to navigate through the book.</p>
  </div>
  <audio controls src="https://cdn-uploads.huggingface.co/production/uploads/6671dd5203d6e8087aaf7ce5/4Kt08OL1g6OrbCu6SAFQe.mpga"></audio>
</center>

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

<details>
  <summary>Merge Details</summary>
  
  ### Merge Method
  
  This model was merged using the [Multi-SLERP](https://goddard.blog/posts/multislerp-wow-what-a-cool-idea) merge method.
  
  ### Models Merged
  
  The following models were included in the merge:
  * [Retreatcost/Irix-mpf-stock](https://huggingface.co/Retreatcost/Irix-mpf-stock)
  * [Retreatcost/Forgotten-directive-Neon-stock](https://huggingface.co/Retreatcost/Forgotten-directive-Neon-stock)
  * [Retreatcost/Lorablated-w2bb-psy-della](https://huggingface.co/Retreatcost/Lorablated-w2bb-psy-della)
  * [mistralai/Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407)
  * [yamatazen/EtherealAurora-12B-Lorablated](https://huggingface.co/yamatazen/EtherealAurora-12B-Lorablated)
  * [Retreatcost/Shisa-K-sakurization](https://huggingface.co/Retreatcost/Shisa-K-sakurization)
  * [Sicarius-Prototyping/Impish_Longtail_12B](https://huggingface.co/Sicarius-Prototyping/Impish_Longtail_12B)
  * [SuperbEmphasis/MN-12b-RP-Ink-RP-Longform](https://huggingface.co/SuperbEmphasis/MN-12b-RP-Ink-RP-Longform)
  
  ### Configuration
  
  The following YAML configuration was used to produce this model:
  
  ```yaml
  merge_method: multislerp
  models:
    - model: yamatazen/EtherealAurora-12B-Lorablated
      parameters:
        weight: [1.000, 1.000, 1.000, 1.000, 0.968, 0.744, 0.256, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.0225, 0.1275, 0.15]
    - model: Retreatcost/Shisa-K-sakurization
      parameters:
        weight: [0.000, 0.000, 0.000, 0.030, 0.256, 0.744, 0.968, 1.000, 1.000, 1.000, 1.000, 0.968, 0.744, 0.256, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.015, 0.085, 0.10]
    - model: ./impish-ink-long
      parameters:
        weight: [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.030, 0.256, 0.744, 0.968, 1.000, 1.000, 1.000, 0.968, 0.744, 0.256, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.0075, 0.0425, 0.05]
    - model: Retreatcost/Lorablated-w2bb-psy-della
      parameters:
        weight: [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.030, 0.256, 0.744, 0.968, 1.000, 1.000, 1.000, 0.968, 0.744, 0.256, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000]
    - model: Retreatcost/Forgotten-directive-Neon-stock
      parameters:
        weight: [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.030, 0.256, 0.744, 0.968, 1.000, 1.000, 1.000, 0.968, 0.744, 0.256, 0.030, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000]
    - model: Retreatcost/Irix-mpf-stock
      parameters:
        weight: [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.030, 0.256, 0.744, 0.968, 1.000, 1.000, 1.000, 1.000, 1.000, 0.850, 0.150, 0.000]
    - model: ./retokenized_NB
      parameters:
        weight: [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.105, 0.595, 0.700]
  dtype: bfloat16
  parameters:
    normalize: true
  tokenizer_source: Retreatcost/KansenSakura-Radiance-RP-12b
  
  ```
</details>

[ [**BACK**](#) ] [ [**MAIN MENU**](https://huggingface.co/Retreatcost) ] [ [ **QUIT** ](/)]