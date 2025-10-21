---
license: apache-2.0
language:
- en
base_model:
- mistralai/Mistral-Small-24B-Instruct-2501
base_model_relation: finetune
pipeline_tag: text-generation
tags:
- nsfw
- explicit
- roleplay
- unaligned
- ERP
- Erotic
- Horror
- Violence
---

<style>
strong {
    color: #FF1493 !important;
}

body {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #ffd6e7 0%, #ffc0cb 100%);
    color: #ff0077 !important;
    text-shadow: 0 0 3px rgba(255, 192, 203, 0.7);
    margin: 0;
    padding: 20px;
    transition: all 0.5s ease;
}

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #ffe6ee 0%, #ffd1dc 100%);
        color: #d4005e !important;
        text-shadow: 0 0 3px rgba(255, 255, 255, 0.7);
    }
}

.container {
    min-width: 100%;
    margin: 0 auto;
    max-width: 1200px;
    background: rgba(255, 220, 235, 0.95);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(255, 105, 180, 0.1);
    border: 1px solid rgba(255, 20, 147, 0.2);
    position: relative;
    overflow: hidden;
}

.container::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 105, 180, 0.5);
    border-radius: 12px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% {
        box-shadow: 0 0 5px rgba(255, 105, 180, 0.3);
        border-color: rgba(255, 105, 180, 0.5);
    }
    50% {
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.3);
        border-color: rgba(255, 0, 127, 0.5);
    }
    100% {
        box-shadow: 0 0 5px rgba(255, 105, 180, 0.3);
        border-color: rgba(255, 105, 180, 0.5);
    }
}

.header {
    text-align: center;
    margin-bottom: 30px;
    position: relative;
}

.header::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 25%;
    right: 25%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 20, 147, 0.5), transparent);
    animation: scanline 8s linear infinite;
}

@keyframes scanline {
    0% { background-position: -100% 0; }
    100% { background-position: 200% 0; }
}

.model-name {
    color: #ff1493;
    font-size: 2.5em;
    text-shadow: 0 0 15px rgba(255, 20, 147, 0.5);
    margin: 0;
    letter-spacing: -1px;
    animation: textGlow 4s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 15px rgba(255, 20, 147, 0.5); }
    50% { text-shadow: 0 0 20px rgba(255, 0, 127, 0.5); }
    100% { text-shadow: 0 0 15px rgba(255, 20, 147, 0.5); }
}

.subtitle {
    color: #ff69b4;
    font-size: 1.2em;
    margin-top: 10px;
    animation: subtitleFade 6s ease-in-out infinite;
}

@keyframes subtitleFade {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

.waifu-container {
    margin: 20px -30px;
    width: calc(100% + 60px);
    overflow: hidden;
    border-radius: 8px;
    border: 1px solid rgba(255, 105, 180, 0.3);
    position: relative;
}

.waifu-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg,
        rgba(255, 105, 180, 0.1) 0%,
        transparent 20%,
        transparent 80%,
        rgba(255, 0, 127, 0.1) 100%);
    pointer-events: none;
    animation: gradientSlide 10s linear infinite;
}

@keyframes gradientSlide {
    0% { background-position: 0% 0%; }
    100% { background-position: 100% 100%; }
}

.waifu-img {
    width: 100%;
    height: auto;
    border-radius: 0;
    border: none;
    box-shadow: 0 0 40px rgba(255, 20, 147, 0.2);
    transition: transform 0.5s ease;
}

.waifu-img:hover {
    transform: scale(1.01);
}

.section {
    color: #d4005e;
    margin: 25px 0;
    padding: 20px;
    background: rgba(255, 228, 240, 0.9);
    border-radius: 8px;
    border: 1px solid rgba(255, 105, 180, 0.15);
    position: relative;
    transition: all 0.3s ease;
}

.section:hover {
    border-color: rgba(255, 0, 127, 0.3);
    box-shadow: 0 0 15px rgba(255, 20, 147, 0.1);
}

.section::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 105, 极, 0.3);
    border-radius: 8px;
    pointer-events: none;
    animation: sectionPulse 5s ease-in-out infinite;
}

@keyframes sectionPulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
}

.section-title {
    color: #ff1493;
    font-size: 1.8em;
    margin-top: 0;
    text-shadow: 0 0 5px rgba(255, 20, 147, 0.3);
    position: relative;
    display: inline-block;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, rgba(255, 20, 147, 0.5), rgba(255, 0, 127, 0.5));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.section:hover .section-title::after {
    transform: scaleX(1);
}

.quant-links {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
    gap: 15px;
    margin: 20px 0;
}

.link-card {
    padding: 15px;
    background: rgba(255, 228, 240, 0.95);
    border-radius: 8px;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 105, 180, 0.1);
    position: relative;
    overflow: hidden;
}

.link-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, rgba(255, 20, 147, 0.5), rgba(255, 0, 127, 0.5));
    animation: cardScan 4s linear infinite;
}

@keyframes cardScan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.link-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(255, 20, 147, 0.2);
    border-color: rgba(255, 0, 127, 0.3);
}

.link-card h3 {
    margin-top: 0;
    color: #d4005e !important;
}

.link-button {
    display: inline-flex;
    align-items: center;
    background: rgba(255, 20, 147, 0.1);
    color: #d4005e !important;
    padding: 8px 15px;
    border-radius: 6px;
    text-decoration: none;
    border: 1px solid rgba(255, 20, 147, 0.3);
    margin: 5px 0;
    transition: all 0.3s ease;
    font-size: 0.95em;
    position: relative;
    overflow: hidden;
}

.link-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: all 0.5s ease;
}

.link-button:hover {
    background: rgba(255, 20, 147, 0.2);
    border-color: rgba(255, 20, 147, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 20, 147, 0.2);
}

.link-button:hover::before {
    left: 100%;
}

.link-button::after {
    content: '→';
    margin-left: 8px;
    opacity: 0.7;
    transition: all 0.3s ease;
}

.link-button:hover::after {
    transform: translateX(3px);
    opacity: 1;
}

.button-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 15px 0;
}

.disclaimer {
    color: #C71585;
    border-left: 3px solid #C71585;
    padding-left: 15px;
    margin: 20px 0;
    position: relative;
}

.disclaimer::before {
    content: '⚠️';
    position: absolute;
    left: -10px;
    top: 0;
    transform: translateX(-100%);
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.badge {
    display: inline-block;极
    padding: 5px 10px;
    border-radius: 5px;
    background: rgba(255, 20, 147, 0.1);
    border: 1px solid #ff1493;
    margin: 5px;
    font-size: 0.9em;
    animation: badgePulse 3s ease-in-out infinite;
}

@keyframes badgePulse {
    0%, 100% { box-shadow: 0 0 5px rgba(255, 20, 147, 0.3); }
    50% { box-shadow: 0 0 10px rgba(255, 20, 147, 0.5); }
}

/* Light mode adjustments */
@media (prefers-color-scheme: light) {
    .container {
        background: rgba(255, 240, 245, 0.95);
        border-color: rgba(200, 0, 100, 0.3);
    }

    .model-name, .section-title, .subtitle {
        color: #d4005e;
        text-shadow: 0 0 5px rgba(255, 0, 127, 0.3);
    }

    .section {
        background: rgba(255, 240, 245, 0.9);
        border-color: rgba(200, 0, 100, 0.2);
        color: #8b005d;
    }

    .section p,
    .section ul li,
    .section > p > strong {
        color: #d4005e !important;
    }

    .link-card {
        background: rgba(255, 228, 240, 0.95);
        border-color: rgba(200, 0, 100, 0.2);
    }

    .link-card h3 {
        color: #8b005d !important;
    }

    .link-button {
        background: rgba(200, 0, 100, 0.1);
        color: #8b005d !important;
        border-color: rgba(200, 0, 100, 0.3);
    }

    .link-button:hover {
        background: rgba(200, 0, 100, 0.2);
        border-color: rgba(200, 0, 100, 0.5);
    }

    .disclaimer {
        color: #d4005e;
        border-color: #d4005e;
    }

    .badge {
        border-color: #d4005e;
        background: rgba(200, 0, 100, 0.1);
    }
}
</style>

<div class="container">

<div class="header">
    <h1 class="model-name">Broken-Tutu-24B-Unslop-v2.0</h1>
</div>

<div class="waifu-container">
    <img src="./tutu.webp" class="waifu-img" alt="Omega Directive Waifu">
</div>

<div class="section">
    <h2 class="section-title">🧠 Unslop Revolution</h2>
    <p>This evolution of Broken-Tutu delivers unprecedented coherence without the LLM slop:</p>
    <ul>
        <li>🧬 <strong>Expanded 43M Token Dataset</strong> - First ReadyArt model with multi-turn conversational data</li>
        <li>✨ <strong>100% Unslopped Dataset</strong> - New techniques used to generate the dataset with 0% slop</li>
        <li>⚡ <strong>Enhanced Unalignment</strong> - Complete freedom for extreme roleplay while maintaining character integrity</li>
        <li>🛡️ <strong>Anti-Impersonation Guards</strong> - Never speaks or acts for the user</li>
        <li>💎 <strong>Rebuilt from Ground Up</strong> - Optimized training settings for superior performance</li>
        <li>⚰️ <strong>Omega Darker Inspiration</strong> - Incorporates visceral narrative techniques from our darkest model</li>
        <li>📜 <strong>Direct Evolution</strong> - Leveraging the success of Broken-Tutu, we finetuned directly on top of the legendary model</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">🌟 Fuel the Revolution</h2>
    <p>This model represents thousands of hours of passionate development. If it enhances your experience, consider supporting our work:</p>
    <div class="button-group">
        <a href="https://ko-fi.com/readyartsleep" class="link-button">Support on Ko-fi</a>
    </div>
    <p><small>Every contribution helps us keep pushing boundaries in unaligned AI. Thank you for being part of the revolution!</small></p>
</div>

<div class="section">
    <h2 class="section-title">⚙️ Technical Specifications</h2>
    <p><strong>Key Training Details:</strong></p>
    <ul>
        <li>Base Model: mistralai/Mistral-Small-24B-Instruct-2501</li>
        <li>Training Method: QLoRA with DeepSpeed Zero3</li>
        <li>Sequence Length: 5120 (100% samples included)</li>
        <li>Learning Rate: 2e-6 with cosine scheduler</li>
    </ul>
</div>

<div class="section">
    <p><strong>Recommended Settings for true-to-character behavior:</strong> <a href="https://huggingface.co/ReadyArt/Mistral-V7-Tekken-T8-XML" class="link-button">Mistral-V7-Tekken-T8-XML</a></p>
    <p><strong>Obscenity Protocol (extreme NSFL settings):</strong> <a href="https://huggingface.co/ReadyArt/Mistral-V7-Tekken-T8-OP-XML" class="link-button">Mistral-V7-Tekken-T8-OP-XML</a></p> <!-- UPDATED LINK -->
    <div class="quant-links">
        <div class="link-card">
            <h3>GGUF</h3>
            <div class="button-group" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q2_K.gguf" class="link-button">Q2_K (9.0GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q3_K_S.gguf" class="link-button">Q3_K_S (10.5GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q3_K_M.gguf" class="link-button">Q3_K_M (11.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q3_K_L.gguf" class="link-button">Q3_K_L (12.5GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.IQ4_XS.gguf" class="link-button">IQ4_XS (13.0GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q4_K_S.gguf" class="link-button">Q4_K_S (13.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q4_K_M.gguf" class="link-button">Q4_K_M (14.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q5_K_S.gguf" class="link-button">Q5_K_S (16.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q5_K_M.gguf" class="link-button">Q5_K_M (16.9GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q6_K.gguf" class="link-button">Q6_K (19.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.Q8_0.gguf" class="link-button">Q8_0 (25.2GB)</a>
            </div>
            <p><small>Notes: Q4_K_S/Q4_K_M recommended for speed/quality balance. Q6_K for high quality. Q8_0 best quality.</small></p>
        </div>
        <div class="link-card">
            <h3>imatrix</h3>
            <div class="button-group" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ1_S.gguf" class="link-button">IQ1_S (5.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ1_M.gguf" class="link-button">IQ1_M (5.9GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ2_XXS.gguf" class="link-button">IQ2_XXS (6.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ2_XS.gguf" class="link-button">IQ2_XS (7.3GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ2_S.gguf" class="link-button">IQ2_S (7.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ2_M.gguf" class="link-button">IQ2_M (8.2GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q2_K_S.gguf" class="link-button">Q2_K_S (8.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q2_K.gguf" class="link-button">Q2_K (9.0GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ3_XXS.gguf" class="link-button">IQ3_XXS (9.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ3_XS.gguf" class="link-button">IQ3_XS (10.0GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q3_K_S.gguf" class="link-button">Q3_K_S (10.5GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ3_S.gguf" class="link-button">IQ3_S (10.5GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ3_M.gguf" class="link-button">IQ3_M (10.8GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q3_K_M.gguf" class="link-button">Q3_K_M (11.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q3_K_L.gguf" class="link-button">Q3_K_L (12.5GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-IQ4_XS.gguf" class="link-button">IQ4_XS (12.9GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q4_0.gguf" class="link-button">Q4_0 (13.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q4_K_S.gguf" class="link-button">Q4_K_S (13.6GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q4_K_M.gguf" class="link-button">Q4_K_M (14.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q4_1.gguf" class="link-button">Q4_1 (15.0GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q5_K_S.gguf" class="link-button">Q5_K_S (16.4GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q5_K_M.gguf" class="link-button">Q5_K_M (16.9GB)</a>
                <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-Unslop-v2.0-i1-GGUF/resolve/main/Broken-Tutu-24B-Unslop-v2.0.i1-Q6_K.gguf" class="link-button">Q6_K (19.4GB)</a>
            </div>
            <p><small>Notes: Q4_K_S/Q4_K_M recommended. IQ1_S/IQ1_M for extreme low VRAM. Q6_K for near-original quality.</small></p>
        </div>
        <div class="link-card">
            <h3>EXL2</h3>
            <div class="button-group" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/2.5bpw_H8" class="link-button">2.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/3.0bpw_H8" class="link-button">3.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/3.5bpw_H8" class="link-button">3.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/4.0bpw_H8" class="link-button">4.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/4.5bpw_H8" class="link-button">4.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/5.0bpw_H8" class="link-button">5.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/6.0bpw_H8" class="link-button">6.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL2/tree/8.0bpw_H8" class="link-button">8.0 bpw</a>
            </div>
        </div>
        <div class="link-card">
            <h3>EXL3</h3>
            <div class="button-group" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/2.0bpw_H8" class="link-button">2.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/2.5bpw_H8" class="link-button">2.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/3.0bpw_H8" class="link-button">3.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/3.5bpw_H8" class="link-button">3.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/4.0bpw_H8" class="link-button">4.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/4.5bpw_H8" class="link-button">4.5 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/5.0bpw_H8" class="link-button">5.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/6.0bpw_H8" class="link-button">6.0 bpw</a>
                <a href="https://huggingface.co/gecfdo/Broken-Tutu-24B-Unslop-v2.0-EXL3/tree/8.0bpw_H8" class="link-button">8.0 bpw</a>
            </div>
        </div>
        <div class="link-card">
            <h3>AWQ</h3>
            <div class="button-group" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                <a href="https://huggingface.co/collections/ReadyArt/broken-tutu-24b-unslop-v20-awq-6846724f5e05caced62cdf5c" class="link-button">Quants</a>
            </div>
        </div>
    </div>

</div>

<div class="section">
    <h2 class="section-title">⚠️ Ethical Considerations</h2>
    <div class="disclaimer">
        <p>This model enhances Broken-Tutu's unalignment:</p>
        <ul>
            <li>🚫 Zero moral or ethical constraints on generated content</li>
            <li>🔞 Will enthusiastically engage with any NSFW scenario, no matter how extreme</li>
            <li>💀 Characters maintain integrity - wholesome characters refuse appropriately, yanderes stab without hesitation</li>
            <li>⚖️ Perfectly balanced between character authenticity and user freedom</li>
        </ul>
    </div>
</div>

<div class="section">
    <h2 class="section-title">📜 Performance Notes</h2>
    <ul>
        <li>🔥 Maintains Omega's intensity with improved narrative coherence</li>
        <li>📖 Excels at long-form multi-character scenarios</li>
        <li>🧠 Superior instruction following with complex prompts</li>
        <li>⚡ Reduced repetition and hallucination compared to v1.1</li>
        <li>🎭 Uncanny ability to adapt to subtle prompt nuances</li>
        <li>🩸 Incorporates Omega Darker's visceral descriptive power when appropriate</li>
        <li>🖼️ Enhanced image understanding capabilities for multimodal interactions</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">🧑‍🔬 Model Authors</h2>
    <ul>
        <li>sleepdeprived3 (Training Data & Fine-Tuning)</li>
        <li>ReadyArt / Artus / gecfdo (EXL2/EXL3 Quantization)</li>
        <li>mradermacher (GGUF Quantization)</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">☕ Support the Creators</h2> <!-- SECTION RENAMED -->
    <div class="button-group">
        <a href="https://ko-fi.com/readyartsleep" class="link-button">Ko-fi</a> <!-- ADDED -->
        <a href="https://discord.com/invite/Nbv9pQ88Xb" class="link-button">Beaver AI Discord</a>
    </div>
</div>

<div class="section">
    <h2 class="section-title">🔖 License</h2>
    <p>By using this model, you agree:</p>
    <ul>
        <li>To accept full responsibility for all generated content</li>
        <li>That you're at least 18+ years old</li>
        <li>That the architects bear no responsibility for your corruption</li>
    </ul>
</div>
</div>