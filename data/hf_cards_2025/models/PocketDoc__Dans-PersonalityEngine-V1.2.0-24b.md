---
thumbnail: https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.2.0-24b/resolve/main/resources/pe24.png
license: apache-2.0
tags:
- general-purpose
- roleplay
- storywriting
- chemistry
- biology
- code
- climate
- axolotl
- text-generation-inference
- finetune
datasets:
- PocketDoc/Dans-MemoryCore-CoreCurriculum-Small
- AquaV/US-Army-Survival-Sharegpt
- AquaV/Multi-Environment-Operations-Sharegpt
- AquaV/Resistance-Sharegpt
- AquaV/Interrogation-Sharegpt
- AquaV/Chemical-Biological-Safety-Applications-Sharegpt
- AquaV/Energetic-Materials-Sharegpt
- PocketDoc/Dans-Mathmaxx
- PocketDoc/Dans-Mathmaxx-Numina-CoT
- PJMixers/Math-Multiturn-1K-ShareGPT
- PocketDoc/Dans-Benchmaxx-COT
- PocketDoc/Dans-Codemaxx-LeetCode
- PocketDoc/Dans-Codemaxx-CodeFeedback-Conversations
- PocketDoc/Dans-Codemaxx-CodeFeedback-SingleTurn
- PocketDoc/Dans-Codemaxx-Bigcode-SelfInstruct
- PocketDoc/Dans-Taskmaxx
- PocketDoc/Dans-Taskmaxx-DataPrepper
- PocketDoc/Dans-Taskmaxx-ConcurrentQA-Reworked
- PocketDoc/Dans-Taskmaxx-TableGPT
- PocketDoc/Dans-Taskmaxx-SciRIFF
- PocketDoc/Dans-Taskmaxx-Edit
- PocketDoc/Dans-Toolmaxx-Agent
- PocketDoc/Dans-Toolmaxx-ShellCommands
- PocketDoc/Dans-Toolmaxx-Functions-Toolbench
- PocketDoc/Dans-Toolmaxx-Functions-ToolACE
- PocketDoc/Dans-ASCIIMaxx-Wordart
- PocketDoc/Dans-Prosemaxx-Gutenberg
- PocketDoc/Dans-Prosemaxx-Cowriter-3-XL
- PocketDoc/Dans-Prosemaxx-Adventure
- PocketDoc/Dans-Failuremaxx-Adventure-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-2
- PocketDoc/Dans-Prosemaxx-InstructWriter-Continue-2
- PocketDoc/Dans-Assistantmaxx-Sharegpt
- PocketDoc/Dans-Assistantmaxx-OpenAssistant2
- PocketDoc/Dans-Assistantmaxx-Opus-Merge
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset-2
- PocketDoc/Dans-Assistantmaxx-NoRobots
- PocketDoc/Dans-Assistantmaxx-Synthia
- PocketDoc/Dans-Assistantmaxx-ASL
- PocketDoc/Dans-Assistantmaxx-PersonaLLM-Opus
- PocketDoc/Dans-Assistantmaxx-UnnaturalInstructions-GPT4
- PocketDoc/Dans-Assistantmaxx-LongAlign
- PocketDoc/Dans-Assistantmaxx-EvolKit
- PocketDoc/Dans-Assistantmaxx-Camel-GPT4
- PocketDoc/Dans-Assistantmaxx-OpenLeecher-Instruct
- PocketDoc/Dans-Assistantmaxx-Tulu3-IF
- PocketDoc/Dans-Systemmaxx
- PocketDoc/Dans-Logicmaxx-Skunkworks
- PocketDoc/Dans-Logicmaxx-FI-VeriMed
- PocketDoc/Dans-Logicmaxx-SAT-AP
- PocketDoc/Dans-Logicmaxx-Magpie-Ultra
- PJMixers/grimulkan_theory-of-mind-ShareGPT
- PJMixers/grimulkan_physical-reasoning-ShareGPT
- PocketDoc/Dans-Personamaxx
- PocketDoc/Dans-Personamaxx-Rainy
- PocketDoc/Dans-Personamaxx-C1
- PocketDoc/Dans-Personamaxx-VN
language:
- en
base_model:
- mistralai/Mistral-Small-24B-Base-2501
pipeline_tag: text-generation
library_name: transformers
new_version: PocketDoc/Dans-PersonalityEngine-V1.3.0-24b
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<div class="crt-container">
  <div class="crt-case">
    <div class="crt-inner-case">
      <div class="crt-bezel">
<div class="terminal-screen">
  <div style="text-align: center;">
    <h2>Dans-PersonalityEngine-V1.2.0-24b</h2>
    <pre class="code-block" style="display: inline-block; text-align: left; font-size: clamp(2px, 0.8vw, 14px); line-height: 1.2; max-width: 100%; overflow: hidden; white-space: pre;">  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠄⠀⡂⠀⠁⡄⢀⠁⢀⣈⡄⠌⠐⠠⠤⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡄⠆⠀⢠⠀⠛⣸⣄⣶⣾⡷⡾⠘⠃⢀⠀⣴⠀⡄⠰⢆⣠⠘⠰⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⡋⢀⣤⡿⠟⠋⠁⠀⡠⠤⢇⠋⠀⠈⠃⢀⠀⠈⡡⠤⠀⠀⠁⢄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⡂⠀⠀⣀⣔⣧⠟⠋⠀⢀⡄⠀⠪⣀⡂⢁⠛⢆⠀⠀⠀⢎⢀⠄⢡⠢⠛⠠⡀⠀⠄⠀⠀
⠀⠀⡀⠡⢑⠌⠈⣧⣮⢾⢏⠁⠀⠀⡀⠠⠦⠈⠀⠞⠑⠁⠀⠀⢧⡄⠈⡜⠷⠒⢸⡇⠐⠇⠿⠈⣖⠂⠀
⠀⢌⠀⠤⠀⢠⣞⣾⡗⠁⠀⠈⠁⢨⡼⠀⠀⠀⢀⠀⣀⡤⣄⠄⠈⢻⡇⠀⠐⣠⠜⠑⠁⠀⣀⡔⡿⠨⡄
⠈⠂⠀⠆⠀⣼⣾⠟⠀⠑⠀⡐⠗⠉⠀⠐⠶⣤⡵⠋⠀⠠⠹⡌⡀⠘⠇⢠⣾⡣⣀⡴⠋⠅⠈⢊⠠⡱⡀
⠪⠑⢌⠂⣼⣿⡟⠀⠀⠙⠀⠀⠀⡀⠀⠀⠐⡞⡐⠀⠀⡧⠀⢀⠠⠀⣁⠾⡇⠀⠙⡁⠀⠀⢀⣨⣄⡠⢱
⣸⠈⠊⠙⣛⣿⡧⠔⠚⠛⠳⣄⣀⡬⠤⠬⠼⡣⠃⠀⢀⡗⠀⡤⠞⠙⠄⠂⠃⢀⣠⣤⠶⠙⠅⠁⠃⠋⠈
⢋⠼⣀⠰⢯⢿⠁⠀⢢⠀⠀⢐⠋⡀⠀⠈⠁⠀⣀⣰⠏⠒⠙⠈⠀⣀⡤⠞⢁⣼⠏⠘⢀⣀⢤⢤⡐⢈⠂
⠀⠢⠀⠀⠸⣿⡄⠲⠚⠘⠚⠃⢀⠀⠈⢋⠶⠛⠉⠉⢃⣀⢤⢾⠋⣁⡤⡚⠁⢹⠁⠠⢛⠠⠬⠁⢬⠀⠀
⠀⠈⢳⣒⠋⠉⣿⢐⠠⣀⣃⠀⠀⠉⠂⢁⣀⣀⡤⢞⠩⢑⡨⠰⡞⠁⠁⢀⡠⠾⠎⡈⡌⡈⡓⡀⠄⠀⠀
⠀⠀⠀⠉⠘⠃⢻⡒⠦⢼⣿⣛⣻⣿⡷⢄⣀⣀⣠⣴⢾⣿⣆⣡⡄⣠⣪⡿⣷⣾⣷⣧⡡⠅⣇⠍⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠛⠛⠓⠉⢹⠀⣷⠴⣻⣽⡻⢧⢻⡿⡏⣼⢿⣻⢾⣿⣿⣿⡿⢠ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠻⠨⠰⢋⡅⠉⣑⡇⡗⣿⢂⣸⡿⣿⣛⠿⠃⠁ ⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣌⣙⣸⢧⣿⣕⣼⣇⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣸⢧⢟⢟⡟⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠙⣾⡟⣻⡕⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⢰⡏⢠⡿⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠸⡇⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⢸⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    </pre>
  </div>
  <p>This model series is intended to be multifarious in its capabilities and should be quite capable at both co-writing and roleplay as well as find itself quite at home performing sentiment analysis or summarization as part of a pipeline.</p>
  <p>It has been trained on a wide array of one shot instructions, multi turn instructions, tool use, role playing scenarios, text adventure games, co-writing, and much more.</p>
  <h3>Key Details</h3>
  <pre class="code-block">
BASE MODEL: mistralai/Mistral-Small-24B-Base-2501
LICENSE: apache-2.0
LANGUAGE: English
CONTEXT LENGTH: 32768 tokens</pre>
<a href="https://chub.ai/">
    <img src="./resources/chub-black.gif" alt="Sponsored by Chub.AI" class="sponsor-image-small">
</a>
  <h3>Recommended Settings</h3>
  <pre class="code-block">
TEMPERATURE: 1.0
TOP_P: 0.95
MIN_P: 0.05</pre>
  <h3>Prompting Format</h3>
  <p>The model uses standard "ChatML" format:</p>
  <pre class="code-block">
<|im_start|>system
system prompt<|im_end|>
<|im_start|>user
Hi there!<|im_end|>
<|im_start|>assistant
Nice to meet you!<|im_end|></pre>
  A word of caution: As of Feb 19 2025 backends can't seem to agree on automatically addind a "bos" token to the start, which they should! I'm investigating if there is a way I can change the config to mitigate this but for now if you have incoherent outputs not typical of a 24b model (verbatim repeating what you said back to you for instance) then try adding "&lt;s&gt;" to the very beginning of your context.
  <h3>SillyTavern Templates</h3>
  <details>
    <summary>Context Template</summary>
    <pre class="code-block">
{
    "story_string": "<|im_start|>system\n{{#if system}}{{system}}\n{{/if}}{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{char}}'s personality: {{personality}}\n{{/if}}{{#if scenario}}Scenario: {{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}{{trim}}<|im_end|>\n",
    "example_separator": "",
    "chat_start": "",
    "use_stop_strings": false,
    "allow_jailbreak": false,
    "always_force_name2": false,
    "trim_sentences": false,
    "include_newline": false,
    "single_line": false,
    "name": "Dan-ChatML"
}</pre>
  </details>
  <details>
    <summary>Instruct Template</summary>
    <pre class="code-block">
{
    "system_prompt": "Write {{char}}'s actions and dialogue, user will write {{user}}'s.",
    "input_sequence": "<|im_start|>user\n",
    "output_sequence": "<|im_start|>assistant\n",
    "first_output_sequence": "",
    "last_output_sequence": "",
    "system_sequence_prefix": "",
    "system_sequence_suffix": "",
    "stop_sequence": "<|im_end|>",
    "wrap": false,
    "macro": true,
    "names": false,
    "names_force_groups": false,
    "activation_regex": "",
    "skip_examples": false,
    "output_suffix": "<|im_end|>\n",
    "input_suffix": "<|im_end|>\n",
    "system_sequence": "<|im_start|>system\n",
    "system_suffix": "<|im_end|>\n",
    "user_alignment_message": "",
    "last_system_sequence": "",
    "system_same_as_user": false,
    "first_input_sequence": "",
    "last_input_sequence": "",
    "name": "Dan-ChatML"
}</pre>
  </details>
  <h3>A Chub.AI Sponsored Model</h3>
  <div>
    <a href="https://chub.ai/">
      <img src="./resources/chub-black.gif" alt="Sponsored by Chub.AI" class="sponsor-image">
    </a>
  </div>
  <div>
    <p>Character Hub supported this model with 65 hours on a 4x H200 144GB system. This is only some of what they've provided me for training and I am very grateful for their contributions, this model especially would have been difficult without it.</p>
    <p>Character Hub has been supporting model development for quite a while now and they may be interested in your projects! Contact them through <a href="https://forms.gle/GSEZ388EkyYoe2Kz6">this google form</a>.</p>
  </div>
  <h3>Support Development</h3>
  <p>Development is limited by funding and resources. To help support:</p>
  <p>- Contact on HF</p>
  <p>- Email: visuallyadequate@gmail.com</p>
  <p class="coffee-container">
  <a href="https://www.buymeacoffee.com/visually" target="_blank" rel="noopener noreferrer">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="45" width="162">
  </a>
</p>
</div>
      </div>
    </div>
  </div>
</div>
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
.crt-container {
  padding: 10px;
  max-width: 1000px;
  margin: 0 auto;
  width: 95%;
}
.crt-case {
  background: #e8d7c3;
  border-radius: 10px;
  padding: 15px;
  box-shadow: inset -2px -2px 5px rgba(0,0,0,0.3), 2px 2px 5px rgba(0,0,0,0.2);
}
.crt-inner-case {
  background: #e8d7c3;
  border-radius: 8px;
  padding: 3px;
  box-shadow: inset -1px -1px 4px rgba(0,0,0,0.3), 1px 1px 4px rgba(0,0,0,0.2);
}
.crt-bezel {
  background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
  padding: 15px;
  border-radius: 5px;
  border: 3px solid #0a0a0a;
  position: relative;
  box-shadow: 
    inset 0 0 20px rgba(0,0,0,0.5),
    inset 0 0 4px rgba(0,0,0,0.4),
    inset 2px 2px 4px rgba(255,255,255,0.05),
    inset -2px -2px 4px rgba(0,0,0,0.8),
    0 0 2px rgba(0,0,0,0.6),
    -1px -1px 4px rgba(255,255,255,0.1),
    1px 1px 4px rgba(0,0,0,0.3);
}
.crt-bezel::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg,
    rgba(255,255,255,0.03) 0%,
    rgba(255,255,255,0) 40%,
    rgba(0,0,0,0.1) 60%,
    rgba(0,0,0,0.2) 100%);
  border-radius: 3px;
  pointer-events: none;
}
.terminal-screen {
  background: #111112;
  padding: 20px;
  border-radius: 15px;
  position: relative;
  overflow: hidden;
  font-family: 'VT323', monospace;
  font-size: clamp(12px, 1.5vw, 16px);
  color: #e49b3e;
  line-height: 1.4;
  text-shadow: 0 0 2px #e49b3e;
  animation: flicker 0.15s infinite;
  filter: brightness(1.1) contrast(1.1);
  box-shadow: 
    inset 0 0 30px rgba(0,0,0,0.9),
    inset 0 0 8px rgba(0,0,0,0.8),
    0 0 5px rgba(0,0,0,0.6);
  max-width: 80ch;
  margin: 0 auto;
}
.terminal-screen h2, .terminal-screen h3 {
  font-size: clamp(16px, 2vw, 20px);
  margin-bottom: 1em;
  color: #e49b3e;
}
.terminal-screen pre.code-block {
  font-size: clamp(10px, 1.3vw, 14px);
  white-space: pre;  /* Changed from pre-wrap to pre */
  margin: 1em 0;
  background-color: #1a1a1a;
  padding: 1em;
  border-radius: 4px;
  color: #e49b3e;
  overflow-x: auto;  /* Added to enable horizontal scrolling */
}
.terminal-screen::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyBAMAAADsEZWCAAAAGFBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4o8JoAAAAB3RSTlMAGwQIEQMYADcPzwAAACJJREFUKM9jYBgFo2AU0Beg+A8YMCLxGYZCbNQEo4BaAAD5TQiR5wU9vAAAAABJRU5ErkJggg==');
  background-size: 100% 2.5px;
  animation: scan 1s linear infinite;
  pointer-events: none;
  z-index: 2;
}
.terminal-screen::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, 
    rgba(17, 17, 18, 0) 0%, 
    rgba(17, 17, 18, 0.2) 50%, 
    rgba(17, 17, 18, 0.15) 100%
  );
  border-radius: 20px;
  animation: vignette-pulse 3s infinite;
  pointer-events: none;
  z-index: 1;
}
.terminal-screen details {
  margin: 1em 0;
  padding: 0.5em;
  border: 1px solid #e49b3e;
  border-radius: 4px;
}
.terminal-screen summary {
  cursor: pointer;
  font-weight: bold;
  margin: -0.5em;
  padding: 0.5em;
  border-bottom: 1px solid #e49b3e;
  color: #e49b3e;
}
.terminal-screen details[open] summary {
  margin-bottom: 0.5em;
}
.badge-container, .coffee-container {
  text-align: center;
  margin: 1em 0;
}
.badge-container img, .coffee-container img {
  max-width: 100%;
  height: auto;
}
.terminal-screen a {
  color: #e49b3e;
  text-decoration: underline;
  transition: opacity 0.2s;
}
.terminal-screen a:hover {
  opacity: 0.8;
}
.terminal-screen strong, .terminal-screen em {
  color: #f0f0f0;  /* off-white color for user/system messages */
}
.terminal-screen p {
  color: #f0f0f0;  /* off-white color for assistant responses */
}
.terminal-screen p, .terminal-screen li {
  color: #e49b3e;
}
.terminal-screen code,
.terminal-screen kbd,
.terminal-screen samp {
  color: #e49b3e;
  font-family: 'VT323', monospace;
  text-shadow: 0 0 2px #e49b3e;
  background-color: #1a1a1a;
  padding: 0.2em 0.4em;
  border-radius: 4px;
}
.terminal-screen pre.code-block,
.terminal-screen pre {
  font-size: clamp(10px, 1.3vw, 14px);
  white-space: pre;  /* Changed from pre-wrap to pre */
  margin: 1em 0;
  background-color: #1a1a1a;
  padding: 1em;
  border-radius: 4px;
  color: #e49b3e;
  overflow-x: auto;  /* Added to enable horizontal scrolling */
}
.sponsor-image {
  width: 360px;
  height: auto;
  border: 2px solid #e49b3e;
  border-radius: 10px;
  filter: brightness(0.9) sepia(0.2);
  transition: all 0.3s ease;
}
.sponsor-image-small {
  width: 180px;
  height: auto;
  border: 2px solid #e49b3e;
  border-radius: 5px;
  filter: brightness(0.9) sepia(0.2);
  transition: all 0.3s ease;
}
.sponsor-image:hover {
  filter: brightness(1) sepia(0);
  box-shadow: 0 0 10px rgba(228, 155, 62, 0.5);
}
</style>