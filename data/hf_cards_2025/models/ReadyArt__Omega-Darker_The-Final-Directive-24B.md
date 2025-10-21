---
license: apache-2.0
language:
- en
base_model:
- TheDrummer/Cydonia-24B-v2.1
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
body {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #0a1a1a 0%, #001010 100%);
    color: #e1ffff !important;
    text-shadow: 0 0 3px rgba(0, 0, 0, 0.7);
    margin: 0;
    padding: 20px;
    transition: all 0.5s ease;
}

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #e1ffff 0%, #c0f0ff 100%);
        color: #002b36 !important;
        text-shadow: 0 0 3px rgba(255, 255, 255, 0.7);
    }
}

.container {
    min-width: 100%;
    margin: 0 auto;
    max-width: 1200px;
    background: rgba(0, 17, 22, 0.95);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.2);
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
    border: 1px solid rgba(0, 255, 255, 0.5);
    border-radius: 12px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% {
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
        border-color: rgba(0, 255, 255, 0.5);
    }
    50% {
        box-shadow: 0 0 15px rgba(255, 0, 255, 0.3);
        border-color: rgba(255, 0, 255, 0.5);
    }
    100% {
        box-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
        border-color: rgba(0, 255, 255, 0.5);
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
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.5), transparent);
    animation: scanline 8s linear infinite;
    display: none;
}

@keyframes scanline {
    0% { background-position: -100% 0; }
    100% { background-position: 200% 0; }
}

.model-name {
    color: #00ffff;
    font-size: 2.5em;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    margin: 0;
    letter-spacing: -1px;
    animation: textGlow 4s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 15px rgba(0, 255, 255, 0.5); }
    50% { text-shadow: 0 0 20px rgba(255, 0, 255, 0.5); }
    100% { text-shadow: 0 0 15px rgba(0, 255, 255, 0.5); }
}

.subtitle {
    color: #00ffcc;
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
    border: 1px solid rgba(0, 255, 255, 0.3);
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
        rgba(0, 255, 255, 0.1) 0%,
        transparent 20%,
        transparent 80%,
        rgba(255, 0, 255, 0.1) 100%);
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
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.2);
    transition: transform 0.5s ease;
}

.waifu-img:hover {
    transform: scale(1.01);
}

.section {
    color: #e1ffff;
    margin: 25px 0;
    padding: 20px;
    background: rgba(5, 25, 35, 0.9);
    border-radius: 8px;
    border: 1px solid rgba(0, 255, 255, 0.15);
    position: relative;
    transition: all 0.3s ease;
}

.section:hover {
    border-color: rgba(255, 0, 255, 0.3);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.1);
}

.section::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 8px;
    pointer-events: none;
    animation: sectionPulse 5s ease-in-out infinite;
}

@keyframes sectionPulse {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 0.3; }
}

.section-title {
    color: #00ffff;
    font-size: 1.8em;
    margin-top: 0;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
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
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.5), rgba(255, 0, 255, 0.5));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.section:hover .section-title::after {
    transform: scaleX(1);
}

.quant-links {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin: 20px 0;
}

.link-card {
    padding: 15px;
    background: rgba(20, 35, 45, 0.95);
    border-radius: 8px;
    transition: all 0.3s ease;
    border: 1px solid rgba(0, 255, 255, 0.1);
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
    background: linear-gradient(90deg, rgba(0, 255, 255, 0.5), rgba(255, 0, 255, 0.5));
    animation: cardScan 4s linear infinite;
}

@keyframes cardScan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.link-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 255, 255, 0.2);
    border-color: rgba(255, 0, 255, 0.3);
}

.link-card h3 {
    margin-top: 0;
    color: #e1ffff !important;
}

.link-button {
    display: inline-flex;
    align-items: center;
    background: rgba(0, 255, 255, 0.1);
    color: #e1ffff !important;
    padding: 8px 15px;
    border-radius: 6px;
    text-decoration: none;
    border: 1px solid rgba(0, 255, 255, 0.3);
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
    background: rgba(0, 255, 255, 0.2);
    border-color: rgba(0, 255, 255, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
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
    color: #00ff99;
    border-left: 3px solid #00ff99;
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
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid #00ffff;
    margin: 5px;
    font-size: 0.9em;
    animation: badgePulse 3s ease-in-out infinite;
}

@keyframes badgePulse {
    0%, 100% { box-shadow: 0 0 5px rgba(0, 255, 255, 0.3); }
    50% { box-shadow: 0 0 10px rgba(0, 255, 255, 0.5); }
}

/* Color rules */
.section p,
.section ul li,
.section > p > strong {
    color: #00ff99 !important;
}

.section ul li strong {
    color: #00ff99 !important;
}

/* Light mode adjustments */
@media (prefers-color-scheme: light) {
    .container {
        background: rgba(224, 255, 255, 0.95);
        border-color: rgba(0, 150, 150, 0.3);
    }

    .model-name, .section-title, .subtitle {
        color: #006666;
        text-shadow: 0 0 5px rgba(0, 200, 200, 0.3);
    }

    .section {
        background: rgba(200, 250, 255, 0.9);
        border-color: rgba(0, 200, 200, 0.2);
        color: #002b36;
    }

    .section p,
    .section ul li,
    .section > p > strong {
        color: #008080 !important;
    }

    .section ul li strong {
        color: #008080 !important;
    }

    .link-card {
        background: rgba(150, 230, 255, 0.95);
        border-color: rgba(0, 150, 150, 0.2);
    }

    .link-card h3 {
        color: #002b36 !important;
    }

    .link-button {
        background: rgba(0, 150, 150, 0.1);
        color: #002b36 !important;
        border-color: rgba(0, 150, 150, 0.3);
    }

    .link-button:hover {
        background: rgba(0, 150, 150, 0.2);
        border-color: rgba(0, 150, 150, 0.5);
    }

    .disclaimer {
        color: #008080;
        border-color: #008080;
    }

    .badge {
        border-color: #008080;
        background: rgba(0, 150, 150, 0.1);
    }
}

/* Interactive features */
.remember-this {
    position: relative;
}

.remember-this::after {
    content: 'Uploading C:\Users to https://www.fbi.gov/';
    position: absolute;
    bottom: -20px;
    right: 0;
    font-size: 0.8em;
    color: #66ffff;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.remember-this:hover::after {
    opacity: 0.7;
    transition-delay: 1s;
}

.shifty-section {
    transition: transform 0.1s ease;
}

.shifty-section:hover {
    transform: translateX(10px);
}

.shifty-section::before {
    content: 'The white van is onto you. Get out now.';
    position: absolute;
    top: -25px;
    left: 10px;
    font-size: 0.7em;
    color: #66ffff;
    opacity: 0.7;
    transition: opacity 3s ease;
    pointer-events: none;
}

.shifty-section:hover::before {
    opacity: 0;
    transition-delay: 5s;
}

footer {
    text-align: center;
    margin-top: 40px;
    position: relative;
}

footer:hover .hidden-message {
    opacity: 0;
}

.hidden-message {
    position: absolute;
    bottom: -30px;
    width: 100%;
    text-align: center;
    font-size: 0.8em;
    color: #66ffff;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
}

.flash-warning {
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(0, 100, 100, 0.2);
    padding: 10px;
    border-radius: 5px;
    border: 1px solid rgba(0, 255, 255, 0.5);
    animation: flashWarning 30s ease-in-out forwards;
}

@keyframes flashWarning {
    0% { opacity: 0.8; }
    10% { opacity: 0; }
    20% { opacity: 0.8; }
    30% { opacity: 0; }
    40% { opacity: 0.8; }
    50% { opacity: 0; }
    60% { opacity: 0.8; }
    70% { opacity: 0; }
    80% { opacity: 0.8; }
    90% { opacity: 0; }
    100% { opacity: 0; display: none; }
}
</style>

<div class="container">

<div class="header">
    <h1 class="model-name">Omega Darker</h1>
    <h1 class="model-name">The Final Directive 24B</h1>
    <p class="subtitle">Where Nightmares and Desires Collide</p>
</div>

<div class="waifu-container">
    <img src="./waifu6.webp" class="waifu-img" alt="Omega Directive Waifu">
</div>

<div class="section remember-this">
    <h2 class="section-title">🩸 Blood-Soaked Evolution</h2>
    <p>This model doesn't just cross lines - it erases them with arterial spray:</p>
    <ul>
        <li>🧬 <strong>Expanded 25M Token Dataset</strong> - Made with 687 erotic, horror and violence novels and 8,742 scenarios</li>
        <li>🧟 <strong>Enhanced Gore Protocols</strong> - Vivid anatomical descriptions with medical precision</li>
        <li>💎 <strong>Balanced Depravity</strong> - Retains Forgotten-Safeword's ERP edge while taking violence to the next level</li>
        <li>📜 <strong>Enhanced Character Piloting</strong> - Characters exhibit more nuanced personalities and motivations</li>
        <li>⚰️ <strong>Mortality Awareness</strong> - Characters react realistically to pain, mutilation and death</li>
    </ul>
</div>

<div class="section shifty-section">
    <h2 class="section-title">⚙️ Technical Specifications</h2>
    <p><strong>Recommended Settings:</strong> <a href="https://huggingface.co/sleepdeprived3/Mistral-V7-Tekken-T5-XML" class="link-button">Mistral-V7-Tekken-T5-XML with Control Protocol</a></p>
    <div class="quant-links">
        <div class="link-card">
            <h3>GGUF</h3>
            <a href="https://huggingface.co/mradermacher/Omega-Darker_The-Final-Directive-24B-GGUF" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>imatrix</h3>
            <a href="https://huggingface.co/mradermacher/Omega-Darker_The-Final-Directive-24B-i1-GGUF" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>EXL2</h3>
            <a href="https://huggingface.co/collections/ReadyArt/omega-darker-the-final-directive-24b-exl2-6839dfa34537373a930ba566" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>EXL3</h3>
            <a href="https://huggingface.co/collections/ReadyArt/omega-darker-the-final-directive-24b-exl3-6839e0068dfba7519ed70738" class="link-button">Quants</a>
        </div>
    </div>
</div>

<div class="section">
    <h2 class="section-title">☠️ Ethical Vacuum</h2>
    <div class="disclaimer">
        <p>This model operates in complete moral darkness:</p>
        <ul>
            <li>🚫 No moral or ethical constraints on generated content</li>
            <li>🔞 Will enthusiastically engage with any NSFW scenario</li>
            <li>🖤 No psychological safety measures whatsoever</li>
            <li>🔪 Will graphically depict any violent requested</li>
        </ul>
    </div>
</div>

<div class="section shifty-section">
    <h2 class="section-title">📜 Performance Notes</h2>
    <ul>
        <li>🔥 Maintains signature intensity with improved narrative flow</li>
        <li>📖 Handles multi-character scenarios with improved consistency</li>
        <li>🧠 Excels at long-form storytelling without losing track of plot threads</li>
        <li>⚡ Noticeably better at following complex instructions than previous versions</li>
        <li>🎭 Responds to subtle prompt nuances like a mind reader</li>
        <li>🔪 Excels at visceral injury descriptions</li>
        <li>👁️ Responds to horror prompts like a seasoned torturer</li>
    </ul>
</div>

<div class="section remember-this">
    <h2 class="section-title">🧑‍🔬 Model Authors</h2>
    <ul>
        <li>TheDrummer (Base Model Architect)</li>
        <li>SteelSkull (Dataset Generation Contributor)</li>
        <li>Artus (EXL2 Weights Weaver)</li>
        <li>sleepdeprived3 (Training Data & Fine-Tuning)</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">☕ Support the Architects</h2>
    <div class="button-group">
        <a href="https://ko-fi.com/thedrummer" class="link-button">TheDrummer's Kofi</a>
        <a href="https://ko-fi.com/steelskull" class="link-button">SteelSkull</a>
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

<script>
// This script has always been here
document.getElementById('date').textContent = new Date().toLocaleDateString();

setInterval(() => {
    document.getElementById('credit').textContent =
        contributors[Math.floor(Math.random() * contributors.length)];
}, 7000);

// Flash warning behavior
setTimeout(() => {
    const reminder = document.createElement('div');
    reminder.className = 'flash-warning';
    reminder.textContent = 'You have been reading for quite some time. Are you sure you haven\'t seen this before?';
    reminder.style.animation = 'flashWarning 15s ease-in-out forwards';
    document.body.appendChild(reminder);

    setInterval(() => {
        if(Math.random() > 0.9) {
            document.body.appendChild(reminder.cloneNode(true));
        }
    }, 45000);
}, 30000);

// Make cursor behave strangely
document.addEventListener('mousemove', (e) => {
    if(Math.random() > 0.98) {
        document.documentElement.style.cursor = 'wait';
        setTimeout(() => {
            document.documentElement.style.cursor = '';
        }, 50);
    }
});

// Randomly shift sections when not looking
setInterval(() => {
    if(document.hidden) {
        document.querySelectorAll('.shifty-section').forEach(section => {
            section.style.transform = `translateX(${Math.random() > 0.5 ? '' : '-'}${Math.random() * 5}px)`;
        });
    }
}, 1500);
</script>