---
base_model:
- Nitral-AI/Violet_Magcap-12B
- DreadPoor/Irix-12B-Model_Stock
library_name: transformers
tags:
- mergekit
- merge
---
<div style="background: #000; padding:30px; border-radius:18px; box-shadow: 0 0 15px #FFFFFF, 0 0 30px #FFFFFF; color:#FFFFFF; max-width:900px; margin:auto; font-family:'Roboto', sans-serif; border:1px solid #FFFFFF;"> <style> 
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap'); 
        /* Animations */
        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        @keyframes pulseGlow {
            0%, 100% {
                box-shadow: 0 0 6px #9D00FFAA, 0 0 12px #DA70D6AA;
            }
            50% {
                box-shadow: 0 0 10px #9D00FF, 0 0 20px #DA70D6;
            }
        }
        @keyframes flicker {
            0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
                opacity: 1;
            }
            20%, 22%, 24%, 55% {
                opacity: 0.7;
            }
        }
        @keyframes floatUp {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
        @keyframes gentleGlow {
            0% { box-shadow: 0 0 12px #7F00FF33; }
            100% { box-shadow: 0 0 24px #DA70D666; }
        }
        @keyframes fadeIn { 
            0% { opacity: 0; transform: translateY(10px); } 
            100% { opacity: 1; transform: translateY(0); } 
        }
        /* General Styles */
        body { 
            margin: 0; 
            padding: 0; 
            background: #111; 
            font-family: 'Roboto', sans-serif; 
            color: #fff; 
        } 
        .blue-btn { 
          display: inline-block; 
          background: #111; 
          border: none; 
          color: #fff; 
          border-radius: 24px; 
          padding: 4px 6px 4px; /* Adjust padding for better alignment */
          text-decoration: none; 
          font-weight: 500; 
          font-size: 1.1em; 
          margin: 0 6px; /* Ensure consistent spacing */
          line-height: 1; /* Match line height to prevent misalignment */
          vertical-align: middle; /* Align with the middle of the text */
          transition: all 0.4s ease; 
          box-shadow: 0 0 6px #9D00FFAA, 0 0 12px #DA70D6AA;
          position: relative;
          overflow: hidden;
          z-index: 0;
          animation: pulseGlow 3s ease-in-out infinite, flicker 8s infinite;
} 
        .blue-btn::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(157, 0, 255, 0.15) 10%, transparent 40%);
            animation: pulseGlow 2.5s infinite;
            opacity: 0;
            transition: opacity 0.3s ease;
            z-index: -1;
        }
        .blue-btn:hover::before {
            opacity: 1;
        }
        .blue-btn:hover {
            color: #BF40BF;
            text-shadow: 0 0 6px #BF40BF, 0 0 12px #9D00FF;
            box-shadow: 0 0 25px #DA70D6, 0 0 40px #9D00FFAA;
            transform: translateY(-4px);
        }
        .glass-card { 
            background: rgba(0, 0, 0, 0.69); 
            backdrop-filter: blur(10px); 
            border-radius: 12px; 
            box-shadow: 0 4px 12px rgba(127, 0, 255, 0.5); 
            padding: 20px; 
            margin-bottom: 2em; 
            border: 1px solid rgba(127, 0, 255, 0.5);
            animation: floatUp 6s ease-in-out infinite;
            transition: box-shadow 0.3s ease;
        } 
        .glass-card:hover {
            box-shadow: 0 8px 24px rgba(218, 112, 214, 0.9), 0 0 48px rgba(157, 0, 255, 0.7);
            transform: translateY(-10px);
        }
        .fancy-img { 
            transition: all 0.5s ease; 
            border-radius: 12px; 
            border: 1px solid #7F00FF33; 
            margin-bottom: 2em; 
            box-shadow: 0 0 12px #7F00FF33; 
            cursor: pointer;
            animation: gentleGlow 8s ease-in-out infinite alternate;
        } 
        .fancy-img:hover { 
            transform: scale(1.07); 
            box-shadow: 0 0 36px #DA70D688, 0 0 48px #9D00FFAA; 
            border-color: #DA70D6AA; 
        } 
        h1, h2, h3 { 
            transition: transform 0.3s ease-in-out, color 0.3s ease; 
            cursor: default;
        } 
        h1:hover, h2:hover, h3:hover { 
            transform: translateY(-5px) scale(1.05); 
            color: #DA70D6; 
            text-shadow: 0 0 12px #9D00FF, 0 0 18px #DA70D6; 
        } 
        .fade-in { 
            animation: fadeIn 1.5s ease-in forwards;
            opacity: 0;
        } 
        blockquote { 
            color: #ccc; 
            font-style: italic; 
            border-left: 6px solid;
            border-image-slice: 1;
            border-width: 6px;
            border-image-source: linear-gradient(to bottom, #7F00FF, #9D00FF);
            padding-left: 1em; 
            margin-left: 0; 
            box-shadow: 0 0 15px #9D00FF44;
            transition: box-shadow 0.3s ease;
        }
        blockquote:hover {
            box-shadow: 0 0 30px #DA70D688;
        }
    </style> 
    <h1 class="fade-in gradient-text" style="font-size:2.2em; margin-bottom:0.3em;">🧠 Irixxed-Magcap-12B-Slerp</h1> 
    <p class="fade-in" style="color:#ccc; font-style:italic; margin-bottom:1.5em;">Merge power meets pure reasoning finesse.</p> 
    <div class="glass-card fade-in" style="animation-delay: 0.3s;"> 
        <p>Starting with <a href="https://huggingface.co/Nitral-AI/Violet_Magcap-12B" class="blue-btn pulse-btn">Violet_Magcap-12B</a>, and blended in the smooth strength of <a href="https://huggingface.co/DreadPoor/Irix-12B-Model_Stock" class="blue-btn">Irix-12B-Model_Stock</a>. </p> 
        <p><strong style="color:#9D00FF;">No gimmicks, just synergy:</strong><br> A classic Slerp merge crafted for sharp reasoning and solid performance—because why settle for one when you can have both?</p> 
    </div>
  <hr style="border:1px solid #9D00FF; margin:2em 0;">
  <p class="fade-in" style="animation-delay: 1s; color:#fff;"><strong>ChatML Format</strong></p> 
    <img src="https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/cbb9qyoPs4cRKCzYU7jPN.png" alt="ChatML Format" class="fancy-img fade-in" style="max-width:100%; margin-bottom:1em; animation-delay: 1.1s;"> 
    <hr style="border:1px solid #9D00FF; margin:2em 0;">  
    <h2 class="gradient-text fade-in" style="animation-delay: 0.7s;">⚙️ Usage Presets</h2> 
    <p class="fade-in" style="animation-delay: 0.8s;">
        <a href="https://huggingface.co/Nitral-AI/Irixxed-Magcap-12B-Slerp/tree/main/ST-Presets" class="blue-btn pulse-btn">🎛️ SillyTavern Presets</a>
    </p>
<hr style="border:1px solid #9D00FF; margin:2em 0;"> 
   <h2>💾 Quantized Versions</h2> 
    <p> <a href="https://huggingface.co/Nitral-AI/Irixxed-Magcap-12B-Slerp-Q8_0-GGUF" class="blue-btn">Q8_0 (GGUF)</a> <br> <a href="https://huggingface.co/Nitral-AI/Irixxed-Magcap-12B-Slerp-Q5_K_M-GGUF" class="blue-btn">Q5_K_M (GGUF)</a><br> <br> <a href="https://huggingface.co/Nitral-AI/Irixxed-Magcap-12B-Slerp-Q4_K_M-GGUF" class="blue-btn">Q4_K_M (GGUF)</a><br> <a href="https://huggingface.co/Nitral-AI/Irixxed-Magcap-12B-4bpw-exl2" class="blue-btn">4bpw (ExL2)</a> </p>
  <hr style="border:1px solid #9D00FF; margin:2em 0;">
  <h2 class="gradient-text fade-in" style="animation-delay: 0.5s;">🛠️ Model Details</h2> 
    <table style="border-collapse: collapse; width: 100%; color: #fff; font-size: 1em;" class="fade-in" style="animation-delay: 0.6s;"> 
        <tr> 
            <th style="border: 1px solid #222; background-color: #000; color: #9D00FF; padding: 0.5em;">Feature</th> 
            <th style="border: 1px solid #222; background-color: #000; color: #9D00FF; padding: 0.5em;">Description</th> 
        </tr> 
        <tr> 
            <td style="border: 1px solid #222; padding: 0.5em;"><strong>Base Models</strong></td> 
            <td style="border: 1px solid #222; padding: 0.5em;"> 
                <a href="https://huggingface.co/Nitral-AI/Violet_Magcap-12B" class="blue-btn">Violet_Magcap-12B</a> + 
                <a href="https://huggingface.co/DreadPoor/Irix-12B-Model_Stock" class="blue-btn">Irix-12B-Model_Stock</a> 
            </td> 
        </tr> 
        <tr> 
            <td style="border: 1px solid #222; padding: 0.5em;"><strong>Size</strong></td> 
            <td style="border: 1px solid #222; padding: 0.5em;">12B Parameters</td> 
        </tr> 
        <tr> 
            <td style="border: 1px solid #222; padding: 0.5em;"><strong>Library</strong></td> 
            <td style="border: 1px solid #222; padding: 0.5em;">Transformers</td> 
        </tr> 
        <tr> 
            <td style="border: 1px solid #222; padding: 0.5em;"><strong>Merge Type</strong></td> 
            <td style="border: 1px solid #222; padding: 0.5em;">Regular Slerp</td> 
        </tr> 
    </table>
  <hr style="border:1px solid #9D00FF; margin:2em 0;"> 
      <h2 class="gradient-text fade-in" style="animation-delay: 0.9s;">📦 Reasoning Information</h2>
    <p class="fade-in" style="animation-delay: 1.2s; color:#fff;"><strong>Reasoning Block + Prefix</strong></p> 
    <img src="https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/tzo7SN9Srcp8VRpLfYgYt.png" alt="Reasoning Format" class="fancy-img fade-in" style="max-width:100%; margin-bottom:1em; animation-delay: 1.3s;">  
    <p class="fade-in" style="animation-delay: 1.4s; color:#fff;"><strong>Quick Reply's</strong></p> 
    <img src="https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/ghNuXOflLlotJ1hrSWZxE.png" alt="Quick Reply Preset" class="fancy-img fade-in" style="max-width:100%; animation-delay: 1.5s;">
    <hr style="border:1px solid #9D00FF; margin:2em 0;"> 
<h2>⚙️ Merge-kit Config</h2>
<pre style="background-color: black; color: #9D00FF; padding: 1em;">
  slices:
  - sources:
      - model: DreadPoor/Irix-12B-Model_Stock
        layer_range: [0, 40]
      - model: Nitral-AI/Violet_Magcap-12B
        layer_range: [0, 40]
merge_method: slerp
base_model: DreadPoor/Irix-12B-Model_Stock
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.50
dtype: bfloat16
</pre>
    <hr style="border:1px solid #9D00FF; margin:2em 0;">
    <h2 class="gradient-text fade-in" style="animation-delay: 1.6s;">🌀 Vibe Check</h2> 
    <blockquote class="fade-in" style="animation-delay: 1.7s;">
        Synergy in code, clarity in reasoning.<br> 
        <strong style="color:#9D00FF;">Use it wisely—or just enjoy the smooth ride.</strong>
    </blockquote> 
    <hr style="border:1px solid #9D00FF; margin:2em 0;"> 
    <p class="fade-in" style="animation-delay: 1.8s; color:#9D00FF; margin-top: 1em;">
    <strong>🧬 Created by:</strong> 
    <a href="https://huggingface.co/Nitral-AI" class="blue-btn">Nitral-AI</a>
    <a href="https://ko-fi.com/nitralai" class="blue-btn" style="margin-left: 10px;">💖 Support on Ko-fi</a>
</p>
</div>