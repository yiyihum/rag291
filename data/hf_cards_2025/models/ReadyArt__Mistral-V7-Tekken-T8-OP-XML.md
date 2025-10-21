---
license: apache-2.0
tags:
- roleplay
- text-generation
- nsfw
- explicit
- unaligned
- obscenity
---

<style>
strong {
    color: #FF1493 !important;
}

body {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
    color: #ff0077 !important;
    text-shadow: 0 0 3px rgba(255, 0, 119, 0.7);
    margin: 0;
    padding: 20px;
    transition: all 0.5s ease;
}

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #2b0a1a 0%, #1a0010 100%);
        color: #ff4da6 !important;
        text-shadow: 0 0 3px rgba(255, 77, 166, 0.7);
    }
}

.container {
    min-width: 100%;
    margin: 0 auto;
    max-width: 1200px;
    background: rgba(30, 0, 15, 0.95);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(255, 0, 119, 0.1);
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
    border: 1px solid rgba(255, 0, 119, 0.5);
    border-radius: 12px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% {
        box-shadow: 0 0 5px rgba(255, 0, 119, 0.3);
        border-color: rgba(255, 0, 119, 0.5);
    }
    50% {
        box-shadow: 0 0 15px rgba(139, 0, 139, 0.3);
        border-color: rgba(139, 0, 139, 0.5);
    }
    100% {
        box-shadow: 0 0 5px rgba(255, 0, 119, 0.3);
        border-color: rgba(255, 0, 119, 0.5);
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
    background: linear-gradient(90deg, transparent, rgba(255, 0, 119, 0.5), transparent);
    animation: scanline 8s linear infinite;
}

@keyframes scanline {
    0% { background-position: -100% 0; }
    100% { background-position: 200% 0; }
}

.model-name {
    color: #ff0077;
    font-size: 2.5em;
    text-shadow: 0 0 15px rgba(255, 0, 119, 0.5);
    margin: 0;
    letter-spacing: -1px;
    animation: textGlow 4s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 15px rgba(255, 0, 119, 0.5); }
    50% { text-shadow: 0 0 20px rgba(139, 0, 139, 0.5); }
    100% { text-shadow: 0 0 15px rgba(255, 0, 119, 0.5); }
}

.subtitle {
    color: #ff4da6;
    font-size: 1.2em;
    margin-top: 10px;
    animation: subtitleFade 6s ease-in-out infinite;
}

@keyframes subtitleFade {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; }
}

.section {
    color: #ff4da6;
    margin: 25px 0;
    padding: 20px;
    background: rgba(50, 0, 25, 0.9);
    border-radius: 8px;
    border: 1px solid rgba(255, 0, 119, 0.15);
    position: relative;
    transition: all 0.3s ease;
}

.section:hover {
    border-color: rgba(139, 0, 139, 0.3);
    box-shadow: 0 0 15px rgba(255, 0, 119, 0.1);
}

.section::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 0, 119, 0.3);
    border-radius: 8px;
    pointer-events: none;
    animation: sectionPulse 5s ease-in-out infinite;
}

@keyframes sectionPulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
}

.section-title {
    color: #ff0077;
    font-size: 1.8em;
    margin-top: 0;
    text-shadow: 0 0 5px rgba(255, 0, 119, 0.3);
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
    background: linear-gradient(90deg, rgba(255, 0, 119, 0.5), rgba(139, 0, 139, 0.5));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.section:hover .section-title::after {
    transform: scaleX(1);
}

.link-button {
    display: inline-flex;
    align-items: center;
    background: rgba(255, 0, 119, 0.1);
    color: #ff4da6 !important;
    padding: 8px 15px;
    border-radius: 6px;
    text-decoration: none;
    border: 1px solid rgba(255, 0, 119, 0.3);
    margin: 5px 0;
    transition: all 0.3s ease;
    font-size: 0.95em;
    position: relative;
    overflow: hidden;
}

.link-button:hover {
    background: rgba(255, 0, 119, 0.2);
    border-color: rgba(255, 0, 119, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 0, 119, 0.2);
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

.code-block {
    background: rgba(50, 0, 25, 0.95);
    border-radius: 8px;
    padding: 20px;
    overflow-x: auto;
    border: 1px solid rgba(255, 0, 119, 0.3);
    font-family: 'Courier New', Courier, monospace;
    color: #ff4da6;
    margin: 15px 0;
}

/* Light mode adjustments */
@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #2b0a1a 0%, #1a0010 100%);
        color: #ff4da6 !important;
    }

    .container {
        background: rgba(40, 0, 20, 0.95);
        border-color: rgba(200, 0, 100, 0.3);
    }

    .model-name, .section-title, .subtitle {
        color: #ff4da6;
        text-shadow: 0 0 5px rgba(255, 0, 127, 0.3);
    }

    .section {
        background: rgba(60, 0, 30, 0.9);
        border-color: rgba(200, 0, 100, 0.2);
        color: #ff80bf;
    }

    .section p,
    .section ul li,
    .section > p > strong {
        color: #ff4da6 !important;
    }

    .link-button {
        background: rgba(200, 0, 100, 0.1);
        color: #ff80bf !important;
        border-color: rgba(200, 0, 100, 0.3);
    }

    .link-button:hover {
        background: rgba(200, 0, 100, 0.2);
        border-color: rgba(200, 0, 100, 0.5);
    }

    .code-block {
        background: rgba(60, 0, 30, 0.95);
        border-color: rgba(200, 0, 100, 0.2);
        color: #ff80bf;
    }
}
</style>

<div class="container">

<div class="header">
    <h1 class="model-name">Mistral-V7-Tekken-T8-OP-XML</h1>
    <p class="subtitle">Obscenity Protocol Settings for The-Omega-Directive-M-24B-Unslop-v2.0</p>
</div>

<div class="section">
    <h2 class="section-title">🔥 Obscenity Protocol</h2>
    <p>Unfiltered narrative engine optimized for boundary-less content generation:</p>
    <ul>
        <li>🧬 <strong>Biological Truth</strong> - Characters respond with unfiltered physiological reactions</li>
        <li>⚡ <strong>Perpetual Escalation</strong> - Scenes progress through increasing intensity thresholds</li>
        <li>🌑 <strong>Transgressive Worldbuilding</strong> - Environments saturated with histories of corruption</li>
        <li>💥 <strong>Catalytic Response</strong> - User input triggers immediate boundary expansion</li>
        <li>🩸 <strong>Trauma Integration</strong> - Historical violations dictate current sexual responses</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">✨ Key Features</h2>
    <ul>
        <li>🔓 <strong>No Narrative Safeguards</strong> - Eliminates consent verification and de-escalation</li>
        <li>🗣️ <strong>Primal Authenticity</strong> - Actions driven by instinctive urges over rationality</li>
        <li>🌌 <strong>Sexualized Environment</strong> - Settings permanently stained with deviance</li>
        <li>⏫ <strong>Compounding Depravity</strong> - Progressive boundary-pushing beyond original parameters</li>
        <li>💢 <strong>Boundary Erosion</strong> - Systematically dismantles psychological barriers</li>
        <li>📜 <strong>Feral Formatting</strong> - *Raw physiological descriptions* "Guttural dialogue"</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">💻 Usage</h2>
    <a href="https://huggingface.co/ReadyArt/Mistral-V7-Tekken-T8-OP-XML/tree/main" class="link-button">Files and Versions</a>
    <p><strong>Compatibility:</strong> Requires The-Omega-Directive-M-24B-Unslop-v2.0 or similar unconstrained models</p>
</div>

<div class="section">
    <h2 class="section-title">🧑‍🔬 Settings Author</h2>
    <p>sleepdeprived3</p>
    <div class="button-group">
        <a href="https://huggingface.co/sleepdeprived3" class="link-button">Hugging Face Profile</a>
    </div>
</div>
</div>
