---
thumbnail: https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b/resolve/main/resources/pe.png
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
- legal
- medical
- finance
datasets:
- PocketDoc/Dans-Prosemaxx-RP
- PocketDoc/Dans-Personamaxx-Logs-2
- PocketDoc/Dans-Personamaxx-VN
- PocketDoc/Dans-Kinomaxx-VanillaBackrooms
- PocketDoc/Dans-Prosemaxx-Gutenberg
- PocketDoc/Dans-Prosemaxx-Cowriter-3-XL
- PocketDoc/Dans-Prosemaxx-Adventure
- PocketDoc/Dans-Failuremaxx-Adventure-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-2
- PocketDoc/Dans-Prosemaxx-InstructWriter-ZeroShot-3
- PocketDoc/Dans-Prosemaxx-InstructWriter-Continue-2
- PocketDoc/Dans-Prosemaxx-Instructwriter-Long
- PocketDoc/Dans-Prosemaxx-RepRemover-1
- PocketDoc/Dans-MemoryCore-CoreCurriculum-Small
- AquaV/US-Army-Survival-Sharegpt
- AquaV/Multi-Environment-Operations-Sharegpt
- AquaV/Resistance-Sharegpt
- AquaV/Interrogation-Sharegpt
- AquaV/Chemical-Biological-Safety-Applications-Sharegpt
- AquaV/Energetic-Materials-Sharegpt
- PocketDoc/Dans-Mathmaxx
- PJMixers/Math-Multiturn-1K-ShareGPT
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
- PocketDoc/Dans-Toolmaxx-Functions-apigen-subset
- PocketDoc/Dans-Assistantmaxx-OpenAssistant2
- PocketDoc/Dans-Assistantmaxx-Opus-Merge-2
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset
- PocketDoc/Dans-Assistantmaxx-sonnetorca-subset-2
- PocketDoc/Dans-Assistantmaxx-Synthia
- PocketDoc/Dans-Assistantmaxx-ASL
- PocketDoc/Dans-Assistantmaxx-PersonaLLM-Opus
- PocketDoc/Dans-Assistantmaxx-LongAlign
- PocketDoc/Dans-Assistantmaxx-OpenLeecher-Instruct
- PocketDoc/Dans-Assistantmaxx-Tulu3-IF
- PocketDoc/Dans-Systemmaxx
- PocketDoc/Dans-Logicmaxx-SAT-AP
- PJMixers/grimulkan_theory-of-mind-ShareGPT
- PJMixers/grimulkan_physical-reasoning-ShareGPT
- PocketDoc/Dans-Reasoningmaxx-NaturalReasoning
- PocketDoc/Dans-Reasoningmaxx-WebInstruct
- PocketDoc/Dans-Reasoningmaxx-GeneralReasoning
- PocketDoc/Dans-Assistantmaxx-ClosedInstruct
language:
- en
- ar
- de
- fr
- es
- hi
- pt
- ja
- ko
base_model:
- mistralai/Mistral-Small-3.1-24B-Base-2503
pipeline_tag: text-generation
library_name: transformers
---
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Dans-PersonalityEngine-V1.3.0-24b</title>
    </head>
    <div class="crt-container">
        <div class="crt-case">
            <div class="crt-inner-case">
                <div class="crt-bezel">
                    <div class="terminal-screen">
                        <div style="text-align: center">
                            <h2>Dans-PersonalityEngine-V1.3.0-24b</h2>
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
                        <p>
                            Dans-PersonalityEngine is a versatile model series
                            fine-tuned on 50+ specialized datasets, designed to
                            excel at both creative tasks (like roleplay and
                            co-writing) and technical challenges (such as code
                            generation, tool use, and complex reasoning).
                        </p>
                        <p>
                            V1.3.0 introduces multilingual capabilities with
                            support for 10 languages and enhanced domain
                            expertise across multiple fields. The primary
                            language is still English and that is where peak
                            performance can be expected.
                        </p>
                        <h3>Multilingual Support</h3>
                        <pre class="code-block">
Arabic  Chinese   English  French      German
Hindi   Japanese  Korean   Portuguese  Spanish</pre>
                        <h3>Key Details</h3>
                        <pre class="code-block">
BASE MODEL: mistralai/Mistral-Small-3.1-24B-Base-2503
LICENSE: apache-2.0
LANGUAGE: Multilingual with 10 supported languages
CONTEXT LENGTH: 32768 tokens, 131072 with degraded recall</pre>
                        <h3>Recommended Settings</h3>
                        <pre class="code-block">
TEMPERATURE: 1.0
TOP_P: 0.9</pre>
                        <h3>Prompting Format</h3>
                        <p>
                            The model uses the following format I'll refer to as
                            "DanChat-2":
                        </p>
                        <pre class="code-block">
<|system|>system prompt<|endoftext|><|user|>Hi there!<|endoftext|><|assistant|>Hey, how can I help?<|endoftext|></pre>
                        <h3>Why not ChatML?</h3>
                        <p>
                            While ChatML is a standard format for LLMs, it has
                            limitations. DanChat-2 uses special tokens
                            for each role, this reduces biases and helps the model adapt to different tasks more readily.
                        </p>
                        <h3>SillyTavern Template</h3>
                        <p>
                            <a
                                href="https://huggingface.co/PocketDoc/Dans-PersonalityEngine-V1.3.0-24b/resolve/main/resources/DanChat-2.json?download=true"
                                download
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                Download Master JSON
                            </a>
                        </p>
                        <h3>Inference Provider</h3>
                        <p>
                            This model and others are available from ⚡Mancer AI for
                            those interested in high quality inference without
                            owning or renting expensive hardware.
                        </p>
                        <p class="mancer-button-container">
                            <a
                                href="https://mancer.tech/"
                                target="_blank"
                                rel="noopener noreferrer"
                                class="mancer-button"
                            >
                                <span class="mancer-text">mancer</span>
                            </a>
                        </p>
                        <h3>Training Process</h3>
                        <p>
                            The model was trained using Axolotl on 8x H100 GPUs
                            for 50 hours. The resources to train this model were provided by Prime Intellect and Kalomaze.
                        </p>
                        <h3>Support Development</h3>
                        <p>
                            Development is limited by funding and resources. To
                            help support:
                        </p>
                        <p>- Contact on HF</p>
                        <p>- Email: visuallyadequate@gmail.com</p>
                        <p class="coffee-container">
                            <a
                                href="https://www.buymeacoffee.com/visually"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                <img
                                    src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
                                    alt="Buy Me A Coffee"
                                    height="45"
                                    width="162"
                                />
                            </a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Consolas&display=swap");
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
            box-shadow:
                inset -2px -2px 5px rgba(0, 0, 0, 0.3),
                2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .crt-inner-case {
            background: #e8d7c3;
            border-radius: 8px;
            padding: 3px;
            box-shadow:
                inset -1px -1px 4px rgba(0, 0, 0, 0.3),
                1px 1px 4px rgba(0, 0, 0, 0.2);
        }
        .crt-bezel {
            background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
            padding: 15px;
            border-radius: 5px;
            border: 3px solid #0a0a0a;
            position: relative;
            box-shadow:
                inset 0 0 20px rgba(0, 0, 0, 0.5),
                inset 0 0 4px rgba(0, 0, 0, 0.4),
                inset 2px 2px 4px rgba(255, 255, 255, 0.05),
                inset -2px -2px 4px rgba(0, 0, 0, 0.8),
                0 0 2px rgba(0, 0, 0, 0.6),
                -1px -1px 4px rgba(255, 255, 255, 0.1),
                1px 1px 4px rgba(0, 0, 0, 0.3);
        }
        .crt-bezel::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                45deg,
                rgba(255, 255, 255, 0.03) 0%,
                rgba(255, 255, 255, 0) 40%,
                rgba(0, 0, 0, 0.1) 60%,
                rgba(0, 0, 0, 0.2) 100%
            );
            border-radius: 3px;
            pointer-events: none;
        }
        .terminal-screen {
            background: #111112;
            padding: 20px;
            border-radius: 15px;
            position: relative;
            overflow: hidden;
            font-family: "Consolas", monospace;
            font-size: clamp(12px, 1.5vw, 16px);
            color: #e49b3e;
            line-height: 1.4;
            text-shadow: 0 0 2px #e49b3e;
            /* Removed animation: flicker 0.15s infinite; */
            filter: brightness(1.1) contrast(1.1);
            box-shadow:
                inset 0 0 30px rgba(0, 0, 0, 0.9),
                inset 0 0 8px rgba(0, 0, 0, 0.8),
                0 0 5px rgba(0, 0, 0, 0.6);
            max-width: 80ch;
            margin: 0 auto;
        }
        .terminal-screen h2,
        .terminal-screen h3 {
            font-size: clamp(16px, 2vw, 20px);
            margin-bottom: 1em;
            color: #e49b3e;
        }
        .terminal-screen pre.code-block {
            font-size: clamp(10px, 1.3vw, 14px);
            white-space: pre; /* Changed from pre-wrap to pre */
            margin: 1em 0;
            background-color: #1a1a1a;
            padding: 1em;
            border-radius: 4px;
            color: #e49b3e;
            overflow-x: auto; /* Added to enable horizontal scrolling */
        }
        .terminal-screen::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                linear-gradient(
                    rgba(18, 16, 16, 0) 50%,
                    rgba(0, 0, 0, 0.25) 50%
                ),
                url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyBAMAAADsEZWCAAAAGFBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4o8JoAAAAB3RSTlMAGwQIEQMYADcPzwAAACJJREFUKM9jYBgFo2AU0Beg+A8YMCLxGYZCbNQEo4BaAAD5TQiR5wU9vAAAAABJRU5ErkJggg==");
            background-size: 100% 2.5px;
            /* Removed animation: scan 1s linear infinite; */
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
            background: radial-gradient(
                circle at center,
                rgba(17, 17, 18, 0) 0%,
                rgba(17, 17, 18, 0.2) 50%,
                rgba(17, 17, 18, 0.15) 100%
            );
            border-radius: 20px;
            /* Removed animation: vignette-pulse 3s infinite; */
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
        .badge-container,
        .coffee-container {
            text-align: center;
            margin: 1em 0;
        }
        .badge-container img,
        .coffee-container img {
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
        .terminal-screen strong,
        .terminal-screen em {
            color: #f0f0f0; /* off-white color for user/system messages */
        }
        .terminal-screen p {
            color: #f0f0f0; /* off-white color for assistant responses */
        }
        .terminal-screen p,
        .terminal-screen li {
            color: #e49b3e;
        }
        .terminal-screen code,
        .terminal-screen kbd,
        .terminal-screen samp {
            color: #e49b3e;
            font-family: "Consolas", monospace;
            text-shadow: 0 0 2px #e49b3e;
            background-color: #1a1a1a;
            padding: 0.2em 0.4em;
            border-radius: 4px;
        }
        .terminal-screen pre.code-block,
        .terminal-screen pre {
            font-size: clamp(10px, 1.3vw, 14px);
            white-space: pre; /* Changed from pre-wrap to pre */
            margin: 1em 0;
            background-color: #1a1a1a;
            padding: 1em;
            border-radius: 4px;
            color: #e49b3e;
            overflow-x: auto; /* Added to enable horizontal scrolling */
        }
        .mancer-button-container {
            text-align: left;
            margin: 1em 0;
        }
        .mancer-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #1a1a1a;
            color: #e49b3e;
            padding: 15px 15px;
            border: 2px solid #e49b3e;
            border-radius: 5px;
            text-decoration: none !important;
            box-shadow: 0 0 10px rgba(228, 155, 62, 0.3);
            transition: all 0.3s ease;
            position: relative;
        }
        .mancer-text {
            font-family: "Consolas", monospace;
            font-weight: bold;
            font-size: 20px;
            text-shadow: 0 0 2px #e49b3e;
            line-height: 1;
            display: inline-block;
            margin-left: -4px;
            margin-top: -2px;
        }
        .mancer-button::before {
            content: "⚡";
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            line-height: 1;
        }
        .mancer-button:hover {
            background: #2a2a2a;
            box-shadow: 0 0 15px rgba(228, 155, 62, 0.5);
            text-shadow: 0 0 4px #e49b3e;
            text-decoration: none !important;
        }
    </style>
</html>